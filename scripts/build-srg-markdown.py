#!/usr/bin/env python3
"""Render a DISA SRG or STIG package into reviewable Markdown.

The source packages are not committed: they are US Government works whose
distribution terms live in the package, and they are large binary-heavy trees.
What is committed is this generated Markdown, one file per rule.

One file per rule is deliberate. When DISA publishes a new release, the diff
then shows exactly which rules changed and how, instead of one unreadable
blob. That diff is the review artifact, and it is the reason the identity of
every source is pinned by digest in artifacts/sources.json.

Usage:
    python scripts/build-srg-markdown.py            # regenerate docs/srg/
    python scripts/build-srg-markdown.py --check    # fail if output is stale
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
OUTPUT = REPOSITORY / "docs" / "srg"
REGISTER = REPOSITORY / "artifacts" / "sources.json"
CROSSWALK = REPOSITORY / "artifacts" / "crosswalk.json"
XCCDF = "{http://checklists.nist.gov/xccdf/1.1}"
CCI_SYSTEM = "http://cyber.mil/cci"

# Where an extracted package may sit. Both are ignored by Git.
SEARCH_ROOTS = (REPOSITORY, REPOSITORY / "sources")

# DISA severity maps onto the category levels an assessor actually uses.
CATEGORY = {"high": "CAT I", "medium": "CAT II", "low": "CAT III"}

# Sections inside the escaped pseudo-XML that <description> carries.
DISCUSSION = re.compile(r"<VulnDiscussion>(.*?)</VulnDiscussion>", re.S)


@dataclass
class Rule:
    group_id: str
    rule_id: str
    stig_id: str
    severity: str
    title: str
    discussion: str
    check: str
    fix: str
    ccis: list[str] = field(default_factory=list)
    legacy: list[str] = field(default_factory=list)

    @property
    def category(self) -> str:
        return CATEGORY.get(self.severity, self.severity)


@dataclass
class Catalogue:
    slug: str
    title: str
    benchmark_id: str
    release: str
    status_date: str
    source_file: str
    rules: list[Rule]


def text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return "".join(node.itertext()).strip()


def paragraphs(raw: str) -> str:
    """Normalise DISA's inconsistent line breaks into Markdown paragraphs."""
    raw = html.unescape(raw or "").replace("\r\n", "\n").replace("\r", "\n")
    raw = re.sub(r"[ \t]+\n", "\n", raw)
    raw = re.sub(r"\n{3,}", "\n\n", raw)
    return raw.strip()


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("security requirements guide", "srg")
    value = value.replace("security technical implementation guide", "stig")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def parse(path: Path) -> Catalogue:
    root = ET.parse(path).getroot()

    release = ""
    for plain in root.findall(XCCDF + "plain-text"):
        if plain.get("id") == "release-info":
            release = (plain.text or "").strip()

    status = root.find(XCCDF + "status")
    rules: list[Rule] = []

    for group in root.findall(XCCDF + "Group"):
        rule = group.find(XCCDF + "Rule")
        if rule is None:
            continue

        described = html.unescape(text(rule.find(XCCDF + "description")))
        discussion = DISCUSSION.search(described)

        check = rule.find(XCCDF + "check")
        check_content = ""
        if check is not None:
            check_content = text(check.find(XCCDF + "check-content"))

        ccis: list[str] = []
        legacy: list[str] = []
        for ident in rule.findall(XCCDF + "ident"):
            value = (ident.text or "").strip()
            if not value:
                continue
            if ident.get("system") == CCI_SYSTEM:
                ccis.append(value)
            else:
                legacy.append(value)

        rules.append(
            Rule(
                group_id=group.get("id", ""),
                rule_id=rule.get("id", ""),
                stig_id=text(rule.find(XCCDF + "version")) or group.get("id", ""),
                severity=rule.get("severity", "unknown"),
                title=text(rule.find(XCCDF + "title")),
                discussion=paragraphs(discussion.group(1) if discussion else ""),
                check=paragraphs(check_content),
                fix=paragraphs(text(rule.find(XCCDF + "fixtext"))),
                ccis=ccis,
                legacy=legacy,
            )
        )

    title = text(root.find(XCCDF + "title"))
    return Catalogue(
        slug=slugify(title),
        title=title,
        benchmark_id=root.get("id", ""),
        release=release,
        status_date=status.get("date", "") if status is not None else "",
        source_file=path.name,
        rules=rules,
    )


def rule_page(
    catalogue: Catalogue, rule: Rule, controls: list[tuple[str, str]]
) -> str:
    out: list[str] = []
    out.append("# " + rule.stig_id)
    out.append("")
    out.append("**" + rule.title + "**")
    out.append("")
    out.append("| | |")
    out.append("| --- | --- |")
    out.append("| Severity | **" + rule.category + "** (" + rule.severity + ") |")
    out.append("| Group ID | `" + rule.group_id + "` |")
    out.append("| Rule ID | `" + rule.rule_id + "` |")
    if rule.ccis:
        out.append("| CCI | " + ", ".join("`" + c + "`" for c in rule.ccis) + " |")
    if rule.legacy:
        out.append("| Legacy IDs | " + ", ".join("`" + c + "`" for c in rule.legacy) + " |")
    if controls:
        out.append(
            "| NIST SP 800-53 Rev 5 | "
            + ", ".join(
                "[" + label + "](../../../crosswalk/controls/" + identifier + ".md)"
                for identifier, label in controls
            )
            + " |"
        )
    out.append("| Source | " + catalogue.title + ", " + catalogue.release + " |")
    out.append("")

    for heading, body in (
        ("Discussion", rule.discussion),
        ("Check", rule.check),
        ("Fix", rule.fix),
    ):
        out.append("## " + heading)
        out.append("")
        out.append(body if body else "_Not stated in the source package._")
        out.append("")

    out.append("---")
    out.append("")
    out.append(
        "Generated from `" + catalogue.source_file + "` by "
        "`scripts/build-srg-markdown.py`. Do not edit by hand; edits are "
        "overwritten and the drift check fails."
    )
    out.append("")
    return "\n".join(out)


def index_page(catalogue: Catalogue) -> str:
    counts: dict[str, int] = {}
    for rule in catalogue.rules:
        counts[rule.category] = counts.get(rule.category, 0) + 1

    out: list[str] = []
    out.append("# " + catalogue.title)
    out.append("")
    out.append(catalogue.release + ". Accepted " + catalogue.status_date + ".")
    out.append("")
    out.append("| | |")
    out.append("| --- | --- |")
    out.append("| Benchmark | `" + catalogue.benchmark_id + "` |")
    out.append("| Rules | **" + str(len(catalogue.rules)) + "** |")
    for category in ("CAT I", "CAT II", "CAT III"):
        if category in counts:
            out.append("| " + category + " | " + str(counts[category]) + " |")
    out.append("")
    out.append(
        "The source package is not committed. Its identity is pinned by "
        "SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json)."
    )
    out.append("")
    out.append("## Rules")
    out.append("")
    out.append(
        "Pages are filed by Group ID, the only identifier DISA guarantees "
        "unique. A STIG ID can repeat across rules."
    )
    out.append("")
    out.append("| Group ID | STIG ID | Severity | Requirement |")
    out.append("| --- | --- | --- | --- |")
    for rule in catalogue.rules:
        title = rule.title.replace("|", "\\|")
        out.append(
            "| [`" + rule.group_id + "`](rules/" + rule.group_id + ".md) | `"
            + rule.stig_id + "` | " + rule.category + " | " + title + " |"
        )
    out.append("")
    return "\n".join(out)


def catalogue_index(catalogues: list[Catalogue]) -> str:
    out: list[str] = []
    out.append("# Rendered requirement catalogues")
    out.append("")
    out.append(
        "Generated from the DISA packages pinned in "
        "[`artifacts/sources.json`](../../artifacts/sources.json). The source "
        "packages themselves are not committed; see "
        "[the sources guide](../SOURCES.md)."
    )
    out.append("")
    out.append("| Catalogue | Release | Rules |")
    out.append("| --- | --- | ---: |")
    for catalogue in catalogues:
        out.append(
            "| [" + catalogue.title + "](" + catalogue.slug + "/README.md) | "
            + catalogue.release + " | " + str(len(catalogue.rules)) + " |"
        )
    out.append("")
    out.append(
        "Regenerate with `python scripts/build-srg-markdown.py`. CI runs "
        "`--check`, which fails if the committed Markdown no longer matches "
        "the packages it was generated from."
    )
    out.append("")
    return "\n".join(out)


def discover() -> list[Path]:
    """Find every extracted XCCDF whose digest the register pins.

    A package that is present but not pinned is skipped, not rendered: the
    weekly verification extracts every pinned package, including those not
    yet rendered, and rendering is a decision recorded in the register rather
    than a side effect of what happens to be on disk. A pinned XCCDF whose
    digest differs is refused outright.
    """
    register = json.loads(REGISTER.read_text(encoding="utf-8"))
    pins = {
        s["xccdf"]["file"]: s["xccdf"]["sha256"]
        for s in register["sources"]
        if s.get("xccdf")
    }

    found: list[Path] = []
    for root in SEARCH_ROOTS:
        if root.is_dir():
            found.extend(sorted(root.glob("U_*/**/*Manual-xccdf.xml")))

    selected: list[Path] = []
    for path in found:
        expected = pins.get(path.name)
        if expected is None:
            print(
                "  skipped  " + path.name + " (its XCCDF is not pinned in the register)",
                file=sys.stderr,
            )
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != expected:
            raise SystemExit(
                path.name + " does not match its pinned digest\n"
                "  pinned   " + expected + "\n"
                "  actual   " + digest + "\n"
                "A replaced release is a finding to review, not a digest to update."
            )
        selected.append(path)
    return selected


def load_crosswalk() -> dict[tuple[str, str], list[tuple[str, str]]]:
    """Read the controls each rule reaches from the committed crosswalk.

    The join of CCIs to 800-53 lives in build-cci-crosswalk.py alone; this
    only reads its output. The crosswalk derives from the XCCDF, not from
    these pages, so run that script first when either changes.
    """
    if not CROSSWALK.is_file():
        return {}
    data = json.loads(CROSSWALK.read_text(encoding="utf-8"))
    labels = {c["id"]: c["label"] for c in data["controls"]}
    return {
        (catalogue["slug"], rule["group_id"]): [
            (identifier, labels[identifier]) for identifier in rule["controls"]
        ]
        for catalogue in data["catalogues"]
        for rule in catalogue["rules"]
    }


def render(catalogues: list[Catalogue]) -> dict[Path, str]:
    crosswalk = load_crosswalk()
    pages: dict[Path, str] = {OUTPUT / "README.md": catalogue_index(catalogues)}
    for catalogue in catalogues:
        base = OUTPUT / catalogue.slug
        pages[base / "README.md"] = index_page(catalogue)
        for rule in catalogue.rules:
            path = base / "rules" / (rule.group_id + ".md")
            # The Group ID is the only identifier DISA guarantees unique. A
            # STIG ID is not: GPOS V3R3 issues SRG-OS-000132-GPOS-00067 as both
            # V-203655 and V-278973. Keying pages on it silently dropped a rule.
            if path in pages:
                raise SystemExit(
                    "duplicate group id " + rule.group_id + " in "
                    + catalogue.title + "; refusing to overwrite a rule page"
                )
            pages[path] = rule_page(
                catalogue, rule, crosswalk.get((catalogue.slug, rule.group_id), [])
            )
    return pages


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift without writing; exit non-zero if stale",
    )
    args = parser.parse_args()

    sources = discover()
    if not sources:
        print(
            "No pinned SRG or STIG package found.\n"
            "Extract a DISA package into the repository root or sources/.\n"
            "Expected a directory matching U_*/ containing *Manual-xccdf.xml\n"
            "whose XCCDF digest is pinned in artifacts/sources.json.\n"
            "See docs/SOURCES.md for which packages this repository uses.",
            file=sys.stderr,
        )
        return 2

    catalogues = sorted((parse(p) for p in sources), key=lambda c: c.title)
    pages = render(catalogues)

    if args.check:
        stale: list[str] = []
        for path, body in pages.items():
            if not path.exists():
                stale.append("missing: " + str(path.relative_to(REPOSITORY)))
            elif path.read_text(encoding="utf-8") != body:
                stale.append("differs: " + str(path.relative_to(REPOSITORY)))

        expected = set(pages)
        for existing in OUTPUT.rglob("*.md"):
            if existing not in expected:
                stale.append("orphaned: " + str(existing.relative_to(REPOSITORY)))

        if stale:
            print(str(OUTPUT.relative_to(REPOSITORY)) + " is stale:", file=sys.stderr)
            for line in stale[:40]:
                print("  " + line, file=sys.stderr)
            if len(stale) > 40:
                print("  ... and " + str(len(stale) - 40) + " more", file=sys.stderr)
            print("\nRegenerate: python scripts/build-srg-markdown.py", file=sys.stderr)
            return 1

        total = sum(len(c.rules) for c in catalogues)
        print(
            str(OUTPUT.relative_to(REPOSITORY))
            + " is up to date ("
            + str(total)
            + " rules)"
        )
        return 0

    for existing in OUTPUT.rglob("*.md"):
        if existing not in pages:
            existing.unlink()

    for path, body in pages.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8", newline="\n")

    for catalogue in catalogues:
        print("  " + str(len(catalogue.rules)).rjust(4) + " rules  " + catalogue.title)
    print("wrote " + str(len(pages)) + " files to " + str(OUTPUT.relative_to(REPOSITORY)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
