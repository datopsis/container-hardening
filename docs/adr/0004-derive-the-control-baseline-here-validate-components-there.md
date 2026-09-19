---
status: accepted
date: 2026-09-18
decision-makers: Joey
---

# Derive the control baseline here, and validate each image's component there

## Context and Problem Statement

Each Datopsis image has to say, for every NIST SP 800-53 control in the High
baseline, whether it satisfies the control, hands it to someone else, or does
not apply. The model for saying so has six origination values, a
responsible role, and a verification pointer on anything the image claims.
Writing the model is quick; applying it is not. An image that authors its own
determinations one control at a time makes a handful and stops.

Hand-authoring 370 determinations per image is roughly 1,850 decisions across
five images. Most of them would be identical across images, since
personnel security is organizational for all of them, and would drift apart the
moment anyone edited one. The question is where the determinations live.

## Decision Drivers

* An image repository must be able to evidence what it claims, so the claim
  itself belongs next to the evidence
* A determination that is the same for every image should be made once
* A standard that changes should change every image's starting point, visibly
* A difference between one image and the standard must be a recorded decision,
  not an accident of editing
* Most determinations follow from the standard already: a criterion anchored to
  an SRG rule that reaches a control is a claim about that control

## Considered Options

* **Each image authors its own** — every repository writes all 370
* **This repository authors every image's component definition** — central
  ownership of every claim
* **Generate complete component definitions here, copy into each image** —
  one source, vendored
* **Derive a baseline here; each image keeps its own component definition,
  checked against the baseline** — shared starting point, local claims

## Decision Outcome

Chosen option: **derive a baseline here; each image keeps its own component
definition, checked against the baseline.**

This repository holds the control baseline: an origination for every control
in the High baseline and every further control the standard reaches. It is
derived from the criteria and expectations through the crosswalk, with a
determinations file for the cases where derivation would be wrong. Each image
repository holds its own OSCAL component definition and runs
`scripts/check-component.py` from a pinned revision of this repository against
it.

*Each image authors its own* makes a handful and stops. It keeps every claim
next to its evidence, which is right, and leaves every image to rediscover the
same 300 answers, which is not.

*Central ownership* was rejected because this repository cannot evidence
anything about an image. An `image-owned` claim with no requirement in the
image's own repository behind it is exactly the unverified assertion the
verification pointer exists to prevent.

*Generate and copy* was the closest alternative. It lost on drift. A vendored
file edited locally diverges silently, and nothing distinguishes a deliberate
local change from an accidental one. A check against a pinned baseline makes
every difference visible, and the Package 4 deviation mechanism makes each one
a recorded decision with an expiry.

### Consequences

* Good: 322 of 379 controls are settled once, for every image, and derived
  rather than asserted
* Good: an image decides only the 57 controls that depend on its function,
  such as accounts, authentication, and session handling
* Good: changing a criterion changes every image's baseline in one pull
  request, and the checker then shows each image what it must now say
* Bad: every image repository takes a dependency on a pinned revision of this
  one, and must update the pin to pick up a changed baseline
* Bad: an image that disagrees with the baseline fails its check until Package
  4 defines how a deviation is recorded
* Bad: derivation is only as good as the anchors. A criterion anchored to a
  loosely fitting rule produces a loosely fitting claim, which is why the
  determinations file exists and why each override carries a reason

### Enforcement

`tests/test_controls.py` re-derives the committed baseline from the committed
standard, crosswalk, and determinations on every pull request, and fails if they
disagree. It also runs the checker against component definitions constructed to
break each of its rules.

`build-control-baseline.py` refuses a determination that repeats derivation,
an `image-owned` control with no required criterion, a handoff naming no
expectation, and expectations that disagree without a determination.

In each image repository, enforcement is that repository running
`check-component.py` in CI. That is adoption work, tracked under Package 5.
