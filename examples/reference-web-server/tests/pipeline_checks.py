#!/usr/bin/env python3
"""Read the pipeline that builds and releases the image, and record what it holds.

The pipeline is an input too (IMG-35). This reads the image's workflows and
checks that every action is pinned to a full commit or is this repository's
own at the running commit; that each workflow's default permissions are
read-only; that only the jobs that must write hold write permissions, and only
those they need; that no checkout persists its credentials; that the release
starts only from a version tag on the default branch; and that CI audits the
workflows.

It reads the workflow files as text, a line at a time, relying only on the
indentation GitHub's own examples use, so it needs nothing installed.

Usage:
    python tests/pipeline_checks.py [--evidence evidence/pipeline.json]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

import evidence

HERE = Path(__file__).resolve().parent.parent
REPOSITORY = HERE.parent.parent
WORKFLOWS = REPOSITORY / ".github" / "workflows"
# The image's own workflows, and what each job may write. Nothing else writes.
PIPELINE = {
    "reference-image.yml": {
        "candidate": {"packages"},
        "release": {"packages", "id-token", "attestations"},
        "badges": {"contents"},
    },
    "reference-drift.yml": {},
}
AUDIT = WORKFLOWS / "ci.yml"
USES = re.compile(r"^\s*(?:-\s*)?uses:\s*([^\s#]+)", re.M)
PINNED = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")


def blocks(lines: list[str], indent: int) -> dict[str, list[str]]:
    """The keys at one indentation, each with the lines beneath it."""
    found: dict[str, list[str]] = {}
    current = None
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        depth = len(line) - len(line.lstrip(" "))
        match = re.match(r"^([A-Za-z0-9_-]+):", stripped)
        if depth == indent and match:
            current = match.group(1)
            found[current] = []
        elif depth < indent:
            current = None
        elif current is not None:
            found[current].append(line)
    return found


def permissions(lines: list[str], indent: int) -> dict[str, str] | None:
    """The permissions map at an indentation, or None if it sets none."""
    for i, line in enumerate(lines):
        if re.match(r"^" + " " * indent + r"permissions:\s*$", line):
            granted = {}
            for below in lines[i + 1:]:
                match = re.match(r"^" + " " * (indent + 2) + r"([a-z-]+):\s*(read|write|none)\s*$", below)
                if not match:
                    break
                granted[match.group(1)] = match.group(2)
            return granted
        if re.match(r"^" + " " * indent + r"permissions:\s*(\S+)", line):
            return {"*": line.split(":", 1)[1].strip()}
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--evidence", type=Path, default=HERE / "evidence" / "pipeline.json")
    args = parser.parse_args()
    results = []

    def record(check_id: str, check: str, passed: bool, detail: str = "") -> None:
        results.append({"id": check_id, "criterion": "IMG-35", "check": check, "passed": bool(passed), "detail": detail})
        print(("PASS " if passed else "FAIL ") + "IMG-35  " + check + ("  (" + detail + ")" if detail and not passed else ""))

    unpinned, defaults, excess, persisted = [], [], [], []
    for name, allowed in PIPELINE.items():
        text = (WORKFLOWS / name).read_text(encoding="utf-8")
        lines = text.splitlines()
        for reference in USES.findall(text):
            if not (PINNED.match(reference) or reference.startswith(("$/", "./"))):
                unpinned.append(name + ": " + reference)
        top = permissions(lines, 0)
        if top is None or any(v not in ("read", "none") for v in top.values()):
            defaults.append(name + ": " + str(top))
        jobs = blocks(lines, 0).get("jobs", [])
        for job, body in blocks(jobs, 2).items():
            granted = permissions(body, 4) or {}
            writes = {k for k, v in granted.items() if v == "write" or k == "*"}
            if not writes <= allowed.get(job, set()):
                excess.append(name + " " + job + ": " + ", ".join(sorted(writes - allowed.get(job, set()))))
        for i, line in enumerate(lines):
            if re.search(r"uses:\s*actions/checkout@", line):
                following = "\n".join(lines[i + 1:i + 6])
                if not re.search(r"persist-credentials:\s*false", following):
                    persisted.append(name + " line " + str(i + 1))

    record("pipeline.actions-pinned", "every action is pinned to a full commit, or is this repository's own", not unpinned,
           "; ".join(unpinned))
    record("pipeline.read-only-defaults", "every workflow's default permissions are read-only", not defaults, "; ".join(defaults))
    record("pipeline.writes-where-needed", "only the jobs that must write hold write permissions, and only those they need",
           not excess, "; ".join(excess))
    record("pipeline.no-persisted-credentials", "no checkout persists its credentials", not persisted, "; ".join(persisted))

    release = (WORKFLOWS / "reference-image.yml").read_text(encoding="utf-8")
    job = blocks(blocks(release.splitlines(), 0).get("jobs", []), 2).get("release", [])
    body = "\n".join(job)
    record("pipeline.release-from-tag-on-main", "a release starts only from a version tag, on a commit on the default branch",
           "github.ref_type == 'tag'" in body and "merge-base --is-ancestor" in body)
    audit = AUDIT.read_text(encoding="utf-8")
    record("pipeline.workflows-audited", "CI audits every workflow for security findings",
           bool(re.search(r"uses:\s*zizmorcore/zizmor-action@[0-9a-f]{40}", audit)))

    failed = [r for r in results if not r["passed"]]
    # The pipeline is the same whatever the image is built for.
    evidence.write(args.evidence, evidence.subject("generic"), results)
    print(str(len(results) - len(failed)) + " passed, " + str(len(failed)) + " failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
