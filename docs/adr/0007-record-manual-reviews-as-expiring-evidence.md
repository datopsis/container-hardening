---
status: accepted
date: 2026-09-20
decision-makers: Joey
---

# Record manual reviews as evidence that lapses when what it reviewed changes

## Context and Problem Statement

Some things cannot be shown by a test. A SCAP scan reports some rules as not
checked, because the rule asks a person to look. NIST SP 800-53A assesses
controls by examining and interviewing as well as by testing. Branch protection
can be read from an API, but whether reviews are actually meaningful cannot.

The scorer counts only results that a check recorded. A criterion that needs a
person's inspection can therefore be met only by a deviation, which says the
image does not meet it, when in fact someone has looked and it does. The
standard also says a criterion whose only evidence is a sentence in a README is
not met, so the answer cannot be to let an image assert it.

## Decision Drivers

* A person's inspection is evidence, but weaker than a test, and it goes stale
* It must be as visible and as bounded as a deviation
* It must name what was inspected, so a later change makes it stale
* It must not become a way round a test that could be written

## Considered Options

* **A review record, as expiring evidence, allowed only where the standard says so**
* **Treat every manual item as a deviation** — the status quo; it misstates a
  met criterion as unmet, and teaches that deviations are routine
* **Let the image's evidence carry manual results** — an image could then record
  a pass for anything, which is the self-assessment the scorer exists to refuse

## Decision Outcome

Chosen: **a review record, allowed only where the standard says so, valid until
what it reviewed changes.**

1. **The standard says where.** A criterion states whether a manual review may
   evidence it, and by which method, examine or interview. Most criteria state
   that it may not. A criterion that allows it is one no test can establish.
2. **The image records reviews in its repository**, merged by pull request,
   each naming the criterion, the requirement, the method, what was inspected
   (by commit, digest, or setting), the result, who reviewed it and when, and
   an expiry no more than 180 days out, as for a deviation.
3. **The scorer turns reviews that hold into results**, marked as reviews, for
   the criteria that allow them. A review of a criterion that allows none, by
   anyone but a code owner, or of a subject since changed, is an error.
4. **SCAP rules not checked** by the scan become review items when the SCAP
   profile exists (IMG-T3).

### What was decided

**One criterion: IMG-04.** IMG-33 was the other candidate; its branch
protection is readable from an API, so it stays testable and takes no review.
No runtime or build criterion allows one.

**No expiry date; a review lapses when its subject changes.** A review names
what it read by path and SHA-256. A fixed period would either expire a review
of something untouched, or leave a review standing after the thing changed.
Binding it to the subject is both stricter and less noisy.

**A code owner reviews.** `reviewed_by` must appear in the repository's
`CODEOWNERS`, the same list GitHub uses to require review before merge.

**The intended end state is no review at all.** If a refresh publishes a
candidate lock with attested provenance, a check can hold the committed lock to
an attested candidate, and IMG-04 becomes testable like everything else. That
is on the roadmap; when it lands, IMG-04 stops allowing a review.

### Consequences

* Good: an inspected criterion can be shown as met, with who looked and when.
* Good: a review expires, so it is repeated rather than forgotten.
* Bad: a review is weaker than a test, and a badge does not show the difference;
  score.json does.
* Bad: another file for an image to keep.

### Enforcement

`scripts/reviews.py`, which the scorer calls, with `tests/test_reviews.py`:
a review that holds, one of a criterion that allows none, one by someone who is
not a code owner, one whose subject has changed, and a repository with no
CODEOWNERS. `tests/test_standard.py` requires the *Manual review* line to name
a method the standard allows, and the control baseline records which criteria
allow one.
