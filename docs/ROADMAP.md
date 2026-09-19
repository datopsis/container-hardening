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
| DISA RHEL 9 STIG | V2R4 | Host controls | Not yet |
| DISA Web Server SRG | V3R3 | Conditional | Not yet |
| DISA Application Server SRG | V4R5 | Conditional | Not yet |
| CIS Benchmarks | — | Cross-reference | Never — terms forbid it |

**The GPOS SRG carries image-level controls.** Per DoD guidance it is used to
assess image-level controls in the absence of a container-specific STIG, which
is the situation for every image this standard covers. It is not a stand-in for
the Container Platform SRG; that one governs the platform, and most of it will
originate as host-inherited for any image.

A **conditional** source applies only to images of a particular function. The
Application Server SRG is the worked example: it was assessed **not applicable**
to `datopsis/nginx-ubi`, because 27 of its 137 rules presuppose a management
interface or hosted applications and 18 refer to accounts, none of which that
image has. Recording why a source does not apply is part of the standard, not
an omission from it.

## Package 1: sources and rendering

- [ ] Render the RHEL 9 STIG, Web Server SRG, and Application Server SRG, which
  are pinned but not yet converted.
- [ ] Extend the weekly source verification to probe adjacent releases. It
  confirms a pinned package is unchanged, which is not the same as confirming
  it is current: DISA serves superseded releases alongside current ones, so a
  `200` is not evidence of currency. A newer release should be reported.
- [ ] Decide how a release upgrade is reviewed. The per-rule file layout exists
  so the diff shows exactly which rules changed; that diff should be the review
  artifact, with an explicit record of what changed and what it means for each
  adopting repository.
- [ ] Obtain a CIS benchmark via an account holder and record its digest. It
  can be cited by identifier but never rendered; its terms forbid reproduction.

## Package 2: the hardening standard

- [ ] Agree a GPOS-derived OpenSCAP rule selection, so that
  [IMG-T3](standard/criteria.md#img-t3-compliance-scan) can become required.
  `clickhouse-ubi` and `postgresql-ubi` currently scan against different ones.
- [ ] Decide whether to adopt antivirus scanning of retrieved build inputs,
  which the DISA process guide asks for and the standard does not yet require.
- [ ] Define the exception register format that
  [IMG-26](standard/criteria.md#img-26-exceptions-expire) requires, together
  with the Package 4 deviation format; they are the same mechanism.

## Package 3: the control mapping

- [ ] Carry the control model across from `datopsis/nginx-ubi`: six origination
  values, a responsible role that must match, and the rule that only
  `image-owned` asserts the project satisfies anything. It is already written
  and enforced there; it needs generalising, not reinventing.
- [ ] Keep the verification-pointer rule. An `image-owned` control must cite a
  requirement identifier the adopting product actually states. This is what
  stops a control asserting an obligation nobody committed to, and it is the
  part most worth carrying.
- [ ] Decide where the control spine lives: in this standard, in each image
  repository, or generated into each from here. This decision shapes every
  adopting repository and should be an ADR.

## Package 4: per-application tailoring

- [ ] Define how an image selects from the standard. Every image takes the
  image-level baseline; function-specific sources are added by declaration.
- [ ] Define how an applicability determination is recorded and reviewed, using
  the Application Server SRG determination as the worked example.
- [ ] Define how an image declares a deviation, with a reason and an expiry.
  A deviation with no expiry is a silent permanent exception.

## Package 5: adoption

- [ ] Adopt in `datopsis/nginx-ubi` first, which already has the requirement
  tree, trace matrix, and OSCAL component definition the mapping needs. Its
  Package 5 is the reconciliation target.
- [ ] Reconcile the two repositories' source registers. `nginx-ubi` currently
  records the Container Platform SRG as unresolved at V2R1; the current release
  is **V2R4** and it retrieves normally.
- [ ] Close the gaps in the [conformance snapshot](standard/conformance.md).
  The largest are `clickhouse-ubi`'s build (IMG-02, IMG-03) and secrets
  (IMG-16), and the missing release workflows in `seaweedfs-ubi` and
  `lakekeeper-ubi` (IMG-21, IMG-22). No image yet asserts IMG-14.
- [ ] Define what adoption costs a repository: which files it must add, which
  checks it must run, and what it must publish.

## Package 6: publication

- [ ] Decide whether the rendered catalogue and standard are published as a
  site or consumed as Markdown in the repository. Both reference points are
  sites; neither is necessary for the content to be useful.
- [ ] Add link checking and Markdown linting to CI. Register validation and
  weekly source verification are in place.
- [ ] Protect `main` and require the checks, matching `datopsis/nginx-ubi`.

## What the scaffold already established

- `scripts/build-srg-markdown.py` converts a DISA XCCDF package into one
  Markdown file per rule, with `--check` for drift. 391 rules across two
  catalogues render today.
- `docs/srg/` holds the generated Container Platform SRG V2R4 and GPOS SRG V3R3.
- `artifacts/sources.json` pins ten sources by digest, recording for each its
  role, whether it has been rendered, and whether it may be redistributed. All
  nine retrievable sources were verified against their recorded digests on
  2026-09-18.
- `scripts/build-cci-crosswalk.py` joins every rendered rule's CCIs to 800-53
  Rev 5 through the pinned DISA CCI list, resolved against the pinned OSCAL
  catalogue. `docs/crosswalk/` and `artifacts/crosswalk.json` hold the result:
  the Container Platform SRG reaches 80 controls and the GPOS SRG 97, 106
  distinct. Every cited CCI resolved, and none was deprecated or unmapped. See
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
  26 required image criteria and three targets, 11 platform expectations, a
  comparison with the DISA Container Hardening Process Guide, and a conformance
  snapshot of the five image repositories. `tests/test_standard.py` checks that
  every cited SRG rule reaches the 800-53 control cited beside it, that image
  criteria cite only image rules and platform expectations only platform rules,
  and that every link and anchor resolves.

Two findings from building it, recorded so they are not rediscovered:

**A STIG ID is not a unique key.** GPOS V3R3 issues
`SRG-OS-000132-GPOS-00067` as two distinct rules, `V-203655` and `V-278973`.
Rule pages are filed by Group ID, and the generator refuses to overwrite rather
than silently dropping a rule.

**DISA serves superseded releases alongside current ones.**
`U_GPOS_V2R7_SRG.zip` still returns `200` while V3R3 is current. Retrievability
never establishes currency; only checking adjacent releases does.
