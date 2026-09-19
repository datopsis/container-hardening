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

### Fixed

- Filed rule pages by Group ID rather than STIG ID. A STIG ID is not unique —
  GPOS V3R3 issues `SRG-OS-000132-GPOS-00067` as both `V-203655` and
  `V-278973` — and keying pages on it silently dropped a rule. The generator
  now refuses to overwrite rather than losing one.

### Notes

- The DISA Container Platform SRG is retrievable at its published URL. An
  earlier conclusion that it was unavailable came from a release sweep that
  checked V2R1 through V2R3 and stopped before V2R4, which is the current
  release.
