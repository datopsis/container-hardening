#!/usr/bin/env python3
"""Verify that every pinned source still matches its recorded digest.

Pinning a source by digest only means something if the digest is checked
again later. DISA replaces a release in place at a URL of the same shape, so
without this the register records that a digest was true once.

This script never edits the register. A drifted source is a finding for a
person to review: the correct response to "DISA replaced the package" is to
read what changed and decide, not to record the new digest and move on.

Unreachable is not the same as unchanged, and is reported separately.

Usage:
    python scripts/verify-sources.py                 # verify digests only
    python scripts/verify-sources.py --fetch DIR     # also keep them for rendering
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
REGISTER = REPOSITORY / "artifacts" / "sources.json"

TIMEOUT = 120
CHUNK = 1 << 16
# The DISA host rejects the default urllib agent.
AGENT = "Mozilla/5.0 (compatible; datopsis-container-hardening)"


@dataclass
class Result:
    source_id: str
    state: str  # "match", "drifted", "unreachable", "skipped"
    detail: str = ""


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        chunks: list[bytes] = []
        while True:
            chunk = response.read(CHUNK)
            if not chunk:
                break
            chunks.append(chunk)
    return b"".join(chunks)


def verify(source: dict, extract_to: Path | None) -> Result:
    identifier = source["id"]

    if source["status"] != "pinned":
        return Result(identifier, "skipped", f"status is {source['status']}")
    if not source.get("url"):
        return Result(identifier, "skipped", "no URL recorded")

    try:
        payload = fetch(source["url"])
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        # Reaching nothing tells us nothing about whether the source changed.
        return Result(identifier, "unreachable", str(error))

    digest = hashlib.sha256(payload).hexdigest()
    if digest != source["sha256"]:
        return Result(
            identifier,
            "drifted",
            f"recorded {source['sha256']}\n      served   {digest}\n"
            f"      size     recorded {source['size']}, served {len(payload)}",
        )

    if extract_to is not None:
        extract_to.mkdir(parents=True, exist_ok=True)
        retrieved = extract_to / Path(source["url"]).name
        retrieved.write_bytes(payload)
        # A zip is extracted for the renderers; anything else, such as the
        # OSCAL catalogue the crosswalk resolves controls against, is kept.
        if retrieved.suffix == ".zip":
            with zipfile.ZipFile(retrieved) as bundle:
                bundle.extractall(extract_to)
            retrieved.unlink()

    return Result(identifier, "match", f"{len(payload)} bytes")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fetch",
        metavar="DIR",
        help="keep verified sources in DIR, extracting zip packages, so the "
             "catalogues and crosswalk can be regenerated and compared",
    )
    args = parser.parse_args()

    extract_to = (REPOSITORY / args.fetch).resolve() if args.fetch else None

    register = json.loads(REGISTER.read_text(encoding="utf-8"))
    results = [verify(s, extract_to) for s in register["sources"]]

    by_state: dict[str, list[Result]] = {}
    for result in results:
        by_state.setdefault(result.state, []).append(result)

    for state, label in (
        ("match", "verified"),
        ("skipped", "skipped"),
        ("unreachable", "UNREACHABLE"),
        ("drifted", "DRIFTED"),
    ):
        for result in by_state.get(state, []):
            print(f"  {label:12} {result.source_id}")
            if result.detail and state in ("drifted", "unreachable"):
                print(f"      {result.detail}")

    drifted = by_state.get("drifted", [])
    unreachable = by_state.get("unreachable", [])

    print()
    print(
        f"{len(by_state.get('match', []))} verified, "
        f"{len(unreachable)} unreachable, "
        f"{len(drifted)} drifted, "
        f"{len(by_state.get('skipped', []))} skipped"
    )

    if drifted:
        print(
            "\nA pinned source no longer matches its recorded digest.\n"
            "Do not update the digest without reading what changed: the "
            "register\nexists so that a replaced release is a decision, not an "
            "accident.\n"
            "Regenerate the affected catalogue and review the per-rule diff.",
            file=sys.stderr,
        )
        return 1

    if unreachable:
        print(
            "\nOne or more sources could not be retrieved. This says nothing "
            "about\nwhether they changed, and no digest has been altered.",
            file=sys.stderr,
        )
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
