# Tailoring the standard to an image

One standard, applied to every image, tailored per application rather than
reinvented per application. This is how the tailoring is recorded, and what
stops it becoming a way to quietly opt out.

Each image repository keeps a **hardening profile**, a JSON file checked in CI
by [`scripts/check-profile.py`](../scripts/check-profile.py) from a pinned
revision of this repository. A worked example for `nginx-ubi` is in
[`examples/nginx-ubi.hardening-profile.json`](../examples/nginx-ubi.hardening-profile.json).
The reasoning is [ADR-0005](adr/0005-tailor-by-profile-deviations-expire.md).

## What every image takes

**Every image takes every required criterion**, and the
[control baseline](controls/README.md) as its starting point. There is no
image-level "profile" that selects a subset. An image that cannot meet a
criterion records a [deviation](#deviations), which expires. It does not
narrow its scope.

That is deliberate. A menu of criteria invites each image to pick what it
already does. A single bar with visible, expiring exceptions keeps the gaps
where a reader can see them.

What does vary per image is:

1. **Which conditional sources apply.** A web server takes the Web Server SRG;
   an image hosting an application runtime takes the Application Server SRG.
2. **The 57 `research-required` controls** the baseline leaves to each image,
   decided in the image's own
   [component definition](CONTROL-MODEL.md#what-an-images-component-definition-must-do).
3. **Deviations**, each temporary.

## Applicability

A source with the role `conditional` in the
[register](../artifacts/sources.json) applies only to images of a particular
function. **Every image records a determination for every conditional source**:
whether it applies, and why. Leaving one out is a violation, because an absent
determination is indistinguishable from a forgotten one.

| Field | Meaning |
| --- | --- |
| `source` | The register `id` |
| `release`, `sha256` | The revision the determination was made against |
| `applies` | `true` or `false` |
| `basis` | Why, in terms a reviewer can check, such as counts of rules whose subject the image lacks |
| `evidence` | Where the full reasoning lives, usually the image's own ADR |
| `reviewed_on`, `reviewed_by` | When, and by whom |

The determination is tied to the revision's digest. When DISA publishes a new
release and the register's pin moves, every determination made against the old
digest becomes a violation until someone reviews it against the new one. A
not-applicable finding against V4R5 says nothing about V4R6, which may have
broadened its scope.

A source that applies but is not yet rendered produces a warning: it is in
scope, but its rules cannot be traced until it is rendered.

### The worked example

`nginx-ubi` serves and proxies HTTP. It has no management interface, no
accounts, and no application runtime. Its determination for the Application
Server SRG, first made in its
[ADR-0010](https://github.com/datopsis/nginx-ubi/blob/main/docs/adr/0010-application-server-srg-not-applicable.md):

```json
{
  "source": "disa-application-server-srg",
  "release": "V4R5",
  "sha256": "ea33d7f18f950e86c9e0cc63835cf8802d319804ac143b2020b1fbac13ff2643",
  "applies": false,
  "basis": "Of the 137 rules in V4R5, 27 presuppose a management interface or hosted applications and 18 refer to accounts. This image has none of those ...",
  "evidence": "https://github.com/datopsis/nginx-ubi/blob/main/docs/adr/0010-application-server-srg-not-applicable.md",
  "reviewed_on": "2026-09-18",
  "reviewed_by": "Joey"
}
```

What makes it a good determination is that it can be checked. It names the
revision, it counts the rules whose subject does not exist in the image, and
it names the source that does apply instead. "Not a web application" would be
a conclusion; this is evidence for one.

### How a determination is reviewed

A determination is a change to the image's profile, so it is reviewed as a
pull request in the image's repository. The reviewer checks three things:

1. The `sha256` is the register's current pin for that source.
2. The `basis` is specific enough to be wrong: a count, a list of the objects
   the source governs that the image lacks, or a statement of function a
   reader could dispute.
3. The inverse holds. If the source does not apply, something else covers the
   function; if it applies, the image's criteria and controls reflect it.

## Deviations

A deviation is a recorded, temporary departure from the standard. It is one
mechanism for three situations:

| `kind` | `target` | For |
| --- | --- | --- |
| `criterion` | A required criterion, such as `IMG-14` | The image does not yet meet it |
| `control` | A baseline control, such as `cm-6` | The image's component definition takes a different origination from the baseline; the deviation states which, in `origination` |
| `vulnerability` | A `CVE-` or `GHSA-` identifier | A finding that will not be fixed within the [remediation timeline](standard/criteria.md#img-25-vulnerability-gate-and-remediation); scoped to one image `digest`. This is the exception register [IMG-26](standard/criteria.md#img-26-exceptions-expire) requires |

Every deviation carries:

| Field | Meaning |
| --- | --- |
| `id` | `DEV-001`, unique within the profile |
| `kind`, `target` | What it departs from |
| `reason` | Why the image cannot meet it now |
| `compensating` | What is done instead, or `None` stated plainly |
| `owner` | Who will close it |
| `approved_by` | Who accepted it |
| `recorded_on`, `expires_on` | When it was accepted, and when it stops being accepted |

```json
{
  "id": "DEV-001",
  "kind": "criterion",
  "target": "IMG-14",
  "reason": "The smoke suite does not yet read listening sockets from /proc.",
  "compensating": "Every declared port is 1024 or above, and the image runs with every capability dropped.",
  "owner": "Joey",
  "approved_by": "Joey",
  "recorded_on": "2026-09-18",
  "expires_on": "2027-03-17"
}
```

This example is illustrative. It is not a deviation any image has recorded.

### Deviations expire

**A deviation with no expiry is a permanent exception nobody decided on.** So
every deviation has one, and it is bounded when it is recorded:

| Kind | Longest allowed |
| --- | --- |
| `criterion`, `control` | 180 days |
| `vulnerability` | 90 days |

A vulnerability deviation is bounded more tightly because the remediation clock
was already running before the deviation was recorded.

On the expiry date the deviation stops being honoured, and the image fails its
checks until the gap is closed or a new deviation is recorded. A new deviation
is a new decision, with a new `id`, a fresh reason, and a reviewer who can see
the old one expired. Extending the date on an existing one is the same edit as
recording a new one, and is reviewed as one. A deviation within 14 days of
expiry draws a warning.

### What a deviation changes

[`check-component.py --profile`](../scripts/check-component.py) honours active
deviations:

- a `control` deviation lets the component definition take the stated
  origination instead of the baseline's
- a `criterion` deviation excuses that criterion from the controls that would
  otherwise have to cite it, and **forbids** any control from citing it, since
  the image has said it does not meet it

A deviation cannot target a `research-required` control, which the image
decides itself, or a target criterion, which is not yet required of anyone.

## Running it

From an image repository, against a pinned revision of this one:

```sh
python ../container-hardening/scripts/check-profile.py artifacts/hardening-profile.json
python ../container-hardening/scripts/check-component.py \
    artifacts/oscal/component-definition.json \
    --requirements docs/L1-REQ.md docs/L2-REQ.md docs/L3-REQ.md \
    --profile artifacts/hardening-profile.json
```

`standard.revision` in the profile records the commit of this repository the
image was checked against, so a reader can reproduce the check. Both scripts
take `--today` to evaluate expiry as of a given date.

## Enforcement

`tests/test_tailoring.py` checks the worked example against the current
register and baseline, and builds profiles that each break one rule, to show
each rule fails when it should. In each image repository, enforcement is that
repository running both checks in CI.
