# SRG to NIST SP 800-53 crosswalk

Every SRG rule cites one or more CCIs, and the DISA CCI list maps each CCI to NIST SP 800-53 Rev 5. This crosswalk is the join of the two. No cross-reference here is hand-authored: each follows from the pinned sources, and it inherits DISA's judgement, errors included.

| Input | Revision |
| --- | --- |
| DISA CCI list | 2025-01-23 |
| NIST SP 800-53 Rev 5 catalogue | 5.2.0 |
| Container Platform Security Requirements Guide | V2R4 |
| General Purpose Operating System Security Requirements Guide | V3R3 |

Each input is pinned by SHA-256 in [`artifacts/sources.json`](../../artifacts/sources.json), and the generator refuses to map against one that does not match. The machine-readable form is [`artifacts/crosswalk.json`](../../artifacts/crosswalk.json).

## Coverage

| Catalogue | Rules | CCIs cited | Controls reached | Of which High baseline |
| --- | ---: | ---: | ---: | ---: |
| [Container Platform Security Requirements Guide](../srg/container-platform-srg/README.md) | 188 | 127 | 80 | 60 |
| [General Purpose Operating System Security Requirements Guide](../srg/general-purpose-operating-system-srg/README.md) | 203 | 157 | 97 | 66 |

## Findings

Every rule cites at least one CCI, and every CCI cited is current in the CCI list and carries at least one Rev 5 reference.

## Controls

Rule counts per catalogue. A control outside the High baseline is still reached by an SRG; the baseline does not select it.

| Control | Title | High | Container Platform Security Requirements Guide | General Purpose Operating System Security Requirements Guide |
| --- | --- | :-: | ---: | ---: |
| [AC-2(1)](controls/ac-2.1.md) | Automated System Account Management | Yes | 6 | 6 |
| [AC-2(2)](controls/ac-2.2.md) | Automated Temporary and Emergency Account Management | Yes | 2 | 2 |
| [AC-2(3)](controls/ac-2.3.md) | Disable Accounts | Yes | 3 | 2 |
| [AC-2(4)](controls/ac-2.4.md) | Automated Audit Actions | Yes | 5 | 5 |
| [AC-2(11)](controls/ac-2.11.md) | Usage Conditions | Yes | 1 |  |
| [AC-3](controls/ac-3.md) | Access Enforcement | Yes | 3 | 1 |
| [AC-3(4)](controls/ac-3.4.md) | Discretionary Access Control | No |  | 3 |
| [AC-3(7)](controls/ac-3.7.md) | Role-based Access Control | No |  | 1 |
| [AC-3(13)](controls/ac-3.13.md) | Attribute-based Access Control | No |  | 1 |
| [AC-4](controls/ac-4.md) | Information Flow Enforcement | Yes | 2 |  |
| [AC-6(8)](controls/ac-6.8.md) | Privilege Levels for Code Execution | No | 1 | 1 |
| [AC-6(9)](controls/ac-6.9.md) | Log Use of Privileged Functions | Yes | 1 | 1 |
| [AC-6(10)](controls/ac-6.10.md) | Prohibit Non-privileged Users from Executing Privileged Functions | Yes | 1 | 1 |
| [AC-7](controls/ac-7.md) | Unsuccessful Logon Attempts | Yes | 2 | 2 |
| [AC-8](controls/ac-8.md) | System Use Notification | Yes | 2 | 3 |
| [AC-10](controls/ac-10.md) | Concurrent Session Control | Yes |  | 1 |
| [AC-11](controls/ac-11.md) | Device Lock | Yes |  | 3 |
| [AC-11(1)](controls/ac-11.1.md) | Pattern-hiding Displays | Yes |  | 1 |
| [AC-12](controls/ac-12.md) | Session Termination | Yes |  | 1 |
| [AC-12(1)](controls/ac-12.1.md) | User-initiated Logouts | No |  | 1 |
| [AC-12(2)](controls/ac-12.2.md) | Termination Message | No | 1 | 1 |
| [AC-17(1)](controls/ac-17.1.md) | Monitoring and Control | Yes |  | 2 |
| [AC-17(2)](controls/ac-17.2.md) | Protection of Confidentiality and Integrity Using Encryption | Yes | 3 | 2 |
| [AC-17(9)](controls/ac-17.9.md) | Disconnect or Disable Access | No |  | 1 |
| [AC-18(1)](controls/ac-18.1.md) | Authentication and Encryption | Yes |  | 2 |
| [AU-3](controls/au-3.md) | Content of Audit Records | Yes | 7 | 6 |
| [AU-3(1)](controls/au-3.1.md) | Additional Audit Information | Yes | 1 | 2 |
| [AU-4](controls/au-4.md) | Audit Log Storage Capacity | Yes | 1 | 1 |
| [AU-4(1)](controls/au-4.1.md) | Transfer to Alternate Storage | No | 1 | 2 |
| [AU-5](controls/au-5.md) | Response to Audit Logging Process Failures | Yes |  | 1 |
| [AU-5(1)](controls/au-5.1.md) | Storage Capacity Warning | Yes | 1 | 1 |
| [AU-5(2)](controls/au-5.2.md) | Real-time Alerts | Yes | 1 | 1 |
| [AU-6(4)](controls/au-6.4.md) | Central Review and Analysis | No | 2 | 1 |
| [AU-7](controls/au-7.md) | Audit Record Reduction and Report Generation | Yes | 1 | 8 |
| [AU-7(1)](controls/au-7.1.md) | Automatic Processing | Yes |  | 1 |
| [AU-8](controls/au-8.md) | Time Stamps | Yes | 3 | 3 |
| [AU-9](controls/au-9.md) | Protection of Audit Information | Yes | 7 | 6 |
| [AU-9(3)](controls/au-9.3.md) | Cryptographic Protection | Yes | 2 | 1 |
| [AU-9(5)](controls/au-9.5.md) | Dual Authorization | No |  | 1 |
| [AU-12](controls/au-12.md) | Audit Record Generation | Yes | 22 | 20 |
| [AU-12(3)](controls/au-12.3.md) | Changes by Authorized Individuals | Yes |  | 1 |
| [AU-14(1)](controls/au-14.1.md) | System Start-up | No | 1 | 1 |
| [CM-3(5)](controls/cm-3.5.md) | Automated Security Response | No |  | 1 |
| [CM-5(1)](controls/cm-5.1.md) | Automated Access Enforcement and Audit Records | Yes | 3 | 2 |
| [CM-5(6)](controls/cm-5.6.md) | Limit Library Privileges | No | 5 | 1 |
| [CM-6](controls/cm-6.md) | Configuration Settings | Yes | 4 | 10 |
| [CM-7](controls/cm-7.md) | Least Functionality | Yes | 5 | 2 |
| [CM-7(1)](controls/cm-7.1.md) | Periodic Review | Yes | 1 |  |
| [CM-7(2)](controls/cm-7.2.md) | Prevent Program Execution | Yes | 1 | 1 |
| [CM-7(5)](controls/cm-7.5.md) | Authorized Software — Allow-by-exception | Yes | 1 | 1 |
| [CM-7(9)](controls/cm-7.9.md) | Prohibiting The Use of Unauthorized Hardware | No |  | 1 |
| [CM-11(2)](controls/cm-11.2.md) | Software Installation with Privileged Status | No | 3 | 1 |
| [CM-14](controls/cm-14.md) | Signed Components | No | 2 | 1 |
| [IA-2](controls/ia-2.md) | Identification and Authentication (Organizational Users) | Yes | 4 | 1 |
| [IA-2(1)](controls/ia-2.1.md) | Multi-factor Authentication to Privileged Accounts | Yes | 2 | 2 |
| [IA-2(2)](controls/ia-2.2.md) | Multi-factor Authentication to Non-privileged Accounts | Yes | 2 | 2 |
| [IA-2(5)](controls/ia-2.5.md) | Individual Authentication with Group Authentication | Yes | 2 | 1 |
| [IA-2(6)](controls/ia-2.6.md) | Access to Accounts —separate Device | No | 2 | 2 |
| [IA-2(8)](controls/ia-2.8.md) | Access to Accounts — Replay Resistant | Yes | 2 | 2 |
| [IA-2(12)](controls/ia-2.12.md) | Acceptance of PIV Credentials | Yes | 1 | 2 |
| [IA-3](controls/ia-3.md) | Device Identification and Authentication | Yes | 1 | 2 |
| [IA-3(1)](controls/ia-3.1.md) | Cryptographic Bidirectional Authentication | No |  | 1 |
| [IA-5(1)](controls/ia-5.1.md) | Password-based Authentication | Yes | 17 | 14 |
| [IA-5(2)](controls/ia-5.2.md) | Public Key-based Authentication | Yes | 3 | 4 |
| [IA-5(13)](controls/ia-5.13.md) | Expiration of Cached Authenticators | No | 1 | 1 |
| [IA-6](controls/ia-6.md) | Authentication Feedback | Yes | 1 | 1 |
| [IA-7](controls/ia-7.md) | Cryptographic Module Authentication | Yes | 1 | 1 |
| [IA-8](controls/ia-8.md) | Identification and Authentication (Non-organizational Users) | Yes |  | 1 |
| [IA-8(1)](controls/ia-8.1.md) | Acceptance of PIV Credentials from Other Agencies | Yes | 1 |  |
| [IA-8(2)](controls/ia-8.2.md) | Acceptance of External Authenticators | Yes |  | 1 |
| [IA-11](controls/ia-11.md) | Re-authentication | Yes | 1 | 3 |
| [MA-3(5)](controls/ma-3.5.md) | Execution with Privilege | No |  | 1 |
| [MA-4](controls/ma-4.md) | Nonlocal Maintenance | Yes | 1 | 1 |
| [MA-4(1)](controls/ma-4.1.md) | Logging and Review | No | 1 | 1 |
| [MA-4(4)](controls/ma-4.4.md) | Authentication and Separation of Maintenance Sessions | No | 1 |  |
| [MA-4(6)](controls/ma-4.6.md) | Cryptographic Protection | No | 2 | 2 |
| [MA-4(7)](controls/ma-4.7.md) | Disconnect Verification | No |  | 1 |
| [RA-5(5)](controls/ra-5.5.md) | Privileged Access | Yes | 1 |  |
| [SA-22](controls/sa-22.md) | Unsupported System Components | Yes | 1 | 1 |
| [SC-2](controls/sc-2.md) | Separation of System and User Functionality | Yes | 1 | 2 |
| [SC-3](controls/sc-3.md) | Security Function Isolation | Yes | 1 | 1 |
| [SC-4](controls/sc-4.md) | Information in Shared System Resources | Yes | 2 | 1 |
| [SC-5](controls/sc-5.md) | Denial-of-service Protection | Yes | 1 | 1 |
| [SC-5(1)](controls/sc-5.1.md) | Restrict Ability to Attack Other Systems | No | 1 |  |
| [SC-5(2)](controls/sc-5.2.md) | Capacity, Bandwidth, and Redundancy | No | 1 | 1 |
| [SC-8](controls/sc-8.md) | Transmission Confidentiality and Integrity | Yes | 1 | 2 |
| [SC-8(1)](controls/sc-8.1.md) | Cryptographic Protection | Yes |  | 1 |
| [SC-8(2)](controls/sc-8.2.md) | Pre- and Post-transmission Handling | No | 2 | 2 |
| [SC-10](controls/sc-10.md) | Network Disconnect | Yes | 1 | 1 |
| [SC-13](controls/sc-13.md) | Cryptographic Protection | Yes | 3 | 3 |
| [SC-17](controls/sc-17.md) | Public Key Infrastructure Certificates | Yes | 1 | 1 |
| [SC-23](controls/sc-23.md) | Session Authenticity | Yes | 1 |  |
| [SC-23(5)](controls/sc-23.5.md) | Allowed Certificate Authorities | No |  | 1 |
| [SC-24](controls/sc-24.md) | Fail in Known State | Yes | 2 | 2 |
| [SC-28](controls/sc-28.md) | Protection of Information at Rest | Yes |  | 1 |
| [SC-28(1)](controls/sc-28.1.md) | Cryptographic Protection | Yes | 1 | 2 |
| [SC-28(3)](controls/sc-28.3.md) | Cryptographic Keys | No | 1 | 1 |
| [SC-39](controls/sc-39.md) | Process Isolation | Yes | 1 |  |
| [SC-45](controls/sc-45.md) | System Time Synchronization | No | 1 | 1 |
| [SC-45(1)](controls/sc-45.1.md) | Synchronization with Authoritative Time Source | No |  | 2 |
| [SI-2](controls/si-2.md) | Flaw Remediation | Yes | 2 | 1 |
| [SI-2(6)](controls/si-2.6.md) | Removal of Previous Versions of Software and Firmware | No | 2 | 1 |
| [SI-6](controls/si-6.md) | Security and Privacy Function Verification | Yes | 3 | 3 |
| [SI-10(3)](controls/si-10.3.md) | Predictable Behavior | No | 1 | 1 |
| [SI-11](controls/si-11.md) | Error Handling | Yes | 1 | 2 |
| [SI-16](controls/si-16.md) | Memory Protection | Yes | 1 | 2 |

Regenerate with `python scripts/build-cci-crosswalk.py`. The weekly source verification runs `--check`, which fails if the committed crosswalk no longer matches the pinned sources.
