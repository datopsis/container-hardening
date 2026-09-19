#!/usr/bin/env python3
"""Publish the reference image by digest, then promote it, without rebuilding.

A release is three steps, run by the release workflow:

- ``candidate``: push one architecture's verified image, untagged, by the
  digest of its own manifest, and confirm the registry serves exactly that
  manifest. The release then pulls and tests that digest.
- ``index``: build a manifest list that names each tested digest, and push only
  the list, untagged, by its digest. The images it names are not copied again,
  so their digests cannot change.
- ``promote``: give the index its version tag. The tag is added last, once the
  index is signed and attested, and a version that already exists is refused
  (IMG-24).

Every registry operation runs in the skopeo image pinned in tools.json, so the
behaviour does not depend on the runner's own copy.

Usage:
    python scripts/publish.py candidate ARCHIVE --authfile AUTH [--out FILE]
    python scripts/publish.py index --child amd64=sha256:... --child arm64=sha256:... --authfile AUTH [--out FILE]
    python scripts/publish.py promote INDEX_DIGEST --version X.Y.Z --authfile AUTH
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOOLS = json.loads((HERE / "tools.json").read_text(encoding="utf-8"))
IMAGE = "ghcr.io/datopsis/reference-web-server"
# Only for rehearsing against a local registry without TLS.
TLS = {"verify": True}
LIST = "application/vnd.docker.distribution.manifest.list.v2+json"


def skopeo(authfile: Path, *args: str, work: Path | None = None, capture: bool = True) -> subprocess.CompletedProcess:
    """Run the pinned skopeo, with WORK mounted at /work."""
    volumes = ["--volume", str(authfile.resolve()) + ":/auth.json:ro,Z"]
    if work is not None:
        volumes += ["--volume", str(work.resolve()) + ":/work:Z"]
    if not TLS["verify"]:
        verb, rest = args[0], list(args[1:])
        flags = ["--tls-verify=false"] if verb == "inspect" else ["--src-tls-verify=false", "--dest-tls-verify=false"]
        args = (verb, *flags, *rest)
    command = ["podman", "run", "--rm", "--network", "host", *volumes, TOOLS["images"]["skopeo"]["reference"], *args]
    return subprocess.run(command, capture_output=capture)


def image() -> str:
    return TLS.get("image", IMAGE)


def served(authfile: Path, reference: str) -> bytes:
    result = skopeo(authfile, "inspect", "--authfile", "/auth.json", "--raw", "docker://" + reference)
    if result.returncode != 0:
        raise SystemExit("cannot read " + reference + ": " + result.stderr.decode()[-300:])
    return result.stdout


def digest_of(body: bytes) -> str:
    return "sha256:" + hashlib.sha256(body).hexdigest()


def candidate(archive: Path, authfile: Path) -> str:
    work = archive.resolve().parent
    with tempfile.TemporaryDirectory(dir=work) as scratch:
        name = Path(scratch).name
        layout = Path(scratch) / "image"
        # The dir transport keeps the Docker manifest, and with it HEALTHCHECK (IMG-20).
        result = skopeo(authfile, "copy", "--quiet", "docker-archive:/work/" + archive.name,
                        "dir:/work/" + name + "/image", work=work)
        if result.returncode != 0:
            raise SystemExit("cannot read the archive: " + result.stderr.decode()[-300:])
        digest = digest_of((layout / "manifest.json").read_bytes())
        result = skopeo(authfile, "copy", "--quiet", "--authfile", "/auth.json", "--preserve-digests",
                        "dir:/work/" + name + "/image", "docker://" + image() + "@" + digest, work=work)
        if result.returncode != 0:
            raise SystemExit("cannot push by digest: " + result.stderr.decode()[-300:])
    if digest_of(served(authfile, image() + "@" + digest)) != digest:
        raise SystemExit("the registry does not serve " + digest + " as pushed")
    return digest


def index(children: dict[str, str], authfile: Path, work: Path) -> str:
    manifests = []
    for architecture, digest in sorted(children.items()):
        body = served(authfile, image() + "@" + digest)
        if digest_of(body) != digest:
            raise SystemExit(architecture + ": the registry serves a different manifest for " + digest)
        manifests.append({"mediaType": json.loads(body)["mediaType"], "size": len(body), "digest": digest,
                          "platform": {"architecture": architecture, "os": "linux"}})
    body = json.dumps({"schemaVersion": 2, "mediaType": LIST, "manifests": manifests}, indent=2).encode()
    digest = digest_of(body)
    with tempfile.TemporaryDirectory(dir=work) as scratch:
        layout = Path(scratch) / "index"
        layout.mkdir()
        (layout / "version").write_text("Directory Transport Version: 1.1\n")
        (layout / "manifest.json").write_bytes(body)
        result = skopeo(authfile, "copy", "--quiet", "--authfile", "/auth.json", "--multi-arch", "index-only",
                        "--preserve-digests", "dir:/work/" + Path(scratch).name + "/index",
                        "docker://" + image() + "@" + digest, work=work)
        if result.returncode != 0:
            raise SystemExit("cannot push the index: " + result.stderr.decode()[-300:])
    if served(authfile, image() + "@" + digest) != body:
        raise SystemExit("the registry does not serve the index as pushed")
    return digest


def promote(digest: str, version: str, authfile: Path) -> None:
    existing = skopeo(authfile, "inspect", "--authfile", "/auth.json", "--raw", "docker://" + image() + ":" + version)
    if existing.returncode == 0:
        raise SystemExit(image() + ":" + version + " already exists; a released version is never replaced")
    result = skopeo(authfile, "copy", "--quiet", "--authfile", "/auth.json", "--multi-arch", "index-only",
                    "--preserve-digests", "docker://" + image() + "@" + digest, "docker://" + image() + ":" + version)
    if result.returncode != 0:
        raise SystemExit("cannot promote: " + result.stderr.decode()[-300:])
    if digest_of(served(authfile, image() + ":" + version)) != digest:
        raise SystemExit(version + " does not resolve to " + digest)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("step", choices=("candidate", "index", "promote"))
    parser.add_argument("subject", nargs="?", help="the archive for candidate; the index digest for promote")
    parser.add_argument("--child", action="append", default=[], help="architecture=digest, for index")
    parser.add_argument("--version", help="for promote")
    parser.add_argument("--authfile", type=Path, required=True)
    parser.add_argument("--out", type=Path, help="write the resulting digest here")
    parser.add_argument("--image", default=IMAGE, help="the repository to publish to")
    parser.add_argument("--insecure", action="store_true", help="skip TLS verification, to rehearse against a local registry")
    args = parser.parse_args()
    TLS["image"], TLS["verify"] = args.image, not args.insecure

    if args.step == "candidate":
        if not args.subject:
            parser.error("candidate needs the verified image's archive")
        digest = candidate(Path(args.subject), args.authfile)
    elif args.step == "index":
        children = dict(c.split("=", 1) for c in args.child)
        if len(children) != len(args.child) or not children:
            parser.error("index needs one --child per architecture")
        digest = index(children, args.authfile, (args.out or Path.cwd() / "index").resolve().parent)
    else:
        if not args.subject or not args.version:
            parser.error("promote needs the index digest and --version")
        promote(args.subject, args.version, args.authfile)
        digest = args.subject
    if args.out:
        args.out.write_text(digest + "\n", encoding="utf-8")
    print(digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
