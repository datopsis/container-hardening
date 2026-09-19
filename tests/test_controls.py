"""Hold the control baseline to the standard, and the checker to its rules.

The baseline is generated from the pinned NIST catalogue, which CI does not
have. What CI can do is re-derive every control's origination from what is
committed (the standard, the crosswalk, and the determinations) and compare.
A criterion or expectation edited without regenerating the baseline fails here.

The checker is tested by building component definitions that each break one
rule, because a checker that passes everything looks exactly like one that
works.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import re
import sys
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REGISTER = REPOSITORY / "artifacts" / "sources.json"
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
MODEL = REPOSITORY / "docs" / "CONTROL-MODEL.md"


def load(name: str):
    path = REPOSITORY / "scripts" / (name + ".py")
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


generator = load("build-control-baseline")
checker = load("check-component")


def baseline() -> dict:
    return json.loads(BASELINE.read_text(encoding="utf-8"))


class BaselineTests(unittest.TestCase):
    def test_the_baseline_names_the_revisions_the_register_pins(self) -> None:
        sources = {s["id"]: s for s in json.loads(REGISTER.read_text(encoding="utf-8"))["sources"]}
        for key in ("catalogue", "baseline"):
            recorded = baseline()["inputs"][key]
            with self.subTest(input=key):
                self.assertEqual(recorded["sha256"], sources[recorded["source"]]["sha256"])

    def test_the_committed_baseline_is_what_the_standard_derives(self) -> None:
        data = baseline()
        crosswalk = json.loads(generator.CROSSWALK.read_text(encoding="utf-8"))
        reached = {
            (c["slug"], r["group_id"]): r["controls"]
            for c in crosswalk["catalogues"] for r in c["rules"]
        }
        criteria = generator.parse_standard(generator.CRITERIA, reached)
        expectations = generator.parse_standard(generator.PLATFORM, reached)
        determinations = json.loads(generator.DETERMINATIONS.read_text(encoding="utf-8"))
        controls = [
            generator.Control(
                id=c["id"], label=c["label"], title=c["title"],
                family=c["family"], high=c["high_baseline"],
            )
            for c in data["controls"]
        ]
        derived = {c["id"]: c for c in generator.determine(controls, criteria, expectations, determinations)}
        for committed in data["controls"]:
            with self.subTest(control=committed["id"]):
                self.assertEqual(committed, derived[committed["id"]])

    def test_every_control_carries_the_role_its_origination_requires(self) -> None:
        for control in baseline()["controls"]:
            with self.subTest(control=control["id"]):
                self.assertEqual(control["responsible_role"], generator.ROLES[control["origination"]])

    def test_the_summary_counts_the_controls(self) -> None:
        data = baseline()
        counts: dict[str, int] = {}
        for control in data["controls"]:
            counts[control["origination"]] = counts.get(control["origination"], 0) + 1
        self.assertEqual(data["summary"]["controls"], len(data["controls"]))
        for origination, count in data["summary"]["by_origination"].items():
            self.assertEqual(count, counts.get(origination, 0))

    def test_the_high_baseline_is_complete(self) -> None:
        # 370 is the size of the pinned 5.2.0 High baseline. If the pinned
        # baseline changes, this number is a finding to review, like a digest.
        self.assertEqual(sum(c["high_baseline"] for c in baseline()["controls"]), 370)

    def test_the_model_document_lists_exactly_the_originations(self) -> None:
        body = MODEL.read_text(encoding="utf-8")
        documented = dict(re.findall(r"^\| `([a-z-]+)` \| [^|]+ \| (?:`([a-z-]+)`|none) \|$", body, re.M))
        self.assertEqual(set(documented), set(generator.ROLES))
        for origination, role in documented.items():
            self.assertEqual(role or None, generator.ROLES[origination])


NS = "https://datopsis.example/ns/oscal"


def prop(name: str, value: str) -> dict:
    return {"name": name, "ns": NS, "value": value}


def entry(control: dict) -> dict:
    """A component entry that satisfies the checker for one baseline control."""
    origination = control["origination"]
    if origination == "research-required":
        origination = "not-applicable"
    props = [prop("origination", origination)]
    if origination == "image-owned":
        props += [prop("criterion", c) for c in control["criteria"]]
        props += [prop("requirement", "L1-IMG-001"), prop("assessment-method", "test")]
    role = generator.ROLES[origination]
    return {
        "control-id": control["id"],
        "props": props,
        "responsible-roles": [{"role-id": role}] if role else [],
        "remarks": "Limitations.",
    }


def component(entries: list[dict]) -> dict:
    return {"component-definition": {"components": [{
        "control-implementations": [{"implemented-requirements": entries}],
    }]}}


class CheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.baseline = baseline()
        self.entries = [entry(c) for c in self.baseline["controls"]]
        self.index = {e["control-id"]: e for e in self.entries}
        self.requirements = {"L1-IMG-001"}

    def violations(self, entries: list[dict] | None = None) -> list[str]:
        found, _ = checker.check(component(entries or self.entries), self.baseline, self.requirements)
        return found

    def image_owned(self) -> dict:
        return next(e for e in self.entries if e["props"][0]["value"] == "image-owned")

    def test_a_complete_conforming_component_passes(self) -> None:
        self.assertEqual(self.violations(), [])

    def test_an_absent_control_is_a_violation_unless_incomplete_is_allowed(self) -> None:
        entries = self.entries[1:]
        self.assertTrue(any("absent" in v for v in self.violations(entries)))
        found, warnings = checker.check(component(entries), self.baseline, self.requirements, allow_incomplete=True)
        self.assertEqual(found, [])
        self.assertTrue(any("absent" in w for w in warnings))

    def test_two_originations_are_a_violation(self) -> None:
        self.entries[0]["props"].append(prop("origination", "host-inherited"))
        self.assertTrue(any("exactly one origination" in v for v in self.violations()))

    def test_a_mismatched_role_is_a_violation(self) -> None:
        self.entries[0]["responsible-roles"] = [{"role-id": "nobody"}]
        self.assertTrue(any("requires responsible role" in v for v in self.violations()))

    def test_image_owned_without_a_requirement_pointer_is_a_violation(self) -> None:
        target = self.image_owned()
        target["props"] = [p for p in target["props"] if p["name"] != "requirement"]
        self.assertTrue(any("without a requirement pointer" in v for v in self.violations()))

    def test_a_requirement_the_repository_does_not_state_is_a_violation(self) -> None:
        self.image_owned()["props"].append(prop("requirement", "L9-XXX-999"))
        self.assertTrue(any("not stated by this repository" in v for v in self.violations()))

    def test_image_owned_resting_on_a_target_is_a_violation(self) -> None:
        self.image_owned()["props"].append(prop("criterion", "IMG-T1"))
        self.assertTrue(any("strength of target" in v for v in self.violations()))

    def test_omitting_a_baseline_criterion_is_a_violation(self) -> None:
        target = self.image_owned()
        first = next(p for p in target["props"] if p["name"] == "criterion")
        target["props"].remove(first)
        self.assertTrue(any("does not cite baseline criteria" in v for v in self.violations()))

    def test_an_assessment_method_off_image_owned_is_a_violation(self) -> None:
        target = next(e for e in self.entries if e["props"][0]["value"] == "organization-inherited")
        target["props"].append(prop("assessment-method", "test"))
        self.assertTrue(any("only an image-owned control" in v for v in self.violations()))

    def test_departing_from_a_settled_baseline_is_a_violation(self) -> None:
        target = next(e for e in self.entries if e["props"][0]["value"] == "organization-inherited")
        target["props"][0] = prop("origination", "not-applicable")
        target["responsible-roles"] = []
        self.assertTrue(any("baseline is organization-inherited" in v for v in self.violations()))

    def test_deciding_a_research_required_control_is_allowed(self) -> None:
        # The baseline leaves these to the image, so any valid answer passes.
        undecided = [c["id"] for c in self.baseline["controls"] if c["origination"] == "research-required"]
        self.assertTrue(undecided)
        self.assertEqual(self.index[undecided[0]]["props"][0]["value"], "not-applicable")
        self.assertEqual(self.violations(), [])

    def test_a_malformed_cross_reference_is_a_violation(self) -> None:
        self.entries[0]["props"].append(prop("cross-reference", "no source id"))
        self.assertTrue(any("cross-reference" in v for v in self.violations()))

    def test_a_cross_reference_to_a_rule_that_does_not_exist_is_a_violation(self) -> None:
        rules = checker.rendered_rules()
        self.entries[0]["props"].append(prop("cross-reference", "disa-web-server-srg:V-000000"))
        found, _ = checker.check(component(self.entries), self.baseline, self.requirements, False, rules=rules)
        self.assertTrue(any("names no rule in the rendered disa-web-server-srg" in v for v in found), found)

    def test_a_cross_reference_to_a_real_rule_passes(self) -> None:
        rules = checker.rendered_rules()
        real = sorted(rules["disa-web-server-srg"])[0]
        self.entries[0]["props"].append(prop("cross-reference", "disa-web-server-srg:" + real))
        found, _ = checker.check(component(self.entries), self.baseline, self.requirements, False, rules=rules)
        self.assertEqual(found, [])

    def test_a_duplicated_control_is_a_violation(self) -> None:
        entries = self.entries + [copy.deepcopy(self.entries[0])]
        self.assertTrue(any("more than once" in v for v in self.violations(entries)))


if __name__ == "__main__":
    unittest.main()
