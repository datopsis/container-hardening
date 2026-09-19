---
status: proposed
date: 2026-09-19
decision-makers: Joey
---

# Record manual reviews as expiring evidence

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

Proposed: **a review record, as expiring evidence, allowed only where the
standard says so.**

1. **The standard says where.** A criterion states whether a manual review may
   evidence it, and by which method, examine or interview. Most criteria state
   that it may not. A criterion that allows it is one no test can establish.
2. **The image records reviews in its repository**, merged by pull request,
   each naming the criterion, the requirement, the method, what was inspected
   (by commit, digest, or setting), the result, who reviewed it and when, and
   an expiry no more than 180 days out, as for a deviation.
3. **The scorer turns current reviews into results**, marked as reviews, for the
   criteria that allow them. An expired review, a review of a criterion that
   does not allow one, or a review naming a commit or digest other than the one
   judged, is an error.
4. **SCAP rules not checked** by the scan become review items when the SCAP
   profile exists (IMG-T3).

### Open question

Which criteria allow a review. Candidates are the process criteria, such as
IMG-04 (refresh is a reviewed change) and IMG-33 (source protected and
traceable), and none of the runtime criteria. Marking one is a change to the
criteria, and so makes every profile's revision stale until it is reassessed.

### Consequences

* Good: an inspected criterion can be shown as met, with who looked and when.
* Good: a review expires, so it is repeated rather than forgotten.
* Bad: a review is weaker than a test, and a badge does not show the difference;
  score.json does.
* Bad: another file for an image to keep.

### Enforcement

None yet: this record is proposed. On acceptance, the scorer's tests and the
conformance self-test would each gain a case for a current, an expired, and a
disallowed review.
