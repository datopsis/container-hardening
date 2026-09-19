---
status: accepted
date: 2026-09-19
decision-makers: Joey
---

# Read evidence strictly, score it per architecture, and keep release eligibility apart from the score

## Context and Problem Statement

The first conformance scorer took evidence on trust. It skipped a file that
did not parse, and counted any `passed` value other than `false` or `null` as
a pass, so `"false"` or `0` would have scored as met. It read one artifact and
the JSON files at its root, so images built natively for amd64 and arm64 in
separate jobs had no way to submit both, and nothing stopped a passing amd64
result standing for an arm64 image it never tested. The workflow compared the
profile's revision with an input the caller chose, which established nothing
about which revision of the checks actually ran; the reference image's own
profile had fallen behind without any check noticing. And a run with missing
or skipped criteria succeeded and drew a yellow badge, which a reader could
take as permission to release.

## Decision Drivers

* A score is only worth what the evidence under it is worth
* An architecture's image is a different image; its properties are evidenced
  on it
* The revision a score is against must be the revision the checks came from
* A score shows adoption progress; a release needs more than progress
* A known, fixable High or Critical vulnerability is not outweighed by a score

## Considered Options

* **Strict, per-architecture evidence, with eligibility separate from the score**
* **Keep one score, and fail the run on anything short of complete** — simple,
  but it removes the adoption-progress signal the score exists for
* **Aggregate architectures into one score** — hides exactly the gap that
  per-architecture evidence exists to show
* **Do nothing**

## Decision Outcome

Chosen option: **strict, per-architecture evidence, with eligibility separate
from the score**, as [Evidence](../EVIDENCE.md) sets out:

1. **Evidence has a schema.** Each file carries a header naming the commit,
   run, architecture, and image; each result a stable id and a Boolean or
   `null`. Anything else, a malformed or missing expected file, a duplicated
   check, or evidence from two images of one architecture, makes the evidence
   invalid, and invalid evidence is not scored.
2. **Criteria have a scope.** Each required criterion is evidenced either per
   architecture or once. The profile declares the architectures, `amd64` and
   `arm64` for now, and the evidence files to expect. A score is kept for each
   architecture and for the generic criteria, and a badge for each.
3. **The revision binds.** The caller's `standard-ref` must be a full commit and
   equal the commit the workflow ran from; the profile's revision must be it or
   an ancestor with no normative change since.
4. **Release eligibility is its own answer.** An image is eligible only when the
   evidence is valid, nothing fails, and every criterion on every architecture
   is met or covered by a deviation. A criterion deviation is allowed. A
   vulnerability deviation, or a deviation from the vulnerability gate, is
   not.

Failing the run on anything incomplete was viable, and lost because an image
adopting the standard needs to see its progress before it is finished.
Aggregating architectures lost because it averages away the case that matters.

### Consequences

* Good: a score can no longer be raised by malformed evidence, by one
  architecture's results, or by a revision the checks did not come from.
* Good: the release job gates on one output that means one thing.
* Bad: the profile moves to schema version 2, and every evidence writer must
  add a header and ids; evidence in the old shape is refused, not ignored.
* Bad: a change to the criteria, platform expectations, baseline, or register
  makes every profile stale until it is reassessed, including the reference
  image's, which must be bumped in its own commit after the change.
* Bad: architectures other than amd64 and arm64 need an amendment.

### Enforcement

`scripts/evidence.py`, `scripts/score.py`, and `scripts/check-revision.py`,
tested by `tests/test_score.py` and `tests/test_revision.py`, and exercised end
to end by `conformance-selftest.yml`, which calls the conformance workflow with
missing, malformed, failing, and partial evidence and with a revision that
does not bind. `tests/test_standard.py` requires every criterion to state its
scope. The reference image's release job refuses to publish unless the
conformance workflow found it release eligible.
