#!/usr/bin/env python3
"""Read an image's evidence, strictly, as docs/EVIDENCE.md defines it.

Evidence is what the image's own CI wrote. Nothing here trusts it to be well
formed: a file that does not parse, a result whose `passed` is not a Boolean,
a check that appears twice, a criterion nobody defined, or an expected file
that is missing is an error, and any error makes the whole evidence invalid.
Invalid evidence is not scored lower; it is not scored.

The hardening profile says what to expect: the architectures the image is
built for, its roles if it has more than one, and each evidence file with its
scope. A file with scope `architecture` is expected once for each
architecture, and for each role; a `generic` file once.
Other JSON files, such as scanner reports, are ignored, unless they carry a
`results` list, which is what evidence looks like without its header.

Usage, to check a directory without scoring it:
    python evidence.py EVIDENCE_DIR --profile hardening-profile.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"

SCHEMA = "container-hardening/evidence"
SCHEMA_VERSION = 1
ARCHITECTURES = ("amd64", "arm64")
GENERIC = "generic"
SCOPES = ("architecture", "generic")
# Declared by the profile when the image has more than one of each. Evidence
# about a built image names one of each declared; evidence about the source or
# process, in a generic file, names none.
QUALIFIERS = {"role": "roles", "topology": "topologies", "platform": "platforms"}

COMMIT = re.compile(r"^[0-9a-f]{40}$")
DIGEST = re.compile(r"^sha256:[0-9a-f]{64}$")
CHECK_ID = re.compile(r"^[a-z0-9][a-z0-9._-]{0,99}$")
FILE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*\.json$")


@dataclass
class Evidence:
    results: list[dict] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    source_commit: str | None = None
    subjects: dict[str, dict] = field(default_factory=dict)

    @property
    def valid(self) -> bool:
        return not self.errors


def manifest_problems(profile: dict) -> list[str]:
    """What is wrong with the profile's own declaration of its evidence."""
    problems: list[str] = []
    architectures = profile.get("architectures")
    if not isinstance(architectures, list) or not architectures:
        problems.append("architectures must list at least one of " + ", ".join(ARCHITECTURES))
    else:
        for architecture in architectures:
            if architecture not in ARCHITECTURES:
                problems.append("architectures: " + repr(architecture) + " is not one of " + ", ".join(ARCHITECTURES))
        if len(set(architectures)) != len(architectures):
            problems.append("architectures lists one more than once")
    expected = profile.get("evidence")
    if not isinstance(expected, list) or not expected:
        problems.append("evidence must list the evidence files the image's CI writes")
        return problems
    names: set[str] = set()
    for position, entry in enumerate(expected):
        where = "evidence #" + str(position)
        if not isinstance(entry, dict):
            problems.append(where + ": must be an object")
            continue
        name = entry.get("file")
        if not isinstance(name, str) or not FILE_NAME.match(name):
            problems.append(where + ": file must be a plain JSON file name, not a path")
        elif name in names:
            problems.append(where + ": " + name + " is listed more than once")
        else:
            names.add(name)
        if entry.get("scope") not in SCOPES:
            problems.append(where + ": scope must be one of " + ", ".join(SCOPES))
    for qualifier, plural in QUALIFIERS.items():
        declared = profile.get(plural)
        if declared is None:
            continue
        if not isinstance(declared, list) or not declared or not all(isinstance(v, str) and v for v in declared):
            problems.append(plural + " must be a non-empty list of names when present")
        elif len(set(declared)) != len(declared):
            problems.append(plural + " lists one more than once")
    return problems


def load(directory: Path, profile: dict, baseline: dict) -> Evidence:
    """Every result in the directory, or the reasons they cannot be trusted."""
    evidence = Evidence()
    errors = evidence.errors
    problems = manifest_problems(profile)
    if problems:
        errors.extend("profile " + p for p in problems)
        return evidence

    declared = list(profile["architectures"])
    expected = {e["file"]: e["scope"] for e in profile["evidence"]}
    criteria = baseline["criteria"]
    qualifiers = {q: profile.get(p) for q, p in QUALIFIERS.items()}

    if not directory.is_dir():
        errors.append("no evidence: " + str(directory) + " does not exist")
        return evidence
    files = sorted(p for p in directory.rglob("*.json") if p.is_file())
    if not files:
        errors.append("no evidence: no JSON file under " + str(directory))
        return evidence

    found: dict[tuple, list[str]] = {}
    commits: dict[str, str] = {}
    images: dict[str, dict[str, str]] = {}
    seen: dict[tuple, str] = {}

    for path in files:
        where = path.relative_to(directory).as_posix()
        try:
            document = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeDecodeError) as error:
            errors.append(where + ": not valid JSON (" + str(error).split("\n")[0] + ")")
            continue
        if not isinstance(document, dict):
            continue
        if document.get("schema") != SCHEMA:
            if "results" in document:
                errors.append(where + ": has results but no evidence header; see docs/EVIDENCE.md")
            continue
        if document.get("schema_version") != SCHEMA_VERSION:
            errors.append(where + ": schema_version must be " + str(SCHEMA_VERSION))
            continue
        if path.name not in expected:
            errors.append(where + ": evidence the profile does not expect; list it under evidence")
            continue
        scope = expected[path.name]

        subject = document.get("subject")
        if not isinstance(subject, dict):
            errors.append(where + ": subject is required")
            continue
        architecture = subject.get("architecture")
        if scope == "architecture":
            if architecture not in declared:
                errors.append(where + ": subject.architecture must be one of the profile's architectures ("
                              + ", ".join(declared) + "), not " + repr(architecture))
                continue
        elif architecture != GENERIC:
            errors.append(where + ": a generic file's subject.architecture must be " + repr(GENERIC))
            continue
        commit = subject.get("source_commit")
        if not isinstance(commit, str) or not COMMIT.match(commit):
            errors.append(where + ": subject.source_commit must be a full commit")
        else:
            commits[where] = commit
        if not isinstance(subject.get("ci_run"), str) or not subject["ci_run"].strip():
            errors.append(where + ": subject.ci_run must say which run produced it")
        for key in ("image_id", "digest"):
            value = subject.get(key)
            if value is not None and (not isinstance(value, str) or not DIGEST.match(value)):
                errors.append(where + ": subject." + key + " must be sha256:<64 hex> when present")
            elif value is not None and scope == "architecture":
                recorded = images.setdefault(architecture, {}).setdefault(key, value)
                if recorded != value:
                    errors.append(where + ": subject." + key + " is " + value + ", but other " + architecture
                                  + " evidence names " + recorded + "; evidence from different images is not one result")
        for qualifier, allowed in qualifiers.items():
            value = subject.get(qualifier)
            if allowed is None and value is not None:
                errors.append(where + ": subject." + qualifier + " is set, but the profile declares no " + QUALIFIERS[qualifier])
            elif allowed is not None and scope == "generic" and value is not None:
                errors.append(where + ": a generic file is about the source or process, and names no " + qualifier)
            elif allowed is not None and scope == "architecture" and value not in allowed:
                errors.append(where + ": subject." + qualifier + " must be one of " + ", ".join(allowed))
        found.setdefault((path.name, architecture, *(subject.get(q) for q in QUALIFIERS)), []).append(where)
        evidence.subjects[where] = subject

        results = document.get("results")
        if not isinstance(results, list) or not results:
            errors.append(where + ": results must be a non-empty list")
            continue
        for position, result in enumerate(results):
            at = where + " result #" + str(position)
            if not isinstance(result, dict):
                errors.append(at + ": must be an object")
                continue
            check_id = result.get("id")
            if not isinstance(check_id, str) or not CHECK_ID.match(check_id):
                errors.append(at + ": id must be a stable lower-case identifier, such as smoke.no-root-process")
                continue
            at = where + " " + check_id
            criterion = result.get("criterion")
            if criterion not in criteria:
                errors.append(at + ": " + repr(criterion) + " is not a criterion of this revision")
                continue
            passed = result.get("passed", "absent")
            # Only a real Boolean is a result. "false", 0, and 1 are not.
            if passed is not None and type(passed) is not bool:
                errors.append(at + ": passed must be true, false, or null, not " + json.dumps(passed))
                continue
            if passed is None and not (isinstance(result.get("detail"), str) and result["detail"].strip()):
                errors.append(at + ": a skipped check must say why in detail")
            if not isinstance(result.get("check"), str) or not result["check"].strip():
                errors.append(at + ": check must say what was checked")

            effective = architecture
            if "architecture" in result:
                if scope != "generic":
                    errors.append(at + ": only a generic file's results may name an architecture")
                    continue
                if result["architecture"] not in declared:
                    errors.append(at + ": architecture must be one of the profile's architectures")
                    continue
                effective = result["architecture"]
            if criteria[criterion].get("scope") == "architecture" and effective == GENERIC:
                errors.append(at + ": " + criterion + " is evidenced per architecture, and a generic result stands for none")
                continue

            key = (check_id, effective, *(subject.get(q) for q in QUALIFIERS))
            if key in seen:
                errors.append(at + ": also recorded in " + seen[key] + "; one check has one result per architecture")
                continue
            seen[key] = where
            evidence.results.append({
                "id": check_id, "criterion": criterion, "passed": passed, "check": result.get("check"),
                "architecture": effective, "file": where,
                **{q: subject.get(q) for q in QUALIFIERS if subject.get(q) is not None},
            })

    roles = qualifiers["role"] or [None]
    for name, scope in expected.items():
        wanted = [(a, r) for a in declared for r in roles] if scope == "architecture" else [(GENERIC, None)]
        for architecture, role in wanted:
            if not any(k[0] == name and k[1] == architecture and (role is None or k[2] == role) for k in found):
                errors.append(name + " (" + architecture + (", " + role if role else "") + "): expected, and missing")
    for key, copies in found.items():
        if len(copies) > 1:
            errors.append(key[0] + " (" + ", ".join(k for k in key[1:] if k) + "): found more than once, at "
                          + ", ".join(copies) + "; each copy must come from a different architecture"
                          + (" or role" if any(qualifiers.values()) else ""))

    distinct = set(commits.values())
    if len(distinct) > 1:
        errors.append("evidence comes from more than one commit: " + ", ".join(sorted(distinct)))
    evidence.source_commit = next(iter(distinct)) if len(distinct) == 1 else None
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("evidence", type=Path)
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    args = parser.parse_args()
    evidence = load(args.evidence, json.loads(args.profile.read_text(encoding="utf-8")),
                    json.loads(args.baseline.read_text(encoding="utf-8")))
    for error in evidence.errors:
        print("error: " + error)
    print(str(len(evidence.results)) + " results; " + ("valid" if evidence.valid else str(len(evidence.errors)) + " errors"))
    return 0 if evidence.valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
