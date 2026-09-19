# Changelog

All notable changes to this project are recorded in this file.

The project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- Established the repository: the criteria, implementation, and controls used
  in every Datopsis container build, and the expectations placed on the
  platform those containers run on.
- Added `scripts/build-srg-markdown.py`, which renders a DISA XCCDF package
  into one Markdown file per rule with a `--check` mode for drift. One file per
  rule is deliberate: a release upgrade then produces a diff naming exactly
  which rules changed, and that diff is the review artifact.
- Rendered the DISA Container Platform SRG V2R4 (188 rules) and the DISA GPOS
  SRG V3R3 (203 rules) into `docs/srg/`.
- Established `artifacts/sources.json`, pinning nine requirement sources by
  SHA-256 with role, rendering state, licence, and redistribution terms. All
  eight retrievable sources were verified against their recorded digests.
- Recorded that the GPOS SRG carries image-level controls: per DoD guidance it
  assesses those where no container-specific STIG exists, which is the case for
  every image this standard covers. The Container Platform SRG governs the
  platform and is not a substitute.
- Added `scripts/verify-sources.py` and a weekly workflow that re-verifies each
  pinned digest and confirms the committed Markdown still matches the packages.
  It never edits the register, and reports unreachable separately from changed.
- Added structural checks over the register and the rendered catalogues that
  run without the source packages present, so pull-request CI can verify a
  regeneration without reaching the public internet.
- Recorded [ADR-0001](docs/adr/0001-render-catalogues-never-commit-packages.md):
  render catalogues to Markdown, never commit the source packages.
- Pinned the DISA CCI list (2025-01-23) and added
  `scripts/build-cci-crosswalk.py`, which derives SRG-to-800-53 Rev 5
  cross-references by joining each rule's CCIs to DISA's published references
  and resolving them against the pinned OSCAL catalogue and High baseline. The
  result is `docs/crosswalk/`, one page per control, and
  `artifacts/crosswalk.json`. It refuses to map against an unpinned input or to
  a missing or withdrawn control. Recorded as
  [ADR-0002](docs/adr/0002-derive-800-53-cross-references-from-cci.md).
- Linked every rendered rule page to the 800-53 controls it reaches, read from
  the committed crosswalk so the join lives in one place.

- Wrote the hardening standard in `docs/standard/`: the prose account of what
  a hardened Datopsis image is and why; 26 testable image criteria and three
  targets, each anchored to a GPOS SRG rule and its 800-53 control; 11 platform
  expectations anchored to the Container Platform SRG; a comparison with the
  DISA Container Hardening Process Guide; and a dated conformance snapshot of
  the image repositories, since moved out of the standard to
  `docs/adoption/`. `tests/test_standard.py` checks every citation
  against the crosswalk.
- Recorded [ADR-0003](docs/adr/0003-secrets-reach-an-image-only-as-read-only-files.md):
  secrets reach an image only as read-only files.

- Adopted NIST SP 800-190, the Application Container Security Guide. It is
  pinned in the register, and `docs/standard/nist-800-190.md` assigns each of
  its 24 countermeasures to the criteria or expectations that implement it,
  with a test that fails if one is missing. Following it added IMG-27 (no
  remote administration), IMG-28 (malware scan), IMG-29 (base kept current),
  and IMG-30 (expected behaviour declared); PLT-12 to PLT-17 for the
  registry, orchestrator, and runtime tiers; and host expectations HST-01 to
  HST-04. It also tightened IMG-13 (default seccomp and SELinux) and IMG-25
  (every layer scanned).

- Wrote the control model, `docs/CONTROL-MODEL.md`, and
  derived a control baseline for all 370 High-baseline controls and 9 more the
  standard reaches. Most originations follow from the criteria's anchors
  through the crosswalk; `artifacts/control-determinations.json` overrides the
  rest, each with a reason, and the generator refuses an override that repeats
  derivation. `scripts/check-component.py` checks an image's OSCAL component
  definition against the baseline and the verification-pointer rule. Recorded
  [ADR-0004](docs/adr/0004-derive-the-control-baseline-here-validate-components-there.md).
- Added HST-05, clock synchronization, which the time-stamp controls needed.

- Rendered the DISA Web Server SRG V3R3 (102 rules) and Application Server SRG
  V4R5 (137 rules), and added them to the crosswalk. The crosswalk now reports
  what DISA maps a CCI to when it gives no Revision 5 reference: three Web
  Server SRG rules cite CCIs mapped only to Revision 4 controls that Revision 5
  withdraws. `check-component.py` now refuses a cross-reference naming a rule
  that is not in the rendered catalogue.
- Detached the standard from specific image repositories. Nothing in the
  standard, the control model, or the ADRs now depends on or names one. The
  conformance snapshot moved to `docs/adoption/` as an adoption record, with a
  plan for a conformance score and badge.
- Defined per-image tailoring in `docs/TAILORING.md`. Each image keeps a
  hardening profile recording an applicability determination for every
  conditional source, tied to the source's pinned digest, and deviations that
  expire within 180 days, or 90 for a vulnerability. `scripts/check-profile.py`
  checks it; `check-component.py --profile` honours active deviations.
  Recorded [ADR-0005](docs/adr/0005-tailor-by-profile-deviations-expire.md).

- Integrated the guidance recorded in `CONVERSATION.md`. Eighteen more sources
  are pinned, among them NIST IR 8176, SP 800-53A, the DISA Kubernetes and
  OpenShift STIGs, the DISA Container Image Creation and Deployment Guide, the
  NSA/CISA Kubernetes Hardening Guide, SSDF, SP 800-161, SLSA 1.2, in-toto, the
  OCI specifications, FIPS 140-3, and SP 800-207 and 207A; the NIST catalogue
  and baseline are now pinned at a tag instead of a moving branch.
  `docs/architecture/` holds the reference architecture, with its six
  diagrams as SVG. Every criterion and expectation now states its
  implementation, verification, expected result, and evidence, and
  `docs/assessment/` holds the SP 800-53A procedures for every baseline
  control, generated from the pinned catalogue. Added IMG-31 and IMG-32
  (restricted-v2 and restricted-v3 SCCs), IMG-33 (protected source), IMG-34
  (source and dependency scanning), PLT-18 (workload identity), and target
  IMG-T4 (SLSA Build Level 3).

- Added the reference web server, `examples/reference-web-server/`: a generic
  nginx image on UBI 9 Micro and the template for new images. Its lock pins
  both bases by manifest-list digest and nine RPMs by SHA-256 and Red Hat
  signing key; `acquire.py` is the only step with network access; assembly
  runs with networking disabled and re-verifies every digest and signature.
  CI shows a tampered or missing input stops the build, and a smoke suite reads
  every runtime property back from the running image, 41 checks across 20
  criteria, recording the evidence. What it does not yet evidence is recorded
  as expiring deviations in its profile.

- Added supply-chain gates to the reference image. The scanners are pinned by
  archive digest and verified before use. Before the build, the source is
  scanned for committed secrets and for dependency, secret, and
  build-definition findings; after it, an SPDX bill of materials is generated
  and checked against the lock, Trivy and Grype gate on fixed High and Critical
  vulnerabilities, and ClamAV scans the image and its inputs with refreshed
  signatures. A drift report fails CI once a base is more than 30 days behind,
  and a weekly read-only job reports it.
- Moved the reference image to the nginx 1.26 module stream. The gates found
  that RHEL 9's default nginx, 1.20, carries CVE-2026-42945 (Critical) and
  eight High CVEs fixed only in the 1.24 and 1.26 streams.
- Added a worked example of group read to IMG-16, under Podman and under
  Kubernetes and OpenShift.

- Added the adoption path: `docs/ADOPTING.md`, a step-by-step guide for an
  image repository, and a reusable `conformance.yml` workflow an image
  repository calls, pinned to a commit of this standard, to check its profile
  and component definition and score its evidence. `scripts/score.py` scores
  required criteria met with passing evidence and no active deviation, and
  writes an SVG badge and a Shields endpoint file.
- Gave the reference image its requirement statements, one per criterion, and
  its OSCAL component definition, generated from the control baseline with its
  own decisions for the controls the baseline leaves open. It scores 28/34 in
  CI; its six gaps are recorded deviations.
- Added a release job for the reference image: on a
  `reference-web-server/v*` tag it publishes the verified image to GHCR under
  that version only, signs it keylessly, attests its bill of materials and
  SLSA provenance, and verifies all three before it finishes.

- Released the reference image as 0.1.1: published publicly to GHCR,
  signed keylessly, with its bill of materials and SLSA provenance attested.
  CI now re-verifies the latest release on every run, as a consumer would,
  and the image's IMG-21, IMG-22, and IMG-24 deviations are closed on that
  evidence.

- The walkthroughs now use the reference image. The traceability diagram
  follows IMG-13 through its real files, from RWS-013 to the score; the
  reference architecture shows the reference image's pipeline, generated as a
  diagram, before the example on another stack; the control model's example is
  the reference image's real CM-7 entry. ADOPTING.md opens with what an
  adopting repository copies from the reference image and when it is done.
- The reference image's image-owned controls now state what each claim rests
  on and where it stops, rather than a generic remark.
- `check-component.py` finds requirement headings such as `### RWS-001` by
  default; `requirement-pattern` is optional in the conformance workflow.
- Evidence has a contract, [Evidence](docs/EVIDENCE.md), recorded as
  ADR-0006. Each file carries a header naming its commit, run, architecture,
  and image, and each result a stable id. `scripts/evidence.py` reads it
  strictly: a malformed or missing expected file, a `passed` that is not a
  Boolean or `null`, a duplicated check, an unknown criterion, or evidence from
  two images of one architecture makes it invalid, and invalid evidence is not
  scored.
- Each required criterion states its scope, per architecture or generic, and
  the control baseline carries it. The score is kept per architecture, amd64
  and arm64, and for the generic criteria, with a dated badge for each; a
  passing result on one architecture never fills a gap on another.
- Conformance reports three answers separately: `evidence-valid`, the score and
  `coverage`, and `release-eligible`. An image is release eligible when every
  criterion on every architecture is met or covered by a deviation, except a
  vulnerability deviation or a deviation from the vulnerability gate. The
  reference image's release job gates on it.
- `scripts/check-revision.py` binds the revision: `standard-ref` must be a full
  commit and the commit the conformance workflow ran from, and the profile's
  revision that commit or an ancestor with no normative change since.
- The reference image is judged by the conformance workflow as any image is,
  and `conformance-selftest.yml` calls that workflow with missing, malformed,
  failing, and partial evidence and with a revision that does not bind, and
  checks each answer.
- Hardening profiles are schema version 2: they declare `architectures` and the
  `evidence` files the image's CI writes, and optionally `roles`, `topologies`,
  and `platforms`. The conformance workflow takes `evidence-artifacts`, a name
  or pattern, in place of `evidence-artifact`.

- The reference image is built and verified natively for amd64 and arm64. The
  lock pins each architecture's RPMs, resolved against that architecture's
  runtime base without emulation, and the tools are pinned per architecture.
  The malware scan uses ClamAV's multi-architecture image,
  `clamav/clamav-debian`, pinned by index digest.
- The reference image's release publishes an index without rebuilding:
  `scripts/publish.py` pushes each tested image untagged by its own digest,
  which is then tested again at that digest; pushes an index naming exactly
  those digests; and, once the index and its images are signed and attested,
  tags the index's digest with the version. A fresh runner with no registry
  credentials then verifies the release. The reference README states what the
  image is not a template for.
- The reference image's badges, one per architecture and one generic, are
  published to GitHub Pages from every run on main.
- ADOPTING.md covers images the reference does not: more than one role, with
  per-role evidence the scorer requires for every role; standalone and
  clustered deployments, and what a single container's tests cannot show; and
  inputs that are not RPMs, with the pattern for a signed, digest-pinned
  upstream image. IMG-02 now states that a lock's digest, a publisher's
  signature, and a checksum published beside an artifact are three different
  claims, and that the last is never the integrity control.
- An image's requirements are mapped to the criteria explicitly, in a
  crosswalk that `check-component.py` and the conformance workflow check.
  `check-component.py --list-requirements` shows which identifiers the pattern
  finds, and it warns on a decision copied from the reference image word for
  word.

- A draft assessment: the conformance workflow's `mode: draft` reports what
  adopting would need, and how far the standard has moved since a pinned
  revision, for an image still researching it. The profile may be incomplete
  and the component definition absent; it claims nothing and never fails.
- Rule-by-rule applicability worksheets, generated from the pinned catalogues
  by `scripts/worksheets.py`, with the rules of other sources that share a CCI
  suggested for `covered-by`. `check-profile.py` holds a determination to the
  worksheet it cites. [Which SRGs an image takes](docs/applicability/README.md)
  gives the rules, including for HTTP applications that are not web servers,
  with a flowchart.
- A decisions worksheet for every control the baseline leaves to the image,
  with origination, rationale, owner, and review, and a warning on every
  access-control and identification control against a copied "no accounts".
  Unreviewed decisions block a release. The reference image's decisions moved
  into one, and await review.
- Released the reference image 0.2.0, its first multi-architecture index,
  verified from a clean runner.
- Coverage by requirement: a result names the requirements it verifies, and
  with a crosswalk a criterion is met only when every requirement it maps to
  has a passing check of its own, in every declared role and topology; short
  of that it is `partial`. Topologies, like roles, must each be evidenced. The
  conformance workflow's `candidates` binds the evidence to the digests to be
  released.
- A multi-architecture, multi-role caller: ADOPTING.md shows the CI, and the
  self-test calls the conformance workflow with that shape, complete and with
  one role's gap.
- [Releasing an image](docs/RELEASING.md): what a person checks before a
  release and what CI then enforces, with a flowchart.
- Proposed [ADR-0007](docs/adr/0007-record-manual-reviews-as-expiring-evidence.md):
  manual reviews as expiring evidence, allowed only where a criterion says so.

### Fixed

- The scorer counted a `passed` of `"false"` or `0` as met, and skipped a file
  that did not parse. Both are now errors.
- The reference image's profile named a revision of the standard from before
  later changes to the criteria and baseline, and nothing checked it; it now
  names the current one, and conformance fails when it falls behind.

- The reference image's release job logged in to the registry at a custom
  credentials path, which the provenance action does not read. Release 0.1.0
  was published, signed, and its bill of materials attested, but its
  provenance attestation failed, so it does not meet IMG-22. The job now uses
  the default location, and the fix is shipped as 0.1.1 rather than by
  republishing 0.1.0, which the job refuses by design.

- Corrected the process guide's register entry. Its title is *Container
  Hardening Process Guide*, V1R2, 24 August 2022, published by DISA under
  Distribution Statement A; the register had taken a title from the PDF's
  filename, left the date empty, and marked it not redistributable.

- The weekly source verification would have failed on every run.
  `verify-sources.py --fetch` extracts every pinned package, including the RHEL
  9 STIG and the Web and Application Server SRGs, and the renderer then tried
  to render them as catalogues. It now renders only XCCDFs whose digest is
  pinned in the register, skipping the rest and refusing a mismatch.

- Filed rule pages by Group ID rather than STIG ID. A STIG ID is not unique —
  GPOS V3R3 issues `SRG-OS-000132-GPOS-00067` as both `V-203655` and
  `V-278973` — and keying pages on it silently dropped a rule. The generator
  now refuses to overwrite rather than losing one.

### Notes

- The DISA Container Platform SRG is retrievable at its published URL. An
  earlier conclusion that it was unavailable came from a release sweep that
  checked V2R1 through V2R3 and stopped before V2R4, which is the current
  release.
