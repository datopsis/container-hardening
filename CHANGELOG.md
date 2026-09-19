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
  Proposed [ADR-0005](docs/adr/0005-tailor-by-profile-deviations-expire.md).

### Fixed

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
