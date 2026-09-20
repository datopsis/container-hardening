#!/usr/bin/env python3
"""Check the form of an image's cyber package, not its truth.

The package is where a person writes what no check can: the architecture, the
trust boundaries, where each control is applied, and what is left open. None of
that can be verified mechanically. What can be verified is that the package is
complete and current, and that nothing raised elsewhere has been quietly left
out of it:

- every section the package must have is present
- every capability the profile declares is discussed
- every diagram in the package is referenced, and every reference resolves
- every control the inspection list flags for review is named
- every control the inspection list raises as worth considering is named
- no placeholder is left behind

It reads; it never edits. A package that passes is well formed, which is not
the same as correct: that is what review is for.

Usage:
    python check-package.py --package package/README.md --profile hardening-profile.json \\
        --inspection-list INSPECTION-LIST.md --statements CONTROL-STATEMENTS.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SECTIONS = (
    "What this image is",
    "Architecture",
    "Data flow and trust boundaries",
    "Where the controls are applied",
    "Controls",
    "Evidence",
    "Deviations and what is open",
    "What this package does not claim",
)
PLACEHOLDERS = re.compile(r"\b(TODO|TBD|FIXME|XXX|Lorem ipsum|to be written)\b", re.I)
LINK = re.compile(r"!?\[[^\]]*\]\(([^)#]+)(?:#[^)]*)?\)")


def check(package: Path, profile: dict, inspection: str, statements: Path | None) -> list[str]:
    problems: list[str] = []
    if not package.is_file():
        return ["the package " + str(package) + " does not exist"]
    body = package.read_text(encoding="utf-8")
    headings = {h.strip() for h in re.findall(r"^##+\s+(.+?)\s*$", body, re.M)}
    for section in SECTIONS:
        if not any(h == section or h.startswith(section) for h in headings):
            problems.append("no section: " + section)

    for capability in profile.get("capabilities", []) or []:
        if capability not in body:
            problems.append("the profile declares " + capability + ", which the package does not discuss")

    referenced = set()
    for target in LINK.findall(body):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (package.parent / target).resolve()
        referenced.add(resolved)
        if not resolved.exists():
            problems.append("links to " + target + ", which does not exist")

    diagrams = sorted((package.parent / "diagrams").glob("*.svg")) if (package.parent / "diagrams").is_dir() else []
    if not diagrams:
        problems.append("no diagrams: a package shows the architecture and its boundaries, it does not only describe them")
    for diagram in diagrams:
        if diagram.resolve() not in referenced:
            problems.append("the diagram " + diagram.name + " is not referenced by the package")

    for flagged in sorted(set(re.findall(r"^\| \[([A-Z][A-Z\-0-9()\.]*)\].*\*\*review:", inspection, re.M))):
        if flagged not in body:
            problems.append("the inspection list flags " + flagged + " for review, which the package does not name")
    consider = re.search(r"^## Worth considering.*?(?=^## |\Z)", inspection, re.M | re.S)
    if consider:
        for raised in sorted(set(re.findall(r"^\| ([A-Z][A-Z\-0-9()\.]*) \|", consider.group(0), re.M))):
            if raised not in body:
                problems.append("the inspection list raises " + raised + " to consider, which the package does not name")

    for match in PLACEHOLDERS.finditer(body):
        problems.append("a placeholder is left in the package: " + match.group(0))

    if statements is not None and statements.is_file():
        unreviewed = statements.read_text(encoding="utf-8").count("**not yet reviewed**")
        if unreviewed and "not yet reviewed" not in body:
            problems.append(str(unreviewed) + " decisions are not yet reviewed, which the package does not say")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--package", type=Path, required=True, help="the package's README")
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--inspection-list", type=Path, required=True)
    parser.add_argument("--statements", type=Path)
    args = parser.parse_args()
    problems = check(
        args.package,
        json.loads(args.profile.read_text(encoding="utf-8")),
        args.inspection_list.read_text(encoding="utf-8") if args.inspection_list.is_file() else "",
        args.statements,
    )
    for problem in problems:
        print("problem: " + problem)
    print(str(len(problems)) + " problems; the package is " + ("well formed" if not problems else "incomplete")
          + ". Whether it is correct is what review decides.")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
