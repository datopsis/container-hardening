---
status: accepted
date: 2026-11-08
decision-makers: Joey
---

# Allow reference-only conditional sources without per-image determinations

## Context and Problem Statement

The owner uses this draft standard as a reference, not as a CI gate for image
repositories. Adding database, object-storage, and API/catalog references
would otherwise require every image profile to record new determinations and
would make existing assessments stale solely because the source register grew.

## Decision Drivers

* Expand the reference library without creating dependencies for image repos
* Preserve checks on existing sources and voluntarily recorded determinations
* Make the loss of mandatory applicability coverage explicit

## Considered Options

* **Require determinations for every conditional source** — the existing rule
* **Mark optional conditional sources as reference-only** — allow their omission
  while continuing to check determinations that are recorded

## Decision Outcome

Chosen option: **mark optional conditional sources with `reference_only: true`**
in `artifacts/sources.json`, retaining `role: conditional`.

`scripts/check-profile.py` does not require a per-image determination for these
entries. An image may consult them without adopting an assessment dependency;
if it records a determination, the existing pin and basis checks still apply.

`scripts/check-revision.py` permits only pure additions of reference-only
conditional sources without making an existing assessment stale. Such additions
expand optional reading without changing what the assessment was against.
Changes to existing entries, removals, and other normative changes still make
the assessment stale. This is a limited exception to the register and
applicability rules in ADR-0005 and ADR-0006.

Requiring every image to decide every new reference was rejected because it
would turn library maintenance into mandatory work for image repositories.

### Consequences

* Good: new references can be registered without changing existing image profiles.
* Good: existing source changes and voluntarily recorded determinations remain checked.
* Bad: an image can ignore a reference-only source silently. A passing profile
  check does not establish that the image considered it or found it inapplicable.

To revert this exception for a source, drop its `reference_only` flag and add
the required determinations to the profiles being checked. The register change
then makes their assessments stale, so reassess and update their revisions.

### Enforcement

`tests/test_tailoring.py`:

* `test_reference_only_sources_do_not_require_a_determination`
* `test_an_optional_determination_still_checks_the_pin`
* `test_a_missing_determination_is_a_violation` preserves the default rule

`tests/test_revision.py`:

* `test_only_reference_additions_leave_the_revision_current`
* `test_source_changes_cannot_hide_behind_reference_additions`
* `test_required_or_malformed_additions_still_make_a_revision_stale`
