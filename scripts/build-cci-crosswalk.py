#!/usr/bin/env python3
"""Derive SRG-to-800-53 cross-references from DISA's CCI list.

Every SRG rule cites one or more Control Correlation Identifiers, and DISA
publishes the CCI list mapping each CCI to NIST SP 800-53 Rev 5. Joining the
two makes the cross-reference derivable rather than hand-authored: nobody
asserts that a rule addresses a control, the pinned sources do.

The join inherits DISA's judgement. Where DISA maps a CCI to a control, so does
this; where DISA is wrong, so is this, and the fix belongs upstream rather than
in a local override that silently diverges from the published list.

Nothing maps against an input whose digest does not match the register. A
reference to a control the pinned catalogue does not contain, or has withdrawn,
stops generation rather than producing a cross-reference to nothing.

Usage:
    python scripts/build-cci-crosswalk.py            # regenerate the crosswalk
    python scripts/build-cci-crosswalk.py --check    # fail if output is stale
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REGISTER = REPOSITORY / "artifacts" / "sources.json"
DATA = REPOSITORY / "artifacts" / "crosswalk.json"
OUTPUT = REPOSITORY / "docs" / "crosswalk"

CCI = "{http://iase.disa.mil/cci}"
REV5 = "NIST SP 800-53 Revision 5"
REV4 = "NIST SP 800-53 Revision 4"

CCI_SOURCE = "disa-cci-list"
CATALOGUE_SOURCE = "nist-sp800-53r5-catalog"
BASELINE_SOURCE = "nist-sp800-53r5-high-baseline"

# DISA writes a Rev 5 reference as the control, an optional enhancement, then
# the part: "AC-2 a 1", "AC-3 (15) (a)". It zero-pads some enhancements, as in
# "IA-13 (03)", so the number is normalised rather than matched as text.
REFERENCE = re.compile(r"^([A-Z]{2})-(\d+)(?:\s*\((\d+)\))?")


def load_srg_builder():
    # Reused rather than reimplemented, so a rule's catalogue slug and page
    # path here cannot diverge from the page build-srg-markdown.py writes.
    path = REPOSITORY / "scripts" / "build-srg-markdown.py"
    spec = importlib.util.spec_from_file_location("build_srg_markdown", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


srg = load_srg_builder()


@dataclass
class Control:
    id: str
    label: str
    title: str
    withdrawn: bool
    family: str
    family_title: str
    high: bool = False


@dataclass
class Citation:
    catalogue: str
    group_id: str
    stig_id: str
    category: str
    title: str
    cci: str
    references: list[str] = field(default_factory=list)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find(name: str) -> Path:
    for root in srg.SEARCH_ROOTS:
        if root.is_dir():
            hits = sorted(root.glob("**/" + name))
            if hits:
                return hits[0]
    raise SystemExit(
        "missing input " + name + "\n"
        "Retrieve the pinned sources first: "
        "python scripts/verify-sources.py --fetch sources/"
    )


def pinned(path: Path, expected: str, what: str) -> str:
    digest = sha256(path)
    if digest != expected:
        raise SystemExit(
            what + " does not match its pinned digest\n"
            "  file     " + str(path) + "\n"
            "  pinned   " + expected + "\n"
            "  actual   " + digest + "\n"
            "Nothing is mapped against an unpinned revision. If DISA or NIST "
            "replaced it, that is a finding to review, not a digest to update."
        )
    return digest


def control_id(reference: str) -> str | None:
    match = REFERENCE.match(reference)
    if match is None:
        return None
    family, number, enhancement = match.groups()
    oscal = family.lower() + "-" + str(int(number))
    if enhancement is not None:
        oscal += "." + str(int(enhancement))
    return oscal


def unmapped_note(entry: dict, controls: dict) -> str:
    """Say what DISA maps a CCI to when it gives no Rev 5 reference."""
    if not entry["rev4"]:
        return "No Rev 5 reference, and no Rev 4 one either"
    parts = []
    for reference in entry["rev4"]:
        identifier = control_id(reference)
        control = controls.get(identifier) if identifier else None
        if control is not None and control.withdrawn:
            parts.append("Rev 4 " + reference + ", which Rev 5 withdraws")
        else:
            parts.append("Rev 4 " + reference)
    return "No Rev 5 reference; DISA maps it only to " + "; ".join(parts)


def load_cci_list(path: Path) -> tuple[str, dict[str, dict]]:
    root = ET.parse(path).getroot()
    version = (root.findtext(CCI + "metadata/" + CCI + "version") or "").strip()
    items: dict[str, dict] = {}
    for item in root.iter(CCI + "cci_item"):
        items[item.get("id", "")] = {
            "status": (item.findtext(CCI + "status") or "").strip(),
            "rev5": [
                ref.get("index", "").strip()
                for ref in item.iter(CCI + "reference")
                if ref.get("title") == REV5
            ],
            "rev4": [
                ref.get("index", "").strip()
                for ref in item.iter(CCI + "reference")
                if ref.get("title") == REV4
            ],
        }
    return version, items


def load_catalogue(path: Path) -> tuple[str, dict[str, Control]]:
    catalogue = json.loads(path.read_text(encoding="utf-8"))["catalog"]
    controls: dict[str, Control] = {}

    def label_of(control: dict) -> str:
        for prop in control.get("props", []):
            if prop.get("name") == "label" and prop.get("class") != "zero-padded":
                return prop["value"]
        return control["id"].upper()

    def walk(nodes: list[dict], group: dict) -> None:
        for node in nodes:
            controls[node["id"]] = Control(
                id=node["id"],
                label=label_of(node),
                title=node["title"],
                withdrawn=any(
                    p.get("name") == "status" and p.get("value") == "withdrawn"
                    for p in node.get("props", [])
                ),
                family=group["id"].upper(),
                family_title=group["title"],
            )
            walk(node.get("controls", []), group)

    for group in catalogue["groups"]:
        walk(group.get("controls", []), group)
    return catalogue["metadata"]["version"], controls


def load_baseline(path: Path) -> set[str]:
    profile = json.loads(path.read_text(encoding="utf-8"))["profile"]
    selected: set[str] = set()
    for imported in profile["imports"]:
        for include in imported.get("include-controls", []):
            selected.update(include.get("with-ids", []))
    return selected


def sort_key(control: str) -> tuple:
    family, rest = control.split("-", 1)
    return (family,) + tuple(int(part) for part in rest.split("."))


def rel(path: Path, start: Path) -> str:
    return Path(os.path.relpath(path, start)).as_posix()


def build() -> dict[Path, str]:
    register = {s["id"]: s for s in json.loads(REGISTER.read_text(encoding="utf-8"))["sources"]}

    cci_source = register[CCI_SOURCE]
    cci_path = find(cci_source["input"]["file"])
    cci_digest = pinned(cci_path, cci_source["input"]["sha256"], "the CCI list")
    cci_version, ccis = load_cci_list(cci_path)

    catalogue_source = register[CATALOGUE_SOURCE]
    catalogue_path = find(Path(catalogue_source["url"]).name)
    pinned(catalogue_path, catalogue_source["sha256"], "the 800-53 catalogue")
    catalogue_version, controls = load_catalogue(catalogue_path)

    baseline_source = register[BASELINE_SOURCE]
    baseline_path = find(Path(baseline_source["url"]).name)
    pinned(baseline_path, baseline_source["sha256"], "the High baseline")
    for identifier in load_baseline(baseline_path):
        controls[identifier].high = True

    xccdf_pins = {
        s["xccdf"]["file"]: s for s in register.values() if s.get("xccdf")
    }
    catalogues = []
    for path in srg.discover():
        source = xccdf_pins.get(path.name)
        if source is None:
            raise SystemExit(path.name + " is not pinned in the register")
        pinned(path, source["xccdf"]["sha256"], path.name)
        catalogues.append((srg.parse(path), source))
    if not catalogues:
        raise SystemExit("no SRG or STIG package found; see docs/SOURCES.md")
    catalogues.sort(key=lambda pair: pair[0].title)

    citations: dict[str, list[Citation]] = {}
    unmapped: list[tuple[str, str, str, str]] = []
    uncited: list[tuple[str, str]] = []
    deprecated: list[tuple[str, str, str]] = []
    data_catalogues = []

    for catalogue, source in catalogues:
        rules_out = []
        for rule in catalogue.rules:
            if not rule.ccis:
                uncited.append((catalogue.slug, rule.group_id))
            rule_controls: set[str] = set()
            rule_ccis = []
            for cci in rule.ccis:
                if cci not in ccis:
                    raise SystemExit(
                        catalogue.title + " " + rule.group_id + " cites " + cci
                        + ", which the pinned CCI list does not define"
                    )
                entry = ccis[cci]
                if entry["status"] == "deprecated":
                    deprecated.append((catalogue.slug, rule.group_id, cci))
                if not entry["rev5"]:
                    unmapped.append((catalogue.slug, rule.group_id, cci, unmapped_note(entry, controls)))

                by_control: dict[str, list[str]] = {}
                for reference in entry["rev5"]:
                    identifier = control_id(reference)
                    if identifier is None or identifier not in controls:
                        raise SystemExit(
                            cci + " maps to " + repr(reference) + ", which the "
                            "pinned 800-53 catalogue does not contain"
                        )
                    if controls[identifier].withdrawn:
                        raise SystemExit(
                            cci + " maps to " + reference + ", which the pinned "
                            "800-53 catalogue has withdrawn"
                        )
                    by_control.setdefault(identifier, []).append(reference)

                for identifier, references in by_control.items():
                    rule_controls.add(identifier)
                    citations.setdefault(identifier, []).append(
                        Citation(
                            catalogue=catalogue.slug,
                            group_id=rule.group_id,
                            stig_id=rule.stig_id,
                            category=rule.category,
                            title=rule.title,
                            cci=cci,
                            references=references,
                        )
                    )
                rule_ccis.append({"cci": cci, "nist": entry["rev5"]})

            rules_out.append({
                "group_id": rule.group_id,
                "stig_id": rule.stig_id,
                "severity": rule.severity,
                "ccis": rule_ccis,
                "controls": sorted(rule_controls, key=sort_key),
            })

        data_catalogues.append({
            "slug": catalogue.slug,
            "source": source["id"],
            "title": catalogue.title,
            "release": source["release"],
            "xccdf": source["xccdf"]["file"],
            "xccdf_sha256": source["xccdf"]["sha256"],
            "rules": rules_out,
        })

    reached = sorted(citations, key=sort_key)
    titles = {c.slug: c.title for c, _ in catalogues}
    slugs = [c.slug for c, _ in catalogues]

    data = {
        "schema_version": 1,
        "note": (
            "Generated by scripts/build-cci-crosswalk.py. Do not edit by hand. "
            "Every cross-reference is derived by joining the CCIs each SRG rule "
            "cites to the NIST SP 800-53 Rev 5 references DISA publishes for "
            "those CCIs. Control identifiers are OSCAL identifiers from the "
            "pinned catalogue."
        ),
        "inputs": {
            "cci_list": {
                "source": CCI_SOURCE,
                "file": cci_path.name,
                "sha256": cci_digest,
                "version": cci_version,
            },
            "catalogue": {
                "source": CATALOGUE_SOURCE,
                "release": catalogue_version,
                "sha256": catalogue_source["sha256"],
            },
            "baseline": {
                "source": BASELINE_SOURCE,
                "sha256": baseline_source["sha256"],
            },
        },
        "catalogues": data_catalogues,
        "controls": [
            {
                "id": identifier,
                "label": controls[identifier].label,
                "title": controls[identifier].title,
                "high_baseline": controls[identifier].high,
                "rules": {
                    slug: sorted({c.group_id for c in citations[identifier] if c.catalogue == slug})
                    for slug in slugs
                    if any(c.catalogue == slug for c in citations[identifier])
                },
            }
            for identifier in reached
        ],
    }

    pages: dict[Path, str] = {
        DATA: json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        OUTPUT / "README.md": index_page(
            data, controls, citations, reached, slugs, titles,
            cci_version, catalogue_version, unmapped, deprecated, uncited,
        ),
    }
    for identifier in reached:
        pages[OUTPUT / "controls" / (identifier + ".md")] = control_page(
            controls[identifier], citations[identifier], slugs, titles,
            cci_version, catalogue_version,
        )
    return pages


def control_page(
    control: Control,
    cited: list[Citation],
    slugs: list[str],
    titles: dict[str, str],
    cci_version: str,
    catalogue_version: str,
) -> str:
    base = OUTPUT / "controls"
    out: list[str] = []
    out.append("# " + control.label + " " + control.title)
    out.append("")
    out.append("| | |")
    out.append("| --- | --- |")
    out.append("| Family | " + control.family + " " + control.family_title + " |")
    out.append("| OSCAL ID | `" + control.id + "` |")
    out.append("| High baseline | " + ("Selected" if control.high else "**Not selected**") + " |")
    out.append("| Catalogue | NIST SP 800-53 Rev 5, " + catalogue_version + " |")
    out.append("")

    for slug in slugs:
        rows = [c for c in cited if c.catalogue == slug]
        if not rows:
            continue
        rules = {c.group_id for c in rows}
        out.append("## " + titles[slug])
        out.append("")
        out.append(
            str(len(rules)) + (" rule reaches" if len(rules) == 1 else " rules reach")
            + " this control."
        )
        out.append("")
        out.append("| Group ID | STIG ID | Severity | CCI | DISA reference |")
        out.append("| --- | --- | --- | --- | --- |")
        for c in sorted(rows, key=lambda c: (c.group_id, c.cci)):
            page = srg.OUTPUT / slug / "rules" / (c.group_id + ".md")
            out.append(
                "| [`" + c.group_id + "`](" + rel(page, base) + ") | `"
                + c.stig_id + "` | " + c.category + " | `" + c.cci + "` | "
                + ", ".join(c.references) + " |"
            )
        out.append("")

    out.append("---")
    out.append("")
    out.append(
        "Derived from the DISA CCI list " + cci_version + " by "
        "`scripts/build-cci-crosswalk.py`. The DISA reference is the part of "
        "the control the CCI addresses. Do not edit by hand; edits are "
        "overwritten and the drift check fails."
    )
    out.append("")
    return "\n".join(out)


def index_page(
    data: dict,
    controls: dict[str, Control],
    citations: dict[str, list[Citation]],
    reached: list[str],
    slugs: list[str],
    titles: dict[str, str],
    cci_version: str,
    catalogue_version: str,
    unmapped: list[tuple[str, str, str, str]],
    deprecated: list[tuple[str, str, str]],
    uncited: list[tuple[str, str]],
) -> str:
    out: list[str] = []
    out.append("# SRG to NIST SP 800-53 crosswalk")
    out.append("")
    out.append(
        "Every SRG rule cites one or more CCIs, and the DISA CCI list maps each "
        "CCI to NIST SP 800-53 Rev 5. This crosswalk is the join of the two. "
        "No cross-reference here is hand-authored: each follows from the "
        "pinned sources, and it inherits DISA's judgement, errors included."
    )
    out.append("")
    out.append("| Input | Revision |")
    out.append("| --- | --- |")
    out.append("| DISA CCI list | " + cci_version + " |")
    out.append("| NIST SP 800-53 Rev 5 catalogue | " + catalogue_version + " |")
    for catalogue in data["catalogues"]:
        out.append("| " + catalogue["title"] + " | " + catalogue["release"] + " |")
    out.append("")
    out.append(
        "Each input is pinned by SHA-256 in "
        "[`artifacts/sources.json`](../../artifacts/sources.json), and the "
        "generator refuses to map against one that does not match. The "
        "machine-readable form is [`artifacts/crosswalk.json`](../../artifacts/crosswalk.json)."
    )
    out.append("")

    out.append("## Coverage")
    out.append("")
    out.append("| Catalogue | Rules | CCIs cited | Controls reached | Of which High baseline |")
    out.append("| --- | ---: | ---: | ---: | ---: |")
    for catalogue in data["catalogues"]:
        slug = catalogue["slug"]
        cited = {c["cci"] for r in catalogue["rules"] for c in r["ccis"]}
        mine = [i for i in reached if any(c.catalogue == slug for c in citations[i])]
        out.append(
            "| [" + catalogue["title"] + "](../srg/" + slug + "/README.md) | "
            + str(len(catalogue["rules"])) + " | " + str(len(cited)) + " | "
            + str(len(mine)) + " | "
            + str(sum(controls[i].high for i in mine)) + " |"
        )
    out.append("")

    out.append("## Findings")
    out.append("")
    if not unmapped and not deprecated and not uncited:
        out.append(
            "Every rule cites at least one CCI, and every CCI cited is current "
            "in the CCI list and carries at least one Rev 5 reference."
        )
    else:
        out.append("| Catalogue | Group ID | CCI | Finding |")
        out.append("| --- | --- | --- | --- |")
        for slug, group_id, cci in deprecated:
            out.append("| " + titles[slug] + " | `" + group_id + "` | `" + cci + "` | Deprecated in the CCI list |")
        for slug, group_id, cci, note in unmapped:
            out.append("| " + titles[slug] + " | `" + group_id + "` | `" + cci + "` | " + note + " |")
        for slug, group_id in uncited:
            out.append("| " + titles[slug] + " | `" + group_id + "` | | Cites no CCI |")
    out.append("")

    out.append("## Controls")
    out.append("")
    out.append(
        "Rule counts per catalogue. A control outside the High baseline is "
        "still reached by an SRG; the baseline does not select it."
    )
    out.append("")
    header = "| Control | Title | High |"
    divider = "| --- | --- | :-: |"
    for slug in slugs:
        header += " " + titles[slug] + " |"
        divider += " ---: |"
    out.append(header)
    out.append(divider)
    for identifier in reached:
        control = controls[identifier]
        row = (
            "| [" + control.label + "](controls/" + identifier + ".md) | "
            + control.title.replace("|", "\\|") + " | "
            + ("Yes" if control.high else "No") + " |"
        )
        for slug in slugs:
            count = len({c.group_id for c in citations[identifier] if c.catalogue == slug})
            row += " " + (str(count) if count else "") + " |"
        out.append(row)
    out.append("")
    out.append(
        "Regenerate with `python scripts/build-cci-crosswalk.py`. The weekly "
        "source verification runs `--check`, which fails if the committed "
        "crosswalk no longer matches the pinned sources."
    )
    out.append("")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift without writing; exit non-zero if stale",
    )
    args = parser.parse_args()

    pages = build()

    if args.check:
        stale: list[str] = []
        for path, body in pages.items():
            if not path.exists():
                stale.append("missing: " + rel(path, REPOSITORY))
            elif path.read_text(encoding="utf-8") != body:
                stale.append("differs: " + rel(path, REPOSITORY))
        for existing in OUTPUT.rglob("*.md"):
            if existing not in pages:
                stale.append("orphaned: " + rel(existing, REPOSITORY))
        if stale:
            print("the crosswalk is stale:", file=sys.stderr)
            for line in stale[:40]:
                print("  " + line, file=sys.stderr)
            if len(stale) > 40:
                print("  ... and " + str(len(stale) - 40) + " more", file=sys.stderr)
            print("\nRegenerate: python scripts/build-cci-crosswalk.py", file=sys.stderr)
            return 1
        print("the crosswalk is up to date (" + str(len(pages) - 2) + " controls)")
        return 0

    if OUTPUT.is_dir():
        for existing in OUTPUT.rglob("*.md"):
            if existing not in pages:
                existing.unlink()
    for path, body in pages.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8", newline="\n")
    print("wrote " + str(len(pages)) + " files; " + str(len(pages) - 2) + " controls reached")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
