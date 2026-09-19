#!/usr/bin/env python3
"""Write evidence for the conformance workflow's self-test.

Evidence shaped for the reference image's hardening profile, one directory per
architecture as its CI uploads them, either complete and passing or broken in
one named way. The self-test calls the conformance workflow with each and
checks it answers as docs/EVIDENCE.md says it must.

Cases:
    pass          every expected file, every required criterion passing
    malformed     as pass, with one "passed" written as the string "false"
    failed-check  as pass, with one check failed
    partial       as pass, with one per-architecture criterion unevidenced on the
                  last architecture only

Usage:
    python tests/conformance_fixtures.py CASE OUT_DIR
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
PROFILE = REPOSITORY / "examples" / "reference-web-server" / "hardening-profile.json"
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
CASES = ("pass", "malformed", "failed-check", "partial")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("case", choices=CASES)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()

    profile = json.loads(PROFILE.read_text(encoding="utf-8"))
    criteria = json.loads(BASELINE.read_text(encoding="utf-8"))["criteria"]
    required = {c: m["scope"] for c, m in criteria.items() if m["level"] == "required" and c != "IMG-26"}
    commit = os.environ.get("GITHUB_SHA") or subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPOSITORY, text=True, capture_output=True, check=True).stdout.strip()

    def about(architecture: str) -> dict:
        extra = {"image_id": "sha256:" + ("1" if architecture == "amd64" else "2") * 64} if architecture != "generic" else {}
        return {"source_commit": commit, "ci_run": "conformance self-test", "architecture": architecture, **extra}

    files = {e["file"]: e["scope"] for e in profile["evidence"]}
    for scope in ("architecture", "generic"):
        names = [n for n, s in files.items() if s == scope]
        owned = sorted(c for c, s in required.items() if s == scope)
        # Every file carries at least one result; the rest go to the first.
        share = {name: owned[i::len(names)] for i, name in enumerate(names)}
        for architecture in (profile["architectures"] if scope == "architecture" else ["generic"]):
            for name in names:
                results = [{"id": "fixture." + c.lower(), "criterion": c, "check": "fixture for " + c, "passed": True}
                           for c in share[name]]
                if name == names[0]:
                    if args.case == "malformed" and architecture == profile["architectures"][0]:
                        results[0]["passed"] = "false"
                    elif args.case == "failed-check" and architecture == profile["architectures"][0]:
                        results[0]["passed"] = False
                    # The gap is on the last architecture, with the first complete,
                    # so the first cannot be seen to fill it.
                    elif args.case == "partial" and architecture == profile["architectures"][-1]:
                        results = results[1:]
                path = args.out / ("evidence-" + architecture) / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps({"schema": "container-hardening/evidence", "schema_version": 1,
                                            "subject": about(architecture), "results": results}, indent=2) + "\n",
                                encoding="utf-8")
    print("wrote the " + args.case + " evidence to " + str(args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
