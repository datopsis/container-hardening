#!/usr/bin/env python3
"""Verify a published release, as anyone pulling it would.

Run with no registry credentials: what is checked is what the public sees. By
default it checks the highest released version, so every CI run re-verifies
what was actually published rather than trusting the release job's report.
After a release, it checks that version, and that its tag resolves to the
index the release built from the tested images.

For a multi-architecture release it checks the index's keyless signature and
SLSA provenance, and for each architecture's image its signature and attested
bill of materials, each against the release workflow's identity. A release
from before the reference image was built for more than one architecture is a
single image, and is checked as one. Either way the registry must carry no
latest tag.

Usage:
    python tests/release_checks.py --bin BIN_DIR [--evidence evidence/release-latest.json]
    python tests/release_checks.py --bin BIN_DIR --version 0.2.0 --expect-digest sha256:... \\
        --evidence evidence/release-published.json
"""

from __future__ import annotations

import argparse
import hashlib
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
INDEXES = ("application/vnd.oci.image.index.v1+json", "application/vnd.docker.distribution.manifest.list.v2+json")


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(list(args), text=True, capture_output=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--bin", type=Path, required=True)
    parser.add_argument("--version", help="the version to check; the highest released one by default")
    parser.add_argument("--expect-digest", help="the index digest the version's tag must resolve to")
    parser.add_argument("--evidence", type=Path, default=HERE / "evidence" / "release-latest.json")
    args = parser.parse_args()
    cosign = str(args.bin / "cosign")
    results = []

    def record(criterion: str, check_id: str, check: str, passed: bool, detail: str = "", architecture: str | None = None) -> None:
        results.append({"id": check_id, "criterion": criterion, "check": check, "passed": bool(passed), "detail": detail,
                        **({"architecture": architecture} if architecture else {})})
        print(("PASS " if passed else "FAIL ") + criterion + "  " + check + (" [" + architecture + "]" if architecture else "")
              + ("  (" + detail + ")" if detail and not passed else ""))

    def signed(reference: str) -> subprocess.CompletedProcess:
        return run(cosign, "verify", "--certificate-identity-regexp", IDENTITY, "--certificate-oidc-issuer", ISSUER, reference)

    def sbom(reference: str) -> subprocess.CompletedProcess:
        return run(cosign, "verify-attestation", "--type", "spdxjson", "--certificate-identity-regexp", IDENTITY,
                   "--certificate-oidc-issuer", ISSUER, reference)

    listing = run("skopeo", "list-tags", "docker://" + IMAGE)
    tags = json.loads(listing.stdout).get("Tags", []) if listing.returncode == 0 else []
    versions = sorted((t for t in tags if VERSION.match(t)), key=lambda t: tuple(int(p) for p in t.split(".")))
    # Signatures and attestations are stored as sha256-... tags; they are not releases.
    named = [t for t in tags if not t.startswith("sha256-")]
    record("IMG-24", "release.version-tags-only", "the registry carries version tags only, and no latest",
           bool(versions) and all(VERSION.match(t) for t in named), ", ".join(named) or listing.stderr.strip()[-200:])
    version = args.version or (versions[-1] if versions else None)
    if not version or version not in versions:
        record("IMG-24", "release.version-published", "the version is published", False, str(version))
        evidence.write(args.evidence, evidence.subject("generic"), results)
        return 1

    # The digest is of the bytes the registry serves, exactly.
    raw = subprocess.run(["skopeo", "inspect", "--raw", "docker://" + IMAGE + ":" + version], capture_output=True).stdout
    manifest = json.loads(raw)
    digest = "sha256:" + hashlib.sha256(raw).hexdigest()
    top = IMAGE + "@" + digest
    if args.expect_digest:
        record("IMG-24", "release.tag-is-the-built-index", "the version tag resolves to the index the release built",
               digest == args.expect_digest, digest + " is not " + args.expect_digest)

    result = signed(top)
    record("IMG-22", "release.latest-signature", "the release's keyless signature verifies against the release workflow",
           result.returncode == 0, result.stderr.strip()[-200:])
    provenance = run("gh", "attestation", "verify", "oci://" + top, "--repo", REPOSITORY)
    record("IMG-22", "release.latest-provenance", "the release's SLSA provenance verifies", provenance.returncode == 0,
           (provenance.stdout + provenance.stderr).strip()[-200:])

    children = {}
    if manifest.get("mediaType") in INDEXES:
        children = {m["platform"]["architecture"]: m["digest"] for m in manifest["manifests"]
                    if m.get("platform", {}).get("os") == "linux"}
        for architecture, child in sorted(children.items()):
            reference = IMAGE + "@" + child
            result = signed(reference)
            record("IMG-22", "release.child-signature", "the image for this architecture is signed by the release workflow",
                   result.returncode == 0, result.stderr.strip()[-200:], architecture)
            result = sbom(reference)
            # A bill of materials describes one architecture's image; say which.
            record("IMG-21", "release.latest-sbom-attested", "the release's bill of materials is attested and retrievable by digest",
                   result.returncode == 0, result.stderr.strip()[-200:], architecture)
    else:
        inspected = json.loads(run("skopeo", "inspect", "docker://" + top).stdout)
        result = sbom(top)
        record("IMG-21", "release.latest-sbom-attested", "the release's bill of materials is attested and retrievable by digest",
               result.returncode == 0, result.stderr.strip()[-200:], inspected["Architecture"])

    failed = [r for r in results if not r["passed"]]
    evidence.write(args.evidence, evidence.subject("generic"), results,
                   release={"image": top, "version": version, "architectures": children})
    print(version + " " + digest + ": " + str(len(results) - len(failed)) + " passed, " + str(len(failed)) + " failed")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
