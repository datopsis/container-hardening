"""Hold the adoption worksheets to their rules.

An applicability worksheet decides every rule of a pinned source, one by one,
and the profile's determination must follow from it. A decisions worksheet
decides every control the baseline leaves to the image, with a rationale, an
owner, and a review, and must agree with the component definition.
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


sheets = load("worksheets")
profiles = load("check-profile")
SOURCE = "disa-application-server-srg"


def decided(sheet: dict, decision: str = "not-applicable") -> dict:
    sheet = copy.deepcopy(sheet)
    for row in sheet["rules"]:
        row["decision"], row["basis"] = decision, "The image has nothing this rule governs."
    return sheet


class ApplicabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.sheet = sheets.new_applicability(SOURCE, "test", ["disa-web-server-srg"])

    def test_a_new_worksheet_lists_every_rule_undecided(self) -> None:
        errors, counts = sheets.check_applicability(self.sheet)
        self.assertEqual(counts["undecided"], 137)
        self.assertEqual(len(errors), 137)

    def test_rules_sharing_a_cci_with_another_source_are_suggested(self) -> None:
        suggested = [r for r in self.sheet["rules"] if r["shares_cci_with"]]
        self.assertTrue(suggested)
        self.assertTrue(all(s.startswith("disa-web-server-srg:V-") for r in suggested for s in r["shares_cci_with"]))

    def test_a_fully_decided_worksheet_passes_and_determines_the_source(self) -> None:
        errors, counts = sheets.check_applicability(decided(self.sheet))
        self.assertEqual(errors, [])
        self.assertFalse(sheets.applies(counts))
        sheet = decided(self.sheet)
        sheet["rules"][0]["decision"] = "applies"
        self.assertTrue(sheets.applies(sheets.check_applicability(sheet)[1]))

    def test_a_decision_other_than_applies_needs_a_basis(self) -> None:
        sheet = decided(self.sheet)
        sheet["rules"][0]["basis"] = ""
        self.assertIn("needs a basis", sheets.check_applicability(sheet)[0][0])

    def test_covered_by_must_name_a_real_rule(self) -> None:
        sheet = decided(self.sheet)
        sheet["rules"][0] |= {"decision": "covered-by", "covered_by": ["disa-web-server-srg:V-000000"]}
        self.assertIn("is not a rule of", " ".join(sheets.check_applicability(sheet)[0]))
        sheet["rules"][0]["covered_by"] = []
        self.assertIn("names the rule that covers it", " ".join(sheets.check_applicability(sheet)[0]))

    def test_a_worksheet_against_another_release_is_stale(self) -> None:
        sheet = decided(self.sheet)
        sheet["sha256"] = "0" * 64
        self.assertIn("regenerate it", sheets.check_applicability(sheet)[0][0])

    def test_the_profiles_determination_must_follow_from_the_worksheet(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            base = Path(scratch)
            (base / "sheet.json").write_text(json.dumps(decided(self.sheet)), encoding="utf-8")
            self.assertEqual(profiles.worksheet_problems(base, "sheet.json", False, SOURCE), [])
            self.assertIn("applies must be false", profiles.worksheet_problems(base, "sheet.json", True, SOURCE)[0])
            self.assertIn("is for", profiles.worksheet_problems(base, "sheet.json", False, "disa-web-server-srg")[0])
            self.assertIn("not found", profiles.worksheet_problems(base, "absent.json", False, SOURCE)[0])


class DecisionTests(unittest.TestCase):
    def test_a_new_worksheet_holds_every_control_left_to_the_image(self) -> None:
        baseline = json.loads((REPOSITORY / "artifacts" / "control-baseline.json").read_text(encoding="utf-8"))
        left = {c["id"] for c in baseline["controls"] if c["origination"] == "research-required"}
        sheet = sheets.new_decisions("test")
        self.assertEqual({r["control"] for r in sheet["decisions"]}, left)

    def test_account_controls_warn_against_a_copied_no_accounts(self) -> None:
        rows = {r["control"]: r for r in sheets.new_decisions("test")["decisions"]}
        self.assertIn("S3 access key", rows["ac-2"]["warning"])
        self.assertNotIn("warning", rows["sc-13"])

    def test_the_reference_images_decisions_are_complete_and_unreviewed(self) -> None:
        sheet = json.loads((REFERENCE / "decisions.json").read_text(encoding="utf-8"))
        component = json.loads((REFERENCE / "oscal" / "component-definition.json").read_text(encoding="utf-8"))
        errors, unreviewed = sheets.check_decisions(sheet, component)
        self.assertEqual(errors, [])
        self.assertEqual(len(unreviewed), len(sheet["decisions"]))

    def test_a_decision_needs_an_owner_a_rationale_and_a_statement(self) -> None:
        sheet = json.loads((REFERENCE / "decisions.json").read_text(encoding="utf-8"))
        sheet["decisions"][0] |= {"owner": "", "rationale": "", "statement": ""}
        errors, _ = sheets.check_decisions(sheet)
        for field in ("owner", "rationale", "statement"):
            self.assertTrue(any(field + " is required" in e for e in errors), field)

    def test_every_decision_states_how_the_control_is_satisfied(self) -> None:
        sheet = json.loads((REFERENCE / "decisions.json").read_text(encoding="utf-8"))
        for row in sheet["decisions"]:
            with self.subTest(control=row["control"]):
                self.assertGreater(len(row["statement"].split()), 12, "a statement says how, not just that")

    def test_a_decision_the_component_contradicts_is_an_error(self) -> None:
        sheet = json.loads((REFERENCE / "decisions.json").read_text(encoding="utf-8"))
        component = json.loads((REFERENCE / "oscal" / "component-definition.json").read_text(encoding="utf-8"))
        sheet["decisions"][0]["origination"] = "deployment-configured"
        errors, _ = sheets.check_decisions(sheet, component)
        self.assertTrue(any("component definition says" in e for e in errors))

    def test_a_reviewed_decision_is_not_listed_as_unreviewed(self) -> None:
        sheet = json.loads((REFERENCE / "decisions.json").read_text(encoding="utf-8"))
        sheet["decisions"][0] |= {"reviewed_by": "a reviewer", "reviewed_on": "2026-09-01"}
        _, unreviewed = sheets.check_decisions(sheet)
        self.assertNotIn(sheet["decisions"][0]["control"], unreviewed)


if __name__ == "__main__":
    unittest.main()
