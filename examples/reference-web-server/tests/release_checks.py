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

import evidence

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

    def record(criterion: str, check_id: str, check: str, passed: bool, detail: str = "", architecture: str | None = None) -> None:
        results.append({"id": check_id, "criterion": criterion, "check": check, "passed": bool(passed), "detail": detail,
                        **({"architecture": architecture} if architecture else {})})
        print(("PASS " if passed else "FAIL ") + criterion + "  " + check + ("  (" + detail + ")" if detail and not passed else ""))

    listing = run("skopeo", "list-tags", "docker://" + IMAGE)
    tags = json.loads(listing.stdout).get("Tags", []) if listing.returncode == 0 else []
    versions = sorted((t for t in tags if VERSION.match(t)), key=lambda t: tuple(int(p) for p in t.split(".")))
    record("IMG-24", "release.version-tags-only", "the registry carries version tags only, and no latest", bool(versions) and "latest" not in tags,
           ", ".join(tags) or listing.stderr.strip()[-200:])
    if not versions:
        evidence.write(args.evidence, evidence.subject("generic"), results)
        return 1

    latest = versions[-1]
    inspected = json.loads(run("skopeo", "inspect", "docker://" + IMAGE + ":" + latest).stdout)
    digest = inspected["Digest"]
    subject = IMAGE + "@" + digest
    signature = run(cosign, "verify", "--certificate-identity-regexp", IDENTITY, "--certificate-oidc-issuer", ISSUER, subject)
    record("IMG-22", "release.latest-signature", "the latest release's keyless signature verifies against the release workflow", signature.returncode == 0,
           signature.stderr.strip()[-200:])
    sbom = run(cosign, "verify-attestation", "--type", "spdxjson", "--certificate-identity-regexp", IDENTITY,
               "--certificate-oidc-issuer", ISSUER, subject)
    # A bill of materials describes one architecture's image; say which.
    record("IMG-21", "release.latest-sbom-attested", "the latest release's bill of materials is attested and retrievable by digest", sbom.returncode == 0,
           sbom.stderr.strip()[-200:], inspected["Architecture"])
    provenance = run("gh", "attestation", "verify", "oci://" + subject, "--repo", REPOSITORY)
    record("IMG-22", "release.latest-provenance", "the latest release's SLSA provenance verifies", provenance.returncode == 0,
           (provenance.stdout + provenance.stderr).strip()[-200:])

    failed = [r for r in results if not r["passed"]]
    evidence.write(args.evidence, evidence.subject("generic"), results, release={"image": subject, "version": latest})
    print(latest + " " + digest + ": " + str(len(results) - len(failed)) + " passed, " + str(len(failed)) + " failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
