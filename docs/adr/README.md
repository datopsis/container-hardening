# Architecture decision records

Each record captures one accepted decision, the problem it answered, the
options weighed, and what the project gave up in exchange.

## Conventions

Records are numbered sequentially from `0001`. **A number is permanent.** A
decision that is later reversed is not deleted or renumbered: its record is
marked `superseded` and names the record that replaced it, so the reasoning
behind the original choice survives the choice itself.

The file name is `NNNN-short-slug.md`. Every record carries frontmatter with
`status`, `date`, and `decision-makers`, and the sections in
[`0000-template.md`](0000-template.md).

`status` is one of:

| Status | Meaning |
| --- | --- |
| `proposed` | Written, not yet accepted |
| `accepted` | In force |
| `superseded` | Replaced; names the superseding record |
| `deprecated` | No longer applies, with nothing replacing it |

The `date` is the date the decision was accepted, not the date the record was
written. The records below were written after the fact, so their dates are the
dates the decisions actually took effect in the repository.

## What belongs here

A decision belongs in an ADR when reversing it would be expensive, when it
gave up something a reader would otherwise expect to have, or when the
reasoning is not recoverable from the code. A decision that is obvious from
reading the configuration does not need a record.

Where a decision is also enforced — by a test, a CI gate, or a lint rule — the
record says so, because an unenforced decision decays quietly.

## Index

| # | Decision | Status |
| --- | --- | --- |
| [0001](0001-render-catalogues-never-commit-packages.md) | Render requirement catalogues to Markdown and never commit the source packages | accepted |
| [0002](0002-derive-800-53-cross-references-from-cci.md) | Derive SRG-to-800-53 cross-references from the DISA CCI list | accepted |
| [0003](0003-secrets-reach-an-image-only-as-read-only-files.md) | Secrets reach an image only as read-only files | accepted |
| [0004](0004-derive-the-control-baseline-here-validate-components-there.md) | Derive the control baseline here, and validate each image's component there | accepted |
| [0005](0005-tailor-by-profile-deviations-expire.md) | Tailor by a per-image profile in which every deviation expires | accepted |
| [0006](0006-strict-per-architecture-evidence-and-release-eligibility.md) | Read evidence strictly, score it per architecture, and keep release eligibility apart from the score | accepted |
| [0007](0007-record-manual-reviews-as-expiring-evidence.md) | Record manual reviews as evidence that lapses when what it reviewed changes | accepted |
| [0008](0008-retrieve-by-locked-location-and-hold-the-pipeline-to-the-standard.md) | Retrieve inputs by locked location, pin keys by fingerprint, and hold the pipeline to the standard | proposed |
