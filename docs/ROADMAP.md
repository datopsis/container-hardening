# Roadmap

This repository defines the criteria, implementation, and controls used in
every Datopsis container build and for the platform those containers run on.
The point is a standardised process applied across repositories, tailored per
application rather than reinvented per application.

A checked item requires reviewable evidence in a pull request or workflow run.
Completed items are deleted rather than checked off, so this file is always the
remaining work. What already exists is recorded in the section below.

## What this repository is

Three things, in dependency order:

1. **Rendered requirement catalogues.** The DISA packages this standard maps
   against, converted to reviewable Markdown, one file per rule.
2. **The hardening standard.** A readable account of what a hardened Datopsis
   container image is and why, written to be used rather than filed.
3. **The control mapping.** What each image contributes to a control, what it
   hands off, and to whom — generated and cross-referenced rather than
   hand-asserted.

It is not a scanner, not a base image, and not an authorization package. It is
the shared definition those things are measured against.

## Documentation model

Two reference points, and the difference between them matters.

[Ignyte's SRG browser](https://www.ignyteplatform.com/stigs/Container_Platform_Security_Requirements_Guide)
is a per-rule catalogue: complete, addressable, and useful when you already
know which rule you need. That is what `docs/srg/` generates.

[Minimus's STIG hardening write-up](https://www.minimus.io/post/stig-hardening-for-container-images)
is the one to emulate for the standard itself: it explains what hardening
actually means for a container image, in prose an engineer reads once and
applies, rather than a rule dump. **The catalogue is generated; the standard is
written.** Conflating them produces a document nobody reads.

## Source packages are never committed

The DISA packages are US Government works whose distribution terms live inside
the package, and they are large binary-heavy trees. `.gitignore` excludes
`U_*_SRG/`, `U_*_STIG/`, `sources/`, and `*.zip`.

What is committed is the generated Markdown. Every source is pinned by SHA-256
in `artifacts/sources.json`, so a mapping is always made against a known
revision and a replaced package is visible rather than silent.

## Requirement sources

| Source | Release | Role | Rendered |
| --- | --- | --- | --- |
| NIST SP 800-53 Rev 5 catalogue | 5.2.0 | Spine | n/a |
| NIST SP 800-53 Rev 5 High baseline | 5.2.0 | Baseline | n/a |
| DISA CCI list | 2025-01-23 | Crosswalk | [Joined, 106 controls](crosswalk/README.md) |
| DISA Container Platform SRG | V2R4 | Platform controls | Yes, 188 rules |
| DISA GPOS SRG | V3R3 | **Image controls** | Yes, 203 rules |
| DISA Container Hardening Process Guide | V1R2 | Process guide | n/a, prose |
| NIST SP 800-190, Application Container Security Guide | Final, 2017 | Process guide | [Mapped, 24 countermeasures](standard/nist-800-190.md) |
| DISA RHEL 9 STIG | V2R4 | Host controls | Not yet |
| DISA Web Server SRG | V3R3 | Conditional | Yes, 102 rules |
| DISA Application Server SRG | V4R5 | Conditional | Yes, 137 rules |
| CIS Benchmarks | — | Cross-reference | Never — terms forbid it |

**The GPOS SRG carries image-level controls.** Per DoD guidance it is used to
assess image-level controls in the absence of a container-specific STIG, which
is the situation for every image this standard covers. It is not a stand-in for
the Container Platform SRG; that one governs the platform, and most of it will
originate as host-inherited for any image.

A **conditional** source applies only to images of a particular function. The
Web Server SRG applies to an image that serves or proxies HTTP; the Application
Server SRG to one that hosts an application runtime, and not to an image with
no management interface, hosted applications, or accounts, which is what much
of it presupposes. Recording why a source does not apply is part of the
standard, not an omission from it.

## Package 1: sources and rendering

- [ ] Render the RHEL 9 STIG, which is pinned but not yet converted. Its
  XCCDF digest must be pinned in the register first; the renderer skips a
  package whose XCCDF is not.
- [ ] Extend the weekly source verification to probe adjacent releases. It
  confirms a pinned package is unchanged, which is not the same as confirming
  it is current: DISA serves superseded releases alongside current ones, so a
  `200` is not evidence of currency. A newer release should be reported.
- [ ] Decide how a release upgrade is reviewed. The per-rule file layout exists
  so the diff shows exactly which rules changed; that diff should be the review
  artifact, with an explicit record of what changed and what it means for each
  adopting repository.
- [ ] Obtain the CIS Kubernetes and OpenShift benchmarks via an account holder
  and record their digests. They can be cited by identifier but never rendered;
  their terms are non-commercial and ShareAlike.
- [ ] Render the DISA Kubernetes STIG V2R6 and OpenShift STIG V2R6, pinned but
  not yet converted, and add them to the crosswalk. They instantiate the
  Container Platform SRG for each product, so platform expectations can then
  cite product rules as well.
- [ ] Map NIST IR 8176, the DISA Container Image Creation and Deployment Guide,
  and the NSA/CISA Kubernetes Hardening Guide countermeasure by countermeasure,
  as SP 800-190 is, with a test that fails on any unmapped item.

## Package 2: the hardening standard

- [ ] Agree a GPOS-derived OpenSCAP rule selection, so that
  [IMG-T3](standard/criteria.md#img-t3-compliance-scan) can become required.
  It is built first as the reference image's SCAP tailoring, starting from the
  SCAP Security Guide's RHEL 9 DISA STIG profile with host-only rules removed.

- [ ] Decide how an image whose own function protects CUI meets FIPS 140-3: the
  standard makes no FIPS claim for images, and a platform secret store must use
  a validated module, but an image that encrypts data itself needs a position.

## Package 3: the control mapping

- [ ] Review the 125 determinations in
  [`artifacts/control-determinations.json`](../artifacts/control-determinations.json).
  They are judgement calls, each with its reason, and have not yet had a
  second reader. Start with the nine that make a control `image-owned` by
  determination rather than derivation: AC-6, CM-2, CM-2(2), CM-2(3), CM-8,
  CM-8(1), CM-8(2), CM-11, and SI-7(15).

## Package 4: per-application tailoring

- [ ] Pin a conditional source for each image function the register does not
  yet cover. Databases have none; the DISA Database SRG is the likely
  candidate. Object storage and API or catalog services likewise need their
  function's source identified. Each image would then record a determination
  for it.

## Package 5: adoption

The [reference web server](../examples/reference-web-server/README.md) is the
template every image adopts from. It records what it does not yet evidence as
deviations in its profile; each item below closes some of them.

- [ ] Release the reference image: attest its bill of materials, sign it with a
  keyless identity with SLSA provenance, and publish immutable tags (IMG-21,
  IMG-22, IMG-24). Publishing needs a decision on where. Add its OSCAL
  component definition and criteria evidence file, and compute its score.
- [ ] Build the reference image's SCAP profile: the SCAP Security Guide's RHEL 9
  DISA STIG profile, pinned, tailored for an image, with each rule tied to the
  GPOS SRG rule it serves. It is what lets IMG-T3 become required.
- [ ] Deploy the reference image under the Restricted Pod Security Standard in
  CI (IMG-31), and on OpenShift under `restricted-v2` and `restricted-v3` when a
  cluster is available.
- [ ] Refuse a group- or world-readable key file at startup without a shell in
  the runtime path (IMG-16). nginx refuses a missing or empty key, not a
  permissive one.
- [ ] Adopt in the image repositories, in the order and with the per-repository
  notes in [adoption](adoption/README.md#planned-order).
- [ ] Add a hardening profile to each image repository and run
  `scripts/check-profile.py` in its CI.
- [ ] Run `scripts/check-component.py` in each image repository's CI, against a
  pinned revision of this one.
- [ ] Close the gaps in the [adoption snapshot](adoption/snapshot-2026-09-18.md),
  then delete it: each image repository tracks its own from then on.
- [ ] Build the [conformance score and badge](adoption/README.md#plan-a-conformance-score-and-badge):
  `scripts/score.py`, and a criteria evidence file in each image repository
  mapping every required criterion to the tests that establish it.

## Package 6: publication

- [ ] Decide whether the rendered catalogue and standard are published as a
  site or consumed as Markdown in the repository. Both reference points are
  sites; neither is necessary for the content to be useful.
- [ ] Add link checking and Markdown linting to CI. Register validation and
  weekly source verification are in place.
- [ ] Protect `main` and require the checks.

## What the scaffold already established

- `scripts/build-srg-markdown.py` converts a DISA XCCDF package into one
  Markdown file per rule, with `--check` for drift. 630 rules across four
  catalogues render today, and only packages whose XCCDF digest is pinned are
  rendered.
- `docs/srg/` holds the generated Container Platform SRG V2R4, GPOS SRG V3R3,
  Web Server SRG V3R3, and Application Server SRG V4R5.
- `artifacts/sources.json` pins eleven sources by digest, recording for each its
  role, whether it has been rendered, and whether it may be redistributed. All
  ten retrievable sources were verified against their recorded digests on
  2026-09-18.
- `scripts/build-cci-crosswalk.py` joins every rendered rule's CCIs to 800-53
  Rev 5 through the pinned DISA CCI list, resolved against the pinned OSCAL
  catalogue. `docs/crosswalk/` and `artifacts/crosswalk.json` hold the result:
  120 distinct controls across the four rendered SRGs. Every cited CCI resolved
  and none was deprecated; three Web Server SRG rules cite CCIs that DISA maps
  only to Revision 4 controls Revision 5 withdraws, which the crosswalk reports
  as findings rather than dropping. See
  [ADR-0002](adr/0002-derive-800-53-cross-references-from-cci.md).
- `scripts/verify-sources.py` re-verifies those digests and never edits the
  register: a replaced release is a finding to read, not a digest to update.
  It reports unreachable separately from changed, because reaching nothing says
  nothing.
- CI validates the register and the internal consistency of the rendered
  catalogues on every pull request; `verify-sources.yml` compares the committed
  Markdown against the real packages weekly.
- `.gitignore` keeps source packages out of the repository.
- [`docs/standard/`](standard/README.md) holds the standard: the prose account,
  30 required image criteria and three targets, 17 platform and 4 host
  expectations, a countermeasure-by-countermeasure mapping of NIST SP 800-190,
  and a comparison with the DISA Container Hardening Process Guide.
  `tests/test_standard.py` checks that
  every cited SRG rule reaches the 800-53 control cited beside it, that image
  criteria cite only image rules and platform expectations only platform rules,
  and that every link and anchor resolves.
- [`docs/CONTROL-MODEL.md`](CONTROL-MODEL.md) defines the control model: six
  originations, matching roles, and a verification pointer naming both a
  standard criterion and a requirement the image states. [`docs/controls/`](controls/README.md) holds the
  derived baseline for 379 controls: 20 image-owned, 13 deployment-configured,
  50 host-inherited, 228 organization-inherited, 11 not applicable, and 57
  left to each image. `scripts/check-component.py` checks an image's OSCAL
  component definition against it.
- [`examples/reference-web-server/`](../examples/reference-web-server/README.md)
  is a generic nginx 1.26 image on UBI 9 Micro, built from eight locked, signed
  RPMs with networking disabled. CI shows a tampered or missing input stops the
  build, verifies the running image against 41 checks, scans the source before
  the build, and gates the image on fixed High and Critical vulnerabilities,
  malware, and a base more than 30 days behind, with pinned, verified
  scanners. A weekly job reports drift without changing anything.
- [`docs/TAILORING.md`](TAILORING.md) defines the hardening profile each image
  keeps: an applicability determination for every conditional source, tied to
  its pinned digest, and deviations that each expire. `scripts/check-profile.py`
  checks it, and `check-component.py --profile` honours active deviations. The
  reference web server's profile is the worked example, and its Application
  Server SRG determination rests on this repository's own
  [analysis](applicability/application-server-srg.md) of the rendered rules.

Two findings from building it, recorded so they are not rediscovered:

**A STIG ID is not a unique key.** GPOS V3R3 issues
`SRG-OS-000132-GPOS-00067` as two distinct rules, `V-203655` and `V-278973`.
Rule pages are filed by Group ID, and the generator refuses to overwrite rather
than silently dropping a rule.

**DISA serves superseded releases alongside current ones.**
`U_GPOS_V2R7_SRG.zip` still returns `200` while V3R3 is current. Retrievability
never establishes currency; only checking adjacent releases does.
