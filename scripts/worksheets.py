#!/usr/bin/env python3
"""Generate and check the two worksheets an adopting image fills in.

**Applicability**, one per conditional source: every rule of the pinned SRG,
decided one by one. A decision is one of:

- ``applies``: the image has what the rule governs, and must meet it
- ``not-applicable``: the image has nothing the rule governs; say what is absent
- ``other-layer``: the rule governs the platform or host, not the image
- ``covered-by``: another source's rule states the same requirement in terms
  that fit the image better; name it, as ``<source>:<Group ID>``

Each rule is generated with the rules in the image's other sources that share a
CCI with it, as suggestions for ``covered-by``, which is how an image weighs two
SRGs that both reach it, such as an HTTP API that is not a web server. The
source's determination in the hardening profile follows from the worksheet: it
applies if any rule applies.

**Decisions**: every control the control baseline leaves ``research-required``,
decided for this image with an origination, a rationale, a statement of how the
control is satisfied in terms of what the image does, an owner, and a review.
Access-control and identification controls carry a warning, because a "no
accounts" answer copied from the reference image is wrong for any image that
takes part in identity: one that verifies a token or session, holds a client
secret, or decides authorization from claims, as much as one that stores
accounts or API keys.

Both are checked against the pinned sources and baseline. Undecided rows,
unknown rules, and missing fields are errors; decisions not yet reviewed are
reported separately, because they block a release but not an audit.

Usage:
    python worksheets.py applicability new --source disa-web-server-srg --out applicability/web-server-srg.json
    python worksheets.py applicability check applicability/web-server-srg.json
    python worksheets.py decisions new --out decisions.json
    python worksheets.py decisions check decisions.json [--component oscal/component-definition.json]
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REGISTER = REPOSITORY / "artifacts" / "sources.json"
CROSSWALK = REPOSITORY / "artifacts" / "crosswalk.json"
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
APPLICABILITY = "container-hardening/applicability-worksheet"
DECISIONS = "container-hardening/decisions-worksheet"
RULE_DECISIONS = ("applies", "not-applicable", "other-layer", "covered-by")
REFERENCE = re.compile(r"^[a-z0-9][a-z0-9-]*:V-\d+$")
ACCOUNTS = ("ac-", "ia-")
ACCOUNTS_WARNING = (
    "Does this image take part in identity at all? It does if it stores accounts or keys; if it verifies a "
    "credential itself, such as a JWT signature, a session cookie, a client certificate, or basic authentication; "
    "if it holds a secret to do so, such as an OIDC client secret or a pinned JWKS; or if it decides authorization "
    "from claims. Any of those makes this image-owned, at least in part. If an identity provider or a proxy does it "
    "instead, the control is inherited from them, not not-applicable: not-applicable means there is nothing for the "
    "control to apply to, which is true only where the image never sees an identity."
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def catalogues() -> dict[str, dict]:
    return {c["source"]: c for c in load(CROSSWALK)["catalogues"]}


def title(slug: str, group_id: str) -> str:
    page = REPOSITORY / "docs" / "srg" / slug / "rules" / (group_id + ".md")
    match = re.search(r"^\*\*(.+)\*\*$", page.read_text(encoding="utf-8"), re.M) if page.exists() else None
    return match.group(1) if match else ""


# Applicability ---------------------------------------------------------------

def new_applicability(source: str, image: str, also: list[str]) -> dict:
    sources = {s["id"]: s for s in load(REGISTER)["sources"]}
    rendered = catalogues()
    if source not in rendered:
        raise SystemExit(source + " is not a rendered catalogue; one of " + ", ".join(sorted(rendered)))
    if sources[source]["role"] != "conditional":
        raise SystemExit(source + " is not conditional; every image takes it")
    others = [s for s in (also or [c for c in rendered if c != source]) if s != source]
    by_cci: dict[str, list[str]] = {}
    for other in others:
        for rule in rendered[other]["rules"]:
            for cci in rule["ccis"]:
                by_cci.setdefault(cci["cci"], []).append(other + ":" + rule["group_id"])
    catalogue = rendered[source]
    rules = []
    for rule in sorted(catalogue["rules"], key=lambda r: r["group_id"]):
        shared = sorted({r for cci in rule["ccis"] for r in by_cci.get(cci["cci"], [])})
        rules.append({
            "group_id": rule["group_id"], "stig_id": rule["stig_id"], "severity": rule["severity"],
            "title": title(catalogue["slug"], rule["group_id"]), "shares_cci_with": shared,
            "decision": None, "basis": "", "covered_by": [],
        })
    return {
        "schema": APPLICABILITY, "schema_version": 1, "image": image,
        "source": source, "release": sources[source]["release"], "sha256": sources[source]["sha256"],
        "status": "draft", "rules": rules,
    }


def check_applicability(sheet: dict) -> tuple[list[str], dict[str, int]]:
    """Return (errors, counts by decision)."""
    if sheet.get("schema") != APPLICABILITY or sheet.get("schema_version") != 1:
        return ["schema must be " + APPLICABILITY + ", schema_version 1"], {}
    sources = {s["id"]: s for s in load(REGISTER)["sources"]}
    rendered = catalogues()
    source = sheet.get("source")
    if source not in rendered:
        return [repr(source) + " is not a rendered catalogue"], {}
    errors: list[str] = []
    if sheet.get("sha256") != sources[source]["sha256"]:
        errors.append("made against " + str(sheet.get("sha256"))[:12] + ", but the register pins "
                      + sources[source]["sha256"][:12] + "; regenerate it and decide the rules again")
    expected = {r["group_id"] for r in rendered[source]["rules"]}
    seen: set[str] = set()
    counts = {d: 0 for d in (*RULE_DECISIONS, "undecided")}
    for row in sheet.get("rules", []):
        group = row.get("group_id")
        if group not in expected:
            errors.append(str(group) + ": not a rule of " + source)
            continue
        if group in seen:
            errors.append(group + ": listed more than once")
        seen.add(group)
        decision = row.get("decision")
        if decision is None:
            counts["undecided"] += 1
            errors.append(group + ": undecided")
            continue
        if decision not in RULE_DECISIONS:
            errors.append(group + ": decision must be one of " + ", ".join(RULE_DECISIONS))
            continue
        counts[decision] += 1
        if decision != "applies" and not str(row.get("basis", "")).strip():
            errors.append(group + ": " + decision + " needs a basis")
        if decision == "covered-by":
            covered = row.get("covered_by") or []
            if not covered or not all(isinstance(c, str) and REFERENCE.match(c) for c in covered):
                errors.append(group + ": covered-by names the rule that covers it, as <source>:<Group ID>")
            for reference in covered:
                other, _, rule = reference.partition(":")
                if other in rendered and rule not in {r["group_id"] for r in rendered[other]["rules"]}:
                    errors.append(group + ": " + reference + " is not a rule of " + other)
    for missing in sorted(expected - seen):
        errors.append(missing + ": missing from the worksheet")
    return errors, counts


def applies(counts: dict[str, int]) -> bool:
    return counts.get("applies", 0) > 0


# Decisions -------------------------------------------------------------------

def new_decisions(image: str) -> dict:
    baseline = load(BASELINE)
    rows = []
    for control in baseline["controls"]:
        if control["origination"] != "research-required":
            continue
        row = {"control": control["id"], "label": control["label"], "title": control["title"],
               "origination": None, "rationale": "", "statement": "", "owner": "",
               "reviewed_by": None, "reviewed_on": None}
        if control["id"].startswith(ACCOUNTS):
            row["warning"] = ACCOUNTS_WARNING
        rows.append(row)
    return {"schema": DECISIONS, "schema_version": 1, "image": image, "decisions": rows}


def check_decisions(sheet: dict, component: dict | None = None) -> tuple[list[str], list[str]]:
    """Return (errors, unreviewed). Unreviewed decisions block a release, not an audit."""
    if sheet.get("schema") != DECISIONS or sheet.get("schema_version") != 1:
        return ["schema must be " + DECISIONS + ", schema_version 1"], []
    baseline = load(BASELINE)
    namespace = baseline["model"]["namespace"]
    originations = set(baseline["model"]["originations"]) - {"research-required"}
    undecided = {c["id"] for c in baseline["controls"] if c["origination"] == "research-required"}
    errors: list[str] = []
    unreviewed: list[str] = []
    seen: set[str] = set()
    for row in sheet.get("decisions", []):
        control = row.get("control")
        if control not in undecided:
            errors.append(str(control) + ": not a control the baseline leaves to the image")
            continue
        if control in seen:
            errors.append(control + ": decided more than once")
        seen.add(control)
        if row.get("origination") not in originations and row.get("origination") != "research-required":
            errors.append(control + ": origination must be one of " + ", ".join(sorted(originations))
                          + ", or research-required with a reason it stays open")
        for field in ("rationale", "statement", "owner"):
            if not str(row.get(field) or "").strip():
                errors.append(control + ": " + field + " is required")
        if not row.get("reviewed_by") or not row.get("reviewed_on"):
            unreviewed.append(control)
        else:
            try:
                if datetime.date.fromisoformat(row["reviewed_on"]) > datetime.date.today():
                    errors.append(control + ": reviewed_on is in the future")
            except (TypeError, ValueError):
                errors.append(control + ": reviewed_on is not an ISO date")
    for missing in sorted(undecided - seen):
        errors.append(missing + ": not decided")
    if component is not None:
        stated = {}
        for comp in component["component-definition"].get("components", []):
            for implementation in comp.get("control-implementations", []):
                for entry in implementation.get("implemented-requirements", []):
                    origin = [p["value"] for p in entry.get("props", []) if p.get("name") == "origination" and p.get("ns") == namespace]
                    stated[entry.get("control-id")] = origin[0] if origin else None
        for row in sheet.get("decisions", []):
            control = row.get("control")
            if control in stated and stated[control] != row.get("origination"):
                errors.append(control + ": the worksheet decides " + str(row.get("origination"))
                              + ", but the component definition says " + str(stated[control]))
    return errors, unreviewed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kind", choices=("applicability", "decisions"))
    parser.add_argument("action", choices=("new", "check"))
    parser.add_argument("sheet", nargs="?", type=Path, help="the worksheet to check")
    parser.add_argument("--source", help="for a new applicability worksheet: the conditional source")
    parser.add_argument("--also", nargs="*", default=[], help="the other sources to suggest covered-by rules from")
    parser.add_argument("--image", default="", help="the image the worksheet is for")
    parser.add_argument("--component", type=Path, help="for decisions: the component definition to compare")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    if args.action == "new":
        if not args.out:
            parser.error("new needs --out")
        if args.out.exists():
            parser.error(str(args.out) + " exists; a worksheet is never overwritten")
        if args.kind == "applicability":
            if not args.source:
                parser.error("a new applicability worksheet needs --source")
            sheet = new_applicability(args.source, args.image, args.also)
        else:
            sheet = new_decisions(args.image)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(sheet, indent=2) + "\n", encoding="utf-8", newline="\n")
        print("wrote " + str(args.out))
        return 0

    if not args.sheet:
        parser.error("check needs the worksheet")
    sheet = load(args.sheet)
    if args.kind == "applicability":
        errors, counts = check_applicability(sheet)
        for error in errors:
            print("error: " + error)
        print(", ".join(k + " " + str(v) for k, v in counts.items()) + "; the source "
              + ("applies" if applies(counts) else "does not apply") + ("" if not errors else "; incomplete"))
        return 1 if errors else 0
    errors, unreviewed = check_decisions(sheet, load(args.component) if args.component else None)
    for error in errors:
        print("error: " + error)
    if unreviewed:
        print(str(len(unreviewed)) + " decisions not yet reviewed, which blocks a release: " + ", ".join(unreviewed[:8])
              + (" and more" if len(unreviewed) > 8 else ""))
    print(str(len(sheet.get("decisions", []))) + " decisions; " + str(len(errors)) + " errors")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
