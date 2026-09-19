# Adoption

The standard is self-contained: nothing in [`docs/standard/`](../standard/README.md)
depends on any particular image. This directory is the other direction, how
image repositories take the standard up, and it is the only place in this
repository that names them.

## What adopting costs an image repository

An image repository adopts the standard by adding three files and running three
checks, each against a pinned revision of this repository:

| File | Checked by | Defined in |
| --- | --- | --- |
| A hardening profile | `scripts/check-profile.py` | [Tailoring](../TAILORING.md) |
| An OSCAL component definition | `scripts/check-component.py` | [Control model](../CONTROL-MODEL.md) |
| Its own tests for each required criterion | Its own CI | [Criteria](../standard/criteria.md) |

## Planned order

1. **`datopsis/nginx-ubi` first.** It already has a requirement tree, a trace
   matrix, and an OSCAL component definition, so it exercises every check.
   Run against it today, `check-component.py` reports 375 of 379 baseline
   controls absent, and its `cm-6` and `ac-6` entries citing no criterion.
   Its own source register still records the Container Platform SRG as
   unresolved at V2R1; the current release is V2R4 and retrieves normally, and
   its register should defer to this one.
2. **`datopsis/postgresql-ubi`**, which meets the most criteria already.
3. **`datopsis/clickhouse-ubi`, `datopsis/seaweedfs-ubi`, and
   `datopsis/lakekeeper-ubi`**, which have the largest gaps in the snapshot.

## The first snapshot

[`snapshot-2026-09-18.md`](snapshot-2026-09-18.md) records where each image
repository stood against the criteria when they were first written, established
by reading each repository rather than by running its checks. It is kept so
its findings are not lost before each repository tracks its own gaps, and is
deleted once they do. It is not part of the standard, and nothing in the
standard cites it.

## Plan: a conformance score and badge

A score an image repository can show in its README, computed the same way for
every image, from evidence rather than assertion. This is a plan; nothing below
exists yet.

### What is scored

The score is **required criteria met, with evidence**, out of the number of
required criteria in the pinned revision of the standard:

```text
score = criteria evidenced / criteria required
```

A criterion counts as met only when all of these hold:

1. The image repository's criteria evidence file names at least one test or CI
   job for it.
2. That job passed in the run producing the score.
3. The hardening profile records no active deviation for it.

A criterion with an active deviation counts as not met. It is visible, it is
temporary, and it is not the same as meeting the standard, so it must not
score as though it were.

### What fails the badge outright

Some conditions are not a lower score but a failure, because a number beside
them would mislead:

- `check-profile.py` reports any violation, including an expired deviation or a
  missing or stale applicability determination
- `check-component.py` reports any violation
- the profile's `standard.revision` is not a commit of this repository

A failing badge says **failing**, not a percentage.

### What the badge shows

```text
hardening | 24/30 · v<short revision>
```

The fraction is shown rather than a percentage, so a reader can see both how
many criteria there are and how many are met. The revision is shown because a
score against an older standard is a different claim from one against the
current standard. A second, optional badge reports control coverage: baseline
controls present in the component definition, out of all baseline controls.

### How it is produced, and staying self-contained

1. This repository adds `scripts/score.py`, which reads the image's profile,
   component definition, and criteria evidence file, together with the CI job
   results, and writes the score.
2. It writes the badge two ways: a standalone SVG, needing no external service,
   and a Shields endpoint JSON file, for repositories that prefer it.
3. The image repository's CI runs it after its checks and publishes both files
   with its release evidence.

A new file is needed in each image repository: a **criteria evidence file**
mapping each required criterion to the tests and CI jobs that establish it.
Without it, "met" would be the repository's word, and the score would be
self-assessment with a badge on it.

### What it must never claim

The badge measures conformance to this standard. It is not a compliance score,
an authorization, or a STIG result, and its label must not suggest otherwise.
Nor is it a ranking between images: an image with more criteria met is not more
secure than one with fewer if its deployment ignores the platform expectations.
