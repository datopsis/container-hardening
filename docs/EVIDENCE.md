# Evidence

What an image's CI must write for the conformance workflow to judge it, and
what the judgement means. The rules here are enforced by
[`scripts/evidence.py`](../scripts/evidence.py) and
[`scripts/score.py`](../scripts/score.py); the decision behind them is
[ADR-0006](adr/0006-strict-per-architecture-evidence-and-release-eligibility.md).
The [reference web server](../examples/reference-web-server/README.md) writes
every file described here, and is judged by the same workflow.

## Three answers, not one

Conformance answers three questions, and they are kept apart because they are
different claims:

| Question | Output | Fails the run |
| --- | --- | --- |
| **Is the evidence valid?** Well formed, complete, and from one commit and one image per architecture | `evidence-valid` | Yes, when it is not |
| **What is the score?** Required criteria met, per architecture | `score`, `coverage` | Only when a check failed, or the revision, profile, or component breaks a rule |
| **Is the image release eligible?** | `release-eligible` | No; the release job gates on it |

A run can succeed with a score short of complete. That is how adoption
progress is shown, and it is why a successful run is never permission to
release: only `release-eligible` is.

## An evidence file

Each check the image's CI runs writes its results to a JSON file:

```json
{
  "schema": "container-hardening/evidence",
  "schema_version": 1,
  "subject": {
    "source_commit": "0123456789abcdef0123456789abcdef01234567",
    "ci_run": "https://github.com/owner/repo/actions/runs/123/attempts/1",
    "architecture": "amd64",
    "image": "localhost/reference-web-server:ci",
    "image_id": "sha256:5f2d…"
  },
  "results": [
    {
      "id": "smoke.no-effective-capabilities",
      "criterion": "IMG-13",
      "check": "every process has an empty effective capability set",
      "passed": true,
      "detail": "",
      "requirements": ["RWS-013"]
    }
  ]
}
```

| Field | Rule |
| --- | --- |
| `schema`, `schema_version` | Exactly as above. A file with a `results` list and no header is refused, so evidence in an older shape cannot be silently ignored |
| `subject.source_commit` | The full commit the image was built from. Every file must name the same one |
| `subject.ci_run` | The run that produced it; `local` outside CI |
| `subject.architecture` | `amd64` or `arm64` for evidence about a built image; `generic` for evidence about the source, process, or release as a whole |
| `subject.image_id`, `subject.digest` | Optional, `sha256:` and 64 hex characters. Every file for one architecture that names one must name the same one, so evidence from two different images is never combined into one result. `digest` is recorded when the image tested was addressed by digest |
| `subject.role`, `subject.topology`, `subject.platform` | Required when the profile declares `roles`, `topologies`, or `platforms`; refused when it does not |
| `results[].id` | A stable, lower-case identifier for the check, such as `smoke.no-root-process`. One check has one result per architecture: the same `id` twice is an error, whatever the outcomes |
| `results[].criterion` | A criterion of the pinned revision |
| `results[].passed` | `true`, `false`, or `null`. Nothing else: `"false"`, `0`, and `1` are errors, not results. `null` is a check that could not run where it ran, which is not a pass, and must say why in `detail` |
| `results[].requirements` | The image's requirements this check verifies. With a crosswalk, each must be one the crosswalk maps the result's criterion to |
| `results[].architecture` | Only in a `generic` file: names the architecture a result is about, such as a release's per-architecture bill of materials |

Other JSON files, such as scanner reports, are ignored. A file that does not
parse is an error wherever it is.

Applicability is not evidence. There is no "not applicable" result: whether a
source applies is decided in the [hardening profile](TAILORING.md), and a
criterion the image does not meet is a [deviation](TAILORING.md#deviations).

## What the profile declares

The hardening profile says what evidence to expect, so a missing file is an
error rather than an absence:

```json
"architectures": ["amd64", "arm64"],
"evidence": [
  {"file": "smoke.json", "scope": "architecture"},
  {"file": "gates-source.json", "scope": "generic"}
]
```

A file with scope `architecture` is expected once for each architecture, a
`generic` file once. Missing is an error; twice for the same architecture is an
error; a file the profile does not list is an error.

An image with more than one role, topology, or platform declares them, such as
`"roles": ["server", "worker"]`, and every architecture-scoped evidence
subject then names one; a generic file names none. With roles, each
architecture-scoped file is expected once for every architecture and role, and
a per-architecture criterion is met only when it is met for every role.

## Scope: per architecture, or generic

Each criterion states its [scope](standard/criteria.md). A **per-architecture**
criterion belongs to the built image, such as the user it runs as or the
vulnerabilities it carries, and is met on an architecture only by evidence
from that architecture. A passing amd64 result never fills an arm64 gap, and a
`generic` result for a per-architecture criterion is an error. A **generic**
criterion belongs to the source, the process, or the release, such as a
pinned base or an unexpired exception register, and is met by evidence from
anywhere.

The score is computed for each architecture the profile declares, over all
required criteria, and once more as **generic**, over the generic criteria
alone.

## Collecting it across architectures

Build and test each architecture natively, and upload each architecture's
evidence as its own artifact. Pass the conformance workflow a pattern:

```yaml
evidence-artifacts: evidence-*
```

It downloads each artifact into its own directory, so files with the same name
from different architectures cannot overwrite each other, and the subject of
each file, not its location, says what it is about.

## What is met

A criterion is met on an architecture when at least one check names it, every
check that names it passed, none was merely skipped, and the profile records no
active deviation from it.

It must be met in every combination of the roles and topologies the profile
declares: a server's pass does not cover a worker, and a standalone run does
not cover a clustered one.

With a crosswalk, it must also be met **for every requirement** the crosswalk
maps it to: each requirement needs a passing check that names it, in each of
those combinations. A criterion whose checks all pass but leave a mapped
requirement without one is `partial`, which is not met and blocks a release.
The mapping is many to many, and one broad requirement, or one passing suite,
does not close a criterion the image states in several requirements. A deviation is visible and temporary, and does not
score as a pass. The exception register itself, IMG-26, is judged by the
conformance workflow from the profile, not taken from the image's evidence.

## What fails

A run fails on invalid evidence, and on any of these, which are not a lower
score but a failure because a number beside them would mislead:

- The revision does not bind (below).
- [`check-profile.py`](../scripts/check-profile.py) reports a violation,
  including an expired deviation or a stale applicability determination.
- [`check-component.py`](../scripts/check-component.py) reports a violation.
- Any check failed.

## Draft assessments

A draft, the conformance workflow's `mode: draft`, is for an image still
researching the standard. The profile may be incomplete, the component
definition and requirements absent, and the architectures and evidence files
are then taken from the evidence headers. The evidence is still read strictly.
Gaps are reported as things to do, and changes to the standard since any pinned
revision as drift. A draft claims nothing, never fails, and is never release
eligible; its badge says `draft`, in blue.

## Release eligibility

An image is release eligible only when all of these hold:

1. The evidence is valid, and nothing fails.
2. On every declared architecture, every required criterion is met, or covered
   by an active deviation.
3. No active deviation is about a vulnerability: neither a `vulnerability`
   deviation, nor a criterion deviation from the vulnerability gate, IMG-25.
4. Every decision in the decisions worksheet, when one is given, is reviewed.
5. With `candidates`, every architecture's evidence is about the digest to be
   released.

A criterion deviation, with its owner, reason, and expiry, does not block a
release: that is what a deviation is for. A vulnerability deviation does,
whatever the score, because a known, fixable High or Critical finding is not
something a score can outweigh. The conformance run lists every release
blocker.

## Binding the revision

The workflow that judges, the criteria it judges by, and the revision the
image names must be one:

- `standard-ref` is a full commit, and equals `job.workflow_sha`, the commit in
  the caller's `uses:` line that the workflow actually ran from.
- The standard is checked out at that commit, not at the input.
- The profile's `standard.revision` is that commit or an ancestor of it, and
  nothing the image is judged by has changed since: the criteria, the platform
  expectations, the control baseline, or the source register. A newer revision
  that changed only prose or tooling does not make a profile stale; one that
  changed a criterion does, until someone reassesses.

[`scripts/check-revision.py`](../scripts/check-revision.py) holds these, and
the scorer runs it.

## Badges

The run keeps, for each declared architecture and for `generic`, a standalone
SVG badge and a Shields endpoint file, such as `badge-arm64.svg`:

```text
hardening arm64 | 31/34 · 0123456 · 2026-09-19
```

Each names its scope, the revision, and the day it was scored, so it never
reads as more, or more current, than it is.

Each image publishes its own badges, from its own CI: the
[badges workflow](../.github/workflows/badges.yml) commits them, on every run
on the default branch, to a `badges` branch in the image's repository, and the
image's README points at them. This repository hosts no image's badges but its
own reference image's, published the same way. How to add them is
[Show the badges](ADOPTING.md#8-show-the-badges).

| Colour | Means |
| --- | --- |
| Green | Release eligible |
| Yellow | Valid and passing, not release eligible |
| Red | `failing` |
| Grey | `evidence invalid` |
| Blue | `draft`: a draft assessment, which claims nothing |

## What it must never claim

The score measures conformance to this standard. It is not a compliance score,
an authorization, or a STIG result, and its label must not suggest otherwise.
Nor is it a ranking between images: an image with more criteria met is not more
secure than one with fewer if its deployment ignores the platform
expectations.
