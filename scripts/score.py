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
check-profile.py or check-component.py, is not a lower score but a failure.
The score itself, and so a successful run, never implies release eligibility;
see docs/EVIDENCE.md.

Writes score.json, and for each scope a standalone SVG badge and a Shields
endpoint file.

Usage:
    python scripts/score.py EVIDENCE_DIR --profile PROFILE --component COMPONENT \\
        --requirements FILE... [--requirement-pattern REGEX] [--out DIR] \\
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


def score(baseline: dict, results: list[dict], deviated: set[str], architectures: list[str]) -> dict[str, list[dict]]:
    """Rows per scope: each architecture, then generic."""
    required = {c: m for c, m in baseline["criteria"].items() if m["level"] == "required"}
    scopes: dict[str, list[dict]] = {}
    for scope in [*architectures, GENERIC]:
        rows = []
        for criterion, meta in required.items():
            per_architecture = meta.get("scope") == "architecture"
            if scope == GENERIC and per_architecture:
                continue
            checks = [r for r in results if r["criterion"] == criterion
                      and (not per_architecture or r["architecture"] == scope)]
            rows.append({"criterion": criterion, "title": meta["title"], "status": status(checks, criterion in deviated),
                         "checks": len(checks)})
        scopes[scope] = rows
    return scopes


def blockers(scopes: dict[str, list[dict]], active: list[dict]) -> list[str]:
    """What stands between a valid, passing image and a release."""
    found = []
    for scope, rows in scopes.items():
        for row in rows:
            if row["status"] in ("no evidence", "skipped", "failed"):
                found.append(row["criterion"] + " on " + scope + ": " + row["status"])
    for deviation in active:
        if deviation.get("kind") == "vulnerability":
            found.append(deviation.get("id", "?") + ": an active vulnerability deviation (" + str(deviation.get("target")) + ")")
        elif deviation.get("kind") == "criterion" and deviation.get("target") == VULNERABILITY_GATE:
            found.append(deviation.get("id", "?") + ": a deviation from the vulnerability gate, " + VULNERABILITY_GATE)
    return found


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


COLOURS = {"invalid": ("#6e7781", "lightgrey"), "failing": ("#cf222e", "red"),
           "eligible": ("#2da44e", "green"), "not eligible": ("#bf8700", "yellow")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("evidence", type=Path)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--component", type=Path, required=True)
    parser.add_argument("--requirements", type=Path, nargs="+", required=True)
    parser.add_argument("--requirement-pattern", default=None)
    parser.add_argument("--out", type=Path, default=Path("score"))
    parser.add_argument("--today", type=datetime.date.fromisoformat, default=datetime.date.today())
    parser.add_argument("--standard-ref", help="the commit the caller names; required with --workflow-sha")
    parser.add_argument("--workflow-sha", help="the commit the conformance workflow ran from (job.workflow_sha)")
    args = parser.parse_args()

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    profiles, components, revisions = load("check-profile"), load("check-component"), load("check-revision")
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    head = revisions.git(REPOSITORY, "rev-parse", "HEAD").stdout.strip() or "unknown"

    revision_errors = revisions.check(REPOSITORY, (profile.get("standard") or {}).get("revision"),
                                      args.standard_ref, args.workflow_sha)
    profile_violations, _ = profiles.check(profile, json.loads(REGISTER.read_text(encoding="utf-8")), baseline, args.today)
    active = profiles.active_deviations(profile, args.today)
    stated = components.stated_requirements(args.requirements, args.requirement_pattern or components.DEFAULT_PATTERN)
    component_violations, _ = components.check(
        json.loads(args.component.read_text(encoding="utf-8")), baseline, stated, False, active, components.rendered_rules()
    )
    if not stated:
        component_violations.append("no requirement identifiers found; check the requirement pattern")

    evidence = evidence_module.load(args.evidence, profile, baseline)
    # The exception register is judged here, from the profile itself, rather
    # than taken from the image's word for it (IMG-26).
    results = evidence.results + [{
        "id": "conformance.exceptions", "criterion": "IMG-26", "architecture": GENERIC, "file": "(conformance)",
        "check": "every exception is a recorded deviation, none expired or over its limit",
        "passed": not profile_violations,
    }]
    architectures = [a for a in profile.get("architectures", []) if a in evidence_module.ARCHITECTURES] \
        if isinstance(profile.get("architectures"), list) else []
    deviated = {d["target"] for d in active if d.get("kind") == "criterion"}
    scopes = score(baseline, results, deviated, architectures) if evidence.valid else {}

    failed_rows = [s + " " + r["criterion"] for s, rows in scopes.items() for r in rows if r["status"] == "failed"]
    failing = bool(revision_errors or profile_violations or component_violations or failed_rows)
    stopping = [] if evidence.valid else ["the evidence is invalid"]
    release_blockers = stopping + (["the checks fail"] if failing else []) + blockers(scopes, active)
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
        "source_commit": evidence.source_commit, "state": state,
        "evidence_valid": evidence.valid, "failing": failing, "release_eligible": eligible,
        "coverage": {"evidenced": evidenced, "required": total},
        "release_blockers": release_blockers, "evidence_errors": evidence.errors,
        "revision_errors": revision_errors, "profile_violations": profile_violations,
        "component_violations": component_violations, "scopes": summary,
    }, indent=2) + "\n", encoding="utf-8")

    colour, named = COLOURS[state]
    for scope in [*architectures, GENERIC]:
        label = "hardening " + scope
        if state == "invalid":
            message = "evidence invalid"
        elif state == "failing":
            message = "failing"
        else:
            message = str(summary[scope]["met"]) + "/" + str(summary[scope]["required"])
        # Scoped to one architecture, and dated, so a badge never reads as
        # more, or more current, than it is.
        message += " · " + head[:7] + " · " + args.today.isoformat()
        (args.out / ("badge-" + scope + ".svg")).write_text(badge(label, message, colour), encoding="utf-8")
        (args.out / ("shields-" + scope + ".json")).write_text(json.dumps({
            "schemaVersion": 1, "label": label, "message": message, "color": named,
        }) + "\n", encoding="utf-8")

    for error in evidence.errors:
        print("  evidence: " + error)
    for problem in revision_errors:
        print("  revision: " + problem)
    for violation in profile_violations + component_violations:
        print("  violation: " + violation)
    for scope, rows in scopes.items():
        for row in rows:
            if row["status"] != "met":
                print(f"  {scope:8} {row['criterion']:7} {row['status']:12} {row['title']}")
    for scope in scopes:
        print(f"hardening {scope}: {summary[scope]['met']}/{summary[scope]['required']}")
    print("evidence " + ("valid" if evidence.valid else "invalid") + "; coverage " + str(evidenced) + "/" + str(total)
          + "; " + ("failing" if failing else "passing") + "; release " + ("eligible" if eligible else "not eligible"))
    for blocker in release_blockers:
        print("  release blocker: " + blocker)
    return 1 if state in ("invalid", "failing") else 0


if __name__ == "__main__":
    raise SystemExit(main())
