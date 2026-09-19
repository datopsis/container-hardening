#!/usr/bin/env python3
"""Write evidence for the conformance workflow's self-test.

Evidence shaped for a hardening profile, one directory per architecture as an
image's CI uploads them, either complete and passing or broken in one named
way. For a profile that declares roles and topologies, each architecture's
evidence is written once for every combination, as a multi-role image's CI
would. Every result names the requirement the crosswalk maps its criterion to.
The self-test calls the conformance workflow with each and checks it answers
as docs/EVIDENCE.md says it must.

Cases:
    pass          every expected file, every required criterion passing
    malformed     as pass, with one "passed" written as the string "false"
    failed-check  as pass, with one check failed
    partial       as pass, with one per-architecture criterion unevidenced on the
                  last architecture only
    role-gap      as pass, with one per-architecture criterion unevidenced for
                  the last role and topology on the last architecture only

Usage:
    python tests/conformance_fixtures.py CASE OUT_DIR [--profile PROFILE]
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import subprocess
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REFERENCE = REPOSITORY / "examples" / "reference-web-server"
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
CASES = ("pass", "malformed", "failed-check", "partial", "role-gap")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("case", choices=CASES)
    parser.add_argument("out", type=Path)
    parser.add_argument("--profile", type=Path, default=REFERENCE / "hardening-profile.json")
    args = parser.parse_args()

    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    crosswalk = json.loads((REFERENCE / "requirements-crosswalk.json").read_text(encoding="utf-8"))["criteria"]
    criteria = json.loads(BASELINE.read_text(encoding="utf-8"))["criteria"]
    required = {c: m["scope"] for c, m in criteria.items() if m["level"] == "required" and c != "IMG-26"}
    commit = os.environ.get("GITHUB_SHA") or subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPOSITORY, text=True, capture_output=True, check=True).stdout.strip()
    architectures = profile["architectures"]
    roles = profile.get("roles") or [None]
    topologies = profile.get("topologies") or [None]
    combos = list(itertools.product(roles, topologies))

    def about(architecture: str, role: str | None, topology: str | None) -> dict:
        extra = {"image_id": "sha256:" + ("1" if architecture == "amd64" else "2") * 64} if architecture != "generic" else {}
        extra |= {k: v for k, v in (("role", role), ("topology", topology)) if v}
        return {"source_commit": commit, "ci_run": "conformance self-test", "architecture": architecture, **extra}

    files = {e["file"]: e["scope"] for e in profile["evidence"]}
    for scope in ("architecture", "generic"):
        names = [n for n, s in files.items() if s == scope]
        owned = sorted(c for c, s in required.items() if s == scope)
        # Every file carries at least one result; the rest go to the first.
        share = {name: owned[i::len(names)] for i, name in enumerate(names)}
        places = [(a, r, t) for a in architectures for r, t in combos] if scope == "architecture" else [("generic", None, None)]
        for architecture, role, topology in places:
            for name in names:
                results = [{"id": "fixture." + c.lower(), "criterion": c, "check": "fixture for " + c, "passed": True,
                            "requirements": crosswalk.get(c, [])} for c in share[name]]
                first = architecture == architectures[0] and (role, topology) == combos[0]
                last = architecture == architectures[-1] and (role, topology) == combos[-1]
                if name == names[0]:
                    if args.case == "malformed" and first:
                        results[0]["passed"] = "false"
                    elif args.case == "failed-check" and first:
                        results[0]["passed"] = False
                    # The gap is on the last architecture, with the first complete,
                    # so the first cannot be seen to fill it.
                    elif args.case == "partial" and architecture == architectures[-1]:
                        results = results[1:]
                    # The gap is in one role and topology, with every other complete.
                    elif args.case == "role-gap" and last:
                        results = results[1:]
                directory = "-".join(p for p in ("evidence", architecture, role, topology) if p)
                path = args.out / directory / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps({"schema": "container-hardening/evidence", "schema_version": 1,
                                            "subject": about(architecture, role, topology), "results": results},
                                           indent=2) + "\n", encoding="utf-8")
    print("wrote the " + args.case + " evidence to " + str(args.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
