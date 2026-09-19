"""Hold the committed crosswalk to the revisions it claims to derive from.

A cross-reference is only as good as the revision it names. These checks run
without the source packages, as CI has none: they verify that the crosswalk
records the digests the register pins, that it covers exactly the rules that
were rendered, and that its pages and its data agree. Whether the crosswalk is
what the pinned sources actually produce is checked weekly by
verify-sources.yml, which has the packages.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REGISTER = REPOSITORY / "artifacts" / "sources.json"
DATA = REPOSITORY / "artifacts" / "crosswalk.json"
PAGES = REPOSITORY / "docs" / "crosswalk"
DIGEST = re.compile(r"^[0-9a-f]{64}$")


def register() -> dict[str, dict]:
    return {s["id"]: s for s in json.loads(REGISTER.read_text(encoding="utf-8"))["sources"]}


def crosswalk() -> dict:
    return json.loads(DATA.read_text(encoding="utf-8"))


class RevisionTests(unittest.TestCase):
    def test_a_crosswalk_source_pins_the_file_it_is_read_from(self) -> None:
        for source in register().values():
            if source["role"] != "crosswalk":
                continue
            with self.subTest(source=source["id"]):
                self.assertEqual(source["status"], "pinned")
                self.assertRegex(source["input"]["sha256"], DIGEST)
                self.assertTrue(source["input"]["file"])

    def test_the_crosswalk_names_the_revisions_the_register_pins(self) -> None:
        sources = register()
        inputs = crosswalk()["inputs"]
        cci = sources[inputs["cci_list"]["source"]]
        self.assertEqual(inputs["cci_list"]["sha256"], cci["input"]["sha256"])
        self.assertEqual(inputs["cci_list"]["file"], cci["input"]["file"])
        for key in ("catalogue", "baseline"):
            with self.subTest(input=key):
                self.assertEqual(
                    inputs[key]["sha256"], sources[inputs[key]["source"]]["sha256"]
                )

    def test_each_catalogue_names_the_xccdf_the_register_pins(self) -> None:
        sources = register()
        for catalogue in crosswalk()["catalogues"]:
            source = sources[catalogue["source"]]
            with self.subTest(catalogue=catalogue["slug"]):
                self.assertEqual(catalogue["xccdf"], source["xccdf"]["file"])
                self.assertEqual(catalogue["xccdf_sha256"], source["xccdf"]["sha256"])
                self.assertEqual(catalogue["release"], source["release"])


class CoverageTests(unittest.TestCase):
    def test_every_rendered_catalogue_is_in_the_crosswalk(self) -> None:
        rendered = {s["id"] for s in register().values() if s["rendered"]}
        covered = {c["source"] for c in crosswalk()["catalogues"]}
        self.assertEqual(rendered, covered)

    def test_the_crosswalk_covers_exactly_the_rendered_rules(self) -> None:
        for catalogue in crosswalk()["catalogues"]:
            rules = REPOSITORY / "docs" / "srg" / catalogue["slug"] / "rules"
            on_disk = {p.stem for p in rules.glob("*.md")}
            mapped = {r["group_id"] for r in catalogue["rules"]}
            with self.subTest(catalogue=catalogue["slug"]):
                self.assertEqual(mapped, on_disk)

    def test_the_control_index_agrees_with_the_rules(self) -> None:
        data = crosswalk()
        from_rules: dict[str, dict[str, set[str]]] = {}
        for catalogue in data["catalogues"]:
            for rule in catalogue["rules"]:
                for control in rule["controls"]:
                    from_rules.setdefault(control, {}).setdefault(
                        catalogue["slug"], set()
                    ).add(rule["group_id"])
        from_index = {
            c["id"]: {slug: set(ids) for slug, ids in c["rules"].items()}
            for c in data["controls"]
        }
        self.assertEqual(from_index, from_rules)


class PageTests(unittest.TestCase):
    def test_every_control_has_a_page_and_every_page_a_control(self) -> None:
        controls = {c["id"] for c in crosswalk()["controls"]}
        pages = {p.stem for p in (PAGES / "controls").glob("*.md")}
        self.assertEqual(controls, pages)

    def test_every_control_page_is_linked_from_the_index(self) -> None:
        body = (PAGES / "README.md").read_text(encoding="utf-8")
        linked = set(re.findall(r"\(controls/([^)]+)\.md\)", body))
        pages = {p.stem for p in (PAGES / "controls").glob("*.md")}
        self.assertEqual(linked, pages)

    def test_every_rule_link_on_a_control_page_resolves(self) -> None:
        for page in (PAGES / "controls").glob("*.md"):
            for target in re.findall(r"\]\((\.\./[^)]+\.md)\)", page.read_text(encoding="utf-8")):
                with self.subTest(page=page.name, target=target):
                    self.assertTrue((page.parent / target).resolve().is_file())


if __name__ == "__main__":
    unittest.main()
