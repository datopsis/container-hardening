---
status: accepted
date: 2026-09-18
decision-makers: Joey
---

# Render requirement catalogues to Markdown and never commit the source packages

## Context and Problem Statement

This standard maps against DISA SRGs and STIGs. Those arrive as zip packages
containing an XCCDF XML file alongside logos, a stylesheet, a release memo, and
revision-history PDFs. The XCCDF is the only part that carries requirements.

Two questions had to be answered before any of it entered the repository: what
form the requirements take once they are here, and whether the packages
themselves are committed.

Neither is cosmetic. The packages are US Government works whose redistribution
terms are stated inside the package rather than in a licence file, and the
whole purpose of pinning a source by digest is defeated if the thing being
mapped against can drift without anyone noticing.

## Decision Drivers

* A mapping is meaningless unless it names the revision it was made against
* DISA reissues releases, and a replaced package must be visible, not silent
* Redistribution terms differ per source, and CIS forbids reproduction outright
* A reviewer must be able to see what changed in a release upgrade
* XCCDF XML is not reviewable by a human in a pull request

## Considered Options

* **Commit the packages** — vendor the zips or their extracted trees, and read
  XCCDF directly wherever requirements are needed
* **Commit nothing, fetch at use time** — treat the catalogues as an external
  dependency resolved on demand
* **Commit generated Markdown, pin the source by digest** — convert XCCDF into
  one Markdown file per rule, commit that, and record the identity of what
  produced it

## Decision Outcome

Chosen option: **commit generated Markdown, pin the source by digest.**

Committing the packages was rejected on terms and on reviewability. The
redistribution terms vary per source and are not uniformly permissive — CIS
forbids reproduction entirely, so any scheme that depends on vendoring breaks
the moment a CIS benchmark is added. And an XCCDF diff is not something a
reviewer can read.

Fetching at use time was the genuinely viable alternative, and it lost on
reviewability rather than principle. It keeps the repository small and has no
redistribution exposure at all. But it makes the requirements invisible in the
repository: you cannot read a rule, link to one in a pull request, or see what
a release upgrade changed without reconstructing the fetch. The standard exists
to be *used*, and a requirement nobody can link to does not get used.

### One file per rule

Rules are rendered one per file rather than one document per catalogue. A
single 188-rule document produces an unreadable diff on a release upgrade; one
file per rule produces a diff that names exactly which rules changed, which
were added, and which were withdrawn.

**That diff is the review artifact.** It is the mechanism by which a release
upgrade is assessed rather than accepted, and it is the reason the per-rule
layout is worth 394 files.

### Rules are filed by Group ID

The obvious key is the STIG ID, which is what humans cite. It is not unique.
GPOS V3R3 issues `SRG-OS-000132-GPOS-00067` as two distinct rules, `V-203655`
and `V-278973`.

This was found because the generator produced one file fewer than the rule
count — the second rule had silently overwritten the first. Pages are therefore
filed by Group ID, which DISA does guarantee unique, with the STIG ID shown on
the page and in the index. The generator raises rather than overwrites if two
rules ever share a Group ID.

### Both digests are recorded

For a rendered source the register records the digest of the package *and* the
digest of the XCCDF inside it. The package digest identifies what was
downloaded. The XCCDF digest identifies what the committed Markdown actually
derives from, which is what a reviewer needs in order to reproduce the output.

### Consequences

* Good: requirements are readable, linkable, and diffable in the repository
* Good: no package is redistributed, so per-source terms are respected by
  construction and CIS can be handled by the same rule rather than an exception
* Good: a release upgrade produces a reviewable diff instead of a version bump
* Bad: 394 generated files, which inflate the file count and can bury
  hand-written changes in a large regeneration commit. Regenerations should be
  their own commit
* Bad: the generated Markdown can drift from the package it claims to derive
  from. Without an automated comparison this decision quietly becomes "we have
  a stale copy of an SRG"
* Bad: contributors need the package locally to regenerate, and obtaining one
  requires a browser because the DISA index cannot be scraped
* Bad: enforcement is split across two workflows rather than one, because the
  packages are deliberately absent from the repository. This is the direct cost
  of not committing them

### Enforcement

Split, because pull-request CI does not have the packages and should not reach
the public internet to get them.

**Every pull request** runs `tests/test_sources.py`, which checks what is
committed: that a source claiming to be rendered points at a real index, that
the rule count in the register matches the number of committed pages, and that
the index and the rule pages reference each other exactly. This catches a
partial or hand-edited regeneration without needing the source.

**`verify-sources.yml`, weekly**, retrieves every pinned source, compares it to
its recorded digest via `scripts/verify-sources.py`, and then runs
`build-srg-markdown.py --check` against the retrieved packages. This is the
check that makes the pinning mean something; without it the register records
only that a digest was true once.

`verify-sources.py` never edits the register. A replaced release is a finding
for a person to read, not a digest to quietly update, and an unreachable source
is reported separately from a changed one because reaching nothing says nothing.

The generator refuses to overwrite a rule page on a Group ID collision, so the
failure that produced this decision cannot recur silently.
