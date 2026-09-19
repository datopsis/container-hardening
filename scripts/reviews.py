#!/usr/bin/env python3
"""Read an image's manual reviews: what a person inspected, and whether it still holds.

Almost every criterion is evidenced by a check. A few cannot be: no test tells
a considered review from a rubber stamp. Such a criterion says so, and then a
review recorded in the image's repository may evidence it, under three rules:

- **Only where the standard allows it.** A review of any other criterion is an
  error, not weaker evidence.
- **By a code owner.** The reviewer is named in the repository's CODEOWNERS for
  the path reviewed, so who may review is the same list that governs merging.
- **Until what it reviewed changes.** A review names its subject by path and
  SHA-256. While that file is unchanged the review holds; the moment it
  changes, the review is stale and the criterion has no evidence again. A
  review therefore has no expiry date: it is bound to the thing, not the
  calendar.

A review is weaker evidence than a test, and the score does not say which is
which; score.json does, and each result records the reviewer and the subject.

Usage:
    python reviews.py reviews.json --repository . --baseline artifacts/control-baseline.json
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parent.parent
BASELINE = REPOSITORY / "artifacts" / "control-baseline.json"
SCHEMA = "container-hardening/reviews"
METHODS = ("examine", "interview")
OWNER = re.compile(r"^[@a-zA-Z0-9][-@a-zA-Z0-9_./+]*$")


def code_owners(repository: Path) -> set[str] | None:
    """Everyone CODEOWNERS names, wherever GitHub looks for it."""
    for name in (".github/CODEOWNERS", "CODEOWNERS", "docs/CODEOWNERS"):
        path = repository / name
        if path.is_file():
            owners: set[str] = set()
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.split("#", 1)[0].strip()
                if not line:
                    continue
                owners.update(o for o in line.split()[1:] if OWNER.match(o))
            return owners
    return None


def check(sheet: dict, repository: Path, baseline: dict, today: datetime.date) -> tuple[list[dict], list[str]]:
    """Return (results, errors): the reviews that hold, and what is wrong with the rest."""
    if sheet.get("schema") != SCHEMA or sheet.get("schema_version") != 1:
        return [], ["schema must be " + SCHEMA + ", schema_version 1"]
    owners = code_owners(repository)
    if owners is None:
        return [], ["the repository has no CODEOWNERS, so there is nobody a review may be by"]
    criteria = baseline["criteria"]
    results: list[dict] = []
    errors: list[str] = []
    seen: set[str] = set()
    for position, review in enumerate(sheet.get("reviews", [])):
        identifier = str(review.get("id") or "#" + str(position))
        where = "review " + identifier
        if identifier in seen:
            errors.append(where + ": id used more than once")
        seen.add(identifier)
        criterion = review.get("criterion")
        if criterion not in criteria:
            errors.append(where + ": " + repr(criterion) + " is not a criterion of this revision")
            continue
        allowed = criteria[criterion].get("manual_review")
        if not allowed:
            errors.append(where + ": " + criterion + " is not evidenced by review; it states no Manual review")
            continue
        if review.get("method") != allowed:
            errors.append(where + ": " + criterion + " allows review by " + allowed + ", not " + repr(review.get("method")))
            continue
        reviewer = review.get("reviewed_by")
        if reviewer not in owners:
            errors.append(where + ": " + repr(reviewer) + " is not a code owner (" + ", ".join(sorted(owners)) + ")")
            continue
        reviewed_on = review.get("reviewed_on")
        try:
            if datetime.date.fromisoformat(str(reviewed_on)) > today:
                errors.append(where + ": reviewed_on is in the future")
                continue
        except ValueError:
            errors.append(where + ": reviewed_on is not an ISO date")
            continue
        subject = review.get("subject") or {}
        path, digest = subject.get("path"), subject.get("sha256")
        target = (repository / str(path)).resolve()
        if not isinstance(path, str) or ".." in Path(str(path)).parts or not target.is_file():
            errors.append(where + ": subject.path must be a file in this repository, not " + repr(path))
            continue
        current = hashlib.sha256(target.read_bytes()).hexdigest()
        if current != digest:
            # Not an error: the review simply no longer describes what is there.
            errors.append(where + ": " + path + " has changed since it was reviewed; review it again")
            continue
        if not isinstance(review.get("result"), bool):
            errors.append(where + ": result must be true or false")
            continue
        if not str(review.get("notes") or "").strip():
            errors.append(where + ": notes must say what was read and what was found")
            continue
        results.append({
            "id": "review." + identifier, "criterion": criterion, "passed": review["result"],
            "check": "reviewed by " + reviewer + " on " + str(reviewed_on) + ", by " + allowed + ": " + review["notes"],
            "architecture": "generic", "file": "(review)", "requirements": list(review.get("requirements") or []),
            "review": {"by": reviewer, "on": reviewed_on, "method": allowed, "subject": {"path": path, "sha256": digest}},
        })
    return results, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("reviews", type=Path)
    parser.add_argument("--repository", type=Path, default=Path.cwd(), help="the image's repository, where CODEOWNERS and the subjects are")
    parser.add_argument("--baseline", type=Path, default=BASELINE)
    parser.add_argument("--today", type=datetime.date.fromisoformat, default=datetime.date.today())
    args = parser.parse_args()
    results, errors = check(json.loads(args.reviews.read_text(encoding="utf-8")), args.repository.resolve(),
                            json.loads(args.baseline.read_text(encoding="utf-8")), args.today)
    for error in errors:
        print("error: " + error)
    for result in results:
        print(("holds  " if result["passed"] else "failed ") + result["criterion"] + "  " + result["check"])
    print(str(len(results)) + " reviews hold; " + str(len(errors)) + " errors")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
