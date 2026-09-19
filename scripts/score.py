#!/usr/bin/env python3
"""Score an image's conformance to the standard, from its evidence.

It answers three questions separately, because they are different claims:

- **Is the evidence valid?** Read strictly by evidence.py, against what the
  hardening profile says to expect. Invalid evidence is not scored.
- **What is the score?** For each architecture the image is built for, the
  required criteria met, out of those required. A per-architecture criterion
  is met only by evidence from that architecture; a generic one by evidence
  from anywhere. A generic score covers the generic criteria alone. A
  criterion is met only when at least one check names it, every check that
  names it passed, none was merely skipped, and the profile records no active
  deviation from it. A deviation is visible and temporary, and is not a pass.
- **Is the image release eligible?** Only when the evidence is valid, nothing
  fails, and every required criterion on every architecture is met or covered
  by an active deviation that is not about a vulnerability. A deviation from
  the vulnerability gate, or an active vulnerability deviation, blocks a
  release whatever the score.

A revision that does not bind (check-revision.py), or a violation from
check-profile.py, check-component.py, or the decisions worksheet, is not a
lower score but a failure. A decision not yet reviewed blocks a release.

With --draft, it is a draft assessment for an image still researching the
standard: the profile may be incomplete, the component definition and
requirements absent, and the revision may be any; each gap is reported as
something to do, a moved standard as drift, and nothing is claimed or failed.
The score itself, and so a successful run, never implies release eligibility;
see docs/EVIDENCE.md.

Writes score.json, and for each scope a standalone SVG badge and a Shields
endpoint file.

Usage:
    python scripts/score.py EVIDENCE_DIR --profile PROFILE --component COMPONENT \\
        --requirements FILE... [--requirement-pattern REGEX] [--crosswalk FILE] [--out DIR] \\
        [--standard-ref SHA --workflow-sha SHA]
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import sys
from pathlib import Path
from xml.sax.saxutils import escape

REPOSITORY = Path(__file__).resolve().parent.parent
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
REGISTER = REPOSITORY / "artifacts" / "sources.json"
# The criterion a vulnerability deviation stands in for.
VULNERABILITY_GATE = "IMG-25"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), REPOSITORY / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


evidence_module = load("evidence")
GENERIC = evidence_module.GENERIC


def status(checks: list[dict], deviated: bool) -> str:
    if deviated:
        return "deviated"
    if not checks:
        return "no evidence"
    if any(c["passed"] is False for c in checks):
        return "failed"
    if any(c["passed"] is None for c in checks):
        return "skipped"
    return "met"


ORDER = ["failed", "no evidence", "partial", "skipped", "met"]


def combinations(qualifiers: dict[str, list[str]] | None) -> list[dict[str, str]]:
    """Every combination of the declared roles and topologies; one empty one if none."""
    combos: list[dict[str, str]] = [{}]
    for name, values in (qualifiers or {}).items():
        if values:
            combos = [c | {name: v} for c in combos for v in values]
    return combos


def score(baseline: dict, results: list[dict], deviated: set[str], architectures: list[str],
          roles: list[str] | None = None, mapping: dict[str, list[str]] | None = None,
          topologies: list[str] | None = None) -> dict[str, list[dict]]:
    """Rows per scope: each architecture, then generic.

    A per-architecture criterion is met on an architecture only if it is met in
    every declared role and topology; the worst combination's status is the
    criterion's. With a crosswalk, a criterion is met only when every
    requirement it maps to has a passing check of its own, in each of those
    combinations: a broad link, or one passing suite, does not close it. Short
    of that, it is "partial".
    """
    required = {c: m for c, m in baseline["criteria"].items() if m["level"] == "required"}
    combos = combinations({"role": roles or [], "topology": topologies or []})
    # A deviation scoped to some architectures excuses the criterion on those alone.
    if not isinstance(deviated, dict):
        deviated = {c: None for c in deviated}
    scopes: dict[str, list[dict]] = {}
    for scope in [*architectures, GENERIC]:
        rows = []
        for criterion, meta in required.items():
            per_architecture = meta.get("scope") == "architecture"
            if scope == GENERIC and per_architecture:
                continue
            checks = [r for r in results if r["criterion"] == criterion
                      and (not per_architecture or r["architecture"] == scope)]
            if criterion in deviated and (deviated[criterion] is None or scope in deviated[criterion]):
                found, uncovered = "deviated", []
            else:
                statuses, uncovered = [], set()
                for combo in (combos if per_architecture else [{}]):
                    subset = [c for c in checks if all(c.get(k) == v for k, v in combo.items())]
                    found = status(subset, False)
                    wanted = (mapping or {}).get(criterion) or []
                    if mapping is not None and found == "met":
                        passing = {r for c in subset if c["passed"] is True for r in c.get("requirements", [])}
                        missing = [r for r in wanted if r not in passing]
                        if missing:
                            found = "partial"
                            uncovered.update(missing)
                    statuses.append(found)
                found = min(statuses, key=ORDER.index)
                uncovered = sorted(uncovered)
            row = {"criterion": criterion, "title": meta["title"], "status": found, "checks": len(checks)}
            if uncovered:
                row["requirements_without_evidence"] = uncovered
            rows.append(row)
        scopes[scope] = rows
    return scopes


def blockers(scopes: dict[str, list[dict]], active: list[dict]) -> list[str]:
    """What stands between a valid, passing image and a release."""
    found = []
    for scope, rows in scopes.items():
        for row in rows:
            if row["status"] in ("no evidence", "skipped", "failed", "partial"):
                found.append(row["criterion"] + " on " + scope + ": " + row["status"])
    for deviation in active:
        if deviation.get("kind") == "vulnerability":
            found.append(deviation.get("id", "?") + ": an active vulnerability deviation (" + str(deviation.get("target")) + ")")
        elif deviation.get("kind") == "criterion" and deviation.get("target") == VULNERABILITY_GATE:
            found.append(deviation.get("id", "?") + ": a deviation from the vulnerability gate, " + VULNERABILITY_GATE)
    return found


def scope_errors(evidence, mapping: dict | None, candidates: list[str]) -> list[str]:
    """What binds a result to a requirement and an image: it must name only
    requirements its criterion maps to, and be about the candidate digest."""
    errors = []
    criteria = (mapping or {}).get("criteria") if isinstance(mapping, dict) else None
    for result in evidence.results:
        for requirement in result.get("requirements", []):
            if criteria is not None and requirement not in (criteria.get(result["criterion"]) or []):
                errors.append(result["file"] + " " + result["id"] + ": names " + requirement + ", which the crosswalk does not map "
                              + result["criterion"] + " to")
    wanted = dict(c.split("=", 1) for c in candidates if "=" in c)
    for where, subject in evidence.subjects.items():
        architecture = subject.get("architecture")
        if architecture in wanted and subject.get("digest") != wanted[architecture]:
            errors.append(where + ": is about " + str(subject.get("digest") or subject.get("image_id")) + ", not the "
                          + architecture + " candidate " + wanted[architecture])
    return errors


def badge(label: str, message: str, colour: str) -> str:
    """A flat badge, sized from the text, needing no external service."""
    width = lambda text: 7 * len(text) + 12
    left, right = width(label), width(message)
    total = left + right
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img" aria-label="{escape(label)}: {escape(message)}">'
        f"<title>{escape(label)}: {escape(message)}</title>"
        f'<rect width="{left}" height="20" fill="#555"/><rect x="{left}" width="{right}" height="20" fill="{colour}"/>'
        '<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">'
        f'<text x="{left / 2}" y="14">{escape(label)}</text><text x="{left + right / 2}" y="14">{escape(message)}</text></g></svg>\n'
    )


COLOURS = {"invalid": ("#6e7781", "lightgrey"), "failing": ("#cf222e", "red"), "draft": ("#0969da", "blue"),
           "eligible": ("#2da44e", "green"), "not eligible": ("#bf8700", "yellow")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("evidence", type=Path)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--component", type=Path)
    parser.add_argument("--requirements", type=Path, nargs="*", default=[])
    parser.add_argument("--requirement-pattern", default=None)
    parser.add_argument("--crosswalk", type=Path, help="the image's map from each criterion to its requirement identifiers")
    parser.add_argument("--decisions", type=Path, help="the image's decisions worksheet for the controls left to it")
    parser.add_argument("--candidate", action="append", default=[], metavar="ARCH=DIGEST",
                        help="the digest to be released for an architecture; that architecture's evidence must be about it")
    parser.add_argument("--draft", action="store_true",
                        help="a draft assessment: report what adopting would need, claim nothing, and never fail")
    parser.add_argument("--out", type=Path, default=Path("score"))
    parser.add_argument("--today", type=datetime.date.fromisoformat, default=datetime.date.today())
    parser.add_argument("--standard-ref", help="the commit the caller names; required with --workflow-sha")
    parser.add_argument("--workflow-sha", help="the commit the conformance workflow ran from (job.workflow_sha)")
    args = parser.parse_args()
    if not args.draft and (args.component is None or not args.requirements):
        parser.error("an audit needs --component and --requirements; a draft may omit them")

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    profiles, components, revisions = load("check-profile"), load("check-component"), load("check-revision")
    sheets = load("worksheets")
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    head = revisions.git(REPOSITORY, "rev-parse", "HEAD").stdout.strip() or "unknown"

    # In a draft, a revision that does not bind is drift to report, not a failure.
    revision_errors = revisions.check(REPOSITORY, (profile.get("standard") or {}).get("revision"),
                                      None if args.draft else args.standard_ref,
                                      None if args.draft else args.workflow_sha)
    profile_violations, _ = profiles.check(profile, json.loads(REGISTER.read_text(encoding="utf-8")), baseline, args.today,
                                           args.profile.resolve().parent)
    active = profiles.active_deviations(profile, args.today)

    component_violations: list[str] = []
    stated = components.stated_requirements(args.requirements, args.requirement_pattern or components.DEFAULT_PATTERN) \
        if args.requirements else set()
    mapping = json.loads(args.crosswalk.read_text(encoding="utf-8")) if args.crosswalk else None
    component = json.loads(args.component.read_text(encoding="utf-8")) if args.component and args.component.exists() else None
    if component is not None:
        component_violations, _ = components.check(component, baseline, stated, args.draft, active,
                                                   components.rendered_rules(), mapping)
    else:
        component_violations.append("no component definition yet")
    if mapping is not None:
        component_violations = components.check_crosswalk(mapping, baseline, stated or None, active) + component_violations
    if not stated:
        component_violations.append("no requirement identifiers found; check the requirement pattern")

    unreviewed: list[str] = []
    if args.decisions:
        decision_errors, unreviewed = sheets.check_decisions(json.loads(args.decisions.read_text(encoding="utf-8")), component)
        component_violations += ["decisions: " + e for e in decision_errors]

    evidence = evidence_module.load(args.evidence, profile, baseline, draft=args.draft)
    if evidence.valid:
        evidence.errors.extend(scope_errors(evidence, mapping, args.candidate))
    # The exception register is judged here, from the profile itself, rather
    # than taken from the image's word for it (IMG-26).
    results = evidence.results + [{
        "id": "conformance.exceptions", "criterion": "IMG-26", "architecture": GENERIC, "file": "(conformance)",
        "check": "every exception is a recorded deviation, none expired or over its limit",
        "passed": not profile_violations,
        # It judges the whole register, so it verifies whatever the image
        # states IMG-26 as.
        "requirements": list(((mapping or {}).get("criteria") or {}).get("IMG-26") or []),
    }]
    architectures = evidence.architectures
    deviated = {d["target"]: (set(d["architectures"]) if d.get("architectures") else None)
                for d in active if d.get("kind") == "criterion"}
    roles = profile.get("roles") if isinstance(profile.get("roles"), list) else None
    topologies = profile.get("topologies") if isinstance(profile.get("topologies"), list) else None
    criteria_map = mapping.get("criteria") if isinstance(mapping, dict) and isinstance(mapping.get("criteria"), dict) else None
    scopes = score(baseline, results, deviated, architectures, roles, criteria_map, topologies) if evidence.valid else {}

    failed_rows = [s + " " + r["criterion"] for s, rows in scopes.items() for r in rows if r["status"] == "failed"]
    failing = bool(revision_errors or profile_violations or component_violations or failed_rows)
    stopping = [] if evidence.valid else ["the evidence is invalid"]
    release_blockers = stopping + (["the checks fail"] if failing else []) + blockers(scopes, active)
    if unreviewed:
        release_blockers.append(str(len(unreviewed)) + " decisions not yet reviewed: " + ", ".join(unreviewed[:6])
                                + (" and more" if len(unreviewed) > 6 else ""))
    if args.draft:
        # A draft claims nothing: not conformance, not eligibility, not failure.
        release_blockers.insert(0, "a draft assessment is not an audit")
        failing, eligible, state = False, False, "draft"
    else:
        eligible = evidence.valid and not failing and not release_blockers
        state = "invalid" if not evidence.valid else "failing" if failing else "eligible" if eligible else "not eligible"

    per_architecture = {s: rows for s, rows in scopes.items() if s != GENERIC}
    evidenced = sum(r["status"] != "no evidence" for rows in per_architecture.values() for r in rows)
    total = sum(len(rows) for rows in per_architecture.values())
    summary = {
        s: {"met": sum(r["status"] == "met" for r in rows), "required": len(rows),
            "evidenced": sum(r["status"] != "no evidence" for r in rows), "criteria": rows}
        for s, rows in scopes.items()
    }

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "score.json").write_text(json.dumps({
        "schema_version": 2, "standard_revision": head, "scored_on": args.today.isoformat(),
        "mode": "draft" if args.draft else "audit",
        "source_commit": evidence.source_commit, "state": state,
        "evidence_valid": evidence.valid, "failing": failing, "release_eligible": eligible,
        "coverage": {"evidenced": evidenced, "required": total},
        "release_blockers": release_blockers, "evidence_errors": evidence.errors,
        "revision_errors" if not args.draft else "drift": revision_errors,
        "profile_violations": profile_violations, "component_violations": component_violations,
        "unreviewed_decisions": unreviewed, "scopes": summary,
    }, indent=2) + "\n", encoding="utf-8")

    colour, named = COLOURS[state]
    for scope in [*architectures, GENERIC]:
        label = "hardening " + scope
        if state == "invalid":
            message = "evidence invalid"
        elif state == "failing":
            message = "failing"
        else:
            message = ("draft " if args.draft else "") + str(summary[scope]["met"]) + "/" + str(summary[scope]["required"])
        # Scoped to one architecture, and dated, so a badge never reads as
        # more, or more current, than it is.
        message += " · " + head[:7] + " · " + args.today.isoformat()
        (args.out / ("badge-" + scope + ".svg")).write_text(badge(label, message, colour), encoding="utf-8")
        (args.out / ("shields-" + scope + ".json")).write_text(json.dumps({
            "schemaVersion": 1, "label": label, "message": message, "color": named,
        }) + "\n", encoding="utf-8")

    prefix = "to do" if args.draft else "violation"
    for error in evidence.errors:
        print("  evidence: " + error)
    for problem in revision_errors:
        print(("  drift: " if args.draft else "  revision: ") + problem)
    for violation in profile_violations + component_violations:
        print("  " + prefix + ": " + violation)
    for scope, rows in scopes.items():
        for row in rows:
            if row["status"] != "met":
                print(f"  {scope:8} {row['criterion']:7} {row['status']:12} {row['title']}")
    for scope in scopes:
        print(f"hardening {scope}: {'draft ' if args.draft else ''}{summary[scope]['met']}/{summary[scope]['required']}")
    if args.draft:
        print("draft assessment against " + head[:12] + "; evidence " + ("valid" if evidence.valid else "invalid")
              + "; coverage " + str(evidenced) + "/" + str(total) + "; no conformance is claimed")
        return 0
    print("evidence " + ("valid" if evidence.valid else "invalid") + "; coverage " + str(evidenced) + "/" + str(total)
          + "; " + ("failing" if failing else "passing") + "; release " + ("eligible" if eligible else "not eligible"))
    for blocker in release_blockers:
        print("  release blocker: " + blocker)
    return 1 if state in ("invalid", "failing") else 0


if __name__ == "__main__":
    raise SystemExit(main())
