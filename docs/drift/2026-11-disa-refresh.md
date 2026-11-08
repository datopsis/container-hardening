# 2026-11 DISA source drift report

| Source | Pinned → candidate | Rules old → new | Added / removed / changed | Image criteria affected | Recommendation |
| --- | --- | ---: | ---: | --- | --- |
| [GPOS SRG](#disa-gpos-srg) | V3R3 → V3R4 | 203 → 202 | 1 / 2 / 26 | Direct: IMG-01, IMG-02, IMG-03, IMG-04, IMG-22, IMG-27, IMG-29, IMG-T2, IMG-T3, IMG-T4; shared controls: IMG-19 | **Adopt with changes** |
| [Container Platform SRG](#disa-container-platform-srg) | V2R4 → V2R5 | 188 → 188 | 0 / 0 / 14 | No direct anchors | **Adopt** |
| [Application Server SRG](#disa-application-server-srg) | V4R5 → V4R6 | 137 → 137 | 0 / 0 / 17 | No direct anchors; shared controls: IMG-01, IMG-02, IMG-03, IMG-04, IMG-06, IMG-07, IMG-14, IMG-15, IMG-19, IMG-22, IMG-27, IMG-30 | **Adopt with changes** |
| [RHEL 9 STIG](#disa-rhel9-stig) | V2R4 → V2R10 | 452 → 445 | 3 / 10 / 166 | No direct anchors; shared controls: IMG-01, IMG-02, IMG-03, IMG-04, IMG-06, IMG-07, IMG-09, IMG-10, IMG-11, IMG-12, IMG-13, IMG-14, IMG-15, IMG-19, IMG-22, IMG-25, IMG-27, IMG-30, IMG-31, IMG-32 | **Hold** |
| [Web Server SRG](#disa-web-server-srg) | V3R3 → V4R5 | 102 → 126 | 32 / 8 / 10 | No direct anchors; shared controls: IMG-01, IMG-02, IMG-03, IMG-04, IMG-05, IMG-15, IMG-16, IMG-17, IMG-19, IMG-22, IMG-25, IMG-26, IMG-27, IMG-29 | **Adopt with changes** |
| [OpenShift STIG](#disa-openshift-stig) | V2R6 → V2R7 | 83 → 83 | 0 / 0 / 5 | No direct anchors; shared controls: IMG-16, IMG-17 | **Adopt with changes** |
| Kubernetes STIG | V2R6 → unchanged | — | 0 / 0 / 0 (same package) | None | **Hold** current pin; no newer candidate found |
| CCI list | 2025-01-23 → unchanged | — | 0 / 0 / 0 (prose/list, no rule diff) | None | **Hold** current pin; no newer candidate found |
| Container Hardening Process Guide | V1R2 → unchanged | — | 0 / 0 / 0 (prose/list, no rule diff) | None | **Hold** current pin; no newer candidate found |
| Container Image Creation and Deployment Guide | V2R0.6 → unchanged | — | 0 / 0 / 0 (prose/list, no rule diff) | None | **Hold** current pin; no newer candidate found |

Checked **2026-11-08 UTC**, following the 2026-11-07 finding. This is an owner
review of a draft reference standard, not adoption or an authorization claim.
**No registered pin, digest, catalogue, crosswalk, workflow, or example is changed.**
Candidate identities below identify this analysis only; they do not amend the
accepted register. Downloaded ZIPs and extracted files remain in gitignored
`sources/` and are not part of this PR.

“Changed” counts a surviving **Group ID** once if its STIG ID, title, discussion,
check, fix, severity, or CCI set changes after the existing renderer's text
normalization. It includes editorial and whitespace changes. Rule-revision IDs
alone are listed separately, not counted as content changes. Adds/removals are
literal Group ID set differences, including renumbered requirements. No matching
or deduplication uses STIG ID.

“Direct” means a rule is linked by `docs/standard/criteria.md`. “Shared controls”
means the old/new CCI join reaches a control whose current baseline lists those
image criteria; it is a **review relationship**, not a claim that the criterion
must change. Platform and host rules keep their own owners. Per-rule entries
identify direct platform/host anchors separately. IMG-T3 also needs the whole
new GPOS selection reviewed when its future compliance scan is tailored; the
summary counts only explicit anchors and baseline relationships.

## Decisions for the owner

- **GPOS — adopt with changes.** Repoint IMG-27 from removed V-203655 to the
  surviving V-278973 only after confirming scope; both have the same STIG ID
  and CCI, and the survivor explicitly includes Zero Trust. Repoint IMG-01 and
  IMG-29 from V-278977 to V-282963. The latter has the same STIG ID, title,
  severity and CCI, but is still a Group ID removal/addition. Review IA-5(1)
  for the 60 → 180 day maximum in V-203632, and IA-7 for the FIPS 140-3-only
  discussion in V-203649. These do not automatically authorize weaker local
  password policy or establish cryptographic validation. Other edits mainly
  change DoD/DOD to DoW, including banner text. No surviving rule changes its
  severity or CCI set.
- **Container Platform — adopt.** No rule, severity or CCI-set churn. Review
  V-233098's 60 → 180 day maximum with the platform identity owner; keeping a
  stricter local maximum still fits. The rest is terminology/banner wording.
  No image criterion directly cites the changed rules, and no control
  origination change is justified by this diff. Adoption still requires the
  owner's source decision and a separate regeneration.
- **Application Server — adopt with changes.** V-204833 (AU-4(1)) becomes CAT I;
  the platform logging handoff and any applicable application assessment must
  reflect that priority. Preserve the function-specific applicability review;
  do not convert all application-server rules into universal image obligations.
  Review the existing FIPS position: V-204758 still says FIPS 140-2 in its title
  despite newer GPOS wording. The release does not resolve that inconsistency.
- **RHEL 9 — hold.** This is six releases beyond the pin, with 179 added,
  removed or changed Group IDs, eight CAT II → CAT I promotions, crypto policy
  and audit-command changes, and CCI references with no Rev 5 mapping. The
  complete diff is below, but host/UBI applicability and replacement of removed
  requirements need an owner decision before adoption or initial rendering.
  RHEL rules have no committed rule crosswalk entries today. Do not silently
  transfer host checks to the image or infer that removal waives a control.
- **Web Server — adopt with changes.** V-206372/V-206373 change from CCI-001749
  (Rev 4 CM-5(3), no Rev 5 mapping) to CCI-003992 (CM-14), repairing two current
  crosswalk findings. Removed V-206420 accounts for the third current unmapped
  finding. Seven HTTP/session rules are rekeyed; 25 additions have no removed
  rule with the same STIG ID. Rebuild applicability worksheets by Group ID,
  reconsider the new authentication/audit/key-storage obligations, and review
  V-206387/V-206431's CAT I severity. V-206443 now requires **installing**
  updates within 30 days, rather than merely checking for them. IMG-04/IMG-22
  and each image's release evidence need review for that obligation. V-206407
  corrects the at-rest encryption example from SHA1 to AES-256. The new release
  does not by itself settle the reference image's open control decisions.
- **OpenShift — adopt with changes.** V-257580 removes redundant module-change
  audit examples and keeps four load/unload rules for b32/b64; have the platform
  owner adjust node audit evidence. V-257564 replaces the version-specific
  encryption documentation link with a general documentation instruction.
  No CCI or severity changes; preserve the platform/host ownership boundary.
- **Kubernetes, CCI list and both guides — hold current pins.** Bytes still
  match. No newer package was found in the stated probe ranges. This is bounded
  evidence, not a guarantee that no differently named release exists.

## Retrieval and comparison evidence

Baseline repository commit: `25bd6922657c8abbbb6bac5f4abbc3c452e45731`.
The three missing registered URLs were tried directly and returned 404; no
matching old ZIP existed in this clean checkout. Their baseline is the
committed rendered Markdown plus `artifacts/crosswalk.json`. This preserves
all requested rule fields, but cannot establish differences in XML metadata
that the renderer did not retain. No third-party copy substitutes for a pin.

For RHEL 9, Web Server and OpenShift, the old ZIPs were retrieved and their
SHA-256 values verified against the register before comparing their XCCDFs.
The retrieved Web Server V3R3 XCCDF was also checked field by field against its
committed Markdown, validating the fallback parser. Every rendered old rule's
Group ID, STIG ID, severity and CCIs was checked against the committed crosswalk.

Candidate XCCDF parsing reuses `scripts/build-srg-markdown.py`'s `parse` function
without calling its writer. Text normalization therefore unescapes entities,
normalizes CR/LF, removes trailing spaces before newlines, caps runs of blank
lines, and strips surrounding whitespace. CCI comparison is order-insensitive.
Prospective joins reuse `load_cci_list`, `control_id`, and `load_catalogue` from
`scripts/build-cci-crosswalk.py`, against the verified pinned CCI XML and OSCAL
5.2.0 catalogue. Undefined/withdrawn Rev 5 targets were checked; none occurred.
Missing Rev 5 references remain findings below. These are review-only joins,
never regenerated accepted crosswalks.

Dates below are **XCCDF release-info Benchmark Dates**, not retrieval dates,
XCCDF acceptance/status dates, or HTTP Last-Modified timestamps. DISA's
Last-Modified can reflect hosting migration and is not a release date.

### Candidate package identities

Each link is the exact official URL retrieved. Size is the downloaded ZIP size
in bytes; SHA-256 is over those exact bytes.

| Source / candidate ZIP | Release date (benchmark) | XCCDF status date | Bytes | ZIP SHA-256 |
| --- | --- | --- | ---: | --- |
| [U_GPOS_V3R4_SRG.zip](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_GPOS_V3R4_SRG.zip) | 2026-09-30 | 2026-09-03 | 1,287,573 | `2f39169c6e6640972eeee82c046f4af81c2c87c4134cc6cc57e8d46c864967e2` |
| [U_Container_Platform_V2R5_SRG.zip](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Container_Platform_V2R5_SRG.zip) | 2026-09-30 | 2026-09-01 | 2,957,050 | `01a2782958b6f4d8084f179d2aa84e94d496aad6f11f8cbb3bc16921a0e542cd` |
| [U_Application_Server_V4R6_SRG.zip](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Application_Server_V4R6_SRG.zip) | 2026-09-30 | 2026-08-26 | 1,364,666 | `7527c3b2b42a8608650c27b3db7be2bcfbf39512859b814076eefe29f1c87aaa` |
| [U_RHEL_9_V2R10_STIG.zip](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RHEL_9_V2R10_STIG.zip) | 2026-09-30 | 2026-09-29 | 2,282,653 | `a9a212444ac39060c6d6ecd3d8113c4e51ce4094ce50f760aaec792945c3d111` |
| [U_Web_Server_V4R5_SRG.zip](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Web_Server_V4R5_SRG.zip) | 2026-07-01 | 2026-05-23 | 1,186,497 | `e7936ed668282a5536b1be9713fc6d69d2be3338c7728e8c2e701c5e5f64d4bd` |
| [U_RH_OpenShift_Container_Platform_4-x_V2R7_STIG.zip](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_RH_OpenShift_Container_Platform_4-x_V2R7_STIG.zip) | 2026-09-30 | 2026-08-24 | 2,381,029 | `98235dc181f0d0671eae9cdd09b880c10bcb5b74254270f1ce3cb710c4d4f2ce` |

### XCCDF identities and comparison bases

- **GPOS SRG** — committed Markdown + crosswalk → candidate XCCDF. Candidate `U_GPOS_SRG_V3R4_Manual-xccdf.xml`: `e554d4278ddaea582343bee66185fa9e47da71f97e49c027e4fd5e01e8abcd4f`.
  Baseline: [GPOS SRG catalogue](../srg/general-purpose-operating-system-srg/README.md), 203 rules; registered old ZIP `97026655bce18d91e12c9c0a9fd54288989f0b483d3b92ec615e2dc0544e6f24` could not be recovered.
- **Container Platform SRG** — committed Markdown + crosswalk → candidate XCCDF. Candidate `U_Container_Platform_SRG_V2R5_Manual-xccdf.xml`: `b45697a19dd0ede9818659f8d836d9d758baa870c928171f34db45ee8d24272d`.
  Baseline: [Container Platform SRG catalogue](../srg/container-platform-srg/README.md), 188 rules; registered old ZIP `975a9e421e62e0ea52b1824e4a719aee87eed9070d5a3145fa9817f6498d99fe` could not be recovered.
- **Application Server SRG** — committed Markdown + crosswalk → candidate XCCDF. Candidate `U_Application_Server_SRG_V4R6_Manual-xccdf.xml`: `a63458c6279a6c71e8b1f2bb981455645fb8d6841424194be69b3065656ae157`.
  Baseline: [Application Server SRG catalogue](../srg/application-server-srg/README.md), 137 rules; registered old ZIP `ea33d7f18f950e86c9e0cc63835cf8802d319804ac143b2020b1fbac13ff2643` could not be recovered.
- **RHEL 9 STIG** — pinned ZIP XCCDF → candidate XCCDF. Candidate `U_RHEL_9_STIG_V2R10_Manual-xccdf.xml`: `3fcb716d5ca2bf539460b7baca42c1a6a65e1faff619737b1e88ffb25db87541`.
  Old ZIP `0434fd47261f992b8aa4e48aa221b7862ada57b8504d82087bc8afb8748169de`; old XCCDF `ca5e3c8283c8f1b07434e5966e761a3233abfb29b57b67adfe5c1af9f3892761`.
- **Web Server SRG** — pinned ZIP XCCDF → candidate XCCDF. Candidate `U_Web_Server_SRG_V4R5_Manual-xccdf.xml`: `c4f66f0744fa06ddd571a0aaaf462e6e97cf587827a33fc8be69208e8b86a8f9`.
  Old ZIP `7345e31a61c162ee4ca0253e3f44b729c18bb45b3a17cb364e5d08422412b409`; old XCCDF `634ff396f651314aed1864ef1af5e617a314218cb7a3dfa7214213329ec1ac86`.
- **OpenShift STIG** — pinned ZIP XCCDF → candidate XCCDF. Candidate `U_RH_OpenShift_Container_Platform_4-x_STIG_V2R7_Manual-xccdf.xml`: `b453e1ad834d07c774117c774421ed293af1d219bffc070854a2175d196110df`.
  Old ZIP `dba61b6440f35a67d9643517ce6c206c885c73a532727070a93e57f8a3dd104a`; old XCCDF `991db8e0517d05ee3e13f647c3a85ba1424792ba84011ab6188b40cc67c8232d`.

### Full DISA/DoD register sweep

195 direct GETs were made, including all ten registered URLs. For the seven
versioned ZIP families, every R1–R12 was probed in both the pinned major
version and the next major version; Web Server also includes V5R1–R12 because
V4 was found. Probes did not stop at the first 404. Only the releases shown
below returned 200; all other URLs in these ranges returned 404, with no
unresolved timeout or 403 in this DISA sweep.

All ZIP filenames use `https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/`.
`U_CCI_List.zip` is unversioned, so its exact package and XML digests were checked.

| Registered source | Registered URL result | Version range probed | Releases served in range | Drift conclusion |
| --- | --- | --- | --- | --- |
| GPOS SRG | 404 | V3–V4, each R1–R12 | V3R4 | Newer served |
| Container Platform SRG | 404 | V2–V3, each R1–R12 | V2R5 | Newer served |
| Application Server SRG | 404 | V4–V5, each R1–R12 | V4R6 | Newer served |
| RHEL 9 STIG | 200; digest matches | V2–V3, each R1–R12 | V2R4, V2R5, V2R6, V2R7, V2R8, V2R9, V2R10 | Newer served |
| Web Server SRG | 200; digest matches | V3–V5, each R1–R12 | V3R3, V4R4, V4R5 | Newer served |
| Kubernetes STIG | 200; digest matches | V2–V3, each R1–R12 | V2R3, V2R4, V2R5, V2R6 | No newer found |
| OpenShift STIG | 200; digest matches | V2–V3, each R1–R12 | V2R3, V2R4, V2R5, V2R6, V2R7 | Newer served |
| [CCI list](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_CCI_List.zip) | 200; digest matches | Unversioned URL; XML digest also matches | 2025-01-23 | No byte drift; no newer filename found |
| [Container Hardening Process Guide](https://dl.dod.cyber.mil/wp-content/uploads/devsecops/pdf/Final_DevSecOps_Enterprise_Container_Hardening_Guide_1.2.pdf) | 200; digest matches | Filename suffixes 1.3, 1.4, 1.5, 2.0, 2.1, 2.2 | V1R2 | No byte drift; no newer filename found |
| [Container Image Creation and Deployment Guide](https://dl.dod.cyber.mil/wp-content/uploads/devsecops/pdf/DevSecOps_Enterprise_Container_Image_Creation_and_Deployment_Guide_2.6-Public-Release.pdf) | 200; digest matches | Filename versions 2.7, 2.8, 2.9, 3.0, 3.1, 3.2 | V2R0.6 | No byte drift; no newer filename found |

Specifically requested higher probes **GPOS V3R5**, **Container Platform V2R6**,
and **Application Server V4R7** each returned **404**. RHEL V2R11/V2R12,
Web Server V4R6–V4R12 and OpenShift V2R8–V2R12 also returned 404. The bounded
search cannot exclude releases outside these versions or under renamed paths.
The two prose-guide probes substitute only the version in the registered
filename; no per-rule diff applies to an unchanged prose document.

### Source verifier output

Command: `python3 scripts/verify-sources.py`, exit **2**. Combined stdout/stderr
is quoted verbatim below (stderr appears first due to redirected buffering).
The NSA/CISA 403 is a separate reachability finding. “0 drifted” means no
successfully downloaded **registered URL** returned a different digest; it
cannot detect the six newer releases found by the adjacent-version sweep.

```text

One or more sources could not be retrieved. This says nothing about
whether they changed, and no digest has been altered.
  verified     nist-sp800-53r5-catalog
  verified     nist-sp800-53r5-high-baseline
  verified     disa-cci-list
  verified     dod-container-hardening-guide
  verified     nist-sp800-190
  verified     disa-rhel9-stig
  verified     disa-web-server-srg
  verified     nist-ir-8176
  verified     nist-sp800-53a-r5
  verified     disa-kubernetes-stig
  verified     disa-openshift-stig
  verified     disa-container-image-guide
  verified     kubernetes-pod-security-standards
  verified     openshift-scc
  verified     nist-sp800-218
  verified     nist-sp800-161r1-upd1
  verified     slsa-v1.2
  verified     in-toto-attestation-v1
  verified     oci-image-spec
  verified     oci-runtime-spec
  verified     oci-distribution-spec
  verified     nist-fips-140-3
  verified     nist-sp800-207
  verified     nist-sp800-207a
  skipped      cis-kubernetes-benchmark
  skipped      cis-openshift-benchmark
  UNREACHABLE  disa-container-platform-srg
      HTTP Error 404: Not Found
  UNREACHABLE  disa-gpos-srg
      HTTP Error 404: Not Found
  UNREACHABLE  disa-application-server-srg
      HTTP Error 404: Not Found
  UNREACHABLE  nsa-cisa-kubernetes-hardening
      HTTP Error 403: Forbidden

24 verified, 4 unreachable, 0 drifted, 2 skipped
```

## Per-rule findings

Every added, removed and changed Group ID is listed below. A surviving field
not named under **Changed fields** is unchanged, including check, fix, severity
and CCI. Title and discussion differences are included to avoid hiding policy
changes in prose. Text diff blocks use `-` for old and `+` for candidate, with
one unchanged line of context; long lines are wrapped only for display.
Title/discussion diffs instead show changed token spans with nearby context,
as quoted strings: `\n` denotes a newline and unchanged intervening spans
are omitted. This retains whitespace changes without repeating whole paragraphs.

Crosswalk links name the existing **control page**, while the section's source
and the heading's Group ID identify the exact rule entry in
[`artifacts/crosswalk.json`](../../artifacts/crosswalk.json). “Prospective only”
means no accepted rule entry exists. The **baseline** lists every reached
control's current origination and basis; `determination` refers to the matching
`control` key in
[`artifacts/control-determinations.json`](../../artifacts/control-determinations.json),
while other bases are derived or unresolved in
[`artifacts/control-baseline.json`](../../artifacts/control-baseline.json).
The current reference image's matching
[`decisions.json`](../../examples/reference-web-server/decisions.json) entries
are listed where present as review pointers, not changed or approved decisions.
Omitted handoffs or reference-image decisions mean none exist for those controls.
No added/removed/changed Group ID in this report is directly linked by a
platform/host expectation; their control-level handoffs are still listed.


<a id="disa-gpos-srg"></a>

## GPOS SRG — V3R3 → V3R4

**Adopt with changes.** 1 added, 2 removed, 26 changed. Comparison: committed Markdown + crosswalk → candidate XCCDF.

Of the 26 changed rules, 8 change check, fix, severity or CCI; 18 change only title/discussion/STIG ID.

Rekeys and removals: V-278977 → V-282963 retains STIG ID
`SRG-OS-000830-GPOS-00300`; V-203655 is removed but V-278973 remains under
`SRG-OS-000132-GPOS-00067`. The latter is not a new rule, so do not count it
as an addition or delete the SC-2 obligation.

### GPOS SRG: added

#### V-282963 — Added

**The operating system must be a version supported by the vendor.**

STIG ID: `SRG-OS-000830-GPOS-00300`. Severity: high.
Rule ID: `SV-282963r1184542_rule`.
CCI: CCI-003376.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-29].
- **Crosswalk:** Prospective only; no accepted rule entry; add [SA-22][cw-sa-22].
- **Baseline / control determinations:** `sa-22`: `image-owned` (criterion).
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the operating system is a version supported by the vendor.

If the operating system is not a version supported by the vendor, this is a finding.
```

**Fix**

```text
Install or upgrade the operating system to a version supported by the vendor.
```

</details>

### GPOS SRG: removed

#### V-203655 — Removed

**The operating system must separate user functionality (including user interface services) from operating system management functionality.**

STIG ID: `SRG-OS-000132-GPOS-00067`. Severity: medium.
Rule ID: `SV-203655r1117266_rule`.
CCI: CCI-001082.

- **Image criteria:** direct: [IMG-27]; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-2][cw-sc-2] → None.
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion).
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the operating system separates user functionality (including user interface services) from operating system management functionality. If it does not, this is a finding.
```

**Fix**

```text
Configure the operating system to separate user functionality (including user interface services) from operating system management functionality.
```

</details>

#### V-278977 — Removed

**The operating system must be a version supported by the vendor.**

STIG ID: `SRG-OS-000830-GPOS-00300`. Severity: high.
Rule ID: `SV-278977r1137711_rule`.
CCI: CCI-003376.

- **Image criteria:** direct: [IMG-01], [IMG-29]; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SA-22][cw-sa-22] → None.
- **Baseline / control determinations:** `sa-22`: `image-owned` (criterion).
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the operating system is a version supported by the vendor.

If the operating system is not a version supported by the vendor, this is a finding.
```

**Fix**

```text
Install or upgrade the operating system to a version supported by the vendor.
```

</details>

### GPOS SRG: changed

#### V-203592 — Changed

**The operating system must automatically remove or disable temporary user accounts after 72 hours.**

STIG ID: `SRG-OS-000002-GPOS-00002`. Severity: medium.
Rule ID: `SV-203592r958364_rule` → `SV-203592r1268212_rule`.
CCI: CCI-000016.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-2(2)][cw-ac-2.2].
- **Baseline / control determinations:** `ac-2.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-2.2`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "accounts after a DoD-defined time period of"
+ "accounts after a DoW-defined time period of"
```

</details>

#### V-203595 — Changed

**The operating system must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system.**

STIG ID: `SRG-OS-000023-GPOS-00006`. Severity: medium.
Rule ID: `SV-203595r958390_rule` → `SV-203595r1268215_rule`.
CCI: CCI-000048.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DoD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Discussion**

```diff
- "accordance with applicable DoD policy. Use the"
+ "accordance with applicable DoW policy. Use the"
```

**Check**

```diff
@@ -1,5 +1,5 @@
-Verify the operating system displays the Standard Mandatory DoD Notice and Consent Banner before granting
+Verify the operating system displays the Standard Mandatory DoW Notice and Consent Banner before granting
 access to the system.

-The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for
+The banner must be formatted in accordance with applicable DoW policy. Use the following verbiage for
 operating systems that can accommodate banners of 1300 characters:
```

**Fix**

```diff
@@ -1,5 +1,5 @@
-Configure the operating system to display the Standard Mandatory DoD Notice and Consent Banner before granting
+Configure the operating system to display the Standard Mandatory DoW Notice and Consent Banner before granting
  access to the system.

-The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for
+The banner must be formatted in accordance with applicable DoW policy. Use the following verbiage for
 operating systems that can accommodate banners of 1300 characters:
```

</details>

#### V-203596 — Changed

**The operating system must display the Standard Mandatory DoW Notice and Consent Banner until users acknowledge the usage conditions and take explicit actions to log on for further access.**

STIG ID: `SRG-OS-000024-GPOS-00007`. Severity: medium.
Rule ID: `SV-203596r958392_rule` → `SV-203596r1268218_rule`.
CCI: CCI-000050.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DoD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Discussion**

```diff
- "by the user, DoD will not be"
+ "by the user, DoW will not be"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify the operating system displays the Standard Mandatory DoD Notice and Consent Banner until users
+Verify the operating system displays the Standard Mandatory DoW Notice and Consent Banner until users
 acknowledge the usage conditions and take explicit actions to log on for further access. If it does not, this
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the operating system to display the Standard Mandatory DoD Notice and Consent Banner until users
+Configure the operating system to display the Standard Mandatory DoW Notice and Consent Banner until users
 acknowledge the usage conditions and take explicit actions to log on for further access.
```

</details>

#### V-203602 — Changed

**The operating system must monitor remote access methods.**

STIG ID: `SRG-OS-000032-GPOS-00013`. Severity: medium.
Rule ID: `SV-203602r958406_rule` → `SV-203602r1268219_rule`.
CCI: CCI-000067.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Accepted rule entry; [AC-17(1)][cw-ac-17.1].
- **Baseline / control determinations:** `ac-17.1`: `host-inherited` (determination); handoff: [PLT-13].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "is access to DoD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-203603 — Changed

**The operating system must implement DoW-approved encryption to protect the confidentiality of remote access sessions.**

STIG ID: `SRG-OS-000033-GPOS-00014`. Severity: high.
Rule ID: `SV-203603r958408_rule` → `SV-203603r1268222_rule`.
CCI: CCI-000068.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "system must implement DoD-approved encryption to protect"
+ "system must implement DoW-approved encryption to protect"
```

**Discussion**

```diff
- "is access to DoD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
- "through an external, non-organization-controlled network. Remote access"
+ "through an external, nonorganization-controlled network. Remote access"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify the operating system implements DoD-approved encryption to protect the confidentiality of remote access
+Verify the operating system implements DoW-approved encryption to protect the confidentiality of remote access
  sessions. If it does not, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the operating system to implement DoD-approved encryption to protect the confidentiality of remote
+Configure the operating system to implement DoW-approved encryption to protect the confidentiality of remote
 access sessions.
```

</details>

#### V-203619 — Changed

**The operating system must provide audit record generation capability for DoW-defined auditable events for all operating system components.**

STIG ID: `SRG-OS-000062-GPOS-00031`. Severity: medium.
Rule ID: `SV-203619r958442_rule` → `SV-203619r1268225_rule`.
CCI: CCI-000169.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AU-12][cw-au-12].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `au-12`: `image-owned`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "generation capability for DoD-defined auditable events for"
+ "generation capability for DoW-defined auditable events for"
```

**Discussion**

```diff
- "generating audit records.\n\nDoD has defined the"
+ "generating audit records.\n\nDoW has defined the"
```

**Check**

```diff
@@ -1,5 +1,5 @@
-Verify the operating system provides audit record generation capability for DoD-defined auditable events for
+Verify the operating system provides audit record generation capability for DoW-defined auditable events for
 all operating system components.

-DoD has defined the list of events for which the operating system will provide an audit record generation
+DoW has defined the list of events for which the operating system will provide an audit record generation
 capability as the following:
```

**Fix**

```diff
@@ -1,5 +1,5 @@
-Configure the operating system to provide audit record generation capability for DoD-defined auditable events
+Configure the operating system to provide audit record generation capability for DoW-defined auditable events
 for all operating system components.

-DoD has defined the list of events for which the operating system will provide an audit record generation
+DoW has defined the list of events for which the operating system will provide an audit record generation
 capability as the following:
```

</details>

#### V-203632 — Changed

**Operating systems must enforce a 180-day maximum password lifetime restriction.**

STIG ID: `SRG-OS-000076-GPOS-00044`. Severity: medium.
Rule ID: `SV-203632r1038967_rule` → `SV-203632r1268211_rule`.
CCI: CCI-004066.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "must enforce a 60-day maximum password lifetime"
+ "must enforce a 180-day maximum password lifetime"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify operating system enforces a 60-day maximum password lifetime restriction. If it does not, this is a
+Verify operating system enforces a 180-day maximum password lifetime restriction. If it does not, this is a
 finding.
```

**Fix**

```diff
@@ -1 +1 @@
-Configure operating system to enforce a 60-day maximum password lifetime restriction.
+Configure operating system to enforce a 180-day maximum password lifetime restriction.
```

</details>

#### V-203636 — Changed

**The operating system must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.**

STIG ID: `SRG-OS-000080-GPOS-00048`. Severity: medium.
Rule ID: `SV-203636r1137691_rule` → `SV-203636r1268226_rule`.
CCI: CCI-000213.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-3][cw-ac-3].
- **Baseline / control determinations:** `ac-3`: `research-required` (determination); handoff: [PLT-06].
- **Reference image decisions to review:** `ac-3`: `deployment-configured`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "issued certificates by DOD-approved PKIs, all DOD systems (e.g., web"
+ "issued certificates by DoW-approved PKIs, all DoW systems (e.g., web"
```

</details>

#### V-203640 — Changed

**The operating system must use multifactor authentication for network access to privileged accounts.**

STIG ID: `SRG-OS-000105-GPOS-00052`. Severity: medium.
Rule ID: `SV-203640r958484_rule` → `SV-203640r1268228_rule`.
CCI: CCI-000765.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(1)][cw-ia-2.1].
- **Baseline / control determinations:** `ia-2.1`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `ia-2.1`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "the Internet).\n\nThe DoD CAC with DoD-approved PKI is an"
+ "the Internet).\n\nThe DoW CAC with DoW-approved PKI is an"
```

</details>

#### V-203641 — Changed

**The operating system must use multifactor authentication for network access to non-privileged accounts.**

STIG ID: `SRG-OS-000106-GPOS-00053`. Severity: medium.
Rule ID: `SV-203641r958486_rule` → `SV-203641r1268229_rule`.
CCI: CCI-000766.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(2)][cw-ia-2.2].
- **Baseline / control determinations:** `ia-2.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.2`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "(e.g., biometric).\n\nA non-privileged account is any"
+ "(e.g., biometric).\n\nA nonprivileged account is any"
- "authorizations of a non-privileged user.\n\nNetwork access"
+ "authorizations of a nonprivileged user.\n\nNetwork access"
- "network connection.\n\nThe DoD CAC with DoD-approved PKI is an"
+ "network connection.\n\nThe DoW CAC with DoW-approved PKI is an"
```

</details>

#### V-203642 — Changed

**The operating system must use multifactor authentication for local access to privileged accounts.**

STIG ID: `SRG-OS-000107-GPOS-00054`. Severity: medium.
Rule ID: `SV-203642r982203_rule` → `SV-203642r1268230_rule`.
CCI: CCI-000765.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(1)][cw-ia-2.1].
- **Baseline / control determinations:** `ia-2.1`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `ia-2.1`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "a network.\n\nThe DOD CAC with DOD-approved PKI is an"
+ "a network.\n\nThe DoW CAC with DoW-approved PKI is an"
```

</details>

#### V-203643 — Changed

**The operating system must use multifactor authentication for local access to nonprivileged accounts.**

STIG ID: `SRG-OS-000108-GPOS-00055`. Severity: medium.
Rule ID: `SV-203643r982204_rule` → `SV-203643r1268231_rule`.
CCI: CCI-000766.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(2)][cw-ia-2.2].
- **Baseline / control determinations:** `ia-2.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.2`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "a network.\n\nThe DOD CAC with DOD-approved PKI is an"
+ "a network.\n\nThe DoW CAC with DoW-approved PKI is an"
```

</details>

#### V-203649 — Changed

**The operating system must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.**

STIG ID: `SRG-OS-000120-GPOS-00061`. Severity: medium.
Rule ID: `SV-203649r971535_rule` → `SV-203649r1268232_rule`.
CCI: CCI-000803.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-7][cw-ia-7].
- **Baseline / control determinations:** `ia-7`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-7`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "or integrity, and DoD data may be"
+ "or integrity, and DoW data may be"
- "cryptographic modules.\n\nFIPS 140-2/140-3 is the current"
+ "cryptographic modules.\n\nFIPS 140-3 is the current"
- "authentication that meets DoD requirements. This allows"
+ "authentication that meets DoW requirements. This allows"
```

</details>

#### V-203657 — Changed

**Operating systems must prevent unauthorized and unintended information transfer via shared system resources.**

STIG ID: `SRG-OS-000138-GPOS-00069`. Severity: medium.
Rule ID: `SV-203657r1137695_rule` → `SV-203657r1268233_rule`.
CCI: CCI-001090.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-4][cw-sc-4].
- **Baseline / control determinations:** `sc-4`: `host-inherited` (determination); handoff: [PLT-02], [PLT-07].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "acceptance/validation processes in DOD or other government"
+ "acceptance/validation processes in DoW or other government"
```

</details>

#### V-203665 — Changed

**Any publicly accessible connection to the operating system must display the Standard Mandatory DoW Notice and Consent Banner before granting access to the system.**

STIG ID: `SRG-OS-000228-GPOS-00088`. Severity: medium.
Rule ID: `SV-203665r958586_rule` → `SV-203665r1268236_rule`.
CCI: CCI-001384, CCI-001385, CCI-001386, CCI-001387, CCI-001388.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "Any publically accessible connection to"
+ "Any publicly accessible connection to"
- "the Standard Mandatory DoD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Discussion**

```diff
- "accordance with applicable DoD policy. Use the"
+ "accordance with applicable DoW policy. Use the"
```

**Check**

```diff
@@ -1,5 +1,5 @@
-Verify any publically accessible connection to the operating system displays the Standard Mandatory DoD Notice
- and Consent Banner before granting access to the system.
+Verify any publicly accessible connection to the operating system displays the Standard Mandatory DoW Notice
+and Consent Banner before granting access to the system.

-The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for
+The banner must be formatted in accordance with applicable DoW policy. Use the following verbiage for
 operating systems that can accommodate banners of 1300 characters:
```

**Fix**

```diff
@@ -1,5 +1,5 @@
-Configure any publically accessible connection to the operating system to display the Standard Mandatory DoD
+Configure any publicly-accessible connection to the operating system to display the Standard Mandatory DoW
 Notice and Consent Banner before granting access to the system.

-The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for
+The banner must be formatted in accordance with applicable DoW policy. Use the following verbiage for
 operating systems that can accommodate banners of 1300 characters:
```

</details>

#### V-203669 — Changed

**The operating system must implement cryptography to protect the integrity of remote access sessions.**

STIG ID: `SRG-OS-000250-GPOS-00093`. Severity: high.
Rule ID: `SV-203669r991554_rule` → `SV-203669r1268237_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "is access to DoD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
- "through an external, non-organization-controlled network. Remote access"
+ "through an external, nonorganization-controlled network. Remote access"
```

</details>

#### V-203686 — Changed

**The operating system must control remote access methods.**

STIG ID: `SRG-OS-000297-GPOS-00115`. Severity: medium.
Rule ID: `SV-203686r958672_rule` → `SV-203686r1268238_rule`.
CCI: CCI-002314.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Accepted rule entry; [AC-17(1)][cw-ac-17.1].
- **Baseline / control determinations:** `ac-17.1`: `host-inherited` (determination); handoff: [PLT-13].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "is access to DoD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-203705 — Changed

**The operating system must provide an audit reduction capability that supports after-the-fact investigations of security incidents.**

STIG ID: `SRG-OS-000349-GPOS-00137`. Severity: low.
Rule ID: `SV-203705r958768_rule` → `SV-203705r1268239_rule`.
CCI: CCI-001877.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Accepted rule entry; [AU-7][cw-au-7].
- **Baseline / control determinations:** `au-7`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Federal laws and DoD policies.\n\nAudit reduction"
+ "Federal laws and DoW policies.\n\nAudit reduction"
```

</details>

#### V-203708 — Changed

**The operating system must provide a report generation capability that supports after-the-fact investigations of security incidents.**

STIG ID: `SRG-OS-000352-GPOS-00140`. Severity: low.
Rule ID: `SV-203708r958774_rule` → `SV-203708r1268240_rule`.
CCI: CCI-001880.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Accepted rule entry; [AU-7][cw-au-7].
- **Baseline / control determinations:** `au-7`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "comply with applicable Federal laws and DoD policies.\n\nThe report"
+ "comply with applicable federal laws and DoW policies.\n\nThe report"
```

</details>

#### V-203720 — Changed

**The operating system must prevent the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization.**

STIG ID: `SRG-OS-000366-GPOS-00153`. Severity: high.
Rule ID: `SV-203720r982212_rule` → `SV-203720r1268241_rule`.
CCI: CCI-003992.

- **Image criteria:** direct: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22], [IMG-T2], [IMG-T4]; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "does not mandate DOD certificates for this"
+ "does not mandate DoW certificates for this"
- "from an approved CA."
+ "from an approved certificate authority (CA)."
```

</details>

#### V-203727 — Changed

**The operating system must implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access.**

STIG ID: `SRG-OS-000375-GPOS-00160`. Severity: medium.
Rule ID: `SV-203727r982216_rule` → `SV-203727r1268242_rule`.
CCI: CCI-004046.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(6)][cw-ia-2.6].
- **Baseline / control determinations:** `ia-2.6`: absent from current control baseline.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "card and the DOD CAC.\n\nA privileged"
+ "card and the DoW CAC.\n\nA privileged"
- "is access to DOD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-203728 — Changed

**The operating system must accept Personal Identity Verification (PIV) credentials.**

STIG ID: `SRG-OS-000376-GPOS-00161`. Severity: medium.
Rule ID: `SV-203728r958816_rule` → `SV-203728r1268243_rule`.
CCI: CCI-001953.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.12`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.12`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "of unauthorized access.\n\nDoD has mandated the"
+ "of unauthorized access.\n\nDoW has mandated the"
- "use of the CAC to support identity"
+ "use of the common access card (CAC) to support identity"
```

</details>

#### V-203729 — Changed

**The operating system must electronically verify Personal Identity Verification (PIV) credentials.**

STIG ID: `SRG-OS-000377-GPOS-00162`. Severity: medium.
Rule ID: `SV-203729r958818_rule` → `SV-203729r1268244_rule`.
CCI: CCI-001954.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.12`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.12`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "of unauthorized access.\n\nDoD has mandated the"
+ "of unauthorized access.\n\nDoW has mandated the"
- "use of the CAC to support identity"
+ "use of the common access card (CAC) to support identity"
```

</details>

#### V-203744 — Changed

**The operating system must only allow the use of DoW Public Key Infrastructure (PKI)-established certificate authorities for authentication in the establishment of protected sessions to the operating system.**

STIG ID: `SRG-OS-000403-GPOS-00182`. Severity: medium.
Rule ID: `SV-203744r958868_rule` → `SV-203744r1268247_rule`.
CCI: CCI-002470.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-23(5)][cw-sc-23.5].
- **Baseline / control determinations:** `sc-23.5`: absent from current control baseline.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the use of DoD PKI-established certificate authorities for"
+ "the use of DoW Public Key Infrastructure (PKI)-established certificate authorities for"
```

**Discussion**

```diff
- "seek to compromise DoD systems or by"
+ "seek to compromise DoW systems or by"
- "is not a DoD-approved CA, trust of"
+ "is not a DoW-approved CA, trust of"
- "been established.\n\nThe DoD will only accept"
+ "been established.\n\nThe DoW will only accept"
- "obtained from a DoD-approved internal or external"
+ "obtained from a DoW-approved internal or external"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify the operating system only allows the use of DoD PKI-established certificate authorities for
+Verify the operating system only allows the use of DoW PKI-established certificate authorities for
 verification of the establishment of protected sessions. If it does not, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the operating system to only allow the use of DoD PKI-established certificate authorities for
+Configure the operating system to only allow the use of DoW PKI-established certificate authorities for
 verification of the establishment of protected sessions.
```

</details>

#### V-203780 — Changed

**The operating system must be configured in accordance with the security configuration settings based on DoW security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.**

STIG ID: `SRG-OS-000480-GPOS-00227`. Severity: medium.
Rule ID: `SV-203780r991589_rule` → `SV-203780r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: [IMG-T3]; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "settings based on DoD security configuration or"
+ "settings based on DoW security configuration or"
```

**Discussion**

```diff
- "security baseline across DoD that reflects the"
+ "security baseline across DoW that reflects the"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify the operating system is configured in accordance with the security configuration settings based on DoD
+Verify the operating system is configured in accordance with the security configuration settings based on DoW
 security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the operating system in accordance with the security configuration settings based on DoD security
+Configure the operating system in accordance with the security configuration settings based on DoW security
 configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.
```

</details>

#### V-252688 — Changed

**The operating system must protect the confidentiality and integrity of communications with wireless peripherals.**

STIG ID: `SRG-OS-000481-GPOS-00481`. Severity: high.
Rule ID: `SV-252688r958358_rule` → `SV-252688r1268254_rule`.
CCI: CCI-002418.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-8][cw-sc-8].
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "peripherals must meet DoD requirements for wireless"
+ "peripherals must meet DoW requirements for wireless"
```

</details>

### GPOS SRG: revision-ID-only changes

These have identical compared content, severity and CCIs. They require no
criterion or control-determination change on this evidence; accepted rendered
crosswalk rule content is unchanged. A later regeneration may change rule IDs.

| Group ID | Old Rule ID | Candidate Rule ID |
| --- | --- | --- |
| V-259333 | `SV-259333r1137708_rule` | `SV-259333r1149426_rule` |

<a id="disa-container-platform-srg"></a>

## Container Platform SRG — V2R4 → V2R5

**Adopt.** 0 added, 0 removed, 14 changed. Comparison: committed Markdown + crosswalk → candidate XCCDF.

Of the 14 changed rules, 7 change check, fix, severity or CCI; 7 change only title/discussion/STIG ID.

### Container Platform SRG: added

None.

### Container Platform SRG: removed

None.

### Container Platform SRG: changed

#### V-233020 — Changed

**The container platform must automatically remove or disable temporary user accounts after 72 hours.**

STIG ID: `SRG-APP-000024-CTR-000060`. Severity: medium.
Rule ID: `SV-233020r960771_rule` → `SV-233020r1268078_rule`.
CCI: CCI-000016.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-2(2)][cw-ac-2.2].
- **Baseline / control determinations:** `ac-2.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-2.2`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "accounts after a DoD-defined period of 72"
+ "accounts after a DoW-defined period of 72"
```

</details>

#### V-233032 — Changed

**The container platform must display the Standard Mandatory DoW Notice and Consent Banner before granting access to platform components.**

STIG ID: `SRG-APP-000068-CTR-000120`. Severity: low.
Rule ID: `SV-233032r960843_rule` → `SV-233032r1268081_rule`.
CCI: CCI-000048.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DoD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Discussion**

```diff
- "presented with a DoD-approved use notification banner"
+ "presented with a DoW-approved use notification banner"
```

**Check**

```diff
@@ -1,8 +1,8 @@
-Review the container platform configuration to determine if the Standard Mandatory DoD Notice and Consent
+Review the container platform configuration to determine if the Standard Mandatory DoW Notice and Consent
 Banner is configured to be displayed before granting access to platform components.

-Log in to the container platform components and verify that the Standard Mandatory DoD  Notice and Consent
+Log in to the container platform components and verify that the Standard Mandatory DoW  Notice and Consent
 Banner is being displayed before granting access.

-If the Standard Mandatory DoD Notice and Consent Banner is not configured or is not displayed before granting
+If the Standard Mandatory DoW Notice and Consent Banner is not configured or is not displayed before granting
 access to container platform components, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the container platform to display the Standard Mandatory DoD Notice and Consent Banner before
+Configure the container platform to display the Standard Mandatory DoW Notice and Consent Banner before
 granting access to container platform components.
```

</details>

#### V-233033 — Changed

**The container platform must retain the Standard Mandatory DoW Notice and Consent Banner on the screen until users acknowledge the usage and conditions and take explicit actions to log on for further access.**

STIG ID: `SRG-APP-000069-CTR-000125`. Severity: low.
Rule ID: `SV-233033r960846_rule` → `SV-233033r1268084_rule`.
CCI: CCI-000050.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DoD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Discussion**

```diff
- "by the user, DoD will not be"
+ "by the user, DoW will not be"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Log in to the container platform components to determine if the Standard Mandatory DoD Notice and Consent
+Log in to the container platform components to determine if the Standard Mandatory DoW Notice and Consent
 Banner remains on the screen until users acknowledge the usage and conditions and take explicit actions to log
@@ -4,3 +4,3 @@

-If the Standard Mandatory DoD Notice and Consent Banner does not stay on the screen until the users
+If the Standard Mandatory DoW Notice and Consent Banner does not stay on the screen until the users
 acknowledge the usage and conditions, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the container platform to retain the Standard Mandatory DoD Notice and Consent Banner on the screen
+Configure the container platform to retain the Standard Mandatory DoW Notice and Consent Banner on the screen
 until users acknowledge the usage and conditions and take explicit actions to log on for further access.
```

</details>

#### V-233038 — Changed

**The container platform must generate audit records for all DoW-defined auditable events within all components in the platform.**

STIG ID: `SRG-APP-000089-CTR-000150`. Severity: medium.
Rule ID: `SV-233038r960879_rule` → `SV-233038r1268087_rule`.
CCI: CCI-000169.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AU-12][cw-au-12].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `au-12`: `image-owned`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "records for all DoD-defined auditable events within"
+ "records for all DoW-defined auditable events within"
```

**Discussion**

```diff
- "need to log DoD-defined auditable events, the"
+ "need to log DoW-defined auditable events, the"
```

**Check**

```diff
@@ -1,7 +1,7 @@
 Review the container platform configuration to determine if the container platform is configured to generate
-audit records for all DoD-defined auditable events within all components in the platform.
+audit records for all DoW-defined auditable events within all components in the platform.

-Generate DoD-defined auditable events within all the components to determine if the events are being audited.
+Generate DoW-defined auditable events within all the components to determine if the events are being audited.

-If the container platform is not configured to generate audit records for all DoD-defined auditable events
+If the container platform is not configured to generate audit records for all DoW-defined auditable events
 within the components or the events are  not generating audit records, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the container platform to generate audit records for all DoD-defined auditable events within all the
+Configure the container platform to generate audit records for all DoW-defined auditable events within all the
  components of the container platform.
```

</details>

#### V-233080 — Changed

**The container platform must use multifactor authentication for network access to nonprivileged accounts.**

STIG ID: `SRG-APP-000150-CTR-000360`. Severity: medium.
Rule ID: `SV-233080r960975_rule` → `SV-233080r1268088_rule`.
CCI: CCI-000766.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(2)][cw-ia-2.2].
- **Baseline / control determinations:** `ia-2.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.2`: `not-applicable`.

**Changed fields:** title, discussion.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "network access to non-privileged accounts."
+ "network access to nonprivileged accounts."
```

**Discussion**

```diff
- "prevent unauthenticated access, non-privileged users must utilize"
+ "prevent unauthenticated access, nonprivileged users must utilize"
- "(e.g., biometric).\n\nA non-privileged account is any"
+ "(e.g., biometric).\n\nA nonprivileged account is any"
- "authorizations of a non-privileged user.\n\nNetwork access"
+ "authorizations of a nonprivileged user.\n\nNetwork access"
- "integrating with the DoD Active Directory and utilize the DoD CAC are examples of"
+ "integrating with the DoW Active Directory and utilize the DoW common access card (CAC) are examples of"
```

</details>

#### V-233084 — Changed

**The container platform must use FIPS-validated SHA-1 or higher hash function to provide replay-resistant authentication mechanisms for network access to privileged accounts.**

STIG ID: `SRG-APP-000156-CTR-000380`. Severity: medium.
Rule ID: `SV-233084r960993_rule` → `SV-233084r1268089_rule`.
CCI: CCI-001941.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(8)][cw-ia-2.8].
- **Baseline / control determinations:** `ia-2.8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.8`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "assured. Use of DoD PKI is inherently"
+ "assured. Use of DoW PKI is inherently"
```

</details>

#### V-233095 — Changed

**For container platform using password authentication, the application must store only cryptographic representations of passwords.**

STIG ID: `SRG-APP-000171-CTR-000435`. Severity: medium.
Rule ID: `SV-233095r981861_rule` → `SV-233095r1268090_rule`.
CCI: CCI-004062.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "not a current DOD employee, member of"
+ "not a current DoW employee, member of"
- "the military, or DOD contractor.\n\n- When"
+ "the military, or DoW contractor.\n\n- When"
```

</details>

#### V-233098 — Changed

**The container platform must enforce a 180-day maximum password lifetime restriction.**

STIG ID: `SRG-APP-000174-CTR-000450`. Severity: medium.
Rule ID: `SV-233098r1043190_rule` → `SV-233098r1268077_rule`.
CCI: CCI-004066.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "must enforce a 60-day maximum password lifetime"
+ "must enforce a 180-day maximum password lifetime"
```

**Check**

```diff
@@ -1,4 +1,4 @@
-Review the container platform configuration to determine if it enforces a 60-day maximum password lifetime
+Review the container platform configuration to determine if it enforces a 180-day maximum password lifetime
 restriction.

-If the container platform does not enforce a 60-day maximum password lifetime restriction, this is a finding.
+If the container platform does not enforce a 180-day maximum password lifetime restriction, this is a finding.
```

**Fix**

```diff
@@ -1 +1 @@
-Configure the container platform to enforce a 60-day maximum password lifetime restriction.
+Configure the container platform to enforce a 180-day maximum password lifetime restriction.
```

</details>

#### V-233101 — Changed

**The container platform must map the authenticated identity to the individual user or group account for PKI-based authentication.**

STIG ID: `SRG-APP-000177-CTR-000465`. Severity: medium.
Rule ID: `SV-233101r961044_rule` → `SV-233101r1268093_rule`.
CCI: CCI-000187.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-5(2)][cw-ia-5.2].
- **Baseline / control determinations:** `ia-5.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.2`: `not-applicable`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,3 +1,3 @@
 Review documentation and configuration to ensure the container platform provides a PKI integration capability
-that meets DoD PKI infrastructure requirements.
+that meets DoW PKI infrastructure requirements.

```

**Fix**

```diff
@@ -1 +1 @@
-Configure the container platform to utilize the DoD Enterprise PKI infrastructure.
+Configure the container platform to utilize the DoW Enterprise PKI infrastructure.
```

</details>

#### V-233190 — Changed

**All nonessential, unnecessary, and unsecure DoW ports, protocols, and services must be disabled in the container platform.**

STIG ID: `SRG-APP-000383-CTR-000910`. Severity: medium.
Rule ID: `SV-233190r961470_rule` → `SV-233190r1268094_rule`.
CCI: CCI-001762.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [CM-7(1)][cw-cm-7.1].
- **Baseline / control determinations:** `cm-7.1`: `organization-inherited` (determination).

**Changed fields:** title, discussion.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "All non-essential, unnecessary, and unsecure DoD ports, protocols, and"
+ "All nonessential, unnecessary, and unsecure DoW ports, protocols, and"
```

**Discussion**

```diff
- "authorized by the DoD.\n\nTo validate that"
+ "authorized by the DoW.\n\nTo validate that"
- "be unneeded or non-secure."
+ "be unneeded or nonsecure."
```

</details>

#### V-233193 — Changed

**The container platform must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.**

STIG ID: `SRG-APP-000389-CTR-000925`. Severity: medium.
Rule ID: `SV-233193r1050787_rule` → `SV-233193r1268095_rule`.
CCI: CCI-002038.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-11][cw-ia-11].
- **Baseline / control determinations:** `ia-11`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-11`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Periodically.\n\nWithin the DOD, the minimum circumstances"
+ "Periodically.\n\nWithin the DoW, the minimum circumstances"
```

</details>

#### V-233195 — Changed

**The container platform must be configured to use multifactor authentication for user authentication.**

STIG ID: `SRG-APP-000391-CTR-000935`. Severity: medium.
Rule ID: `SV-233195r961494_rule` → `SV-233195r1268098_rule`.
CCI: CCI-001953.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.12`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.12`: `not-applicable`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "configured to use multi-factor authentication for user"
+ "configured to use multifactor authentication for user"
```

**Discussion**

```diff
- "the preferred method.\n\nDoD has mandated the"
+ "the preferred method.\n\nDoW has mandated the"
- "use of the CAC to support identity"
+ "use of the common access card (CAC) to support identity"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Review documentation and configuration to ensure the container platform is configured to use an approved DoD
+Review documentation and configuration to ensure the container platform is configured to use an approved DoW
 multifactor token (CAC) when accessing platform via user interfaces.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the container platform to accept standard DoD multifactor token-based credentials when users
+Configure the container platform to accept standard DoW multifactor token-based credentials when users
 interface with the platform.
```

</details>

#### V-233207 — Changed

**Container platform applications and Application Program Interfaces (API) used for nonlocal maintenance sessions must use FIPS-validated keyed-hash message authentication code (HMAC) to protect the integrity of nonlocal maintenance and diagnostic communications.**

STIG ID: `SRG-APP-000411-CTR-000995`. Severity: medium.
Rule ID: `SV-233207r961554_rule` → `SV-233207r1270941_rule`.
CCI: CCI-002890.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [MA-4(6)][cw-ma-4.6].
- **Baseline / control determinations:** `ma-4.6`: absent from current control baseline.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "or integrity, and DoD data may be"
+ "or integrity, and DoW data may be"
```

</details>

#### V-233273 — Changed

**Container platform components must be configured in accordance with the security configuration settings based on DoW security configuration or implementation guidance, including SRGs, STIGs, NSA configuration guides, CTOs, and DTMs.**

STIG ID: `SRG-APP-000516-CTR-001325`. Severity: medium.
Rule ID: `SV-233273r961863_rule` → `SV-233273r1268102_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "settings based on DoD security configuration or"
+ "settings based on DoW security configuration or"
```

**Check**

```diff
@@ -2,3 +2,3 @@
 validate that any services that are offered are configured in accordance with the security configuration
-settings based on DoD security configuration or implementation guidance, including SRGs, STIGs, NSA
+settings based on DoW security configuration or implementation guidance, including SRGs, STIGs, NSA
 configuration guides, CTOs, and DTMs.
@@ -6,3 +6,3 @@
 If container platform services are not configured in accordance with the security configuration settings based
- on DoD security configuration or implementation guidance, including SRGs, STIGs, NSA configuration guides,
+ on DoW security configuration or implementation guidance, including SRGs, STIGs, NSA configuration guides,
 CTOs, and DTMs, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure container services in accordance with the security configuration settings based on DoD security
+Configure container services in accordance with the security configuration settings based on DoW security
 configuration or implementation guidance, including SRGs, STIGs, NSA configuration guides, CTOs, and DTMs.
```

</details>

### Container Platform SRG: revision-ID-only changes

These have identical compared content, severity and CCIs. They require no
criterion or control-determination change on this evidence; accepted rendered
crosswalk rule content is unchanged. A later regeneration may change rule IDs.

| Group ID | Old Rule ID | Candidate Rule ID |
| --- | --- | --- |
| V-233276 | `SV-233276r961869_rule` | `SV-233276r1201983_rule` |
| V-233290 | `SV-233290r961911_rule` | `SV-233290r1250356_rule` |

<a id="disa-application-server-srg"></a>

## Application Server SRG — V4R5 → V4R6

**Adopt with changes.** 0 added, 0 removed, 17 changed. Comparison: committed Markdown + crosswalk → candidate XCCDF.

Of the 17 changed rules, 6 change check, fix, severity or CCI; 11 change only title/discussion/STIG ID.

### Application Server SRG: added

None.

### Application Server SRG: removed

None.

### Application Server SRG: changed

#### V-204708 — Changed

**The application server must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.**

STIG ID: `SRG-APP-000001-AS-000001`. Severity: medium.
Rule ID: `SV-204708r960735_rule` → `SV-204708r1265167_rule`.
CCI: CCI-000054.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-10][cw-ac-10].
- **Baseline / control determinations:** `ac-10`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-10`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "settings should follow DoD-recommended values, but the"
+ "settings should follow DoW-recommended values, but the"
- "allow for future DoD direction.\n\nWhile the DoD will specify recommended"
+ "allow for future DoW direction.\n\nWhile the DoW will specify recommended"
```

</details>

#### V-204716 — Changed

**For application servers providing log record aggregation, the application server must compile log records from organization-defined information system components into a system-wide log trail that is time-correlated with an organization-defined level of tolerance for the relationship between time stamps of individual records in the log trail.**

STIG ID: `SRG-APP-000086-AS-000048`. Severity: medium.
Rule ID: `SV-204716r960873_rule` → `SV-204716r1265168_rule`.
CCI: CCI-000174.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Accepted rule entry; [AU-12(1)][cw-au-12.1].
- **Baseline / control determinations:** `au-12.1`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "criteria. For instance, DoD may define that"
+ "criteria. For instance, DoW may define that"
```

</details>

#### V-204740 — Changed

**The application server must prevent the installation of patches, service packs, or application components without verification the software component has been digitally signed using a certificate recognized and approved by the organization.**

STIG ID: `SRG-APP-000131-AS-000002`. Severity: medium.
Rule ID: `SV-204740r981678_rule` → `SV-204740r1265169_rule`.
CCI: CCI-003992.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Accepted rule entry; [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "does not mandate DOD certificates for this"
+ "does not mandate DoW certificates for this"
```

</details>

#### V-204743 — Changed

**The application server must adhere to the principles of least functionality by providing only essential capabilities.**

STIG ID: `SRG-APP-000141-AS-000095`. Severity: medium.
Rule ID: `SV-204743r960963_rule` → `SV-204743r1265170_rule`.
CCI: CCI-000381.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Accepted rule entry; [CM-7][cw-cm-7].
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "on a production DoD system. Application servers"
+ "on a production DoW system. Application servers"
```

</details>

#### V-204744 — Changed

**The application server must prohibit or restrict the use of nonsecure ports, protocols, modules, and/or services as defined in the PPSM CAL and vulnerability assessments.**

STIG ID: `SRG-APP-000142-AS-000014`. Severity: medium.
Rule ID: `SV-204744r1043177_rule` → `SV-204744r1265171_rule`.
CCI: CCI-000382.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Accepted rule entry; [CM-7][cw-cm-7].
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "protocols, reference the DoD ports and protocols"
+ "protocols, reference the DoW ports and protocols"
```

</details>

#### V-204745 — Changed

**The application server must use an approved DoW enterprise identity, credential, and access management (ICAM) solution to uniquely identify and authenticate users (or processes acting on behalf of organizational users).**

STIG ID: `SRG-APP-000148-AS-000101`. Severity: medium.
Rule ID: `SV-204745r1051118_rule` → `SV-204745r1265172_rule`.
CCI: CCI-000764.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2][cw-ia-2].
- **Baseline / control determinations:** `ia-2`: `research-required` (determination); handoff: [PLT-18].
- **Reference image decisions to review:** `ia-2`: `not-applicable`.

**Changed fields:** title, discussion.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "use an approved DOD enterprise identity, credential,"
+ "use an approved DoW enterprise identity, credential,"
```

**Discussion**

```diff
- "use an approved DOD enterprise (E-ICAM) solution"
+ "use an approved DoW enterprise (E-ICAM) solution"
- "and transition to DOD enterprise ICAM solutions"
+ "and transition to DoW enterprise ICAM solutions"
```

</details>

#### V-204756 — Changed

**The application server must map the authenticated identity to the individual user or group account for PKI-based authentication.**

STIG ID: `SRG-APP-000177-AS-000126`. Severity: medium.
Rule ID: `SV-204756r961044_rule` → `SV-204756r1265175_rule`.
CCI: CCI-000187.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-5(2)][cw-ia-5.2].
- **Baseline / control determinations:** `ia-5.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.2`: `not-applicable`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " to a user.  Without mapping the "
+ " to a user. Without mapping the "
- "requirements of the DoD Enterprise PKI infrastructure"
+ "requirements of the DoW Enterprise PKI infrastructure"
```

**Check**

```diff
@@ -1,3 +1,3 @@
 Review application server documentation to ensure the application server provides a PKI integration capability
- that meets DoD PKI infrastructure requirements.
+ that meets DoW PKI infrastructure requirements.

```

**Fix**

```diff
@@ -1 +1 @@
-Configure the application server to utilize the DoD Enterprise PKI infrastructure.
+Configure the application server to utilize the DoW Enterprise PKI infrastructure.
```

</details>

#### V-204758 — Changed

**The application server must utilize FIPS 140-2 approved encryption modules when authenticating users and processes.**

STIG ID: `SRG-APP-000179-AS-000129`. Severity: high.
Rule ID: `SV-204758r961050_rule` → `SV-204758r1265176_rule`.
CCI: CCI-000803.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-7][cw-ia-7].
- **Baseline / control determinations:** `ia-7`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-7`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " encryption modules utilized.  Unapproved cryptographic module "
+ " encryption modules utilized. Unapproved cryptographic module "
- "or integrity, and DoD data may be"
+ "or integrity, and DoW data may be"
- " to weak algorithms.  The use of "
+ " to weak algorithms. The use of "
- " must be disabled.  NIST SP 800-52 "
+ " must be disabled. NIST SP 800-52 "
```

</details>

#### V-204770 — Changed

**The application server must protect the confidentiality and integrity of all information at rest.**

STIG ID: `SRG-APP-000231-AS-000133`. Severity: medium.
Rule ID: `SV-204770r961128_rule` → `SV-204770r1265177_rule`.
CCI: CCI-001199.

- **Image criteria:** direct: None; shared-control review: [IMG-15].
- **Crosswalk:** Accepted rule entry; [SC-28][cw-sc-28].
- **Baseline / control determinations:** `sc-28`: `host-inherited` (determination); handoff: [PLT-17].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "data owners and DoD consider routinely encrypting"
+ "data owners and the DoW should consider routinely encrypting"
```

</details>

#### V-204798 — Changed

**The application server must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.**

STIG ID: `SRG-APP-000389-AS-000253`. Severity: medium.
Rule ID: `SV-204798r1050785_rule` → `SV-204798r1265178_rule`.
CCI: CCI-002038.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-11][cw-ia-11].
- **Baseline / control determinations:** `ia-11`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-11`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Periodically.\n\nWithin the DOD, the minimum circumstances"
+ "Periodically.\n\nWithin the DoW, the minimum circumstances"
```

</details>

#### V-204800 — Changed

**The application server must accept Personal Identity Verification (PIV) credentials to access the management interface.**

STIG ID: `SRG-APP-000391-AS-000239`. Severity: high.
Rule ID: `SV-204800r961494_rule` → `SV-204800r1265179_rule`.
CCI: CCI-001953.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.12`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.12`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "an unclassified environment.\n\nDoD has mandated the"
+ "an unclassified environment.\n\nDoW has mandated the"
```

</details>

#### V-204801 — Changed

**The application server must electronically verify Personal Identity Verification (PIV) credentials for access to the management interface.**

STIG ID: `SRG-APP-000392-AS-000240`. Severity: high.
Rule ID: `SV-204801r961497_rule` → `SV-204801r1265180_rule`.
CCI: CCI-001954.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.12`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.12`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "an unclassified environment.\n\nDoD has mandated the"
+ "an unclassified environment.\n\nDoW has mandated the"
```

</details>

#### V-204807 — Changed

**The application server must electronically verify Personal Identity Verification (PIV) credentials from other federal agencies to access the management interface.**

STIG ID: `SRG-APP-000403-AS-000248`. Severity: medium.
Rule ID: `SV-204807r961530_rule` → `SV-204807r1265182_rule`.
CCI: CCI-002010.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-8(1)][cw-ia-8.1].
- **Baseline / control determinations:** `ia-8.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-8.1`: `not-applicable`.

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " of PIV credentials.  PIV credentials are "
+ " of PIV credentials. PIV credentials are "
```

**Check**

```diff
@@ -1,5 +1,5 @@
-The CAC is the standard DoD authentication token;the PIV is the standard authentication token used by
+The CAC is the standard DoW authentication token; the PIV is the standard authentication token used by
 federal/civilian agencies.

-If access to the application server is limited to DoD personnel accessing the system via CAC; and PIV access
+If access to the application server is limited to DoW personnel accessing the system via CAC; and PIV access
 is not warranted or allowed as per the system security plan, the PIV requirement is NA.
```

</details>

#### V-204811 — Changed

**The application server must only allow the use of DoW PKI-established certificate authorities for verification of the establishment of protected sessions.**

STIG ID: `SRG-APP-000427-AS-000264`. Severity: medium.
Rule ID: `SV-204811r961596_rule` → `SV-204811r1265185_rule`.
CCI: CCI-002470.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-23(5)][cw-sc-23.5].
- **Baseline / control determinations:** `sc-23.5`: absent from current control baseline.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the use of DoD PKI-established certificate authorities"
+ "the use of DoW PKI-established certificate authorities"
```

**Discussion**

```diff
- "seek to compromise DoD systems or by"
+ "seek to compromise DoW systems or by"
- "is not a DoD-approved CA, trust of"
+ "is not a DoW-approved CA, trust of"
- "been established.\n\nThe DoD will only accept"
+ "been established.\n\nThe DoW will only accept"
- "obtained from a DoD-approved internal or external"
+ "obtained from a DoW-approved internal or external"
- " of SSL/TLS certificates.  The application server "
+ " of SSL/TLS certificates. The application server "
- "the use of DoD PKI-established certificate authorities"
+ "the use of DoW PKI-established certificate authorities"
```

**Check**

```diff
@@ -1,3 +1,3 @@
 Review the application server documentation and configuration to determine if the application server only
-allows the use of DoD PKI-established certificate authorities.
+allows the use of DoW PKI-established certificate authorities.

```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the application server to allow the use of DoD PKI-established certificate authorities for
+Configure the application server to allow the use of DoW PKI-established certificate authorities for
 verification of the establishment of protected sessions.
```

</details>

#### V-204832 — Changed

**The application server must use DoW or CNSS-approved PKI Class 3 or Class 4 certificates.**

STIG ID: `SRG-APP-000514-AS-000137`. Severity: medium.
Rule ID: `SV-204832r1137585_rule` → `SV-204832r1265188_rule`.
CCI: CCI-002450.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-13][cw-sc-13].
- **Baseline / control determinations:** `sc-13`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-13`: `research-required`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "server must use DOD- or CNSS-approved PKI"
+ "server must use DoW or CNSS-approved PKI"
```

**Discussion**

```diff
- "or approved by DOD or CNS creates"
+ "or approved by DoW or CNS creates"
- "must utilize approved DOD or CNS Class"
+ "must utilize approved DoW or CNS Class"
```

**Check**

```diff
@@ -3,2 +3,2 @@

-If the application server is not configured to use approved DOD or CNS certificates, this is a finding.
+If the application server is not configured to use approved DoW or CNS certificates, this is a finding.
```

**Fix**

```diff
@@ -1 +1 @@
-Configure the application server to use DOD- or CNSS-approved Class 3 or Class 4 PKI certificates.
+Configure the application server to use DoW or CNSS-approved Class 3 or Class 4 PKI certificates.
```

</details>

#### V-204833 — Changed

**The application server must, at a minimum, transfer the logs of interconnected systems in real time, and transfer the logs of standalone systems weekly.**

STIG ID: `SRG-APP-000515-AS-000203`. Severity: medium → high.
Rule ID: `SV-204833r961860_rule` → `SV-204833r1265166_rule`.
CCI: CCI-001851.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AU-4(1)][cw-au-4.1].
- **Baseline / control determinations:** `au-4.1`: absent from current control baseline.

**Changed fields:** discussion, severity.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " deletion or alteration.  Protecting log data "
+ " deletion or alteration. Protecting log data "
- " may have occurred.  Off-loading should be "
+ " may have occurred. Off-loading should be "
```

</details>

#### V-204834 — Changed

**The application server must be configured in accordance with the security configuration settings based on DoW security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.**

STIG ID: `SRG-APP-000516-AS-000237`. Severity: medium.
Rule ID: `SV-204834r961863_rule` → `SV-204834r1265191_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "settings based on DoD security configuration or"
+ "settings based on DoW security configuration or"
```

**Discussion**

```diff
- "security baseline across DoD that reflects the"
+ "security baseline across DoW that reflects the"
```

**Check**

```diff
@@ -1,3 +1,3 @@
 Review the application server documentation and configuration to determine if the application server is
-configured in accordance with the security configuration settings based on DoD security configuration or
+configured in accordance with the security configuration settings based on DoW security configuration or
 implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the application server to be in accordance with the security configuration settings based on DoD
+Configure the application server to be in accordance with the security configuration settings based on DoW
 security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.
```

</details>

### Application Server SRG: revision-ID-only changes

None.


<a id="disa-rhel9-stig"></a>

## RHEL 9 STIG — V2R4 → V2R10

**Hold.** 3 added, 10 removed, 166 changed. Comparison: pinned ZIP XCCDF → candidate XCCDF.

Of the 166 changed rules, 150 change check, fix, severity or CCI; 16 change only title/discussion/STIG ID.

No RHEL rule is currently rendered or present in the accepted crosswalk.
All rule-to-control joins here are prospective; shared-control image criteria
are review context only. The host expectations' pinned baseline and the IMG-T3 scan
selection also need review if this source is adopted. Removed rules are not
authority to remove the associated baseline control.

### RHEL 9 STIG: added

#### V-279936 — Added

**RHEL 9 must audit any script or executable called by cron as root or by any privileged user.**

STIG ID: `RHEL-09-654097`. Severity: medium.
Rule ID: `SV-279936r1210929_rule`.
CCI: CCI-000172.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [AU-12][cw-au-12].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `au-12`: `image-owned`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify RHEL 9 is configured to audit the execution of any system call made by cron as root or by any privileged user with the following command:

$ sudo auditctl -l | grep crond_t
-a always,exit -F arch=b64 -S execve -F subj_type=crond_t -F euid=0 -k cron_exec
-a always,exit -F arch=b32 -S execve -F subj_type=crond_t -F euid=0 -k cron_exec
-a always,exit -F arch=b64 -S execve -F subj_type=crond_t -F auid>=1000 -F auid!=unset -k cron_exec
-a always,exit -F arch=b32 -S execve -F subj_type=crond_t -F auid>=1000 -F auid!=unset -k cron_exec

If this command does not return the expected output, or the lines are commented out, this is a finding.
```

**Fix**

```text
Configure RHEL 9 to audit the execution of any system call made by cron as root or by any privileged user.

Add or update the following file system rules to "/etc/audit/rules.d/audit.rules":

-a always,exit -F arch=b64 -S execve -F subj_type=crond_t -F euid=0 -k cron_exec
-a always,exit -F arch=b32 -S execve -F subj_type=crond_t -F euid=0 -k cron_exec
-a always,exit -F arch=b64 -S execve -F subj_type=crond_t -F auid>=1000 -F auid!=unset -k cron_exec
-a always,exit -F arch=b32 -S execve -F subj_type=crond_t -F auid>=1000 -F auid!=unset -k cron_exec

To load the rules to the kernel immediately, use the following command:

$ sudo augenrules --load
```

</details>

#### V-288832 — Added

**RHEL 9 must audit all uses of the useradd command.**

STIG ID: `RHEL-09-654176`. Severity: medium.
Rule ID: `SV-288832r1262053_rule`.
CCI: CCI-000130.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [AU-3][cw-au-3].
- **Baseline / control determinations:** `au-3`: `research-required` (undetermined).
- **Reference image decisions to review:** `au-3`: `image-owned`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify that RHEL 9 is configured to audit the execution of the "useradd" command with the following command:

$ sudo auditctl -l | grep useradd

-a always,exit -S all -F path=/usr/sbin/useradd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-useradd

If the command does not return a line or the line is commented out, this is a finding.
```

**Fix**

```text
Configure RHEL 9 to generate audit records upon successful/unsuccessful attempts to use the "useradd " command by adding or updating the following rule in "/etc/audit/rules.d/audit.rules":

-a always,exit -F path=/usr/sbin/useradd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-useradd

To load the rules to the kernel immediately, use the following command:

$ sudo augenrules --load
```

</details>

#### V-288833 — Added

**RHEL 9 must implement DoW-approved encryption in the OpenSSL package.**

STIG ID: `RHEL-09-672055`. Severity: high.
Rule ID: `SV-288833r1268237_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the RHEL 9 OpenSSL library is configured to use only ciphers employing FIPS 140-3-approved algorithms with the following command:

$ grep -i opensslcnf.config /etc/pki/tls/openssl.cnf
.include = /etc/crypto-policies/back-ends/opensslcnf.config

If the "opensslcnf.config" is not defined in the "/etc/pki/tls/openssl.cnf" file, this is a finding.
```

**Fix**

```text
Configure the RHEL 9 OpenSSL library to use the systemwide cryptographic policy.

Edit the "/etc/pki/tls/openssl.cnf" and add or modify the following line:

.include = /etc/crypto-policies/back-ends/opensslcnf.config
```

</details>

### RHEL 9 STIG: removed

#### V-257829 — Removed

**RHEL 9 must not have the ypserv package installed.**

STIG ID: `RHEL-09-215030`. Severity: medium.
Rule ID: `SV-257829r1044896_rule`.
CCI: CCI-000381.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7][cw-cm-7] → None.
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify that the ypserv package is not installed with the following command:

$ dnf list --installed ypserv

Error: No matching Packages to list

If the "ypserv" package is installed, this is a finding.
```

**Fix**

```text
Remove the ypserv package with the following command:

$ sudo dnf remove ypserv
```

</details>

#### V-257836 — Removed

**RHEL 9 must not have the quagga package installed.**

STIG ID: `RHEL-09-215065`. Severity: medium.
Rule ID: `SV-257836r1044908_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6] → None.
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify that the quagga package is not installed with the following command:

$ dnf list --installed quagga

Error: No matching Packages to list

If the "quagga" package is installed and is not documented with the information system security officer (ISSO) as an operational requirement, this is a finding.
```

**Fix**

```text
Remove the quagga package with the following command:

$ sudo dnf remove quagga
```

</details>

#### V-257987 — Removed

**RHEL 9 SSH daemon must be configured to use system-wide crypto policies.**

STIG ID: `RHEL-09-255055`. Severity: medium.
Rule ID: `SV-257987r1014852_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2] → None.
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify that systemwide crypto policies are in effect with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*include'

/etc/ssh/sshd_config:Include /etc/ssh/sshd_config.d/*.conf
/etc/ssh/sshd_config.d/50-redhat.conf:Include /etc/crypto-policies/back-ends/opensshserver.config

If "Include /etc/ssh/sshd_config.d/*.conf" or "Include /etc/crypto-policies/back-ends/opensshserver.config" are not included in the system sshd config this is a finding. Additionally, if the file /etc/ssh/sshd_config.d/50-redhat.conf is missing, this is a finding.
```

**Fix**

```text
Configure the RHEL 9 SSH daemon to use system-wide crypto policies by running the following commands:

$ sudo dnf reinstall openssh-server
```

</details>

#### V-257988 — Removed

**RHEL 9 must implement DOD-approved encryption ciphers to protect the confidentiality of SSH connections.**

STIG ID: `RHEL-09-255060`. Severity: medium.
Rule ID: `SV-257988r1051234_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2] → None.
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify that RHEL 9 implements DOD-approved encryption ciphers for SSH connections.

Verify that the SSH configuration files include the path to the systemwide policy with the following command:

$ sudo grep -R Include /etc/ssh/sshd_config  /etc/ssh/sshd_config.d/

/etc/ssh/sshd_config:Include /etc/ssh/sshd_config.d/*.conf
/etc/ssh/sshd_config.d/50-redhat.conf:Include /etc/crypto-policies/back-ends/opensshserver.config

If "Include /etc/ssh/sshd_config.d/*.conf" or "Include /etc/crypto-policies/back-ends/opensshserver.config" are not included in the system sshd config or if the file "/etc/ssh/sshd_config.d/50-redhat.conf" is missing, this is a finding.
```

**Fix**

```text
Configure the RHEL 9 SSH daemon to use systemwide crypto policies.

Reinstall OpenSSH client package contents with the following command:

$ sudo dnf -y reinstall openssh
```

</details>

#### V-258002 — Removed

**RHEL 9 SSH daemon must not allow compression or must only allow compression after successful authentication.**

STIG ID: `RHEL-09-255130`. Severity: medium.
Rule ID: `SV-258002r991589_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6] → None.
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the SSH daemon performs compression after a user successfully authenticates with the following command:

$ sudo /usr/sbin/sshd -dd 2>&1 | awk '/filename/ {print $4}' | tr -d '\r' | tr '\n' ' ' | xargs sudo grep -iH '^\s*compression'

Compression delayed

If the "Compression" keyword is set to "yes", is missing, or the returned line is commented out, this is a finding.
```

**Fix**

```text
Configure the SSH daemon to not allow compression.

Uncomment the "Compression" keyword in "/etc/ssh/sshd_config" on the system and set the value to "delayed" or "no":

Compression no

The SSH service must be restarted for changes to take effect:

$ sudo systemctl restart sshd.service
```

</details>

#### V-258062 — Removed

**Local RHEL 9 initialization files must not execute world-writable programs.**

STIG ID: `RHEL-09-411115`. Severity: medium.
Rule ID: `SV-258062r991589_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6] → None.
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify that local initialization files do not execute world-writable programs with the following command:

Note: The example will be for a system that is configured to create user home directories in the "/home" directory.

$ sudo find /home -perm -002 -type f -name ".[^.]*" -exec ls -ld {} \;

If any local initialization files are found to reference world-writable files, this is a finding.
```

**Fix**

```text
Set the mode on files being executed by the local initialization files with the following command:

$ sudo chmod 0755 <file>
```

</details>

#### V-258076 — Removed

**RHEL 9 must display the date and time of the last successful account logon upon logon.**

STIG ID: `RHEL-09-412075`. Severity: low.
Rule ID: `SV-258076r991589_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6] → None.
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify users are provided with feedback on when account accesses last occurred with the following command:

$ sudo grep pam_lastlog /etc/pam.d/postlogin

session required pam_lastlog.so showfailed

If "pam_lastlog" is missing from "/etc/pam.d/postlogin" file, or the silent option is present, this is a finding.
```

**Fix**

```text
Configure RHEL 9 to provide users with feedback on when account accesses last occurred by setting the required configuration options in "/etc/pam.d/postlogin".

Add the following line to the top of "/etc/pam.d/postlogin":

session required pam_lastlog.so showfailed
```

</details>

#### V-258172 — Removed

**RHEL 9 /etc/audit/auditd.conf file must have 0640 or less permissive to prevent unauthorized access.**

STIG ID: `RHEL-09-653115`. Severity: medium.
Rule ID: `SV-258172r958444_rule`.
CCI: CCI-000171.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-12][cw-au-12] → None.
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `au-12`: `image-owned`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the mode of /etc/audit/auditd.conf with the command:

$ sudo stat -c "%a %n" /etc/audit/auditd.conf

640 /etc/audit/auditd.conf

If "/etc/audit/auditd.conf" does not have a mode of "0640", this is a finding.
```

**Fix**

```text
Set the mode of /etc/audit/auditd.conf file to 0640 with the command:

$ sudo chmod 0640 /etc/audit/auditd.conf
```

</details>

#### V-258226 — Removed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/tallylog.**

STIG ID: `RHEL-09-654260`. Severity: medium.
Rule ID: `SV-258226r958846_rule`.
CCI: CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1] → None.
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify RHEL 9 generates audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/tallylog" with the following command:

$ sudo auditctl -l | grep /var/log/tallylog

-w /var/log/tallylog -p wa -k logins

If the command does not return a line, or the line is commented out, is a finding.
```

**Fix**

```text
Configure RHEL 9 to generate audit records for all account creations, modifications, disabling, and termination events that affect "/var/log/tallylog".

Add or update the following file system rule to "/etc/audit/rules.d/audit.rules":

-w /var/log/tallylog -p wa -k logins

The audit daemon must be restarted for the changes to take effect.
```

</details>

#### V-258237 — Removed

**RHEL 9 must use mechanisms meeting the requirements of applicable federal laws, executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.**

STIG ID: `RHEL-09-672025`. Severity: medium.
Rule ID: `SV-258237r1051256_rule`.
CCI: CCI-000803.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-7][cw-ia-7] → None.
- **Baseline / control determinations:** `ia-7`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-7`: `not-applicable`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify that the symlink exists and targets the correct Kerberos cryptographic policy with the following command:

$ file /etc/crypto-policies/back-ends/krb5.config

If command output shows the following line, Kerberos is configured to use the systemwide crypto policy:

/etc/crypto-policies/back-ends/krb5.config: symbolic link to /usr/share/crypto-policies/FIPS/krb5.txt

If the symlink does not exist or points to a different target, this is a finding.
```

**Fix**

```text
Configure Kerberos to use system cryptographic policy.

Create a symlink pointing to system crypto policy in the Kerberos configuration using the following command:

$ sudo ln -s /etc/crypto-policies/back-ends/krb5.config /usr/share/crypto-policies/FIPS/krb5.txt
```

</details>

### RHEL 9 STIG: changed

#### V-257777 — Changed

**RHEL 9 must be a vendor-supported release.**

STIG ID: `RHEL-09-211010`. Severity: high.
Rule ID: `SV-257777r991589_rule` → `SV-257777r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "the system software.\n\nRed Hat offers the Extended Update Support (EUS) add-on to a Red Hat Enterprise Linux subscription, for a fee, for those customers who wish to standardize on a specific minor release for an extended period."
+ "the system software.\n\nEnd Of Life dates for Red Hat Linux 9 releases are as follows:\nCurrent end of Full Support for Red Hat Linux 9 is 31 May 2027.\nCurrent end of Maintenance Support for Red Hat Linux 9 is 31 May 3032.\nCurrent end of Extended Life Cycle Support (ELS) for Red Hat Linux 9 is 31 May 2035."
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify that the version or RHEL 9 is vendor supported with the following command:
+Verify the version or RHEL 9 is vendor supported with the following command:

@@ -4,3 +4,3 @@

-Red Hat Enterprise Linux release 9.2 (Plow)
+Red Hat Enterprise Linux release 9.6 (Plow)

```

</details>

#### V-257778 — Changed

**RHEL 9 vendor packaged system security patches and updates must be installed and up to date.**

STIG ID: `RHEL-09-211015`. Severity: medium.
Rule ID: `SV-257778r991589_rule` → `SV-257778r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -10,3 +10,3 @@

-$ dnf history list | more
+$ sudo dnf history list | more

```

</details>

#### V-257779 — Changed

**RHEL 9 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a command line user logon.**

STIG ID: `RHEL-09-211020`. Severity: medium.
Rule ID: `SV-257779r958390_rule` → `SV-257779r1268215_rule`.
CCI: CCI-000048, CCI-001384, CCI-001385, CCI-001386, CCI-001387, CCI-001388.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DOD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify RHEL 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the
+Verify RHEL 9 displays the Standard Mandatory DoW Notice and Consent Banner before granting access to the
 operating system via a command line user logon.
@@ -31,3 +31,3 @@

-If the banner text does not match the Standard Mandatory DOD Notice and Consent Banner exactly, or the line is
+If the banner text does not match the Standard Mandatory DoW Notice and Consent Banner exactly, or the line is
  commented out, this is a finding.
```

**Fix**

```diff
@@ -1,6 +1,6 @@
-Configure RHEL 9 to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the
+Configure RHEL 9 to display the Standard Mandatory DoW Notice and Consent Banner before granting access to the
  system via command line logon.

-Edit the "/etc/issue" file to replace the default text with the Standard Mandatory DOD Notice and Consent
-Banner. The DOD-required text is:
+Edit the "/etc/issue" file to replace the default text with the Standard Mandatory DoW Notice and Consent
+Banner. The DoW-required text is:

```

</details>

#### V-257784 — Changed

**The systemd Ctrl-Alt-Delete burst key sequence in RHEL 9 must be disabled.**

STIG ID: `RHEL-09-211045`. Severity: high.
Rule ID: `SV-257784r1044832_rule` → `SV-257784r1262100_rule`.
CCI: CCI-002235.

- **Image criteria:** direct: None; shared-control review: [IMG-11], [IMG-31].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-6(10)][cw-ac-6.10].
- **Baseline / control determinations:** `ac-6.10`: `image-owned` (criterion); handoff: [PLT-02].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -3,6 +3,5 @@

-$ grep -i ctrl /etc/systemd/system.conf
+$ sudo grep -iR CtrlAltDelBurstAction /etc/systemd/system*
+/etc/systemd/system.conf.d/55-CtrlAltDel-BurstAction.conf:CtrlAltDelBurstAction=none

-CtrlAltDelBurstAction=none
-
-If the "CtrlAltDelBurstAction" is not set to "none", commented out, or is missing, this is a finding.
+If the "CtrlAltDelBurstAction" is not set to "none", is commented out, or is missing, this is a finding.
```

**Fix**

```diff
@@ -1,4 +1,12 @@
-Configure the system to disable the CtrlAltDelBurstAction by added or modifying the following line in the
-"/etc/systemd/system.conf" configuration file:
+Configure RHEL 9 to disable the CtrlAltDelBurstAction by adding it to a drop file in a
+"/etc/systemd/system.conf.d/" configuration file:

+If no drop file exists, create one with the following command:
+
+$ sudo mkdir -p /etc/systemd/system.conf.d && sudo vi /etc/systemd/system.conf.d/55-CtrlAltDel-
+BurstAction.conf
+
+Edit the file to contain the setting by adding the following text:
+
+[Manager]
 CtrlAltDelBurstAction=none
```

</details>

#### V-257787 — Changed

**RHEL 9 must require authentication upon booting into single-user and maintenance modes.**

STIG ID: `RHEL-09-212010`. Severity: medium.
Rule ID: `SV-257787r1044836_rule` → `SV-257787r1268226_rule`.
CCI: CCI-000213.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-3][cw-ac-3].
- **Baseline / control determinations:** `ac-3`: `research-required` (determination); handoff: [PLT-06].
- **Reference image decisions to review:** `ac-3`: `deployment-configured`.

**Changed fields:** title, discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "9 must require a boot loader superuser password."
+ "9 must require authentication upon booting into single-user and maintenance modes."
```

**Discussion**

```diff
- "issued certificates by DOD-approved PKIs, all DOD systems (e.g., web"
+ "issued certificates by DoW-approved PKIs, all DoW systems (e.g., web"
```

**Check**

```diff
@@ -1,17 +1,19 @@
-Verify the boot loader superuser password has been set with the following command:
+Verify that RHEL 9 requires a password for the GRUB 2 bootloader to prevent unauthorized modifications to boot
+ parameters.

-$ sudo grep password_pbkdf2 /etc/grub2.cfg
+Check the unified configuration file where the GRUB 2 password is stored:

-password_pbkdf2  <superusers-accountname>   ${GRUB2_PASSWORD}
+# sudo grep -iw "GRUB2_PASSWORD" /boot/grub2/user.cfg
+GRUB2_PASSWORD=grub.pbkdf2.sha512.[password_hash]

-To verify the boot loader superuser account password has been set and the password encrypted, run the
-following command:
+If the "GRUB2_PASSWORD" entry does not exist, is commented out, or if the hash does not begin with
+"grub.pbkdf2.sha512", this is a finding.

-$ sudo cat /boot/grub2/user.cfg
+Note for upgraded systems: If the system was upgraded from an early release of RHEL 8 to RHEL 9, legacy
+configurations might still reside in the EFI partition. If "/boot/grub2/user.cfg" does not exist, verify the
+legacy path:

-GRUB2_PASSWORD=grub.pbkdf2.sha512.10000.C4E08AC72FBFF7E837FD267BFAD7AEB3D42DDC
-2C99F2A94DD5E2E75C2DC331B719FE55D9411745F82D1B6CFD9E927D61925F9BBDD1CFAA0080E0
-916F7AB46E0D.1302284FCCC52CD73BA3671C6C12C26FF50BA873293B24EE2A96EE3B57963E6D7
-0C83964B473EC8F93B07FE749AA6710269E904A9B08A6BBACB00A2D242AD828
+# grep -iw "GRUB2_PASSWORD" /boot/efi/EFI/redhat/user.cfg

-If a "GRUB2_PASSWORD" is not set, this is a finding.
+If the "GRUB2_PASSWORD" entry does not exist in either location, is commented out, or does not begin with
+"grub.pbkdf2.sha512", this is a finding.
```

</details>

#### V-257789 — Changed

**RHEL 9 must require a unique superusers name upon booting into single-user and maintenance modes.**

STIG ID: `RHEL-09-212020`. Severity: high.
Rule ID: `SV-257789r1069356_rule` → `SV-257789r1268226_rule`.
CCI: CCI-000213.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-3][cw-ac-3].
- **Baseline / control determinations:** `ac-3`: `research-required` (determination); handoff: [PLT-06].
- **Reference image decisions to review:** `ac-3`: `deployment-configured`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify the boot loader superuser account has been set with the following command:
+Verify the RHEL 9 boot loader superuser account has been set with the following command:

```

**Fix**

```diff
@@ -10,6 +10,6 @@

-Regenerate the GRUB configuration:
-$ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
+In RHEL 9.0, 9.1 and 9.2:
+sudo grub2-mkconfig -o /boot/grub2/grub.cfg

-Reboot the system:
-$ sudo reboot
+In RHEL 9.3 and later:
+sudo grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline
```

</details>

#### V-257792 — Changed

**RHEL 9 must disable virtual system calls.**

STIG ID: `RHEL-09-212035`. Severity: medium.
Rule ID: `SV-257792r1044842_rule` → `SV-257792r1268251_rule`.
CCI: CCI-001084.

- **Image criteria:** direct: None; shared-control review: [IMG-13].
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-3][cw-sc-3].
- **Baseline / control determinations:** `sc-3`: `host-inherited` (expectation); handoff: [PLT-07].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "System calls are "
+ "System calls are special routines in the Linux kernel, which userspace applications ask to do privileged tasks. Invoking a system call is an expensive operation because the processor must interrupt the currently executing task and switch context to kernel mode and then back to userspace after the system call completes. Virtual system calls map into user space a page that contains some variables and the implementation of some system calls. This allows the system calls System calls are "
- "be executed in userspace to alleviate the context switching expense.\n\nVirtual system"
+ "be executed in user space to alleviate the context-switching expense.\n\nVirtual system"
- "help to prevent return oriented programming (ROP) attacks via buffer overflows and overruns. If the system intends to run containers based on RHEL 6 components, then virtual system calls will need enabled so the components function properly.\n\nSatisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000134-GPOS-00068"
+ "help to prevent return-oriented programming attacks via buffer overflows and overruns.\n\nSatisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000134-GPOS-00068"
```

</details>

#### V-257797 — Changed

**RHEL 9 must restrict access to the kernel message buffer.**

STIG ID: `RHEL-09-213010`. Severity: medium.
Rule ID: `SV-257797r958514_rule` → `SV-257797r1262133_rule`.
CCI: CCI-001082, CCI-001090.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-2][cw-sc-2], [SC-4][cw-sc-4].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion); `sc-4`: `host-inherited` (determination); handoff: [PLT-02], [PLT-07].

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "acceptance/validation processes in DOD or other government"
+ "acceptance/validation processes in DoW or other government"
- "a nonprivileged user.\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069"
+ "a nonprivileged user.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069"
```

**Check**

```diff
@@ -1,7 +1,6 @@
-Verify RHEL 9 is configured to restrict access to the kernel message buffer with the following commands:
+Verify RHEL 9 is configured to restrict access to the kernel message buffer.

-Check the status of the kernel.dmesg_restrict kernel parameter.
+Check the status of the "kernel.dmesg_restrict" kernel parameter with the following command:

 $ sudo sysctl kernel.dmesg_restrict
-
 kernel.dmesg_restrict = 1
@@ -9,10 +8 @@
 If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.dmesg_restrict | tail
- -1
-
-kernel.dmesg_restrict = 1
-
-If "kernel.dmesg_restrict" is not set to "1" or is missing, this is a finding.
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a system configuration file, in the "/etc/sysctl.d/" directory:
+Create a drop-in if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-dmesg_restrict.conf
+
+Add the following to the file:
 kernel.dmesg_restrict = 1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257798 — Changed

**RHEL 9 must prevent kernel profiling by nonprivileged users.**

STIG ID: `RHEL-09-213015`. Severity: medium.
Rule ID: `SV-257798r1044849_rule` → `SV-257798r1262134_rule`.
CCI: CCI-001082, CCI-001090.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-2][cw-sc-2], [SC-4][cw-sc-4].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion); `sc-4`: `host-inherited` (determination); handoff: [PLT-02], [PLT-07].

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "acceptance/validation processes in DOD or other government"
+ "acceptance/validation processes in DoW or other government"
- "a nonprivileged user.\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069"
+ "a nonprivileged user.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000138-GPOS-00069"
```

**Check**

```diff
@@ -1,7 +1,6 @@
-Verify RHEL 9 is configured to prevent kernel profiling by nonprivileged users with the following commands:
+Verify RHEL 9 is configured to prevent kernel profiling by nonprivileged users.

-Check the status of the kernel.perf_event_paranoid kernel parameter.
+Check the status of the "kernel.perf_event_paranoid" kernel parameter.

-$ sysctl kernel.perf_event_paranoid
-
+$ sudo sysctl kernel.perf_event_paranoid
 kernel.perf_event_paranoid = 2
@@ -9,10 +8 @@
 If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config  | egrep -v '^(#|;)' | grep -F kernel.perf_event_paranoid
-| tail -1
-
-kernel.perf_event_paranoid = 2
-
-If "kernel.perf_event_paranoid" is not set to "2" or is missing, this is a finding.
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a system configuration file, in the "/etc/sysctl.d/" directory:
+Create a drop-in if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-kernel_perf_event_paranoid.conf
+
+Add the following to the file:
 kernel.perf_event_paranoid = 2

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257799 — Changed

**RHEL 9 must prevent the loading of a new kernel for later execution.**

STIG ID: `RHEL-09-213020`. Severity: medium.
Rule ID: `SV-257799r1044850_rule` → `SV-257799r1268251_rule`.
CCI: CCI-003992, CCI-001749.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].
- **CCI findings:** old: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3); candidate: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3).

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "unsigned kernel images.\n\nSatisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000366-GPOS-00153"
+ "unsigned kernel images.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000366-GPOS-00153"
```

**Check**

```diff
@@ -2,6 +2,5 @@

-Check the status of the kernel.kexec_load_disabled kernel parameter with the following command:
+Check the status of the "kernel.kexec_load_disabled" kernel parameter with the following command:

 $ sudo sysctl kernel.kexec_load_disabled
-
 kernel.kexec_load_disabled = 1
@@ -9,10 +8 @@
 If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter with the following command:
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.kexec_load_disabled |
- tail -1
-
-kernel.kexec_load_disabled = 1
-
-If "kernel.kexec_load_disabled" is not set to "1" or is missing, this is a finding.
```

**Fix**

```diff
@@ -1,6 +1,11 @@
-Add or edit the following line in a system configuration file in the "/etc/sysctl.d/" directory:
+Configure RHEL 9 to disable kernel image loading.

+Create a drop-in if it does not already exist:
+
+$ sudo vi /etc/sysctl.d/99-kernel_kexec_load_disabled.conf
+
+Add the following to the file:
 kernel.kexec_load_disabled = 1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257800 — Changed

**RHEL 9 must restrict exposed kernel pointer addresses access.**

STIG ID: `RHEL-09-213025`. Severity: medium.
Rule ID: `SV-257800r1044851_rule` → `SV-257800r1198253_rule`.
CCI: CCI-001082, CCI-002824.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-2][cw-sc-2], [SI-16][cw-si-16].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion); `si-16`: `host-inherited` (determination); handoff: [PLT-07].

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Exposing kernel pointers (through procfs or \"seq_printf()\") exposes kernel writeable structures, which may contain functions pointers. If a write vulnerability occurs in the kernel, allowing write access to any of this structure, the kernel can be compromised. This option disallows any program without the CAP_SYSLOG capability to get the addresses of kernel pointers by replacing them with \"0\".\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000433-GPOS-00192,"
+ "It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000433-GPOS-00192,"
```

**Check**

```diff
@@ -1,14 +1,8 @@
-Verify the runtime status of the kernel.kptr_restrict kernel parameter with the following command:
+Verify RHEL 9 is configured to restrict exposed kernel pointer address access.
+
+Verify the runtime status of the "kernel.kptr_restrict" kernel parameter with the following command:

 $ sudo sysctl kernel.kptr_restrict
-
 kernel.kptr_restrict = 1

-Verify the configuration of the kernel.kptr_restrict kernel parameter with the following command:
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F kernel.kptr_restrict | tail
- -1
-
-kernel.kptr_restrict =1
-
 If "kernel.kptr_restrict" is not set to "1" or is missing, this is a finding.
```

**Fix**

```diff
@@ -1,3 +1,8 @@
-Add or edit the following line in a system configuration file in the "/etc/sysctl.d/" directory:
+Configure RHEL 9 to restrict exposed kernel pointer addresses access.

+Create a drop-in if it does not already exist:
+
+$ sudo vi /etc/sysctl.d/99-kernel_kptr_restrict.conf
+
+Add the following to the file:
 kernel.kptr_restrict = 1
```

</details>

#### V-257801 — Changed

**RHEL 9 must enable kernel parameters to enforce discretionary access control (DAC) on hardlinks.**

STIG ID: `RHEL-09-213030`. Severity: medium.
Rule ID: `SV-257801r958702_rule` → `SV-257801r1155703_rule`.
CCI: CCI-002165, CCI-002235.

- **Image criteria:** direct: None; shared-control review: [IMG-11], [IMG-31].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-3(4)][cw-ac-3.4], [AC-6(10)][cw-ac-6.10].
- **Baseline / control determinations:** `ac-3.4`: absent from current control baseline; `ac-6.10`: `image-owned` (criterion); handoff: [PLT-02].

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "discretionary access control on hardlinks."
+ "discretionary access control (DAC) on hardlinks."
```

**Discussion**

```diff
- "By enabling the "
+ "DAC is based on the notion that individual users are \"owners\" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions.\n\nWhen discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.\n\nBy enabling the "
- "Disallowing such hardlinks mitigates vulnerabilities based on"
+ "Disallowing such hardlinks mitigate vulnerabilities based on"
- "open() or creat().\n\nSatisfies: SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125"
+ "open() or creat().\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124, SRG-OS-000324-GPOS-00125"
```

**Check**

```diff
@@ -2,6 +2,5 @@

-Check the status of the fs.protected_hardlinks kernel parameter with the following command:
+Check the status of the "fs.protected_hardlinks" kernel parameter with the following command:

 $ sudo sysctl fs.protected_hardlinks
-
 fs.protected_hardlinks = 1
@@ -9,10 +8 @@
 If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F fs.protected_hardlinks |
-tail -1
-
-fs.protected_hardlinks = 1
-
-If "fs.protected_hardlinks" is not set to "1" or is missing, this is a finding.
```

**Fix**

```diff
@@ -1,8 +1,11 @@
-Configure RHEL 9 to enable DAC on hardlinks with the following:
+Configure RHEL 9 to enable DAC on hardlinks.

-Add or edit the following line in a system configuration file in the "/etc/sysctl.d/" directory:
+Create a drop-in if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-fs_protected_hardlinks.conf
+
+Add the following to the file:
 fs.protected_hardlinks = 1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257802 — Changed

**RHEL 9 must enable kernel parameters to enforce discretionary access (DAC) control on symlinks.**

STIG ID: `RHEL-09-213035`. Severity: medium.
Rule ID: `SV-257802r958702_rule` → `SV-257802r1155706_rule`.
CCI: CCI-002165, CCI-002235.

- **Image criteria:** direct: None; shared-control review: [IMG-11], [IMG-31].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-3(4)][cw-ac-3.4], [AC-6(10)][cw-ac-6.10].
- **Baseline / control determinations:** `ac-3.4`: absent from current control baseline; `ac-6.10`: `image-owned` (criterion); handoff: [PLT-02].

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "enforce discretionary access control on symlinks."
+ "enforce discretionary access (DAC) control on symlinks."
```

**Discussion**

```diff
- "By enabling the "
+ "DAC is based on the notion that individual users are \"owners\" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions.\n\nWhen discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.\n\nBy enabling the "
- "or when the user identifier (UID) of the link"
+ "or when the UID of the link"
- "open() or creat().\n\nSatisfies: SRG-OS-000312-GPOS-00123, SRG-OS-000324-GPOS-00125"
+ "open() or creat().\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000312-GPOS-00122, SRG-OS-000312-GPOS-00123, SRG-OS-000312-GPOS-00124, SRG-OS-000324-GPOS-00125"
```

**Check**

```diff
@@ -2,15 +2,5 @@

-Check the status of the fs.protected_symlinks kernel parameter with the following command:
+Check the status of the "fs.protected_symlinks" kernel parameter with the following command:

 $ sudo sysctl fs.protected_symlinks
-
-fs.protected_symlinks = 1
-
-If "fs.protected_symlinks " is not set to "1" or is missing, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F fs.protected_symlinks | tail
- -1
-
 fs.protected_symlinks = 1
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a system configuration file in the "/etc/sysctl.d/" directory:
+Create a drop-in if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-fs_protected_symlinks.conf
+
+Add the following to the file:
 fs.protected_symlinks = 1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257803 — Changed

**RHEL 9 must disable the kernel.core_pattern.**

STIG ID: `RHEL-09-213040`. Severity: medium.
Rule ID: `SV-257803r991589_rule` → `SV-257803r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " to debug problems."
+ " to debug problems.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,19 +1,10 @@
-Verify RHEL 9 disables storing core dumps with the following commands:
+Verify RHEL 9 disables storing core dumps.
+
+Check the status of the "kernel.core_pattern" kernel parameter with the following command:

 $ sudo sysctl kernel.core_pattern
-
 kernel.core_pattern = |/bin/false

-If the returned line does not have a value of "|/bin/false", or a line is not returned and the need for core
-dumps is not documented with the information system security officer (ISSO) as an operational requirement,
-this is a finding.
-
-Check that the configuration files are present to disable core dump storage.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.core_pattern | tail
--1
-
-kernel.core_pattern = |/bin/false
-
-If "kernel.core_pattern" is not set to "|/bin/false" and is not documented with the ISSO as an operational
-requirement, or is missing, this is a finding.
+If "kernel.core_pattern" is not set to "|/bin/false", or a line is not returned and the need for core dumps is
+ not documented with the information system security officer (ISSO) as an operational requirement, this is a
+finding.
```

**Fix**

```diff
@@ -2,8 +2,10 @@

-Add or edit the following line in a system configuration file, in the "/etc/sysctl.d/" directory:
+Create a drop-in if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-kernel_core_pattern.conf
+
+Add the following to the file:
 kernel.core_pattern = |/bin/false

-The system configuration files need to be reloaded for the changes to take effect. To reload the contents of
-the files, run the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257809 — Changed

**RHEL 9 must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution.**

STIG ID: `RHEL-09-213070`. Severity: medium.
Rule ID: `SV-257809r1044866_rule` → `SV-257809r1208769_rule`.
CCI: CCI-002824.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SI-16][cw-si-16].
- **Baseline / control determinations:** `si-16`: `host-inherited` (determination); handoff: [PLT-07].

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Address space layout randomization (ASLR) makes it more difficult for an attacker to predict the location of attack code they have introduced into a process' address space during an attempt at exploitation. Additionally, ASLR makes it more difficult for an attacker to know the location of existing code in order to repurpose it using return oriented programming (ROP) techniques.\n\nSatisfies: SRG-OS-000433-GPOS-00193, SRG-OS-000480-GPOS-00227"
+ "Some adversaries launch attacks with the intent of executing code in nonexecutable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can be either hardware-enforced or software-enforced with hardware providing the greater strength of mechanism.\n\nExamples of attacks are buffer overflow attacks.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000433-GPOS-00193, SRG-OS-000480-GPOS-00227"
```

**Check**

```diff
@@ -1,15 +1,16 @@
-Verify RHEL 9 is implementing ASLR with the following command:
+Verify RHEL 9 is implementing ASLR.

 $ sudo sysctl kernel.randomize_va_space
-
 kernel.randomize_va_space = 2

+If "kernel.randomize_va_space" is not set to "2", this is a finding.
+
 Check that the configuration files are present to enable this kernel parameter.
-Verify the configuration of the kernel.kptr_restrict kernel parameter with the following command:

-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F kernel.randomize_va_space |
- tail -1
+$ sudo grep -rs kernel.randomize_va_space /run/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf
+/usr/lib/sysctl.d/*.conf /lib/sysctl.d/*.conf /etc/sysctl.conf /etc/sysctl.d/*.conf
+/etc/sysctl.d/99-kernel_randomize_va_space.conf:kernel.randomize_va_space = 2

-kernel.randomize_va_space = 2
+If "kernel.randomize_va_space" is not set to "2", or is missing or commented out, this is a finding.

-If "kernel.randomize_va_space" is not set to "2" or is missing, this is a finding.
+If conflicting results are returned, this is a finding.
```

**Fix**

```diff
@@ -1,6 +1,15 @@
-Add or edit the following line in a system configuration file in the "/etc/sysctl.d/" directory:
+Configure RHEL 9 to implement ASLR.

-kernel.randomize_va_space = 2
+$ echo 'kernel.randomize_va_space = 2' | sudo tee /etc/sysctl.d/99-kernel_randomize_va_space.conf

-Reload settings from all system configuration files with the following command:
+Remove any configurations that conflict with the above from the following locations:
+
+/run/sysctl.d/*.conf
+/usr/local/lib/sysctl.d/*.conf
+/usr/lib/sysctl.d/*.conf
+/lib/sysctl.d/*.conf
+/etc/sysctl.conf
+/etc/sysctl.d/*.conf
+
+Issue the following command to make the changes take effect:

```

</details>

#### V-257810 — Changed

**RHEL 9 must disable access to network bpf system call from nonprivileged processes.**

STIG ID: `RHEL-09-213075`. Severity: medium.
Rule ID: `SV-257810r1044869_rule` → `SV-257810r1198253_rule`.
CCI: CCI-001082.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-2][cw-sc-2].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion).

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Loading and accessing the packet filters programs and maps using the bpf() system call has the potential of revealing sensitive information about the kernel state.\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000480-GPOS-00227"
+ "It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000480-GPOS-00227"
```

**Check**

```diff
@@ -1,18 +1,8 @@
-Verify that RHEL 9 prevents privilege escalation through the kernel by disabling access to the bpf system call
- with the following commands:
+Verify RHEL 9 prevents privilege escalation through the kernel by disabling access to the bpf system call.
+
+Check the status of the "kernel.unprivileged_bpf_disabled" kernel parameter with the following command:

 $ sysctl kernel.unprivileged_bpf_disabled
-
 kernel.unprivileged_bpf_disabled = 1

-If the returned line does not have a value of "1", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-kernel.unprivileged_bpf_disabled | tail -1
-
-kernel.unprivileged_bpf_disabled = 1
-
-If the network parameter "kernel.unprivileged_bpf_disabled" is not equal to "1", or nothing is returned, this
-is a finding.
+If "kernel.unprivileged_bpf_disabled" is not set to "1", or is missing, this is a finding.
```

**Fix**

```diff
@@ -1,13 +1,13 @@
-Configure the currently loaded kernel parameter to the secure setting:
+Configure RHEL 9 to prevent privilege escalation through the kernel by disabling access to the bpf system
+call.

-$ sudo sysctl -w kernel.unprivileged_bpf_disabled=1
+Create the drop-in file if it does not already exist:

-Configure RHEL 9 to prevent privilege escalation through the kernel by disabling access to the bpf syscall by
-adding the following line to a file in the "/etc/sysctl.d" directory:
+$ sudo vi /etc/sysctl.d/99-kernel_unprivileged_bpf_disabled.conf

+Add the following line to the file:
 kernel.unprivileged_bpf_disabled = 1

-The system configuration files must be reloaded for the changes to take effect. To reload the contents of the
-files, run the following command:
+Reload settings from all system configuration files with the following command:

-$ sysctl --system
+$ sudo sysctl --system
```

</details>

#### V-257811 — Changed

**RHEL 9 must restrict usage of ptrace to descendant processes.**

STIG ID: `RHEL-09-213080`. Severity: medium.
Rule ID: `SV-257811r1044872_rule` → `SV-257811r1198253_rule`.
CCI: CCI-001082.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-2][cw-sc-2].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion).

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Unrestricted usage of ptrace allows compromised binaries to run ptrace on other processes of the user. Like this, the attacker can steal sensitive information from the target processes (e.g., SSH sessions, web browser, etc.) without any additional assistance from the user (i.e., without resorting to phishing).\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000480-GPOS-00227"
+ "It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000132-GPOS-00067, SRG-OS-000480-GPOS-00227"
```

**Check**

```diff
@@ -1,14 +1,6 @@
-Verify RHEL 9 restricts the usage of ptrace to descendant processes with the following commands:
+Verify RHEL 9 restricts the usage of ptrace to descendant processes.
+
+Check the status of the "kernel.yama.ptrace_scope" kernel parameter with the following command:

 $ sysctl kernel.yama.ptrace_scope
-
-kernel.yama.ptrace_scope = 1
-
-If the returned line does not have a value of "1", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F kernel.yama.ptrace_scope|
-tail -1
-
 kernel.yama.ptrace_scope = 1
```

**Fix**

```diff
@@ -1,13 +1,12 @@
-Configure the currently loaded kernel parameter to the secure setting:
+Configure RHEL 9 to restrict the usage of ptrace to descendant processes.

-$ sudo sysctl -w kernel.yama.ptrace_scope=1
+Create the drop-in if it doesn't already exist:

-Configure RHEL 9 to restrict usage of ptrace to descendant processes by adding the following line to a file in
- the "/etc/sysctl.d" directory:
+$ sudo vi /etc/sysctl.d/99-kernel_yama.ptrace_scope.conf

+Add the following line to the file:
 kernel.yama.ptrace_scope = 1

-The system configuration files must be reloaded for the changes to take effect. To reload the contents of the
-files, run the following command:
+Reload settings from all system configuration files with the following command:

-$ sysctl --system
+$ sudo sysctl --system
```

</details>

#### V-257812 — Changed

**RHEL 9 must disable core dump backtraces.**

STIG ID: `RHEL-09-213085`. Severity: medium.
Rule ID: `SV-257812r1051005_rule` → `SV-257812r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,3 @@
+Note: If kernel dumps are disabled in accordance with RHEL-09-213040, this requirement is not applicable.
+
 Verify RHEL 9 disables core dump backtraces by issuing the following command:
```

</details>

#### V-257813 — Changed

**RHEL 9 must disable storing core dumps.**

STIG ID: `RHEL-09-213090`. Severity: medium.
Rule ID: `SV-257813r991589_rule` → `SV-257813r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,3 @@
+Note: If kernel dumps are disabled in accordance with RHEL-09-213040, this requirement is not applicable.
+
 Verify RHEL 9 disables storing core dumps for all users by issuing the following command:
@@ -6,4 +8,4 @@

-If the "Storage" item is missing, commented out, or the value is anything other than "none" and the need for
-core dumps is not documented with the information system security officer (ISSO) as an operational requirement
- for all domains that have the "core" item assigned, this is a finding.
+If the "Storage" item is missing or commented out, or the value is anything other than "none", and the need
+for core dumps is not documented with the information system security officer (ISSO) as an operational
+requirement for all domains that have the "core" item assigned, this is a finding.
```

</details>

#### V-257814 — Changed

**RHEL 9 must disable core dumps for all users.**

STIG ID: `RHEL-09-213095`. Severity: medium.
Rule ID: `SV-257814r991589_rule` → `SV-257814r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,4 +1,6 @@
+Note: If kernel dumps are disabled in accordance with RHEL-09-213040, this requirement is not applicable.
+
 Verify RHEL 9 disables core dumps for all users by issuing the following command:

-$ grep -r -s core /etc/security/limits.conf /etc/security/limits.d/*.conf
+$ grep -rs core /etc/security/limits.conf /etc/security/limits.d/*.conf

@@ -8,4 +10,6 @@

-If the "core" item is missing, commented out, or the value is anything other than "0" and the need for core
-dumps is not documented with the information system security officer (ISSO) as an operational requirement for
-all domains that have the "core" item assigned, this is a finding.
+If the "core" item is missing or commented out, or the value is anything other than "0", and the need for core
+ dumps is not documented with the information system security officer (ISSO) as an operational requirement for
+ all domains that have the "core" item assigned, this is a finding.
+
+If entries exist for users or groups with a value set to anything other than "0", this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the operating system to disable core dumps for all users.
+Configure RHEL 9 to disable core dumps for all users.

@@ -6 +6,3 @@
 * hard core 0
+
+Remove or comment out any entries for users or groups with a value set to anything other than "0".
```

</details>

#### V-257815 — Changed

**RHEL 9 must disable acquiring, saving, and processing core dumps.**

STIG ID: `RHEL-09-213100`. Severity: medium.
Rule ID: `SV-257815r991589_rule` → `SV-257815r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,3 @@
+Note: If kernel dumps are disabled in accordance with RHEL-09-213040, this requirement is not applicable.
+
 Verify RHEL 9 is not configured to acquire, save, or process core dumps with the following command:
@@ -8,3 +10,3 @@

-If the "systemd-coredump.socket" is loaded and not masked and the need for core dumps is not documented with
+If the "systemd-coredump.socket" is loaded and not masked, and the need for core dumps is not documented with
 the information system security officer (ISSO) as an operational requirement, this is a finding.
```

</details>

#### V-257816 — Changed

**RHEL 9 must disable the use of user namespaces.**

STIG ID: `RHEL-09-213105`. Severity: medium.
Rule ID: `SV-257816r1014825_rule` → `SV-257816r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "User namespaces are used primarily for Linux containers. The value \"0\" disallows the use of user namespaces."
+ "It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore, may remain unsecured. They increase the risk to the platform by providing additional attack vectors.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,2 +1,4 @@
-Verify RHEL 9 disables the use of user namespaces with the following commands:
+Verify RHEL 9 disables the use of user namespaces.
+
+Check the status of the "user.max_user_namespaces" parameter with the following command:

@@ -6,14 +8,5 @@

-If the returned line does not have a value of "0", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F user.max_user_namespaces |
-tail -1
-user.max_user_namespaces = 0
-
-If the network parameter "user.max_user_namespaces" is not equal to "0", or nothing is returned, this is a
-finding.
+If "user.max_user_namespaces" is not set to "0" or is missing, this is a finding.

 If the use of namespaces is operationally required and documented with the information system security manager
- (ISSM), this is not a finding.
+ (ISSM), it is not a finding.
```

**Fix**

```diff
@@ -1,3 +1,8 @@
-Configure RHEL 9 to disable the use of user namespaces by adding the following line to a file, in the
-"/etc/sysctl.d" directory:
+Configure RHEL 9 to disable the use of user namespaces.
+
+Create the drop-in if it does not already exist:
+
+$ sudo vi /etc/sysctl.d/99-user_max_user_namespaces.conf
+
+Add the following line to the file:

@@ -5,4 +10,3 @@

-The system configuration files need to be reloaded for the changes to take effect. To reload the contents of
-the files, run the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257820 — Changed

**RHEL 9 must check the GPG signature of software packages originating from external software repositories before installation.**

STIG ID: `RHEL-09-214015`. Severity: high.
Rule ID: `SV-257820r1044878_rule` → `SV-257820r1286923_rule`.
CCI: CCI-003992, CCI-001749.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].
- **CCI findings:** old: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3); candidate: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,11 +1,11 @@
-Verify that dnf always checks the GPG signature of software packages originating from external software
-repositories before installation:
+Verify RHEL 9 dnf always checks the GPG signature of software packages originating from external software
+repositories before installation with the following command:

-$ grep -w gpgcheck /etc/dnf/dnf.conf
-
+$ sudo grep -w gpgcheck /etc/dnf/dnf.conf
 gpgcheck=1

-If "gpgcheck" is not set to "1", or if the option is missing or commented out, ask the system administrator
-how the GPG signatures of software packages are being verified.
+If "gpgcheck" is not set to either "1", "true", or "yes" (keywords containing letters are case insensitive),
+or if the option is missing or commented out, ask the system administrator (SA) how the GPG signatures of
+software packages are being verified.

-If there is no process to verify GPG signatures that is approved by the organization, this is a finding.
+If no process to verify GPG signatures has been approved by the organization, this is a finding.
```

**Fix**

```diff
@@ -1,6 +1,9 @@
-Configure dnf to always check the GPG signature of software packages originating from external software
-repositories before installation.
+Configure RHEL 9 dnf to always check the GPG signature of software packages originating from external software
+ repositories before installation.

-Add or update the following line in the [main] section of the /etc/dnf/dnf.conf file:
+Add or update the following line in the [main] section of the "/etc/dnf/dnf.conf" file:

 gpgcheck=1
+
+Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case
+insensitive).
```

</details>

#### V-257821 — Changed

**RHEL 9 must check the GPG signature of locally installed software packages before installation.**

STIG ID: `RHEL-09-214020`. Severity: high.
Rule ID: `SV-257821r1015077_rule` → `SV-257821r1286926_rule`.
CCI: CCI-003992, CCI-001749.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].
- **CCI findings:** old: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3); candidate: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,10 +1,11 @@
-Verify that dnf always checks the GPG signature of locally installed software packages before installation:
+Verify RHEL 9 dnf always checks the GPG signature of locally installed software packages before installation
+with the following command:

-$ grep localpkg_gpgcheck /etc/dnf/dnf.conf
-
+$ sudo grep localpkg_gpgcheck /etc/dnf/dnf.conf
 localpkg_gpgcheck=1

-If "localpkg_gpgcheck" is not set to "1", or if the option is missing or commented out, ask the system
-administrator how the GPG signatures of local software packages are being verified.
+If "localpkg_gpgcheck" is not set to either "1", "true", or "yes" (keywords containing letters are case
+insensitive), or if the option is missing or commented out, ask the system administrator how the GPG
+signatures of local software packages are being verified.

-If there is no process to verify GPG signatures that is approved by the organization, this is a finding.
+If no process to verify GPG signatures has been approved by the organization, this is a finding.
```

**Fix**

```diff
@@ -1,5 +1,8 @@
-Configure dnf to always check the GPG signature of local software packages before installation.
+Configure RHEL 9 dnf to always check the GPG signature of local software packages before installation.

-Add or update the following line in the [main] section of the /etc/dnf/dnf.conf file:
+Add or update the following line in the [main] section of the "/etc/dnf/dnf.conf" file:

 localpkg_gpgcheck=1
+
+Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case
+insensitive).
```

</details>

#### V-257822 — Changed

**RHEL 9 must have GPG signature verification enabled for all software repositories.**

STIG ID: `RHEL-09-214025`. Severity: high.
Rule ID: `SV-257822r1044880_rule` → `SV-257822r1286929_rule`.
CCI: CCI-003992, CCI-001749.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].
- **CCI findings:** old: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3); candidate: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,8 +1,11 @@
-Verify that all software repositories defined in "/etc/yum.repos.d/" have been configured with "gpgcheck"
-enabled:
+Verify RHEL 9 software repositories defined in "/etc/yum.repos.d/" have been configured with "gpgcheck"
+enabled with the following command:

-$ grep -w gpgcheck /etc/yum.repos.d/*.repo | more
-
+$ sudo grep -w gpgcheck /etc/yum.repos.d/*.repo | more
 gpgcheck = 1

-If "gpgcheck" is not set to "1" for all returned lines, this is a finding.
+If "gpgcheck" for software packages and repositories is not set to either "1", "true", or "yes" (keywords
+containing letters are case insensitive), or if the option is missing or commented out, ask the system
+administrator how the GPG signatures of local software packages are being verified.
+
+If no process to verify GPG signatures has been approved by the organization, this is a finding.
```

**Fix**

```diff
@@ -1,3 +1,7 @@
-Configure all software repositories defined in "/etc/yum.repos.d/" to have "gpgcheck" enabled:
+Configure RHEL 9 software repositories defined in "/etc/yum.repos.d/" to have "gpgcheck" enabled with the
+following command:

 $ sudo sed -i 's/gpgcheck\s*=.*/gpgcheck=1/g' /etc/yum.repos.d/*
+
+Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case
+insensitive).
```

</details>

#### V-257823 — Changed

**RHEL 9 must be configured so that the cryptographic hashes of system files match vendor values.**

STIG ID: `RHEL-09-214030`. Severity: medium.
Rule ID: `SV-257823r1051231_rule` → `SV-257823r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " on the system."
+ " on the system.\nIf the Check Text command returns results from third-party software vendors, it is an indication that the vendor is not implementing their rpm packages correctly and this must be corrected by the software vendor."
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify that RHEL 9 is configured so that the cryptographic hashes of system files match vendor values.
+Verify RHEL 9 is configured so that the cryptographic hashes of system files match vendor values.

```

</details>

#### V-257824 — Changed

**RHEL 9 must remove all software components after updated versions have been installed.**

STIG ID: `RHEL-09-214035`. Severity: low.
Rule ID: `SV-257824r1044886_rule` → `SV-257824r1286932_rule`.
CCI: CCI-002617.

- **Image criteria:** direct: None; shared-control review: [IMG-25].
- **Crosswalk:** Prospective only; no accepted rule entry; [SI-2(6)][cw-si-2.6].
- **Baseline / control determinations:** `si-2.6`: `image-owned` (criterion); handoff: [PLT-08].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -3,6 +3,6 @@

-$ grep -i clean_requirements_on_remove /etc/dnf/dnf.conf
-
+$ sudo grep -i clean_requirements_on_remove /etc/dnf/dnf.conf
 clean_requirements_on_remove=True

-If "clean_requirements_on_remove" is not set to "True", this is a finding.
+If "clean_requirements_on_remove" is not set to either "1", "true", or "yes" (keywords containing letters are
+case insensitive), this is a finding.
```

**Fix**

```diff
@@ -2,4 +2,7 @@

-Edit the file /etc/dnf/dnf.conf by adding or editing the following line:
+Edit the file "/etc/dnf/dnf.conf" by adding or editing the following line:

  clean_requirements_on_remove=True
+
+Note: Any of the following are acceptable: "1", "true", or "yes" (keywords containing letters are case
+insensitive).
```

</details>

#### V-257825 — Changed

**RHEL 9 subscription-manager package must be installed.**

STIG ID: `RHEL-09-215010`. Severity: medium.
Rule ID: `SV-257825r1044888_rule` → `SV-257825r1268241_rule`.
CCI: CCI-003992, CCI-001749.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].
- **CCI findings:** old: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3); candidate: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3).

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,3 @@
+Note: If the system is not an internet connected system, this requirement is not applicable.
+
 Verify that RHEL 9 subscription-manager package is installed with the following command:
```

</details>

#### V-257826 — Changed

**RHEL 9 must not have a File Transfer Protocol (FTP) server package installed.**

STIG ID: `RHEL-09-215015`. Severity: high.
Rule ID: `SV-257826r1044890_rule` → `SV-257826r1208770_rule`.
CCI: CCI-000197, CCI-000381.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7][cw-cm-7], [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16]; `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "of accidental activation.\n\nSatisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000095-GPOS-00049, "
+ "of accidental activation.\n\nIf FTP is required for operational support (such as transmission of router configurations), its use must be documented with the information systems security manager (ISSM), restricted to only authorized personnel, and have access control rules established.\n\nSatisfies: SRG-OS-000074-GPOS-00042, SRG-OS-000095-GPOS-00049, "
```

**Check**

```diff
@@ -1,8 +1,5 @@
-Verify that RHEL 9 does not have a File Transfer Protocol (FTP) server package installed with the following
-command:
+Verify RHEL 9 does not have an FTP server package installed with the following command:

-$ rpm -q vsftpd
+$ sudo dnf list --installed | grep vsftpd

-package vsftpd is not installed
-
-If the "ftp" package is installed, this is a finding.
+If the "vsftpd" package is installed, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-The ftp package can be removed with the following command (using vsftpd as an example):
+Remove the vsftpd package with the following command:

```

</details>

#### V-257830 — Changed

**RHEL 9 must not install packages from the Extra Packages for Enterprise Linux (EPEL) repository.**

STIG ID: `RHEL-09-215035`. Severity: medium.
Rule ID: `SV-257830r958478_rule` → `SV-257830r1134906_rule`.
CCI: CCI-000381.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7][cw-cm-7].
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "9 must not have the rsh-server package installed."
+ "9 must not install packages from the Extra Packages for Enterprise Linux (EPEL) repository."
```

**Discussion**

```diff
- "The \"rsh-server\" service provides unencrypted remote access service, which does not provide for the confidentiality and integrity of user passwords or the remote session and has very weak authentication. If a privileged user were to login using this service, the privileged user password could be compromised. The \"rsh-server\" package provides several obsolete and insecure network services. Removing it decreases the risk of accidental (or intentional) activation of those services."
+ "The EPEL is a repository of high-quality open-source packages for enterprise-class Linux distributions such as RHEL, CentOS, AlmaLinux, Rocky Linux, and Oracle Linux. These packages are not part of the official distribution but are built using the same Fedora build system to ensure compatibility and maintain quality standards."
```

**Check**

```diff
@@ -1,7 +1,7 @@
-Verify that the rsh-server package is not installed with the following command:
+Verify that RHEL 9 is not able to install packages from the EPEL with the following command:

-$ sudo dnf list --installed rsh-server
+$ dnf repolist
+rhel-9-for-x86_64-appstream-rpms                Red Hat Enterprise Linux 9 for x86_64 - AppStream (RPMs)
+rhel-9-for-x86_64-baseos-rpms                   Red Hat Enterprise Linux 9 for x86_64 - BaseOS (RPMs)

-Error: No matching Packages to list
-
-If the "rsh-server" package is installed, this is a finding.
+If any repositories containing the word "epel" in the name exist, this is a finding.
```

**Fix**

```diff
@@ -1,3 +1,7 @@
-Remove the rsh-server package with the following command:
+The repo package can be manually removed with the following command:

-$ sudo dnf remove rsh-server
+$ sudo dnf remove epel-release
+
+Configure the operating system to disable use of the EPEL repository with the following command:
+
+$ sudo dnf config-manager --set-disabled epel
```

</details>

#### V-257832 — Changed

**RHEL 9 must not have the gssproxy package installed.**

STIG ID: `RHEL-09-215045`. Severity: medium.
Rule ID: `SV-257832r1044900_rule` → `SV-257832r1155653_rule`.
CCI: CCI-000381.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7][cw-cm-7].
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,4 @@
-Verify that the gssproxy package is not installed with the following command:
+Note: If NFS mounts are authorized and in use on the system, this control is not applicable.
+
+Verify the gssproxy package is not installed with the following command:

```

</details>

#### V-257835 — Changed

**The Trivial File Transfer Protocol (TFTP) server must not be installed unless it is required, and if required, the RHEL 9 TFTP daemon must be configured to operate in secure mode.**

STIG ID: `RHEL-09-215060`. Severity: high.
Rule ID: `SV-257835r1069368_rule` → `SV-257835r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "RHEL 9 must not have a Trivial File Transfer"
+ "The Trivial File Transfer"
- "Protocol (TFTP) server package installed."
+ "Protocol (TFTP) server must not be installed unless it is required, and if required, the RHEL 9 TFTP daemon must be configured to operate in secure mode."
```

**Discussion**

```diff
- " control rules established."
+ " control rules established.\n\nRestricting TFTP to a specific directory prevents remote users from copying, transferring, or overwriting system files."
```

**Check**

```diff
@@ -1,7 +1,22 @@
-Verify that RHEL 9 does not have a "tftp-server" package installed with the following command:
+Verify if TFTP is installed, it is configured to operate in secure mode.

-$ dnf list --installed tftp-server
+Note: If TFTP is not required, it must not be installed. If TFTP is not installed, this rule is not
+applicable.

-Error: No matching Packages to list
+Check to see if TFTP server is installed with the following command:

-If the "tftp-server" package is installed, this is a finding.
+$ sudo dnf list --installed tftp-server
+
+Updating Subscription Management repositories.
+Installed Packages
+tftp-server.x86_64                             5.2-38.el9
+@rhel-9-for-x86_64-appstream-rpms
+
+Verify the TFTP daemon, if tftp.server is installed, is configured to operate in secure mode with the
+following command:
+
+$ grep -i execstart /usr/lib/systemd/system/tftp.service
+ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot
+
+Note: The "-s" option ensures the TFTP server only serves files from the specified directory, which is a
+security measure to prevent unauthorized access to other parts of the file system.
```

**Fix**

```diff
@@ -1,3 +1,18 @@
-The "tftp-server" package can be removed with the following command:
+Configure RHEL 9 so that TFTP operates in secure mode if installed.

-$ sudo dnf remove tftp-server
+If TFTP server is not required, remove it with the following command:
+$ sudo dnf -y remove tftp-server
+
+Configure the TFTP daemon to operate in secure mode with the following command:
+$ sudo systemctl edit tftp.service
+
+In the editor, enter:
+[Service]
+ExecStart=/usr/sbin/in.tftpd -s /var/lib/tftpboot
+
+After making changes, reload the systemd daemon and restart the TFTP service as follows:
+
+$ sudo systemctl daemon-reload
+$ sudo systemctl restart tftp.service
+
+If the "-s" option is not present in the "ExecStart" line or if the line is missing, this is a finding.
```

</details>

#### V-257838 — Changed

**RHEL 9 must have the openssl-pkcs11 package installed.**

STIG ID: `RHEL-09-215075`. Severity: medium.
Rule ID: `SV-257838r1044912_rule` → `SV-257838r1268228_rule`.
CCI: CCI-000765, CCI-004046, CCI-001953, CCI-001954, CCI-001948.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2(1)][cw-ia-2.1], [IA-2(6)][cw-ia-2.6], [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.1`: `research-required` (determination); handoff: [PLT-13]; `ia-2.12`: `research-required` (undetermined); `ia-2.6`: absent from current control baseline.
- **Reference image decisions to review:** `ia-2.1`: `not-applicable`; `ia-2.12`: `not-applicable`.
- **CCI findings:** old: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11); candidate: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "privileged user. The DOD common access card (CAC) with DOD-approved PKI is an"
+ "privileged user. The DoW common access card (CAC) with DoW-approved PKI is an"
```

</details>

#### V-257849 — Changed

**The RHEL 9 file system automounter must be disabled.**

STIG ID: `RHEL-09-231040`. Severity: medium.
Rule ID: `SV-257849r1044928_rule` → `SV-257849r1262109_rule`.
CCI: CCI-000778, CCI-001958.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-3][cw-ia-3].
- **Baseline / control determinations:** `ia-3`: `host-inherited` (expectation); handoff: [PLT-15].

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "RHEL 9 file system automount function must be disabled unless required."
+ "The RHEL 9 file system automounter must be disabled."
```

**Discussion**

```diff
- "An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message.\n\nSatisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163, SRG-OS-000480-GPOS-00227"
+ "Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity.\n\nPeripherals include, but are not limited to, devices such as flash drives, external storage, and printers.\n\nSatisfies: SRG-OS-000114-GPOS-00059, SRG-OS-000378-GPOS-00163"
```

**Check**

```diff
@@ -1,11 +1,6 @@
-Note: If the autofs service is not installed, this requirement is Not Applicable.
+Verify that RHEL 9 file system automount function has been disabled and masked with the following command:

-Verify that the RHEL 9 file system automount function has been disabled with the following command:
-
-$ systemctl is-enabled  autofs
-
+$ $ systemctl is-enabled  autofs
 masked

-If the returned value is not "masked", "disabled", or "Failed to get unit file state for autofs.service for
-autofs" and is not documented as an operational requirement with the information system security officer
-(ISSO), this is a finding.
+If the returned value is not "masked", "disabled", or "not-found", this is a finding.
```

**Fix**

```diff
@@ -1,4 +1,4 @@
-Configure RHEL 9 to disable the ability to automount devices.
+Configure RHEL 9 to disable and mask the ability to automount devices.

-The autofs service can be disabled with the following command:
+The "autofs" service can be disabled with the following command:

```

</details>

#### V-257862 — Changed

**RHEL 9 must prevent files with the setuid and setgid bit set from being executed on the /boot/efi directory.**

STIG ID: `RHEL-09-231105`. Severity: medium.
Rule ID: `SV-257862r1051265_rule` → `SV-257862r1184295_rule`.
CCI: CCI-001764.

- **Image criteria:** direct: None; shared-control review: [IMG-07], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7(2)][cw-cm-7.2].
- **Baseline / control determinations:** `cm-7.2`: `host-inherited` (determination); handoff: [PLT-01], [PLT-16].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,2 @@
-Note: For systems that use BIOS, this requirement is Not Applicable.
+Note: For systems that use BIOS, this is not applicable.

@@ -10 +10,3 @@
 If the /boot/efi file system does not have the "nosuid" option set, this is a finding.
+
+Note: This control is not applicable to vfat file systems.
```

</details>

#### V-257863 — Changed

**RHEL 9 must mount /dev/shm with the nodev option.**

STIG ID: `RHEL-09-231110`. Severity: medium.
Rule ID: `SV-257863r958804_rule` → `SV-257863r1155633_rule`.
CCI: CCI-001764.

- **Image criteria:** direct: None; shared-control review: [IMG-07], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7(2)][cw-cm-7.2].
- **Baseline / control determinations:** `cm-7.2`: `host-inherited` (determination); handoff: [PLT-01], [PLT-16].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,6 +2,7 @@

-$ mount | grep /dev/shm
+$ findmnt /dev/shm

-tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel)
+TARGET   SOURCE FSTYPE OPTIONS
+/dev/shm tmpfs  tmpfs  rw,nodev,nosuid,noexec,seclabel

-If the /dev/shm file system is mounted without the "nodev" option, this is a finding.
+If the mount options for /dev/shm does not include nodev, this is a finding.
```

**Fix**

```diff
@@ -1 +1,12 @@
+Configure "/dev/shm" to mount with the "nodev" option.
+
 Modify "/etc/fstab" to use the "nodev" option on the "/dev/shm" file system.
+
+To reload all implicit mount units and update the dependency graph so that new options will apply correctly at
+ next remount, run the following command:
+
+$ sudo systemctl daemon-reload
+
+Use the following command to apply the changes immediately without a reboot:
+
+$ sudo mount -o remount /dev/shm
```

</details>

#### V-257864 — Changed

**RHEL 9 must mount /dev/shm with the noexec option.**

STIG ID: `RHEL-09-231115`. Severity: medium.
Rule ID: `SV-257864r958804_rule` → `SV-257864r1155639_rule`.
CCI: CCI-001764.

- **Image criteria:** direct: None; shared-control review: [IMG-07], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7(2)][cw-cm-7.2].
- **Baseline / control determinations:** `cm-7.2`: `host-inherited` (determination); handoff: [PLT-01], [PLT-16].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,6 +2,6 @@

-$ mount | grep /dev/shm
+$ findmnt /dev/shm

-tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel)
+/dev/shm tmpfs  tmpfs  rw,nodev,nosuid,noexec,seclabel

-If the /dev/shm file system is mounted without the "noexec" option, this is a finding.
+If the mount options for /dev/shm does not include noexec, this is a finding.
```

**Fix**

```diff
@@ -1 +1,12 @@
+Configure "/dev/shm" to mount with the "noexec" option.
+
 Modify "/etc/fstab" to use the "noexec" option on the "/dev/shm" file system.
+
+To reload all implicit mount units and update the dependency graph so that new options will apply correctly at
+ next remount, run the following command:
+
+$ sudo systemctl daemon-reload
+
+Use the following command to apply the changes immediately without a reboot:
+
+$ sudo mount -o remount /dev/shm
```

</details>

#### V-257865 — Changed

**RHEL 9 must mount /dev/shm with the nosuid option.**

STIG ID: `RHEL-09-231120`. Severity: medium.
Rule ID: `SV-257865r1044946_rule` → `SV-257865r1184297_rule`.
CCI: CCI-001764.

- **Image criteria:** direct: None; shared-control review: [IMG-07], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7(2)][cw-cm-7.2].
- **Baseline / control determinations:** `cm-7.2`: `host-inherited` (determination); handoff: [PLT-01], [PLT-16].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,6 +2,5 @@

-$ mount | grep /dev/shm
+$ findmnt /dev/shm
+/dev/shm tmpfs  tmpfs  rw,nodev,nosuid,noexec,seclabel

-tmpfs on /dev/shm type tmpfs (rw,nodev,nosuid,noexec,seclabel)
-
-If the /dev/shm file system is mounted without the "nosuid" option, this is a finding.
+If the mount options for /dev/shm does not include nosuid, this is a finding.
```

**Fix**

```diff
@@ -1 +1,12 @@
+Configure "/dev/shm" to mount with the "nosuid" option.
+
 Modify "/etc/fstab" to use the "nosuid" option on the "/dev/shm" file system.
+
+To reload all implicit mount units and update the dependency graph so that new options will apply correctly at
+ next remount, run the following command:
+
+$ sudo systemctl daemon-reload
+
+Use the following command to apply the changes immediately without a reboot:
+
+$ sudo mount -o remount /dev/shm
```

</details>

#### V-257881 — Changed

**RHEL 9 must prevent special devices on non-root local partitions.**

STIG ID: `RHEL-09-231200`. Severity: medium.
Rule ID: `SV-257881r991589_rule` → `SV-257881r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify all non-root local partitions are mounted with the "nodev" option with the following command:
+Verify all nonroot local partitions are mounted with the "nodev" option with the following command:

```

</details>

#### V-257884 — Changed

**RHEL 9 library files must have mode 755 or less permissive.**

STIG ID: `RHEL-09-232020`. Severity: medium.
Rule ID: `SV-257884r991560_rule` → `SV-257884r1106306_rule`.
CCI: CCI-001499.

- **Image criteria:** direct: None; shared-control review: [IMG-10], [IMG-15].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-5(6)][cw-cm-5.6].
- **Baseline / control determinations:** `cm-5.6`: `image-owned` (criterion); handoff: [PLT-03], [PLT-12].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,6 +1,8 @@
-Verify the system-wide shared library files contained in the following directories have mode "755" or less
-permissive with the following command:
+Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and
+"/usr/lib64" have mode 0755 or less permissive.

-$ sudo find -L /lib /lib64 /usr/lib /usr/lib64 -perm /022 -type f -exec ls -l {} \;
+Check that the systemwide shared library files have mode 0755 or less permissive with the following command:

-If any system-wide shared library file is found to be group-writable or world-writable, this is a finding.
+$ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec stat -c "%n %a" {} +
+
+If any output is returned, this is a finding.
```

**Fix**

```diff
@@ -1,4 +1,4 @@
-Configure the library files to be protected from unauthorized access. Run the following command, replacing
-"[FILE]" with any library file with a mode more permissive than 755.
+Configure the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and
+"/usr/lib64" to have mode 0755 or less permissive with the following command.

-$ sudo chmod 755 [FILE]
+$ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' -perm /022 -exec chmod go-w {} +
```

</details>

#### V-257889 — Changed

**All RHEL 9 local initialization files must have mode 0740 or less permissive.**

STIG ID: `RHEL-09-232045`. Severity: medium.
Rule ID: `SV-257889r1044959_rule` → `SV-257889r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,9 +1,8 @@
-Verify that all local initialization files have a mode of "0740" or less permissive with the following
-command:
+Verify all local initialization files have a mode of "0740" or less permissive with the following command:

-Note: The example will be for the "bingwa" user, who has a home directory of "/home/bingwa".
+Note: The example will be for the "disauser" user, who has a home directory of "/home/disauser".

-$ find /home/bingwa/.[^.]* -maxdepth 0 -perm -740 -exec stat -c "%a %n" {} \; | more
+$ sudo find /home /root -maxdepth 2 -type f -name ".*" -perm /037 -ls

-755 /home/bingwa/.somepermissivefile
+755 /home/disauser/.somepermissivefile

```

**Fix**

```diff
@@ -2,4 +2,4 @@

-Note: The example will be for the wadea user, who has a home directory of "/home/wadea".
+Note: The example will be for the disauser user, who has a home directory of "/home/disauser".

-$ sudo chmod 0740 /home/wadea/.<INIT_FILE>
+$ sudo chmod 0740 /home/disauser/.<INIT_FILE>
```

</details>

#### V-257890 — Changed

**All RHEL 9 local interactive user home directories must have mode 0750 or less permissive.**

STIG ID: `RHEL-09-232050`. Severity: medium.
Rule ID: `SV-257890r1044961_rule` → `SV-257890r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -8,3 +8,3 @@

-700 /home/bingwa
+700 /home/disauser

```

**Fix**

```diff
@@ -1,6 +1,5 @@
-Change the mode of interactive user's home directories to "0750". To change the mode of a local interactive
-user's home directory, use the following command:
+Change the mode of interactive user's home directories to "0750" using the following command:

-Note: The example will be for the user "wadea".
+Note: The example will be for the user "disauser".

-$ sudo chmod 0750 /home/wadea
+$ sudo chmod 0750 /home/disauser
```

</details>

#### V-257916 — Changed

**RHEL 9 /var/log/messages file must be owned by root.**

STIG ID: `RHEL-09-232180`. Severity: medium.
Rule ID: `SV-257916r1044973_rule` → `SV-257916r1101916_rule`.
CCI: CCI-001314.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SI-11][cw-si-11].
- **Baseline / control determinations:** `si-11`: `research-required` (undetermined).
- **Reference image decisions to review:** `si-11`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,3 +4,3 @@

-root /var/log
+root /var/log/messages

```

</details>

#### V-257917 — Changed

**RHEL 9 /var/log/messages file must be group-owned by root.**

STIG ID: `RHEL-09-232185`. Severity: medium.
Rule ID: `SV-257917r1044975_rule` → `SV-257917r1101914_rule`.
CCI: CCI-001314.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SI-11][cw-si-11].
- **Baseline / control determinations:** `si-11`: `research-required` (undetermined).
- **Reference image decisions to review:** `si-11`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,3 +4,3 @@

-root /var/log
+root /var/log/messages

```

</details>

#### V-257920 — Changed

**RHEL 9 library files must be owned by root.**

STIG ID: `RHEL-09-232200`. Severity: medium.
Rule ID: `SV-257920r1069385_rule` → `SV-257920r1101926_rule`.
CCI: CCI-001499.

- **Image criteria:** direct: None; shared-control review: [IMG-10], [IMG-15].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-5(6)][cw-cm-5.6].
- **Baseline / control determinations:** `cm-5.6`: `image-owned` (criterion); handoff: [PLT-03], [PLT-12].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,5 +1,6 @@
-Verify the systemwide shared library files are owned by "root" with the following command:
+Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and
+"/usr/lib64" are owned by root with the following command:

-$ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -user root ! -type d -exec stat -L -c "%U %n" {} \;
+$ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec stat -c "%n %U" {} +

-If any systemwide shared library file is not owned by root, this is a finding.
+If any output is returned, this is a finding.
```

**Fix**

```diff
@@ -1,6 +1,4 @@
-Configure the systemwide shared library files (/lib, /lib64, /usr/lib and /usr/lib64) to be protected from
-unauthorized access.
+Configure the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and
+"/usr/lib64" to be owned by root with the following command:

-Run the following command, replacing "[FILE]" with any library file not owned by "root".
-
-$ sudo chown root [FILE]
+$ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -user root -exec chown root {} +
```

</details>

#### V-257921 — Changed

**RHEL 9 library files must be group-owned by root or a system account.**

STIG ID: `RHEL-09-232205`. Severity: medium.
Rule ID: `SV-257921r1069387_rule` → `SV-257921r1106308_rule`.
CCI: CCI-001499.

- **Image criteria:** direct: None; shared-control review: [IMG-10], [IMG-15].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-5(6)][cw-cm-5.6].
- **Baseline / control determinations:** `cm-5.6`: `image-owned` (criterion); handoff: [PLT-03], [PLT-12].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,6 +1,6 @@
-Verify the systemwide shared library files are group-owned by "root" with the following command:
+Verify the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and
+"/usr/lib64" are group owned by root with the following command:

-$ sudo find -L /lib /lib64 /usr/lib /usr/lib64 ! -group root ! -type d -exec stat -L -c "%G %n" {} \;
+$ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec stat -c "%n %G" {} +

-If any systemwide shared library file is returned and is not group-owned by a required system account, this is
- a finding.
+If any output is returned, this is a finding.
```

**Fix**

```diff
@@ -1,6 +1,4 @@
-Configure the systemwide shared library files (/lib, /lib64, /usr/lib and /usr/lib64) to be protected from
-unauthorized access.
+Configure the systemwide shared library files contained in the directories "/lib", "/lib64", "/usr/lib", and
+"/usr/lib64" to be group owned by root with the following command:

-Run the following command, replacing "[FILE]" with any library file not group-owned by "root".
-
-$ sudo chgrp root [FILE]
+$ sudo find /lib /lib64 /usr/lib /usr/lib64 -type f -name '*.so*' ! -group root -exec chown :root {} +
```

</details>

#### V-257928 — Changed

**All RHEL 9 world-writable directories must be owned by root, sys, bin, or an application user.**

STIG ID: `RHEL-09-232240`. Severity: medium.
Rule ID: `SV-257928r1044992_rule` → `SV-257928r1268251_rule`.
CCI: CCI-001090.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-4][cw-sc-4].
- **Baseline / control determinations:** `sc-4`: `host-inherited` (determination); handoff: [PLT-02], [PLT-07].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,7 +1,7 @@
-Verify that world writable directories are owned by root, a system account, or an application account with the
- following command. It will discover and print world-writable directories that are not owned by root.  Run it
-once for each local partition [PART]:
+Verify RHEL 9 world writable directories are owned by root, a system account, or an application account with
+the following command:

-$ sudo find  PART  -xdev -type d -perm -0002 -uid +0 -print
+$ sudo find / -xdev -type d -perm -0002 -uid +999 -exec stat -c "%U, %u, %A, %n" {} \; 2>/dev/null

-If there is output, this is a finding.
+If there is output that indicates world-writable directories are owned by any account other than root or an
+approved system account, this is a finding.
```

**Fix**

```diff
@@ -1,7 +1,6 @@
-Configure all public directories to be owned by root or a system account to prevent unauthorized and
+Configure all RHEL 9 public directories to be owned by root or a system account to prevent unauthorized and
 unintended information transferred via shared system resources.

-Set the owner of all public directories as root or a system account using the command, replace "[Public
-Directory]" with any directory path not owned by root or a system account:
+Use the following command template to set ownership of public directories to root or a system account:

-$ sudo chown root [Public Directory]
+$ sudo chown [root or system account] [Public Directory]
```

</details>

#### V-257929 — Changed

**A sticky bit must be set on all RHEL 9 public directories.**

STIG ID: `RHEL-09-232245`. Severity: medium.
Rule ID: `SV-257929r958524_rule` → `SV-257929r1268233_rule`.
CCI: CCI-001090.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-4][cw-sc-4].
- **Baseline / control determinations:** `sc-4`: `host-inherited` (determination); handoff: [PLT-02], [PLT-07].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "acceptance/validation processes in DOD or other government"
+ "acceptance/validation processes in DoW or other government"
```

</details>

#### V-257935 — Changed

**RHEL 9 must have the firewalld package installed.**

STIG ID: `RHEL-09-251010`. Severity: medium.
Rule ID: `SV-257935r1044994_rule` → `SV-257935r1262137_rule`.
CCI: CCI-000382, CCI-002314, CCI-002322.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(1)][cw-ac-17.1], [AC-17(9)][cw-ac-17.9], [CM-7][cw-cm-7].
- **Baseline / control determinations:** `ac-17.1`: `host-inherited` (determination); handoff: [PLT-13]; `ac-17.9`: absent from current control baseline; `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "is access to DOD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-257936 — Changed

**The firewalld service on RHEL 9 must be active.**

STIG ID: `RHEL-09-251015`. Severity: medium.
Rule ID: `SV-257936r1044995_rule` → `SV-257936r1262138_rule`.
CCI: CCI-000382, CCI-002314.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(1)][cw-ac-17.1], [CM-7][cw-cm-7].
- **Baseline / control determinations:** `ac-17.1`: `host-inherited` (determination); handoff: [PLT-13]; `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "is access to DOD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-257937 — Changed

**The RHEL 9 firewall must employ a deny-all, allow-by-exception policy for allowing connections to other systems.**

STIG ID: `RHEL-09-251020`. Severity: medium.
Rule ID: `SV-257937r991589_rule` → `SV-257937r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "A RHEL 9 firewall"
+ "The RHEL 9 firewall"
```

**Discussion**

```diff
- "facilitate exfiltration of DOD data.\n\nRHEL 9"
+ "facilitate exfiltration of DoW data.\n\nRHEL 9"
```

**Check**

```diff
@@ -1,20 +1,29 @@
-Verify the RHEL 9 "firewalld" is configured to employ a deny-all, allow-by-exception policy for allowing
+Verify the RHEL 9 firewalld is configured to employ a deny-all, allow-by-exception policy for allowing
 connections to other systems with the following commands:

-$ sudo  firewall-cmd --state
-
+Ensure firewalld is running:
+$ sudo firewall-cmd --state
 running

+Identify active zones:
 $ sudo firewall-cmd --get-active-zones
+drop
+  interfaces: ens192

-public
-   interfaces: ens33
-
-$ sudo firewall-cmd --info-zone=public | grep target
-
-   target: DROP
-
-$ sudo firewall-cmd --permanent --info-zone=public | grep target
-
-   target: DROP
+Check what rules are applied in that zone:
+$ sudo firewall-cmd --list-all --zone=$(firewall-cmd --get-default-zone)
+drop (active)
+  target: DROP
+  icmp-block-inversion: no
+  interfaces: ens192
+  sources:
+  services: ssh
+  ports:
+  protocols:
+  forward: yes
+  masquerade: no
+  forward-ports:
+  source-ports:
+  icmp-blocks:
+  rich rules:

```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure the "firewalld" daemon to employ a deny-all, allow-by-exception with the following commands:
+Configure the "firewalld" daemon to employ a deny-all, allow-by-exception policy with the following commands:

@@ -14,3 +14,3 @@
 Add any interfaces to the newly modified "drop" zone:
-$ sudo firewall-cmd --permanent --zone=drop --change-interface=ens33
+$ sudo firewall-cmd --permanent --zone=drop --change-interface=ens192

```

</details>

#### V-257940 — Changed

**RHEL 9 must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments.**

STIG ID: `RHEL-09-251035`. Severity: medium.
Rule ID: `SV-257940r958480_rule` → `SV-257940r1106312_rule`.
CCI: CCI-000382.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7][cw-cm-7].
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -5,15 +5,3 @@

-$ sudo firewall-cmd --list-all-zones
-
-custom (active)
-target: DROP
-icmp-block-inversion: no
-interfaces: ens33
-sources:
-services: dhcpv6-client dns http https ldaps rpc-bind ssh
-ports:
-masquerade: no
-forward-ports:
-icmp-blocks:
-rich rules:
+$ sudo firewall-cmd --list-all-zones | grep -e "active" -e "services"

@@ -23,2 +11,2 @@
 If there are additional ports, protocols, or services that are not in the PPSM CLSA, or there are ports,
-protocols, or services that are prohibited by the PPSM Category Assurance List (CAL), this is a finding.
+protocols, or services that are prohibited by the PPSM CAL, this is a finding.
```

</details>

#### V-257942 — Changed

**RHEL 9 must enable hardening for the Berkeley Packet Filter just-in-time compiler.**

STIG ID: `RHEL-09-251045`. Severity: medium.
Rule ID: `SV-257942r1044999_rule` → `SV-257942r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "When hardened, the extended Berkeley Packet Filter (BPF) just-in-time (JIT) compiler will randomize any kernel addresses in the BPF programs and maps, and will not expose the JIT addresses in \"/proc/kallsyms\"."
+ "It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors.\n\nEnabling hardening for the Berkeley Packet Filter (BPF) Just-in-time (JIT) compiler aids in mitigating JIT spraying attacks. Setting the value to \"2\" enables JIT hardening for all users.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,17 +1,8 @@
-Verify RHEL 9 enables hardening for the BPF JIT with the following commands:
+Verify RHEL 9 enables hardening for the BPF JIT compiler.
+
+Check the status of the "net.core.bpf_jit_harden" parameter with the following command:

 $ sudo sysctl net.core.bpf_jit_harden
-
 net.core.bpf_jit_harden = 2

-If the returned line does not have a value of "2", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F net.core.bpf_jit_harden |
-tail -1
-
-net.core.bpf_jit_harden = 2
-
-If the network parameter "net.core.bpf_jit_harden" is not equal to "2" or nothing is returned, this is a
-finding.
+If "net.core.bpf_jit_harden" is not equal to "2" or is missing, this is a finding.
```

**Fix**

```diff
@@ -1,8 +1,11 @@
-Configure RHEL 9 to enable hardening for the BPF JIT compiler by adding the following line to a file, in the
-"/etc/sysctl.d" directory:
+Configure RHEL 9 to enable hardening for the BPF JIT compiler.

+Create the drop-in file if it does not already exist:
+
+$ sudo vi /etc/sysctl.d/99-net_core-bpf_jit_harden.conf
+
+Add the following line to the file:
 net.core.bpf_jit_harden = 2

-The system configuration files need to be reloaded for the changes to take effect. To reload the contents of
-the files, run the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257945 — Changed

**RHEL 9 must securely compare internal information system clocks at least every 24 hours.**

STIG ID: `RHEL-09-252020`. Severity: medium.
Rule ID: `SV-257945r1038944_rule` → `SV-257945r1262140_rule`.
CCI: CCI-001890, CCI-004923, CCI-004926, CCI-001891, CCI-002046.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-8][cw-au-8], [SC-45(1)][cw-sc-45.1].
- **Baseline / control determinations:** `au-8`: `host-inherited` (expectation); handoff: [HST-05]; `sc-45.1`: absent from current control baseline.
- **CCI findings:** old: CCI-001891: no Rev 5 reference; Rev 4 AU-8 (1) (a); CCI-002046: no Rev 5 reference; Rev 4 AU-8 (1) (b); candidate: CCI-001891: no Rev 5 reference; Rev 4 AU-8 (1) (a); CCI-002046: no Rev 5 reference; Rev 4 AU-8 (1) (b).

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "for the appropriate DOD network (NIPRNet/SIPRNet), and/or"
+ "for the appropriate DoW network (NIPRNet/SIPRNet), and/or"
```

**Check**

```diff
@@ -9,3 +9,3 @@

-Verify the "chrony.conf" file is configured to an authoritative DOD time source by running the following
+Verify the "chrony.conf" file is configured to an authoritative DoW time source by running the following
 command:
@@ -15,2 +15,2 @@

-If the parameter "server" is not set or is not set to an authoritative DOD time source, this is a finding.
+If the parameter "server" is not set or is not set to an authoritative DoW time source, this is a finding.
```

</details>

#### V-257946 — Changed

**RHEL 9 must disable the chrony daemon from acting as a server.**

STIG ID: `RHEL-09-252025`. Severity: low.
Rule ID: `SV-257946r958480_rule` → `SV-257946r1184307_rule`.
CCI: CCI-000381, CCI-000382.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7][cw-cm-7].
- **Baseline / control determinations:** `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,3 @@
+Note: If the server is serving as an NTP server, this is not applicable.
+
 Verify RHEL 9 disables the chrony daemon from acting as a server with the following command:
```

</details>

#### V-257949 — Changed

**RHEL 9 must configure a DNS processing mode in Network Manager.**

STIG ID: `RHEL-09-252040`. Severity: medium.
Rule ID: `SV-257949r1014841_rule` → `SV-257949r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "In order to ensure that DNS"
+ "To ensure that DNS"
- " must be configured."
+ " must be configured. The following are common DNS values in NetworkManager.conf [main]:\n\n- default: NetworkManager will update /etc/resolv.conf to reflect the nameservers provided by currently active connections.\n- none: NetworkManager will not modify /etc/resolv.conf. Used when DNS is managed manually or by another service.\n- systemd-resolved: Uses systemd-resolved to manage DNS.\n- dnsmasq: Enables the internal dnsmasq plugin."
```

**Check**

```diff
@@ -6,3 +6,4 @@

-If the dns key under main does not exist or is not set to "none" or "default", this is a finding.
+If the dns key under main does not exist or is not set to "default", "none", or "systemd-resolved", this is a
+finding.

```

**Fix**

```diff
@@ -2,5 +2,7 @@

-In "/etc/NetworkManager/NetworkManager.conf" add the following line in the "[main]" section:
+In "/etc/NetworkManager/NetworkManager.conf", add the following line in the "[main]" section:

-dns = none
+dns = <dns processing mode>
+
+Where <dns processing mode> is default, none, or systemd-resolved.

```

</details>

#### V-257954 — Changed

**RHEL 9 libreswan package must be installed.**

STIG ID: `RHEL-09-252065`. Severity: medium.
Rule ID: `SV-257954r1045008_rule` → `SV-257954r1268251_rule`.
CCI: CCI-000803.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-7][cw-ia-7].
- **Baseline / control determinations:** `ia-7`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-7`: `not-applicable`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,3 @@
+Note: If there is no operational need for Libreswan to be installed, this rule is not applicable.
+
 Verify that RHEL 9 libreswan service package is installed.
```

</details>

#### V-257957 — Changed

**RHEL 9 must be configured to use TCP syncookies.**

STIG ID: `RHEL-09-253010`. Severity: medium.
Rule ID: `SV-257957r1045009_rule` → `SV-257957r1268251_rule`.
CCI: CCI-001095, CCI-002385.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-5][cw-sc-5], [SC-5(2)][cw-sc-5.2].
- **Baseline / control determinations:** `sc-5`: `deployment-configured` (determination); handoff: [PLT-05], [PLT-10]; `sc-5.2`: `deployment-configured` (expectation); handoff: [PLT-05].

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "Denial of service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity.\n\nManaging excess capacity ensures that sufficient capacity is available to counter flooding attacks. Employing increased capacity and service redundancy may reduce the susceptibility to some DoS attacks. Managing excess capacity may include, for example, establishing selected usage priorities, quotas, or partitioning.\n\nSatisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000420-GPOS-00186,"
+ "Preventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection.\n\nThis requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoW or other government agencies.\n\nThere may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.\n\nRestricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a nonprivileged user.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf\n\nSatisfies: SRG-OS-000480-GPOS-00227, SRG-OS-000420-GPOS-00186,"
```

**Check**

```diff
@@ -2,15 +2,5 @@

-Determine if syncookies are used with the following command:
-
-Check the status of the kernel.perf_event_paranoid kernel parameter.
+Check the value of all "tcp_syncookies" variables with the following command:

 $ sudo sysctl net.ipv4.tcp_syncookies
-
-net.ipv4.tcp_syncookies = 1
-
-Check that the configuration files are present to enable this kernel parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F net.ipv4.tcp_syncookies |
-tail -1
-
 net.ipv4.tcp_syncookies = 1
```

**Fix**

```diff
@@ -2,6 +2,10 @@

-Add or edit the following line in a system configuration file in the "/etc/sysctl.d/" directory:
- net.ipv4.tcp_syncookies = 1
+Create a configuration file if it does not already exist:

-Load settings from all system configuration files with the following command:
+$ sudo vi /etc/sysctl.d/99-ipv4_tcp_syncookies.conf
+
+Add the following line to the file:
+net.ipv4.tcp_syncookies = 1
+
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257958 — Changed

**RHEL 9 must ignore Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages.**

STIG ID: `RHEL-09-253015`. Severity: medium.
Rule ID: `SV-257958r991589_rule` → `SV-257958r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "a man-in-the-middle attack.\n\nThis feature of the IPv4 protocol has few legitimate uses. It should be disabled unless absolutely required."
+ "a man-in-the-middle attack.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -2,16 +2,5 @@

-Check the value of the all "accept_redirects" variables with the following command:
+Check the value of all "net.ipv4.conf.all.accept_redirects" variables with the following command:

 $ sudo sysctl net.ipv4.conf.all.accept_redirects
-
-net.ipv4.conf.all.accept_redirects = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.all.accept_redirects | tail -1
-
 net.ipv4.conf.all.accept_redirects = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-ipv4_accept_redirects.conf
+
+Add the following line to the file:
 net.ipv4.conf.all.accept_redirects = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257959 — Changed

**RHEL 9 must not forward Internet Protocol version 4 (IPv4) source-routed packets.**

STIG ID: `RHEL-09-253020`. Severity: medium.
Rule ID: `SV-257959r991589_rule` → `SV-257959r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " packet to suggest routers forward the"
+ " packet to suggest that routers forward the"
- "the forwarding of source-routerd traffic, such as when IPv4 forwarding is enabled"
+ "the forwarding of source-routed traffic, such as when forwarding is enabled"
- "as a router.\n\nAccepting source-routed packets in the IPv4 protocol has few legitimate uses. It must be disabled unless it is absolutely required."
+ "as a router.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of which of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -2,16 +2,5 @@

-Check the value of the all "accept_source_route" variables with the following command:
+Check the value of the "accept_source_route" variable with the following command:

 $ sudo sysctl net.ipv4.conf.all.accept_source_route
-
-net.ipv4.conf.all.accept_source_route = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.all.accept_source_route | tail -1
-
 net.ipv4.conf.all.accept_source_route = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-ipv4_accept_source.conf
+
+Add the following line to the file:
 net.ipv4.conf.all.accept_source_route = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257960 — Changed

**RHEL 9 must log IPv4 packets with impossible addresses.**

STIG ID: `RHEL-09-253025`. Severity: medium.
Rule ID: `SV-257960r991589_rule` → `SV-257960r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " to be detected."
+ " to be detected.\n\nPreventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection.\n\nThis requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoW or other government agencies.\n\nThere may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.\n\nRestricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a nonprivileged user.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -2,16 +2,5 @@

-Check the value of the accept source route variable with the following command:
+Check the value of the "log_martians" variable with the following command:

 $ sudo sysctl net.ipv4.conf.all.log_martians
-
-net.ipv4.conf.all.log_martians = 1
-
-If the returned line does not have a value of "1", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.all.log_martians | tail -1
-
 net.ipv4.conf.all.log_martians = 1
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-ipv4_log_martians.conf
+
+Add the following line to the file:
 net.ipv4.conf.all.log_martians=1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257961 — Changed

**RHEL 9 must log IPv4 packets with impossible addresses by default.**

STIG ID: `RHEL-09-253030`. Severity: medium.
Rule ID: `SV-257961r991589_rule` → `SV-257961r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " to be detected."
+ " to be detected.\n\nPreventing unauthorized information transfers mitigates the risk of information, including encrypted representations of information, produced by the actions of prior users/roles (or the actions of processes acting on behalf of prior users/roles) from being available to any current users/roles (or current processes) that obtain access to shared system resources (e.g., registers, main memory, hard disks) after those resources have been released back to information systems. The control of information in shared resources is also commonly referred to as object reuse and residual information protection.\n\nThis requirement generally applies to the design of an information technology product, but it can also apply to the configuration of particular information system components that are, or use, such products. This can be verified by acceptance/validation processes in DoW or other government agencies.\n\nThere may be shared resources with configurable protections (e.g., files in storage) that may be assessed on specific information system components.\n\nRestricting access to the kernel message buffer limits access to only root. This prevents attackers from gaining additional system information as a nonprivileged user.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -2,16 +2,5 @@

-Check the value of the accept source route variable with the following command:
+Check the value of the "default.log_martians" variable with the following command:

 $ sudo sysctl net.ipv4.conf.default.log_martians
-
-net.ipv4.conf.default.log_martians = 1
-
-If the returned line does not have a value of "1", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.default.log_martians | tail -1
-
 net.ipv4.conf.default.log_martians = 1
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-ipv4_log_martians.conf
+
+Add the following line to the file:
 net.ipv4.conf.default.log_martians=1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257962 — Changed

**RHEL 9 must use reverse path filtering on all IPv4 interfaces.**

STIG ID: `RHEL-09-253035`. Severity: medium.
Rule ID: `SV-257962r991589_rule` → `SV-257962r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " serving small networks."
+ " serving small networks.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,14 +1,6 @@
-Verify RHEL 9 uses reverse path filtering on all IPv4 interfaces with the following commands:
+Verify RHEL 9 uses reverse path filtering on all IPv4 interfaces.
+
+Check the value of the "rp_filter" variable with the following command:

 $ sudo sysctl net.ipv4.conf.all.rp_filter
-
-net.ipv4.conf.all.rp_filter = 1
-
-If the returned line does not have a value of "1", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F net.ipv4.conf.all.rp_filter
-| tail -1
-
 net.ipv4.conf.all.rp_filter = 1
```

**Fix**

```diff
@@ -2,8 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-ipv4_rp_filter.conf
+
+Add the following line to the file:
 net.ipv4.conf.all.rp_filter = 1

-The system configuration files need to be reloaded for the changes to take effect. To reload the contents of
-the files, run the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257963 — Changed

**RHEL 9 must prevent IPv4 Internet Control Message Protocol (ICMP) redirect messages from being accepted.**

STIG ID: `RHEL-09-253040`. Severity: medium.
Rule ID: `SV-257963r991589_rule` → `SV-257963r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " unless absolutely required."
+ " unless absolutely required.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -2,16 +2,5 @@

-Check the value of the default "accept_redirects" variables with the following command:
+Check the value of the default "accept_redirects" variable with the following command:

 $ sudo sysctl net.ipv4.conf.default.accept_redirects
-
-net.ipv4.conf.default.accept_redirects = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.default.accept_redirects | tail -1
-
 net.ipv4.conf.default.accept_redirects = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-ipv4_accept_redirects.conf
+
+Add the following line to the file:
 net.ipv4.conf.default.accept_redirects = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257964 — Changed

**RHEL 9 must not forward IPv4 source-routed packets by default.**

STIG ID: `RHEL-09-253045`. Severity: medium.
Rule ID: `SV-257964r991589_rule` → `SV-257964r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " network security measures.\n\nAccepting source-routed packets in the IPv4 protocol has few legitimate uses. It must be disabled unless it is absolutely required, such as when IPv4 forwarding is enabled"
+ " network security measures. This requirement applies only to the forwarding of source-routed traffic, such as when forwarding is enabled"
- "the system is legitimately functioning as a router."
+ "the system is functioning as a router.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -2,16 +2,5 @@

-Check the value of the accept source route variable with the following command:
+Check the value of the "accept source route" variable with the following command:

 $ sudo sysctl net.ipv4.conf.default.accept_source_route
-
-net.ipv4.conf.default.accept_source_route = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.default.accept_source_route | tail -1
-
 net.ipv4.conf.default.accept_source_route = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/99-ipv4_accept_source_route.conf
+
+Add the following line to the file:
 net.ipv4.conf.default.accept_source_route = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257965 — Changed

**RHEL 9 must use a reverse-path filter for IPv4 network traffic when possible by default.**

STIG ID: `RHEL-09-253050`. Severity: medium.
Rule ID: `SV-257965r991589_rule` → `SV-257965r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " serving small networks."
+ " serving small networks.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographic order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,5 +1,6 @@
-Verify RHEL 9 uses reverse path filtering on IPv4 interfaces with the following commands:
+Verify RHEL 9 uses reverse path filtering on IPv4 interfaces.
+
+Check the value of the "net.ipv4.conf.default.rp_filter" with the following command:

 $ sudo sysctl net.ipv4.conf.default.rp_filter
-
 net.ipv4.conf.default.rp_filter = 1
@@ -7,10 +8 @@
 If the returned line does not have a value of "1", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.default.rp_filter | tail -1
-
-net.ipv4.conf.default.rp_filter = 1
-
-If "net.ipv4.conf.default.rp_filter" is not set to "1" or is missing, this is a finding.
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv4_rp_filter.conf
+
+Add the following line to the file:
 net.ipv4.conf.default.rp_filter = 1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257966 — Changed

**RHEL 9 must not respond to Internet Control Message Protocol (ICMP) echoes sent to a broadcast address.**

STIG ID: `RHEL-09-253055`. Severity: medium.
Rule ID: `SV-257966r991589_rule` → `SV-257966r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " on the network."
+ " on the network.\n\nThere are notable differences between Internet Protocol version 4 (IPv4) and Internet Protocol version 6 (IPv6). IPv6 does not implement the same method of broadcast as IPv4. Instead, IPv6 uses multicast addressing to the all-hosts multicast group. Refer to RFC4294 for an explanation of \"IPv6 Node Requirements\", which resulted in this difference between IPv4 and IPv6.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify RHEL 9 does not respond to ICMP echoes sent to a broadcast address.
+Verify RHEL 9 ignores ICMP echoes sent to a broadcast address.

@@ -5,13 +5,2 @@
 $ sudo sysctl net.ipv4.icmp_echo_ignore_broadcasts
-
-net.ipv4.icmp_echo_ignore_broadcasts = 1
-
-If the returned line does not have a value of "1", a line is not returned, or the retuned line is commented
-out, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|$)' | grep -F
-net.ipv4.icmp_echo_ignore_broadcasts | tail -1
-
 net.ipv4.icmp_echo_ignore_broadcasts = 1
```

**Fix**

```diff
@@ -1,8 +1,11 @@
-Configure RHEL 9 to not respond to IPv4 ICMP echoes sent to a broadcast address.
+Configure RHEL 9 to ignore IPv4 ICMP echoes sent to a broadcast address.

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv4_icmp_echo_ignore_broadcasts.conf
+
+Add the following line to the file:
 net.ipv4.icmp_echo_ignore_broadcasts = 1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257967 — Changed

**RHEL 9 must limit the number of bogus Internet Control Message Protocol (ICMP) response errors logs.**

STIG ID: `RHEL-09-253060`. Severity: medium.
Rule ID: `SV-257967r991589_rule` → `SV-257967r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " not be logged."
+ " not be logged.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,17 +1,8 @@
-The runtime status of the net.ipv4.icmp_ignore_bogus_error_responses kernel parameter can be queried by
-running the following command:
+Verify RHEL 9 limits the number of bogus Internet Control Message Protocol (ICMP) response errors logs.
+
+Check the value of the "net.ipv4.icmp_ignore_bogus_error_response" variables with the following command:

 $ sudo sysctl net.ipv4.icmp_ignore_bogus_error_responses
-
 net.ipv4.icmp_ignore_bogus_error_responses = 1

-If "net.ipv4.icmp_ignore_bogus_error_responses" is not set to "1", this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.icmp_ignore_bogus_error_response | tail -1
-
-net.ipv4.icmp_ignore_bogus_error_response = 1
-
 If "net.ipv4.icmp_ignore_bogus_error_response" is not set to "1" or is missing, this is a finding.
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv4_icmp_ignore_bogus_error_responses.conf
+
+Add the following line to the file:
 net.ipv4.icmp_ignore_bogus_error_responses = 1

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257968 — Changed

**RHEL 9 must not send Internet Control Message Protocol (ICMP) redirects.**

STIG ID: `RHEL-09-253065`. Severity: medium.
Rule ID: `SV-257968r991589_rule` → `SV-257968r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " acting as routers."
+ " acting as routers.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -5,12 +5,2 @@
 $ sudo sysctl net.ipv4.conf.all.send_redirects
-
-net.ipv4.conf.all.send_redirects = 0
-
-If the returned line does not have a value of "0", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F
-net.ipv4.conf.all.send_redirects | tail -1
-
 net.ipv4.conf.all.send_redirects = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv4_send_redirects.conf
+
+Add the following line to the file:
 net.ipv4.conf.all.send_redirects = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257969 — Changed

**RHEL 9 must not allow interfaces to perform Internet Control Message Protocol (ICMP) redirects by default.**

STIG ID: `RHEL-09-253070`. Severity: medium.
Rule ID: `SV-257969r991589_rule` → `SV-257969r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " the network topology.\n\nThe ability to "
+ " the network topology. The ability to "
- " acting as routers."
+ " acting as routers.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,4 +1 @@
-Verify RHEL 9 does not allow interfaces to perform Internet Protocol version 4 (IPv4) ICMP redirects by
-default.
-
 Check the value of the "default send_redirects" variables with the following command:
@@ -6,13 +3,3 @@
 $ sudo sysctl net.ipv4.conf.default.send_redirects
-
 net.ipv4.conf.default.send_redirects=0
-
-If the returned line does not have a value of "0", or a line is not returned, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F
-net.ipv4.conf.default.send_redirects | tail -1
-
-net.ipv4.conf.default.send_redirects = 0

```

**Fix**

```diff
@@ -3,4 +3,7 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv4_send_redirect.conf
+
+Add the following line to the file:
 net.ipv4.conf.default.send_redirects = 0
```

</details>

#### V-257970 — Changed

**RHEL 9 must not enable IPv4 packet forwarding unless the system is a router.**

STIG ID: `RHEL-09-253075`. Severity: medium.
Rule ID: `SV-257970r1045011_rule` → `SV-257970r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " across the network."
+ " across the network.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -2,19 +2,8 @@

-Check that IPv4 forwarding is disabled using the following command:
+Check that "net.ipv4.conf.all.forwarding" is disabled using the following command:

 $ sudo sysctl net.ipv4.conf.all.forwarding
-
 net.ipv4.conf.all.forwarding = 0

-If the IPv4 forwarding value is not "0" and is not documented with the information system security officer
-(ISSO) as an operational requirement, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|$)' | grep -F net.ipv4.conf.all.forwarding |
-tail -1
-
-net.ipv4.conf.all.forwarding = 0
-
-If "net.ipv4.conf.all.forwarding" is not set to "0" and is not documented with the ISSO as an operational
-requirement or is missing, this is a finding.
+If "net.ipv4.conf.all.forwarding" is not set to "0" and is not documented with the information system security
+ officer (ISSO) as an operational requirement or is missing, this is a finding.
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv4_forwarding.conf
+
+Add the following line to the file:
 net.ipv4.conf.all.forwarding = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257971 — Changed

**RHEL 9 must not accept router advertisements on all IPv6 interfaces.**

STIG ID: `RHEL-09-254010`. Severity: medium.
Rule ID: `SV-257971r991589_rule` → `SV-257971r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "An illicit router "
+ "Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.\n\nAn illicit router "
- " a man-in-the-middle attack."
+ " a man-in-the-middle attack.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -4,16 +4,6 @@

-Determine if router advertisements are not accepted by using the following command:
+Check that "net.ipv6.conf.all.accept_ra" is set to not accept router advertisements by using the following
+command:

 $ sudo sysctl net.ipv6.conf.all.accept_ra
-
-net.ipv6.conf.all.accept_ra = 0
-
-If the "accept_ra" value is not "0" and is not documented with the information system security officer (ISSO)
-as an operational requirement, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F net.ipv6.conf.all.accept_ra
-| tail -1
-
 net.ipv6.conf.all.accept_ra = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv4_accept_ra.conf
+
+Add the following line to the file:
 net.ipv6.conf.all.accept_ra = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257972 — Changed

**RHEL 9 must ignore IPv6 Internet Control Message Protocol (ICMP) redirect messages.**

STIG ID: `RHEL-09-254015`. Severity: medium.
Rule ID: `SV-257972r991589_rule` → `SV-257972r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "An illicit ICMP "
+ "ICMP redirect messages are used by routers to inform hosts that a more direct route exists for a particular destination. These messages modify the host's route table and are unauthenticated. An illicit ICMP "
- " a man-in-the-middle attack."
+ " a man-in-the-middle attack.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -4,16 +4,5 @@

-Check the value of the "accept_redirects" variables with the following command:
+Check the value of the "accept_redirects" variable with the following command:

 $ sysctl net.ipv6.conf.all.accept_redirects
-
-net.ipv6.conf.all.accept_redirects = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F
-net.ipv6.conf.all.accept_redirects | tail -1
-
 net.ipv6.conf.all.accept_redirects = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv6_accept_redirects.conf
+
+Add the following line to the file:
 net.ipv6.conf.all.accept_redirects = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257973 — Changed

**RHEL 9 must not forward IPv6 source-routed packets.**

STIG ID: `RHEL-09-254020`. Severity: medium.
Rule ID: `SV-257973r991589_rule` → `SV-257973r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " as a router."
+ " as a router.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -4,16 +4,5 @@

-Check the value of the accept source route variable with the following command:
+Check the value of the "net.ipv6.conf.all.accept_source_route" variable with the following command:

 $ sudo sysctl net.ipv6.conf.all.accept_source_route
-
-net.ipv6.conf.all.accept_source_route = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F
-net.ipv6.conf.all.accept_source_route | tail -1
-
 net.ipv6.conf.all.accept_source_route = 0
```

**Fix**

```diff
@@ -1,8 +1,11 @@
-Configure RHEL 9 to not forward IPv6 source-routed packets.
+Configure RHEL 9 to not accept IPv6 source-routed packets.

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv6_accept_source_route.conf
+
+Add the following line to the file:
 net.ipv6.conf.all.accept_source_route = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257974 — Changed

**RHEL 9 must not enable IPv6 packet forwarding unless the system is a router.**

STIG ID: `RHEL-09-254025`. Severity: medium.
Rule ID: `SV-257974r991589_rule` → `SV-257974r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "IP forwarding permits the kernel to forward packets from one network interface to another. The ability to forward packets between two networks is only appropriate for systems acting as routers."
+ "Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -4,16 +4,5 @@

-Check that IPv6 forwarding is disabled using the following commands:
+Check the value of the "net.ipv6.conf.all.forwarding" variable with the following command:

 $ sudo sysctl net.ipv6.conf.all.forwarding
-
-net.ipv6.conf.all.forwarding = 0
-
-If the IPv6 forwarding value is not "0" and is not documented with the information system security officer
-(ISSO) as an operational requirement, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' | grep -F net.ipv6.conf.all.forwarding
- | tail -1
-
 net.ipv6.conf.all.forwarding = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv6_forwarding.conf
+
+Add the following line to the file:
 net.ipv6.conf.all.forwarding = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257975 — Changed

**RHEL 9 must not accept router advertisements on all IPv6 interfaces by default.**

STIG ID: `RHEL-09-254030`. Severity: medium.
Rule ID: `SV-257975r991589_rule` → `SV-257975r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "An illicit router "
+ "Routing protocol daemons are typically used on routers to exchange network topology information with other routers. If this software is used when not required, system network information may be unnecessarily transmitted across the network. An illicit router "
- " a man-in-the-middle attack."
+ " a man-in-the-middle attack.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -5,16 +5,5 @@

-Determine if router advertisements are not accepted by default by using the following command:
+Check the value of the "net.ipv6.conf.default.accept_ra" variable with the following command:

 $ sudo sysctl net.ipv6.conf.default.accept_ra
-
-net.ipv6.conf.default.accept_ra = 0
-
-If the "accept_ra" value is not "0" and is not documented with the information system security officer (ISSO)
-as an operational requirement, this is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F
-net.ipv6.conf.default.accept_ra | tail -1
-
 net.ipv6.conf.default.accept_ra = 0
```

**Fix**

```diff
@@ -3,7 +3,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv6_accept_ra.conf
+
+Add the following line to the file:
 net.ipv6.conf.default.accept_ra = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257976 — Changed

**RHEL 9 must prevent IPv6 Internet Control Message Protocol (ICMP) redirect messages from being accepted.**

STIG ID: `RHEL-09-254035`. Severity: medium.
Rule ID: `SV-257976r991589_rule` → `SV-257976r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " a man-in-the-middle attack."
+ " a man-in-the-middle attack.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify RHEL 9 will not accept IPv6 ICMP redirect messages.
+Verify RHEL 9 to prevent IPv6 ICMP redirect messages.

@@ -4,16 +4,5 @@

-Check the value of the default "accept_redirects" variables with the following command:
+Check the value of the "net.ipv6.conf.default.accept_redirects" variables with the following command:

 $ sudo sysctl net.ipv6.conf.default.accept_redirects
-
-net.ipv6.conf.default.accept_redirects = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F
-net.ipv6.conf.default.accept_redirects | tail -1
-
 net.ipv6.conf.default.accept_redirects = 0
```

**Fix**

```diff
@@ -2,7 +2,10 @@

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv6_accept_redirects.conf
+
+Add the following line to the file:
 net.ipv6.conf.default.accept_redirects = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257977 — Changed

**RHEL 9 must not forward IPv6 source-routed packets by default.**

STIG ID: `RHEL-09-254040`. Severity: medium.
Rule ID: `SV-257977r991589_rule` → `SV-257977r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " is absolutely required."
+ " is absolutely required.\n\nThe sysctl --system command will load settings from all system configuration files. All configuration files are sorted by their filename in lexicographical order, regardless of the directories in which they reside. If multiple files specify the same option, the entry in the file with the lexicographically latest name will take precedence. Files are read from directories in the following list from top to bottom. Once a file of a given filename is loaded, any file of the same name in subsequent directories is ignored.\n\n/etc/sysctl.d/*.conf\n/run/sysctl.d/*.conf\n/usr/local/lib/sysctl.d/*.conf\n/usr/lib/sysctl.d/*.conf\n/lib/sysctl.d/*.conf\n/etc/sysctl.conf"
```

**Check**

```diff
@@ -4,16 +4,5 @@

-Check the value of the accept source route variable with the following command:
+Check the value of the "net.ipv6.conf.default.accept_source_route" variables with the following command:

 $ sudo sysctl net.ipv6.conf.default.accept_source_route
-
-net.ipv6.conf.default.accept_source_route = 0
-
-If the returned line does not have a value of "0", a line is not returned, or the line is commented out, this
-is a finding.
-
-Check that the configuration files are present to enable this network parameter.
-
-$ sudo /usr/lib/systemd/systemd-sysctl --cat-config | egrep -v '^(#|;)' |  grep -F
-net.ipv6.conf.default.accept_source_route | tail -1
-
 net.ipv6.conf.default.accept_source_route = 0
```

**Fix**

```diff
@@ -1,8 +1,11 @@
-Configure RHEL 9 to not forward IPv6 source-routed packets by default.
+Configure RHEL 9 to not accept IPv6 source-routed packets by default.

-Add or edit the following line in a single system configuration file, in the "/etc/sysctl.d/" directory:
+Create a configuration file if it does not already exist:

+$ sudo vi /etc/sysctl.d/ipv6_accept_source_route.conf
+
+Add the following line to the file:
 net.ipv6.conf.default.accept_source_route = 0

-Load settings from all system configuration files with the following command:
+Reload settings from all system configuration files with the following command:

```

</details>

#### V-257981 — Changed

**RHEL 9 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a SSH logon.**

STIG ID: `RHEL-09-255025`. Severity: medium.
Rule ID: `SV-257981r1045019_rule` → `SV-257981r1268215_rule`.
CCI: CCI-000048, CCI-001384, CCI-001385, CCI-001386, CCI-001387, CCI-001388.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DOD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Check**

```diff
@@ -1,5 +1,5 @@
-Verify that any SSH connection to the operating system displays the Standard Mandatory DOD Notice and Consent
-Banner before granting access to the system.
+Verify any SSH connection to RHEL 9 displays the Standard Mandatory DoW Notice and Consent Banner before
+granting access to the system.

-Check for the location of the banner file currently being used with the following command:
+Check for the location of the banner file being used with the following command:

@@ -7,5 +7,7 @@
 '^\s*banner'
+/etc/ssh/sshd_config.d/80-bannerPointer.conf:Banner /etc/issue

-banner /etc/issue
+This command will return the banner keyword and the name of the file that contains the SSH banner (in this
+case "/etc/issue").

-If the line is commented out or if the file is missing, this is a finding.
+If the line is commented out, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure RHEL 9 to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the
+Configure RHEL 9 to display the Standard Mandatory DoW Notice and Consent Banner before granting access to the
  system via ssh.
```

</details>

#### V-257983 — Changed

**RHEL 9 SSHD must accept public key authentication.**

STIG ID: `RHEL-09-255035`. Severity: medium.
Rule ID: `SV-257983r1045024_rule` → `SV-257983r1268228_rule`.
CCI: CCI-000765, CCI-000766, CCI-000767, CCI-000768.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2(1)][cw-ia-2.1], [IA-2(2)][cw-ia-2.2].
- **Baseline / control determinations:** `ia-2.1`: `research-required` (determination); handoff: [PLT-13]; `ia-2.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.1`: `not-applicable`; `ia-2.2`: `not-applicable`.
- **CCI findings:** old: CCI-000767: no Rev 5 reference; Rev 4 IA-2 (3); CCI-000768: no Rev 5 reference; Rev 4 IA-2 (4); candidate: CCI-000767: no Rev 5 reference; Rev 4 IA-2 (3); CCI-000768: no Rev 5 reference; Rev 4 IA-2 (4).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "privileged user. A DOD common access card (CAC) with DOD-approved PKI is an"
+ "privileged user. A DoW common access card (CAC) with DoW-approved PKI is an"
```

</details>

#### V-257989 — Changed

**The RHEL 9 SSH server must be configured to use only DoW-approved encryption ciphers employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.**

STIG ID: `RHEL-09-255065`. Severity: medium → high.
Rule ID: `SV-257989r1051240_rule` → `SV-257989r1268237_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.

**Changed fields:** title, discussion, severity.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "to use only DOD-approved encryption ciphers employing"
+ "to use only DoW-approved encryption ciphers employing"
```

**Discussion**

```diff
- "is access to DOD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-257991 — Changed

**The RHEL 9 SSH server must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections.**

STIG ID: `RHEL-09-255075`. Severity: medium → high.
Rule ID: `SV-257991r1051246_rule` → `SV-257991r1268237_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.

**Changed fields:** discussion, severity.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "is access to DOD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-257996 — Changed

**RHEL 9 must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive.**

STIG ID: `RHEL-09-255100`. Severity: medium.
Rule ID: `SV-257996r1045055_rule` → `SV-257996r1134915_rule`.
CCI: CCI-001133, CCI-002361, CCI-002891.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-12][cw-ac-12], [MA-4(7)][cw-ma-4.7], [SC-10][cw-sc-10].
- **Baseline / control determinations:** `ac-12`: `research-required` (undetermined); `ma-4.7`: absent from current control baseline; `sc-10`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-12`: `not-applicable`; `sc-10`: `deployment-configured`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -6,3 +6,9 @@

-ClientAliveInterval 600
+/etc/ssh/sshd_config.d/ClientAliveInterval.conf:ClientAliveInterval 600
+
+Verify the runtime value of "ClientAliveInterval" with the following command:
+
+$ sudo sshd -T | grep -i clientaliveinterval
+
+clientaliveinterval 600

```

</details>

#### V-257999 — Changed

**RHEL 9 SSH server configuration files' permissions must not be modified.**

STIG ID: `RHEL-09-255115`. Severity: medium.
Rule ID: `SV-257999r1082182_rule` → `SV-257999r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,3 +2,3 @@

-$ sudo rpm --verify openssh-server
+$ sudo rpm --verify openssh-server | awk '! ($2 == "c" && $1 ~ /^.\..\.\.\.\..\./) {print $0}'

```

**Fix**

```diff
@@ -2,4 +2,3 @@

-$ sudo dnf reinstall -y openssh-server
-$ rpm --setugids openssh-server
-$ rpm --setperms openssh-server
+$ sudo rpm --setugids openssh-server
+$ sudo rpm --setperms openssh-server
```

</details>

#### V-258000 — Changed

**RHEL 9 SSH private host key files must have mode 0600 or less permissive.**

STIG ID: `RHEL-09-255120`. Severity: medium.
Rule ID: `SV-258000r1045063_rule` → `SV-258000r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "must have mode 0640 or less permissive."
+ "must have mode 0600 or less permissive."
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify the SSH private host key files have a mode of "0640" or less permissive with the following command:
+Verify the SSH private host key files have a mode of "0600" or less permissive with the following command:

@@ -4,7 +4,7 @@

-640 /etc/ssh/ssh_host_dsa_key
-640 /etc/ssh/ssh_host_ecdsa_key
-640 /etc/ssh/ssh_host_ed25519_key
-640 /etc/ssh/ssh_host_rsa_key
+600 /etc/ssh/ssh_host_dsa_key
+600 /etc/ssh/ssh_host_ecdsa_key
+600 /etc/ssh/ssh_host_ed25519_key
+600 /etc/ssh/ssh_host_rsa_key

-If any private host key file has a mode more permissive than "0640", this is a finding.
+If any private host key file has a mode more permissive than "0600", this is a finding.
```

**Fix**

```diff
@@ -1,4 +1,4 @@
-Configure the mode of SSH private host key files under "/etc/ssh" to "0640" with the following command:
+Configure the mode of SSH private host key files under "/etc/ssh" to "0600" with the following command:

-$ sudo chmod 0640 /etc/ssh/ssh_host*key
+$ sudo chmod 0600 /etc/ssh/ssh_host*key

```

</details>

#### V-258012 — Changed

**RHEL 9 must enable the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a graphical user logon.**

STIG ID: `RHEL-09-271010`. Severity: medium.
Rule ID: `SV-258012r1014855_rule` → `SV-258012r1268215_rule`.
CCI: CCI-000048, CCI-001384, CCI-001385, CCI-001386, CCI-001387, CCI-001388.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "RHEL 9 must display the Standard Mandatory DOD Notice and Consent"
+ "RHEL 9 must enable the Standard Mandatory DoW Notice and Consent"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify RHEL 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the
+Verify RHEL 9 enables the Standard Mandatory DoW Notice and Consent Banner before granting access to the
 operating system via a graphical user logon.
```

**Fix**

```diff
@@ -1,3 +1,3 @@
-Configure RHEL 9 to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the
- system via a graphical user logon.
+Configure RHEL 9 to enable the Standard Mandatory DoW Notice and Consent Banner before granting access to the
+system via a graphical user logon.

```

</details>

#### V-258017 — Changed

**RHEL 9 must prevent a user from overriding the disabling of the graphical user interface autorun function.**

STIG ID: `RHEL-09-271035`. Severity: medium.
Rule ID: `SV-258017r1045088_rule` → `SV-258017r1155688_rule`.
CCI: CCI-000778, CCI-001958.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-3][cw-ia-3].
- **Baseline / control determinations:** `ia-3`: `host-inherited` (expectation); handoff: [PLT-15].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -6,3 +6,3 @@

-Determine which profile the system database is using with the following command:
+Check that the autorun setting is set to prevent user modification with the following command:

```

</details>

#### V-258023 — Changed

**RHEL 9 must automatically lock graphical user sessions after 10 minutes of inactivity.**

STIG ID: `RHEL-09-271065`. Severity: medium.
Rule ID: `SV-258023r958402_rule` → `SV-258023r1155656_rule`.
CCI: CCI-000057, CCI-000060.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-11][cw-ac-11], [AC-11(1)][cw-ac-11.1].
- **Baseline / control determinations:** `ac-11`: `not-applicable` (determination); `ac-11.1`: `not-applicable` (determination).

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "user sessions after 15 minutes of inactivity."
+ "user sessions after 10 minutes of inactivity."
```

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify RHEL 9 initiates a session lock after a 15-minute period of inactivity for graphical user interfaces
+Verify RHEL 9 initiates a session lock after a 10-minute period of inactivity for graphical user interfaces
 with the following command:
@@ -9,4 +9,4 @@

-uint32 900
+uint32 600

-If "idle-delay" is set to "0" or a value greater than "900", this is a finding.
+If "idle-delay" is set to "0" or a value greater than "600", this is a finding.
```

**Fix**

```diff
@@ -1,5 +1,5 @@
-Configure RHEL 9 to initiate a screensaver after a 15-minute period of inactivity for graphical user
+Configure RHEL 9 to initiate a screensaver after a 10-minute period of inactivity for graphical user
 interfaces.

-Create a database to contain the system-wide screensaver settings (if it does not already exist) with the
+Create a database to contain the systemwide screensaver settings (if it does not already exist) with the
 following command:
@@ -11,4 +11,4 @@
 [org/gnome/desktop/session]
-# Set the lock time out to 900 seconds before the session is considered idle
-idle-delay=uint32 900
+# Set the lock time out to 600 seconds before the session is considered idle
+idle-delay=uint32 600

```

</details>

#### V-258031 — Changed

**RHEL 9 must disable the ability of a user to accidentally press Ctrl-Alt-Del and cause a system to shut down or reboot.**

STIG ID: `RHEL-09-271105`. Severity: medium.
Rule ID: `SV-258031r1045114_rule` → `SV-258031r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,4 +4,4 @@
 Note: This requirement assumes the use of the RHEL 9 default graphical user interface, the GNOME desktop
-environment. If the system does not have any graphical user interface installed, this requirement is Not
-Applicable.
+environment. If the system does not have any graphical user interface installed, this requirement is not
+applicable.

@@ -9,3 +9,3 @@

-"['']"
+['']

```

</details>

#### V-258037 — Changed

**RHEL 9 must enable Linux audit logging for the USBGuard daemon.**

STIG ID: `RHEL-09-291025`. Severity: low.
Rule ID: `SV-258037r1014863_rule` → `SV-258037r1268225_rule`.
CCI: CCI-000169.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-12][cw-au-12].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `au-12`: `image-owned`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "generating audit records.\n\nDOD has defined the"
+ "generating audit records.\n\nDoW has defined the"
```

</details>

#### V-258039 — Changed

**RHEL 9 Bluetooth must be disabled.**

STIG ID: `RHEL-09-291035`. Severity: medium.
Rule ID: `SV-258039r1045131_rule` → `SV-258039r1262150_rule`.
CCI: CCI-000381, CCI-001443.

- **Image criteria:** direct: None; shared-control review: [IMG-06], [IMG-07], [IMG-14], [IMG-27], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-18(1)][cw-ac-18.1], [CM-7][cw-cm-7].
- **Baseline / control determinations:** `ac-18.1`: `not-applicable` (determination); `cm-7`: `image-owned` (criterion); handoff: [PLT-04], [PLT-16].

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "peripherals must meet DOD requirements for wireless"
+ "peripherals must meet DoW requirements for wireless"
```

</details>

#### V-258040 — Changed

**RHEL 9 wireless network adapters must be disabled.**

STIG ID: `RHEL-09-291040`. Severity: medium.
Rule ID: `SV-258040r991568_rule` → `SV-258040r1262151_rule`.
CCI: CCI-001443, CCI-001444, CCI-002418, CCI-002421.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-18(1)][cw-ac-18.1], [SC-8][cw-sc-8], [SC-8(1)][cw-sc-8.1].
- **Baseline / control determinations:** `ac-18.1`: `not-applicable` (determination); `sc-8`: `research-required` (undetermined); `sc-8.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`; `sc-8.1`: `deployment-configured`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "peripherals must meet DOD requirements for wireless"
+ "peripherals must meet DoW requirements for wireless"
```

</details>

#### V-258041 — Changed

**RHEL 9 user account passwords for new users or password changes must have a 180-day maximum password lifetime restriction in /etc/login.defs.**

STIG ID: `RHEL-09-411010`. Severity: medium.
Rule ID: `SV-258041r1038967_rule` → `SV-258041r1268211_rule`.
CCI: CCI-004066, CCI-000199 → CCI-000199, CCI-004066.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
- **CCI findings:** old: CCI-000199: no Rev 5 reference; Rev 4 IA-5 (1) (d); candidate: CCI-000199: no Rev 5 reference; Rev 4 IA-5 (1) (d).

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "must have a 60-day maximum password lifetime"
+ "must have a 180-day maximum password lifetime"
```

**Check**

```diff
@@ -1,8 +1,7 @@
-Verify that RHEL 9 enforces a 60-day maximum password lifetime for new user accounts by running the following
-command:
+Verify that RHEL 9 enforces a 180-day maximum password lifetime for new user accounts by running the following
+ command:

-$ grep -i pass_max_days /etc/login.defs
+$ sudo grep -i pass_max_days /etc/login.defs
+PASS_MAX_DAYS 180

-PASS_MAX_DAYS 60
-
-If the "PASS_MAX_DAYS" parameter value is greater than "60", or commented out, this is a finding.
+If the "PASS_MAX_DAYS" parameter value is greater than "180", or commented out, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure RHEL 9 to enforce a 60-day maximum password lifetime.
+Configure RHEL 9 to enforce a 180-day maximum password lifetime.

@@ -4,2 +4,2 @@

-PASS_MAX_DAYS 60
+PASS_MAX_DAYS 180
```

</details>

#### V-258042 — Changed

**RHEL 9 user account passwords must have a 180-day maximum password lifetime restriction.**

STIG ID: `RHEL-09-411015`. Severity: medium.
Rule ID: `SV-258042r1045133_rule` → `SV-258042r1268211_rule`.
CCI: CCI-004066, CCI-000199 → CCI-000199, CCI-004066.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
- **CCI findings:** old: CCI-000199: no Rev 5 reference; Rev 4 IA-5 (1) (d); candidate: CCI-000199: no Rev 5 reference; Rev 4 IA-5 (1) (d).

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "must have a 60-day maximum password lifetime"
+ "must have a 180-day maximum password lifetime"
```

**Check**

```diff
@@ -1,6 +1,6 @@
-Verify the maximum time period for existing passwords is restricted to 60 days with the following commands:
+Verify the maximum time period for existing passwords is restricted to 180 days with the following commands:

-$ sudo awk -F: '$5 > 60 {printf "%s %d\n", $1, $5}' /etc/shadow
+$ sudo awk -F: '$5 > 180 {print $1 " " $5}' /etc/shadow

-$ sudo awk -F: '$5 <= 0 {printf "%s %d\n", $1, $5}' /etc/shadow
+$ sudo awk -F: '$5 <= 0 {print $1 " " $5}' /etc/shadow

```

**Fix**

```diff
@@ -1,3 +1,3 @@
-Configure noncompliant accounts to enforce a 60-day maximum password lifetime restriction.
+Configure noncompliant accounts to enforce a 180-day maximum password lifetime restriction.

-passwd -x 60 [user]
+$ sudo passwd -x 180 [user]
```

</details>

#### V-258044 — Changed

**RHEL 9 must set the umask value to 077 for all local interactive user accounts.**

STIG ID: `RHEL-09-411025`. Severity: medium.
Rule ID: `SV-258044r1045135_rule` → `SV-258044r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -12,4 +12,4 @@

-/home/wadea/.bash_history:grep -i umask /etc/bashrc /etc/csh.cshrc /etc/profile
-/home/wadea/.bash_history:grep -i umask /etc/login.defs
+/home/disauser/.bash_history:grep -i umask /etc/bashrc /etc/csh.cshrc /etc/profile
+/home/disauser/.bash_history:grep -i umask /etc/login.defs

```

</details>

#### V-258046 — Changed

**RHEL 9 system accounts must not have an interactive login shell.**

STIG ID: `RHEL-09-411035`. Severity: medium.
Rule ID: `SV-258046r991589_rule` → `SV-258046r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,14 +1,9 @@
-Verify that system accounts must not have an interactive login shell with the following command:
+Verify that RHEL 9 system accounts do not have an interactive login shell.

-$ awk -F: '($3<1000){print $1 ":" $3 ":" $7}' /etc/passwd
+Run the following command to list any system account (UID < 1000) that has an interactive shell, excluding
+authorized system utility accounts (root, sync, shutdown, halt):

-root:0:/bin/bash
-bin:1:/sbin/nologin
-daemon:2:/sbin/nologin
-adm:3:/sbin/nologin
-lp:4:/sbin/nologin
+$ $ awk -F: '(($3 > 0 && $3 < 1000) && $1 !~ /^(halt|sync|shutdown)$/ && $7 !~ /(nologin|false)$/) {print $1
+":" $3 ":" $7}' /etc/passwd

-Identify the system accounts from this listing that do not have a nologin shell.
-
-If any system account (other than the root account) has a login shell and it is not documented with the
-information system security officer (ISSO), this is a finding.
+If the command returns any output, this is a finding.
```

**Fix**

```diff
@@ -8,7 +8,2 @@

-Replace <user> with the user that has a login shell.
-
-$ sudo usermod --shell /sbin/nologin <user>
-
-Do not perform the steps in this section on the root account. Doing so will cause the system to become
-inaccessible.
+$ sudo usermod --shell /usr/sbin/nologin <user>
```

</details>

#### V-258052 — Changed

**All RHEL 9 local interactive user home directories defined in the /etc/passwd file must exist.**

STIG ID: `RHEL-09-411065`. Severity: medium.
Rule ID: `SV-258052r991589_rule` → `SV-258052r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,6 +4,10 @@

-user 'mailnull': directory 'var/spool/mqueue' does not exist
+The output should not return any interactive (human) users.

-The output should not return any interactive users.
+Ask the system administrator (SA) if any users found without home directories are local interactive users.
+If the SA is unable to provide a response, check for users with a user identifier (UID) of 1000 or greater
+with the following command:

-If users home directory does not exist, this is a finding.
+$ awk -F: '($3>=1000)&&($1!="nobody"){print $1 ":" $3}' /etc/passwd
+
+If any interactive users do not have a home directory assigned, this is a finding.
```

**Fix**

```diff
@@ -3,8 +3,8 @@

-Note: The example will be for the user wadea, who has a home directory of "/home/wadea", a user identifier
-(UID) of "wadea", and a Group Identifier (GID) of "users assigned" in "/etc/passwd".
+Note: The example will be for the user disauser, who has a home directory of "/home/disauser", a user
+identifier (UID) of "disauser", and a group identifier (GID) of "users assigned" in "/etc/passwd".

-$ sudo mkdir /home/wadea
-$ sudo chown wadea /home/wadea
-$ sudo chgrp users /home/wadea
-$ sudo chmod 0750 /home/wadea
+$ sudo mkdir /home/disauser
+$ sudo chown disauser /home/disauser
+$ sudo chgrp users /home/disauser
+$ sudo chmod 0750 /home/disauser
```

</details>

#### V-258053 — Changed

**All RHEL 9 local interactive user home directories must be group-owned by the home directory owner's primary group.**

STIG ID: `RHEL-09-411070`. Severity: medium.
Rule ID: `SV-258053r991589_rule` → `SV-258053r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -5,7 +5,7 @@
 Evidence of interactive use may be obtained from a number of log files containing system logon information.
-The returned directory "/home/wadea" is used as an example.
+The returned directory "/home/disauser" is used as an example.

-$ sudo ls -ld $(awk -F: '($3>=1000)&&($7 !~ /nologin/){print $6}' /etc/passwd)
-
-drwxr-x--- 2 wadea admin 4096 Jun 5 12:41 wadea
+$ getent passwd | awk -F: '($3>=1000 && $7!~/(nologin|false)$/){printf "User: %-15s Primary GID: %-5s Home:
+%s\n", $1, $4, $6}'
+User: disauser        Primary GID: 1002  Home: /home/disauser

@@ -13,5 +13,4 @@

-$ sudo grep $(grep wadea /etc/passwd | awk -F: ‘{print $4}') /etc/group
-
-admin:x:250:wadea,jonesj,jacksons
+$ stat -c "Directory: %n --> Actual GID: %g (%G)" /home/disauser
+Directory: /home/disauser --> Actual GID: 1002 (disauser)

```

**Fix**

```diff
@@ -3,5 +3,5 @@

-Note: The example will be for the user "wadea", who has a home directory of "/home/wadea", and has a primary
-group of users.
+Note: The example will be for the user "disauser", who has a home directory of "/home/disauser", and has a
+primary group of users.

-$ sudo chgrp users /home/wadea
+$ sudo chgrp users /home/disauser
```

</details>

#### V-258072 — Changed

**RHEL 9 must define default permissions for the bash shell.**

STIG ID: `RHEL-09-412055`. Severity: medium.
Rule ID: `SV-258072r1045155_rule` → `SV-258072r1184320_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,4 +2,4 @@

-Note: If the value of the "umask" parameter is set to "000" "/etc/bashrc" file, the Severity is raised to a
-CAT I.
+Note: If the value of the "umask" parameter is set to "000" in the "/etc/bashrc" file, the Severity is raised
+to a CAT I.

```

</details>

#### V-258073 — Changed

**RHEL 9 must define default permissions for the c shell.**

STIG ID: `RHEL-09-412060`. Severity: medium.
Rule ID: `SV-258073r1045157_rule` → `SV-258073r1184322_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,4 +2,4 @@

-Note: If the value of the "umask" parameter is set to "000" "/etc/csh.cshrc" file, the Severity is raised to a
- CAT I.
+Note: If the value of the "umask" parameter is set to "000" in the "/etc/csh.cshrc" file, the Severity is
+raised to a CAT I.

```

</details>

#### V-258075 — Changed

**RHEL 9 must define default permissions for the system default profile.**

STIG ID: `RHEL-09-412070`. Severity: medium.
Rule ID: `SV-258075r991590_rule` → `SV-258075r1184324_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,4 +2,4 @@

-Note: If the value of the "umask" parameter is set to "000" "/etc/profile" file, the Severity is raised to a
-CAT I.
+Note: If the value of the "umask" parameter is set to "000" in the "/etc/profile" file, the Severity is raised
+ to a CAT I.

```

</details>

#### V-258077 — Changed

**RHEL 9 must terminate idle user sessions.**

STIG ID: `RHEL-09-412080`. Severity: medium.
Rule ID: `SV-258077r1014874_rule` → `SV-258077r1262114_rule`.
CCI: CCI-001133.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-10][cw-sc-10].
- **Baseline / control determinations:** `sc-10`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-10`: `deployment-configured`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,7 +1,10 @@
-Verify that RHEL 9 logs out sessions that are idle for 15 minutes with the following command:
+Note: For cloud-hosted systems where "ClientAliveInterval" (V-257996) is configured, this setting is not
+applicable.

-$ sudo grep -i ^StopIdleSessionSec /etc/systemd/logind.conf
+Verify RHEL 9 logs out sessions that are idle for 10 minutes with the following command:

-StopIdleSessionSec=900
+$ systemd-analyze cat-config systemd/logind.conf | grep StopIdleSessionSec
+#StopIdleSessionSec=infinity
+StopIdleSessionSec=600

-If "StopIdleSessionSec" is not configured to "900" seconds, this is a finding.
+If "StopIdleSessionSec" is not configured to "600" seconds, this is a finding.
```

**Fix**

```diff
@@ -1,9 +1,15 @@
-Configure RHEL 9 to log out idle sessions by editing the /etc/systemd/logind.conf file with the following
-line:
+Configure RHEL 9 to log out idle sessions.

-StopIdleSessionSec=900
+Create the directory if necessary:

-The "logind" service must be restarted for the changes to take effect. To restart the "logind" service, run
-the following command:
+$ mkdir -p /etc/systemd/logind.conf.d/

-$ sudo systemctl restart systemd-logind
+Create a *.conf file in /etc/systemd/logind.conf.d/ with the following content:
+
+[Login]
+StopIdleSessionSec=600
+KillUserProcesses=no
+
+Restart systemd-logind:
+
+$ systemctl restart systemd-logind
```

</details>

#### V-258084 — Changed

**RHEL 9 must require reauthentication when using the "sudo" command.**

STIG ID: `RHEL-09-432015`. Severity: medium.
Rule ID: `SV-258084r1050789_rule` → `SV-258084r1262115_rule`.
CCI: CCI-004895, CCI-002038.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-11][cw-ia-11], `SC-11` (no committed crosswalk page).
- **Baseline / control determinations:** `ia-11`: `research-required` (undetermined); `sc-11`: absent from current control baseline.
- **Reference image decisions to review:** `ia-11`: `not-applicable`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,3 +4,2 @@
 $ sudo grep -ir 'timestamp_timeout' /etc/sudoers /etc/sudoers.d/
-
 /etc/sudoers:Defaults timestamp_timeout=0
@@ -9,3 +8,3 @@

-If "timestamp_timeout" is set to a negative number, is commented out, or no results are returned, this is a
-finding.
+If "timestamp_timeout" is set to a value other than "0" (including negative numbers), is commented out, or is
+missing entirely, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Configure RHEL 9 to reauthenticate "sudo" commands after the specified timeout:
+Configure RHEL 9 to reauthenticate every invocation of the "sudo" command.

@@ -5 +5,3 @@
 Defaults timestamp_timeout=0
+
+Remove any duplicate definitions.
```

</details>

#### V-258086 — Changed

**RHEL 9 must require users to reauthenticate for privilege escalation.**

STIG ID: `RHEL-09-432025`. Severity: medium.
Rule ID: `SV-258086r1050789_rule` → `SV-258086r1102063_rule`.
CCI: CCI-004895, CCI-002038.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-11][cw-ia-11], `SC-11` (no committed crosswalk page).
- **Baseline / control determinations:** `ia-11`: `research-required` (undetermined); `sc-11`: absent from current control baseline.
- **Reference image decisions to review:** `ia-11`: `not-applicable`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,3 +2,3 @@

-$ sudo grep -ir '!authenticate' /etc/sudoers /etc/sudoers.d/
+$ sudo egrep -iR '!authenticate' /etc/sudoers /etc/sudoers.d/

```

</details>

#### V-258087 — Changed

**RHEL 9 must restrict privilege elevation to authorized personnel.**

STIG ID: `RHEL-09-432030`. Severity: medium.
Rule ID: `SV-258087r1045177_rule` → `SV-258087r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,3 +2,3 @@

-$ sudo grep -riw ALL /etc/sudoers /etc/sudoers.d/
+$ sudo grep -iwR 'ALL' /etc/sudoers /etc/sudoers.d/ | grep -v '#'

```

</details>

#### V-258088 — Changed

**RHEL 9 must restrict the use of the "su" command.**

STIG ID: `RHEL-09-432035`. Severity: medium.
Rule ID: `SV-258088r1050789_rule` → `SV-258088r1155643_rule`.
CCI: CCI-004895, CCI-002165, CCI-002038.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-3(4)][cw-ac-3.4], [IA-11][cw-ia-11], `SC-11` (no committed crosswalk page).
- **Baseline / control determinations:** `ac-3.4`: absent from current control baseline; `ia-11`: `research-required` (undetermined); `sc-11`: absent from current control baseline.
- **Reference image decisions to review:** `ia-11`: `not-applicable`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,4 +1,5 @@
-Verify that RHEL 9 requires uses to be members of the "wheel" group with the following command:
+Verify RHEL 9 includes users who require privilege escalation to be members of the "wheel" group with the
+following command:

-$ grep pam_wheel /etc/pam.d/su
+$ sudo grep pam_wheel /etc/pam.d/su

@@ -6,2 +7,2 @@

-If a line for "pam_wheel.so" does not exist, or is commented out, this is a finding.
+If a line for "pam_wheel.so" does not exist, or the line is commented out, this is a finding.
```

</details>

#### V-258091 — Changed

**RHEL 9 must ensure the password complexity module in the system-auth file is configured for three retries or less.**

STIG ID: `RHEL-09-611010`. Severity: medium.
Rule ID: `SV-258091r1045185_rule` → `SV-258091r1208774_rule`.
CCI: CCI-004066, CCI-000192.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
- **CCI findings:** old: CCI-000192: no Rev 5 reference; Rev 4 IA-5 (1) (a); candidate: CCI-000192: no Rev 5 reference; Rev 4 IA-5 (1) (a).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "on the system.\n\nRHEL 9 uses \"pwquality\" as a mechanism to enforce password complexity. This is set in both:\n/etc/pam.d/password-auth\n/etc/pam.d/system-auth\n\nBy limiting the "
+ "on the system.\n\nBy limiting the "
```

</details>

#### V-258106 — Changed

**RHEL 9 must require users to provide a password for privilege escalation.**

STIG ID: `RHEL-09-611085`. Severity: medium.
Rule ID: `SV-258106r1050789_rule` → `SV-258106r1102061_rule`.
CCI: CCI-004895, CCI-002038.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-11][cw-ia-11], `SC-11` (no committed crosswalk page).
- **Baseline / control determinations:** `ia-11`: `research-required` (undetermined); `sc-11`: absent from current control baseline.
- **Reference image decisions to review:** `ia-11`: `not-applicable`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,6 +2,6 @@

-$ sudo grep -ri nopasswd /etc/sudoers /etc/sudoers.d/
+$ sudo grep -iR 'NOPASSWD' /etc/sudoers /etc/sudoers.d/

 If any occurrences of "NOPASSWD" are returned from the command and have not been documented with the
-information system security officer (ISSO) as an organizationally defined administrative group using MFA, this
- is a finding.
+information system security officer (ISSO) as an organizationally defined administrative group using
+multifactor authentication (MFA), this is a finding.
```

</details>

#### V-258107 — Changed

**RHEL 9 passwords must be created with a minimum of 15 characters.**

STIG ID: `RHEL-09-611090`. Severity: medium.
Rule ID: `SV-258107r1045218_rule` → `SV-258107r1262152_rule`.
CCI: CCI-004066, CCI-000205.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
- **CCI findings:** old: CCI-000205: no Rev 5 reference; Rev 4 IA-5 (1) (a); candidate: CCI-000205: no Rev 5 reference; Rev 4 IA-5 (1) (a).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "15-character minimum.\n\nThe DOD minimum password requirement"
+ "15-character minimum.\n\nThe DoW minimum password requirement"
```

</details>

#### V-258116 — Changed

**RHEL 9 must be configured so that user and group account administration utilities are configured to store only encrypted representations of passwords.**

STIG ID: `RHEL-09-611135`. Severity: medium.
Rule ID: `SV-258116r1045240_rule` → `SV-258116r1262116_rule`.
CCI: CCI-004062, CCI-000196.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
- **CCI findings:** old: CCI-000196: no Rev 5 reference; Rev 4 IA-5 (1) (c); candidate: CCI-000196: no Rev 5 reference; Rev 4 IA-5 (1) (c).

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,3 @@
+Note: If the libuser package is not installed, this requirement is Not Applicable.
+
 Verify the user and group account administration utilities are configured to store only encrypted
@@ -4,3 +6,2 @@
 $ grep crypt_style /etc/libuser.conf
-
 crypt_style = sha512
```

</details>

#### V-258121 — Changed

**RHEL 9 must use the common access card (CAC) smart card driver.**

STIG ID: `RHEL-09-611160`. Severity: medium.
Rule ID: `SV-258121r1045243_rule` → `SV-258121r1155682_rule`.
CCI: CCI-000764, CCI-000766, CCI-000765, CCI-004045, CCI-001941, CCI-000767, CCI-000768, CCI-000770, CCI-001942.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2][cw-ia-2], [IA-2(1)][cw-ia-2.1], [IA-2(2)][cw-ia-2.2], [IA-2(5)][cw-ia-2.5], [IA-2(8)][cw-ia-2.8].
- **Baseline / control determinations:** `ia-2`: `research-required` (determination); handoff: [PLT-18]; `ia-2.1`: `research-required` (determination); handoff: [PLT-13]; `ia-2.2`: `research-required` (undetermined); `ia-2.5`: `research-required` (undetermined); `ia-2.8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2`: `not-applicable`; `ia-2.1`: `not-applicable`; `ia-2.2`: `not-applicable`; `ia-2.5`: `not-applicable`; `ia-2.8`: `not-applicable`.
- **CCI findings:** old: CCI-000767: no Rev 5 reference; Rev 4 IA-2 (3); CCI-000768: no Rev 5 reference; Rev 4 IA-2 (4); CCI-000770: no Rev 5 reference; Rev 4 IA-2 (5); CCI-001942: no Rev 5 reference; Rev 4 IA-2 (9); candidate: CCI-000767: no Rev 5 reference; Rev 4 IA-2 (3); CCI-000768: no Rev 5 reference; Rev 4 IA-2 (4); CCI-000770: no Rev 5 reference; Rev 4 IA-2 (5); CCI-001942: no Rev 5 reference; Rev 4 IA-2 (9).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,4 +1,4 @@
-Verify that RHEL loads the CAC driver with the following command:
+Verify RHEL loads the CAC driver with the following command:

-$ sudo opensc-tool --get-conf-entry app:default:card_driver cac
+$ sudo opensc-tool --get-conf-entry app:default:card_drivers

```

**Fix**

```diff
@@ -2,3 +2,3 @@

-$ sudo opensc-tool --set-conf-entry app:default:card_driver:cac
+$ sudo opensc-tool --set-conf-entry app:default:card_drivers:cac

```

</details>

#### V-258122 — Changed

**RHEL 9 must enable certificate based smart card authentication.**

STIG ID: `RHEL-09-611165`. Severity: medium.
Rule ID: `SV-258122r1045246_rule` → `SV-258122r1268242_rule`.
CCI: CCI-000765, CCI-004046, CCI-004047, CCI-001948.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2(1)][cw-ia-2.1], [IA-2(6)][cw-ia-2.6].
- **Baseline / control determinations:** `ia-2.1`: `research-required` (determination); handoff: [PLT-13]; `ia-2.6`: absent from current control baseline.
- **Reference image decisions to review:** `ia-2.1`: `not-applicable`.
- **CCI findings:** old: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11); candidate: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "privileged user. The DOD Common Access Card (CAC) with DOD-approved PKI is an"
+ "privileged user. The DoW Common Access Card (CAC) with DoW-approved PKI is an"
```

</details>

#### V-258123 — Changed

**RHEL 9 must implement certificate status checking for multifactor authentication.**

STIG ID: `RHEL-09-611170`. Severity: medium.
Rule ID: `SV-258123r1045248_rule` → `SV-258123r1268242_rule`.
CCI: CCI-004046, CCI-001954, CCI-001948.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2(6)][cw-ia-2.6], [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.12`: `research-required` (undetermined); `ia-2.6`: absent from current control baseline.
- **Reference image decisions to review:** `ia-2.12`: `not-applicable`.
- **CCI findings:** old: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11); candidate: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11).

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "such as a DOD common access card"
+ "such as a DoW common access card"
- "card and the DOD CAC.\n\nRHEL 9"
+ "card and the DoW CAC.\n\nRHEL 9"
```

**Check**

```diff
@@ -1,3 +1,3 @@
 Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor
-authentication method, this requirement is Not Applicable.
+authentication method, this requirement is not applicable.

@@ -6,5 +6,5 @@

-$ sudo grep -ir certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/ | grep -v "^#"
+$ sudo grep -sir certificate_verification /etc/sssd/sssd.conf /etc/sssd/conf.d/ | grep -v "^#"

-certificate_verification = ocsp_dgst=sha512
+/etc/sssd/conf.d/certificate_verification:certificate_verification = ocsp_dgst=sha512

```

</details>

#### V-258125 — Changed

**The pcscd socket on RHEL 9 must be active.**

STIG ID: `RHEL-09-611180`. Severity: medium.
Rule ID: `SV-258125r1045253_rule` → `SV-258125r1268242_rule`.
CCI: CCI-004046, CCI-001948.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2(6)][cw-ia-2.6].
- **Baseline / control determinations:** `ia-2.6`: absent from current control baseline.
- **CCI findings:** old: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11); candidate: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11).

**Changed fields:** title.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "The pcscd service on RHEL 9"
+ "The pcscd socket on RHEL 9"
```

</details>

#### V-258126 — Changed

**RHEL 9 must have the opensc package installed.**

STIG ID: `RHEL-09-611185`. Severity: medium.
Rule ID: `SV-258126r1045255_rule` → `SV-258126r1268242_rule`.
CCI: CCI-004046, CCI-001953, CCI-001948.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2(6)][cw-ia-2.6], [IA-2(12)][cw-ia-2.12].
- **Baseline / control determinations:** `ia-2.12`: `research-required` (undetermined); `ia-2.6`: absent from current control baseline.
- **Reference image decisions to review:** `ia-2.12`: `not-applicable`.
- **CCI findings:** old: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11); candidate: CCI-001948: no Rev 5 reference; Rev 4 IA-2 (11).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "unauthorized access.\n\nThe DOD has mandated the"
+ "unauthorized access.\n\nThe DoW has mandated the"
```

</details>

#### V-258127 — Changed

**RHEL 9, for PKI-based authentication, must enforce authorized access to the corresponding private key.**

STIG ID: `RHEL-09-611190`. Severity: medium.
Rule ID: `SV-258127r958450_rule` → `SV-258127r1155648_rule`.
CCI: CCI-000186.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(2)][cw-ia-5.2].
- **Baseline / control determinations:** `ia-5.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.2`: `not-applicable`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,4 @@
+Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication
+method, this requirement is not applicable.
+
 Verify the SSH private key files have a passcode.
@@ -6,2 +9,5 @@

-If the contents of the key are displayed, this is a finding.
+The expected output is a password prompt:
+ "Enter passphrase:"
+
+If the password prompt is not displayed, and the contents of the key are displayed, this is a finding.
```

**Fix**

```diff
@@ -2,2 +2,2 @@

-$ sudo ssh-keygen -n [passphrase]
+$ sudo ssh-keygen -N [passphrase]
```

</details>

#### V-258128 — Changed

**RHEL 9 must require authentication to access emergency mode.**

STIG ID: `RHEL-09-611195`. Severity: medium.
Rule ID: `SV-258128r958472_rule` → `SV-258128r1268226_rule`.
CCI: CCI-000213.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-3][cw-ac-3].
- **Baseline / control determinations:** `ac-3`: `research-required` (determination); handoff: [PLT-06].
- **Reference image decisions to review:** `ac-3`: `deployment-configured`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "issued certificates by DOD-approved PKIs, all DOD systems (e.g., web"
+ "issued certificates by DoW-approved PKIs, all DoW systems (e.g., web"
```

**Check**

```diff
@@ -1,8 +1,14 @@
-Verify that RHEL 9 requires authentication for emergency mode with the following command:
+Verify RHEL 9 requires authentication for emergency mode with the following command:

 $ grep sulogin /usr/lib/systemd/system/emergency.service
-
 ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency

-If this line is not returned, or is commented out, this is a finding. If the output is different, this is a
-finding.
+If the line is not returned from the default systemd file, use the following command to look for modifications
+ to the emergency.service:
+
+$ grep sulogin /etc/systemd/system/emergency.service.d/*.conf
+
+If the line is not returned from either location this is a finding.
+
+Note: The configuration setting can only be in either the default location, or in the drop in file, not both
+locations.
```

**Fix**

```diff
@@ -2,4 +2,18 @@

-Add or modify the following line in the "/usr/lib/systemd/system/emergency.service" file:
+Create a directory for supplementary configuration files:

+$ sudo mkdir /etc/systemd/system/emergency.service.d/
+
+Create a new file:
+
+$ sudo vi /etc/systemd/system/emergency.service.d/emergency.service.conf
+
+Add these lines to the new file:
+
+[Service]
+ExecStart=
 ExecStart=-/usr/lib/systemd/systemd-sulogin-shell emergency
+
+Apply changes to unit files without rebooting the system:
+
+$ sudo systemctl daemon-reload
```

</details>

#### V-258129 — Changed

**RHEL 9 must require authentication to access single-user mode.**

STIG ID: `RHEL-09-611200`. Severity: medium.
Rule ID: `SV-258129r958472_rule` → `SV-258129r1268226_rule`.
CCI: CCI-000213.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-3][cw-ac-3].
- **Baseline / control determinations:** `ac-3`: `research-required` (determination); handoff: [PLT-06].
- **Reference image decisions to review:** `ac-3`: `deployment-configured`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "issued certificates by DOD-approved PKIs, all DOD systems (e.g., web"
+ "issued certificates by DoW-approved PKIs, all DoW systems (e.g., web"
- " the bootloader password."
+ " the bootloader password.\n\nTo modify properties, such as dependencies or timeouts, of a service that is handled by a SysV initscript, do not modify the initscript itself. Instead, create a systemd drop-in configuration file for the service. Then manage this service in the same way as a normal systemd service.\n\nFor example, to extend the configuration of the network service, do not modify the /etc/rc.d/init.d/network initscript file. Instead, create new directory /etc/systemd/system/network.service.d/ and a systemd drop-in file /etc/systemd/system/network.service.d/my_config.conf. Then, put the modified values into the drop-in file. Note: systemd knows the network service as network.service, which is why the created directory must be called \"network.service.d\"."
```

**Check**

```diff
@@ -1,7 +1,14 @@
-Verify that RHEL 9 requires authentication for single-user mode with the following command:
+Verify RHEL 9 requires authentication for single-user mode with the following command:

 $ grep sulogin /usr/lib/systemd/system/rescue.service
-
 ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue

-If this line is not returned, or is commented out, this is a finding.
+If the line is not returned from the default systemd file, use the following command to look for modifications
+ to the rescue.service:
+
+$ grep sulogin /etc/systemd/system/rescue.service.d/*.conf
+
+If the line is not returned from either location this is a finding.
+
+Note: The configuration setting can only be in either the default location, or in the drop in file, not both
+locations.
```

**Fix**

```diff
@@ -2,4 +2,18 @@

-Add or modify the following line in the "/usr/lib/systemd/system/rescue.service" file:
+Create a directory for supplementary configuration files:

+$ sudo mkdir /etc/systemd/system/rescue.service.d/
+
+Create a new file:
+
+$ sudo vi etc/systemd/system/rescue.service.d/rescue.service.conf
+
+Add these lines to the new file:
+
+[Service]
+ExecStart=
 ExecStart=-/usr/lib/systemd/systemd-sulogin-shell rescue
+
+Apply changes to unit files without rebooting the system:
+
+$ sudo systemctl daemon-reload
```

</details>

#### V-258131 — Changed

**RHEL 9, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.**

STIG ID: `RHEL-09-631010`. Severity: medium.
Rule ID: `SV-258131r1015125_rule` → `SV-258131r1262156_rule`.
CCI: CCI-000185, CCI-004068, CCI-001991.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(2)][cw-ia-5.2].
- **Baseline / control determinations:** `ia-5.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.2`: `not-applicable`.
- **CCI findings:** old: CCI-001991: no Rev 5 reference; Rev 4 IA-5 (2) (d); candidate: CCI-001991: no Rev 5 reference; Rev 4 IA-5 (2) (d).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,4 @@
+Note: If the system administrator demonstrates the use of an approved alternate multifactor authentication
+method, this requirement is not applicable.
+
 Verify RHEL 9 for PKI-based authentication has valid certificates by constructing a certification path (which
@@ -14,3 +17,3 @@
         Signature Algorithm: sha256WithRSAEncryption
-        Issuer: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3
+        Issuer: C = US, O = U.S. Government, OU = DoW, OU = PKI, CN = DoD Root CA 3
         Validity
@@ -18,3 +21,3 @@
         Not After: Dec 30 18:46:41 2029 GMT
-        Subject: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3
+        Subject: C = US, O = U.S. Government, OU = DoW, OU = PKI, CN = DoD Root CA 3
         Subject Public Key Info:
@@ -22,3 +25,3 @@

-If the root CA file is not a DOD-issued certificate with a valid date and installed in the
+If the root CA file is not a DoW-issued certificate with a valid date and installed in the
 "/etc/sssd/pki/sssd_auth_ca_db.pem" location, this is a finding.
```

**Fix**

```diff
@@ -4,3 +4,3 @@
 Obtain a valid copy of the DOD root CA file from the PKI CA certificate bundle from cyber.mil and copy the
-DoD_PKE_CA_chain.pem into the following file:
+DoW_PKE_CA_chain.pem into the following file:
 /etc/sssd/pki/sssd_auth_ca_db.pem
```

</details>

#### V-258132 — Changed

**RHEL 9 must map the authenticated identity to the user or group account for PKI-based authentication.**

STIG ID: `RHEL-09-631015`. Severity: medium.
Rule ID: `SV-258132r1045260_rule` → `SV-258132r1134929_rule`.
CCI: CCI-000187.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(2)][cw-ia-5.2].
- **Baseline / control determinations:** `ia-5.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.2`: `not-applicable`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1 +1,4 @@
+Note: If the system administrator (SA) demonstrates the use of an approved alternate multifactor
+authentication method, this requirement is not applicable.
+
 Verify the certificate of the user or group is mapped to the corresponding user or group in the "sssd.conf"
@@ -10,4 +13,3 @@

-If the certmap section does not exist, ask the system administrator (SA) to indicate how certificates are
-mapped to accounts.
+If the certmap section does not exist, ask the SA to indicate how certificates are mapped to accounts.

```

</details>

#### V-258134 — Changed

**RHEL 9 must have the AIDE package installed.**

STIG ID: `RHEL-09-651010`. Severity: medium.
Rule ID: `SV-258134r1045265_rule` → `SV-258134r1262119_rule`.
CCI: CCI-001744, CCI-002696.

- **Image criteria:** direct: None; shared-control review: [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-3(5)][cw-cm-3.5], [SI-6][cw-si-6].
- **Baseline / control determinations:** `cm-3.5`: absent from current control baseline; `si-6`: `host-inherited` (expectation); handoff: [PLT-16].

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "intrusion detection parameters.\n\nSatisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000445-GPOS-00199"
+ "intrusion detection parameters.\n\nSelection lines in the aide.conf file determine which files and directories AIDE will monitor for changes. They follow this format:\n\n<path> <rules>\n\nThe <path> specifies a file, directory or wildcard pattern to monitor.\nThe <rules>define which attributes (hashes, permissions, timestamps, etc.) to check.\n\nSatisfies: SRG-OS-000363-GPOS-00150, SRG-OS-000445-GPOS-00199"
```

**Check**

```diff
@@ -1,9 +1,18 @@
-Verify that RHEL 9 has the Advanced Intrusion Detection Environment (AIDE) package installed with the
-following command:
+Verify the file integrity tool is configured to verify ACLs.

-$ dnf list --installed aide
+Note: AIDE is highly configurable at install time. This requirement assumes the "aide.conf" file is under the
+"/etc" directory.

-Example output:
+Verify AIDE is installed with the following command:

-aide.x86_64          0.16.100.el9
+$ sudo dnf list installed aide
+
+Updating Subscription Management repositories.
+Installed Packages
+aide.x86_64                                0.16-103.el9
+@rhel-9-for-x86_64-appstream-rpms
+
+Use the following command to determine if the file is in a location other than "/etc/aide/aide.conf":
+
+$ sudo find / -name aide.conf

@@ -11,9 +20 @@
 system.
-
-If there is no application installed to perform integrity checks, this is a finding.
-
-If AIDE is installed, check if it has been initialized with the following command:
-
-$ sudo /usr/sbin/aide --check
-
-If the output is "Couldn't open file /var/lib/aide/aide.db.gz for reading", this is a finding.
```

**Fix**

```diff
@@ -5,3 +5,2 @@
 $ sudo dnf install aide
-
 Initialize AIDE:
@@ -9,9 +8,9 @@
 $ sudo /usr/sbin/aide --init
-
 Example output:

-Start timestamp: 2023-06-05 10:09:04 -0600 (AIDE 0.16)
-AIDE initialized database at /var/lib/aide/aide.db.new.gz
+Start timestamp: 2026-07-13 11:49:19 -0400 (AIDE 0.19.2)
+AIDE successfully initialized database.
+New AIDE database written to /var/lib/aide/aide.db.new.gz

-Number of entries:      86833
+Number of entries:      186298

@@ -22,11 +21,21 @@
 /var/lib/aide/aide.db.new.gz
-  MD5      : coZUtPHhoFoeD7+k54fUvQ==
-  SHA1     : DVpOEMWJwo0uPgrKZAygIUgSxeM=
-  SHA256   : EQiZH0XNEk001tcDmJa+5STFEjDb4MPE
-             TGdBJ/uvZKc=
-  SHA512   : 86KUqw++PZhoPK0SZvT3zuFq9yu9nnPP
-             toei0nENVELJ1LPurjoMlRig6q69VR8l
-             +44EwO9eYyy9nnbzQsfG1g==
+ SHA256    : StfQ7hBYTf83ZEBRy7I+ufhA4Ewhdpsg
+             0LOAvlSGddY=
+ SHA512    : Vo8jkWTpcRoBfjf3TFcYqANkbpMaol16
+             2SjE+6gnWFd5qqM6tQYUZu4TiKCIOqnd
+             SM6thAjSZbsKluqI7aHDNQ==
+ STRIBOG256: VEslFSImVozED21UckdDaw2hmgVJawCC
+             FT+rBRof3GA=
+ STRIBOG512: GCm3WUKXA2YRo/zAbFK8gsQBxecLgUlT
+             bTlkcEUOP8OKQhFlh4ipbVQhwh9jf/fc
+             fidl+HNDHFid62mM/ETmcg==
+ SHA512/256: cR1SOYUC3oN1R2e4UQlLW/juiZceL5E7
+             xDbRpCSK+DI=
+ SHA3-256  : GyR262apcKopWo9TOe3zLIfP9YDq7N3/
+             26ZIUpe1xt4=
+ SHA3-512  : r5xi/0GmfLv1SCZ0vb8GDWPNUicp42X7
+             ZVZD8xffjLPl7XgyefAg5VTy2qFTnbuu
+             kq83J3d3cu6eRiAzmcj6zg==

-End timestamp: 2023-06-05 10:09:57 -0600 (run time: 0m 53s)
+End timestamp: 2026-07-13 11:49:50 -0400 (run time: 0m 31s)

@@ -35,3 +44,2 @@
 $ sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
-
 Perform a manual check:
@@ -39,8 +47,6 @@
 $ sudo /usr/sbin/aide --check
-
 Example output:

-2023-06-05 10:16:08 -0600 (AIDE 0.16)
+Start timestamp: 2026-07-13 11:53:34 -0400 (AIDE 0.19.2)
 AIDE found NO differences between database and filesystem. Looks okay!!
-
 ...
```

</details>

#### V-258137 — Changed

**RHEL 9 must use cryptographic mechanisms to protect the integrity of audit tools.**

STIG ID: `RHEL-09-651025`. Severity: medium.
Rule ID: `SV-258137r1045272_rule` → `SV-258137r1102081_rule`.
CCI: CCI-001493, CCI-001494, CCI-001495, CCI-001496.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-9][cw-au-9], [AU-9(3)][cw-au-9.3].
- **Baseline / control determinations:** `au-9`: `host-inherited` (expectation); handoff: [PLT-09]; `au-9.3`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,3 +2,3 @@

-$ sudo grep /usr/bin/au /etc/aide.conf
+$ sudo grep /usr/sbin/au /etc/aide.conf

```

</details>

#### V-258140 — Changed

**RHEL 9 must have the rsyslog package installed.**

STIG ID: `RHEL-09-652010`. Severity: medium.
Rule ID: `SV-258140r1045278_rule` → `SV-258140r1106460_rule`.
CCI: CCI-000154, CCI-001851.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-4(1)][cw-au-4.1], [AU-6(4)][cw-au-6.4].
- **Baseline / control determinations:** `au-4.1`: absent from current control baseline; `au-6.4`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify that RHEL 9 has the rsyslogd package installed with the following command:
+Verify RHEL 9 has the rsyslog package installed with the following command:

@@ -8,2 +8,2 @@

-If the "rsyslogd" package is not installed, this is a finding.
+If the "rsyslog" package is not installed, this is a finding.
```

**Fix**

```diff
@@ -1,3 +1,3 @@
-The rsyslogd package can be installed with the following command:
+Install the rsyslog package with the following command:

-$ sudo dnf install rsyslogd
+$ sudo dnf install rsyslog
```

</details>

#### V-258143 — Changed

**RHEL 9 must be configured so that the rsyslog daemon does not accept log messages from other servers unless the server is being used for log aggregation.**

STIG ID: `RHEL-09-652025`. Severity: medium.
Rule ID: `SV-258143r1045283_rule` → `SV-258143r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,34 +1,18 @@
-Verify that RHEL 9 is not configured to receive remote logs using rsyslog with the following commands:
+Note: If the system administrator (SA) can demonstrate that another tool (e.g., SPLUNK) is being used to
+manage log off-load and aggregation in lieu of rsyslog, this is not applicable.

-$ grep -i modload /etc/rsyslog.conf /etc/rsyslog.d/*
+Verify RHEL 9 is not configured to receive remote logs using rsyslog with the following command:

-$ModLoad imtcp
-$ModLoad imrelp
-$ModLoad imudp
+$ ss -tulnp | grep rsyslog

-$ grep -i 'load="imtcp"' /etc/rsyslog.conf /etc/rsyslog.d/*
+If no output is returned, rsyslog is not listening for remote messages and is compliant.

-$ grep -i 'load="imrelp"' /etc/rsyslog.conf /etc/rsyslog.d/*
+If output appears, check for configured ports (514 is the default for syslog).

-$ grep -i serverrun /etc/rsyslog.conf /etc/rsyslog.d/*
+Check for remote logging configuration in rsyslog by examining the rsyslog configuration files:

-$InputTCPServerRun 514
-$InputRELPServerRun 514
-$InputUDPServerRun 514
+$ sudo grep -E 'InputTCPServerRun|UDPServerRun|RELPServerRun|imtcp|imudp|imrelp' /etc/rsyslog.conf
+/etc/rsyslog.d/*

-$ grep -i 'port="\S*"' /etc/rsyslog.conf /etc/rsyslog.d/*
-
-/etc/rsyslog.conf:#input(type="imudp" port="514")
-/etc/rsyslog.conf:#input(type="imtcp" port="514")
-/etc/rsyslog.conf:#Target="remote_host" Port="XXX" Protocol="tcp")
-
-If any uncommented lines are returned by the commands, rsyslog is configured to receive remote messages, and
-this is a finding.
-
-Note: An error about no files or directories from the above commands may be returned. This is not a finding.
-
-If any modules are being loaded in the "/etc/rsyslog.conf" file or in the "/etc/rsyslog.d" subdirectories, ask
- to see the documentation for the system being used for log aggregation.
-
-If the documentation does not exist or does not specify the server as a log aggregation system, this is a
-finding.
+If this command returns uncommented lines enabling network listeners, the system is accepting remote logs.  If
+ this system is not documented and authorized as a log aggregation server, this is a finding.
```

**Fix**

```diff
@@ -4,2 +4,5 @@
 following:
+InputTCPServerRun
+UDPServerRun
+RELPServerRun
 module(load="imtcp")
```

</details>

#### V-258149 — Changed

**RHEL 9 must be configured to forward audit records via TCP to a different system or media from the system being audited via rsyslog.**

STIG ID: `RHEL-09-652055`. Severity: medium.
Rule ID: `SV-258149r1045294_rule` → `SV-258149r1155580_rule`.
CCI: CCI-001851.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-4(1)][cw-au-4.1].
- **Baseline / control determinations:** `au-4.1`: absent from current control baseline.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "deletion or alteration.\n\nOffloading is a common"
+ "deletion or alteration.\n\nOff-loading is a common"
- "securely encrypt and offload auditing.\n\nRsyslog provides"
+ "securely encrypt and off-load auditing.\n\nRsyslog provides"
```

**Check**

```diff
@@ -1,11 +1,14 @@
-Verify that RHEL 9 audit system offloads audit records onto a different system or media from the system being
-audited via rsyslog using TCP with the following command:
+Verify RHEL 9 audit system off-loads audit records onto a different system or media from the system being
+audited via rsyslog using TCP with the following commands:

-$ grep -i 'type="omfwd"' /etc/rsyslog.conf /etc/rsyslog.d/*.conf
+To check for legacy configuration syntax, perform the following:
+$ sudo grep -ir '@@' /etc/rsyslog.conf /etc/rsyslog.d/

-*.* action(type="omfwd" target="[remoteloggingserver]" protocol="tcp" port="[port]"
+To check for Rainer script syntax, perform the following:
+$ sudo grep -rq 'type="omfwd"' /etc/rsyslog.conf /etc/rsyslog.d/

 If a remote server is not configured, or the line is commented out, ask the system administrator (SA) to
-indicate how the audit logs are offloaded to a different system or media.
+indicate how the audit logs are off-loaded to a different system or media.

-If there is no evidence that the audit logs are being offloaded to another system or media, this is a finding.
+If there is no evidence that the audit logs are being off-loaded to another system or media, this is a
+finding.
```

**Fix**

```diff
@@ -1,5 +1,21 @@
-Configure RHEL 9 to offload audit records onto a different system or media from the system being audited via
-TCP using rsyslog by specifying the remote logging server in "/etc/rsyslog.conf"" or
-"/etc/rsyslog.d/[customfile].conf" with the name or IP address of the log aggregation server.
+Configure RHEL 9 to off-load audit records onto a different system or media from the system being audited via
+TCP using rsyslog by specifying the remote logging server in "/etc/rsyslog.conf" or
+"/etc/rsyslog.d/[customfile].conf" with the name or IP address of the log aggregation server. The following
+are examples of the configuration for the legacy syntax and for the newer Rainer script. Only one should be
+used.

-*.* @@[remoteloggingserver]:[port]"
+Using legacy '@host:port" syntax example:
+*.* @@[remoteloggingserver]:[port]
+
+Using Rainer script example:
+action(
+    type="omfwd"
+    target="logserver.example.com"
+    port="514"
+    protocol="tcp"
+    action.resumeRetryCount="-1"
+    queue.type="linkedList"
+    que.size="10000"
+)
+
+Note: The Rainer Script above does not contain the required encryption settings.
```

</details>

#### V-258150 — Changed

**RHEL 9 must use cron logging.**

STIG ID: `RHEL-09-652060`. Severity: medium.
Rule ID: `SV-258150r1045296_rule` → `SV-258150r1268251_rule`.
CCI: CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-6][cw-cm-6].
- **Baseline / control determinations:** `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify that "rsyslog" is configured to log cron events with the following command:
+Verify rsyslog is configured to log cron events with the following command:

@@ -5,14 +5,16 @@

-$ grep -s cron /etc/rsyslog.conf /etc/rsyslog.d/*.conf
+$ grep -s "cron.\*" /etc/rsyslog.conf /etc/rsyslog.d/*.conf
+/etc/rsyslog.d/99-cron-stig.conf:cron.* action(type="omfile" file="/var/log/cron")

-/etc/rsyslog.conf:*.info;mail.none;authpriv.none;cron.none /var/log/messages
-/etc/rsyslog.conf:cron.* /var/log/cron
+If the command does not return a line demonstrating logging to "/var/log/cron", perform a functional cron
+test.

-If the command does not return a response, check for cron logging all facilities with the following command:
+Inject a message into the cron logging facility with the following command:

-$ logger -p local0.info "Test message for all facilities."
+$ logger -p cron.info "STIG-TEST-CRON-LOGGING"

-Check the logs for the test message with:
+Check if it successfully wrote to the dedicated log file with the following command:

-$ sudo tail /var/log/messages
+$ sudo grep "STIG-TEST-CRON-LOGGING" /var/log/cron
+Jul 16 11:33:00 RHEL10Sim pdosadmin[33692]: STIG-TEST-CRON-LOGGING

```

**Fix**

```diff
@@ -1,3 +1,3 @@
 Configure "rsyslog" to log all cron messages by adding or updating the following line to "/etc/rsyslog.conf"
-or a configuration file in the /etc/rsyslog.d/ directory:
+or a configuration file in the "/etc/rsyslog.d/" directory:

@@ -5,3 +5,3 @@

-The rsyslog daemon must be restarted for the changes to take effect:
+Restart the rsyslog daemon for the changes to take effect:

```

</details>

#### V-258156 — Changed

**RHEL 9 must take action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity.**

STIG ID: `RHEL-09-653035`. Severity: medium.
Rule ID: `SV-258156r971542_rule` → `SV-258156r1106364_rule`.
CCI: CCI-001855.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-5(1)][cw-au-5.1].
- **Baseline / control determinations:** `au-5.1`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " storage volume reaches 75 percent utilization,"
+ " storage volume reaches a maximum of 75 percent utilization,"
- " storage capacity expansion."
+ " storage capacity expansion. The notification can be set to trigger at lower utilization thresholds at the information system security officer's (ISSO's) discretion."
```

**Check**

```diff
@@ -7,5 +7,5 @@

-If the value of the "space_left" keyword is not set to 25 percent of the storage volume allocated to audit
-logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system is
-providing real-time alerts to the SA and information system security officer (ISSO). If the "space_left" value
- is not configured to the correct value, this is a finding.
+If the value of the "space_left" keyword is not set to 25 percent or greater of the storage volume allocated
+to audit logs, or if the line is commented out, ask the system administrator (SA) to indicate how the system
+is providing real-time alerts to the SA and ISSO. If the "space_left" value is not configured to the value 25
+percent or more, this is a finding.
```

**Fix**

```diff
@@ -1,4 +1,4 @@
 Configure RHEL 9 to initiate an action to notify the SA and ISSO (at a minimum) when allocated audit record
-storage volume reaches 75 percent of the repository maximum audit record storage capacity by adding/modifying
-the following line in the /etc/audit/auditd.conf file.
+storage volume reaches (at most) 75 percent of the repository maximum audit record storage capacity by
+adding/modifying the following line in the /etc/audit/auditd.conf file.

```

</details>

#### V-258157 — Changed

**RHEL 9 must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume reaches 75 percent utilization.**

STIG ID: `RHEL-09-653040`. Severity: medium.
Rule ID: `SV-258157r971542_rule` → `SV-258157r1134932_rule`.
CCI: CCI-001855.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-5(1)][cw-au-5.1].
- **Baseline / control determinations:** `au-5.1`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** title.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "record storage volume 75 percent utilization."
+ "record storage volume reaches 75 percent utilization."
```

</details>

#### V-258158 — Changed

**RHEL 9 must take action when allocated audit record storage volume reaches 95 percent of the audit record storage capacity.**

STIG ID: `RHEL-09-653045`. Severity: medium.
Rule ID: `SV-258158r971542_rule` → `SV-258158r1263516_rule`.
CCI: CCI-001855.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-5(1)][cw-au-5.1].
- **Baseline / control determinations:** `au-5.1`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " volume reaches capacity."
+ " volume reaches capacity.\n\nWhile \"%\" is fully compliant for auditd.conf, you must account for how auditd processes it. The percentage-to-megabyte conversion occurs only when the audit daemon starts. If you dynamically resize the underlying logical volume/partition where /var/log/audit resides while the system is running, the daemon will not automatically know. You must reload it to trigger a recalculation."
```

**Check**

```diff
@@ -4,3 +4,2 @@
 $ sudo grep -w admin_space_left /etc/audit/auditd.conf
-
 admin_space_left = 5%
```

</details>

#### V-258162 — Changed

**RHEL 9 must take appropriate action when the internal event queue is full.**

STIG ID: `RHEL-09-653065`. Severity: medium.
Rule ID: `SV-258162r958754_rule` → `SV-258162r1184331_rule`.
CCI: CCI-001851.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-4(1)][cw-au-4.1].
- **Baseline / control determinations:** `au-4.1`: absent from current control baseline.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -11,3 +11,4 @@

-If there is no evidence that the transfer of the audit logs being offloaded to another system or media takes
-appropriate action if the internal event queue becomes full, this is a finding.
+If there is no evidence that the audit system is configured to off-load the audit logs to another system or
+media and if the overflow action is not set to take appropriate action if the internal event queue becomes
+full, this is a finding.
```

</details>

#### V-258167 — Changed

**RHEL 9 audit logs file must have mode 0600 or less permissive to prevent unauthorized access to the audit log.**

STIG ID: `RHEL-09-653090`. Severity: medium.
Rule ID: `SV-258167r1045306_rule` → `SV-258167r1155630_rule`.
CCI: CCI-000162, CCI-000163, CCI-000164, CCI-001314.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-9][cw-au-9], [SI-11][cw-si-11].
- **Baseline / control determinations:** `au-9`: `host-inherited` (expectation); handoff: [PLT-09]; `si-11`: `research-required` (undetermined).
- **Reference image decisions to review:** `si-11`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,3 +4,3 @@

-$ sudo grep -iw log_file /etc/audit/auditd.conf
+$ sudo grep "^log_file" /etc/audit/auditd.conf

@@ -12,3 +12,3 @@

-rw-------. 2 root root 237923 Jun 11 11:56 /var/log/audit/audit.log
+600 /var/log/audit/audit.log

```

</details>

#### V-258171 — Changed

**RHEL 9 must allow only the information system security manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.**

STIG ID: `RHEL-09-653110`. Severity: medium.
Rule ID: `SV-258171r1045308_rule` → `SV-258171r1262122_rule`.
CCI: CCI-000171.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-12][cw-au-12].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `au-12`: `image-owned`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,9 +1,14 @@
-Verify that the files in directory "/etc/audit/rules.d/" and "/etc/audit/auditd.conf" file have a mode of
-"0640" or less permissive with the following command:
+Verify that the files in the directory "/etc/audit/rules.d/" have a mode of "0600" or less permissive with the
+ following command:

-$ sudo find /etc/audit/rules.d/ /etc/audit/audit.rules /etc/audit/auditd.conf -type f -exec stat -c "%a %n" {}
- \;
+$ sudo find /etc/audit/rules.d/ -type f -name "*.rules" -exec stat -c "%a %n" {} \;
+600 /etc/audit/rules.d/audit.rules

-600 /etc/audit/rules.d/audit.rules
-640 /etc/audit/audit.rules
-640 /etc/audit/auditd.conf
+Verify that the files "/etc/audit/audit.rules" and "/etc/audit/auditd.conf" have a mode of "0600" or less
+permissive with the following command:
+
+$ sudo stat -c "%a %n" /etc/audit/audit.rules /etc/audit/auditd.conf
+600 /etc/audit/audit.rules
+600 /etc/audit/auditd.conf
+
+If any of the audit configuration files have a mode more permissive than "0600", this is a finding.
```

**Fix**

```diff
@@ -1,6 +1,8 @@
-Configure the files in directory "/etc/audit/rules.d/" and the "/etc/audit/auditd.conf" file to have a mode of
- "0640" with the following commands:
+Configure the rules files in the directory "/etc/audit/rules.d/", the "/etc/audit/audit.rules" file, and the
+"/etc/audit/auditd.conf" file to have a mode of "0600" with the following commands:

-$ sudo chmod 0640 /etc/audit/rules.d/audit.rules
-$ sudo chmod 0640 /etc/audit/rules.d/[customrulesfile].rules
-$ sudo chmod 0640 /etc/audit/auditd.conf
+$ sudo find /etc/audit/rules.d/ -type f -name "*.rules" -exec chmod 0600 {} +
+
+$ sudo chmod 0600 /etc/audit/audit.rules
+
+$ sudo chmod 0600 /etc/audit/auditd.conf
```

</details>

#### V-258173 — Changed

**RHEL 9 must allocate an audit_backlog_limit of sufficient size to capture processes that start prior to the audit daemon.**

STIG ID: `RHEL-09-653120`. Severity: low.
Rule ID: `SV-258173r991555_rule` → `SV-258173r1101933_rule`.
CCI: CCI-001464, CCI-001849.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-4][cw-au-4], [AU-14(1)][cw-au-14.1].
- **Baseline / control determinations:** `au-14.1`: absent from current control baseline; `au-4`: `host-inherited` (determination); handoff: [PLT-09].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -3,3 +3,3 @@

-$ sudo grubby --info=ALL | grep args | grep -v 'audit_backlog_limit=8192'
+$ sudo grubby --info=ALL | grep args | grep 'audit_backlog_limit'

```

</details>

#### V-258176 — Changed

**RHEL 9 must audit uses of the "execve" system call.**

STIG ID: `RHEL-09-654010`. Severity: medium.
Rule ID: `SV-258176r1045313_rule` → `SV-258176r1155595_rule`.
CCI: CCI-002233, CCI-002234.

- **Image criteria:** direct: None; shared-control review: [IMG-09], [IMG-11], [IMG-12], [IMG-13], [IMG-31], [IMG-32].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-6(8)][cw-ac-6.8], [AC-6(9)][cw-ac-6.9].
- **Baseline / control determinations:** `ac-6.8`: `image-owned` (criterion); handoff: [PLT-02]; `ac-6.9`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-6.9`: `not-applicable`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,3 +1,2 @@
-Verify that RHEL 9 is configured to audit the execution of the "execve" system call with the following
-command:
+Verify RHEL 9 is configured to audit the execution of the "execve" system call with the following command:

@@ -5,6 +4,6 @@

--a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -F key=execpriv
--a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -F key=execpriv
--a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -F key=execpriv
--a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -F key=execpriv
+-a always,exit -F arch=b32 -S execve -C uid!=euid -F euid=0 -k execpriv
+-a always,exit -F arch=b64 -S execve -C uid!=euid -F euid=0 -k execpriv
+-a always,exit -F arch=b32 -S execve -C gid!=egid -F egid=0 -k execpriv
+-a always,exit -F arch=b64 -S execve -C gid!=egid -F egid=0 -k execpriv

```

</details>

#### V-258177 — Changed

**RHEL 9 must audit all uses of the chmod, fchmod, and fchmodat system calls.**

STIG ID: `RHEL-09-654015`. Severity: medium.
Rule ID: `SV-258177r1045316_rule` → `SV-258177r1155597_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " generating audit records that are specific to the"
+ " generating audit records specific to the"
```

**Check**

```diff
@@ -1,3 +1,3 @@
-Verify that RHEL 9 is configured to audit the execution of the "chmod", "fchmod", and "fchmodat" system calls
-with the following command:
+Verify RHEL 9 is configured to audit the execution of the "chmod", "fchmod", and "fchmodat" system calls with
+the following command:

```

</details>

#### V-258178 — Changed

**RHEL 9 must audit all uses of the chown, fchown, fchownat, and lchown system calls.**

STIG ID: `RHEL-09-654020`. Severity: medium.
Rule ID: `SV-258178r1045319_rule` → `SV-258178r1155599_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** discussion, check.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " generating audit records that are specific to the"
+ " generating audit records specific to the"
```

**Check**

```diff
@@ -1,3 +1,3 @@
-Verify that RHEL 9 is configured to audit the execution of the  "chown", "fchown", "fchownat", and "lchown"
-system calls with the following command:
+Verify RHEL 9 is configured to audit the execution of the  "chown", "fchown", "fchownat", and "lchown" system
+calls with the following command:

```

</details>

#### V-258187 — Changed

**RHEL 9 must audit all uses of the rename, unlink, rmdir, renameat, and unlinkat system calls.**

STIG ID: `RHEL-09-654065`. Severity: medium.
Rule ID: `SV-258187r1045346_rule` → `SV-258187r1155603_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,3 +1,3 @@
-Verify that RHEL 9 is configured to audit successful/unsuccessful attempts to use the "rename", "unlink",
-"rmdir", "renameat", and "unlinkat" system calls with the following command:
+Verify RHEL 9 is configured to audit successful/unsuccessful attempts to use the "rename", "unlink", "rmdir",
+"renameat", and "unlinkat" system calls with the following command:

```

</details>

#### V-258188 — Changed

**RHEL 9 must audit all uses of the truncate, ftruncate, creat, open, openat, and open_by_handle_at system calls.**

STIG ID: `RHEL-09-654070`. Severity: medium.
Rule ID: `SV-258188r1045349_rule` → `SV-258188r1155605_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,3 +1,3 @@
-Verify that RHEL 9 is configured to audit successful/unsuccessful attempts to use the "truncate", "ftruncate",
- "creat", "open", "openat", and "open_by_handle_at" system calls with the following command:
+Verify RHEL 9 is configured to audit successful/unsuccessful attempts to use the "truncate", "ftruncate",
+"creat", "open", "openat", and "open_by_handle_at" system calls with the following command:

```

</details>

#### V-258189 — Changed

**RHEL 9 must audit all uses of the delete_module system call.**

STIG ID: `RHEL-09-654075`. Severity: medium.
Rule ID: `SV-258189r1045352_rule` → `SV-258189r1155607_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify that RHEL 9 is configured to audit the execution of the "delete_module" system call with the following
+Verify RHEL 9 is configured to audit the execution of the "delete_module" system call with the following
 command:
```

</details>

#### V-258190 — Changed

**RHEL 9 must audit all uses of the init_module and finit_module system calls.**

STIG ID: `RHEL-09-654080`. Severity: medium.
Rule ID: `SV-258190r1045355_rule` → `SV-258190r1155609_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,3 +1,3 @@
-Verify that RHEL 9 is configured to audit the execution of the "init_module" and "finit_module" system calls
-with the following command:
+Verify RHEL 9 is configured to audit the execution of the "init_module" and "finit_module" system calls with
+the following command:

```

</details>

#### V-258194 — Changed

**RHEL 9 must audit all uses of the gpasswd command.**

STIG ID: `RHEL-09-654100`. Severity: medium.
Rule ID: `SV-258194r1045367_rule` → `SV-258194r1262123_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,6 +1,6 @@
-Verify that RHEL 9 is configured to audit the execution of the "gpasswd" command with the following command:
+Verify RHEL 9 is configured to audit the execution of the "gpasswd" command with the following command:

 $ sudo auditctl -l | grep gpasswd
-
--a always,exit -S all -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-gpasswd
+-a always,exit -F arch=b32 -S execve -F path=/usr/bin/gpasswd -F perm=x -F key=identity
+-a always,exit -F arch=b64 -S execve -F path=/usr/bin/gpasswd -F perm=x -F key=identity

```

**Fix**

```diff
@@ -3,3 +3,4 @@

--a always,exit -F path=/usr/bin/gpasswd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-gpasswd
+-a always,exit -F arch=b32 -F path=/usr/bin/gpasswd -F perm=x -k identity
+-a always,exit -F arch=b64 -F path=/usr/bin/gpasswd -F perm=x -k identity

```

</details>

#### V-258198 — Changed

**RHEL 9 must audit all uses of the passwd command.**

STIG ID: `RHEL-09-654120`. Severity: medium.
Rule ID: `SV-258198r1045379_rule` → `SV-258198r1262124_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,7 +1,6 @@
-Verify RHEL 9 generates audit records for all account creations, modifications, disabling, and termination
-events that affect "/etc/gshadow" with the following command:
+Verify RHEL 9 generates audit records for all uses of the "passwd" command with the following command:

 $ sudo auditctl -l | egrep '(/usr/bin/passwd)'
-
--a always,exit -S all -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=-1 -F key=privileged-passwd
+-a always,exit -F arch=b32 -F path=/usr/bin/passwd -F perm=x -k identity
+-a always,exit -F arch=b64 -F path=/usr/bin/passwd -F perm=x -k identity

```

**Fix**

```diff
@@ -3,3 +3,4 @@

--a always,exit -F path=/usr/bin/passwd -F perm=x -F auid>=1000 -F auid!=unset -k privileged-passwd
+-a always,exit -F arch=b32 -F path=/usr/bin/passwd -F perm=x -k identity
+-a always,exit -F arch=b64 -F path=/usr/bin/passwd -F perm=x -k identity

```

</details>

#### V-258215 — Changed

**Successful/unsuccessful uses of the umount system call in RHEL 9 must generate an audit record.**

STIG ID: `RHEL-09-654205`. Severity: medium.
Rule ID: `SV-258215r1045430_rule` → `SV-258215r1155611_rule`.
CCI: CCI-000130, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,2 @@
-Verify that RHEL 9 generates an audit record for all uses of the "umount" and system call with the following
+Verify RHEL 9 generates an audit record for all uses of the "umount" and system call with the following
 command:
```

</details>

#### V-258217 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.**

STIG ID: `RHEL-09-654215`. Severity: medium.
Rule ID: `SV-258217r1045436_rule` → `SV-258217r1210919_rule`.
CCI: CCI-000018, CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-001403, CCI-001404, CCI-001405, CCI-002130, CCI-000015, CCI-002884, CCI-002132.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1], [AC-2(4)][cw-ac-2.4], [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined); `ac-2.4`: `research-required` (undetermined); `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`; `ac-2.4`: `not-applicable`; `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.
- **CCI findings:** old: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4); candidate: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4).

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "methods to a system, auditing the editing of"
+ "methods to a system. Auditing the editing of"
```

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | grep '/etc/sudoers[^.]'
-
--w /etc/sudoers -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/sudoers -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/sudoers -F perm=wa -k identity

```

**Fix**

```diff
@@ -5,3 +5,4 @@

--w /etc/sudoers -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/sudoers -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/sudoers -F perm=wa -k identity

```

</details>

#### V-258218 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.d/directory.**

STIG ID: `RHEL-09-654220`. Severity: medium.
Rule ID: `SV-258218r1045439_rule` → `SV-258218r1210920_rule`.
CCI: CCI-000018, CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-001403, CCI-001404, CCI-001405, CCI-002130, CCI-000015, CCI-002884, CCI-002132.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1], [AC-2(4)][cw-ac-2.4], [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined); `ac-2.4`: `research-required` (undetermined); `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`; `ac-2.4`: `not-applicable`; `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.
- **CCI findings:** old: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4); candidate: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4).

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "events that affect /etc/sudoers.d/ directory."
+ "events that affect /etc/sudoers.d/directory."
```

**Discussion**

```diff
- "methods to a system, auditing the editing of"
+ "methods to a system. Auditing the editing of"
```

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | grep /etc/sudoers.d
-
--w /etc/sudoers.d -p wa -k actions
+-a always,exit -F arch=b32 -F path=/etc/sudoers.d -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/sudoers.d -F perm=wa -k identity

```

**Fix**

```diff
@@ -5,3 +5,4 @@

--w /etc/sudoers.d/ -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/sudoers.d -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/sudoers.d -F perm=wa -k identity

```

</details>

#### V-258219 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group.**

STIG ID: `RHEL-09-654225`. Severity: medium.
Rule ID: `SV-258219r1015130_rule` → `SV-258219r1210921_rule`.
CCI: CCI-000018, CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-001403, CCI-001404, CCI-001405, CCI-002130, CCI-000015, CCI-002884, CCI-002132.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1], [AC-2(4)][cw-ac-2.4], [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined); `ac-2.4`: `research-required` (undetermined); `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`; `ac-2.4`: `not-applicable`; `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.
- **CCI findings:** old: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4); candidate: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | egrep '(/etc/group)'
-
--w /etc/group -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/group -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/group -F perm=wa -k identity

```

**Fix**

```diff
@@ -5,4 +5,7 @@

--w /etc/group -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/group -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/group -F perm=wa -k identity

-The audit daemon must be restarted for the changes to take effect.
+To load the rules to the kernel immediately, use the following command:
+
+$ sudo augenrules --load
```

</details>

#### V-258220 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow.**

STIG ID: `RHEL-09-654230`. Severity: medium.
Rule ID: `SV-258220r1015131_rule` → `SV-258220r1210922_rule`.
CCI: CCI-000018, CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-001403, CCI-001404, CCI-001405, CCI-002130, CCI-000015, CCI-002884, CCI-002132.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1], [AC-2(4)][cw-ac-2.4], [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined); `ac-2.4`: `research-required` (undetermined); `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`; `ac-2.4`: `not-applicable`; `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.
- **CCI findings:** old: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4); candidate: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | egrep '(/etc/gshadow)'
-
--w /etc/gshadow -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/gshadow -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/gshadow -F perm=wa -k identity

```

**Fix**

```diff
@@ -5,4 +5,7 @@

--w /etc/gshadow -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/gshadow -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/gshadow -F perm=wa -k identity

-The audit daemon must be restarted for the changes to take effect.
+To load the rules to the kernel immediately, use the following command:
+
+$ sudo augenrules --load
```

</details>

#### V-258221 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/security/opasswd.**

STIG ID: `RHEL-09-654235`. Severity: medium.
Rule ID: `SV-258221r1015132_rule` → `SV-258221r1262128_rule`.
CCI: CCI-000018, CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-001403, CCI-001404, CCI-001405, CCI-002130, CCI-000015, CCI-002884, CCI-002132.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1], [AC-2(4)][cw-ac-2.4], [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined); `ac-2.4`: `research-required` (undetermined); `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`; `ac-2.4`: `not-applicable`; `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.
- **CCI findings:** old: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4); candidate: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4).

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "events that affect /etc/opasswd."
+ "events that affect /etc/security/opasswd."
```

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | egrep '(/etc/security/opasswd)'
-
--w /etc/security/opasswd -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/security/opasswd -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/security/opasswd -F perm=wa -k identity

```

**Fix**

```diff
@@ -5,4 +5,7 @@

--w /etc/security/opasswd -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/security/opasswd -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/security/opasswd -F perm=wa -k identity

-The audit daemon must be restarted for the changes to take effect.
+To load the rules to the kernel immediately, use the following command:
+
+$ sudo augenrules --load
```

</details>

#### V-258222 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd.**

STIG ID: `RHEL-09-654240`. Severity: medium.
Rule ID: `SV-258222r1015133_rule` → `SV-258222r1210924_rule`.
CCI: CCI-000015, CCI-000018, CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-001403, CCI-001404, CCI-001405, CCI-002130, CCI-002884, CCI-001683, CCI-001684, CCI-001685, CCI-001686, CCI-002132.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1], [AC-2(4)][cw-ac-2.4], [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined); `ac-2.4`: `research-required` (undetermined); `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`; `ac-2.4`: `not-applicable`; `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.
- **CCI findings:** old: CCI-001683: no Rev 5 reference; Rev 4 AC-2 (4); CCI-001684: no Rev 5 reference; Rev 4 AC-2 (4); CCI-001685: no Rev 5 reference; Rev 4 AC-2 (4); CCI-001686: no Rev 5 reference; Rev 4 AC-2 (4); CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4); candidate: CCI-001683: no Rev 5 reference; Rev 4 AC-2 (4); CCI-001684: no Rev 5 reference; Rev 4 AC-2 (4); CCI-001685: no Rev 5 reference; Rev 4 AC-2 (4); CCI-001686: no Rev 5 reference; Rev 4 AC-2 (4); CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | egrep '(/etc/passwd)'
-
--w /etc/passwd -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/passwd -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/passwd -F perm=wa -k identity

```

**Fix**

```diff
@@ -5,4 +5,7 @@

--w /etc/passwd -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/passwd -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/passwd -F perm=wa -k identity

-The audit daemon must be restarted for the changes to take effect.
+To load the rules to the kernel immediately, use the following command:
+
+$ sudo augenrules --load
```

</details>

#### V-258223 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow.**

STIG ID: `RHEL-09-654245`. Severity: medium.
Rule ID: `SV-258223r1015134_rule` → `SV-258223r1210925_rule`.
CCI: CCI-000018, CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-001403, CCI-001404, CCI-001405, CCI-002130, CCI-000015, CCI-002884, CCI-002132.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1], [AC-2(4)][cw-ac-2.4], [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined); `ac-2.4`: `research-required` (undetermined); `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`; `ac-2.4`: `not-applicable`; `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.
- **CCI findings:** old: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4); candidate: CCI-002132: no Rev 5 reference; Rev 4 AC-2 (4).

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,7 +1,7 @@
 Verify RHEL 9 generates audit records for all account creations, modifications, disabling, and termination
-events that affect "/etc/passwd with the following command:
+events that affect "/etc/shadow" with the following command:

 $ sudo auditctl -l | egrep '(/etc/shadow)'
-
--w /etc/shadow -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/shadow -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/shadow -F perm=wa -k identity

```

**Fix**

```diff
@@ -5,4 +5,7 @@

--w /etc/shadow -p wa -k identity
+-a always,exit -F arch=b32 -F path=/etc/shadow -F perm=wa -k identity
+-a always,exit -F arch=b64 -F path=/etc/shadow -F perm=wa -k identity

-The audit daemon must be restarted for the changes to take effect.
+To load the rules to the kernel immediately, use the following command:
+
+$ sudo augenrules --load
```

</details>

#### V-258224 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/faillock.**

STIG ID: `RHEL-09-654250`. Severity: medium.
Rule ID: `SV-258224r1014988_rule` → `SV-258224r1210926_rule`.
CCI: CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | grep /var/log/faillock
-
--w /var/log/faillock -p wa -k logins
+-a always,exit -F arch=b32 -F path=/var/log/faillock -F perm=wa -F auid>=1000 -F auid!=unset -k logins
+-a always,exit -F arch=b64 -F path=/var/log/faillock -F perm=wa -F auid>=1000 -F auid!=unset -k logins

```

**Fix**

```diff
@@ -5,6 +5,7 @@

--w /var/log/faillock -p wa -k logins
+-a always,exit -F arch=b32 -F path=/var/log/faillock -F perm=wa -F auid>=1000 -F auid!=unset -k logins
+-a always,exit -F arch=b64 -F path=/var/log/faillock -F perm=wa -F auid>=1000 -F auid!=unset -k logins

-The audit daemon must be restarted for the changes to take effect.
+To load the rules to the kernel immediately, use the following command:

-$ sudo service auditd restart
+$ sudo augenrules --load
```

</details>

#### V-258225 — Changed

**RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/lastlog.**

STIG ID: `RHEL-09-654255`. Severity: medium.
Rule ID: `SV-258225r1014990_rule` → `SV-258225r1210927_rule`.
CCI: CCI-000130, CCI-000135, CCI-000169, CCI-000172, CCI-002884.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3][cw-au-3], [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [MA-4(1)][cw-ma-4.1].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3`: `research-required` (undetermined); `au-3.1`: `research-required` (undetermined); `ma-4.1`: absent from current control baseline.
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3`: `image-owned`; `au-3.1`: `deployment-configured`.

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,4 +4,4 @@
 $ sudo auditctl -l | grep /var/log/lastlog
-
--w /var/log/lastlog -p wa -k logins
+-a always,exit -F arch=b32 -F path=/var/log/lastlog -F perm=wa -F auid>=1000 -F auid!=unset -k logins
+-a always,exit -F arch=b64 -F path=/var/log/lastlog  -F perm=wa -F auid>=1000 -F auid!=unset -k logins

```

**Fix**

```diff
@@ -5,6 +5,6 @@

--w /var/log/lastlog -p wa -k logins
+-a always,exit -F arch=b32 -F path=/var/log/lastlog -F perm=wa -F auid>=1000 -F auid!=unset -k logins
+-a always,exit -F arch=b64 -F path=/var/log/lastlog  -F perm=wa -F auid>=1000 -F auid!=unset -k logins
+To load the rules to the kernel immediately, use the following command:

-The audit daemon must be restarted for the changes to take effect.
-
-$ sudo service auditd restart
+$ sudo augenrules --load
```

</details>

#### V-258230 — Changed

**RHEL 9 must enable FIPS mode.**

STIG ID: `RHEL-09-671010`. Severity: high.
Rule ID: `SV-258230r958408_rule` → `SV-258230r1268222_rule`.
CCI: CCI-000068, CCI-000877, CCI-002418, CCI-002450.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2], [MA-4][cw-ma-4], [SC-8][cw-sc-8], [SC-13][cw-sc-13].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10]; `ma-4`: `organization-inherited` (family); `sc-13`: `research-required` (undetermined); `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`; `sc-13`: `research-required`; `sc-8`: `deployment-configured`.

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "the purposes of utilizing encryption to protect"
+ "the purposes of using encryption to protect"
- "the federal government since this provides assurance"
+ "the federal government because this provides assurance"
- " tested and validated. This includes NIST FIPS-validated cryptography for the following: Provisioning digital signatures, generating cryptographic hashes, and to protect data requiring data-at-rest protections in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.\n\nSatisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000396-GPOS-00176, SRG-OS-000423-GPOS-00187, SRG-OS-000478-GPOS-00223"
+ " tested and validated.\n\nSatisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000125-GPOS-00065, SRG-OS-000250-GPOS-00093, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000396-GPOS-00176, SRG-OS-000423-GPOS-00187, SRG-OS-000478-GPOS-00223"
```

**Check**

```diff
@@ -1,7 +1,6 @@
-Verify that RHEL 9 is in FIPS mode with the following command:
+Verify RHEL 9 is in FIPS mode with the following command:

-$ sudo fips-mode-setup --check
+$ cat /proc/sys/crypto/fips_enabled
+1

-FIPS mode is enabled.
-
-If FIPS mode is not enabled, this is a finding.
+If the command does not return "1", this is a finding.
```

**Fix**

```diff
@@ -1,5 +1,4 @@
-Configure the operating system to implement FIPS mode with the following command
+Configure RHEL 9 to implement FIPS mode.

-$ sudo fips-mode-setup --enable
-
-Reboot the system for the changes to take effect.
+If this check fails on an installed system, it is a permanent finding until the system is reinstalled with
+"fips=1" during installation.
```

</details>

#### V-258231 — Changed

**RHEL 9 must employ FIPS 140-3-approved cryptographic hashing algorithms for all stored passwords.**

STIG ID: `RHEL-09-671015`. Severity: medium.
Rule ID: `SV-258231r1069375_rule` → `SV-258231r1208790_rule`.
CCI: CCI-004062, CCI-000803, CCI-000196.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(1)][cw-ia-5.1], [IA-7][cw-ia-7].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined); `ia-7`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`; `ia-7`: `not-applicable`.
- **CCI findings:** old: CCI-000196: no Rev 5 reference; Rev 4 IA-5 (1) (c); candidate: CCI-000196: no Rev 5 reference; Rev 4 IA-5 (1) (c).

**Changed fields:** title, check.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "must employ FIPS 140-3 approved cryptographic hashing algorithms"
+ "must employ FIPS 140-3-approved cryptographic hashing algorithms"
```

**Check**

```diff
@@ -2,5 +2,4 @@

-$ sudo cut -d: -f2 /etc/shadow
-
-$6$kcOnRq/5$NUEYPuyL.wghQwWssXRcLRFiiru7f5JPV6GaJhNC2aK5F3PZpE/BCCtwrxRc/AInKMNX3CdMw11m9STiql12f/
+$ sudo cut -d: -f1,2 /etc/shadow
+nsauser:$6$kcOnRq/5$NUEYPuyL.wghQwWssXRcLRFiiru7f5JPV6GaJhNC2aK5F3PZpE/BCCtwrxRc/AInKMNX3CdMw11m9STiql12f/

```

</details>

#### V-258232 — Changed

**RHEL 9 IP tunnels must use FIPS 140-3 approved cryptographic algorithms.**

STIG ID: `RHEL-09-671020`. Severity: medium → high.
Rule ID: `SV-258232r1045440_rule` → `SV-258232r1268222_rule`.
CCI: CCI-000068.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.

**Changed fields:** severity.

<details>
<summary>Field-by-field text diff</summary>

</details>

#### V-258233 — Changed

**RHEL 9 pam_unix.so module must be configured in the password-auth file to use a FIPS 140-3 approved cryptographic hashing algorithm for system authentication.**

STIG ID: `RHEL-09-671025`. Severity: medium.
Rule ID: `SV-258233r1015136_rule` → `SV-258233r1262157_rule`.
CCI: CCI-004062, CCI-000196.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
- **CCI findings:** old: CCI-000196: no Rev 5 reference; Rev 4 IA-5 (1) (c); candidate: CCI-000196: no Rev 5 reference; Rev 4 IA-5 (1) (c).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "or integrity, and DOD data may be"
+ "or integrity, and DoW data may be"
- "authentication that meets DOD requirements. This allows"
+ "authentication that meets DoW requirements. This allows"
```

</details>

#### V-258234 — Changed

**RHEL 9 must have the crypto-policies package installed.**

STIG ID: `RHEL-09-215100`. Severity: medium → high.
Rule ID: `SV-258234r1051250_rule` → `SV-258234r1184292_rule`.
CCI: CCI-002450, CCI-002890, CCI-003123.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [MA-4(6)][cw-ma-4.6], [SC-13][cw-sc-13].
- **Baseline / control determinations:** `ma-4.6`: absent from current control baseline; `sc-13`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-13`: `research-required`.

**Changed fields:** severity.

<details>
<summary>Field-by-field text diff</summary>

</details>

#### V-258236 — Changed

**RHEL 9 cryptographic policy must not be overridden.**

STIG ID: `RHEL-09-672020`. Severity: high.
Rule ID: `SV-258236r1051253_rule` → `SV-258236r1101920_rule`.
CCI: CCI-002450, CCI-002890, CCI-003123.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [MA-4(6)][cw-ma-4.6], [SC-13][cw-sc-13].
- **Baseline / control determinations:** `ma-4.6`: absent from current control baseline; `sc-13`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-13`: `research-required`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -4,8 +4,9 @@

-$ sudo update-crypto-policies --check && echo PASS
+$ sudo update-crypto-policies --check

 The configured policy matches the generated policy
-PASS

-If the last line is not "PASS", this is a finding.
+If the returned message does not match the above, but instead matches the following, this is a finding:
+
+The configured policy does NOT match the generated policy

@@ -33,2 +34,7 @@
 finding.
-Note: nss.config should not be hyperlinked.
+
+Note: nss.config should not be symlinked.
+
+Note: If there is an operational need to use a subpolicy that causes the links to the crypto backends to
+break, this is a finding, and exceptions will need to be made by the authorizing official (AO) and documented
+with the information system security officer (ISSO).
```

</details>

#### V-258241 — Changed

**RHEL 9 must implement a FIPS 140-3-compliant systemwide cryptographic policy.**

STIG ID: `RHEL-09-215105`. Severity: medium → high.
Rule ID: `SV-258241r1051259_rule` → `SV-258241r1262108_rule`.
CCI: CCI-002450, CCI-002890, CCI-003123.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [MA-4(6)][cw-ma-4.6], [SC-13][cw-sc-13].
- **Baseline / control determinations:** `ma-4.6`: absent from current control baseline; `sc-13`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-13`: `research-required`.

**Changed fields:** title, check, fix, severity.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "implement a FIPS 140-3 compliant systemwide cryptographic policy."
+ "implement a FIPS 140-3-compliant systemwide cryptographic policy."
```

**Check**

```diff
@@ -1,23 +1,9 @@
-Verify that RHEL 9 is set to use a FIPS 140-3 compliant systemwide cryptographic policy.
+Verify RHEL 9 is set to use a FIPS 140-3-compliant systemwide cryptographic policy.
+
+Verify the current systemwide crypto-policy with the following command:

 $ update-crypto-policies --show
-
 FIPS

-If the systemwide crypto policy is not set to "FIPS", this is a finding.
-
-Inspect the contents of the REQUIRE.pmod file (if it exists) to ensure that only authorized modifications to
-the current policy are included with the following command:
-
-$ cat /etc/crypto-policies/policies/modules/REQUIRE.pmod
-
-Note: If subpolicies have been configured, they could be listed in a colon-separated list starting with FIPS
-as follows FIPS:<SUBPOLICY-NAME>:<SUBPOLICY-NAME>. This is not a finding.
-
-If the AD-SUPPORT subpolicy module is included (e.g., "FIPS:AD-SUPPORT"), and Active Directory support is not
-documented as an operational requirement with the information system security officer (ISSO), this is a
-finding.
-
-If the NO-ENFORCE-EMS subpolicy module is included (e.g., "FIPS:NO-ENFORCE-EMS"), and not enforcing EMS is not
- documented as an operational requirement with the ISSO, this is a finding.
+If the systemwide crypto-policy is not set to "FIPS", this is a finding.

@@ -25,3 +11,3 @@

-$ grep -E 'rsa_size|hash' /etc/crypto-policies/state/CURRENT.pol
+$ sudo grep -E 'rsa_size|hash' /etc/crypto-policies/state/CURRENT.pol
 hash = SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256
@@ -29,8 +15,9 @@

-If the "hash" values do not include at least the following FIPS 140-3 compliant algorithms  "SHA2-256 SHA2-384
- SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256", this is a finding.
+If the "hash" values do not include at least the following FIPS 140-3-compliant algorithms, this is a finding:

-If there are algorithms that include "SHA1" or a hash value less than "256" this is a finding.
+"SHA2-256 SHA2-384 SHA2-512 SHA2-224 SHA3-256 SHA3-384 SHA3-512 SHAKE-256"

-If the "min_rsa_size" is not set to a value of at least 2048, this is a finding.
+If any algorithms include "SHA1" or a hash value less than "224", this is a finding.
+
+If the "min_rsa_size" is not set to a value of at least "2048", this is a finding.

```

**Fix**

```diff
@@ -1,45 +1,9 @@
-Configure RHEL 9 to use a FIPS 140-3 compliant systemwide cryptographic policy.
+Configure RHEL 9 to use a FIPS 140-3-compliant systemwide cryptographic policy.

-Create subpolicies for enhancements to the systemwide crypto-policy with the following commands:
-
-Create or edit the SCOPES-AND-WILDCARDS policy module in a text editor and insert options that modify the
-systemwide cryptographic policy as follows:
-$ sudo vi /etc/crypto-policies/policies/modules/SCOPES-AND-WILDCARDS.pmod
-
-Add the following lines to the policy:
-# Disable CHACHA20-POLY1305 for the TLS protocol (OpenSSL, GnuTLS, NSS, and OpenJDK)
-cipher@TLS = -CHACHA20-POLY1305
-
-# Disable all CBC mode ciphers for the SSH protocol (libssh and OpenSSH)
-cipher@SSH = -*-CBC
-
-Create or edit the OPENSSH-SUBPOLICY module in a text editor and insert options that modify the systemwide
-crypto-policy as follows:
-$ sudo vi /etc/crypto-policies/policies/modules/OPENSSH-SUBPOLICY.pmod
-
-Add the following lines to the policy:
-# Define ciphers for OpenSSH
-cipher@SSH=AES-256-GCM AES-128-GCM AES-256-CTR AES-128-CTR
-
-# Define MACs for OpenSSH
-mac@SSH=HMAC-SHA2-512 HMAC-SHA2-256
-
-Create or edit the REQUIRE.pmod file and add the following lines to include the subpolicies in the FIPS
-configuration with the following command:
-
-$ sudo vi /etc/crypto-policies/policies/modules/REQUIRE.pmod
-
-Add the following lines to REQUIRE.pmod:
-@OPENSSH-SUBPOLICY
-@SCOPES-AND-WILDCARDS
-
-Apply the policy enhancements to the FIPS systemwide cryptographic policy level with the following command:
+Set the systemwide crypto-policy to FIPS with the following command:

 $ sudo update-crypto-policies --set FIPS
+Setting system policy to FIPS

-Note: If additional subpolicies are being employed, they should be added to the REQUIRE.pmod as well.
-REQUIRE.pmod is included in the systemwide crypto-policy when it is set.
-
-To make the cryptographic settings effective for already running services and applications, restart the
-system:
-$ sudo reboot
+Note: Systemwide crypto-policies are applied on application startup. It is recommended to restart the system
+for the change of policies to fully take place.
```

</details>

#### V-258242 — Changed

**RHEL 9 must implement DoW-approved encryption in the bind package.**

STIG ID: `RHEL-09-672050`. Severity: medium → high.
Rule ID: `SV-258242r958908_rule` → `SV-258242r1262158_rule`.
CCI: CCI-002418, CCI-002422.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-8][cw-sc-8], [SC-8(2)][cw-sc-8.2].
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined); `sc-8.2`: absent from current control baseline.
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.

**Changed fields:** title, severity.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "9 must implement DOD-approved encryption in the"
+ "9 must implement DoW-approved encryption in the"
```

</details>

#### V-270174 — Changed

**RHEL 9 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a graphical user logon.**

STIG ID: `RHEL-09-171011 → RHEL-09-271011`. Severity: medium.
Rule ID: `SV-270174r1044831_rule` → `SV-270174r1268215_rule`.
CCI: CCI-000048.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** stig_id, title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DOD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Discussion**

```diff
- "accordance with applicable DOD policy. Use the"
+ "accordance with applicable DoW policy. Use the"
```

**Check**

```diff
@@ -3,6 +3,6 @@

-Verify RHEL 9 displays the Standard Mandatory DOD Notice and Consent Banner before granting access to the
+Verify RHEL 9 displays the Standard Mandatory DoW Notice and Consent Banner before granting access to the
 operating system via a graphical user logon.

-Check that the operating system displays the exact Standard Mandatory DOD Notice and Consent Banner text with
+Check that the operating system displays the exact Standard Mandatory DoW Notice and Consent Banner text with
 the command:
@@ -28,2 +28,2 @@

-If the banner does not match the Standard Mandatory DOD Notice and Consent Banner exactly, this is a finding.
+If the banner does not match the Standard Mandatory DoW Notice and Consent Banner exactly, this is a finding.
```

**Fix**

```diff
@@ -1,3 +1,3 @@
-Configure the operating system to display the Standard Mandatory DOD Notice and Consent Banner before granting
- access to the system.
+Configure RHEL 9 to display the Standard Mandatory DoW Notice and Consent Banner before granting access to the
+ system.

```

</details>

#### V-270177 — Changed

**The RHEL 9 SSH client must be configured to use only DoW-approved encryption ciphers employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH client connections.**

STIG ID: `RHEL-09-255064`. Severity: medium → high.
Rule ID: `SV-270177r1051237_rule` → `SV-270177r1268237_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.

**Changed fields:** title, discussion, severity.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "to use only DOD-approved encryption ciphers employing"
+ "to use only DoW-approved encryption ciphers employing"
```

**Discussion**

```diff
- "is access to DOD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-270178 — Changed

**The RHEL 9 SSH client must be configured to use only DoW-approved Message Authentication Codes (MACs) employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH client connections.**

STIG ID: `RHEL-09-255070`. Severity: medium → high.
Rule ID: `SV-270178r1051243_rule` → `SV-270178r1268237_rule`.
CCI: CCI-001453.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-17(2)][cw-ac-17.2].
- **Baseline / control determinations:** `ac-17.2`: `research-required` (determination); handoff: [PLT-01], [PLT-10].
- **Reference image decisions to review:** `ac-17.2`: `deployment-configured`.

**Changed fields:** title, discussion, severity.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "to use only DOD-approved Message Authentication Codes"
+ "to use only DoW-approved Message Authentication Codes"
```

**Discussion**

```diff
- "is access to DOD nonpublic information systems"
+ "is access to DoW nonpublic information systems"
```

</details>

#### V-270180 — Changed

**The RHEL 9 fapolicy module must be configured to employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs.**

STIG ID: `RHEL-09-433016`. Severity: medium.
Rule ID: `SV-270180r1045182_rule` → `SV-270180r1184327_rule`.
CCI: CCI-001764.

- **Image criteria:** direct: None; shared-control review: [IMG-07], [IMG-30].
- **Crosswalk:** Prospective only; no accepted rule entry; [CM-7(2)][cw-cm-7.2].
- **Baseline / control determinations:** `cm-7.2`: `host-inherited` (determination); handoff: [PLT-01], [PLT-16].

**Changed fields:** check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -2,3 +2,3 @@

-Check that "fapolicyd" is in enforcement mode with the following command:
+Verify "fapolicyd" is in enforcement mode with the following command:

@@ -7,2 +7,4 @@
 permissive = 0
+
+If "fapolicyd" is not running in enforcement mode, this is a finding.

@@ -16,3 +18,5 @@

-If "fapolicyd" is not running in enforcement mode with a deny-all, permit-by-exception policy, this is a
-finding.
+If "fapolicyd" is not running with a deny-all, permit-by-exception policy, this is a finding.
+
+Note: "deny_log" or "deny_audit" options meet the security requirements.  These options will generate higher
+volumes of logs.
```

**Fix**

```diff
@@ -8,4 +8,4 @@

-Build the allow list in a file within the "/etc/fapolicyd/rules.d" directory, ensuring the last rule is "deny
-perm=any all : all".
+Build the allow list in a file within the "/etc/fapolicyd/rules.d" directory, ensuring the last rule
+implements a deny-all policy, such as "deny perm=any all : all".

```

</details>

#### V-272488 — Changed

**RHEL 9 must have the Postfix package installed.**

STIG ID: `RHEL-09-215101`. Severity: medium.
Rule ID: `SV-272488r1082178_rule` → `SV-272488r1155665_rule`.
CCI: CCI-000015.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-2(1)][cw-ac-2.1].
- **Baseline / control determinations:** `ac-2.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-2.1`: `not-applicable`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,2 +1,5 @@
-Verify that RHEL 9 has the Postfix package installed with the following command:
+Note: If the admin can demonstrate that there is another system/service to send audit failure notifications to
+ the administrator/ISSO, this control is not applicable.
+
+Verify RHEL 9 has the Postfix package installed with the following command:

```

</details>

#### V-272496 — Changed

**RHEL 9 must elevate the SELinux context when an administrator calls the sudo command.**

STIG ID: `RHEL-09-431016`. Severity: medium.
Rule ID: `SV-272496r1082184_rule` → `SV-272496r1155582_rule`.
CCI: CCI-002235.

- **Image criteria:** direct: None; shared-control review: [IMG-11], [IMG-31].
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-6(10)][cw-ac-6.10].
- **Baseline / control determinations:** `ac-6.10`: `image-owned` (criterion); handoff: [PLT-02].

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -1,3 +1,3 @@
-Verify that RHEL 9 elevates the SELinux context when an administrator calls the sudo command with the
-following command:
+Verify RHEL 9 elevates the SELinux context when an administrator calls the sudo command with the following
+command:

@@ -8,4 +8,2 @@

-If conflicting results are returned, this is a finding.
-
 If a designated sudoers administrator group or account(s) is not configured to elevate the SELinux type and
```

</details>

### RHEL 9 STIG: revision-ID-only changes

These have identical compared content, severity and CCIs. They require no
criterion or control-determination change on this evidence; accepted rendered
crosswalk rule content is unchanged. A later regeneration may change rule IDs.

| Group ID | Old Rule ID | Candidate Rule ID |
| --- | --- | --- |
| V-257781 | `SV-257781r991589_rule` | `SV-257781r1268251_rule` |
| V-257782 | `SV-257782r991589_rule` | `SV-257782r1268251_rule` |
| V-257788 | `SV-257788r1044838_rule` | `SV-257788r1268251_rule` |
| V-257790 | `SV-257790r991589_rule` | `SV-257790r1268251_rule` |
| V-257791 | `SV-257791r991589_rule` | `SV-257791r1268251_rule` |
| V-257793 | `SV-257793r1044843_rule` | `SV-257793r1268251_rule` |
| V-257818 | `SV-257818r1044876_rule` | `SV-257818r1268251_rule` |
| V-257819 | `SV-257819r1015075_rule` | `SV-257819r1268241_rule` |
| V-257827 | `SV-257827r1044892_rule` | `SV-257827r1268251_rule` |
| V-257837 | `SV-257837r1044910_rule` | `SV-257837r1268251_rule` |
| V-257839 | `SV-257839r991589_rule` | `SV-257839r1268251_rule` |
| V-257840 | `SV-257840r991589_rule` | `SV-257840r1268251_rule` |
| V-257841 | `SV-257841r1044914_rule` | `SV-257841r1268251_rule` |
| V-257843 | `SV-257843r991589_rule` | `SV-257843r1268251_rule` |
| V-257844 | `SV-257844r1044918_rule` | `SV-257844r1268251_rule` |
| V-257845 | `SV-257845r1044920_rule` | `SV-257845r1268251_rule` |
| V-257846 | `SV-257846r1044922_rule` | `SV-257846r1268251_rule` |
| V-257848 | `SV-257848r1044926_rule` | `SV-257848r1268251_rule` |
| V-257852 | `SV-257852r991589_rule` | `SV-257852r1268251_rule` |
| V-257854 | `SV-257854r1044934_rule` | `SV-257854r1268251_rule` |
| V-257855 | `SV-257855r1044936_rule` | `SV-257855r1268251_rule` |
| V-257856 | `SV-257856r1044938_rule` | `SV-257856r1268251_rule` |
| V-257857 | `SV-257857r991589_rule` | `SV-257857r1268251_rule` |
| V-257858 | `SV-257858r991589_rule` | `SV-257858r1268251_rule` |
| V-257859 | `SV-257859r991589_rule` | `SV-257859r1268251_rule` |
| V-257869 | `SV-257869r958804_rule` | `SV-257869r1102009_rule` |
| V-257888 | `SV-257888r1069378_rule` | `SV-257888r1268251_rule` |
| V-257891 | `SV-257891r991589_rule` | `SV-257891r1268251_rule` |
| V-257892 | `SV-257892r991589_rule` | `SV-257892r1268251_rule` |
| V-257893 | `SV-257893r991589_rule` | `SV-257893r1268251_rule` |
| V-257894 | `SV-257894r991589_rule` | `SV-257894r1268251_rule` |
| V-257895 | `SV-257895r991589_rule` | `SV-257895r1268251_rule` |
| V-257896 | `SV-257896r991589_rule` | `SV-257896r1268251_rule` |
| V-257897 | `SV-257897r991589_rule` | `SV-257897r1268251_rule` |
| V-257898 | `SV-257898r991589_rule` | `SV-257898r1268251_rule` |
| V-257899 | `SV-257899r991589_rule` | `SV-257899r1268251_rule` |
| V-257900 | `SV-257900r991589_rule` | `SV-257900r1268251_rule` |
| V-257901 | `SV-257901r991589_rule` | `SV-257901r1268251_rule` |
| V-257902 | `SV-257902r991589_rule` | `SV-257902r1268251_rule` |
| V-257903 | `SV-257903r991589_rule` | `SV-257903r1268251_rule` |
| V-257904 | `SV-257904r991589_rule` | `SV-257904r1268251_rule` |
| V-257905 | `SV-257905r991589_rule` | `SV-257905r1268251_rule` |
| V-257906 | `SV-257906r991589_rule` | `SV-257906r1268251_rule` |
| V-257907 | `SV-257907r991589_rule` | `SV-257907r1268251_rule` |
| V-257908 | `SV-257908r991589_rule` | `SV-257908r1268251_rule` |
| V-257909 | `SV-257909r991589_rule` | `SV-257909r1268251_rule` |
| V-257910 | `SV-257910r991589_rule` | `SV-257910r1268251_rule` |
| V-257911 | `SV-257911r991589_rule` | `SV-257911r1268251_rule` |
| V-257912 | `SV-257912r991589_rule` | `SV-257912r1268251_rule` |
| V-257913 | `SV-257913r991589_rule` | `SV-257913r1268251_rule` |
| V-257926 | `SV-257926r991589_rule` | `SV-257926r1268251_rule` |
| V-257927 | `SV-257927r991589_rule` | `SV-257927r1268251_rule` |
| V-257930 | `SV-257930r991589_rule` | `SV-257930r1268251_rule` |
| V-257931 | `SV-257931r991589_rule` | `SV-257931r1268251_rule` |
| V-257932 | `SV-257932r1014838_rule` | `SV-257932r1268251_rule` |
| V-257934 | `SV-257934r991589_rule` | `SV-257934r1268251_rule` |
| V-257941 | `SV-257941r991589_rule` | `SV-257941r1268251_rule` |
| V-257948 | `SV-257948r1045004_rule` | `SV-257948r1268251_rule` |
| V-257950 | `SV-257950r1045006_rule` | `SV-257950r1268251_rule` |
| V-257951 | `SV-257951r1014843_rule` | `SV-257951r1268251_rule` |
| V-257955 | `SV-257955r991589_rule` | `SV-257955r1268251_rule` |
| V-257956 | `SV-257956r991589_rule` | `SV-257956r1268251_rule` |
| V-257980 | `SV-257980r1045016_rule` | `SV-257980r1268251_rule` |
| V-257982 | `SV-257982r1045021_rule` | `SV-257982r1268219_rule` |
| V-257984 | `SV-257984r1045026_rule` | `SV-257984r1268229_rule` |
| V-257997 | `SV-257997r1069370_rule` | `SV-257997r1268251_rule` |
| V-257998 | `SV-257998r1082181_rule` | `SV-257998r1268251_rule` |
| V-258001 | `SV-258001r991589_rule` | `SV-258001r1268251_rule` |
| V-258005 | `SV-258005r1045069_rule` | `SV-258005r1268251_rule` |
| V-258006 | `SV-258006r1045071_rule` | `SV-258006r1268251_rule` |
| V-258007 | `SV-258007r1045073_rule` | `SV-258007r1268251_rule` |
| V-258008 | `SV-258008r1045075_rule` | `SV-258008r1268251_rule` |
| V-258009 | `SV-258009r1045077_rule` | `SV-258009r1268251_rule` |
| V-258011 | `SV-258011r1045079_rule` | `SV-258011r1268251_rule` |
| V-258013 | `SV-258013r1045082_rule` | `SV-258013r1268215_rule` |
| V-258028 | `SV-258028r991589_rule` | `SV-258028r1268251_rule` |
| V-258029 | `SV-258029r1045109_rule` | `SV-258029r1268251_rule` |
| V-258030 | `SV-258030r1045112_rule` | `SV-258030r1268251_rule` |
| V-258032 | `SV-258032r1045117_rule` | `SV-258032r1268251_rule` |
| V-258033 | `SV-258033r1045120_rule` | `SV-258033r1268251_rule` |
| V-258043 | `SV-258043r991589_rule` | `SV-258043r1268251_rule` |
| V-258047 | `SV-258047r958508_rule` | `SV-258047r1101951_rule` |
| V-258050 | `SV-258050r1045137_rule` | `SV-258050r1268251_rule` |
| V-258051 | `SV-258051r991589_rule` | `SV-258051r1268251_rule` |
| V-258058 | `SV-258058r1045148_rule` | `SV-258058r1268251_rule` |
| V-258059 | `SV-258059r991589_rule` | `SV-258059r1268251_rule` |
| V-258068 | `SV-258068r1069388_rule` | `SV-258068r1101950_rule` |
| V-258081 | `SV-258081r1045164_rule` | `SV-258081r1268251_rule` |
| V-258082 | `SV-258082r1045166_rule` | `SV-258082r1268251_rule` |
| V-258085 | `SV-258085r1045173_rule` | `SV-258085r1268251_rule` |
| V-258094 | `SV-258094r1045187_rule` | `SV-258094r1268251_rule` |
| V-258098 | `SV-258098r1045195_rule` | `SV-258098r1268251_rule` |
| V-258120 | `SV-258120r991589_rule` | `SV-258120r1268251_rule` |
| V-258124 | `SV-258124r1045250_rule` | `SV-258124r1268242_rule` |
| V-258136 | `SV-258136r1045270_rule` | `SV-258136r1268251_rule` |
| V-258138 | `SV-258138r1045274_rule` | `SV-258138r1268251_rule` |
| V-258139 | `SV-258139r1045276_rule` | `SV-258139r1268251_rule` |
| V-258141 | `SV-258141r1045280_rule` | `SV-258141r1268251_rule` |
| V-258142 | `SV-258142r991589_rule` | `SV-258142r1268251_rule` |
| V-258144 | `SV-258144r1045286_rule` | `SV-258144r1268219_rule` |
| V-258151 | `SV-258151r1045298_rule` | `SV-258151r1268225_rule` |
| V-258152 | `SV-258152r1015127_rule` | `SV-258152r1268225_rule` |
| V-258164 | `SV-258164r1045301_rule` | `SV-258164r1268225_rule` |
| V-258170 | `SV-258170r991589_rule` | `SV-258170r1268251_rule` |
| V-258179 | `SV-258179r1069366_rule` | `SV-258179r1155601_rule` |
| V-258216 | `SV-258216r1045433_rule` | `SV-258216r1155613_rule` |
| V-270175 | `SV-270175r1044964_rule` | `SV-270175r1268226_rule` |
| V-270176 | `SV-270176r1044967_rule` | `SV-270176r1268226_rule` |

<a id="disa-web-server-srg"></a>

## Web Server SRG — V3R3 → V4R5

**Adopt with changes.** 32 added, 8 removed, 10 changed. Comparison: pinned ZIP XCCDF → candidate XCCDF.

Of the 10 changed rules, 7 change check, fix, severity or CCI; 3 change only title/discussion/STIG ID.

Seven removed IDs V-260896–V-260902 correspond in order to added IDs
V-264360–V-264366 (same STIG IDs). These count as seven removals and seven
additions, not surviving-rule edits. V-206420 has no same-STIG-ID replacement.
The other 25 additions are new relative to this pin.

### Web Server SRG: added

#### V-264337 — Added

**The web server must disable accounts when the accounts have expired.**

STIG ID: `SRG-APP-000700-WSR-000100`. Severity: medium.
Rule ID: `SV-264337r984356_rule`.
CCI: CCI-003627.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [AC-2(3)][cw-ac-2.3].
- **Baseline / control determinations:** `ac-2.3`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-2.3`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to disable accounts when the accounts have expired.

If the web server is not configured to disable accounts when the accounts have expired, this is a finding.
```

**Fix**

```text
Configure the web server to disable accounts when the accounts have expired.
```

</details>

#### V-264338 — Added

**The web server must disable accounts when the accounts are no longer associated to a user.**

STIG ID: `SRG-APP-000705-WSR-000110`. Severity: medium.
Rule ID: `SV-264338r984359_rule`.
CCI: CCI-003628.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [AC-2(3)][cw-ac-2.3].
- **Baseline / control determinations:** `ac-2.3`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-2.3`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to disable accounts when the accounts are no longer associated to a user.

If the web server is not configured to disable accounts when the accounts are no longer associated to a user, this is a finding.
```

**Fix**

```text
Configure the web server to disable accounts when the accounts are no longer associated to a user.
```

</details>

#### V-264339 — Added

**The web server must implement the capability to centrally review and analyze audit records from multiple components within the system.**

STIG ID: `SRG-APP-000745-WSR-000120`. Severity: medium.
Rule ID: `SV-264339r984362_rule`.
CCI: CCI-003821.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; add [AU-6(4)][cw-au-6.4].
- **Baseline / control determinations:** `au-6.4`: `host-inherited` (determination); handoff: [PLT-09].
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to implement the capability to centrally review and analyze audit records from multiple components within the system.

If the web server is not configured to implement the capability to centrally review and analyze audit records from multiple components within the system, this is a finding.
```

**Fix**

```text
Configure the web server to implement the capability to centrally review and analyze audit records from multiple components within the system.
```

</details>

#### V-264340 — Added

**The web server must alert organization-defined personnel or roles upon detection of unauthorized access, modification, or deletion of audit information.**

STIG ID: `SRG-APP-000795-WSR-000130`. Severity: medium.
Rule ID: `SV-264340r984365_rule`.
CCI: CCI-003831.

- **Image criteria:** direct: None; shared-control review: [IMG-19].
- **Crosswalk:** Prospective only; no accepted rule entry; add [AU-9][cw-au-9].
- **Baseline / control determinations:** `au-9`: `host-inherited` (expectation); handoff: [PLT-09].
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to alert organization-defined personnel or roles upon detection of unauthorized access, modification, or deletion of audit information.

If the web server is not configured to alert organization-defined personnel or roles upon detection of unauthorized access, modification, or deletion of audit information, this is a finding.
```

**Fix**

```text
Configure the web server to alert organization-defined personnel or roles upon detection of unauthorized access, modification, or deletion of audit information.
```

</details>

#### V-264341 — Added

**The web server must automatically generate audit records of the enforcement actions.**

STIG ID: `SRG-APP-000805-WSR-000140`. Severity: medium.
Rule ID: `SV-264341r984368_rule`.
CCI: CCI-003938.

- **Image criteria:** direct: None; shared-control review: [IMG-15].
- **Crosswalk:** Prospective only; no accepted rule entry; add [CM-5(1)][cw-cm-5.1].
- **Baseline / control determinations:** `cm-5.1`: `deployment-configured` (expectation); handoff: [PLT-03].
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to automatically generate audit records of the enforcement actions.

If the web server is not configured to automatically generate audit records of the enforcement actions, this is a finding.
```

**Fix**

```text
Configure the web server to automatically generate audit records of the enforcement actions.
```

</details>

#### V-264342 — Added

**The web server must require users to be individually authenticated before granting access to the shared accounts or resources.**

STIG ID: `SRG-APP-000815-WSR-000160`. Severity: medium.
Rule ID: `SV-264342r984371_rule`.
CCI: CCI-004045.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-2(5)][cw-ia-2.5].
- **Baseline / control determinations:** `ia-2.5`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.5`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to require users to be individually authenticated before granting access to the shared accounts or resources.

If the web server is not configured to require users to be individually authenticated before granting access to the shared accounts or resources, this is a finding.
```

**Fix**

```text
Configure the web server to require users to be individually authenticated before granting access to the shared accounts or resources.
```

</details>

#### V-264343 — Added

**The web server must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access.**

STIG ID: `SRG-APP-000820-WSR-000170`. Severity: medium.
Rule ID: `SV-264343r984374_rule`.
CCI: CCI-004046.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-2(6)][cw-ia-2.6].
- **Baseline / control determinations:** `ia-2.6`: absent from current control baseline.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access.

If the web server is not configured to implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access, this is a finding.
```

**Fix**

```text
Configure the web server to implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access.
```

</details>

#### V-264344 — Added

**The web server must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements.**

STIG ID: `SRG-APP-000825-WSR-000180`. Severity: medium.
Rule ID: `SV-264344r984377_rule`.
CCI: CCI-004047.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-2(6)][cw-ia-2.6].
- **Baseline / control determinations:** `ia-2.6`: absent from current control baseline.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements.

If the web server is not configured to implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements, this is a finding.
```

**Fix**

```text
Configure the web server to implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements.
```

</details>

#### V-264345 — Added

**The web server must, for password-based authentication, maintain a list of commonly used, expected, or compromised passwords on an organization-defined frequency.**

STIG ID: `SRG-APP-000830-WSR-000190`. Severity: medium.
Rule ID: `SV-264345r984380_rule`.
CCI: CCI-004058.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to maintain a list of commonly used, expected, or compromised passwords on an organization-defined frequency.

If the web server is not configured to maintain a list of commonly used, expected, or compromised passwords on an organization-defined frequency, this is a finding.
```

**Fix**

```text
Configure the web server to maintain a list of commonly used, expected, or compromised passwords on an organization-defined frequency.
```

</details>

#### V-264346 — Added

**The web server must, for password-based authentication, update the list of passwords on an organization-defined frequency.**

STIG ID: `SRG-APP-000835-WSR-000200`. Severity: medium.
Rule ID: `SV-264346r984383_rule`.
CCI: CCI-004059.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to update the list of passwords on an organization-defined frequency.

If the web server is not configured to update the list of passwords on an organization-defined frequency, this is a finding.
```

**Fix**

```text
Configure the web server to update the list of passwords on an organization-defined frequency.
```

</details>

#### V-264347 — Added

**The web server must, for password-based authentication, update the list of passwords when organizational passwords are suspected to have been compromised directly or indirectly.**

STIG ID: `SRG-APP-000840-WSR-000210`. Severity: medium.
Rule ID: `SV-264347r984386_rule`.
CCI: CCI-004060.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to update the list of passwords when organizational passwords are suspected to have been compromised directly or indirectly.

If the web server is not configured to update the list of passwords when organizational passwords are suspected to have been compromised directly or indirectly, this is a finding.
```

**Fix**

```text
Configure the web server to update the list of passwords when organizational passwords are suspected to have been compromised directly or indirectly.
```

</details>

#### V-264348 — Added

**The web server must, for password-based authentication, verify when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a).**

STIG ID: `SRG-APP-000845-WSR-000220`. Severity: medium.
Rule ID: `SV-264348r984389_rule`.
CCI: CCI-004061.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to verify when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a).

If the web server is not configured to verify when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a), this is a finding.
```

**Fix**

```text
Configure the web server to verify when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a).
```

</details>

#### V-264349 — Added

**The web server must, for password-based authentication, store passwords using an approved salted key derivation function, preferably using a keyed hash.**

STIG ID: `SRG-APP-000850-WSR-000230`. Severity: medium.
Rule ID: `SV-264349r984392_rule`.
CCI: CCI-004062.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to store passwords using an approved salted key derivation function, preferably using a keyed hash.

If the web server is not configured to store passwords using an approved salted key derivation function, preferably using a keyed hash, this is a finding.
```

**Fix**

```text
Configure the web server to store passwords using an approved salted key derivation function, preferably using a keyed hash.
```

</details>

#### V-264350 — Added

**The web server must, for password-based authentication, require immediate selection of a new password upon account recovery.**

STIG ID: `SRG-APP-000855-WSR-000240`. Severity: medium.
Rule ID: `SV-264350r984395_rule`.
CCI: CCI-004063.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to require immediate selection of a new password upon account recovery.

If the web server is not configured to require immediate selection of a new password upon account recovery, this is a finding.
```

**Fix**

```text
Configure the web server to require immediate selection of a new password upon account recovery.
```

</details>

#### V-264351 — Added

**The web server must, for password-based authentication, allow user selection of long passwords and passphrases, including spaces and all printable characters.**

STIG ID: `SRG-APP-000860-WSR-000250`. Severity: medium.
Rule ID: `SV-264351r984398_rule`.
CCI: CCI-004064.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to allow user selection of long passwords and passphrases, including spaces and all printable characters.

If the web server is not configured to allow user selection of long passwords and passphrases, including spaces and all printable characters, this is a finding.
```

**Fix**

```text
Configure the web server to allow user selection of long passwords and passphrases, including spaces and all printable characters.
```

</details>

#### V-264352 — Added

**The web server must, for password-based authentication, employ automated tools to assist the user in selecting strong password authenticators.**

STIG ID: `SRG-APP-000865-WSR-000260`. Severity: medium.
Rule ID: `SV-264352r984401_rule`.
CCI: CCI-004065.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to employ automated tools to assist the user in selecting strong password authenticators.

If the web server is not configured to employ automated tools to assist the user in selecting strong password authenticators, this is a finding.
```

**Fix**

```text
Configure the web server to employ automated tools to assist the user in selecting strong password authenticators.
```

</details>

#### V-264353 — Added

**The web server must, for password-based authentication, enforce organization-defined composition and complexity rules.**

STIG ID: `SRG-APP-000870-WSR-000270`. Severity: medium.
Rule ID: `SV-264353r984404_rule`.
CCI: CCI-004066.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to enforce organization-defined composition and complexity rules.

If the web server is not configured to enforce organization-defined composition and complexity rules, this is a finding.
```

**Fix**

```text
Configure the web server to enforce organization-defined composition and complexity rules.
```

</details>

#### V-264354 — Added

**The web server must, for public key-based authentication, implement a local cache of revocation data to support path discovery and validation.**

STIG ID: `SRG-APP-000875-WSR-000280`. Severity: medium.
Rule ID: `SV-264354r984407_rule`.
CCI: CCI-004068.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [IA-5(2)][cw-ia-5.2].
- **Baseline / control determinations:** `ia-5.2`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.2`: `not-applicable`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to implement a local cache of revocation data to support path discovery and validation.

If the web server is not configured to implement a local cache of revocation data to support path discovery and validation, this is a finding.
```

**Fix**

```text
Configure the web server to implement a local cache of revocation data to support path discovery and validation.
```

</details>

#### V-264355 — Added

**The web server must protect nonlocal maintenance sessions by separating the maintenance session from other network sessions with the system by logically separated communications paths.**

STIG ID: `SRG-APP-000880-WSR-000290`. Severity: medium.
Rule ID: `SV-264355r984410_rule`.
CCI: CCI-004192.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [MA-4(4)][cw-ma-4.4].
- **Baseline / control determinations:** `ma-4.4`: absent from current control baseline.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to protect nonlocal maintenance sessions by separating the maintenance session from other network sessions with the system by logically separated communications paths.

If the web server is not configured to protect nonlocal maintenance sessions by separating the maintenance session from other network sessions with the system by logically separated communications paths, this is a finding.
```

**Fix**

```text
Configure the web server to protect nonlocal maintenance sessions by separating the maintenance session from other network sessions with the system by logically separated communications paths.
```

</details>

#### V-264356 — Added

**The web server must include only approved trust anchors in trust stores or certificate stores managed by the organization.**

STIG ID: `SRG-APP-000910-WSR-000300`. Severity: medium.
Rule ID: `SV-264356r984413_rule`.
CCI: CCI-004909.

- **Image criteria:** direct: None; shared-control review: [IMG-17].
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-17][cw-sc-17].
- **Baseline / control determinations:** `sc-17`: `deployment-configured` (determination); handoff: [PLT-06].
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to include only approved trust anchors in trust stores or certificate stores managed by the organization.

If the web server is not configured to include only approved trust anchors in trust stores or certificate stores managed by the organization, this is a finding.
```

**Fix**

```text
Configure the web server to include only approved trust anchors in trust stores or certificate stores managed by the organization.
```

</details>

#### V-264357 — Added

**The web server must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store.**

STIG ID: `SRG-APP-000915-WSR-000310`. Severity: medium.
Rule ID: `SV-264357r984416_rule`.
CCI: CCI-004910.

- **Image criteria:** direct: None; shared-control review: [IMG-05], [IMG-16].
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-28(3)][cw-sc-28.3].
- **Baseline / control determinations:** `sc-28.3`: `deployment-configured` (determination); handoff: [PLT-06].
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store.

If the web server is not configured to provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store, this is a finding.
```

**Fix**

```text
Configure the web server to provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store.
```

</details>

#### V-264358 — Added

**The web server must synchronize system clocks within and between systems or system components.**

STIG ID: `SRG-APP-000920-WSR-000320`. Severity: medium.
Rule ID: `SV-264358r984419_rule`.
CCI: CCI-004922.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-45][cw-sc-45].
- **Baseline / control determinations:** `sc-45`: `host-inherited` (expectation); handoff: [HST-05].
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to synchronize system clocks within and between systems or system components.

If the web server is not configured to synchronize system clocks within and between systems or system components, this is a finding.
```

**Fix**

```text
Configure the web server to synchronize system clocks within and between systems or system components.
```

</details>

#### V-264359 — Added

**The web server must compare the internal system clocks on an organization-defined frequency with organization-defined authoritative time source.**

STIG ID: `SRG-APP-000925-WSR-000330`. Severity: medium.
Rule ID: `SV-264359r984422_rule`.
CCI: CCI-004923.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-45(1)][cw-sc-45.1].
- **Baseline / control determinations:** `sc-45.1`: absent from current control baseline.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server is configured to compare the internal system clocks on an organization-defined frequency with organization-defined authoritative time source.

If the web server is not configured to compare the internal system clocks on an organization-defined frequency with organization-defined authoritative time source, this is a finding.
```

**Fix**

```text
Configure the web server to compare the internal system clocks on an organization-defined frequency with organization-defined authoritative time source.
```

</details>

#### V-264360 — Added

**The web server must restrict a consistent inbound source IP for the entire management session.**

STIG ID: `SRG-APP-000219-WSR-000190`. Severity: medium.
Rule ID: `SV-264360r1043178_rule`.
CCI: CCI-001184.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-23][cw-sc-23].
- **Baseline / control determinations:** `sc-23`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-23`: `deployment-configured`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server limits authenticated client management sessions to initial session source IP.

If the web server does not limit authenticated client management sessions to initial session source IP, this is a finding.
```

**Fix**

```text
Configure the web server to restrict the management session to a consistent inbound IP for the entire management session.
```

</details>

#### V-264361 — Added

**The web server must restrict a consistent inbound source IP for the entire user session.**

STIG ID: `SRG-APP-000219-WSR-000191`. Severity: medium.
Rule ID: `SV-264361r1067566_rule`.
CCI: CCI-001184.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-23][cw-sc-23].
- **Baseline / control determinations:** `sc-23`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-23`: `deployment-configured`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server limits authenticated user sessions to a consistent inbound IP for the entire user session

If the web server does not limit authenticated user sessions to a consistent inbound IP for the entire user session, this is a finding.
```

**Fix**

```text
Configure the web server to restrict the user session to a consistent inbound IP for the entire user session.
```

</details>

#### V-264362 — Added

**The web server must use HTTP/2, at a minimum.**

STIG ID: `SRG-APP-000439-WSR-000192`. Severity: medium.
Rule ID: `SV-264362r984431_rule`.
CCI: CCI-002418.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-8][cw-sc-8].
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server uses HTTP/2.

If the web server does not use HTTP/2 at a minimum, this is a finding.
```

**Fix**

```text
Configure the web server to use HTTP/2, at a minimum.

Note that browsers support HTTP/2 only in HTTPS mode. The tunneling of HTTP/1.x through HTTPS is not an approved configuration.
```

</details>

#### V-264363 — Added

**The web server must disable HTTP/1.x downgrading.**

STIG ID: `SRG-APP-000439-WSR-000193`. Severity: medium.
Rule ID: `SV-264363r984434_rule`.
CCI: CCI-002418.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-8][cw-sc-8].
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
If HTTP downgrading is operationally necessary, and the rewritten request is validated against HTTP/1.x specification (i.e., verify requests that contain new lines in the headers, colons in header names, and spaces in the request method are rejected), mark as a CAT III finding.

Verify that HTTP/1.x downgrading is disabled.

If the HTTP/1.x downgrading is enabled, this is a finding.
```

**Fix**

```text
Configure the web server to disable HTTP/1.x downgrading.

If HTTP downgrading is operationally necessary, validate the rewritten request against the HTTP/1.1 specification, i.e., reject requests that contain new lines in the headers, colons in header names, and spaces in the request method.
```

</details>

#### V-264364 — Added

**The web server must interpret and normalize ambiguous HTTP requests or terminate the TCP connection.**

STIG ID: `SRG-APP-000251-WSR-000194`. Severity: medium.
Rule ID: `SV-264364r984437_rule`.
CCI: CCI-001310.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SI-10][cw-si-10].
- **Baseline / control determinations:** `si-10`: `research-required` (undetermined).
- **Reference image decisions to review:** `si-10`: `research-required`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server normalizes ambiguous requests or terminates the TCP connection.

If the web server does not drop ambiguous requests that cannot be normalized and terminate the TCP connection, this is a finding.
```

**Fix**

```text
Configure the web server to interpret HTTP headers so they are normalized and unambiguous. The web server must validate requests that report message body as "zero" in the HTTP header.

Configure the web server to drop ambiguous requests that cannot be normalized and terminate the TCP connection.
```

</details>

#### V-264365 — Added

**The web server must terminate the connection if server-level exceptions are triggered when handling requests to prevent HTTP request smuggling attacks.**

STIG ID: `SRG-APP-000251-WSR-000195`. Severity: medium.
Rule ID: `SV-264365r984440_rule`.
CCI: CCI-001310.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SI-10][cw-si-10].
- **Baseline / control determinations:** `si-10`: `research-required` (undetermined).
- **Reference image decisions to review:** `si-10`: `research-required`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify the web server terminates the connection if server-level exceptions are triggered when handling requests.

If the web server does not terminate the connection if server-level exceptions are triggered when handling requests, this is a finding.
```

**Fix**

```text
Configure web server to terminate the connection if server-level exceptions are triggered when handling requests to prevent HTTP request smuggling attacks.
```

</details>

#### V-264366 — Added

**The web server must only use forward proxies that route HTTP/2 requests upstream.**

STIG ID: `SRG-APP-000439-WSR-000196`. Severity: medium.
Rule ID: `SV-264366r984443_rule`.
CCI: CCI-002418.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [SC-8][cw-sc-8].
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
If a forward proxy is not used, this is not applicable.

Verify the web server only uses forward proxies that route HTTP/2 requests upstream.

If the web server uses forward proxies that do not only route HTTP/2 requests, this is a finding.
```

**Fix**

```text
Configure the web server to only use forward proxies that route HTTP/2 requests upstream.
```

</details>

#### V-279028 — Added

**The web server must uniquely identify and authenticate source by organization, system, application, and/or individual for information transfer.**

STIG ID: `SRG-APP-000334-WSR-000024`. Severity: medium.
Rule ID: `SV-279028r1138077_rule`.
CCI: CCI-002205, CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; add [AC-4(17)][cw-ac-4.17], [CM-6][cw-cm-6].
- **Baseline / control determinations:** `ac-4.17`: absent from current control baseline; `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `cm-6`: `research-required`.
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify that the web server is configured to uniquely identify and authenticate source by organization, system, application, and/or individual for information transfer.

If the web server does not uniquely identify and authenticate source by organization, system, application, and/or individual for information transfer, this is a finding.
```

**Fix**

```text
Configure the web server to uniquely identify and authenticate source by organization, system, application, and/or individual for information transfer.
```

</details>

#### V-279029 — Added

**The web server must be a version supported by the vendor.**

STIG ID: `SRG-APP-001035-WSR-000340`. Severity: high.
Rule ID: `SV-279029r1138083_rule`.
CCI: CCI-003376.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-29].
- **Crosswalk:** Prospective only; no accepted rule entry; add [SA-22][cw-sa-22].
- **Baseline / control determinations:** `sa-22`: `image-owned` (criterion).
<details>
<summary>Candidate check and fix text</summary>

**Check**

```text
Verify that the web server is a version supported by the vendor.

If the web server is not a version supported by the vendor, this is a finding.
```

**Fix**

```text
Install or upgrade the webserver to a version supported by the vendor.
```

</details>

### Web Server SRG: removed

#### V-206420 — Removed

**A web server that is part of a web server cluster must route all remote management through a centrally managed access control point.**

STIG ID: `SRG-APP-000356-WSR-000007`. Severity: medium.
Rule ID: `SV-206420r961389_rule`.
CCI: CCI-001844.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; None.
- **Baseline / control determinations:** No Rev 5 control resolved.
- **CCI findings:** old: CCI-001844: no Rev 5 reference; Rev 4 AU-3 (2); candidate: none.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Review the web server documentation and configuration to determine if the web server is part of a cluster.

If the web server is not part of a cluster, then this is NA.

If the web server is part of a cluster and is not centrally managed, then this is a finding.
```

**Fix**

```text
Configure the web server to be centrally managed.
```

</details>

#### V-260896 — Removed

**The web server must restrict a consistent inbound source IP for the entire management session.**

STIG ID: `SRG-APP-000219-WSR-000190`. Severity: medium.
Rule ID: `SV-260896r962359_rule`.
CCI: CCI-001184.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-23][cw-sc-23] → None.
- **Baseline / control determinations:** `sc-23`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-23`: `deployment-configured`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the web server limits authenticated client management sessions to initial session source IP.

If the web server does not limit authenticated client management sessions to initial session source IP, this is a finding.
```

**Fix**

```text
Configure the web server to restrict the management session to a consistent inbound IP for the entire management session.
```

</details>

#### V-260897 — Removed

**The web server must restrict a consistent inbound source IP for the entire user session.**

STIG ID: `SRG-APP-000219-WSR-000191`. Severity: info.
Rule ID: `SV-260897r962360_rule`.
CCI: CCI-001184.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-23][cw-sc-23] → None.
- **Baseline / control determinations:** `sc-23`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-23`: `deployment-configured`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the web server limits authenticated user sessions to a consistent inbound IP for the entire user session

If the web server does not limit authenticated user sessions to a consistent inbound IP for the entire user session, this is a finding.
```

**Fix**

```text
Configure the web server to restrict the user session to a consistent inbound IP for the entire user session.
```

</details>

#### V-260898 — Removed

**The web server must use HTTP/2, at a minimum.**

STIG ID: `SRG-APP-000439-WSR-000192`. Severity: medium.
Rule ID: `SV-260898r962361_rule`.
CCI: CCI-002418.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-8][cw-sc-8] → None.
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the web server uses HTTP/2.

If the web server does not use HTTP/2 at a minimum, this is a finding.
```

**Fix**

```text
Configure the web server to use HTTP/2, at a minimum.

Note that browsers support HTTP/2 only in HTTPS mode. The tunneling of HTTP/1.x through HTTPS is not an approved configuration.
```

</details>

#### V-260899 — Removed

**The web server must disable HTTP/1.x downgrading.**

STIG ID: `SRG-APP-000439-WSR-000193`. Severity: medium.
Rule ID: `SV-260899r965427_rule`.
CCI: CCI-002418.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-8][cw-sc-8] → None.
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
If HTTP downgrading is operationally necessary, and the rewritten request is validated against HTTP/1.x specification (i.e., verify requests that contain new lines in the headers, colons in header names, and spaces in the request method are rejected), mark as a CAT III finding.

Verify that HTTP/1.x downgrading is disabled.

If the HTTP/1.x downgrading is enabled, this is a finding.
```

**Fix**

```text
Configure the web server to disable HTTP/1.x downgrading.

If HTTP downgrading is operationally necessary, validate the rewritten request against the HTTP/1.1 specification, i.e., reject requests that contain new lines in the headers, colons in header names, and spaces in the request method.
```

</details>

#### V-260900 — Removed

**The web server must interpret and normalize ambiguous HTTP requests or terminate the TCP connection.**

STIG ID: `SRG-APP-000251-WSR-000194`. Severity: medium.
Rule ID: `SV-260900r965405_rule`.
CCI: CCI-001310.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SI-10][cw-si-10] → None.
- **Baseline / control determinations:** `si-10`: `research-required` (undetermined).
- **Reference image decisions to review:** `si-10`: `research-required`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the web server normalizes ambiguous requests or terminates the TCP connection.

If the web server does not drop ambiguous requests that cannot be normalized and terminate the TCP connection, this is a finding.
```

**Fix**

```text
Configure the web server to interpret HTTP headers so they are normalized and unambiguous. The web server must validate requests that report message body as "zero" in the HTTP header.

Configure the web server to drop ambiguous requests that cannot be normalized and terminate the TCP connection.
```

</details>

#### V-260901 — Removed

**The web server must terminate the connection if server-level exceptions are triggered when handling requests to prevent HTTP request smuggling attacks.**

STIG ID: `SRG-APP-000251-WSR-000195`. Severity: medium.
Rule ID: `SV-260901r962364_rule`.
CCI: CCI-001310.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SI-10][cw-si-10] → None.
- **Baseline / control determinations:** `si-10`: `research-required` (undetermined).
- **Reference image decisions to review:** `si-10`: `research-required`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
Verify the web server terminates the connection if server-level exceptions are triggered when handling requests.

If the web server does not terminate the connection if server-level exceptions are triggered when handling requests, this is a finding.
```

**Fix**

```text
Configure web server to terminate the connection if server-level exceptions are triggered when handling requests to prevent HTTP request smuggling attacks.
```

</details>

#### V-260902 — Removed

**The web server must only use forward proxies that route HTTP/2 requests upstream.**

STIG ID: `SRG-APP-000439-WSR-000196`. Severity: medium.
Rule ID: `SV-260902r965429_rule`.
CCI: CCI-002418.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [SC-8][cw-sc-8] → None.
- **Baseline / control determinations:** `sc-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `sc-8`: `deployment-configured`.
<details>
<summary>Removed baseline check and fix text</summary>

**Check**

```text
If a forward proxy is not used, this is not applicable.

Verify the web server only uses forward proxies that route HTTP/2 requests upstream.

If the web server uses forward proxies that do not only route HTTP/2 requests, this is a finding.
```

**Fix**

```text
Configure the web server to only use forward proxies that route HTTP/2 requests upstream.
```

</details>

### Web Server SRG: changed

#### V-206355 — Changed

**The web server must enforce approved authorizations for logical access to hosted applications and resources in accordance with applicable access control policies.**

STIG ID: `SRG-APP-000033-WSR-000169`. Severity: medium.
Rule ID: `SV-206355r960792_rule` → `SV-206355r1138069_rule`.
CCI: CCI-000213.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [AC-3][cw-ac-3].
- **Baseline / control determinations:** `ac-3`: `research-required` (determination); handoff: [PLT-06].
- **Reference image decisions to review:** `ac-3`: `deployment-configured`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "issued certificates by DoD-approved PKIs, the web"
+ "issued certificates by DOD-approved PKIs, the web"
- " the production system."
+ " the production system.\n\nThis requirement also applies to Zero Trust initiatives."
```

</details>

#### V-206372 — Changed

**All web server files must be verified for their integrity (e.g., checksums and hashes) before becoming part of the production web server.**

STIG ID: `SRG-APP-000131-WSR-000051`. Severity: medium.
Rule ID: `SV-206372r960954_rule` → `SV-206372r984351_rule`.
CCI: CCI-001749 → CCI-003992.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Accepted rule entry; None → [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].
- **CCI findings:** old: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3); candidate: none.

**Changed fields:** discussion, ccis.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "file validation and non-repudiation of the information."
+ "file validation and nonrepudiation of the information."
```

</details>

#### V-206373 — Changed

**Expansion modules must be fully reviewed, tested, and signed before they can exist on a production web server.**

STIG ID: `SRG-APP-000131-WSR-000073`. Severity: medium.
Rule ID: `SV-206373r960954_rule` → `SV-206373r984352_rule`.
CCI: CCI-001749 → CCI-003992.

- **Image criteria:** direct: None; shared-control review: [IMG-01], [IMG-02], [IMG-03], [IMG-04], [IMG-22].
- **Crosswalk:** Accepted rule entry; None → [CM-14][cw-cm-14].
- **Baseline / control determinations:** `cm-14`: `image-owned` (criterion); handoff: [PLT-01].
- **CCI findings:** old: CCI-001749: no Rev 5 reference; Rev 4 CM-5 (3); candidate: none.

**Changed fields:** discussion, ccis.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " a development website.  The process of "
+ " a development website. The process of "
- " and repeated testing.  This process is "
+ " and repeated testing. This process is "
- " the main goals.  The opportunity for "
+ " the main goals. The opportunity for "
- " in this situation.  The existence of "
+ " in this situation. The existence of "
- " a production environment.  By signing modules, "
+ " a production environment. By signing modules, "
```

</details>

#### V-206387 — Changed

**The web server must encrypt passwords during transmission.**

STIG ID: `SRG-APP-000172-WSR-000104`. Severity: medium → high.
Rule ID: `SV-206387r961029_rule` → `SV-206387r1207727_rule`.
CCI: CCI-000197.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Accepted rule entry; [IA-5(1)][cw-ia-5.1].
- **Baseline / control determinations:** `ia-5.1`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-5.1`: `not-applicable`.

**Changed fields:** severity.

<details>
<summary>Field-by-field text diff</summary>

</details>

#### V-206393 — Changed

**Web server accounts accessing the directory tree, the shell, or other operating system functions and utilities must only be administrative accounts.**

STIG ID: `SRG-APP-000211-WSR-000030`. Severity: medium.
Rule ID: `SV-206393r961095_rule` → `SV-206393r1138072_rule`.
CCI: CCI-001082.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Accepted rule entry; [SC-2][cw-sc-2].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion).

**Changed fields:** discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " server configuration files."
+ " server configuration files.\n\nThis requirement also applies to Zero Trust initiatives."
```

**Check**

```diff
@@ -3,3 +3,3 @@

-If non-privileged web server accounts are available with access to functions, directories, or files not needed
- for the role of the account, this is a finding.
+If nonprivileged web server accounts are available with access to functions, directories, or files not needed
+for the role of the account, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
 Limit the functions, directories, and files that are accessible by each account and role to administrative
-accounts and remove or modify non-privileged account access.
+accounts and remove or modify nonprivileged account access.
```

</details>

#### V-206394 — Changed

**Anonymous user access to the web server application directories must be prohibited.**

STIG ID: `SRG-APP-000211-WSR-000031`. Severity: medium.
Rule ID: `SV-206394r961095_rule` → `SV-206394r1138073_rule`.
CCI: CCI-001082.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Accepted rule entry; [SC-2][cw-sc-2].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "In order to properly monitor the"
+ "To properly monitor the"
- "must be enabled. Along with logging being enabled, each record must"
+ "must be enabled. Additionally, each record must"
- " can be made."
+ " can be made.\n\nThis requirement also applies to Zero Trust initiatives."
```

</details>

#### V-206395 — Changed

**The web server must separate the hosted applications from hosted web server management functionality.**

STIG ID: `SRG-APP-000211-WSR-000129`. Severity: medium.
Rule ID: `SV-206395r961095_rule` → `SV-206395r1138074_rule`.
CCI: CCI-001082.

- **Image criteria:** direct: None; shared-control review: [IMG-27].
- **Crosswalk:** Accepted rule entry; [SC-2][cw-sc-2].
- **Baseline / control determinations:** `sc-2`: `image-owned` (criterion).

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- " address or port.  To further separate "
+ " address or port. To further separate "
- "management functions by non-privileged users during hosted"
+ "management functions by nonprivileged users during hosted"
- " use is minimized."
+ " use is minimized.\n\nThis requirement also applies to Zero Trust initiatives."
```

</details>

#### V-206407 — Changed

**Information at rest must be encrypted using a DOD-accepted algorithm to protect the confidentiality and integrity of the information.**

STIG ID: `SRG-APP-000231-WSR-000144`. Severity: medium.
Rule ID: `SV-206407r961128_rule` → `SV-206407r1029555_rule`.
CCI: CCI-001199.

- **Image criteria:** direct: None; shared-control review: [IMG-15].
- **Crosswalk:** Accepted rule entry; [SC-28][cw-sc-28].
- **Baseline / control determinations:** `sc-28`: `host-inherited` (determination); handoff: [PLT-17].

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "encrypted using a DoD-accepted algorithm to protect"
+ "encrypted using a DOD-accepted algorithm to protect"
```

**Discussion**

```diff
- " is inactive data which is stored physically in"
+ " is inactive data stored physically in"
- "archived data, data which is not accessed"
+ "archived data, data that is not accessed"
- "pieces of data that the web server "
+ "pieces of data the web server "
- "method, such as SHA1, to protect the"
+ "method, such as AES-256, to protect the"
```

**Check**

```diff
@@ -3,5 +3,5 @@

-Verify that the data is encrypted using a DoD-accepted algorithm to protect the confidentiality and integrity
+Verify that the data is encrypted using a DOD-accepted algorithm to protect the confidentiality and integrity
 of the information.

-If the data is not encrypted using a DoD-accepted algorithm, this is a finding.
+If the data is not encrypted using a DOD-accepted algorithm, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-Use a DoD-accepted algorithm to encrypt data at rest to protect the information's confidentiality and
+Use a DOD-accepted algorithm to encrypt data at rest to protect the information's confidentiality and
 integrity.
```

</details>

#### V-206431 — Changed

**The web server must encrypt user identifiers and passwords.**

STIG ID: `SRG-APP-000429-WSR-000113`. Severity: medium → high.
Rule ID: `SV-206431r961602_rule` → `SV-206431r1022705_rule`.
CCI: CCI-002476.

- **Image criteria:** direct: None; shared-control review: [IMG-16], [IMG-17].
- **Crosswalk:** Accepted rule entry; [SC-28(1)][cw-sc-28.1].
- **Baseline / control determinations:** `sc-28.1`: `deployment-configured` (expectation); handoff: [PLT-06].

**Changed fields:** severity.

<details>
<summary>Field-by-field text diff</summary>

</details>

#### V-206443 — Changed

**The web server must install security-relevant software updates within 30 days unless the time period is directed by an authoritative source (e.g., IAVM, CTOs, DTMs, STIGs).**

STIG ID: `SRG-APP-000456-WSR-000187`. Severity: medium.
Rule ID: `SV-206443r961683_rule` → `SV-206443r1138080_rule`.
CCI: CCI-002605.

- **Image criteria:** direct: None; shared-control review: [IMG-25], [IMG-26], [IMG-29].
- **Crosswalk:** Accepted rule entry; [SI-2][cw-si-2].
- **Baseline / control determinations:** `si-2`: `image-owned` (criterion); handoff: [PLT-08].

**Changed fields:** title, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "software updates within the configured time period directed by an"
+ "software updates within 30 days unless the time period is directed by an"
- "IAVM, CTOs, DTMs, and STIGs)."
+ "IAVM, CTOs, DTMs, STIGs)."
```

**Check**

```diff
@@ -1,4 +1,5 @@
-Review the web server documentation and configuration to determine if the web server checks for patches from
-an authoritative source at least every 30 days.
+Verify the web server installs security-relevant software updates within 30 days unless the time period is
+directed by an authoritative source (e.g., IAVM, CTOs, DTMs, STIGs).

-If there is no timeframe or the timeframe is greater than 30 days, this is a finding.
+If security-relevant software updates to the web server are not installed within 30 days, unless the time
+period is directed by an authoritative source, this is a finding.
```

**Fix**

```diff
@@ -1 +1,2 @@
-Configure the web server to check for patches and updates from an authoritative source at least every 30 days.
+Install security-relevant web server updates within 30 days unless the time period is directed by an
+authoritative source (e.g., IAVM, CTOs, DTMs, STIGs).
```

</details>

### Web Server SRG: revision-ID-only changes

These have identical compared content, severity and CCIs. They require no
criterion or control-determination change on this evidence; accepted rendered
crosswalk rule content is unchanged. A later regeneration may change rule IDs.

| Group ID | Old Rule ID | Candidate Rule ID |
| --- | --- | --- |
| V-206361 | `SV-206361r960897_rule` | `SV-206361r1022706_rule` |
| V-206386 | `SV-206386r960966_rule` | `SV-206386r1043177_rule` |
| V-206396 | `SV-206396r961113_rule` | `SV-206396r1043179_rule` |
| V-206397 | `SV-206397r961116_rule` | `SV-206397r1043180_rule` |
| V-206398 | `SV-206398r961116_rule` | `SV-206398r1043180_rule` |
| V-206399 | `SV-206399r961119_rule` | `SV-206399r1043181_rule` |
| V-206400 | `SV-206400r961119_rule` | `SV-206400r1043181_rule` |
| V-206401 | `SV-206401r961119_rule` | `SV-206401r1043181_rule` |
| V-206402 | `SV-206402r961119_rule` | `SV-206402r1043181_rule` |
| V-206403 | `SV-206403r961119_rule` | `SV-206403r1043181_rule` |
| V-206414 | `SV-206414r962268_rule` | `SV-206414r1043182_rule` |
| V-206415 | `SV-206415r961221_rule` | `SV-206415r1043182_rule` |
| V-239371 | `SV-239371r962034_rule` | `SV-239371r1117186_rule` |

<a id="disa-openshift-stig"></a>

## OpenShift STIG — V2R6 → V2R7

**Adopt with changes.** 0 added, 0 removed, 5 changed. Comparison: pinned ZIP XCCDF → candidate XCCDF.

Of the 5 changed rules, 3 change check, fix, severity or CCI; 2 change only title/discussion/STIG ID.

OpenShift is pinned but not yet rendered or joined. All rule-to-control
joins here are prospective. The product baseline and PLT-06's encrypted keystore handoff should be
reviewed on adoption; no changed Group ID is directly anchored by an image
criterion.

### OpenShift STIG: added

None.

### OpenShift STIG: removed

None.

### OpenShift STIG: changed

#### V-257516 — Changed

**OpenShift must display the Standard Mandatory DoW Notice and Consent Banner before granting access to platform components.**

STIG ID: `CNTR-OS-000130`. Severity: low.
Rule ID: `SV-257516r960843_rule` → `SV-257516r1262597_rule`.
CCI: CCI-000048.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AC-8][cw-ac-8].
- **Baseline / control determinations:** `ac-8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ac-8`: `not-applicable`.

**Changed fields:** title, discussion, check, fix.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "the Standard Mandatory DOD Notice and Consent"
+ "the Standard Mandatory DoW Notice and Consent"
```

**Discussion**

```diff
- "presented with a DOD-approved use notification banner"
+ "presented with a DoW-approved use notification banner"
```

**Check**

```diff
@@ -1,2 +1,2 @@
-To verify the OpenShift CLI tool is configured to display the DOD Notice and Consent Banner, do either of the
+To verify the OpenShift CLI tool is configured to display the DoW Notice and Consent Banner, do either of the
 following steps:
@@ -8,3 +8,3 @@

-If the DOD Notice and Consent Banner is not displayed, this is a finding.
+If the DoW Notice and Consent Banner is not displayed, this is a finding.

@@ -12,3 +12,3 @@

-Verify that motd config map exists and contains the DOD Notice and Consent Banner by executing the following:
+Verify that motd config map exists and contains the DoW Notice and Consent Banner by executing the following:

@@ -16,3 +16,3 @@

-If the configmap does not exist, or it does not contain the DOD Notice and Consent Banner text in the message
+If the configmap does not exist, or it does not contain the DoW Notice and Consent Banner text in the message
 data attribute, this is a finding.
```

**Fix**

```diff
@@ -1,2 +1,2 @@
-The following command will create a configmap that displays the DOD Notice and Consent Banner when logging in
+The following command will create a configmap that displays the DoW Notice and Consent Banner when logging in
 using the OpenShift CLI tool by executing the following:
```

</details>

#### V-257517 — Changed

**OpenShift must generate audit records for all DoW-defined auditable events within all components in the platform.**

STIG ID: `CNTR-OS-000150`. Severity: medium.
Rule ID: `SV-257517r1208201_rule` → `SV-257517r1262598_rule`.
CCI: CCI-000135, CCI-000169, CCI-000171, CCI-000172, CCI-000366.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-3(1)][cw-au-3.1], [AU-12][cw-au-12], [CM-6][cw-cm-6].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13]; `au-3.1`: `research-required` (undetermined); `cm-6`: `research-required` (determination).
- **Reference image decisions to review:** `au-12`: `image-owned`; `au-3.1`: `deployment-configured`; `cm-6`: `research-required`.

**Changed fields:** title.

<details>
<summary>Field-by-field text diff</summary>

**Title**

```diff
- "records for all DOD-defined auditable events within"
+ "records for all DoW-defined auditable events within"
```

</details>

#### V-257542 — Changed

**OpenShift must use FIPS-validated SHA-1 or higher hash function to provide replay-resistant authentication mechanisms for network access to privileged accounts.**

STIG ID: `CNTR-OS-000440`. Severity: medium.
Rule ID: `SV-257542r960993_rule` → `SV-257542r1262599_rule`.
CCI: CCI-001941.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [IA-2(8)][cw-ia-2.8].
- **Baseline / control determinations:** `ia-2.8`: `research-required` (undetermined).
- **Reference image decisions to review:** `ia-2.8`: `not-applicable`.

**Changed fields:** discussion.

<details>
<summary>Field-by-field text diff</summary>

**Discussion**

```diff
- "assured. Use of DOD PKI is inherently"
+ "assured. Use of DoW PKI is inherently"
```

</details>

#### V-257564 — Changed

**OpenShift keystore must implement encryption to prevent unauthorized disclosure of information at rest within the container platform.**

STIG ID: `CNTR-OS-000780`. Severity: medium.
Rule ID: `SV-257564r1050650_rule` → `SV-257564r1262594_rule`.
CCI: CCI-002476.

- **Image criteria:** direct: None; shared-control review: [IMG-16], [IMG-17].
- **Crosswalk:** Prospective only; no accepted rule entry; [SC-28(1)][cw-sc-28.1].
- **Baseline / control determinations:** `sc-28.1`: `deployment-configured` (expectation); handoff: [PLT-06].

**Changed fields:** fix.

<details>
<summary>Field-by-field text diff</summary>

**Fix**

```diff
@@ -9,3 +9,2 @@

-Additional details about the configuration can be found in the documentation:
-https://docs.openshift.com/container-platform/4.8/security/encrypting-etcd.html
+Additional details about the configuration can be found in the OpenShift documentation.
```

</details>

#### V-257580 — Changed

**Red Hat Enterprise Linux CoreOS (RHCOS) must be configured to audit the loading and unloading of dynamic kernel modules.**

STIG ID: `CNTR-OS-000980`. Severity: medium.
Rule ID: `SV-257580r961827_rule` → `SV-257580r1262592_rule`.
CCI: CCI-000172.

- **Image criteria:** direct: None; shared-control review: None.
- **Crosswalk:** Prospective only; no accepted rule entry; [AU-12][cw-au-12].
- **Baseline / control determinations:** `au-12`: `research-required` (determination); handoff: [PLT-13].
- **Reference image decisions to review:** `au-12`: `image-owned`.

**Changed fields:** check.

<details>
<summary>Field-by-field text diff</summary>

**Check**

```diff
@@ -7,13 +7,6 @@
 Confirm the following rules exist on each node.
-
+-a always,exit -F arch=b64 -S delete_module -F key=module-unload
+-a always,exit -F arch=b64 -S init_module,finit_module -F key=module-load
 -a always,exit -F arch=b32 -S init_module,finit_module -F key=module-load
--a always,exit -F arch=b64 -S init_module,finit_module -F key=module-load
 -a always,exit -F arch=b32 -S delete_module -F key=module-unload
--a always,exit -F arch=b64 -S delete_module -F key=module-unload
--a always,exit -F arch=b32 -S delete_module -k module-change
--a always,exit -F arch=b64 -S delete_module -k module-change
--a always,exit -F arch=b32 -S finit_module -k module-change
--a always,exit -F arch=b64 -S finit_module -k module-change
--a always,exit -F arch=b32 -S init_module -k module-change
--a always,exit -F arch=b64 -S init_module -k module-change

```

</details>

### OpenShift STIG: revision-ID-only changes

None.


## Validation

`python3 -m unittest discover -s tests` passed: **171 tests**. All Python
commands in `.github/workflows/ci.yml` also passed: its explicit unittest
selection (171 tests), reference revision, control statements, inspection list,
package diagrams, package structure and standard diagrams. Local execution used
Python 3.11.2; the PR workflow uses Python 3.13 and performs the zizmor audit.
The source verifier's expected exit 2 and exact output are recorded above.
A separate report check verified all 294 per-rule entries, local links and
criterion anchors. The final diff is limited to this report and the roadmap.

## Adoption boundary

The owner can accept, amend or reject each recommendation independently. Any
accepted source update belongs in a separate PR that records the new package
and XCCDF identities, regenerates the crosswalk before the catalogues, updates
removed Group ID anchors and applicable determinations, and reviews the
resulting image requirements. This report approves none of those changes.
The existing pins and generated material deliberately remain the reference
baseline while that decision is pending.

[IMG-33]: ../standard/criteria.md#img-33-source-is-protected-and-traceable
[IMG-34]: ../standard/criteria.md#img-34-source-and-dependencies-are-scanned-before-build
[IMG-35]: ../standard/criteria.md#img-35-the-pipeline-is-pinned-and-least-privileged
[IMG-01]: ../standard/criteria.md#img-01-base-image-pinned-by-digest
[IMG-02]: ../standard/criteria.md#img-02-every-build-input-pinned-and-verified
[IMG-03]: ../standard/criteria.md#img-03-hermetic-assembly
[IMG-04]: ../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change
[IMG-29]: ../standard/criteria.md#img-29-base-kept-current
[IMG-05]: ../standard/criteria.md#img-05-no-secrets-in-the-build
[IMG-06]: ../standard/criteria.md#img-06-no-package-manager
[IMG-07]: ../standard/criteria.md#img-07-only-what-the-function-needs
[IMG-27]: ../standard/criteria.md#img-27-no-remote-administration
[IMG-08]: ../standard/criteria.md#img-08-embedded-package-inventory
[IMG-09]: ../standard/criteria.md#img-09-no-privilege-raising-files
[IMG-10]: ../standard/criteria.md#img-10-software-and-configuration-not-writable-by-the-service
[IMG-11]: ../standard/criteria.md#img-11-non-root-with-no-privilege-transition
[IMG-12]: ../standard/criteria.md#img-12-runs-under-an-arbitrary-uid
[IMG-13]: ../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges
[IMG-31]: ../standard/criteria.md#img-31-admitted-under-the-restricted-v2-scc-and-the-restricted-pod-security-standard
[IMG-32]: ../standard/criteria.md#img-32-runs-in-a-user-namespace-under-the-restricted-v3-scc
[IMG-14]: ../standard/criteria.md#img-14-unprivileged-ports
[IMG-15]: ../standard/criteria.md#img-15-read-only-root-filesystem
[IMG-16]: ../standard/criteria.md#img-16-secrets-only-as-read-only-files
[IMG-17]: ../standard/criteria.md#img-17-trust-material-supplied-by-the-operator
[IMG-18]: ../standard/criteria.md#img-18-fails-closed
[IMG-19]: ../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets
[IMG-20]: ../standard/criteria.md#img-20-lifecycle-is-declared
[IMG-30]: ../standard/criteria.md#img-30-expected-behaviour-is-declared
[IMG-21]: ../standard/criteria.md#img-21-bill-of-materials
[IMG-22]: ../standard/criteria.md#img-22-signed-with-provenance
[IMG-23]: ../standard/criteria.md#img-23-identifying-labels
[IMG-24]: ../standard/criteria.md#img-24-immutable-tags
[IMG-25]: ../standard/criteria.md#img-25-vulnerability-gate-and-remediation
[IMG-28]: ../standard/criteria.md#img-28-malware-scan
[IMG-26]: ../standard/criteria.md#img-26-exceptions-expire
[IMG-T1]: ../standard/criteria.md#img-t1-no-shell
[IMG-T2]: ../standard/criteria.md#img-t2-reproducible-build
[IMG-T4]: ../standard/criteria.md#img-t4-slsa-build-level-3
[IMG-T3]: ../standard/criteria.md#img-t3-compliance-scan
[PLT-01]: ../standard/platform.md#plt-01-images-are-admitted-by-verified-digest
[PLT-02]: ../standard/platform.md#plt-02-least-privilege-is-imposed
[PLT-03]: ../standard/platform.md#plt-03-the-root-filesystem-is-read-only
[PLT-04]: ../standard/platform.md#plt-04-ports-are-non-privileged-and-declared
[PLT-05]: ../standard/platform.md#plt-05-resources-are-bounded
[PLT-06]: ../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files
[PLT-07]: ../standard/platform.md#plt-07-containers-are-isolated
[PLT-08]: ../standard/platform.md#plt-08-images-are-scanned-and-replaced
[PLT-09]: ../standard/platform.md#plt-09-logs-are-collected-centrally
[PLT-10]: ../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted
[PLT-11]: ../standard/platform.md#plt-11-stops-are-given-time-to-finish
[PLT-12]: ../standard/platform.md#plt-12-registry-access-is-controlled-and-audited
[PLT-13]: ../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited
[PLT-14]: ../standard/platform.md#plt-14-workloads-are-placed-by-sensitivity
[PLT-15]: ../standard/platform.md#plt-15-nodes-are-trusted-before-they-run-workloads
[PLT-16]: ../standard/platform.md#plt-16-runtime-behaviour-is-monitored
[PLT-17]: ../standard/platform.md#plt-17-data-volumes-are-encrypted-at-rest
[PLT-18]: ../standard/platform.md#plt-18-workloads-have-identities-and-authenticate-each-other
[HST-01]: ../standard/platform.md#hst-01-the-host-runs-containers-and-nothing-else
[HST-02]: ../standard/platform.md#hst-02-the-host-is-current-and-immutable
[HST-03]: ../standard/platform.md#hst-03-host-access-is-audited
[HST-04]: ../standard/platform.md#hst-04-trust-is-rooted-in-hardware
[HST-05]: ../standard/platform.md#hst-05-clocks-are-synchronized
[cw-ac-10]: ../crosswalk/controls/ac-10.md
[cw-ac-11.1]: ../crosswalk/controls/ac-11.1.md
[cw-ac-11]: ../crosswalk/controls/ac-11.md
[cw-ac-12.1]: ../crosswalk/controls/ac-12.1.md
[cw-ac-12.2]: ../crosswalk/controls/ac-12.2.md
[cw-ac-12]: ../crosswalk/controls/ac-12.md
[cw-ac-16.1]: ../crosswalk/controls/ac-16.1.md
[cw-ac-16]: ../crosswalk/controls/ac-16.md
[cw-ac-17.1]: ../crosswalk/controls/ac-17.1.md
[cw-ac-17.2]: ../crosswalk/controls/ac-17.2.md
[cw-ac-17.9]: ../crosswalk/controls/ac-17.9.md
[cw-ac-18.1]: ../crosswalk/controls/ac-18.1.md
[cw-ac-2.1]: ../crosswalk/controls/ac-2.1.md
[cw-ac-2.11]: ../crosswalk/controls/ac-2.11.md
[cw-ac-2.2]: ../crosswalk/controls/ac-2.2.md
[cw-ac-2.3]: ../crosswalk/controls/ac-2.3.md
[cw-ac-2.4]: ../crosswalk/controls/ac-2.4.md
[cw-ac-3.13]: ../crosswalk/controls/ac-3.13.md
[cw-ac-3.4]: ../crosswalk/controls/ac-3.4.md
[cw-ac-3.7]: ../crosswalk/controls/ac-3.7.md
[cw-ac-3]: ../crosswalk/controls/ac-3.md
[cw-ac-4.17]: ../crosswalk/controls/ac-4.17.md
[cw-ac-4]: ../crosswalk/controls/ac-4.md
[cw-ac-6.10]: ../crosswalk/controls/ac-6.10.md
[cw-ac-6.8]: ../crosswalk/controls/ac-6.8.md
[cw-ac-6.9]: ../crosswalk/controls/ac-6.9.md
[cw-ac-7]: ../crosswalk/controls/ac-7.md
[cw-ac-8]: ../crosswalk/controls/ac-8.md
[cw-au-10]: ../crosswalk/controls/au-10.md
[cw-au-12.1]: ../crosswalk/controls/au-12.1.md
[cw-au-12.3]: ../crosswalk/controls/au-12.3.md
[cw-au-12]: ../crosswalk/controls/au-12.md
[cw-au-14.1]: ../crosswalk/controls/au-14.1.md
[cw-au-3.1]: ../crosswalk/controls/au-3.1.md
[cw-au-3]: ../crosswalk/controls/au-3.md
[cw-au-4.1]: ../crosswalk/controls/au-4.1.md
[cw-au-4]: ../crosswalk/controls/au-4.md
[cw-au-5.1]: ../crosswalk/controls/au-5.1.md
[cw-au-5.2]: ../crosswalk/controls/au-5.2.md
[cw-au-5]: ../crosswalk/controls/au-5.md
[cw-au-6.4]: ../crosswalk/controls/au-6.4.md
[cw-au-7.1]: ../crosswalk/controls/au-7.1.md
[cw-au-7]: ../crosswalk/controls/au-7.md
[cw-au-8]: ../crosswalk/controls/au-8.md
[cw-au-9.2]: ../crosswalk/controls/au-9.2.md
[cw-au-9.3]: ../crosswalk/controls/au-9.3.md
[cw-au-9.5]: ../crosswalk/controls/au-9.5.md
[cw-au-9]: ../crosswalk/controls/au-9.md
[cw-cm-11.2]: ../crosswalk/controls/cm-11.2.md
[cw-cm-14]: ../crosswalk/controls/cm-14.md
[cw-cm-3.5]: ../crosswalk/controls/cm-3.5.md
[cw-cm-5.1]: ../crosswalk/controls/cm-5.1.md
[cw-cm-5.6]: ../crosswalk/controls/cm-5.6.md
[cw-cm-6]: ../crosswalk/controls/cm-6.md
[cw-cm-7.1]: ../crosswalk/controls/cm-7.1.md
[cw-cm-7.2]: ../crosswalk/controls/cm-7.2.md
[cw-cm-7.5]: ../crosswalk/controls/cm-7.5.md
[cw-cm-7.9]: ../crosswalk/controls/cm-7.9.md
[cw-cm-7]: ../crosswalk/controls/cm-7.md
[cw-ia-11]: ../crosswalk/controls/ia-11.md
[cw-ia-2.1]: ../crosswalk/controls/ia-2.1.md
[cw-ia-2.12]: ../crosswalk/controls/ia-2.12.md
[cw-ia-2.2]: ../crosswalk/controls/ia-2.2.md
[cw-ia-2.5]: ../crosswalk/controls/ia-2.5.md
[cw-ia-2.6]: ../crosswalk/controls/ia-2.6.md
[cw-ia-2.8]: ../crosswalk/controls/ia-2.8.md
[cw-ia-2]: ../crosswalk/controls/ia-2.md
[cw-ia-3.1]: ../crosswalk/controls/ia-3.1.md
[cw-ia-3]: ../crosswalk/controls/ia-3.md
[cw-ia-5.1]: ../crosswalk/controls/ia-5.1.md
[cw-ia-5.13]: ../crosswalk/controls/ia-5.13.md
[cw-ia-5.2]: ../crosswalk/controls/ia-5.2.md
[cw-ia-6]: ../crosswalk/controls/ia-6.md
[cw-ia-7]: ../crosswalk/controls/ia-7.md
[cw-ia-8.1]: ../crosswalk/controls/ia-8.1.md
[cw-ia-8.2]: ../crosswalk/controls/ia-8.2.md
[cw-ia-8.4]: ../crosswalk/controls/ia-8.4.md
[cw-ia-8]: ../crosswalk/controls/ia-8.md
[cw-ma-3.5]: ../crosswalk/controls/ma-3.5.md
[cw-ma-4.1]: ../crosswalk/controls/ma-4.1.md
[cw-ma-4.4]: ../crosswalk/controls/ma-4.4.md
[cw-ma-4.6]: ../crosswalk/controls/ma-4.6.md
[cw-ma-4.7]: ../crosswalk/controls/ma-4.7.md
[cw-ma-4]: ../crosswalk/controls/ma-4.md
[cw-pt-2.1]: ../crosswalk/controls/pt-2.1.md
[cw-pt-3.1]: ../crosswalk/controls/pt-3.1.md
[cw-ra-5.5]: ../crosswalk/controls/ra-5.5.md
[cw-sa-22]: ../crosswalk/controls/sa-22.md
[cw-sc-10]: ../crosswalk/controls/sc-10.md
[cw-sc-13]: ../crosswalk/controls/sc-13.md
[cw-sc-17]: ../crosswalk/controls/sc-17.md
[cw-sc-18.1]: ../crosswalk/controls/sc-18.1.md
[cw-sc-2]: ../crosswalk/controls/sc-2.md
[cw-sc-23.1]: ../crosswalk/controls/sc-23.1.md
[cw-sc-23.3]: ../crosswalk/controls/sc-23.3.md
[cw-sc-23.5]: ../crosswalk/controls/sc-23.5.md
[cw-sc-23]: ../crosswalk/controls/sc-23.md
[cw-sc-24]: ../crosswalk/controls/sc-24.md
[cw-sc-28.1]: ../crosswalk/controls/sc-28.1.md
[cw-sc-28.3]: ../crosswalk/controls/sc-28.3.md
[cw-sc-28]: ../crosswalk/controls/sc-28.md
[cw-sc-3]: ../crosswalk/controls/sc-3.md
[cw-sc-39]: ../crosswalk/controls/sc-39.md
[cw-sc-4]: ../crosswalk/controls/sc-4.md
[cw-sc-45.1]: ../crosswalk/controls/sc-45.1.md
[cw-sc-45]: ../crosswalk/controls/sc-45.md
[cw-sc-5.1]: ../crosswalk/controls/sc-5.1.md
[cw-sc-5.2]: ../crosswalk/controls/sc-5.2.md
[cw-sc-5]: ../crosswalk/controls/sc-5.md
[cw-sc-8.1]: ../crosswalk/controls/sc-8.1.md
[cw-sc-8.2]: ../crosswalk/controls/sc-8.2.md
[cw-sc-8]: ../crosswalk/controls/sc-8.md
[cw-si-10.3]: ../crosswalk/controls/si-10.3.md
[cw-si-10]: ../crosswalk/controls/si-10.md
[cw-si-11]: ../crosswalk/controls/si-11.md
[cw-si-16]: ../crosswalk/controls/si-16.md
[cw-si-2.6]: ../crosswalk/controls/si-2.6.md
[cw-si-2]: ../crosswalk/controls/si-2.md
[cw-si-4.3]: ../crosswalk/controls/si-4.3.md
[cw-si-6]: ../crosswalk/controls/si-6.md
