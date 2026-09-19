"""Hold a manual review to its rules.

A review evidences a criterion only where the criterion allows one, only by a
code owner, and only until what it reviewed changes. Everything else is an
error, so nothing can be asserted into being met.
"""

from __future__ import annotations

import copy
import datetime
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("reviews", REPOSITORY / "scripts" / "reviews.py")
reviews = importlib.util.module_from_spec(spec)
sys.modules["reviews"] = reviews
spec.loader.exec_module(reviews)
BASELINE = json.loads((REPOSITORY / "artifacts" / "control-baseline.json").read_text(encoding="utf-8"))
TODAY = datetime.date(2026, 9, 20)
OWNER = "@a-code-owner"


class ReviewTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory()
        self.repository = Path(self.scratch.name)
        (self.repository / ".github").mkdir()
        (self.repository / ".github" / "CODEOWNERS").write_text("# owners\n*  " + OWNER + "\n", encoding="utf-8")
        self.subject = self.repository / "lock.json"
        self.subject.write_text('{"locked": true}', encoding="utf-8")
        self.sheet = {
            "schema": reviews.SCHEMA, "schema_version": 1,
            "reviews": [{
                "id": "lock-2026-09-20", "criterion": "IMG-04", "requirements": ["RWS-004"], "method": "examine",
                "subject": {"path": "lock.json", "sha256": hashlib.sha256(self.subject.read_bytes()).hexdigest()},
                "result": True, "reviewed_by": OWNER, "reviewed_on": "2026-09-19",
                "notes": "Read the change that produced the lock.",
            }],
        }

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def check(self, sheet: dict | None = None) -> tuple[list[dict], list[str]]:
        return reviews.check(sheet or self.sheet, self.repository, BASELINE, TODAY)

    def test_a_review_of_a_criterion_that_allows_one_holds(self) -> None:
        results, errors = self.check()
        self.assertEqual(errors, [])
        self.assertEqual(len(results), 1)
        self.assertEqual((results[0]["criterion"], results[0]["passed"], results[0]["architecture"]), ("IMG-04", True, "generic"))
        self.assertIn(OWNER, results[0]["check"])
        self.assertEqual(results[0]["requirements"], ["RWS-004"])

    def test_only_img_04_allows_a_review_today(self) -> None:
        allowed = [c for c, m in BASELINE["criteria"].items() if m.get("manual_review")]
        self.assertEqual(allowed, ["IMG-04"])

    def test_a_review_of_any_other_criterion_is_an_error(self) -> None:
        sheet = copy.deepcopy(self.sheet)
        sheet["reviews"][0]["criterion"] = "IMG-13"
        results, errors = self.check(sheet)
        self.assertEqual(results, [])
        self.assertIn("states no Manual review", errors[0])

    def test_a_reviewer_who_is_not_a_code_owner_is_an_error(self) -> None:
        sheet = copy.deepcopy(self.sheet)
        sheet["reviews"][0]["reviewed_by"] = "@someone-else"
        results, errors = self.check(sheet)
        self.assertEqual(results, [])
        self.assertIn("is not a code owner", errors[0])

    def test_a_review_lapses_when_its_subject_changes(self) -> None:
        self.subject.write_text('{"locked": true, "changed": true}', encoding="utf-8")
        results, errors = self.check()
        self.assertEqual(results, [])
        self.assertIn("has changed since it was reviewed", errors[0])

    def test_a_repository_without_codeowners_has_nobody_to_review(self) -> None:
        (self.repository / ".github" / "CODEOWNERS").unlink()
        results, errors = self.check()
        self.assertEqual(results, [])
        self.assertIn("no CODEOWNERS", errors[0])

    def test_a_review_names_what_was_read_and_when(self) -> None:
        for field, message in (("notes", "must say what was read"), ("result", "result must be true or false")):
            sheet = copy.deepcopy(self.sheet)
            sheet["reviews"][0][field] = "" if field == "notes" else "yes"
            with self.subTest(field=field):
                self.assertIn(message, self.check(sheet)[1][0])
        sheet = copy.deepcopy(self.sheet)
        sheet["reviews"][0]["reviewed_on"] = "2026-12-01"
        self.assertIn("in the future", self.check(sheet)[1][0])

    def test_a_subject_outside_the_repository_is_an_error(self) -> None:
        sheet = copy.deepcopy(self.sheet)
        sheet["reviews"][0]["subject"]["path"] = "../elsewhere.json"
        self.assertIn("must be a file in this repository", self.check(sheet)[1][0])

    def test_the_method_must_be_the_one_the_criterion_allows(self) -> None:
        sheet = copy.deepcopy(self.sheet)
        sheet["reviews"][0]["method"] = "interview"
        self.assertIn("allows review by examine", self.check(sheet)[1][0])


if __name__ == "__main__":
    unittest.main()
