# Adoption

The standard is self-contained: nothing in [`docs/standard/`](../standard/README.md)
depends on any particular image. This directory is the other direction, how
image repositories take the standard up, and it is the only place in this
repository that names them.

## What adopting costs an image repository

The step-by-step guide is [ADOPTING.md](../ADOPTING.md). In summary:

An image repository adopts the standard by adding three files and running three
checks, each against a pinned revision of this repository:

| File | Checked by | Defined in |
| --- | --- | --- |
| A hardening profile | `scripts/check-profile.py` | [Tailoring](../TAILORING.md) |
| An OSCAL component definition | `scripts/check-component.py` | [Control model](../CONTROL-MODEL.md) |
| Its own tests for each required criterion | Its own CI | [Criteria](../standard/criteria.md) |

## Notes per image repository

What is known about each repository before it adopts, in no particular order
of priority. Each repository chooses when to adopt.

- **`datopsis/clickhouse-ubi`** has among the largest gaps in the
  [snapshot](snapshot-2026-09-18.md): its build and its secret handling.
- **`datopsis/lakekeeper-ubi`** has among the largest gaps in the snapshot,
  including no release workflow and secrets taken only from the environment.
- **`datopsis/nginx-ubi`** already has a requirement tree, a trace matrix, and
  an OSCAL component definition, so every check has something to run against.
  Run against it on 2026-09-18, `check-component.py` reported 375 of 379
  baseline controls absent, and its `cm-6` and `ac-6` entries citing no
  criterion. Its own source register records the Container Platform SRG as
  unresolved at V2R1; the current release is V2R4 and retrieves normally, and
  its register should defer to this one.
- **`datopsis/postgresql-ubi`** met the most criteria in the snapshot.
- **`datopsis/seaweedfs-ubi`** has among the largest gaps in the snapshot,
  including no release workflow. Its function, S3-compatible object storage,
  has no conditional source pinned in the register yet.

## The first snapshot

[`snapshot-2026-09-18.md`](snapshot-2026-09-18.md) records where each image
repository stood against the criteria when they were first written, established
by reading each repository rather than by running its checks. It is kept so
its findings are not lost before each repository tracks its own gaps, and is
deleted once they do. It is not part of the standard, and nothing in the
standard cites it.

## The conformance score and badge

The score, the badge, and what an image's evidence must contain are defined in
[Evidence](../EVIDENCE.md), and computed by the conformance workflow from the
image's own evidence. An image repository publishes its badges to its own
`badges` branch with the badges workflow, and shows them in its README, as
[Show the badges](../ADOPTING.md#8-show-the-badges) describes.
