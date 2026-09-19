#!/usr/bin/env python3
"""Check that an image is judged by the revision of the standard it names.

Three things must agree, or a score says nothing about which standard it
measured:

- **The workflow that ran.** Called as a reusable workflow, conformance.yml
  runs from the commit in the caller's `uses:` line, which GitHub reports as
  `job.workflow_sha`. The caller's `standard-ref` input must be that commit,
  in full, and the standard checked out must be at it. Otherwise the checks
  could come from one revision and the criteria from another.
- **The profile.** Its `standard.revision` is the revision the image was last
  assessed against. It must be that commit or an ancestor of it, with no
  change since to what the image is judged by: the criteria, the platform
  expectations, the control baseline, and the source register. A newer
  revision that changed only prose or tooling does not make a profile stale;
  one that changed a criterion does, until someone reassesses.

Needs the standard's full history.

Usage:
    python check-revision.py --profile hardening-profile.json \\
        [--standard-ref SHA --workflow-sha SHA]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
COMMIT = re.compile(r"^[0-9a-f]{40}$")
# What an image is judged by. A change to any of these is a change to the
# standard an assessment was made against.
NORMATIVE = (
    "docs/standard/criteria.md",
    "docs/standard/platform.md",
    "artifacts/control-baseline.json",
    "artifacts/sources.json",
)


def git(repository: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repository), *args], text=True, capture_output=True)


def check(
    repository: Path,
    profile_revision: object,
    standard_ref: str | None = None,
    workflow_sha: str | None = None,
) -> list[str]:
    """Return the reasons the image cannot be judged against this revision."""
    errors: list[str] = []
    head = git(repository, "rev-parse", "HEAD").stdout.strip()
    if not COMMIT.match(head):
        return ["the standard at " + str(repository) + " is not a git checkout; its revision cannot be established"]

    if standard_ref is not None or workflow_sha is not None:
        if not isinstance(standard_ref, str) or not COMMIT.match(standard_ref):
            errors.append("standard-ref must be a full 40-character commit, not " + repr(standard_ref))
        if not isinstance(workflow_sha, str) or not COMMIT.match(workflow_sha):
            errors.append("the workflow's own commit is unknown (" + repr(workflow_sha) + ")")
        elif standard_ref != workflow_sha:
            errors.append("standard-ref is " + str(standard_ref) + ", but the conformance workflow ran from "
                          + workflow_sha + "; call it at the same commit you name")
        if standard_ref and head != standard_ref:
            errors.append("the standard checked out is at " + head + ", not standard-ref " + str(standard_ref))
        if errors:
            return errors

    if not isinstance(profile_revision, str) or not COMMIT.match(profile_revision):
        return ["the profile's standard.revision must be a full commit, not " + repr(profile_revision)]
    if git(repository, "cat-file", "-e", profile_revision + "^{commit}").returncode != 0:
        return ["the profile names " + profile_revision + ", which is not a commit of the standard"
                " (or the checkout is shallow; fetch its full history)"]
    if profile_revision != head and git(repository, "merge-base", "--is-ancestor", profile_revision, head).returncode != 0:
        return ["the profile names " + profile_revision + ", which is not an ancestor of " + head]
    changed = git(repository, "diff", "--name-only", profile_revision, head, "--", *NORMATIVE)
    if changed.returncode != 0:
        return ["cannot compare " + profile_revision + " with " + head + ": " + changed.stderr.strip()]
    if changed.stdout.strip():
        errors.append("the profile was assessed against " + profile_revision[:12] + ", and since then "
                      + ", ".join(changed.stdout.split()) + " changed; reassess and name the newer revision")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--standard-ref")
    parser.add_argument("--workflow-sha")
    args = parser.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    errors = check(REPOSITORY, (profile.get("standard") or {}).get("revision"), args.standard_ref, args.workflow_sha)
    for error in errors:
        print("error: " + error)
    if not errors:
        print("the profile's revision holds against " + git(REPOSITORY, "rev-parse", "HEAD").stdout.strip())
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
