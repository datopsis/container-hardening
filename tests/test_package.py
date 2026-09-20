"""Hold the inspection list and the cyber package to what can be checked.

Which controls an image inspects follows from what it declares; the whole
baseline is listed so a reviewer can walk it. The package's form is checkable
and its truth is not, so the checks here are about completeness: a section
missing, a capability nobody discussed, a diagram nobody referenced, a flagged
control passed over in silence.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REFERENCE = REPOSITORY / "examples" / "reference-web-server"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), REPOSITORY / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


inspection = load("build-inspection-list")
package = load("check-package")
BASELINE = json.loads((REPOSITORY / "artifacts" / "control-baseline.json").read_text(encoding="utf-8"))
MAP = json.loads((REPOSITORY / "artifacts" / "inspection-map.json").read_text(encoding="utf-8"))
PROFILE = json.loads((REFERENCE / "hardening-profile.json").read_text(encoding="utf-8"))
COMPONENT = json.loads((REFERENCE / "oscal" / "component-definition.json").read_text(encoding="utf-8"))


class MapTests(unittest.TestCase):
    def test_every_capability_names_controls_the_baseline_has(self) -> None:
        known = {c["id"] for c in BASELINE["controls"]}
        for capability, entry in MAP["capabilities"].items():
            with self.subTest(capability=capability):
                self.assertTrue(entry["controls"], "a capability brings controls, or it is not one")
                self.assertEqual([c for c in entry["controls"] if c not in known], [])
                self.assertTrue(entry["question"].endswith("?"))
                self.assertTrue(entry["why"])

    def test_a_control_worth_considering_is_one_the_baseline_does_not_select(self) -> None:
        known = {c["id"] for c in BASELINE["controls"]}
        raised = [(c, e["control"]) for c, v in MAP["capabilities"].items() for e in v.get("consider", [])]
        self.assertTrue(raised, "the map raises at least one control outside the baseline")
        for capability, control in raised:
            with self.subTest(capability=capability, control=control):
                self.assertNotIn(control, known, "a control in the baseline belongs in controls, not consider")

    def test_the_documentation_lists_every_capability(self) -> None:
        body = (REPOSITORY / "docs" / "CYBER-PACKAGE.md").read_text(encoding="utf-8")
        adopting = (REPOSITORY / "docs" / "ADOPTING.md").read_text(encoding="utf-8")
        for capability in ("terminates-mutual-tls", "authenticates-clients"):
            self.assertTrue(capability in body or capability in adopting, capability)


class InspectionTests(unittest.TestCase):
    def wanted(self, capabilities: list[str]) -> dict:
        profile = copy.deepcopy(PROFILE) | {"capabilities": capabilities}
        found, problems = inspection.inspect(profile, COMPONENT, BASELINE, MAP)
        self.assertEqual(problems, [])
        return found

    def test_what_the_image_does_decides_the_list(self) -> None:
        plain = self.wanted(["serves-http"])
        with_mtls = self.wanted(["serves-http", "terminates-mutual-tls"])
        self.assertLess(len(plain), len(with_mtls))
        self.assertNotIn("ia-2", plain)
        self.assertIn("ia-2", with_mtls, "verifying a client certificate is authentication")

    def test_the_controls_the_baseline_gives_the_image_are_always_there(self) -> None:
        found = self.wanted(["serves-http"])
        owned = [c["id"] for c in BASELINE["controls"] if c["origination"] == "image-owned"]
        for control in owned:
            self.assertIn(control, found)

    def test_a_capability_flags_a_control_answered_not_applicable(self) -> None:
        # The image answers IA-2 not-applicable; declaring that it authenticates
        # clients must contradict that, not pass quietly.
        found = self.wanted(["serves-http", "authenticates-clients"])
        self.assertIn("authenticates-clients", found["ia-2"].get("review", []))

    def test_an_image_that_declares_nothing_is_reported(self) -> None:
        profile = copy.deepcopy(PROFILE) | {"capabilities": []}
        _, problems = inspection.inspect(profile, COMPONENT, BASELINE, MAP)
        self.assertTrue(any("declares no capabilities" in p for p in problems))

    def test_an_unknown_capability_is_reported(self) -> None:
        profile = copy.deepcopy(PROFILE) | {"capabilities": ["serves-tea"]}
        _, problems = inspection.inspect(profile, COMPONENT, BASELINE, MAP)
        self.assertTrue(any("unknown capability" in p for p in problems))

    def test_the_committed_list_covers_every_control(self) -> None:
        body = (REFERENCE / "INSPECTION-LIST.md").read_text(encoding="utf-8")
        for control in BASELINE["controls"]:
            self.assertIn("](../../docs/assessment/" + control["id"] + ".md)", body, control["id"])


class PackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.body = (REFERENCE / "package" / "README.md").read_text(encoding="utf-8")
        self.inspection = (REFERENCE / "INSPECTION-LIST.md").read_text(encoding="utf-8")

    def check(self, body: str | None = None, profile: dict | None = None, inspection_list: str | None = None) -> list[str]:
        with tempfile.TemporaryDirectory() as scratch:
            root = Path(scratch) / "package"
            (root / "diagrams").mkdir(parents=True)
            for diagram in (REFERENCE / "package" / "diagrams").glob("*.svg"):
                (root / "diagrams" / diagram.name).write_text("<svg/>", encoding="utf-8")
            readme = root / "README.md"
            text = self.body if body is None else body
            # The real package links outside itself; those targets are not copied.
            text = text.replace("](../", "](https://example.invalid/")
            readme.write_text(text, encoding="utf-8")
            return package.check(readme, profile or PROFILE, self.inspection if inspection_list is None else inspection_list, None)

    def test_the_reference_package_is_well_formed(self) -> None:
        self.assertEqual(self.check(), [])

    def test_a_missing_section_is_reported(self) -> None:
        body = self.body.replace("## Data flow and trust boundaries", "## Something else")
        self.assertTrue(any("no section: Data flow" in p for p in self.check(body)))

    def test_a_capability_the_package_never_discusses_is_reported(self) -> None:
        profile = copy.deepcopy(PROFILE) | {"capabilities": ["serves-http", "stores-data"]}
        self.assertTrue(any("stores-data" in p for p in self.check(profile=profile)))

    def test_a_diagram_nobody_references_is_reported(self) -> None:
        body = self.body.replace("![Network: what listens, what it reaches, and who decides who may reach it](diagrams/network.svg)", "")
        self.assertTrue(any("network.svg is not referenced" in p for p in self.check(body)))

    def test_a_flagged_control_the_package_ignores_is_reported(self) -> None:
        flagged = ("| Control | Title | Who carries it | Inspect because | The image's part |\n"
                   "| [AC-7](../../docs/assessment/ac-7.md) | Unsuccessful Logon Attempts | not-applicable | "
                   "authenticates clients | decided **review: authenticates-clients says this applies** |\n")
        problems = self.check(inspection_list=flagged)
        self.assertTrue(any("flags AC-7 for review" in p for p in problems), problems)

    def test_a_placeholder_is_reported(self) -> None:
        self.assertTrue(any("placeholder" in p for p in self.check(self.body + "\n\nTODO: write this up.\n")))

    def test_a_broken_link_is_reported(self) -> None:
        body = self.body.replace("(diagrams/context.svg)", "(diagrams/absent.svg)")
        self.assertTrue(any("does not exist" in p for p in self.check(body)))


if __name__ == "__main__":
    unittest.main()
