"""Hold the conformance score to its definition.

A criterion is met only with passing evidence and no active deviation; a
skipped check is not a pass, a deviation is not a pass, and any failure turns
the badge to failing rather than lowering a number.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("score", REPOSITORY / "scripts" / "score.py")
score = importlib.util.module_from_spec(spec)
sys.modules["score"] = score
spec.loader.exec_module(score)
BASELINE = json.loads((REPOSITORY / "artifacts" / "control-baseline.json").read_text(encoding="utf-8"))


def status(results: dict, deviated: set[str] = frozenset(), criterion: str = "IMG-13") -> str:
    rows = score.score(BASELINE, results, set(deviated))
    return next(r["status"] for r in rows if r["criterion"] == criterion)


def check(passed) -> dict:
    return {"criterion": "IMG-13", "check": "x", "passed": passed}


class ScoreTests(unittest.TestCase):
    def test_passing_evidence_is_met(self) -> None:
        self.assertEqual(status({"IMG-13": [check(True), check(True)]}), "met")

    def test_one_failure_fails_the_criterion(self) -> None:
        self.assertEqual(status({"IMG-13": [check(True), check(False)]}), "failed")

    def test_a_skipped_check_is_not_a_pass(self) -> None:
        self.assertEqual(status({"IMG-13": [check(True), check(None)]}), "skipped")

    def test_a_deviation_is_not_a_pass(self) -> None:
        self.assertEqual(status({"IMG-13": [check(True)]}, {"IMG-13"}), "deviated")

    def test_no_evidence_is_not_a_pass(self) -> None:
        self.assertEqual(status({}), "no evidence")

    def test_only_required_criteria_are_scored(self) -> None:
        rows = score.score(BASELINE, {}, set())
        required = [c for c, v in BASELINE["criteria"].items() if v["level"] == "required"]
        self.assertEqual(sorted(r["criterion"] for r in rows), sorted(required))

    def test_evidence_is_read_from_every_results_file(self) -> None:
        with tempfile.TemporaryDirectory() as scratch:
            directory = Path(scratch)
            (directory / "a.json").write_text(json.dumps({"results": [check(True)]}))
            (directory / "b.json").write_text(json.dumps({"results": [check(False)]}))
            (directory / "c.json").write_text("not json")
            found = score.evidence(directory)
        self.assertEqual(len(found["IMG-13"]), 2)

    def test_the_badge_states_its_message(self) -> None:
        svg = score.badge("hardening", "failing · abc1234", "#cf222e")
        self.assertIn("hardening: failing · abc1234", svg)
        self.assertTrue(svg.startswith("<svg"))


if __name__ == "__main__":
    unittest.main()
