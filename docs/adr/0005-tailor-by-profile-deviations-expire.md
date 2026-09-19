---
status: proposed
date: 2026-09-18
decision-makers: Joey
---

# Tailor by a per-image profile in which every deviation expires

## Context and Problem Statement

The standard is meant to be applied to every image, tailored per application.
Three things vary between images: which function-specific sources apply, how
the controls that depend on function are answered, and where an image does not
yet meet the standard.

Before this decision, the first was answered once, in `nginx-ubi`'s ADR-0010,
and the third had no mechanism at all. [IMG-26](../standard/criteria.md#img-26-exceptions-expire)
required an expiring exception register without defining one, and ADR-0004 left
an image that disagrees with the baseline failing its check "until Package 4
defines how a deviation is recorded".

## Decision Drivers

* A tailoring mechanism is also an opt-out mechanism; the question is whether
  the opt-out is visible and temporary
* An absent applicability determination must be distinguishable from a
  forgotten one
* A determination made against one release must not silently carry to the next
* One mechanism is better than three for a reader to learn and a checker to
  enforce
* A small organization has one decision-maker, so separation of duties cannot
  be the safeguard

## Considered Options

* **Per-image criteria selection** — each image lists the criteria it adopts
* **Deviations without expiry** — each image records departures with a reason
* **A profile of applicability determinations and expiring deviations** —
  every image takes every required criterion; departures are recorded, bounded,
  and expire

## Decision Outcome

Chosen option: **a profile of applicability determinations and expiring
deviations.** The format and rules are in [TAILORING.md](../TAILORING.md).

*Per-image selection* was rejected because it inverts the default. An image
that lists what it adopts is compliant with whatever it listed, and a reader has
to compare lists to find what was left out. Taking everything, and recording
departures, puts the gaps in one place.

*Deviations without expiry* were the real alternative, and simpler. They lost
because the failure they allow is the one this repository keeps naming: a
departure recorded once and never revisited. The expiry is what makes a
deviation a decision with a date on it, rather than a permanent exception.

The limits, 180 days for a criterion or control and 90 for a vulnerability, are
a judgement. 180 days is two quarters, long enough to close a real gap. 90 days
for a vulnerability is already generous against the 7, 14, and 30-day
remediation timelines, and three times the GPOS SRG's 30-day ceiling.

Separation of duties was considered and not enforced. The checker requires an
`owner` and an `approved_by`, but does not require them to differ, because a
one-person organization would have to record a fiction to pass. The expiry
does the work separation of duties would otherwise do: the same person has to
decide again, on a date.

### Consequences

* Good: every conditional source has a recorded determination per image, tied
  to the revision it was made against
* Good: one mechanism covers unmet criteria, control positions, and
  vulnerability exceptions, and `check-component.py` honours it
* Good: a new DISA release invalidates the determinations made against the old
  one, instead of carrying them forward
* Bad: an image with a long-standing gap re-records its deviation twice a year.
  That friction is the point, but it is friction
* Bad: the limits are fixed in the checker. Changing them is a change to this
  repository, and applies to every image at once
* Bad: without separation of duties, a deviation is only as good as the
  decision-maker's honesty on the day

### Enforcement

`scripts/check-profile.py` refuses a missing or stale determination, a
deviation without an owner, approver, reason, or compensating measure, and any
deviation expiring beyond its limit or already expired.
`scripts/check-component.py --profile` honours only active deviations.
`tests/test_tailoring.py` tests each rule by breaking it, and checks the
`nginx-ubi` worked example against the current register and baseline.
