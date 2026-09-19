#!/usr/bin/env python3
"""Check an image's hardening profile: what it takes from the standard, and why.

Every image takes every required criterion. What varies per image is recorded
in its hardening profile, and this script holds it to docs/TAILORING.md:

- **Applicability.** Every conditional source in the register has exactly one
  determination, applies or does not, with its basis. It is made against the
  source's pinned digest, so a new release makes it stale rather than silently
  carrying it forward.
- **Evidence.** The architectures the image is built for, and each evidence
  file its CI writes with that file's scope, which is what the scorer holds
  the evidence to (docs/EVIDENCE.md). Roles, topologies, and platforms, when
  the image has more than one of any.
- **Deviations.** A criterion not met, a control positioned differently from the
  baseline, or a vulnerability not fixed in time. Each has an owner, an
  approver, a reason, what is done instead, and an expiry no further out than
  the limit for its kind. An expired deviation is a violation.

It never edits the profile.

Usage:
    python check-profile.py artifacts/hardening-profile.json
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
SCHEMA_VERSION = 2
REGISTER = REPOSITORY / "artifacts" / "sources.json"
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"

KINDS = ("criterion", "control", "vulnerability")
# How far out a deviation may expire when it is recorded. A vulnerability
# deviation is bounded tightly because the remediation clock is already running;
# see ADR-0005.
MAXIMUM_DAYS = {"criterion": 180, "control": 180, "vulnerability": 90}
WARN_DAYS = 14

DEVIATION_ID = re.compile(r"^DEV-\d{3}$")
REVISION = re.compile(r"^[0-9a-f]{40}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
ADVISORY = re.compile(r"^(CVE-\d{4}-\d{4,}|GHSA(-[23456789cfghjmpqrvwx]{4}){3})$")


def evidence_module():
    spec = importlib.util.spec_from_file_location("evidence", REPOSITORY / "scripts" / "evidence.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("evidence", module)
    spec.loader.exec_module(module)
    return module


def date(value, where: str, problems: list[str]) -> datetime.date | None:
    try:
        return datetime.date.fromisoformat(value)
    except (TypeError, ValueError):
        problems.append(where + ": " + repr(value) + " is not an ISO date")
        return None


def text(entry: dict, key: str, where: str, problems: list[str]) -> str:
    value = entry.get(key)
    if not isinstance(value, str) or not value.strip():
        problems.append(where + ": " + key + " is required")
        return ""
    return value


def active_deviations(profile: dict, today: datetime.date) -> list[dict]:
    """Deviations in force on the given day, for other checks to honour."""
    found = []
    for deviation in profile.get("deviations", []):
        try:
            if datetime.date.fromisoformat(deviation["expires_on"]) >= today:
                found.append(deviation)
        except (KeyError, TypeError, ValueError):
            continue
    return found


def check(
    profile: dict,
    register: dict,
    baseline: dict,
    today: datetime.date,
) -> tuple[list[str], list[str]]:
    """Return (violations, warnings)."""
    violations: list[str] = []
    warnings: list[str] = []
    sources = {s["id"]: s for s in register["sources"]}

    if profile.get("schema_version") != SCHEMA_VERSION:
        violations.append("schema_version must be " + str(SCHEMA_VERSION) + "; see the changelog for what version 2 adds")
    text(profile, "image", "profile", violations)
    text(profile, "function", "profile", violations)
    revision = (profile.get("standard") or {}).get("revision", "")
    if not REVISION.match(revision or ""):
        violations.append("standard.revision must be the full commit of container-hardening this profile was checked against")

    violations.extend(evidence_module().manifest_problems(profile))

    # Applicability.
    conditional = {i for i, s in sources.items() if s["role"] == "conditional"}
    determined: dict[str, dict] = {}
    for position, entry in enumerate(profile.get("applicability", [])):
        source_id = entry.get("source", "")
        where = "applicability " + (source_id or "#" + str(position))
        if source_id in determined:
            violations.append(where + ": determined more than once")
        determined[source_id] = entry
        if source_id not in sources:
            violations.append(where + ": not a source in the register")
            continue
        if source_id not in conditional:
            violations.append(
                where + ": role is " + sources[source_id]["role"] + ", not conditional; "
                "only conditional sources are selected per image"
            )
            continue
        if not isinstance(entry.get("applies"), bool):
            violations.append(where + ": applies must be true or false")
        text(entry, "basis", where, violations)
        text(entry, "reviewed_by", where, violations)
        reviewed = date(entry.get("reviewed_on"), where + " reviewed_on", violations)
        if reviewed and reviewed > today:
            violations.append(where + ": reviewed_on is in the future")
        if entry.get("sha256") != sources[source_id]["sha256"]:
            violations.append(
                where + ": made against " + str(entry.get("sha256"))[:12] + ", but the register now pins "
                + str(sources[source_id]["sha256"])[:12] + " (" + str(sources[source_id]["release"])
                + "); review it against the current revision"
            )
        if entry.get("applies") is True and not sources[source_id]["rendered"]:
            warnings.append(where + ": applies, but the source is not yet rendered, so its rules cannot be traced")
    for missing in sorted(conditional - set(determined)):
        violations.append("applicability " + missing + ": conditional source with no determination")

    # Deviations.
    criteria = baseline["criteria"]
    controls = {c["id"]: c for c in baseline["controls"]}
    originations = set(baseline["model"]["originations"])
    seen: set[str] = set()
    targets: set[tuple[str, str, str]] = set()
    for position, deviation in enumerate(profile.get("deviations", [])):
        identifier = deviation.get("id", "")
        where = "deviation " + (identifier or "#" + str(position))
        if not DEVIATION_ID.match(identifier):
            violations.append(where + ": id must look like DEV-001")
        if identifier in seen:
            violations.append(where + ": id used more than once")
        seen.add(identifier)

        kind = deviation.get("kind")
        if kind not in KINDS:
            violations.append(where + ": kind must be one of " + ", ".join(KINDS))
            continue
        target = deviation.get("target", "")
        scope = deviation.get("digest", "")
        key = (kind, target, scope)
        if key in targets:
            violations.append(where + ": another deviation already covers " + target)
        targets.add(key)

        if kind == "criterion":
            if target not in criteria:
                violations.append(where + ": " + repr(target) + " is not a criterion")
            elif criteria[target]["level"] != "required":
                violations.append(where + ": " + target + " is a target; there is nothing to deviate from")
        elif kind == "control":
            if target not in controls:
                violations.append(where + ": " + repr(target) + " is not in the baseline")
            elif controls[target]["origination"] == "research-required":
                violations.append(where + ": the baseline leaves " + target + " to the image; decide it, do not deviate")
            if deviation.get("origination") not in originations:
                violations.append(where + ": origination must state what the component says instead")
            elif target in controls and deviation["origination"] == controls[target]["origination"]:
                violations.append(where + ": origination is the same as the baseline's")
        elif kind == "vulnerability":
            if not ADVISORY.match(target or ""):
                violations.append(where + ": target must be a CVE or GHSA identifier")
            if not DIGEST.match(scope or ""):
                violations.append(where + ": a vulnerability deviation is scoped to one image digest (sha256:...)")

        for key_name in ("reason", "compensating", "owner", "approved_by"):
            text(deviation, key_name, where, violations)

        recorded = date(deviation.get("recorded_on"), where + " recorded_on", violations)
        expires = date(deviation.get("expires_on"), where + " expires_on", violations)
        if recorded and expires:
            if expires <= recorded:
                violations.append(where + ": expires_on must be after recorded_on")
            elif (expires - recorded).days > MAXIMUM_DAYS[kind]:
                violations.append(
                    where + ": expires " + str((expires - recorded).days) + " days after it was recorded; "
                    "the limit for a " + kind + " deviation is " + str(MAXIMUM_DAYS[kind])
                )
            if recorded > today:
                violations.append(where + ": recorded_on is in the future")
        if expires:
            if expires < today:
                violations.append(where + ": expired on " + expires.isoformat())
            elif (expires - today).days <= WARN_DAYS:
                warnings.append(where + ": expires on " + expires.isoformat())

    return violations, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("profile", type=Path, help="the image's hardening profile")
    parser.add_argument("--register", type=Path, default=REGISTER, help="the source register (default: this repository's)")
    parser.add_argument("--baseline", type=Path, default=BASELINE, help="the control baseline (default: this repository's)")
    parser.add_argument("--today", type=datetime.date.fromisoformat, default=datetime.date.today(), help="evaluate expiry as of this date")
    parser.add_argument("--report", type=Path, help="write the result as criterion evidence (IMG-26) to this file")
    args = parser.parse_args()

    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    register = json.loads(args.register.read_text(encoding="utf-8"))
    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))

    violations, warnings = check(profile, register, baseline, args.today)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        commit = os.environ.get("GITHUB_SHA") or subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=args.profile.resolve().parent, text=True, capture_output=True).stdout.strip()
        run = os.environ.get("GITHUB_RUN_ID")
        args.report.write_text(json.dumps({
            "schema": "container-hardening/evidence", "schema_version": 1,
            "subject": {
                "source_commit": commit, "architecture": "generic",
                "ci_run": os.environ.get("GITHUB_SERVER_URL", "") + "/" + os.environ.get("GITHUB_REPOSITORY", "")
                + "/actions/runs/" + run if run else "local",
            },
            "checked_on": args.today.isoformat(),
            "violations": violations, "warnings": warnings,
            "results": [{
                "id": "profile.exceptions",
                "criterion": "IMG-26",
                "check": "every exception is a recorded deviation, none expired or over its limit",
                "passed": not violations, "detail": "; ".join(violations),
            }],
        }, indent=2) + "\n", encoding="utf-8")
    for warning in warnings:
        print("warning: " + warning)
    for violation in violations:
        print("violation: " + violation)
    print(
        str(len(profile.get("applicability", []))) + " applicability determinations, "
        + str(len(profile.get("deviations", []))) + " deviations; "
        + str(len(violations)) + " violations, " + str(len(warnings)) + " warnings"
    )
    return 1 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
