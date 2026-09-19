#!/usr/bin/env python3
"""Verify the latest published release, as anyone pulling it would.

Every CI run re-checks what was actually published, rather than trusting the
release job's own report: the highest released version's keyless signature,
its attested bill of materials, and its SLSA provenance, each against the
release workflow's identity, and that the registry carries no latest tag.

Usage:
    python tests/release_checks.py --bin BIN_DIR [--evidence evidence/release-latest.json]
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
IMAGE = "ghcr.io/datopsis/reference-web-server"
REPOSITORY = "datopsis/container-hardening"
IDENTITY = r"^https://github\.com/datopsis/container-hardening/\.github/workflows/reference-image\.yml@refs/tags/reference-web-server/v\d+\.\d+\.\d+$"
ISSUER = "https://token.actions.githubusercontent.com"
VERSION = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(list(args), text=True, capture_output=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--bin", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, default=HERE / "evidence" / "release-latest.json")
    args = parser.parse_args()
    cosign = str(args.bin / "cosign")
    results = []

    def record(criterion: str, check: str, passed: bool, detail: str = "") -> None:
        results.append({"criterion": criterion, "check": check, "passed": bool(passed), "detail": detail})
        print(("PASS " if passed else "FAIL ") + criterion + "  " + check + ("  (" + detail + ")" if detail and not passed else ""))

    listing = run("skopeo", "list-tags", "docker://" + IMAGE)
    tags = json.loads(listing.stdout).get("Tags", []) if listing.returncode == 0 else []
    versions = sorted((t for t in tags if VERSION.match(t)), key=lambda t: tuple(int(p) for p in t.split(".")))
    record("IMG-24", "the registry carries version tags only, and no latest", bool(versions) and "latest" not in tags,
           ", ".join(tags) or listing.stderr.strip()[-200:])
    if not versions:
        args.evidence.parent.mkdir(parents=True, exist_ok=True)
        args.evidence.write_text(json.dumps({"results": results}, indent=2) + "\n", encoding="utf-8")
        return 1

    latest = versions[-1]
    digest = json.loads(run("skopeo", "inspect", "docker://" + IMAGE + ":" + latest).stdout)["Digest"]
    subject = IMAGE + "@" + digest
    signature = run(cosign, "verify", "--certificate-identity-regexp", IDENTITY, "--certificate-oidc-issuer", ISSUER, subject)
    record("IMG-22", "the latest release's keyless signature verifies against the release workflow", signature.returncode == 0,
           signature.stderr.strip()[-200:])
    sbom = run(cosign, "verify-attestation", "--type", "spdxjson", "--certificate-identity-regexp", IDENTITY,
               "--certificate-oidc-issuer", ISSUER, subject)
    record("IMG-21", "the latest release's bill of materials is attested and retrievable by digest", sbom.returncode == 0,
           sbom.stderr.strip()[-200:])
    provenance = run("gh", "attestation", "verify", "oci://" + subject, "--repo", REPOSITORY)
    record("IMG-22", "the latest release's SLSA provenance verifies", provenance.returncode == 0,
           (provenance.stdout + provenance.stderr).strip()[-200:])

    failed = [r for r in results if not r["passed"]]
    args.evidence.parent.mkdir(parents=True, exist_ok=True)
    args.evidence.write_text(json.dumps({"image": subject, "version": latest, "results": results}, indent=2) + "\n",
                             encoding="utf-8")
    print(latest + " " + digest + ": " + str(len(results) - len(failed)) + " passed, " + str(len(failed)) + " failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
