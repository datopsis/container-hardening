"""Hold the shape of the source register and the rendered catalogues.

The register is the only thing tying a mapping to a revision. A half-recorded
entry is the dangerous shape: it looks authoritative and identifies nothing.

These checks run without the DISA packages present, because the packages are
not committed and CI does not have them. They verify what is committed — the
register and the generated Markdown — rather than re-parsing the source.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REGISTER = REPOSITORY / "artifacts" / "sources.json"
RENDERED = REPOSITORY / "docs" / "srg"

STATUSES = {"pinned", "unresolved", "unavailable"}
ROLES = {
    "spine",
    "baseline",
    "image-controls",
    "platform-controls",
    "host-controls",
    "process-guide",
    "conditional",
    "cross-reference",
    "not-applicable",
}
REQUIRED = (
    "id", "publisher", "title", "release", "retrieved_on", "url", "sha256",
    "size", "xccdf", "rendered", "status", "role", "license", "redistributable",
)
DIGEST = re.compile(r"^[0-9a-f]{64}$")


def register() -> dict:
    return json.loads(REGISTER.read_text(encoding="utf-8"))


def sources() -> list[dict]:
    return register()["sources"]


class RegisterShapeTests(unittest.TestCase):
    def test_every_source_records_the_fields_a_mapping_needs(self) -> None:
        for source in sources():
            with self.subTest(source=source["id"]):
                for field in REQUIRED:
                    self.assertIn(field, source)
                self.assertIn(source["status"], STATUSES)
                self.assertIn(source["role"], ROLES)
                self.assertIsInstance(source["redistributable"], bool)

    def test_source_ids_are_unique(self) -> None:
        ids = [s["id"] for s in sources()]
        self.assertEqual(len(ids), len(set(ids)))

    def test_a_pinned_source_carries_a_digest_and_an_unpinned_one_does_not(self) -> None:
        for source in sources():
            with self.subTest(source=source["id"]):
                if source["status"] == "pinned":
                    self.assertRegex(source["sha256"] or "", DIGEST)
                    self.assertTrue((source["url"] or "").startswith("https://"))
                    self.assertIsNotNone(source["release"])
                    self.assertIsInstance(source["size"], int)
                else:
                    self.assertIsNone(source["sha256"])
                    self.assertTrue(
                        (source.get("notes") or "").strip(),
                        "an unpinned source must record why it is unpinned",
                    )

    def test_the_spine_and_baseline_are_pinned(self) -> None:
        # Cross-references may lag. The spine may not: without it there is no
        # catalogue to map against at all.
        by_role = {s["role"]: s for s in sources()}
        for role in ("spine", "baseline"):
            self.assertIn(role, by_role)
            self.assertEqual(by_role[role]["status"], "pinned")

    def test_the_image_control_source_is_pinned(self) -> None:
        # Per DoD guidance the GPOS SRG carries image-level controls where no
        # container-specific STIG exists. Every image this standard covers is
        # in that situation, so it is not an optional cross-reference.
        image = [s for s in sources() if s["role"] == "image-controls"]
        self.assertTrue(image, "no source carries image-level controls")
        for source in image:
            self.assertEqual(source["status"], "pinned")

    def test_a_source_ruled_not_applicable_records_the_basis(self) -> None:
        for source in sources():
            if source["role"] != "not-applicable":
                continue
            with self.subTest(source=source["id"]):
                self.assertTrue(
                    (source.get("notes") or "").strip(),
                    "a source ruled not applicable must record why",
                )


class RenderingTests(unittest.TestCase):
    def test_a_rendered_source_points_at_a_committed_index(self) -> None:
        for source in sources():
            rendered = source["rendered"]
            if rendered is None:
                continue
            with self.subTest(source=source["id"]):
                self.assertTrue(
                    (REPOSITORY / rendered).is_file(),
                    f"{source['id']} claims to be rendered at {rendered}, "
                    f"which does not exist",
                )

    def test_a_rendered_source_pins_the_xccdf_it_was_rendered_from(self) -> None:
        # The package digest says what was downloaded. The XCCDF digest says
        # what the committed Markdown actually derives from, which is what a
        # reviewer needs to reproduce it.
        for source in sources():
            if source["rendered"] is None:
                continue
            with self.subTest(source=source["id"]):
                xccdf = source["xccdf"]
                self.assertIsNotNone(xccdf, "a rendered source must pin its XCCDF")
                self.assertRegex(xccdf["sha256"], DIGEST)
                self.assertTrue(xccdf["file"].endswith(".xml"))
                self.assertGreater(xccdf["rules"], 0)

    def test_an_unrendered_source_claims_no_rendered_output(self) -> None:
        rendered_dirs = {p.parent.name for p in RENDERED.glob("*/README.md")}
        claimed = {
            Path(s["rendered"]).parent.name
            for s in sources()
            if s["rendered"] is not None
        }
        self.assertEqual(
            rendered_dirs,
            claimed,
            "the rendered catalogues on disk do not match what the register claims",
        )

    def test_every_rule_page_is_reachable_from_its_index(self) -> None:
        for index in RENDERED.glob("*/README.md"):
            body = index.read_text(encoding="utf-8")
            linked = set(re.findall(r"\(rules/([^)]+)\.md\)", body))
            on_disk = {p.stem for p in (index.parent / "rules").glob("*.md")}
            with self.subTest(catalogue=index.parent.name):
                self.assertEqual(
                    on_disk - linked,
                    set(),
                    "rule pages exist that the index does not link to",
                )
                self.assertEqual(
                    linked - on_disk,
                    set(),
                    "the index links to rule pages that do not exist",
                )

    def test_the_rule_count_in_the_register_matches_what_was_rendered(self) -> None:
        for source in sources():
            if source["rendered"] is None:
                continue
            directory = (REPOSITORY / source["rendered"]).parent
            pages = list((directory / "rules").glob("*.md"))
            with self.subTest(source=source["id"]):
                self.assertEqual(
                    len(pages),
                    source["xccdf"]["rules"],
                    f"{source['id']} records {source['xccdf']['rules']} rules "
                    f"but {len(pages)} pages are committed",
                )


if __name__ == "__main__":
    unittest.main()
