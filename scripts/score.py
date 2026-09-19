#!/usr/bin/env python3
"""Score an image's conformance to the standard, from its evidence.

The score is the number of required criteria met, out of the number required
by the pinned revision of the standard. A criterion is met only when:

- at least one recorded check names it,
- every check that names it passed, and none was merely skipped, and
- the image's hardening profile records no active deviation from it.

A deviation is visible and temporary, and not the same as meeting the
criterion, so it does not score as one. A violation from check-profile.py or
check-component.py is not a lower score but a failure: the badge says so.

Evidence is any JSON file in EVIDENCE_DIR with a "results" list of
{criterion, check, passed} entries, which is what the reference image's checks
write. The badge is written as a standalone SVG and as a Shields endpoint file.

Usage:
    python scripts/score.py EVIDENCE_DIR --profile PROFILE --component COMPONENT \\
        --requirements FILE... [--requirement-pattern REGEX] [--out DIR]
"""

from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape

REPOSITORY = Path(__file__).resolve().parent.parent
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
REGISTER = REPOSITORY / "artifacts" / "sources.json"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), REPOSITORY / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def evidence(directory: Path) -> dict[str, list[dict]]:
    by_criterion: dict[str, list[dict]] = {}
    for path in sorted(directory.glob("*.json")):
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeDecodeError):
            continue
        if not isinstance(document, dict):
            continue
        for result in document.get("results", []):
            if isinstance(result, dict) and "criterion" in result:
                by_criterion.setdefault(result["criterion"], []).append(result | {"file": path.name})
    return by_criterion


def score(baseline: dict, results: dict[str, list[dict]], deviated: set[str]) -> list[dict]:
    rows = []
    for criterion, meta in baseline["criteria"].items():
        if meta["level"] != "required":
            continue
        checks = results.get(criterion, [])
        if criterion in deviated:
            status = "deviated"
        elif not checks:
            status = "no evidence"
        elif any(c.get("passed") is False for c in checks):
            status = "failed"
        elif any(c.get("passed") is None for c in checks):
            status = "skipped"
        else:
            status = "met"
        rows.append({"criterion": criterion, "title": meta["title"], "status": status, "checks": len(checks)})
    return rows


def badge(label: str, message: str, colour: str) -> str:
    """A flat badge, sized from the text, needing no external service."""
    width = lambda text: 7 * len(text) + 12
    left, right = width(label), width(message)
    total = left + right
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{total}" height="20" role="img" aria-label="{escape(label)}: {escape(message)}">'
        f"<title>{escape(label)}: {escape(message)}</title>"
        f'<rect width="{left}" height="20" fill="#555"/><rect x="{left}" width="{right}" height="20" fill="{colour}"/>'
        '<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" font-size="11">'
        f'<text x="{left / 2}" y="14">{escape(label)}</text><text x="{left + right / 2}" y="14">{escape(message)}</text></g></svg>\n'
    )


def revision() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=REPOSITORY, text=True,
                              capture_output=True, check=True).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("evidence", type=Path)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--component", type=Path, required=True)
    parser.add_argument("--requirements", type=Path, nargs="+", required=True)
    parser.add_argument("--requirement-pattern", default=None)
    parser.add_argument("--out", type=Path, default=Path("score"))
    parser.add_argument("--today", type=datetime.date.fromisoformat, default=datetime.date.today())
    args = parser.parse_args()

    baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
    profiles, components = load("check-profile"), load("check-component")
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    profile_violations, _ = profiles.check(profile, json.loads(REGISTER.read_text(encoding="utf-8")), baseline, args.today)
    active = profiles.active_deviations(profile, args.today)
    pattern = args.requirement_pattern or components.DEFAULT_PATTERN
    stated = components.stated_requirements(args.requirements, pattern)
    component_violations, _ = components.check(
        json.loads(args.component.read_text(encoding="utf-8")), baseline, stated, False, active, components.rendered_rules()
    )

    rows = score(baseline, evidence(args.evidence), {d["target"] for d in active if d["kind"] == "criterion"})
    met = sum(r["status"] == "met" for r in rows)
    failing = bool(profile_violations or component_violations or any(r["status"] == "failed" for r in rows))
    version = revision()
    message = "failing" if failing else f"{met}/{len(rows)}"
    colour = "#cf222e" if failing else ("#2da44e" if met == len(rows) else "#bf8700")

    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "score.json").write_text(json.dumps({
        "standard_revision": version, "scored_on": args.today.isoformat(),
        "met": met, "required": len(rows), "failing": failing,
        "profile_violations": profile_violations, "component_violations": component_violations,
        "criteria": rows,
    }, indent=2) + "\n", encoding="utf-8")
    (args.out / "badge.svg").write_text(badge("hardening", message + " · " + version, colour), encoding="utf-8")
    (args.out / "shields.json").write_text(json.dumps({
        "schemaVersion": 1, "label": "hardening", "message": message + " · " + version,
        "color": "red" if failing else ("green" if met == len(rows) else "yellow"),
    }) + "\n", encoding="utf-8")

    for row in rows:
        if row["status"] != "met":
            print(f"  {row['criterion']:7} {row['status']:12} {row['title']}")
    for violation in profile_violations + component_violations:
        print("  violation: " + violation)
    print(f"hardening {message} against revision {version}")
    return 1 if failing else 0


if __name__ == "__main__":
    raise SystemExit(main())
