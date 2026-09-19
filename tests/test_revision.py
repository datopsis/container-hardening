"""Hold the binding between an image, its profile, and the standard's revision.

The workflow that ran, the revision the caller names, and the standard checked
out must be one commit; the profile's revision must be that commit or an
ancestor with no normative change since.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("check_revision", REPOSITORY / "scripts" / "check-revision.py")
revision = importlib.util.module_from_spec(spec)
sys.modules["check_revision"] = revision
spec.loader.exec_module(revision)


class RevisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.scratch = tempfile.TemporaryDirectory()
        self.root = Path(self.scratch.name)
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "test")
        self.git("config", "commit.gpgsign", "false")
        (self.root / "docs" / "standard").mkdir(parents=True)
        self.base = self.commit("docs/standard/criteria.md", "one")

    def tearDown(self) -> None:
        self.scratch.cleanup()

    def git(self, *args: str) -> str:
        return subprocess.run(["git", "-C", str(self.root), *args], text=True, capture_output=True, check=True).stdout.strip()

    def commit(self, path: str, content: str) -> str:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        self.git("add", path)
        self.git("commit", "-q", "-m", path)
        return self.git("rev-parse", "HEAD")

    def test_the_same_commit_holds(self) -> None:
        self.assertEqual(revision.check(self.root, self.base), [])

    def test_an_ancestor_with_no_normative_change_holds(self) -> None:
        self.commit("docs/README.md", "prose")
        self.commit("scripts/tool.py", "tooling")
        self.assertEqual(revision.check(self.root, self.base), [])

    def test_a_normative_change_since_makes_the_profile_stale(self) -> None:
        self.commit("docs/standard/criteria.md", "two")
        found = revision.check(self.root, self.base)
        self.assertEqual(len(found), 1)
        self.assertIn("criteria.md changed", found[0])

    def test_a_short_or_unknown_revision_is_refused(self) -> None:
        self.assertIn("full commit", revision.check(self.root, self.base[:7])[0])
        self.assertIn("not a commit", revision.check(self.root, "0" * 40)[0])

    def test_a_revision_off_the_history_is_refused(self) -> None:
        self.git("checkout", "-q", "-b", "side")
        side = self.commit("other.md", "x")
        self.git("checkout", "-q", "-")
        self.assertIn("not an ancestor", revision.check(self.root, side)[0])

    def test_the_workflow_must_run_from_the_named_commit(self) -> None:
        head = self.git("rev-parse", "HEAD")
        self.assertEqual(revision.check(self.root, self.base, head, head), [])
        other = "f" * 40
        self.assertIn("ran from", revision.check(self.root, self.base, head, other)[0])

    def test_standard_ref_must_be_a_full_commit(self) -> None:
        head = self.git("rev-parse", "HEAD")
        self.assertIn("full 40-character commit", revision.check(self.root, self.base, head[:7], head)[0])

    def test_the_standard_checked_out_must_be_the_named_commit(self) -> None:
        named = self.base
        self.commit("docs/README.md", "later")
        found = revision.check(self.root, self.base, named, named)
        self.assertTrue(any("checked out is at" in f for f in found))


class FixtureTests(unittest.TestCase):
    def test_the_multi_role_fixture_names_the_reference_revision(self) -> None:
        # The self-test judges both against one checkout; bump them together.
        import json
        reference = REPOSITORY / "examples" / "reference-web-server" / "hardening-profile.json"
        fixture = REPOSITORY / "tests" / "fixtures" / "multi-role" / "hardening-profile.json"
        revisions = [json.loads(p.read_text(encoding="utf-8"))["standard"]["revision"] for p in (reference, fixture)]
        self.assertEqual(revisions[0], revisions[1])


if __name__ == "__main__":
    unittest.main()
