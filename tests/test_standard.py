"""Hold the written standard to the catalogues and crosswalk it cites.

The standard is prose, but its citations are claims: that a criterion serves a
given SRG rule, and that the rule reaches a given 800-53 control. A citation
that is wrong reads exactly like one that is right, so these are checked
against the committed crosswalk rather than trusted.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
STANDARD = REPOSITORY / "docs" / "standard"
CRITERIA = STANDARD / "criteria.md"
PLATFORM = STANDARD / "platform.md"
SP800190 = STANDARD / "nist-800-190.md"
CROSSWALK = REPOSITORY / "artifacts" / "crosswalk.json"

HEADING = re.compile(r"^### ((IMG|PLT|HST)-(T?\d+)) (.+)$", re.M)
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
RULE = re.compile(r"\.\./srg/([^/]+)/rules/(V-\d+)\.md")
CONTROL = re.compile(r"\.\./crosswalk/controls/([a-z0-9.-]+)\.md")
ORIGINATIONS = {"deployment-configured", "host-inherited"}

# Every countermeasure in Section 4 of NIST SP 800-190.
COUNTERMEASURES = (
    ["4.1.%d" % n for n in range(1, 6)]
    + ["4.2.%d" % n for n in range(1, 4)]
    + ["4.3.%d" % n for n in range(1, 6)]
    + ["4.4.%d" % n for n in range(1, 6)]
    + ["4.5.%d" % n for n in range(1, 6)]
    + ["4.6"]
)


def sections(path: Path) -> dict[str, str]:
    body = path.read_text(encoding="utf-8")
    found = list(HEADING.finditer(body))
    out: dict[str, str] = {}
    for index, match in enumerate(found):
        end = found[index + 1].start() if index + 1 < len(found) else len(body)
        out[match.group(1)] = body[match.start():end]
    return out


def reached() -> dict[tuple[str, str], set[str]]:
    data = json.loads(CROSSWALK.read_text(encoding="utf-8"))
    return {
        (catalogue["slug"], rule["group_id"]): set(rule["controls"])
        for catalogue in data["catalogues"]
        for rule in catalogue["rules"]
    }


def anchors_line(section: str) -> str:
    match = re.search(r"^- \*\*Anchors:\*\*(.*)$", section, re.M)
    return match.group(1) if match else ""


def slug(heading: str) -> str:
    # GitHub's anchor rule, for the characters these documents use.
    heading = heading.strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def anchors_in(path: Path) -> set[str]:
    return {
        slug(line.lstrip("#"))
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("#")
    }


class CriteriaShapeTests(unittest.TestCase):
    def test_identifiers_are_unique_with_no_gaps(self) -> None:
        # Identifiers are permanent once published, so a criterion added later
        # takes the next number and sits in its topical section; order in the
        # file is not order of number. A gap would mean one was deleted.
        for path, prefixes in ((CRITERIA, ("IMG",)), (PLATFORM, ("PLT", "HST"))):
            ids = [m.group(1) for m in HEADING.finditer(path.read_text(encoding="utf-8"))]
            with self.subTest(document=path.name):
                self.assertEqual(len(ids), len(set(ids)))
                for prefix in prefixes:
                    numbered = sorted(
                        int(i.split("-")[1]) for i in ids
                        if i.startswith(prefix + "-") and not i.split("-")[1].startswith("T")
                    )
                    self.assertEqual(numbered, list(range(1, len(numbered) + 1)), prefix)
                self.assertTrue(all(i.split("-")[0] in prefixes for i in ids))

    def test_every_required_criterion_states_its_level_test_and_anchors(self) -> None:
        for identifier, section in sections(CRITERIA).items():
            if identifier.startswith("IMG-T"):
                continue
            with self.subTest(criterion=identifier):
                self.assertIn("**Required.**", section)
                self.assertRegex(section, r"(?m)^- \*\*Test:\*\* \S")
                self.assertTrue(anchors_line(section).strip())

    def test_every_platform_expectation_names_the_image_contribution(self) -> None:
        for identifier, section in sections(PLATFORM).items():
            with self.subTest(expectation=identifier):
                self.assertRegex(section, r"(?m)^- \*\*Image contribution:\*\* \S")
                self.assertTrue(anchors_line(section).strip())
                origination = re.search(r"(?m)^- \*\*Origination:\*\* `([a-z-]+)`$", section)
                self.assertIsNotNone(origination, "an expectation must state its origination")
                self.assertIn(origination.group(1), ORIGINATIONS)

    def test_platform_expectations_cite_only_platform_rules(self) -> None:
        # The layers stay apart: a platform expectation anchored to an image
        # rule would be claiming one layer's control on another's behalf.
        for identifier, section in sections(PLATFORM).items():
            for catalogue, _ in RULE.findall(anchors_line(section)):
                with self.subTest(expectation=identifier):
                    self.assertEqual(catalogue, "container-platform-srg")

    def test_image_criteria_cite_only_image_rules(self) -> None:
        for identifier, section in sections(CRITERIA).items():
            for catalogue, _ in RULE.findall(anchors_line(section)):
                with self.subTest(criterion=identifier):
                    self.assertEqual(catalogue, "general-purpose-operating-system-srg")


class SP800190Tests(unittest.TestCase):
    def rows(self) -> dict[str, str]:
        body = SP800190.read_text(encoding="utf-8")
        found: dict[str, str] = {}
        for line in body.splitlines():
            match = re.match(r"^\| §(4\.\d(?:\.\d)?) ", line)
            if match:
                self.assertNotIn(match.group(1), found, "countermeasure listed twice")
                found[match.group(1)] = line
        return found

    def test_every_countermeasure_is_listed(self) -> None:
        self.assertEqual(sorted(self.rows()), sorted(COUNTERMEASURES))

    def test_every_countermeasure_is_implemented_by_something_that_exists(self) -> None:
        known = set(sections(CRITERIA)) | set(sections(PLATFORM))
        for number, row in self.rows().items():
            cited = set(re.findall(r"\[((?:IMG|PLT|HST)-T?\d+)\]", row))
            with self.subTest(countermeasure=number):
                self.assertTrue(cited, "a countermeasure must name what implements it")
                self.assertEqual(cited - known, set())


class AnchorTests(unittest.TestCase):
    def test_each_cited_control_is_one_the_cited_rule_reaches(self) -> None:
        crosswalk = reached()
        for path in (CRITERIA, PLATFORM):
            for identifier, section in sections(path).items():
                for citation in anchors_line(section).split(";"):
                    rules = RULE.findall(citation)
                    controls = CONTROL.findall(citation)
                    if not rules:
                        continue
                    with self.subTest(item=identifier, citation=citation.strip()[:60]):
                        self.assertEqual(len(rules), 1, "one rule per citation")
                        self.assertTrue(controls, "a cited rule must name its controls")
                        self.assertIn(rules[0], crosswalk, "rule is not in the crosswalk")
                        self.assertEqual(set(controls), crosswalk[rules[0]])

    def test_an_anchor_without_a_rule_says_so(self) -> None:
        for path in (CRITERIA, PLATFORM):
            for identifier, section in sections(path).items():
                line = anchors_line(section)
                if RULE.search(line):
                    continue
                with self.subTest(item=identifier):
                    self.assertIn("No rendered SRG rule", line)


class LinkTests(unittest.TestCase):
    def test_every_relative_link_resolves(self) -> None:
        documents = (
            list(STANDARD.glob("*.md"))
            + list((REPOSITORY / "docs" / "adr").glob("*.md"))
            + list((REPOSITORY / "docs" / "adoption").glob("*.md"))
            + [
                REPOSITORY / "docs" / "CONTROL-MODEL.md",
                REPOSITORY / "docs" / "TAILORING.md",
                REPOSITORY / "docs" / "controls" / "README.md",
            ]
        )
        for document in documents:
            for target in LINK.findall(document.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                path, _, fragment = target.partition("#")
                resolved = (document.parent / path).resolve() if path else document
                with self.subTest(document=document.name, target=target):
                    self.assertTrue(resolved.exists(), "link target does not exist")
                    if fragment and resolved.suffix == ".md":
                        self.assertIn(fragment, anchors_in(resolved), "anchor does not exist")


if __name__ == "__main__":
    unittest.main()
