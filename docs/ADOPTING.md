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
| A crosswalk from criteria to requirements | [`requirements-crosswalk.json`](../examples/reference-web-server/requirements-crosswalk.json) | Which of the image's requirements states each criterion |
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
is the pattern. The requirements can live in one file or several, in any
prose the repository already uses.

**Identifiers.** Each requirement is a level-three heading whose identifier
ends in three digits. The prefix is the image's: `### RWS-001` and
`### L1-SUP-001` both match the default pattern, so most repositories need no
pattern of their own. To see what the checks find:

```sh
python ../container-hardening/scripts/check-component.py --requirements docs/*.md --list-requirements
```

If that lists nothing, or not everything, pass `--requirement-pattern` with a
regular expression that captures one identifier per match.

**The crosswalk.** Record which requirement states each criterion, explicitly,
in a file like the reference image's
[`requirements-crosswalk.json`](../examples/reference-web-server/requirements-crosswalk.json):

```json
{"schema": "container-hardening/requirements-crosswalk", "schema_version": 1,
 "criteria": {"IMG-01": ["L1-SUP-001"], "IMG-13": ["L2-RUN-004", "L2-RUN-005"]}}
```

The checks then hold that every required criterion maps to a requirement the
image states, unless the profile records a deviation from it, and that a
control the image claims cites only requirements its criteria map to.

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
| The candidate, release, and published jobs in [`reference-image.yml`](../.github/workflows/reference-image.yml), with [`scripts/publish.py`](../examples/reference-web-server/scripts/publish.py) | IMG-21, IMG-22, IMG-24 | The image name and registry |

### Releasing more than one architecture

The reference image's release is the pattern: build and test each
architecture natively, then publish what was tested without rebuilding it.

1. **Push each verified image by its own digest, untagged**, and confirm the
   registry serves that exact manifest.
2. **Test it again at that digest**, and check it is the image conformance
   judged: its image ID equals the `image_id` in that architecture's evidence.
3. **Push an index naming exactly those digests**, and only the index, so the
   images it names are not copied again and cannot change digest.
4. **Sign the index and every image it names, and attest** each image's bill of
   materials to it and the index's provenance to the index.
5. **Promote by tagging the index's digest**, refusing a version that exists.
6. **Verify from a clean environment**, with no registry credentials, as a
   consumer would.

## 6. Write the component definition

Copy [`scripts/component.py`](../examples/reference-web-server/scripts/component.py).
It takes the standard's [control baseline](controls/README.md) as given, and
asks the image to decide only the controls the baseline leaves
`research-required`, each with a reason. Those depend on what the image does:
a database has accounts and a static server does not.

**Decide these; do not copy them.** The reference image's `DECISIONS` are a
static web server's: no accounts, no sessions, no stored data. An image with
credentials, replication, or a storage API decides each control again, and the
check warns on any decision whose remarks are the reference image's word for
word.

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
      crosswalk: requirements-crosswalk.json
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

## Images the reference does not cover

The reference image is one process, one role, and one container, built from
RPMs. What changes for other shapes:

### More than one role

An image that runs as different roles, such as a server and its workers,
declares them in its profile:

```json
"roles": ["server", "worker"]
```

Each role then has its own behaviour declaration, with the processes,
listeners, health check, secrets, and writable paths of that role, and its own
runtime evidence: every architecture-scoped evidence file is written once per
role, naming the role in its subject. A per-architecture criterion is met only
when it is met for every role; one role's pass never covers another's gap.
Evidence about the source or the process, in a generic file, names no role.

### Standalone and clustered

What a single container's tests show is the image's half: that each role runs
restricted, listens where it declares, reads its secrets from files, and fails
closed. They cannot show replication, or that the components authenticate and
encrypt the traffic between them. That is the platform's half, stated in
[PLT-10](standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) and
[PLT-18](standard/platform.md#plt-18-workloads-have-identities-and-authenticate-each-other),
and is shown by deploying the image as it runs clustered.

Record the topology an evidence file was produced in, by declaring
`"topologies": ["standalone", "clustered"]` and naming one in each
architecture-scoped subject. Keep evidence from a clustered deployment
separate from the image's own, and do not claim a platform expectation as an
image criterion.

### Inputs that are not RPMs

[IMG-02](standard/criteria.md#img-02-every-build-input-pinned-and-verified)
keeps three claims apart. Record each input under the strongest one it has,
and say which:

| Evidence | What it shows | Where it belongs |
| --- | --- | --- |
| The publisher's signature, verified against a pinned key or identity | Who published it, and that it is unchanged | The integrity control |
| A digest recorded in the lock when it was reviewed | That it is unchanged since review; not who published it | The integrity control, stated as review, not provenance |
| A checksum published beside it, such as an `.md5` file | Neither | Metadata at most; never the integrity control |

For an input taken from an upstream container image:

1. **Pin the image by digest** in the lock, with the publisher's signing
   identity and issuer.
2. **Verify the signature at that digest** with `cosign verify
   --certificate-identity ... --certificate-oidc-issuer ...`, in the networked
   acquisition step, before anything is read from it. A tag is never verified;
   a digest is.
3. **Extract only the files the image needs**, from a container created from the
   verified digest, and record each file's size and SHA-256 in the lock.
4. **Build from the extracted files**, which the build verifies against the lock
   again, with networking disabled, as for any other input.

An upstream archive with no signature is pinned by the digest recorded when it
was reviewed, and the lock says so. The reference image has an example of that
kind: its scanner images are pinned by digest and not signature-verified, and
its [tools](../examples/reference-web-server/tools.json) by archive digest.

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
