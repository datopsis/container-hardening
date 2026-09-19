# Adopting the standard

What an image repository adds, in order, to align with this standard and show
that it does. The [reference web server](../examples/reference-web-server/README.md)
has done every step; each step below points at its copy.

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
| `standard.revision` | The commit from step 1 |
| `function` | What the image does, in a sentence a reviewer can check |
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

Every check writes a JSON file with a `results` list, each entry naming the
criterion it establishes:

```json
{"results": [{"criterion": "IMG-13", "check": "every process has an empty effective capability set", "passed": true}]}
```

`passed` is `true`, `false`, or `null` for a check that could not run where it
ran; a `null` never counts as met. Upload the files as one artifact.

The reference image's checks can be copied and adapted:

| Copy | Establishes | Adapt |
| --- | --- | --- |
| [`scripts/acquire.py`](../examples/reference-web-server/scripts/acquire.py), [`scripts/build.py`](../examples/reference-web-server/scripts/build.py), [`lock.json`](../examples/reference-web-server/lock.json) | IMG-01 to IMG-03 | The packages, module streams, and omissions |
| [`tests/build_checks.py`](../examples/reference-web-server/tests/build_checks.py) | IMG-01 to IMG-05 | Nothing, beyond paths |
| [`tests/smoke.py`](../examples/reference-web-server/tests/smoke.py) | IMG-06 to IMG-20, IMG-27, IMG-30, IMG-32 | The service's probes, paths, secrets, and failure cases |
| [`tools.json`](../examples/reference-web-server/tools.json), [`scripts/install_tools.py`](../examples/reference-web-server/scripts/install_tools.py), [`tests/gates.py`](../examples/reference-web-server/tests/gates.py) | IMG-21, IMG-25, IMG-28, IMG-34 | Nothing |
| [`scripts/drift.py`](../examples/reference-web-server/scripts/drift.py) and a read-only scheduled workflow | IMG-04, IMG-29 | Nothing |
| The release job in [`reference-image.yml`](../.github/workflows/reference-image.yml) | IMG-21, IMG-22, IMG-24 | The image name |

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
    needs: verify            # the job that uploads the evidence
    uses: datopsis/container-hardening/.github/workflows/conformance.yml@<commit>
    with:
      standard-ref: <commit>
      requirements: requirements.md
      requirement-pattern: '^###\s+(RWS-\d{3})\s*$'
      evidence-artifact: evidence
```

It fails if the profile names a different revision, if the profile or the
component definition breaks a rule, or if any check failed. Otherwise it
scores the image, and keeps the score and a badge with the run.

## 8. Keep aligned

- **Deviations expire.** The check fails on the expiry date; close the gap or
  record a new decision.
- **Sources move.** When this repository pins a new release of a conditional
  source, every determination against the old digest fails until someone
  reviews it again.
- **The standard moves.** Updating the pinned commit is a pull request, and
  the checks show what changed for the image.

## What the score means

`hardening 28/34` means 28 of the 34 required criteria are met with passing
evidence and no active deviation. It is conformance to this standard. It is not
a compliance score, an authorization, or a STIG result, and it is not a
ranking between images.
