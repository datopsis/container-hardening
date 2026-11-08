# 2026-11 DISA adoption

The owner directed adoption of all six releases in the
[drift report](2026-11-disa-refresh.md), including RHEL 9. The report remains
historical comparison evidence; its earlier hold recommendation is superseded
by this source decision. This is a draft reference standard, not a CI adoption
requirement, certification, or authorization.

All six downloaded ZIPs and XCCDFs matched the report's SHA-256 digests and ZIP
sizes on 2026-11-08. The register records benchmark, acceptance, and retrieval
dates separately. The existing generators accept the complete input set,
including RHEL 9; rendering adds reference material without changing ownership.

| Source | Adopted release | Rendered rules | Standard changes |
| --- | --- | ---: | --- |
| GPOS | V3R3 → V3R4 | 202 | IMG-27: V-203655 → V-278973; IMG-01/IMG-29: V-278977 → V-282963 |
| Container Platform | V2R4 → V2R5 | 188 | No image criterion or origination change |
| Application Server | V4R5 → V4R6 | 137 | PLT-09 records V-204833's CAT I priority; no image criterion change |
| Web Server | V3R3 → V4R5 | 126 | CCI-003992 repairs CM-14 for V-206372/V-206373; no image criterion change |
| OpenShift | V2R6 → V2R7 | 83 | PLT-06 records the IMG-16/IMG-17 scope review; no image criterion change |
| RHEL 9 | V2R4 → V2R10 | 445 | Host reference only; no image criterion change |

Database V4R6 (142 rules), API V1R1 (65), and ASD V6R5 (286), already pinned
in PR #23, also render now that the complete input set is available. Their
optional, conditional-reference status is unchanged. Kubernetes stays at its
existing pin and rendering state.

## Mechanical review

**GPOS scope.** V-278973 preserves the separation of user and management
functionality, STIG ID and CCI-001082/SC-2 of removed V-203655, and explicitly
includes Zero Trust. IMG-27's absence of remote administration still contributes
to that separation; it does not claim to satisfy the whole Zero Trust scope.
V-282963 preserves V-278977's STIG ID, title, severity and CCI/SA-22. Repointing
IMG-01/IMG-29 preserves their existing unsupported-software requirement.

**IA-5(1).** GPOS V-203632 and Container Platform V-233098 change a maximum
password lifetime from 60 to 180 days. No image criterion sets that lifetime;
IA-5(1) remains `research-required`. Adoption does not relax local policy.

**IA-7.** GPOS V-203649's discussion now refers only to FIPS 140-3, while
Application Server V-204758 still names FIPS 140-2 in its title. IA-7 and the
image cryptographic position remain unresolved. Calling an algorithm approved
is not evidence of module validation. No FIPS claim or determination changes.

**Application Server.** V-204833's CAT II → CAT I promotion concerns audit
record off-loading, AU-4(1). PLT-09 records that priority for applicable
assessments and the logging handoff. Function-specific applicability remains
necessary; no universal image obligation is added.

**Web Server.** V-206372/V-206373 now cite CCI-003992/CM-14 instead of unmapped
CCI-001749. Removing V-206420 removes the third old crosswalk finding, not an
underlying control. The generated join supplies the repair without a local
mapping override. The at-rest encryption example in V-206407 now says AES-256.

**OpenShift.** V-257564 changes a documentation pointer, not the keystore
requirement. IMG-16/IMG-17 cover mounted secrets/trust material; keystore
configuration remains with PLT-06. V-257580's four b32/b64 module load/unload
audit rules concern nodes, not the image or its logging configuration.

## Owner judgment

These decisions remain unchanged and unreviewed by this adoption:

- Identity owners must decide whether the GPOS/platform 180-day password
  maximum changes any local policy. A stricter maximum remains compatible.
- Resolve the IA-7/SC-13 FIPS position and the inconsistent GPOS/Application
  Server wording; obtain actual validation evidence where applicable.
- Rebuild Web Server applicability worksheets by Group ID: seven HTTP/session
  rekeys, 25 other additions, authentication/audit/key-storage obligations, and
  V-206387/V-206431's CAT I priority need application-owner assessment.
- Review V-206443's requirement to **install** updates within 30 days against
  IMG-04/IMG-22 and release evidence. The current standard and reference image
  do not gain a compliance claim from this source change.
- Have the OpenShift platform owner update node audit evidence for V-257580
  and identify the appropriate version's encryption documentation for V-257564.
- Decide RHEL host/UBI applicability, crypto and audit changes, replacement of
  removed requirements, and future IMG-T3 tailoring. The eight CAT I promotions
  and all 26 CCIs without a Rev 5 mapping are listed in the
  [roadmap](../ROADMAP.md#package-1-sources-and-rendering). No host check moves
  onto an image and no removed rule is a waiver.
- The reference image's 57 control decisions, including AU-10, TLS-dependent
  controls, SC-10 and IA-7, still need owner review. No review signature or date
  is supplied by this adoption.
