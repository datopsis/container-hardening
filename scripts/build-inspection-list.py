#!/usr/bin/env python3
"""Write the list of controls an image must inspect, from what the image does.

The standard lists every control. Which of them an image must actually look at
depends on what that image is: a static file server and one that terminates
mutual TLS do not inspect the same list. An image declares its capabilities in
its hardening profile; this turns them into the list, from
artifacts/inspection-map.json:

- **Always**: every control the baseline leaves to the image to decide, or
  gives the image or its deployment. These are the image's to answer whatever
  it does.
- **By capability**: each capability adds the controls that only apply because
  the image does that thing. Declaring `terminates-mutual-tls` adds
  identification and access enforcement; removing it takes them away again.
- **Worth considering**: a capability may also raise a control the High
  baseline does not select, such as output filtering for an image that renders
  content a caller supplied. Those are not required; they are put in front of
  whoever inspects, to select or to decline with a reason.

It says which controls to inspect, and flags a control whose decision looks
wrong beside a declared capability, such as one answered not-applicable that a
capability says the image does. It does not inspect anything: that is a
person's work, written up in the image's cyber package
(docs/CYBER-PACKAGE.md). What this can check is that the list is complete, and
that every control on it has been addressed somewhere.

Usage:
    python build-inspection-list.py --profile hardening-profile.json \\
        --component oscal/component-definition.json --decisions decisions.json \\
        --image my-image --out INSPECTION-LIST.md [--check]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
MAP = REPOSITORY / "artifacts" / "inspection-map.json"
# An image answers these itself, whatever it does.
ALWAYS = ("image-owned", "deployment-configured", "research-required")
# A capability says the image does this; these answers then need a second look.
SUSPECT = ("not-applicable", "organization-inherited", "host-inherited")


def implemented(component: dict) -> dict[str, dict]:
    found = {}
    for comp in component["component-definition"].get("components", []):
        for implementation in comp.get("control-implementations", []):
            for entry in implementation.get("implemented-requirements", []):
                found[entry.get("control-id")] = entry
    return found


def origination(entry: dict, control: dict) -> str:
    values = [p.get("value") for p in entry.get("props", []) if p.get("name") == "origination"]
    return values[0] if values else control["origination"]


def inspect(profile: dict, component: dict, baseline: dict, mapping: dict) -> tuple[dict[str, dict], list[str]]:
    """Return (controls to inspect, problems with the declaration)."""
    capabilities = profile.get("capabilities")
    problems = []
    if not isinstance(capabilities, list) or not capabilities:
        problems.append("the profile declares no capabilities; an image says what it does, even if that is little")
        capabilities = []
    known = mapping["capabilities"]
    for capability in capabilities:
        if capability not in known:
            problems.append("unknown capability " + repr(capability) + "; one of " + ", ".join(sorted(known)))
    controls = {c["id"]: c for c in baseline["controls"]}
    entries = implemented(component)
    wanted: dict[str, dict] = {}
    for control in baseline["controls"]:
        decided = origination(entries.get(control["id"], {}), control)
        if decided in ALWAYS:
            wanted[control["id"]] = {"control": control, "origination": decided, "because": ["the baseline gives it to the image"]}
    for capability in capabilities:
        if capability not in known:
            continue
        for identifier in known[capability]["controls"]:
            if identifier not in controls:
                problems.append(capability + " names " + identifier + ", which is not in the baseline")
                continue
            decided = origination(entries.get(identifier, {}), controls[identifier])
            row = wanted.setdefault(identifier, {"control": controls[identifier], "origination": decided, "because": []})
            row["because"].append(known[capability]["title"].lower())
            if decided in SUSPECT:
                row.setdefault("review", []).append(capability)
    return wanted, problems


def rows_for(identifiers, controls, wanted, stated, entries, mapping) -> list[str]:
    lines = []
    for identifier in identifiers:
        control = controls[identifier]
        row = wanted.get(identifier)
        because = "; ".join(sorted(set(row["because"]))) if row else "inherited, or nothing to apply it to"
        if identifier in stated:
            reviewed = stated[identifier].get("reviewed_by")
            answered = "decided, " + ("reviewed by " + str(reviewed) if reviewed else "**not yet reviewed**")
        elif entries.get(identifier, {}).get("remarks"):
            answered = "statement"
        else:
            answered = "**nothing**"
        flag = " **review: " + ", ".join(row["review"]) + " says this applies**" if row and row.get("review") else ""
        lines.append("| [" + control["label"] + "](../../docs/assessment/" + identifier + ".md) | " + control["title"]
                     + " | " + (row["origination"] if row else control["origination"]) + " | " + because + " | "
                     + answered + flag + " |")
    return lines


def build(profile: dict, component: dict, decisions: dict, image: str) -> tuple[str, list[str]]:
    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    mapping = json.loads(MAP.read_text(encoding="utf-8"))
    wanted, problems = inspect(profile, component, baseline, mapping)
    stated = {r["control"]: r for r in decisions.get("decisions", [])}
    entries = implemented(component)
    controls = {c["id"]: c for c in baseline["controls"]}
    capabilities = [c for c in profile.get("capabilities", []) if c in mapping["capabilities"]]

    def sorted_ids(identifiers):
        return sorted(identifiers, key=lambda i: (controls[i]["family"], i))

    decided_here = set(wanted)
    inapplicable = [i for i, c in controls.items()
                    if i not in decided_here and origination(entries.get(i, {}), c) == "not-applicable"]
    inherited = [i for i in controls if i not in decided_here and i not in inapplicable]

    lines = [
        "# Controls: " + image,
        "",
        "Every control in the standard's [baseline](../../docs/controls/README.md), in three",
        "groups: the ones this image must inspect, the ones it inherits, and the ones with",
        "nothing here to apply to. The whole list is here so a reviewer can walk it and",
        "confirm each group, rather than trust that the short list is the right short list.",
        "Generated from this image's [hardening profile](hardening-profile.json), its",
        "[component definition](oscal/component-definition.json), and the standard's",
        "[inspection map](../../artifacts/inspection-map.json) by",
        "`scripts/build-inspection-list.py`; do not edit it by hand.",
        "",
        "Inspecting a control is a person's work. What is written here is which controls",
        "that work covers, and where this image's part of each is recorded. Controls and",
        "criteria are many to many: a control is usually divided between the image, its",
        "deployment, the host, and the organization, so the image's part alone never",
        "satisfies one. The parts are in the [control statements](CONTROL-STATEMENTS.md),",
        "and where they are applied in this image is in its",
        "[cyber package](package/README.md).",
        "",
        "| Group | Controls | What a reviewer confirms |",
        "| --- | ---: | --- |",
        "| [To inspect](#to-inspect) | " + str(len(wanted)) + " | That the image's part is right, and complete |",
        "| [Inherited](#inherited) | " + str(len(inherited)) + " | That the platform, host, or organization really does carry it here |",
        "| [Nothing to apply it to](#nothing-to-apply-it-to) | " + str(len(inapplicable)) + " | That the thing the control governs is genuinely absent |",
        "| **Total** | **" + str(len(controls)) + "** | |",
        "",
        "## What this image does",
        "",
        "| Capability | Question it answers yes to |",
        "| --- | --- |",
    ]
    for capability in capabilities:
        entry = mapping["capabilities"][capability]
        lines.append("| `" + capability + "` | " + entry["question"] + " |")
    absent = [c for c in sorted(mapping["capabilities"]) if c not in capabilities]
    lines += ["", "It declares none of: " + ", ".join("`" + c + "`" for c in absent) + ". Each of those",
              "would move controls into the first group below.", "",
              "## To inspect", "",
              "The baseline gives these to the image or its deployment, or a capability brings",
              "them in. Each needs an answer of this image's own.", "",
              "| Control | Title | Who carries it | Inspect because | The image's part |",
              "| --- | --- | --- | --- | --- |"]
    lines += rows_for(sorted_ids(wanted), controls, wanted, stated, entries, mapping)

    consider = [(c, entry) for c in capabilities for entry in mapping["capabilities"][c].get("consider", [])]
    if consider:
        lines += ["", "## Worth considering, though the baseline does not select them", "",
                  "Not required. A capability raises each of these; select it, or decline it with a reason, in the",
                  "cyber package.", "",
                  "| Control | Title | Raised by | Why |", "| --- | --- | --- | --- |"]
        seen = set()
        for capability, entry in consider:
            if entry["control"] in seen:
                continue
            seen.add(entry["control"])
            raised = ", ".join("`" + c + "`" for c, e in consider if e["control"] == entry["control"])
            lines.append("| " + entry["label"] + " | " + entry["title"] + " | " + raised + " | " + entry["why"] + " |")

    lines += ["", "## Inherited", "",
              "Carried by the platform, the host, or the organization. The image contributes to",
              "some of them; none is this image's to answer alone. A reviewer confirms the",
              "inheritance is real for this deployment, not assumed.", "",
              "| Control | Title | Who carries it | Inspect because | The image's part |",
              "| --- | --- | --- | --- | --- |"]
    lines += rows_for(sorted_ids(inherited), controls, wanted, stated, entries, mapping)

    lines += ["", "## Nothing to apply it to", "",
              "Answered not-applicable: the thing the control governs is absent from this image.",
              "This is the group to read most carefully, because it is the one that shrinks as",
              "soon as an image does more. A reviewer confirms each absence.", "",
              "| Control | Title | Who carries it | Inspect because | The image's part |",
              "| --- | --- | --- | --- | --- |"]
    lines += rows_for(sorted_ids(inapplicable), controls, wanted, stated, entries, mapping)
    return "\n".join(lines) + "\n", problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--component", type=Path, required=True)
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--image", default="this image")
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="fail if the committed list is stale")
    args = parser.parse_args()

    body, problems = build(
        json.loads(args.profile.read_text(encoding="utf-8")),
        json.loads(args.component.read_text(encoding="utf-8")),
        json.loads(args.decisions.read_text(encoding="utf-8")) if args.decisions else {},
        args.image,
    )
    for problem in problems:
        print("error: " + problem, file=sys.stderr)
    if args.check:
        if not args.out.exists() or args.out.read_text(encoding="utf-8") != body:
            print("the inspection list is stale: python scripts/build-inspection-list.py", file=sys.stderr)
            return 1
        print("the inspection list is up to date")
        return 1 if problems else 0
    args.out.write_text(body, encoding="utf-8", newline="\n")
    print("wrote " + str(args.out))
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
