#!/usr/bin/env python3
"""Derive the control baseline every Datopsis image component starts from.

For each control in the NIST SP 800-53 Rev 5 High baseline, and each further
control the standard reaches, the baseline records an origination: who
satisfies the control, and on what basis. Most of it is derived rather than
asserted:

1. A control reached by a required image criterion is `image-owned`, because
   the criterion is a testable property the image states it has.
2. Otherwise, a control reached only by platform or host expectations takes
   their origination, `deployment-configured` or `host-inherited`.
3. Otherwise, the control's family may have a default, for families no image
   can meet, such as personnel or physical security.
4. Otherwise it is `research-required`: whether an image implements it depends
   on the image's function, and each image decides.

"Reached" means through an anchor: the criterion cites an SRG rule, and the
crosswalk says the rule reaches the control. Where that derivation is wrong,
artifacts/control-determinations.json overrides it, with a reason. An override
that says what derivation already says is refused, so the file only ever holds
decisions.

Usage:
    python scripts/build-control-baseline.py            # regenerate
    python scripts/build-control-baseline.py --check    # fail if stale
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REGISTER = REPOSITORY / "artifacts" / "sources.json"
CROSSWALK = REPOSITORY / "artifacts" / "crosswalk.json"
DETERMINATIONS = REPOSITORY / "artifacts" / "control-determinations.json"
CRITERIA = REPOSITORY / "docs" / "standard" / "criteria.md"
PLATFORM = REPOSITORY / "docs" / "standard" / "platform.md"
DATA = REPOSITORY / "artifacts" / "control-baseline.json"
OUTPUT = REPOSITORY / "docs" / "controls" / "README.md"
ASSESSMENT = REPOSITORY / "docs" / "assessment"
INSERT = re.compile(r"\{\{\s*insert:\s*param,\s*([\w.-]+)\s*\}\}")
SEARCH_ROOTS = (REPOSITORY, REPOSITORY / "sources")

CATALOGUE_SOURCE = "nist-sp800-53r5-catalog"
BASELINE_SOURCE = "nist-sp800-53r5-high-baseline"

# An identifier, not a URL anyone resolves. It is fixed: changing it would
# orphan every property written against it.
NAMESPACE = "https://datopsis.example/ns/oscal"

# Origination values and the role that must act on each. See
# docs/CONTROL-MODEL.md.
ROLES = {
    "image-owned": "image-project",
    "deployment-configured": "deployment-profile",
    "host-inherited": "host-orchestrator",
    "organization-inherited": "organization",
    "not-applicable": None,
    "research-required": "image-project",
}
HANDOFFS = {"deployment-configured", "host-inherited"}

HEADING = re.compile(r"^### ((IMG|PLT|HST)-(T?\d+)) (.+)$", re.M)
RULE = re.compile(r"\.\./srg/([^/]+)/rules/(V-\d+)\.md")
IDENTIFIER = re.compile(r"\b((?:IMG|PLT|HST)-T?\d+)\b")


@dataclass
class Item:
    id: str
    title: str
    required: bool
    controls: set[str] = field(default_factory=set)
    platform: list[str] = field(default_factory=list)
    contributions: list[str] = field(default_factory=list)
    origination: str | None = None
    verification: str = ""
    evidence: str = ""
    scope: str | None = None
    manual_review: str | None = None


@dataclass
class Control:
    id: str
    label: str
    title: str
    family: str
    high: bool


def field_line(section: str, name: str) -> str:
    match = re.search(r"^- \*\*" + name + r":\*\*(.*(?:\n  .*)*)", section, re.M)
    return match.group(1) if match else ""


def parse_standard(
    path: Path, reached: dict[tuple[str, str], list[str]]
) -> dict[str, Item]:
    body = path.read_text(encoding="utf-8")
    found = list(HEADING.finditer(body))
    items: dict[str, Item] = {}
    for index, match in enumerate(found):
        end = found[index + 1].start() if index + 1 < len(found) else len(body)
        section = body[match.start():end]
        identifier = match.group(1)
        item = Item(
            id=identifier,
            title=match.group(4).strip(),
            required=not match.group(3).startswith("T"),
        )
        for catalogue, rule in RULE.findall(field_line(section, "Anchors")):
            item.controls.update(reached[(catalogue, rule)])
        item.platform = IDENTIFIER.findall(field_line(section, "Platform"))
        item.contributions = [
            i for i in IDENTIFIER.findall(field_line(section, "Image contribution"))
            if i.startswith("IMG-")
        ]
        origination = re.search(r"`([a-z-]+)`", field_line(section, "Origination"))
        item.origination = origination.group(1) if origination else None
        item.verification = " ".join(field_line(section, "Verification").split())
        item.evidence = " ".join(field_line(section, "Evidence").split())
        manual = field_line(section, "Manual review").strip()
        item.manual_review = "examine" if manual.startswith("Allowed, by examine") else None
        scope = field_line(section, "Scope").strip()
        item.scope = "architecture" if scope.startswith("Per architecture") else "generic" if scope.startswith("Generic") else None
        items[identifier] = item
    return items


def sort_key(control: str) -> tuple:
    family, rest = control.split("-", 1)
    return (family,) + tuple(int(part) for part in rest.split("."))


def ordered(values) -> list[str]:
    def key(value: str) -> tuple:
        prefix, number = value.split("-", 1)
        return ({"IMG": 0, "PLT": 1, "HST": 2}[prefix], number.startswith("T"), int(number.lstrip("T")))
    return sorted(set(values), key=key)


def derive(
    control: str,
    criteria: dict[str, Item],
    expectations: dict[str, Item],
    defaults: dict[str, dict],
    undetermined: str,
) -> dict:
    """What the standard alone says about a control, before any override."""
    owning = [c for c in criteria.values() if c.required and control in c.controls]
    reaching = [e for e in expectations.values() if control in e.controls]

    if owning:
        handoff = {e.id for e in reaching}
        for criterion in owning:
            handoff.update(criterion.platform)
        return {
            "origination": "image-owned",
            "criteria": ordered(c.id for c in owning),
            "handoff": ordered(handoff),
            "basis": "criterion",
            "reason": "Reached by a required image criterion.",
        }

    if reaching:
        originations = {e.origination for e in reaching}
        if len(originations) != 1:
            return {
                "conflict": ordered(e.id for e in reaching),
                "originations": sorted(o or "none" for o in originations),
            }
        contributions = set()
        for expectation in reaching:
            contributions.update(expectation.contributions)
        return {
            "origination": originations.pop(),
            "criteria": ordered(contributions),
            "handoff": ordered(e.id for e in reaching),
            "basis": "expectation",
            "reason": "Reached only by platform or host expectations.",
        }

    family = control.split("-")[0]
    if family in defaults:
        return {
            "origination": defaults[family]["origination"],
            "criteria": [],
            "handoff": [],
            "basis": "family",
            "reason": defaults[family]["reason"],
        }

    return {
        "origination": "research-required",
        "criteria": [],
        "handoff": [],
        "basis": "undetermined",
        "reason": undetermined,
    }


def determine(
    controls: list[Control],
    criteria: dict[str, Item],
    expectations: dict[str, Item],
    determinations: dict,
) -> list[dict]:
    """Resolve every control. Raises SystemExit on any inconsistency."""
    known = {c.id for c in controls}
    overrides: dict[str, dict] = {}
    for entry in determinations["determinations"]:
        if entry["control"] in overrides:
            raise SystemExit("determination for " + entry["control"] + " given twice")
        overrides[entry["control"]] = entry

    problems: list[str] = []
    resolved: list[dict] = []
    for control in controls:
        derived = derive(
            control.id, criteria, expectations,
            determinations["family_defaults"], determinations["undetermined"],
        )
        override = overrides.pop(control.id, None)

        if override is None:
            if "conflict" in derived:
                problems.append(
                    control.id + " is reached by " + ", ".join(derived["conflict"])
                    + " with different originations (" + ", ".join(derived["originations"])
                    + "); add a determination"
                )
                continue
            result = derived
        else:
            result = {
                "origination": override["origination"],
                "criteria": ordered(override.get("criteria", [])),
                "handoff": ordered(override.get("handoff", [])),
                "basis": "determination",
                "reason": override.get("reason", "").strip(),
            }
            same = all(result[k] == derived.get(k) for k in ("origination", "criteria", "handoff"))
            if same:
                problems.append(control.id + " determination repeats what derivation gives; remove it")
            if not result["reason"]:
                problems.append(control.id + " determination has no reason")

        problems.extend(validate(control.id, result, criteria, expectations))
        resolved.append({
            "id": control.id,
            "label": control.label,
            "title": control.title,
            "family": control.family,
            "high_baseline": control.high,
            "origination": result["origination"],
            "responsible_role": ROLES.get(result["origination"]),
            "criteria": result["criteria"],
            "handoff": result["handoff"],
            "basis": result["basis"],
            "reason": result["reason"],
        })

    for leftover in overrides:
        problems.append(
            "determination for " + leftover + ", which is neither in the High "
            "baseline nor reached by the standard" if leftover not in known else ""
        )
    problems = [p for p in problems if p]
    if problems:
        raise SystemExit("the control baseline cannot be derived:\n  " + "\n  ".join(problems))
    return resolved


def validate(control: str, result: dict, criteria: dict[str, Item], expectations: dict[str, Item]) -> list[str]:
    problems: list[str] = []
    origination = result["origination"]
    if origination not in ROLES:
        return [control + " has unknown origination " + origination]
    for identifier in result["criteria"]:
        if identifier not in criteria:
            problems.append(control + " cites unknown criterion " + identifier)
        elif origination == "image-owned" and not criteria[identifier].required:
            problems.append(control + " is image-owned on the strength of target " + identifier)
    for identifier in result["handoff"]:
        if identifier not in expectations:
            problems.append(control + " hands off to unknown expectation " + identifier)
    if origination == "image-owned" and not result["criteria"]:
        problems.append(control + " is image-owned without a criterion")
    if origination in HANDOFFS and not result["handoff"]:
        problems.append(control + " is " + origination + " without naming an expectation")
    return problems


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find(name: str) -> Path:
    for root in SEARCH_ROOTS:
        if root.is_dir():
            hits = sorted(root.glob("**/" + name))
            if hits:
                return hits[0]
    raise SystemExit(
        "missing input " + name + "\nRetrieve the pinned sources first: "
        "python scripts/verify-sources.py --fetch sources/"
    )


def pinned(source: dict) -> Path:
    path = find(Path(source["url"]).name)
    digest = sha256(path)
    if digest != source["sha256"]:
        raise SystemExit(
            path.name + " does not match its pinned digest\n  pinned   "
            + source["sha256"] + "\n  actual   " + digest
        )
    return path


def load_controls(
    register: dict[str, dict], reached_ids: set[str]
) -> tuple[str, list[Control], dict[str, dict], dict[str, dict]]:
    catalogue = json.loads(pinned(register[CATALOGUE_SOURCE]).read_text(encoding="utf-8"))["catalog"]
    profile = json.loads(pinned(register[BASELINE_SOURCE]).read_text(encoding="utf-8"))["profile"]
    high = {
        i for imported in profile["imports"]
        for include in imported.get("include-controls", [])
        for i in include.get("with-ids", [])
    }

    entries: dict[str, Control] = {}
    withdrawn: set[str] = set()
    nodes: dict[str, dict] = {}
    params: dict[str, dict] = {}

    def label_of(node: dict) -> str:
        for prop in node.get("props", []):
            if prop.get("name") == "label" and prop.get("class") != "zero-padded":
                return prop["value"]
        return node["id"].upper()

    def walk(children: list[dict], family: str) -> None:
        for node in children:
            nodes[node["id"]] = node
            for param in node.get("params", []):
                params[param["id"]] = param
            if any(p.get("name") == "status" and p.get("value") == "withdrawn" for p in node.get("props", [])):
                withdrawn.add(node["id"])
            else:
                entries[node["id"]] = Control(
                    id=node["id"], label=label_of(node), title=node["title"],
                    family=family, high=node["id"] in high,
                )
            walk(node.get("controls", []), family)

    for group in catalogue["groups"]:
        walk(group.get("controls", []), group["id"])

    wanted = high | reached_ids
    missing = sorted(wanted - set(entries))
    if missing:
        raise SystemExit("not in the pinned catalogue, or withdrawn: " + ", ".join(missing))
    chosen = sorted((entries[i] for i in wanted), key=lambda c: sort_key(c.id))
    return catalogue["metadata"]["version"], chosen, nodes, params


def build() -> dict[Path, str]:
    register = {s["id"]: s for s in json.loads(REGISTER.read_text(encoding="utf-8"))["sources"]}
    crosswalk = json.loads(CROSSWALK.read_text(encoding="utf-8"))
    reached = {
        (c["slug"], r["group_id"]): r["controls"]
        for c in crosswalk["catalogues"] for r in c["rules"]
    }
    criteria = parse_standard(CRITERIA, reached)
    expectations = parse_standard(PLATFORM, reached)
    determinations = json.loads(DETERMINATIONS.read_text(encoding="utf-8"))

    reached_ids = set()
    for item in list(criteria.values()) + list(expectations.values()):
        if item.required:
            reached_ids |= item.controls
    reached_ids |= {d["control"] for d in determinations["determinations"]}

    version, controls, nodes, params = load_controls(register, reached_ids)
    resolved = determine(controls, criteria, expectations, determinations)
    data = assemble(resolved, criteria, expectations, register, version)
    pages = {
        DATA: json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        OUTPUT: page(data, determinations),
    }
    anchors = heading_anchors()
    BASELINE_IDS.clear()
    BASELINE_IDS.update(c["id"] for c in resolved)
    for control in resolved:
        pages[ASSESSMENT / (control["id"] + ".md")] = assessment_page(
            control, nodes[control["id"]], params, criteria, anchors, version
        )
    return pages


def heading_anchors() -> dict[str, str]:
    anchors = {}
    for path in (CRITERIA, PLATFORM):
        for match in HEADING.finditer(path.read_text(encoding="utf-8")):
            slug = re.sub(r"[^\w\- ]", "", match.group(0).lstrip("#").strip().lower()).replace(" ", "-")
            anchors[match.group(1)] = slug
    return anchors


CATALOGUE_LINK = re.compile(r"\[([^\]]*)\]\(#([^)]+)\)")
LOCAL_LINK = re.compile(r"\]\((#|criteria\.md|platform\.md)")
BASELINE_IDS: set[str] = set()


def prose(text: str, params: dict[str, dict]) -> str:
    """Render OSCAL prose, marking organization-defined parameters as assignments.

    The catalogue links to its own anchors: another control, or a part of one.
    A control this baseline covers links to its assessment page here; anything
    else becomes plain text, since the anchor does not exist on these pages.
    """
    def assignment(match: re.Match) -> str:
        param = params.get(match.group(1), {})
        label = param.get("label") or " ".join(
            g.get("prose", "") for g in param.get("guidelines", [])
        ).strip().rstrip(";") or match.group(1)
        return "[*Assignment: " + label + "*]"

    def relink(match: re.Match) -> str:
        label, target = match.groups()
        if target in BASELINE_IDS:
            return "[" + label + "](" + target + ".md)"
        return label

    text = INSERT.sub(assignment, text or "")
    return " ".join(CATALOGUE_LINK.sub(relink, text).split())


def rebase(text: str) -> str:
    """Re-point a criterion's own links so they resolve from docs/assessment/."""
    def fix(match: re.Match) -> str:
        target = match.group(1)
        if target == "#":
            return "](../standard/criteria.md#"
        return "](../standard/" + target
    return LOCAL_LINK.sub(fix, text)


def label_prop(part: dict) -> str:
    for prop in part.get("props", []):
        if prop.get("name") == "label":
            return prop["value"]
    return ""


def outline(part: dict, params: dict[str, dict], kind: str, depth: int = 0) -> list[str]:
    """A nested list of a statement or objective and its sub-parts."""
    lines = []
    text = prose(part.get("prose", ""), params)
    label = label_prop(part)
    if text or label:
        lines.append("  " * depth + "- " + ("**" + label + "** " if label else "") + text)
    for child in part.get("parts", []):
        if child.get("name") == kind:
            lines.extend(outline(child, params, kind, depth + (1 if (text or label) else 0)))
    return lines


def assessment_page(control, node, params, criteria, anchors, version) -> str:
    def ref(identifier: str) -> str:
        target = "criteria.md" if identifier.startswith("IMG-") else "platform.md"
        return "[" + identifier + "](../standard/" + target + "#" + anchors[identifier] + ")"

    parts = node.get("parts", [])
    out: list[str] = []
    out.append("# " + control["label"] + " " + control["title"])
    out.append("")
    out.append("| | |")
    out.append("| --- | --- |")
    out.append("| Origination | `" + control["origination"] + "` |")
    out.append("| High baseline | " + ("Selected" if control["high_baseline"] else "Not selected") + " |")
    if control["criteria"]:
        out.append("| Criteria | " + ", ".join(ref(i) for i in control["criteria"]) + " |")
    if control["handoff"]:
        out.append("| Handoff | " + ", ".join(ref(i) for i in control["handoff"]) + " |")
    out.append("| Catalogue | NIST SP 800-53 Rev 5, " + version + ", with SP 800-53A procedures |")
    out.append("")
    out.append(control["reason"])
    out.append("")

    for part in parts:
        if part.get("name") == "statement":
            out.append("## Control")
            out.append("")
            out.extend(outline(part, params, "item") or [prose(part.get("prose", ""), params)])
            out.append("")

    goals = [p for p in parts if p.get("name") == "assessment-objective"]
    out.append("## Assessment objective")
    out.append("")
    if goals:
        out.append("Determine if:")
        out.append("")
        for goal in goals:
            out.extend(outline(goal, params, "assessment-objective"))
    else:
        out.append("_The pinned catalogue gives no assessment objective for this control._")
    out.append("")

    methods = [p for p in parts if p.get("name") == "assessment-method"]
    if methods:
        out.append("## Assessment methods")
        out.append("")
        for method in methods:
            name = next((q["value"] for q in method.get("props", []) if q.get("name") == "method"), "")
            out.append("### " + name.title())
            out.append("")
            for objects in method.get("parts", []):
                for item in (objects.get("prose") or "").split("\n"):
                    if item.strip():
                        out.append("- " + prose(item, params))
            out.append("")

    if control["origination"] == "image-owned":
        out.append("## What the image's evidence answers")
        out.append("")
        out.append(
            "The Test method is answered by the image's own verification of each "
            "criterion this claim rests on, and the evidence it records. Examine "
            "and Interview are answered by the image's documentation and by the "
            "people responsible for it."
        )
        out.append("")
        out.append("| Criterion | Verification | Evidence |")
        out.append("| --- | --- | --- |")
        for identifier in control["criteria"]:
            item = criteria[identifier]
            out.append(
                "| " + ref(identifier) + " | " + rebase(item.verification).replace("|", "\\|")
                + " | " + rebase(item.evidence).replace("|", "\\|") + " |"
            )
        out.append("")

    out.append("---")
    out.append("")
    out.append(
        "Generated by `scripts/build-control-baseline.py` from the pinned NIST "
        "catalogue, which carries the SP 800-53A procedures. Do not edit by hand."
    )
    out.append("")
    return "\n".join(out)


def assemble(resolved, criteria, expectations, register, version) -> dict:
    counts: dict[str, int] = {}
    for control in resolved:
        counts[control["origination"]] = counts.get(control["origination"], 0) + 1
    return {
        "schema_version": 1,
        "note": (
            "Generated by scripts/build-control-baseline.py. Do not edit by hand. "
            "The origination each Datopsis image component starts from, for every "
            "control in the NIST SP 800-53 Rev 5 High baseline and every further "
            "control the standard reaches. See docs/CONTROL-MODEL.md."
        ),
        "inputs": {
            "catalogue": {"source": CATALOGUE_SOURCE, "release": version, "sha256": register[CATALOGUE_SOURCE]["sha256"]},
            "baseline": {"source": BASELINE_SOURCE, "sha256": register[BASELINE_SOURCE]["sha256"]},
        },
        "model": {
            "namespace": NAMESPACE,
            "originations": {k: {"responsible_role": v} for k, v in ROLES.items()},
        },
        "criteria": {
            c.id: {"title": c.title, "level": "required" if c.required else "target",
                   **({"scope": c.scope} if c.required else {}),
                   **({"manual_review": c.manual_review} if c.manual_review else {})}
            for c in (criteria[i] for i in ordered(criteria))
        },
        "expectations": {
            e.id: {"title": e.title, "origination": e.origination}
            for e in (expectations[i] for i in ordered(expectations))
        },
        "summary": {
            "controls": len(resolved),
            "high_baseline": sum(c["high_baseline"] for c in resolved),
            "by_origination": {k: counts.get(k, 0) for k in ROLES},
        },
        "controls": resolved,
    }


def page(data: dict, determinations: dict) -> str:
    anchors = {}
    for path in (CRITERIA, PLATFORM):
        for match in HEADING.finditer(path.read_text(encoding="utf-8")):
            slug = re.sub(r"[^\w\- ]", "", match.group(0).lstrip("#").strip().lower()).replace(" ", "-")
            anchors[match.group(1)] = slug

    def ref(identifier: str) -> str:
        target = "criteria.md" if identifier.startswith("IMG-") else "platform.md"
        return "[" + identifier + "](../standard/" + target + "#" + anchors[identifier] + ")"

    summary = data["summary"]
    out: list[str] = []
    out.append("# Control baseline")
    out.append("")
    out.append(
        "The origination every Datopsis image component starts from, for each "
        "control in the NIST SP 800-53 Rev 5 High baseline and each further "
        "control the [standard](../standard/README.md) reaches. What the values "
        "mean, and how an image repository uses this, is in "
        "[the control model](../CONTROL-MODEL.md)."
    )
    out.append("")
    out.append(
        "Most of it is derived. A control an image criterion reaches through its "
        "anchors is `image-owned`; one only platform or host expectations reach "
        "takes their origination; some families have a default; the rest are "
        "`research-required`. Where derivation would be wrong, a "
        "[determination](#determinations) overrides it, with its reason."
    )
    out.append("")
    out.append("| Origination | Controls | Responsible role |")
    out.append("| --- | ---: | --- |")
    for origination, role in ROLES.items():
        out.append(
            "| `" + origination + "` | " + str(summary["by_origination"][origination])
            + " | " + (("`" + role + "`") if role else "none") + " |"
        )
    out.append(
        "| **Total** | **" + str(summary["controls"]) + "** | "
        + str(summary["high_baseline"]) + " in the High baseline |"
    )
    out.append("")
    out.append(
        "`research-required` is not a gap in the standard. It marks controls "
        "whose answer depends on what the image does: a database authenticates "
        "users and a static file server does not. Each image determines them in "
        "its own component definition."
    )
    out.append("")

    out.append("## By family")
    out.append("")
    families: dict[str, list[dict]] = {}
    for control in data["controls"]:
        families.setdefault(control["family"], []).append(control)
    columns = list(ROLES)
    out.append("| Family | " + " | ".join("`" + c + "`" for c in columns) + " |")
    out.append("| --- |" + " ---: |" * len(columns))
    for family, members in families.items():
        row = "| [" + family.upper() + "](#" + family + ") |"
        for origination in columns:
            count = sum(1 for m in members if m["origination"] == origination)
            row += " " + (str(count) if count else "") + " |"
        out.append(row)
    out.append("")

    out.append("## Controls")
    out.append("")
    out.append(
        "**High** marks the control as selected by the High baseline. "
        "**Criteria** are the image criteria behind an `image-owned` control, or "
        "the image's contribution to someone else's. **Handoff** names what the "
        "platform or host must do."
    )
    out.append("")
    for family, members in families.items():
        out.append('<a id="' + family + '"></a>')
        out.append("")
        out.append("### " + family.upper())
        out.append("")
        out.append("| Control | Title | High | Origination | Criteria | Handoff | Basis |")
        out.append("| --- | --- | :-: | --- | --- | --- | --- |")
        for control in members:
            out.append(
                "| [" + control["label"] + "](../assessment/" + control["id"] + ".md) | "
                + control["title"].replace("|", "\\|")
                + " | " + ("Yes" if control["high_baseline"] else "")
                + " | `" + control["origination"] + "` | "
                + ", ".join(ref(i) for i in control["criteria"]) + " | "
                + ", ".join(ref(i) for i in control["handoff"]) + " | "
                + control["basis"] + " |"
            )
        out.append("")

    out.append("## Determinations")
    out.append("")
    out.append(
        "Where derivation would give the wrong answer. Each is held in "
        "[`artifacts/control-determinations.json`](../../artifacts/control-determinations.json), "
        "and the generator refuses one that repeats what derivation already gives."
    )
    out.append("")
    labels = {c["id"]: c["label"] for c in data["controls"]}
    for entry in sorted(determinations["determinations"], key=lambda e: sort_key(e["control"])):
        out.append("- **" + labels[entry["control"]] + "** `" + entry["origination"] + "`. " + entry["reason"])
    out.append("")
    out.append("### Family defaults")
    out.append("")
    for family, default in determinations["family_defaults"].items():
        out.append("- **" + family.upper() + "** `" + default["origination"] + "`. " + default["reason"])
    out.append("")
    out.append("---")
    out.append("")
    out.append(
        "Generated by `scripts/build-control-baseline.py` from the standard, the "
        "crosswalk, and the pinned NIST catalogue and High baseline. Do not edit "
        "by hand; the drift check fails."
    )
    out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if the committed baseline is stale")
    args = parser.parse_args()

    pages = build()
    orphans = [p for p in ASSESSMENT.glob("*.md") if p not in pages] if ASSESSMENT.is_dir() else []
    if args.check:
        stale = [
            Path(os.path.relpath(p, REPOSITORY)).as_posix()
            for p, body in pages.items()
            if not p.exists() or p.read_text(encoding="utf-8") != body
        ] + ["orphaned " + Path(os.path.relpath(p, REPOSITORY)).as_posix() for p in orphans]
        if stale:
            print("the control baseline is stale: " + ", ".join(stale), file=sys.stderr)
            print("Regenerate: python scripts/build-control-baseline.py", file=sys.stderr)
            return 1
        print("the control baseline is up to date")
        return 0

    for orphan in orphans:
        orphan.unlink()
    for path, body in pages.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8", newline="\n")
    data = json.loads(pages[DATA])
    print(
        "wrote the control baseline: " + str(data["summary"]["controls"]) + " controls, "
        + ", ".join(k + " " + str(v) for k, v in data["summary"]["by_origination"].items() if v)
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
