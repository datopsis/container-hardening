#!/usr/bin/env python3
"""Report how far the locked inputs are behind their publishers.

It changes nothing (IMG-04). For each base it compares the locked
manifest-list digest with the publisher's current one; when they differ, the
base is behind by the time since the publisher released the current image
(IMG-29). For each locked RPM it reports whether a newer build exists.

With --enforce it fails when a base is more than 30 days behind, which is how
CI stops an image from shipping on a stale base.

Usage:
    python scripts/drift.py [--enforce] [--report evidence/drift.json]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LOCK = json.loads((HERE / "lock.json").read_text(encoding="utf-8"))
REGISTRY = "https://registry.access.redhat.com/v2/"
INDEX = "application/vnd.oci.image.index.v1+json, application/vnd.docker.distribution.manifest.list.v2+json"
MANIFEST = "application/vnd.oci.image.manifest.v1+json, application/vnd.docker.distribution.image.manifest.v2+json"
LIMIT_DAYS = 30


def get(path: str, accept: str) -> tuple[bytes, dict]:
    request = urllib.request.Request(REGISTRY + path, headers={"Accept": accept})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read(), dict(response.headers)


def base_drift(name: str, base: dict, today: datetime) -> dict:
    body, headers = get(base["repository"] + "/manifests/" + base["tag"], INDEX)
    current = headers.get("Docker-Content-Digest") or headers.get("docker-content-digest")
    entry = {"base": name, "repository": base["repository"], "locked": base["digest"], "current": current, "days_behind": 0}
    if current == base["digest"]:
        return entry
    index = json.loads(body)
    amd64 = next(m for m in index["manifests"] if m["platform"]["architecture"] == "amd64")
    manifest = json.loads(get(base["repository"] + "/manifests/" + amd64["digest"], MANIFEST)[0])
    config = json.loads(get(base["repository"] + "/blobs/" + manifest["config"]["digest"], "*/*")[0])
    released = datetime.fromisoformat(config["created"].replace("Z", "+00:00"))
    entry["current_released"] = released.date().isoformat()
    entry["days_behind"] = (today - released).days
    return entry


def rpm_drift() -> list[dict]:
    builder = "registry.access.redhat.com/" + LOCK["bases"]["builder"]["repository"] + "@" + LOCK["bases"]["builder"]["digest"]
    names = " ".join(r["name"] for r in LOCK["rpms"])
    result = subprocess.run(
        ["podman", "run", "--rm", builder, "bash", "-c",
         "dnf -q repoquery --latest-limit 1 --arch x86_64,noarch --qf '%{name} %{epoch}:%{version}-%{release}.%{arch}' " + names],
        text=True, capture_output=True, check=True)
    latest = {}
    for line in result.stdout.splitlines():
        name, evra = line.split(" ", 1)
        latest[name] = evra
    report = []
    for rpm in LOCK["rpms"]:
        locked = rpm["nevra"][len(rpm["name"]) + 1:]
        locked = locked if ":" in locked else "0:" + locked
        report.append({"name": rpm["name"], "locked": locked, "latest": latest.get(rpm["name"]),
                       "newer_available": latest.get(rpm["name"]) not in (None, locked)})
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--enforce", action="store_true", help=f"fail when a base is more than {LIMIT_DAYS} days behind")
    parser.add_argument("--report", type=Path, default=HERE / "evidence" / "drift.json")
    args = parser.parse_args()

    today = datetime.now(timezone.utc)
    bases = [base_drift(name, base, today) for name, base in LOCK["bases"].items()]
    rpms = rpm_drift()
    stale = [b for b in bases if b["days_behind"] > LIMIT_DAYS]
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps({
        "checked_on": today.date().isoformat(), "lock_refreshed_on": LOCK.get("refreshed_on"),
        "limit_days": LIMIT_DAYS, "bases": bases, "rpms": rpms,
    }, indent=2) + "\n", encoding="utf-8")

    for base in bases:
        state = "current" if base["days_behind"] == 0 and base["locked"] == base["current"] else \
            "behind by " + str(base["days_behind"]) + " days (publisher released " + base.get("current_released", "?") + ")"
        print("base " + base["base"] + ": " + state)
    newer = [r for r in rpms if r["newer_available"]]
    print(str(len(newer)) + " of " + str(len(rpms)) + " locked RPMs have a newer build" +
          ("".join("\n  " + r["name"] + " " + r["locked"] + " -> " + str(r["latest"]) for r in newer)))
    if stale:
        print("a base is more than " + str(LIMIT_DAYS) + " days behind; refresh the lock with scripts/acquire.py --refresh")
    return 1 if args.enforce and stale else 0


if __name__ == "__main__":
    raise SystemExit(main())
