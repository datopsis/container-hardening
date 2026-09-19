"""Hold the hardening profile to its rules, and the worked example to the register.

Each rule is tested by building a profile that breaks it. The worked example is
checked against the live register and baseline, so a release upgrade that makes
its determinations stale fails here, the same way it would in an image repository.
"""

from __future__ import annotations

import copy
import datetime
import importlib.util
import json
import sys
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
EXAMPLE = REPOSITORY / "examples" / "reference-web-server" / "hardening-profile.json"
TODAY = datetime.date(2026, 9, 18)


def load(name: str):
    path = REPOSITORY / "scripts" / (name + ".py")
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


profiles = load("check-profile")
components = load("check-component")


def register() -> dict:
    return json.loads(profiles.REGISTER.read_text(encoding="utf-8"))


def baseline() -> dict:
    return json.loads(profiles.BASELINE.read_text(encoding="utf-8"))


def example() -> dict:
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))


def deviation(**overrides) -> dict:
    entry = {
        "id": "DEV-001",
        "kind": "criterion",
        "target": "IMG-14",
        "reason": "Not yet tested.",
        "compensating": "None.",
        "owner": "Joey",
        "approved_by": "Joey",
        "recorded_on": "2026-09-01",
        "expires_on": "2026-12-01",
    }
    entry.update(overrides)
    return entry


class WorkedExampleTests(unittest.TestCase):
    def test_the_worked_example_passes_against_the_live_register(self) -> None:
        violations, _ = profiles.check(example(), register(), baseline(), TODAY)
        self.assertEqual(violations, [])

    def test_the_worked_example_records_the_application_server_srg_as_not_applicable(self) -> None:
        entry = next(e for e in example()["applicability"] if e["source"] == "disa-application-server-srg")
        self.assertIs(entry["applies"], False)
        self.assertIn("27", entry["basis"])


class ProfileRuleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.profile = example()
        self.register = register()
        self.baseline = baseline()

    def violations(self, today: datetime.date = TODAY) -> list[str]:
        found, _ = profiles.check(self.profile, self.register, self.baseline, today)
        return found

    def assertViolation(self, fragment: str, today: datetime.date = TODAY) -> None:
        found = self.violations(today)
        self.assertTrue(any(fragment in v for v in found), found)

    def test_a_missing_determination_is_a_violation(self) -> None:
        self.profile["applicability"] = self.profile["applicability"][:1]
        self.assertViolation("conditional source with no determination")

    def test_a_stale_determination_is_a_violation(self) -> None:
        self.profile["applicability"][0]["sha256"] = "0" * 64
        self.assertViolation("review it against the current revision")

    def test_a_determination_without_a_basis_is_a_violation(self) -> None:
        self.profile["applicability"][0]["basis"] = " "
        self.assertViolation("basis is required")

    def test_a_non_conditional_source_cannot_be_selected(self) -> None:
        gpos = next(s for s in self.register["sources"] if s["id"] == "disa-gpos-srg")
        self.profile["applicability"].append({
            "source": "disa-gpos-srg", "release": gpos["release"], "sha256": gpos["sha256"],
            "applies": False, "basis": "x", "reviewed_on": "2026-09-18", "reviewed_by": "Joey",
        })
        self.assertViolation("only conditional sources are selected per image")

    def test_an_unpinned_standard_revision_is_a_violation(self) -> None:
        self.profile["standard"]["revision"] = "main"
        self.assertViolation("standard.revision")

    def test_a_valid_deviation_passes(self) -> None:
        self.profile["deviations"] = [deviation()]
        self.assertEqual(self.violations(), [])

    def test_an_expired_deviation_is_a_violation(self) -> None:
        self.profile["deviations"] = [deviation(expires_on="2026-09-17")]
        self.assertViolation("expired on 2026-09-17")

    def test_a_deviation_beyond_its_limit_is_a_violation(self) -> None:
        self.profile["deviations"] = [deviation(recorded_on="2026-09-01", expires_on="2027-06-01")]
        self.assertViolation("the limit for a criterion deviation is 180")

    def test_a_vulnerability_deviation_has_the_tighter_limit_and_a_digest(self) -> None:
        self.profile["deviations"] = [deviation(kind="vulnerability", target="CVE-2026-12345", expires_on="2026-12-15")]
        self.assertViolation("the limit for a vulnerability deviation is 90")
        self.assertViolation("scoped to one image digest")

    def test_a_deviation_from_a_target_is_a_violation(self) -> None:
        self.profile["deviations"] = [deviation(target="IMG-T1")]
        self.assertViolation("nothing to deviate from")

    def test_a_deviation_from_a_research_required_control_is_a_violation(self) -> None:
        undecided = next(c["id"] for c in self.baseline["controls"] if c["origination"] == "research-required")
        self.profile["deviations"] = [deviation(kind="control", target=undecided, origination="not-applicable")]
        self.assertViolation("decide it, do not deviate")

    def test_a_control_deviation_must_state_a_different_origination(self) -> None:
        settled = next(c for c in self.baseline["controls"] if c["origination"] == "image-owned")
        self.profile["deviations"] = [deviation(kind="control", target=settled["id"], origination="image-owned")]
        self.assertViolation("same as the baseline's")

    def test_every_accountability_field_is_required(self) -> None:
        for field in ("reason", "compensating", "owner", "approved_by"):
            with self.subTest(field=field):
                entry = deviation()
                del entry[field]
                self.profile["deviations"] = [entry]
                self.assertViolation(field + " is required")

    def test_deviation_ids_are_unique(self) -> None:
        self.profile["deviations"] = [deviation(), deviation(target="IMG-09")]
        self.assertViolation("id used more than once")


class DeviationHonouredTests(unittest.TestCase):
    """check-component.py honours active deviations and nothing else."""

    def setUp(self) -> None:
        self.baseline = baseline()
        self.settled = next(c for c in self.baseline["controls"] if c["origination"] == "organization-inherited")

    def component(self, origination: str) -> dict:
        role = self.baseline["model"]["originations"][origination]["responsible_role"]
        return {"component-definition": {"components": [{"control-implementations": [{
            "implemented-requirements": [{
                "control-id": self.settled["id"],
                "props": [{"name": "origination", "ns": self.baseline["model"]["namespace"], "value": origination}],
                "responsible-roles": [{"role-id": role}] if role else [],
            }],
        }]}]}}

    def departures(self, deviations: list[dict]) -> list[str]:
        found, _ = components.check(self.component("not-applicable"), self.baseline, None, True, deviations)
        return [v for v in found if "baseline is" in v]

    def test_a_departure_without_a_deviation_is_a_violation(self) -> None:
        self.assertTrue(self.departures([]))

    def test_an_active_control_deviation_permits_the_departure(self) -> None:
        active = deviation(kind="control", target=self.settled["id"], origination="not-applicable")
        self.assertEqual(self.departures(profiles.active_deviations({"deviations": [active]}, TODAY)), [])

    def test_an_expired_control_deviation_does_not(self) -> None:
        expired = deviation(kind="control", target=self.settled["id"], origination="not-applicable", expires_on="2026-09-17")
        self.assertTrue(self.departures(profiles.active_deviations({"deviations": [expired]}, TODAY)))

    def test_a_control_may_not_cite_a_criterion_the_image_deviates_from(self) -> None:
        owned = next(c for c in self.baseline["controls"] if c["origination"] == "image-owned")
        namespace = self.baseline["model"]["namespace"]
        entry = {
            "control-id": owned["id"],
            "props": [{"name": "origination", "ns": namespace, "value": "image-owned"}]
            + [{"name": "criterion", "ns": namespace, "value": c} for c in owned["criteria"]]
            + [{"name": "requirement", "ns": namespace, "value": "L1-IMG-001"},
               {"name": "assessment-method", "ns": namespace, "value": "test"}],
            "responsible-roles": [{"role-id": "image-project"}],
            "remarks": "x",
        }
        document = {"component-definition": {"components": [{"control-implementations": [{"implemented-requirements": [entry]}]}]}}
        deviated = [deviation(target=owned["criteria"][0])]
        found, _ = components.check(document, self.baseline, {"L1-IMG-001"}, True, deviated)
        self.assertTrue(any("records a deviation from" in v for v in found), found)


if __name__ == "__main__":
    unittest.main()
