#!/usr/bin/env python3
"""Show that the build refuses what it should, and read the build definition.

The hermetic build is only a control if a defective input stops it. This
builds from a copy of a verified bundle with one RPM tampered with, then with
one missing, and requires each build to fail (IMG-02, IMG-03). It also reads
the Containerfile for anything that would fetch during assembly or carry a
credential into image history (IMG-03, IMG-05).

Usage:
    python tests/build_checks.py BUNDLE_DIR [--evidence evidence/build.json]
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LOCK = json.loads((HERE / "lock.json").read_text(encoding="utf-8"))
# A retrieval tool or package manager in command position: at the start of a
# RUN, or after a separator. A path that merely names one, such as the
# /etc/dnf the build deletes, is not an invocation.
FETCHERS = re.compile(r"(?:^\s*RUN\s+|[;&|]\s*|\$\(\s*)(curl|wget|dnf|microdnf|yum|pip3?|npm|go\s+get|git\s+clone)\b", re.M)
CREDENTIAL = re.compile(r"^\s*(ARG|ENV)\s+\S*(PASSWORD|PASSWD|SECRET|TOKEN|API_KEY|PRIVATE_KEY|CREDENTIAL)", re.I | re.M)


def build(bundle: Path, tag: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, str(HERE / "scripts" / "build.py"), str(bundle), "--tag", tag],
                          text=True, capture_output=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--evidence", type=Path, default=HERE / "evidence" / "build.json")
    args = parser.parse_args()
    results = []

    def record(criterion: str, check: str, passed: bool, detail: str = "") -> None:
        results.append({"criterion": criterion, "check": check, "passed": bool(passed), "detail": detail})
        print(("PASS " if passed else "FAIL ") + criterion + "  " + check + ("  (" + detail + ")" if detail and not passed else ""))

    containerfile = (HERE / "Containerfile").read_text(encoding="utf-8")
    run_lines = "\n".join(line for line in containerfile.splitlines() if not line.lstrip().startswith("#"))
    fetch = sorted(set(FETCHERS.findall(run_lines)))
    record("IMG-03", "the build definition runs no retrieval tool or package manager", not fetch, ", ".join(fetch))
    froms = re.findall(r"^ARG (BUILDER|RUNTIME)=(\S+)", containerfile, re.M)
    pinned = {name: ref for name, ref in froms}
    expected = {name.upper(): "registry.access.redhat.com/" + b["repository"] + "@" + b["digest"] for name, b in LOCK["bases"].items()}
    record("IMG-01", "every base is referenced by its locked manifest-list digest", pinned == expected, str(pinned))
    record("IMG-05", "no credential-shaped build argument or environment variable", not CREDENTIAL.search(containerfile))
    # Drift automation reports; it must not be able to change the lock (IMG-04).
    drift = (HERE.parent.parent / ".github" / "workflows" / "reference-drift.yml").read_text(encoding="utf-8")
    permissions = re.findall(r"^\s+([a-z-]+):\s*(read|write|none)\s*$", drift, re.M)
    writes = re.search(r"git push|git commit|gh pr create|create-pull-request", drift)
    record("IMG-04", "drift automation holds only read permission and changes nothing",
           permissions == [("contents", "read")] and not writes, str(permissions))

    victim = LOCK["rpms"][0]["file"]
    with tempfile.TemporaryDirectory() as scratch:
        tampered = Path(scratch) / "tampered"
        shutil.copytree(args.bundle, tampered)
        data = bytearray((tampered / victim).read_bytes())
        data[len(data) // 2] ^= 0xFF
        (tampered / victim).write_bytes(bytes(data))
        result = build(tampered, "reference-web-server:tampered")
        output = result.stdout + result.stderr
        record("IMG-02", "a tampered input stops the build",
               result.returncode != 0 and victim in output and "FAILED" in output, output[-200:])

        missing = Path(scratch) / "missing"
        shutil.copytree(args.bundle, missing)
        (missing / victim).unlink()
        result = build(missing, "reference-web-server:missing")
        output = result.stdout + result.stderr
        # It must fail at the missing file, not for some unrelated reason that
        # would make this check pass without testing anything.
        record("IMG-03", "a missing input stops the build rather than being fetched",
               result.returncode != 0 and victim in output and "No such file" in output, output[-200:])

    failed = [r for r in results if not r["passed"]]
    args.evidence.parent.mkdir(parents=True, exist_ok=True)
    args.evidence.write_text(json.dumps({"passed": len(results) - len(failed), "failed": len(failed), "results": results}, indent=2) + "\n",
                             encoding="utf-8")
    print(str(len(results) - len(failed)) + " passed, " + str(len(failed)) + " failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
