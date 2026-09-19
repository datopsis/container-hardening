"""Hold the evidence contract and the conformance score to their definitions.

Evidence is read strictly: anything malformed, missing, duplicated, or from
the wrong architecture makes it invalid rather than lowering a number. A
criterion is met only with passing evidence and no active deviation, and a
per-architecture criterion only by evidence from that architecture. Release
eligibility is separate from the score, and a vulnerability deviation blocks it.
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


def module(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), REPOSITORY / "scripts" / (name + ".py"))
    loaded = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = loaded
    spec.loader.exec_module(loaded)
    return loaded


score = module("score")
evidence = module("evidence")
BASELINE = json.loads((REPOSITORY / "artifacts" / "control-baseline.json").read_text(encoding="utf-8"))
REQUIRED = {c: m for c, m in BASELINE["criteria"].items() if m["level"] == "required"}
PER_ARCHITECTURE = sorted(c for c, m in REQUIRED.items() if m["scope"] == "architecture")
GENERIC = sorted(c for c, m in REQUIRED.items() if m["scope"] == "generic")
COMMIT = "a" * 40
IMAGE = {"amd64": "sha256:" + "1" * 64, "arm64": "sha256:" + "2" * 64}
PROFILE = {
    "architectures": ["amd64", "arm64"],
    "evidence": [{"file": "runtime.json", "scope": "architecture"}, {"file": "source.json", "scope": "generic"}],
}


def result(criterion: str, passed=True, check_id: str | None = None, **extra) -> dict:
    return {"id": check_id or "check." + criterion.lower(), "criterion": criterion, "check": "x", "passed": passed,
            "detail": "why", **extra}


def document(architecture: str, results: list[dict], **subject) -> dict:
    about = {"source_commit": COMMIT, "ci_run": "https://ci/run/1", "architecture": architecture}
    if architecture in IMAGE:
        about["image_id"] = IMAGE[architecture]
    return {"schema": evidence.SCHEMA, "schema_version": 1, "subject": about | subject, "results": results}


def complete() -> dict[str, dict]:
    """A passing, valid evidence set for both architectures: path -> document."""
    return {
        "evidence-amd64/runtime.json": document("amd64", [result(c) for c in PER_ARCHITECTURE]),
        "evidence-arm64/runtime.json": document("arm64", [result(c) for c in PER_ARCHITECTURE]),
        "evidence-amd64/source.json": document("generic", [result(c) for c in GENERIC if c != "IMG-26"]),
    }


def load(files: dict[str, object], profile: dict = PROFILE) -> evidence.Evidence:
    with tempfile.TemporaryDirectory() as scratch:
        root = Path(scratch)
        for name, content in files.items():
            path = root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content if isinstance(content, str) else json.dumps(content), encoding="utf-8")
        return evidence.load(root, profile, BASELINE)


def errors(files: dict[str, object], profile: dict = PROFILE) -> str:
    return "\n".join(load(files, profile).errors)


def scopes(files: dict[str, object], deviated: set[str] = frozenset(), profile: dict = PROFILE) -> dict:
    loaded = load(files, profile)
    assert loaded.valid, loaded.errors
    results = loaded.results + [result("IMG-26", architecture="generic") | {"architecture": "generic"}]
    return score.score(BASELINE, results, set(deviated), profile["architectures"], profile.get("roles"))


def status(rows: list[dict], criterion: str) -> str:
    return next(r["status"] for r in rows if r["criterion"] == criterion)


class EvidenceTests(unittest.TestCase):
    def test_a_complete_set_is_valid(self) -> None:
        self.assertEqual(load(complete()).errors, [])

    def test_a_string_or_number_is_not_a_result(self) -> None:
        for bad in ("false", "true", 0, 1):
            files = complete()
            files["evidence-amd64/runtime.json"]["results"][0]["passed"] = bad
            with self.subTest(passed=bad):
                self.assertIn("passed must be true, false, or null", errors(files))

    def test_malformed_json_is_an_error_not_a_skip(self) -> None:
        files = complete() | {"evidence-amd64/report.json": "{not json"}
        self.assertIn("not valid JSON", errors(files))

    def test_results_without_a_header_are_refused(self) -> None:
        files = complete() | {"evidence-amd64/old.json": {"results": [result("IMG-13")]}}
        self.assertIn("no evidence header", errors(files))

    def test_a_scanner_report_is_ignored(self) -> None:
        files = complete() | {"evidence-amd64/trivy.json": {"Results": []}, "evidence-amd64/gitleaks.json": []}
        self.assertEqual(errors(files), "")

    def test_an_expected_file_that_is_missing_is_an_error(self) -> None:
        files = complete()
        del files["evidence-arm64/runtime.json"]
        self.assertIn("runtime.json (arm64): expected, and missing", errors(files))

    def test_no_evidence_at_all_is_an_error(self) -> None:
        self.assertIn("no evidence", errors({}))

    def test_an_unexpected_evidence_file_is_an_error(self) -> None:
        files = complete() | {"evidence-amd64/extra.json": document("amd64", [result("IMG-13", check_id="extra.x")])}
        self.assertIn("does not expect", errors(files))

    def test_the_same_file_twice_for_one_architecture_is_a_collision(self) -> None:
        files = complete() | {"elsewhere/runtime.json": document("amd64", [result("IMG-13", check_id="other.x")])}
        self.assertIn("found more than once", errors(files))

    def test_a_check_recorded_twice_is_an_error(self) -> None:
        files = complete()
        files["evidence-amd64/runtime.json"]["results"].append(result("IMG-13", passed=False))
        self.assertIn("also recorded", errors(files))

    def test_an_unknown_criterion_is_an_error(self) -> None:
        files = complete()
        files["evidence-amd64/runtime.json"]["results"].append(result("IMG-99"))
        self.assertIn("not a criterion", errors(files))

    def test_a_skip_must_say_why(self) -> None:
        files = complete()
        files["evidence-amd64/runtime.json"]["results"][0] |= {"passed": None, "detail": ""}
        self.assertIn("must say why", errors(files))

    def test_a_generic_result_cannot_stand_for_an_architecture(self) -> None:
        files = complete()
        files["evidence-amd64/source.json"]["results"].append(result("IMG-13", check_id="source.runtime"))
        self.assertIn("a generic result stands for none", errors(files))

    def test_an_undeclared_architecture_is_an_error(self) -> None:
        profile = PROFILE | {"architectures": ["amd64"]}
        files = complete()
        self.assertIn("must be one of the profile's architectures", errors(files, profile))

    def test_evidence_from_two_images_of_one_architecture_is_an_error(self) -> None:
        profile = copy.deepcopy(PROFILE)
        profile["evidence"].append({"file": "gates.json", "scope": "architecture"})
        files = complete() | {
            "evidence-amd64/gates.json": document("amd64", [result("IMG-25", check_id="gates.x")], image_id="sha256:" + "9" * 64),
            "evidence-arm64/gates.json": document("arm64", [result("IMG-25", check_id="gates.x")]),
        }
        self.assertIn("evidence from different images", errors(files, profile))

    def test_evidence_from_two_commits_is_an_error(self) -> None:
        files = complete()
        files["evidence-arm64/runtime.json"]["subject"]["source_commit"] = "b" * 40
        self.assertIn("more than one commit", errors(files))

    def test_a_role_is_refused_unless_the_profile_declares_roles(self) -> None:
        files = complete()
        files["evidence-amd64/runtime.json"]["subject"]["role"] = "server"
        self.assertIn("declares no roles", errors(files))

    def test_declared_roles_are_required_on_every_subject(self) -> None:
        profile = PROFILE | {"roles": ["server", "volume"]}
        self.assertIn("subject.role must be one of", errors(complete(), profile))


def with_roles() -> dict[str, dict]:
    """A complete set for an image with two roles: each role's runtime file per architecture."""
    files = {"evidence-amd64/source.json": complete()["evidence-amd64/source.json"]}
    for architecture in ("amd64", "arm64"):
        for role in ("server", "worker"):
            files["evidence-" + architecture + "-" + role + "/runtime.json"] = document(
                architecture, [result(c) for c in PER_ARCHITECTURE], role=role)
    return files


ROLES = PROFILE | {"roles": ["server", "worker"]}


class RoleTests(unittest.TestCase):
    def test_a_complete_set_with_roles_is_valid(self) -> None:
        self.assertEqual(errors(with_roles(), ROLES), "")

    def test_each_role_is_expected_on_each_architecture(self) -> None:
        files = with_roles()
        del files["evidence-arm64-worker/runtime.json"]
        self.assertIn("runtime.json (arm64, worker): expected, and missing", errors(files, ROLES))

    def test_a_generic_file_names_no_role(self) -> None:
        files = with_roles()
        files["evidence-amd64/source.json"]["subject"]["role"] = "server"
        self.assertIn("names no role", errors(files, ROLES))

    def test_one_role_does_not_fill_another_roles_gap(self) -> None:
        files = with_roles()
        runtime = files["evidence-amd64-worker/runtime.json"]
        runtime["results"] = [r for r in runtime["results"] if r["criterion"] != "IMG-13"]
        rows = scopes(files, profile=ROLES)
        self.assertEqual(status(rows["amd64"], "IMG-13"), "no evidence")
        self.assertEqual(status(rows["arm64"], "IMG-13"), "met")


class ScoreTests(unittest.TestCase):
    def test_passing_evidence_is_met_on_every_architecture(self) -> None:
        result_scopes = scopes(complete())
        for scope in ("amd64", "arm64", "generic"):
            with self.subTest(scope=scope):
                self.assertTrue(all(r["status"] == "met" for r in result_scopes[scope]))

    def test_the_generic_scope_covers_only_generic_criteria(self) -> None:
        rows = scopes(complete())["generic"]
        self.assertEqual(sorted(r["criterion"] for r in rows), GENERIC)
        self.assertEqual(len(scopes(complete())["amd64"]), len(REQUIRED))

    def test_amd64_does_not_fill_an_arm64_gap(self) -> None:
        files = complete()
        files["evidence-arm64/runtime.json"]["results"] = [
            r for r in files["evidence-arm64/runtime.json"]["results"] if r["criterion"] != "IMG-13"
        ]
        result_scopes = scopes(files)
        self.assertEqual(status(result_scopes["amd64"], "IMG-13"), "met")
        self.assertEqual(status(result_scopes["arm64"], "IMG-13"), "no evidence")

    def test_a_generic_file_may_evidence_one_architecture_by_name(self) -> None:
        files = complete()
        files["evidence-arm64/runtime.json"]["results"] = [
            r for r in files["evidence-arm64/runtime.json"]["results"] if r["criterion"] != "IMG-21"
        ]
        files["evidence-amd64/source.json"]["results"].append(result("IMG-21", check_id="release.sbom", architecture="arm64"))
        self.assertEqual(status(scopes(files)["arm64"], "IMG-21"), "met")

    def test_one_failure_fails_the_criterion(self) -> None:
        files = complete()
        files["evidence-arm64/runtime.json"]["results"].append(result("IMG-13", passed=False, check_id="check.second"))
        self.assertEqual(status(scopes(files)["arm64"], "IMG-13"), "failed")

    def test_a_skipped_check_is_not_a_pass(self) -> None:
        files = complete()
        files["evidence-amd64/runtime.json"]["results"].append(result("IMG-32", passed=None, check_id="check.second"))
        self.assertEqual(status(scopes(files)["amd64"], "IMG-32"), "skipped")

    def test_a_deviation_is_not_a_pass(self) -> None:
        self.assertEqual(status(scopes(complete(), {"IMG-13"})["amd64"], "IMG-13"), "deviated")


class EligibilityTests(unittest.TestCase):
    def test_a_criterion_deviation_does_not_block_a_release(self) -> None:
        deviations = [{"id": "DEV-001", "kind": "criterion", "target": "IMG-31"}]
        self.assertEqual(score.blockers(scopes(complete(), {"IMG-31"}), deviations), [])

    def test_a_vulnerability_deviation_blocks_a_release(self) -> None:
        deviations = [{"id": "DEV-002", "kind": "vulnerability", "target": "CVE-2026-0001"}]
        self.assertTrue(score.blockers(scopes(complete()), deviations))

    def test_a_deviation_from_the_vulnerability_gate_blocks_a_release(self) -> None:
        deviations = [{"id": "DEV-003", "kind": "criterion", "target": "IMG-25"}]
        found = score.blockers(scopes(complete(), {"IMG-25"}), deviations)
        self.assertTrue(any("vulnerability gate" in b for b in found))

    def test_missing_evidence_on_one_architecture_blocks_a_release(self) -> None:
        files = complete()
        files["evidence-arm64/runtime.json"]["results"] = files["evidence-arm64/runtime.json"]["results"][1:]
        found = score.blockers(scopes(files), [])
        self.assertEqual(found, [PER_ARCHITECTURE[0] + " on arm64: no evidence"])

    def test_the_badge_states_its_scope_and_message(self) -> None:
        svg = score.badge("hardening arm64", "failing · abc1234 · 2026-09-19", "#cf222e")
        self.assertIn("hardening arm64: failing · abc1234 · 2026-09-19", svg)
        self.assertTrue(svg.startswith("<svg"))


if __name__ == "__main__":
    unittest.main()
