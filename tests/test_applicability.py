"""Hold each applicability analysis to the catalogue it describes.

An analysis is evidence an image cites for a determination, so its lists and
counts must be true of the rendered revision, and must still be true after a
release upgrade. A listed rule that no longer exists, or a count that no
longer matches its list, fails here.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
ANALYSES = REPOSITORY / "docs" / "applicability"
EXAMPLE = REPOSITORY / "examples" / "reference-web-server" / "hardening-profile.json"

RULE = re.compile(r"^\| \[`(V-\d+)`\]\(\.\./srg/([^/]+)/rules/\1\.md\) \|", re.M)
SECTION = re.compile(r"^## (.+)$", re.M)
SUMMARY_ROW = re.compile(r"^\| (?:\*\*)?([^|*]+?)(?:\*\*)? \| (?:\*\*)?(\d+)(?:\*\*)?(?: of \d+)? \|$", re.M)


def sections(body: str) -> dict[str, str]:
    found = list(SECTION.finditer(body))
    return {
        m.group(1): body[m.end(): found[i + 1].start() if i + 1 < len(found) else len(body)]
        for i, m in enumerate(found)
    }


class AnalysisTests(unittest.TestCase):
    def analyses(self) -> list[Path]:
        # The README is the guide to choosing sources, not an analysis of one.
        found = sorted(p for p in ANALYSES.glob("*.md") if p.name != "README.md")
        self.assertTrue(found)
        return found

    def test_every_listed_rule_exists_in_the_rendered_catalogue(self) -> None:
        for path in self.analyses():
            for rule, catalogue in RULE.findall(path.read_text(encoding="utf-8")):
                with self.subTest(analysis=path.name, rule=rule):
                    self.assertTrue((REPOSITORY / "docs" / "srg" / catalogue / "rules" / (rule + ".md")).is_file())

    def test_the_summary_counts_are_the_lengths_of_the_lists(self) -> None:
        for path in self.analyses():
            parts = sections(path.read_text(encoding="utf-8"))
            lists = {name: set(r for r, _ in RULE.findall(text)) for name, text in parts.items()}
            lists = {name: rules for name, rules in lists.items() if rules}
            summary = dict(SUMMARY_ROW.findall(parts["Summary"]))
            with self.subTest(analysis=path.name):
                for name, rules in lists.items():
                    self.assertEqual(int(summary[name]), len(rules), name)
                self.assertEqual(int(summary["Any of these"]), len(set().union(*lists.values())))

    def test_the_reference_profile_cites_the_count_its_evidence_supports(self) -> None:
        profile = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        for entry in profile["applicability"]:
            evidence = REPOSITORY / entry["evidence"]
            if evidence.parent != ANALYSES:
                continue
            summary = dict(SUMMARY_ROW.findall(sections(evidence.read_text(encoding="utf-8"))["Summary"]))
            with self.subTest(source=entry["source"]):
                self.assertTrue(entry["basis"].startswith(summary["Any of these"] + " of the "))


if __name__ == "__main__":
    unittest.main()
