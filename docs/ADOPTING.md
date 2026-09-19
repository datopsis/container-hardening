# Adopting the standard

What an image repository adds, in order, to align with this standard and show
that it does. The [reference web server](../examples/reference-web-server/README.md)
in this repository has done every step; each step below points at its copy,
and the fastest route is to copy that directory and change it.

## In short

An adopting image repository ends up with these, each copied from the
reference image and changed for its own service:

| Add | Copy from the reference image | You change |
| --- | --- | --- |
| A hardening profile | [`hardening-profile.json`](../examples/reference-web-server/hardening-profile.json) | Image name, function, the pinned commit, architectures, expected evidence, applicability, deviations |
| Requirement statements | [`requirements.md`](../examples/reference-web-server/requirements.md) | The wording, an identifier prefix, and the checks that verify each |
| A locked, hermetic build | [`lock.json`](../examples/reference-web-server/lock.json), [`scripts/acquire.py`](../examples/reference-web-server/scripts/acquire.py), [`scripts/build.py`](../examples/reference-web-server/scripts/build.py), [`Containerfile`](../examples/reference-web-server/Containerfile) | The packages and what the image ships |
| Checks that write evidence | [`tests/`](../examples/reference-web-server/tests/), [`tools.json`](../examples/reference-web-server/tools.json), [`scripts/drift.py`](../examples/reference-web-server/scripts/drift.py) | The runtime probes in `smoke.py` for the service |
| A behaviour declaration | [`behaviour.json`](../examples/reference-web-server/behaviour.json) | Processes, listeners, writable paths, outbound destinations |
| A component definition | [`scripts/component.py`](../examples/reference-web-server/scripts/component.py) | Decisions for the controls the baseline leaves to the image |
| CI | [`reference-image.yml`](../.github/workflows/reference-image.yml) and a call to [`conformance.yml`](../.github/workflows/conformance.yml) | The image name and paths |

**It is done when** the conformance workflow passes in the image repository's
CI and reports the image **release eligible**: valid evidence, nothing failing,
and every required criterion on every architecture met or covered by a
recorded deviation with an expiry. That is what makes the image aligned rather
than finished. The reference image reports `hardening amd64 31/34` and is
release eligible, because its three gaps are deviations.

A passing run that is not yet release eligible is progress, not alignment:
conformance lists what blocks the release.

Nothing here requires the image to meet every criterion on day one. It
requires every gap to be visible: a criterion the image does not yet meet is a
[deviation](TAILORING.md#deviations), with a reason and an expiry, and the
score says so.

## 1. Pin a revision of this standard

Choose a full commit of this repository's `main` branch. Every file below
names it, and every check runs against it. Moving to a newer revision is a
pull request in the image repository, like any other input change.

## 2. Read what the image must do

- [The standard](standard/README.md): what a hardened image is, and why.
- [The criteria](standard/criteria.md): each requirement, its implementation,
  its verification, the result expected, and the evidence it leaves.
- [The platform expectations](standard/platform.md): what the platform must do,
  which the image cannot, and must not claim.

## 3. Add a hardening profile

Copy [`hardening-profile.json`](../examples/reference-web-server/hardening-profile.json)
and change it for the image:

| Field | What to put |
| --- | --- |
| `image` | The image's name |
| `schema_version` | `2` |
| `standard.revision` | The commit from step 1 |
| `function` | What the image does, in a sentence a reviewer can check |
| `architectures` | The architectures it is built for: `amd64`, `arm64`, or both |
| `evidence` | Each evidence file its CI writes, with its scope: `architecture` for a file written once per architecture, `generic` for one written once |
| `applicability` | A determination for **every** conditional source in the [register](../artifacts/sources.json), pinned to its digest, with its basis |
| `deviations` | One for each criterion the image does not yet meet, each expiring within 180 days |

Check it with:

```sh
python ../container-hardening/scripts/check-profile.py hardening-profile.json
```

## 4. State the image's requirements

Write one requirement per criterion, in the image's own words, naming the
check that verifies it: [`requirements.md`](../examples/reference-web-server/requirements.md)
is the pattern. Choose an identifier prefix and a heading form, such as
`### RWS-001`; the checks find them with a regular expression you supply.

This is the verification pointer: a control the image claims cites both the
standard's criterion and the image's own requirement.

## 5. Produce evidence in CI

Every check writes a JSON file in the shape [Evidence](EVIDENCE.md) defines: a
header saying which commit, run, architecture, and image it is about, and a
`results` list in which each check has a stable id and names the criterion it
establishes:

```json
{"id": "smoke.no-effective-capabilities", "criterion": "IMG-13",
 "check": "every process has an empty effective capability set", "passed": true}
```

`passed` is `true`, `false`, or `null` for a check that could not run where it
ran, with the reason in `detail`; a `null` never counts as met, and any other
value makes the evidence invalid. The reference image's
[`tests/evidence.py`](../examples/reference-web-server/tests/evidence.py)
writes the header for you.

Build and test each architecture natively, and upload each architecture's
evidence as its own artifact, such as `evidence-amd64` and `evidence-arm64`.
Evidence about a built image is per architecture; a passing result on one never
stands for another.

The reference image's checks can be copied and adapted:

| Copy | Establishes | Adapt |
| --- | --- | --- |
| [`scripts/acquire.py`](../examples/reference-web-server/scripts/acquire.py), [`scripts/build.py`](../examples/reference-web-server/scripts/build.py), [`lock.json`](../examples/reference-web-server/lock.json) | IMG-01 to IMG-03 | The packages, module streams, and omissions |
| [`tests/build_checks.py`](../examples/reference-web-server/tests/build_checks.py) | IMG-01 to IMG-05 | Nothing, beyond paths |
| [`tests/smoke.py`](../examples/reference-web-server/tests/smoke.py) | IMG-06 to IMG-20, IMG-27, IMG-30, IMG-32 | The service's probes, paths, secrets, and failure cases |
| [`tools.json`](../examples/reference-web-server/tools.json), [`scripts/install_tools.py`](../examples/reference-web-server/scripts/install_tools.py), [`tests/gates.py`](../examples/reference-web-server/tests/gates.py) | IMG-21, IMG-25, IMG-28, IMG-34 | Nothing |
| [`scripts/drift.py`](../examples/reference-web-server/scripts/drift.py) and a read-only scheduled workflow | IMG-04, IMG-29 | Nothing |
| The release job in [`reference-image.yml`](../.github/workflows/reference-image.yml) | IMG-21, IMG-22, IMG-24 | The image name. It builds one architecture |

## 6. Write the component definition

Copy [`scripts/component.py`](../examples/reference-web-server/scripts/component.py).
It takes the standard's [control baseline](controls/README.md) as given, and
asks the image to decide only the controls the baseline leaves
`research-required`, each with a reason. Those depend on what the image does:
a database has accounts and a static server does not.

## 7. Call the conformance workflow

```yaml
jobs:
  conformance:
    needs: verify            # the jobs that upload the evidence
    if: ${{ !cancelled() }}
    uses: datopsis/container-hardening/.github/workflows/conformance.yml@<commit>
    with:
      standard-ref: <the same commit>
      requirements: requirements.md
      evidence-artifacts: evidence-*
      # requirement-pattern: only if headings are not like "### RWS-001" or "### L1-SUP-001"

  release:
    needs: conformance
    if: needs.conformance.outputs.release-eligible == 'true'
```

`standard-ref` must be the full commit in the `uses:` line; the workflow checks
it against the commit it actually ran from. It fails on invalid evidence, a
revision that does not bind, a profile or component that breaks a rule, or a
failed check. Otherwise it scores each architecture and keeps the score and a
badge per architecture with the run. Its outputs are `evidence-valid`,
`failing`, `coverage`, `score`, and `release-eligible`; gate a release on the
last, never on the run succeeding.

## 8. Keep aligned

- **Deviations expire.** The check fails on the expiry date; close the gap or
  record a new decision.
- **Sources move.** When this repository pins a new release of a conditional
  source, every determination against the old digest fails until someone
  reviews it again.
- **The standard moves.** Updating the pinned commit is a pull request, and
  the checks show what changed for the image. The profile's revision need not
  move with every commit: it stays valid until the criteria, platform
  expectations, baseline, or register change, and then conformance fails until
  the image is reassessed.

## What the score means

`hardening arm64 28/34` means 28 of the 34 required criteria are met on the
arm64 image with passing evidence and no active deviation. It is conformance to
this standard, on that architecture, on the day and at the revision the badge
names. It is not release eligibility, which is a separate answer; it is not a
compliance score, an authorization, or a STIG result; and it is not a ranking
between images. See [Evidence](EVIDENCE.md).
