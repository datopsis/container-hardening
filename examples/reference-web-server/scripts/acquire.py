#!/usr/bin/env python3
"""Retrieve and verify every input the reference image is built from.

This is the only step that touches the network (IMG-03). It pulls the base
images by manifest-list digest, downloads the locked RPMs, and verifies each
against the lock by size and SHA-256 (IMG-02). Signatures are verified during
assembly, against a pinned key, because the key comes from the pinned builder.

A refresh re-resolves everything and rewrites the lock. It never runs in the
build; its output is a change to lock.json, reviewed like any other (IMG-04).

Usage:
    python scripts/acquire.py BUNDLE_DIR             # fetch and verify
    python scripts/acquire.py --refresh              # rewrite lock.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LOCK = HERE / "lock.json"
REGISTRY = "registry.access.redhat.com"
INDEX_TYPES = "application/vnd.oci.image.index.v1+json, application/vnd.docker.distribution.manifest.list.v2+json"


def run(*args: str, capture: bool = False) -> str:
    result = subprocess.run(args, check=True, text=True, capture_output=capture)
    return result.stdout if capture else ""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest_list_digest(repository: str, tag: str) -> str:
    request = urllib.request.Request(
        "https://" + REGISTRY + "/v2/" + repository + "/manifests/" + tag, headers={"Accept": INDEX_TYPES}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return "sha256:" + hashlib.sha256(response.read()).hexdigest()


def reference(base: dict) -> str:
    return REGISTRY + "/" + base["repository"] + "@" + base["digest"]


def in_builder(lock: dict, work: Path, script: str) -> None:
    """Run a script in the pinned builder, with the network, and work mounted."""
    run("podman", "run", "--rm", "--volume", str(work) + ":/work:Z", reference(lock["bases"]["builder"]),
        "bash", "-euo", "pipefail", "-c", script)


def enable(lock: dict, options: str = "") -> str:
    """The shell prefix that enables the locked module streams, if any."""
    streams = " ".join(lock.get("modules", []))
    return ("dnf -q -y " + options + "module enable " + streams + " >/dev/null && ") if streams else ""


def export_runtime(lock: dict, work: Path) -> None:
    container = run("podman", "create", reference(lock["bases"]["runtime"]), capture=True).strip()
    try:
        run("podman", "export", "--output", str(work / "runtime.tar"), container)
    finally:
        run("podman", "rm", "--force", container, capture=True)


def fetch(lock: dict, bundle: Path) -> int:
    for base in lock["bases"].values():
        run("podman", "pull", "--quiet", reference(base), capture=True)
    bundle.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as scratch:
        work = Path(scratch)
        (work / "rpms").mkdir()
        nevras = " ".join(p["nevra"] for p in lock["rpms"])
        # A package from a module stream is hidden until its stream is enabled.
        in_builder(lock, work, enable(lock) + "dnf -q download --destdir=/work/rpms " + nevras)
        problems = []
        for package in lock["rpms"]:
            path = work / "rpms" / package["file"]
            if not path.is_file():
                problems.append(package["file"] + ": not retrieved")
                continue
            if path.stat().st_size != package["size"] or sha256(path) != package["sha256"]:
                problems.append(package["file"] + ": does not match the lock")
                continue
            shutil.copy2(path, bundle / package["file"])
        if problems:
            print("\n".join(problems), file=sys.stderr)
            return 1
    shutil.copy2(LOCK, bundle / "lock.json")
    print("verified " + str(len(lock["rpms"])) + " RPMs and " + str(len(lock["bases"])) + " bases into " + str(bundle))
    return 0


def refresh(lock: dict) -> int:
    for base in lock["bases"].values():
        base["digest"] = manifest_list_digest(base["repository"], base["tag"])
        run("podman", "pull", "--quiet", reference(base), capture=True)
    with tempfile.TemporaryDirectory() as scratch:
        work = Path(scratch)
        (work / "rpms").mkdir()
        export_runtime(lock, work)
        in_builder(lock, work, (
            "mkdir /r && tar -xf /work/runtime.tar -C /r && "
            + enable(lock, "--installroot=/r --releasever=9 --setopt=reposdir=/etc/yum.repos.d ") +
            "dnf -q -y --installroot=/r --releasever=9 --setopt=reposdir=/etc/yum.repos.d "
            "--setopt=install_weak_deps=False --nodocs --downloadonly --downloaddir=/work/rpms install "
            + " ".join(lock["install"]) + " && "
            "sha256sum /etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release > /work/key.sha256 && "
            "for f in /work/rpms/*.rpm; do printf '%s\\t' \"$(basename \"$f\")\"; "
            "rpm -qp --nosignature --qf '%{NAME}\\t%{NEVRA}\\t%{RSAHEADER:pgpsig}\\n' \"$f\"; done > /work/rpms.tsv"
        ))
        wanted = set(lock["install"]) | set(lock["dependencies"])
        rpms, keys = [], set()
        for line in (work / "rpms.tsv").read_text().splitlines():
            filename, name, nevra, signature = line.split("\t")
            if name not in wanted:
                continue
            path = work / "rpms" / filename
            key = signature.rsplit("Key ID ", 1)[-1].strip()
            keys.add(key)
            rpms.append({"name": name, "nevra": nevra, "file": path.name, "size": path.stat().st_size, "sha256": sha256(path), "key_id": key})
        missing = wanted - {r["name"] for r in rpms}
        if missing:
            print("resolved set lacks " + ", ".join(sorted(missing)), file=sys.stderr)
            return 1
        lock["rpms"] = sorted(rpms, key=lambda r: r["name"])
        lock["signing"] = {
            "key_file": "/etc/pki/rpm-gpg/RPM-GPG-KEY-redhat-release",
            "key_file_sha256": (work / "key.sha256").read_text().split()[0],
            "key_ids": sorted(keys),
        }
    lock["refreshed_on"] = datetime.now(timezone.utc).date().isoformat()
    LOCK.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("rewrote lock.json: review the diff before committing it")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bundle", nargs="?", type=Path, help="directory to receive the verified inputs")
    parser.add_argument("--refresh", action="store_true", help="re-resolve every input and rewrite lock.json")
    args = parser.parse_args()
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    if args.refresh:
        return refresh(lock)
    if not args.bundle:
        parser.error("a bundle directory is required")
    return fetch(lock, args.bundle.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
