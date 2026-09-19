#!/usr/bin/env python3
"""Show that the build refuses what it should, and read the build definition.

The hermetic build is only a control if a defective input stops it. This
builds from a copy of a verified bundle with one RPM tampered with, then with
one missing, then with an extra input, then with another key in place of the
pinned one, and requires each build to fail (IMG-02, IMG-03). It checks that
retrieval runs no package manager, and that each base pulled is the
architecture being built (IMG-03). It also reads
the Containerfile for anything that would fetch during assembly or carry a
credential into image history (IMG-03, IMG-05).

Usage:
    python tests/build_checks.py BUNDLE_DIR [--evidence evidence/build.json]
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import evidence

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

    def record(criterion: str, check_id: str, check: str, passed: bool, detail: str = "") -> None:
        results.append({"id": check_id, "criterion": criterion, "check": check, "passed": bool(passed), "detail": detail})
        print(("PASS " if passed else "FAIL ") + criterion + "  " + check + ("  (" + detail + ")" if detail and not passed else ""))

    containerfile = (HERE / "Containerfile").read_text(encoding="utf-8")
    run_lines = "\n".join(line for line in containerfile.splitlines() if not line.lstrip().startswith("#"))
    fetch = sorted(set(FETCHERS.findall(run_lines)))
    record("IMG-03", "build.no-fetch-in-definition", "the build definition runs no retrieval tool or package manager", not fetch, ", ".join(fetch))
    froms = re.findall(r"^ARG (BUILDER|RUNTIME)=(\S+)", containerfile, re.M)
    pinned = {name: ref for name, ref in froms}
    expected = {name.upper(): "registry.access.redhat.com/" + b["repository"] + "@" + b["digest"] for name, b in LOCK["bases"].items()}
    record("IMG-01", "build.bases-pinned", "every base is referenced by its locked manifest-list digest", pinned == expected, str(pinned))
    record("IMG-05", "build.no-credential-arguments", "no credential-shaped build argument or environment variable", not CREDENTIAL.search(containerfile))
    # Drift automation reports; it must not be able to change the lock (IMG-04).
    drift = (HERE.parent.parent / ".github" / "workflows" / "reference-drift.yml").read_text(encoding="utf-8")
    permissions = re.findall(r"^\s+([a-z-]+):\s*(read|write|none)\s*$", drift, re.M)
    writes = re.search(r"git push|git commit|gh pr create|create-pull-request", drift)
    record("IMG-04", "build.drift-automation-read-only", "drift automation holds only read permission and changes nothing",
           permissions == [("contents", "read")] and not writes, str(permissions))

    # Retrieval fetches what the lock names and resolves nothing (IMG-03): the
    # functions that retrieve run no package manager.
    source = ast.parse((HERE / "scripts" / "acquire.py").read_text(encoding="utf-8"))
    retrieval = [n for n in source.body if isinstance(n, ast.FunctionDef) and n.name in ("fetch", "download")]
    resolvers = sorted({s.value for f in retrieval for s in ast.walk(f)
                        if isinstance(s, ast.Constant) and isinstance(s.value, str)
                        and re.search(r"\b(dnf|microdnf|yum|rpm|repoquery|pip|npm)\b", s.value)})
    record("IMG-03", "build.retrieval-resolves-nothing", "retrieval runs no package manager or resolver",
           len(retrieval) == 2 and not resolvers, ", ".join(resolvers))
    architecture = evidence.host_architecture()
    bases = {name: subprocess.run(["podman", "image", "inspect", "--format", "{{.Architecture}}",
                                   "registry.access.redhat.com/" + b["repository"] + "@" + b["digest"]],
                                  text=True, capture_output=True).stdout.strip()
             for name, b in LOCK["bases"].items()}
    record("IMG-03", "build.bases-native", "each base pulled is the architecture being built",
           all(a == architecture for a in bases.values()), str(bases))

    victim = LOCK["rpms"][architecture][0]["file"]
    key = LOCK["signing"]["keys"][0]["file"]
    with tempfile.TemporaryDirectory() as scratch:
        tampered = Path(scratch) / "tampered"
        shutil.copytree(args.bundle, tampered)
        data = bytearray((tampered / victim).read_bytes())
        data[len(data) // 2] ^= 0xFF
        (tampered / victim).write_bytes(bytes(data))
        result = build(tampered, "reference-web-server:tampered")
        output = result.stdout + result.stderr
        record("IMG-02", "build.tampered-input-refused", "a tampered input stops the build",
               result.returncode != 0 and victim in output and "FAILED" in output, output[-200:])

        missing = Path(scratch) / "missing"
        shutil.copytree(args.bundle, missing)
        (missing / victim).unlink()
        result = build(missing, "reference-web-server:missing")
        output = result.stdout + result.stderr
        # It must fail at the missing file, not for some unrelated reason that
        # would make this check pass without testing anything.
        record("IMG-03", "build.missing-input-refused", "a missing input stops the build rather than being fetched",
               result.returncode != 0 and victim in output and "not exactly the lock" in output, output[-200:])

        extra = Path(scratch) / "extra"
        shutil.copytree(args.bundle, extra)
        (extra / "unlocked.rpm").write_bytes(b"not in the lock")
        result = build(extra, "reference-web-server:extra")
        output = result.stdout + result.stderr
        record("IMG-02", "build.extra-input-refused", "an input the lock does not name stops the build",
               result.returncode != 0 and "unlocked.rpm" in output and "not exactly the lock" in output, output[-200:])

        # Another key under the pinned key's name: the build must not trust it.
        substituted = Path(scratch) / "substituted"
        shutil.copytree(args.bundle, substituted)
        (substituted / key).write_text("-----BEGIN PGP PUBLIC KEY BLOCK-----\n\nnot the pinned key\n-----END PGP PUBLIC KEY BLOCK-----\n")
        result = build(substituted, "reference-web-server:substituted")
        output = result.stdout + result.stderr
        record("IMG-02", "build.other-key-refused", "a signing key other than the pinned one stops the build",
               result.returncode != 0 and key in output and "FAILED" in output, output[-200:])

    failed = [r for r in results if not r["passed"]]
    # The bundle holds this machine's architecture's inputs, and the builds
    # above ran natively on it.
    evidence.write(args.evidence, evidence.subject(evidence.host_architecture()), results)
    print(str(len(results) - len(failed)) + " passed, " + str(len(failed)) + " failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
