#!/usr/bin/env python3
"""Retrieve and verify every input the reference image is built from.

This is the only step that touches the network (IMG-03), and it resolves
nothing: it fetches exactly what the lock names, from where the lock says
(IMG-02). The bases are pulled by manifest-list digest, and each is checked to
be the architecture being built. The signing keys and this architecture's RPMs
are downloaded from their locked locations, over HTTPS, from the hosts named
below and no others, following no redirect elsewhere; each is hashed as it
arrives and checked against the lock by size and SHA-256. The bundle is
admitted only once every input has verified, into a directory that did not
exist, so it holds exactly the lock: nothing missing, nothing extra, nothing
left from an earlier run. Package signatures, signers, and source packages are
verified again during assembly, against the fingerprinted keys.

Because it only fetches, it can be repeated from a mirror: the same lock, and
the same digests, verify the result.

A refresh is the one step that resolves. It re-resolves everything, for every
architecture, with the package manager, against that architecture's runtime
base, so it needs no emulation; records each package's location and source
package; and rewrites the lock. It never runs in the build; its output is a
change to lock.json, reviewed like any other (IMG-04).

Usage:
    python scripts/acquire.py BUNDLE_DIR             # fetch and verify
    python scripts/acquire.py --refresh              # rewrite lock.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LOCK = HERE / "lock.json"
REGISTRY = "registry.access.redhat.com"
# The only hosts inputs are fetched from. Anything else, or a redirect to it, is refused.
ALLOWED_HOSTS = {"cdn-ubi.redhat.com", "security.access.redhat.com"}
# The architectures the image is built for, and RPM's name for each.
ARCHITECTURES = {"amd64": "x86_64", "arm64": "aarch64"}
TIMEOUT, ATTEMPTS, CHUNK = 60, 3, 1 << 20
sys.path.insert(0, str(HERE / "tests"))
import evidence  # noqa: E402
INDEX_TYPES = "application/vnd.oci.image.index.v1+json, application/vnd.docker.distribution.manifest.list.v2+json"


def run(*args: str, capture: bool = False) -> str:
    result = subprocess.run(args, check=True, text=True, capture_output=capture)
    return result.stdout if capture else ""


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def allowed(url: str) -> str | None:
    """Why the URL may not be fetched, or None."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme != "https":
        return "not HTTPS"
    if parts.hostname not in ALLOWED_HOSTS:
        return "host " + str(parts.hostname) + " is not allowed"
    if parts.username or parts.password or parts.query or parts.fragment:
        return "carries credentials, a query, or a fragment"
    return None


class Redirects(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to where a locked location could be."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        problem = allowed(newurl)
        if problem:
            raise urllib.error.URLError("redirect to " + newurl + " refused: " + problem)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


OPENER = urllib.request.build_opener(Redirects)


def download(url: str, target: Path, size: int, digest: str) -> str | None:
    """Fetch URL to TARGET, hashing as it arrives. Returns why it failed, or None."""
    problem = allowed(url)
    if problem:
        return problem
    last = ""
    for attempt in range(ATTEMPTS):
        try:
            hasher, received = hashlib.sha256(), 0
            with OPENER.open(url, timeout=TIMEOUT) as response, target.open("wb") as out:
                while chunk := response.read(CHUNK):
                    received += len(chunk)
                    if received > size:
                        return "larger than the lock's " + str(size) + " bytes"
                    hasher.update(chunk)
                    out.write(chunk)
            if received != size or hasher.hexdigest() != digest:
                return "does not match the lock"
            return None
        except (urllib.error.URLError, OSError) as error:
            last = str(error)
            time.sleep(2 ** attempt)
    return "not retrieved: " + last


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


def export_runtime(lock: dict, work: Path, architecture: str) -> None:
    # Creating a container runs nothing, so another architecture's base needs
    # no emulation to be exported.
    container = run("podman", "create", "--platform", "linux/" + architecture,
                    reference(lock["bases"]["runtime"]), capture=True).strip()
    try:
        run("podman", "export", "--output", str(work / "runtime.tar"), container)
    finally:
        run("podman", "rm", "--force", container, capture=True)


def fetch(lock: dict, bundle: Path, architecture: str) -> int:
    if bundle.exists():
        print(str(bundle) + " already exists; a bundle is made fresh, never added to", file=sys.stderr)
        return 1
    problems = []
    for name, base in lock["bases"].items():
        run("podman", "pull", "--quiet", "--platform", "linux/" + architecture, reference(base), capture=True)
        pulled = run("podman", "image", "inspect", "--format", "{{.Architecture}}", reference(base), capture=True).strip()
        if pulled != architecture:
            problems.append(name + " base: pulled " + pulled + ", building " + architecture)
    inputs = [(k["file"], k["url"], k["size"], k["sha256"]) for k in lock["signing"]["keys"]]
    inputs += [(p["file"], p["url"], p["size"], p["sha256"]) for p in lock["rpms"][architecture]]
    bundle.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=".bundle-", dir=bundle.parent))
    try:
        for name, url, size, digest in inputs:
            problem = download(url, staging / name, size, digest)
            if problem:
                problems.append(name + ": " + problem)
        if problems:
            print("\n".join(problems), file=sys.stderr)
            return 1
        shutil.copy2(LOCK, staging / "lock.json")
        # Admitted all at once, and only now that every input has verified.
        os.replace(staging, bundle)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    print("verified " + str(len(lock["rpms"][architecture])) + " " + architecture + " RPMs, "
          + str(len(lock["signing"]["keys"])) + " signing keys, and " + str(len(lock["bases"])) + " bases into " + str(bundle))
    return 0


def refresh(lock: dict) -> int:
    for base in lock["bases"].values():
        base["digest"] = manifest_list_digest(base["repository"], base["tag"])
        run("podman", "pull", "--quiet", reference(base), capture=True)
    resolved, keys = {}, set()
    for architecture, rpm_arch in ARCHITECTURES.items():
        rpms = resolve(lock, architecture, rpm_arch, keys)
        if rpms is None:
            return 1
        resolved[architecture] = rpms
    # Pulling another architecture's base replaced the native one locally.
    for base in lock["bases"].values():
        run("podman", "pull", "--quiet", reference(base), capture=True)
    trusted = set(lock["signing"]["key_ids"])
    if not keys <= trusted:
        print("packages are signed by keys the lock does not pin: " + ", ".join(sorted(keys - trusted))
              + "; pin each by fingerprint under signing.keys first", file=sys.stderr)
        return 1
    lock["rpms"] = resolved
    lock["refreshed_on"] = datetime.now(timezone.utc).date().isoformat()
    LOCK.write_text(json.dumps(lock, indent=2) + "\n", encoding="utf-8", newline="\n")
    print("rewrote lock.json: review the diff before committing it")
    return 0


def resolve(lock: dict, architecture: str, rpm_arch: str, keys: set) -> list[dict] | None:
    """One architecture's install set, resolved against its own runtime base."""
    with tempfile.TemporaryDirectory() as scratch:
        work = Path(scratch)
        (work / "rpms").mkdir()
        export_runtime(lock, work, architecture)
        options = "--forcearch=" + rpm_arch + " --installroot=/r --releasever=9 --setopt=reposdir=/etc/yum.repos.d "
        in_builder(lock, work, (
            "mkdir /r && tar -xf /work/runtime.tar -C /r && "
            + enable(lock, options) +
            "dnf -q -y " + options +
            "--setopt=install_weak_deps=False --nodocs --downloadonly --downloaddir=/work/rpms install "
            + " ".join(lock["install"]) + " && "
            "for f in /work/rpms/*.rpm; do printf '%s\\t' \"$(basename \"$f\")\"; "
            "rpm -qp --nosignature --qf '%{NAME}\\t%{NEVRA}\\t%{RSAHEADER:pgpsig}\\t%{SOURCERPM}\\n' \"$f\"; done > /work/rpms.tsv && "
            "cd /work/rpms && dnf -q " + options + "repoquery --location "
            "$(for f in *.rpm; do rpm -qp --nosignature --qf '%{NEVRA} ' \"$f\"; done) > /work/locations.txt"
        ))
        wanted = set(lock["install"]) | set(lock["dependencies"])
        locations = {u.rsplit("/", 1)[1]: u for u in (work / "locations.txt").read_text().split()}
        rpms = []
        for line in (work / "rpms.tsv").read_text().splitlines():
            filename, name, nevra, signature, source = line.split("\t")
            if name not in wanted:
                continue
            path = work / "rpms" / filename
            key = signature.rsplit("Key ID ", 1)[-1].strip()
            keys.add(key)
            url = locations.get(filename, "")
            if allowed(url):
                print(architecture + ": " + filename + " is not at an allowed location: " + (url or "none found"), file=sys.stderr)
                return None
            rpms.append({"name": name, "nevra": nevra, "file": path.name, "url": url, "size": path.stat().st_size,
                         "sha256": sha256(path), "key_id": key, "source_rpm": source})
        missing = wanted - {r["name"] for r in rpms}
        if missing:
            print(architecture + ": resolved set lacks " + ", ".join(sorted(missing)), file=sys.stderr)
            return None
        return sorted(rpms, key=lambda r: r["name"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bundle", nargs="?", type=Path, help="directory to receive the verified inputs; must not exist")
    parser.add_argument("--refresh", action="store_true", help="re-resolve every input and rewrite lock.json")
    args = parser.parse_args()
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    if args.refresh:
        return refresh(lock)
    if not args.bundle:
        parser.error("a bundle directory is required")
    return fetch(lock, args.bundle.resolve(), evidence.host_architecture())


if __name__ == "__main__":
    raise SystemExit(main())
