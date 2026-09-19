"""Write evidence the way the standard's scorer reads it.

Every file states what it is evidence about: the commit it was built from, the
run that produced it, and the architecture, with the image's ID where there is
an image. The scorer refuses evidence without them; see the standard's
docs/EVIDENCE.md. Each result has a stable id, so a check is the same check
from one run to the next.
"""

from __future__ import annotations

import json
import os
import platform
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SCHEMA = "container-hardening/evidence"
MACHINES = {"x86_64": "amd64", "amd64": "amd64", "aarch64": "arm64", "arm64": "arm64"}


def host_architecture() -> str:
    """The architecture this machine builds for natively."""
    machine = platform.machine().lower()
    if machine not in MACHINES:
        raise SystemExit("unsupported architecture " + machine)
    return MACHINES[machine]


def subject(architecture: str, **extra: str) -> dict:
    commit = os.environ.get("GITHUB_SHA") or subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=HERE, text=True, capture_output=True).stdout.strip()
    run = os.environ.get("GITHUB_RUN_ID")
    ci_run = (os.environ.get("GITHUB_SERVER_URL", "") + "/" + os.environ.get("GITHUB_REPOSITORY", "")
              + "/actions/runs/" + run + "/attempts/" + os.environ.get("GITHUB_RUN_ATTEMPT", "1")) if run else "local"
    return {"source_commit": commit, "ci_run": ci_run, "architecture": architecture, **extra}


def image_subject(image: str) -> dict:
    """The image as it was tested: its architecture, its ID, and its digest if it was named by one."""
    inspected = json.loads(subprocess.run(["podman", "image", "inspect", image], text=True, capture_output=True,
                                          check=True).stdout)[0]
    extra = {"image": image, "image_id": "sha256:" + inspected["Id"].removeprefix("sha256:")}
    if "@sha256:" in image:
        extra["digest"] = image.rsplit("@", 1)[1]
    return subject(inspected["Architecture"], **extra)


def write(path: Path, about: dict, results: list[dict], **extra) -> None:
    passed = sum(r["passed"] is True for r in results)
    failed = sum(r["passed"] is False for r in results)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({
        "schema": SCHEMA, "schema_version": 1, "subject": about, **extra,
        "passed": passed, "failed": failed, "skipped": len(results) - passed - failed, "results": results,
    }, indent=2) + "\n", encoding="utf-8")
