---
status: proposed
date: 2026-09-20
decision-makers: Joey
---

# Retrieve inputs by locked location, pin keys by fingerprint, and hold the pipeline to the standard

## Context and Problem Statement

A comparison with an image repository that had gone further on its build
found four places where the standard, and the reference image that shows it,
were weaker than they looked:

- **Retrieval still resolved.** The reference image's acquisition ran the
  package manager to download its locked package versions. The lock named what
  to fetch, but the package manager decided where from, by reading live
  repository metadata. A build could not be repeated from a mirror or from
  inputs carried across an air gap, and would fail once the repository stopped
  listing an old version.
- **The signing key came from what it vouched for.** The reference image
  trusted the key file shipped in its builder base, pinned by that file's
  digest, and matched signers by 16-character key ID. That works only while the
  base's vendor is also the packages' signer; for a third-party repository it
  means trusting whatever key the base carries.
- **The bundle was not held to the lock.** A partly filled bundle directory
  could be reused, and extra files in it were ignored.
- **The pipeline was held to nothing.** The reference image pinned its actions
  and restricted permissions, and CI audited its workflows, but no criterion
  required it, so an image could meet the standard with an unpinned,
  over-privileged pipeline.

It also found that exceptions could not say which architecture they
concerned, now that each architecture is scored separately.

## Decision Drivers

* The lock is the reviewed statement of what an image is built from; nothing
  unreviewed should decide it at build time
* A key vouches for inputs only if it is obtained independently of them
* The pipeline that builds an image is one of its inputs
* An exception should excuse no more than it must

## Considered Options

* **Tighten IMG-02, IMG-03, IMG-05, and IMG-26, and add IMG-35**
* **Guidance only** — leaves each image free to keep resolving at build time,
  which is the weakness found
* **Do nothing**

## Decision Outcome

Proposed: **tighten the criteria and add one.**

1. **IMG-02** records each input's location and source package, pins each
   signing key by full fingerprint obtained from the publisher, and requires
   the verified inputs to be exactly those the lock names.
2. **IMG-03** confines retrieval to fetching what the lock names from where it
   says; resolving versions belongs to the reviewed refresh.
3. **IMG-05** extends the scan for credentials and acquisition material to the
   bill of materials and the provenance.
4. **IMG-26** lets an exception be scoped to the architectures it concerns; it
   then excuses nothing on any other. The scorer honours the scope.
5. **IMG-35**, new and required: the pipeline is pinned and least-privileged.

The required criteria go from 34 to 35, and every profile's pinned revision is
stale until it is reassessed. An image not yet meeting a tightened or new
criterion records a deviation, as for any gap.

### Consequences

* Good: a build can be repeated from a mirror or an air-gapped copy of the
  bundle, and verified against the same lock.
* Good: a third-party repository's key is trusted for what it is, not because
  the base happened to carry it.
* Bad: a lock records more, and a refresh must record locations, source
  packages, and keys.
* Bad: every adopting image must reassess, and most will record deviations
  from IMG-02, IMG-03, or IMG-35 first.

### Enforcement

`tests/test_standard.py` holds the criteria's shape, `check-profile.py` the
architecture scope of a deviation, and the scorer's tests its effect. The
reference image evidences each change: its build refuses a key with another
fingerprint, an extra input, and a base of the wrong architecture; its
acquisition runs no package manager; its gates scan history, labels, and the
bill of materials; and a pipeline check reads its workflows.
