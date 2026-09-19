#!/usr/bin/env python3
"""Build the reference image hermetically from a verified bundle.

The build never reaches the network and never pulls (IMG-03): the bases must
already be present by digest, and every other input comes from BUNDLE_DIR,
which scripts/acquire.py filled and verified. A missing input fails the build
instead of being fetched.

The image is built in Docker format because the OCI image format has no
HEALTHCHECK, which IMG-20 requires.

Usage:
    python scripts/build.py BUNDLE_DIR [--tag reference-web-server:dev]
"""

from __future__ import annotations

import argparse
import hashlib
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LOCK = HERE / "lock.json"


def git(*args: str) -> str:
    return subprocess.run(["git", *args], cwd=HERE, check=True, text=True, capture_output=True).stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bundle", type=Path, help="directory filled by scripts/acquire.py")
    parser.add_argument("--tag", default="reference-web-server:dev")
    parser.add_argument("--version", default="0.0.0-dev")
    args = parser.parse_args()

    revision = git("rev-parse", "HEAD")
    # The creation time is the commit's, not the clock's, so a rebuild of the
    # same commit carries the same label.
    created = datetime.fromtimestamp(int(git("log", "-1", "--format=%ct")), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    lock_sha256 = hashlib.sha256(LOCK.read_bytes()).hexdigest()

    # Towards a reproducible build (IMG-T2): timestamps come from the commit,
    # where this Podman can set them. It does not yet show two builds agree.
    epoch = git("log", "-1", "--format=%ct")
    options = subprocess.run(["podman", "build", "--help"], text=True, capture_output=True).stdout
    reproducible = ["--source-date-epoch", epoch, "--rewrite-timestamp"] if "--rewrite-timestamp" in options else []

    command = [
        "podman", "build",
        *reproducible,
        "--format", "docker",
        "--network", "none",
        "--pull=never",
        "--no-cache",
        "--build-context", "bundle=" + str(args.bundle.resolve()),
        "--build-arg", "REVISION=" + revision,
        "--build-arg", "VERSION=" + args.version,
        "--build-arg", "CREATED=" + created,
        "--build-arg", "LOCK_SHA256=" + lock_sha256,
        "--file", str(HERE / "Containerfile"),
        "--tag", args.tag,
        str(HERE),
    ]
    return subprocess.run(command, env=os.environ | {"SOURCE_DATE_EPOCH": epoch}).returncode


if __name__ == "__main__":
    raise SystemExit(main())
