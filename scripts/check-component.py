#!/usr/bin/env python3
"""Check an image's OSCAL component definition against the control model.

Run from an image repository, against a pinned revision of this one. It holds
the rules in docs/CONTROL-MODEL.md:

- every control carries exactly one origination, and a responsible role that
  matches it
- an `image-owned` control cites the standard's criteria behind it, and at
  least one requirement the image's own repository states, which is the
  verification pointer
- only an `image-owned` control carries an assessment method
- a control's origination matches the baseline, except where the baseline
  leaves it `research-required` for the image to decide
- every control in the baseline is present, unless --allow-incomplete

It never edits the component definition.

Usage:
    python check-component.py artifacts/oscal/component-definition.json \\
        --requirements docs/L1-REQ.md docs/L2-REQ.md docs/L3-REQ.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"

# The heading shape nginx-ubi's requirement tree uses: "### L1-IMG-001".
DEFAULT_PATTERN = r"^###\s+(L[123]-[A-Z]{3}-\d{3})\s*$"
METHODS = {"examine", "test", "interview"}
CROSS_REFERENCE = re.compile(r"^[a-z0-9][a-z0-9-]*:\S+$")


def props(entry: dict, name: str, namespace: str) -> list[str]:
    return [
        p.get("value", "")
        for p in entry.get("props", [])
        if p.get("name") == name and p.get("ns") == namespace
    ]


def implemented(component: dict) -> list[dict]:
    found: list[dict] = []
    for comp in component["component-definition"].get("components", []):
        for implementation in comp.get("control-implementations", []):
            found.extend(implementation.get("implemented-requirements", []))
    return found


def stated_requirements(files: list[Path], pattern: str) -> set[str]:
    expression = re.compile(pattern, re.M)
    found: set[str] = set()
    for path in files:
        found.update(expression.findall(path.read_text(encoding="utf-8")))
    return found


def check(
    component: dict,
    baseline: dict,
    requirements: set[str] | None,
    allow_incomplete: bool = False,
) -> tuple[list[str], list[str]]:
    """Return (violations, warnings)."""
    namespace = baseline["model"]["namespace"]
    roles = {k: v["responsible_role"] for k, v in baseline["model"]["originations"].items()}
    required = {k for k, v in baseline["criteria"].items() if v["level"] == "required"}
    expected = {c["id"]: c for c in baseline["controls"]}

    violations: list[str] = []
    warnings: list[str] = []
    seen: set[str] = set()

    for entry in implemented(component):
        control = entry.get("control-id", "")
        where = control or "(no control-id)"
        if control in seen:
            violations.append(where + ": listed more than once")
        seen.add(control)

        originations = props(entry, "origination", namespace)
        if len(originations) != 1:
            violations.append(where + ": must carry exactly one origination, has " + str(len(originations)))
            continue
        origination = originations[0]
        if origination not in roles:
            violations.append(where + ": unknown origination " + repr(origination))
            continue

        role = roles[origination]
        assigned = {r.get("role-id") for r in entry.get("responsible-roles", [])}
        if role is not None and role not in assigned:
            violations.append(where + ": " + origination + " requires responsible role " + role)

        criteria = props(entry, "criterion", namespace)
        pointers = props(entry, "requirement", namespace)
        methods = props(entry, "assessment-method", namespace)

        for criterion in criteria:
            if criterion not in baseline["criteria"]:
                violations.append(where + ": cites unknown criterion " + criterion)

        if origination == "image-owned":
            if not criteria:
                violations.append(where + ": image-owned without a criterion")
            for criterion in criteria:
                if criterion in baseline["criteria"] and criterion not in required:
                    violations.append(where + ": image-owned on the strength of target " + criterion)
            if not pointers:
                violations.append(where + ": image-owned without a requirement pointer")
            if requirements is not None:
                for pointer in pointers:
                    if pointer not in requirements:
                        violations.append(where + ": requirement " + pointer + " is not stated by this repository")
            if not methods:
                violations.append(where + ": image-owned without an assessment method")
            if not (entry.get("remarks") or "").strip():
                warnings.append(where + ": image-owned with no remarks; an image-owned control with no limitations is usually one nobody has thought about")
        elif methods:
            violations.append(where + ": only an image-owned control carries an assessment method")

        for method in methods:
            if method not in METHODS:
                violations.append(where + ": unknown assessment method " + repr(method))

        for reference in props(entry, "cross-reference", namespace):
            if not CROSS_REFERENCE.match(reference):
                violations.append(where + ": cross-reference " + repr(reference) + " must be <source-id>:<reference>")

        if control not in expected:
            warnings.append(where + ": not in the baseline; nothing to check it against")
            continue
        base = expected[control]
        if base["origination"] != "research-required" and origination != base["origination"]:
            violations.append(
                where + ": baseline is " + base["origination"] + ", component says " + origination
            )
        if origination == "image-owned" and base["origination"] == "image-owned":
            missing = [c for c in base["criteria"] if c not in criteria]
            if missing:
                violations.append(where + ": does not cite baseline criteria " + ", ".join(missing))

    absent = [c for c in expected if c not in seen]
    if absent:
        message = str(len(absent)) + " baseline controls are absent, first " + ", ".join(absent[:8])
        (warnings if allow_incomplete else violations).append(message)

    return violations, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("component", type=Path, help="the OSCAL component definition to check")
    parser.add_argument("--baseline", type=Path, default=BASELINE, help="the control baseline (default: this repository's)")
    parser.add_argument("--requirements", type=Path, nargs="*", help="files stating the image's requirement identifiers")
    parser.add_argument("--requirement-pattern", default=DEFAULT_PATTERN, help="regular expression capturing one identifier per match")
    parser.add_argument("--allow-incomplete", action="store_true", help="report absent baseline controls as warnings")
    args = parser.parse_args()

    component = json.loads(args.component.read_text(encoding="utf-8"))
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    requirements = stated_requirements(args.requirements, args.requirement_pattern) if args.requirements else None
    if requirements is not None and not requirements:
        print("no requirement identifiers found; check --requirement-pattern", file=sys.stderr)
        return 2

    violations, warnings = check(component, baseline, requirements, args.allow_incomplete)
    for warning in warnings:
        print("warning: " + warning)
    for violation in violations:
        print("violation: " + violation)
    checked = len(implemented(component))
    print(
        str(checked) + " controls checked against " + str(baseline["summary"]["controls"])
        + " in the baseline; " + str(len(violations)) + " violations, " + str(len(warnings)) + " warnings"
    )
    if requirements is None:
        print("requirement pointers were not resolved; pass --requirements to check them")
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
