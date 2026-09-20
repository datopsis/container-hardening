#!/usr/bin/env python3
"""Write an image's control statements: how every control is satisfied, in one page.

The component definition says what each control's origination is, and cites the
criteria and requirements behind an image-owned claim. This renders that as
prose a reader can follow without reading OSCAL: for each of the baseline's
controls, what satisfies it, and who satisfies it.

- **image-owned**: the criteria the claim rests on, the image's own requirements
  that state them, and where it stops, which is the platform's part.
- **deployment-configured**, **host-inherited**, **organization-inherited**: what
  the image contributes, if anything, and who does the rest.
- **not-applicable**: what is absent, so there is nothing to satisfy.
- Controls the baseline leaves to the image carry that image's own statement
  from its decisions worksheet, which is where the reasoning is reviewed.

Generated, never hand-edited: it follows the baseline, the component
definition, and the decisions worksheet.

Usage:
    python build-statements.py --component oscal/component-definition.json \\
        --decisions decisions.json --crosswalk requirements-crosswalk.json \\
        --image "reference-web-server" --out CONTROL-STATEMENTS.md [--check]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
FAMILIES = {
    "ac": "Access Control", "at": "Awareness and Training", "au": "Audit and Accountability",
    "ca": "Assessment, Authorization, and Monitoring", "cm": "Configuration Management",
    "cp": "Contingency Planning", "ia": "Identification and Authentication", "ir": "Incident Response",
    "ma": "Maintenance", "mp": "Media Protection", "pe": "Physical and Environmental Protection",
    "pl": "Planning", "pm": "Program Management", "ps": "Personnel Security", "pt": "PII Processing",
    "ra": "Risk Assessment", "sa": "System and Services Acquisition", "sc": "System and Communications Protection",
    "si": "System and Information Integrity", "sr": "Supply Chain Risk Management",
}
WHO = {
    "image-owned": "This image", "deployment-configured": "The deployment", "host-inherited": "The host or platform",
    "organization-inherited": "The organization", "not-applicable": "Nobody: nothing here to apply it to",
    "research-required": "Undecided",
}


def implemented(component: dict) -> dict[str, dict]:
    found = {}
    for comp in component["component-definition"].get("components", []):
        for implementation in comp.get("control-implementations", []):
            for entry in implementation.get("implemented-requirements", []):
                found[entry.get("control-id")] = entry
    return found


def props(entry: dict, name: str) -> list[str]:
    return [p.get("value", "") for p in entry.get("props", []) if p.get("name") == name]


def statement(control: dict, entry: dict, decided: dict, criteria: dict, mapping: dict) -> str:
    """How this control is satisfied, in one paragraph."""
    if control["id"] in decided:
        return decided[control["id"]]
    origination = props(entry, "origination")[0] if entry and props(entry, "origination") else control["origination"]
    cited = props(entry, "criterion") if entry else control["criteria"]
    parts = []
    if origination == "image-owned":
        titles = "; ".join(c + " " + criteria[c]["title"] for c in cited if c in criteria)
        stated = sorted({r for c in cited for r in (mapping.get(c) or [])})
        parts.append("This image carries it, through " + (titles or "its criteria") + ".")
        if stated:
            parts.append("It states them as " + ", ".join(stated) + ", which name the checks that verify them.")
        if control["handoff"]:
            parts.append("The image cannot constrain how a deployment runs it: " + ", ".join(control["handoff"])
                         + " is the platform's part.")
    else:
        parts.append(WHO[origination] + " carries it. " + control["reason"])
        if cited:
            parts.append("This image contributes " + ", ".join(cited) + ".")
        if control["handoff"] and origination != "not-applicable":
            parts.append("The platform's part is " + ", ".join(control["handoff"]) + ".")
    return " ".join(parts)


def build(component: dict, decisions: dict, mapping: dict, image: str) -> str:
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    criteria = baseline["criteria"]
    entries = implemented(component)
    decided = {r["control"]: r["statement"] for r in decisions.get("decisions", [])}
    reviewed = {r["control"]: (r.get("reviewed_by"), r.get("reviewed_on")) for r in decisions.get("decisions", [])}
    counts: dict[str, int] = {}
    families: dict[str, list[str]] = {}
    for control in baseline["controls"]:
        entry = entries.get(control["id"], {})
        origination = props(entry, "origination")[0] if props(entry, "origination") else control["origination"]
        counts[origination] = counts.get(origination, 0) + 1
        row = ["| [" + control["label"] + "](../../docs/assessment/" + control["id"] + ".md) | "
               + control["title"] + " | " + origination + " | "
               + statement(control, entry, decided, criteria, mapping).replace("|", "\\|")]
        if control["id"] in decided:
            by, on = reviewed[control["id"]]
            row.append(" Decided by this image" + (", reviewed by " + str(by) + " on " + str(on) if by and on
                                                   else ", **not yet reviewed**") + ".")
        row.append(" |")
        families.setdefault(control["family"], []).append("".join(row))

    lines = [
        "# Control statements: " + image,
        "",
        "What carries every control in the standard's [baseline](../../docs/controls/README.md) for",
        "this image, and who carries the rest. Generated from the baseline, this image's",
        "[component definition](oscal/component-definition.json), and its",
        "[decisions](decisions.json) by `scripts/build-statements.py`; do not edit it by hand.",
        "",
        "Controls and criteria are many to many. A criterion contributes to several",
        "controls, and a control is usually divided between the image, its deployment, the",
        "host, and the organization. A statement says **what this image carries of a",
        "control**, and who carries the rest; it does not say the control is satisfied,",
        "which is true only when every part of it is. Nor is it evidence: what this image",
        "evidences, and how well, is its [conformance score](../../docs/EVIDENCE.md).",
        "",
        "| Origination | Controls |",
        "| --- | ---: |",
    ]
    for origination in ("image-owned", "deployment-configured", "host-inherited", "organization-inherited",
                        "not-applicable", "research-required"):
        if counts.get(origination):
            lines.append("| `" + origination + "` | " + str(counts[origination]) + " |")
    lines.append("| **Total** | **" + str(sum(counts.values())) + "** |")
    for family in sorted(families):
        lines += ["", "## " + FAMILIES.get(family, family.upper()) + " (" + family.upper() + ")", "",
                  "| Control | Title | Origination | What carries it |", "| --- | --- | --- | --- |"]
        lines += families[family]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--component", type=Path, required=True)
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--crosswalk", type=Path)
    parser.add_argument("--image", default="this image")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="fail if the committed page is stale")
    args = parser.parse_args()

    body = build(
        json.loads(args.component.read_text(encoding="utf-8")),
        json.loads(args.decisions.read_text(encoding="utf-8")) if args.decisions else {},
        json.loads(args.crosswalk.read_text(encoding="utf-8"))["criteria"] if args.crosswalk else {},
        args.image,
    )
    if args.check:
        if not args.out.exists() or args.out.read_text(encoding="utf-8") != body:
            print("the control statements are stale: python scripts/build-statements.py", file=sys.stderr)
            return 1
        print("the control statements are up to date")
        return 0
    args.out.write_text(body, encoding="utf-8", newline="\n")
    print("wrote " + str(args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
