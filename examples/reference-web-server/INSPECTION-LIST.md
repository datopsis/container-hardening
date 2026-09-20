# Controls: reference-web-server

Every control in the standard's [baseline](../../docs/controls/README.md), in three
groups: the ones this image must inspect, the ones it inherits, and the ones with
nothing here to apply to. The whole list is here so a reviewer can walk it and
confirm each group, rather than trust that the short list is the right short list.
Generated from this image's [hardening profile](hardening-profile.json), its
[component definition](oscal/component-definition.json), and the standard's
[inspection map](../../artifacts/inspection-map.json) by
`scripts/build-inspection-list.py`; do not edit it by hand.

Inspecting a control is a person's work. What is written here is which controls
that work covers, and where this image's part of each is recorded. Controls and
criteria are many to many: a control is usually divided between the image, its
deployment, the host, and the organization, so the image's part alone never
satisfies one. The parts are in the [control statements](CONTROL-STATEMENTS.md),
and where they are applied in this image is in its
[cyber package](package/README.md).

| Group | Controls | What a reviewer confirms |
| --- | ---: | --- |
| [To inspect](#to-inspect) | 52 | That the image's part is right, and complete |
| [Inherited](#inherited) | 278 | That the platform, host, or organization really does carry it here |
| [Nothing to apply it to](#nothing-to-apply-it-to) | 49 | That the thing the control governs is genuinely absent |
| **Total** | **379** | |

## What this image does

| Capability | Question it answers yes to |
| --- | --- |
| `serves-http` | Does the image answer HTTP requests, for content, an API, or as a proxy? |
| `terminates-tls` | Does the image itself terminate TLS, with key material it is given? |

It declares none of: `authenticates-clients`, `authorizes-by-claims`, `issues-credentials`, `manages-accounts`, `offers-admin-interface`, `processes-untrusted-content`, `runs-several-roles`, `sends-email`, `stores-data`, `talks-to-other-services`, `terminates-mutual-tls`. Each of those
would move controls into the first group below.

## To inspect

The baseline gives these to the image or its deployment, or a capability brings
them in. Each needs an answer of this image's own.

| Control | Title | Who carries it | Inspect because | The image's part |
| --- | --- | --- | --- | --- |
| [AC-14](../../docs/assessment/ac-14.md) | Permitted Actions Without Identification or Authentication | deployment-configured | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [AC-17(2)](../../docs/assessment/ac-17.2.md) | Protection of Confidentiality and Integrity Using Encryption | deployment-configured | terminates tls; the baseline gives it to the image | decided, **not yet reviewed** |
| [AC-3](../../docs/assessment/ac-3.md) | Access Enforcement | deployment-configured | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [AC-4](../../docs/assessment/ac-4.md) | Information Flow Enforcement | deployment-configured | the baseline gives it to the image | statement |
| [AC-4(4)](../../docs/assessment/ac-4.4.md) | Flow Control of Encrypted Information | deployment-configured | the baseline gives it to the image | statement |
| [AC-6](../../docs/assessment/ac-6.md) | Least Privilege | image-owned | the baseline gives it to the image | statement |
| [AC-6(10)](../../docs/assessment/ac-6.10.md) | Prohibit Non-privileged Users from Executing Privileged Functions | image-owned | the baseline gives it to the image | statement |
| [AC-6(8)](../../docs/assessment/ac-6.8.md) | Privilege Levels for Code Execution | image-owned | the baseline gives it to the image | statement |
| [AU-12](../../docs/assessment/au-12.md) | Audit Record Generation | image-owned | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [AU-2](../../docs/assessment/au-2.md) | Event Logging | image-owned | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [AU-3](../../docs/assessment/au-3.md) | Content of Audit Records | image-owned | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [AU-3(1)](../../docs/assessment/au-3.1.md) | Additional Audit Information | deployment-configured | the baseline gives it to the image | decided, **not yet reviewed** |
| [CM-11](../../docs/assessment/cm-11.md) | User-installed Software | image-owned | the baseline gives it to the image | statement |
| [CM-11(2)](../../docs/assessment/cm-11.2.md) | Software Installation with Privileged Status | image-owned | the baseline gives it to the image | statement |
| [CM-14](../../docs/assessment/cm-14.md) | Signed Components | image-owned | the baseline gives it to the image | statement |
| [CM-2](../../docs/assessment/cm-2.md) | Baseline Configuration | image-owned | the baseline gives it to the image | statement |
| [CM-2(2)](../../docs/assessment/cm-2.2.md) | Automation Support for Accuracy and Currency | image-owned | the baseline gives it to the image | statement |
| [CM-2(3)](../../docs/assessment/cm-2.3.md) | Retention of Previous Configurations | image-owned | the baseline gives it to the image | statement |
| [CM-5(1)](../../docs/assessment/cm-5.1.md) | Automated Access Enforcement and Audit Records | deployment-configured | the baseline gives it to the image | statement |
| [CM-5(6)](../../docs/assessment/cm-5.6.md) | Limit Library Privileges | image-owned | the baseline gives it to the image | statement |
| [CM-6](../../docs/assessment/cm-6.md) | Configuration Settings | research-required | the baseline gives it to the image | decided, **not yet reviewed** |
| [CM-6(1)](../../docs/assessment/cm-6.1.md) | Automated Management, Application, and Verification | research-required | the baseline gives it to the image | decided, **not yet reviewed** |
| [CM-7](../../docs/assessment/cm-7.md) | Least Functionality | image-owned | the baseline gives it to the image | statement |
| [CM-8](../../docs/assessment/cm-8.md) | System Component Inventory | image-owned | the baseline gives it to the image | statement |
| [CM-8(1)](../../docs/assessment/cm-8.1.md) | Updates During Installation and Removal | image-owned | the baseline gives it to the image | statement |
| [CM-8(2)](../../docs/assessment/cm-8.2.md) | Automated Maintenance | image-owned | the baseline gives it to the image | statement |
| [IA-5](../../docs/assessment/ia-5.md) | Authenticator Management | deployment-configured | terminates tls; the baseline gives it to the image | decided, **not yet reviewed** |
| [IA-5(6)](../../docs/assessment/ia-5.6.md) | Protection of Authenticators | deployment-configured | terminates tls; the baseline gives it to the image | decided, **not yet reviewed** |
| [SA-22](../../docs/assessment/sa-22.md) | Unsupported System Components | image-owned | the baseline gives it to the image | statement |
| [SC-10](../../docs/assessment/sc-10.md) | Network Disconnect | deployment-configured | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [SC-12](../../docs/assessment/sc-12.md) | Cryptographic Key Establishment and Management | deployment-configured | terminates tls; the baseline gives it to the image | statement |
| [SC-12(1)](../../docs/assessment/sc-12.1.md) | Availability | deployment-configured | the baseline gives it to the image | statement |
| [SC-13](../../docs/assessment/sc-13.md) | Cryptographic Protection | research-required | terminates tls; the baseline gives it to the image | decided, **not yet reviewed** |
| [SC-17](../../docs/assessment/sc-17.md) | Public Key Infrastructure Certificates | deployment-configured | terminates tls; the baseline gives it to the image | statement |
| [SC-18](../../docs/assessment/sc-18.md) | Mobile Code | deployment-configured | the baseline gives it to the image | decided, **not yet reviewed** |
| [SC-2](../../docs/assessment/sc-2.md) | Separation of System and User Functionality | image-owned | the baseline gives it to the image | statement |
| [SC-23](../../docs/assessment/sc-23.md) | Session Authenticity | deployment-configured | terminates tls; the baseline gives it to the image | decided, **not yet reviewed** |
| [SC-24](../../docs/assessment/sc-24.md) | Fail in Known State | image-owned | the baseline gives it to the image | statement |
| [SC-28(1)](../../docs/assessment/sc-28.1.md) | Cryptographic Protection | deployment-configured | the baseline gives it to the image | statement |
| [SC-28(3)](../../docs/assessment/sc-28.3.md) | Cryptographic Keys | deployment-configured | the baseline gives it to the image | statement |
| [SC-5](../../docs/assessment/sc-5.md) | Denial-of-service Protection | deployment-configured | serves or proxies http; the baseline gives it to the image | statement |
| [SC-5(2)](../../docs/assessment/sc-5.2.md) | Capacity, Bandwidth, and Redundancy | deployment-configured | the baseline gives it to the image | statement |
| [SC-7](../../docs/assessment/sc-7.md) | Boundary Protection | deployment-configured | the baseline gives it to the image | statement |
| [SC-7(5)](../../docs/assessment/sc-7.5.md) | Deny by Default — Allow by Exception | deployment-configured | the baseline gives it to the image | statement |
| [SC-7(8)](../../docs/assessment/sc-7.8.md) | Route Traffic to Authenticated Proxy Servers | deployment-configured | the baseline gives it to the image | statement |
| [SC-8](../../docs/assessment/sc-8.md) | Transmission Confidentiality and Integrity | deployment-configured | terminates tls; the baseline gives it to the image | decided, **not yet reviewed** |
| [SC-8(1)](../../docs/assessment/sc-8.1.md) | Cryptographic Protection | deployment-configured | terminates tls; the baseline gives it to the image | decided, **not yet reviewed** |
| [SI-10](../../docs/assessment/si-10.md) | Information Input Validation | research-required | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [SI-11](../../docs/assessment/si-11.md) | Error Handling | research-required | serves or proxies http; the baseline gives it to the image | decided, **not yet reviewed** |
| [SI-2](../../docs/assessment/si-2.md) | Flaw Remediation | image-owned | the baseline gives it to the image | statement |
| [SI-2(6)](../../docs/assessment/si-2.6.md) | Removal of Previous Versions of Software and Firmware | image-owned | the baseline gives it to the image | statement |
| [SI-7(15)](../../docs/assessment/si-7.15.md) | Code Authentication | image-owned | the baseline gives it to the image | statement |

## Inherited

Carried by the platform, the host, or the organization. The image contributes to
some of them; none is this image's to answer alone. A reviewer confirms the
inheritance is real for this deployment, not assumed.

| Control | Title | Who carries it | Inspect because | The image's part |
| --- | --- | --- | --- | --- |
| [AC-1](../../docs/assessment/ac-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-17](../../docs/assessment/ac-17.md) | Remote Access | host-inherited | inherited, or nothing to apply it to | statement |
| [AC-17(1)](../../docs/assessment/ac-17.1.md) | Monitoring and Control | host-inherited | inherited, or nothing to apply it to | statement |
| [AC-17(3)](../../docs/assessment/ac-17.3.md) | Managed Access Control Points | host-inherited | inherited, or nothing to apply it to | statement |
| [AC-17(4)](../../docs/assessment/ac-17.4.md) | Privileged Commands and Access | host-inherited | inherited, or nothing to apply it to | statement |
| [AC-2(13)](../../docs/assessment/ac-2.13.md) | Disable Accounts for High-risk Individuals | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-20](../../docs/assessment/ac-20.md) | Use of External Systems | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-20(1)](../../docs/assessment/ac-20.1.md) | Limits on Authorized Use | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-20(2)](../../docs/assessment/ac-20.2.md) | Portable Storage Devices — Restricted Use | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-21](../../docs/assessment/ac-21.md) | Information Sharing | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-22](../../docs/assessment/ac-22.md) | Publicly Accessible Content | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-5](../../docs/assessment/ac-5.md) | Separation of Duties | organization-inherited | inherited, or nothing to apply it to | statement |
| [AC-6(7)](../../docs/assessment/ac-6.7.md) | Review of User Privileges | organization-inherited | inherited, or nothing to apply it to | statement |
| [AT-1](../../docs/assessment/at-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [AT-2](../../docs/assessment/at-2.md) | Literacy Training and Awareness | organization-inherited | inherited, or nothing to apply it to | statement |
| [AT-2(2)](../../docs/assessment/at-2.2.md) | Insider Threat | organization-inherited | inherited, or nothing to apply it to | statement |
| [AT-2(3)](../../docs/assessment/at-2.3.md) | Social Engineering and Mining | organization-inherited | inherited, or nothing to apply it to | statement |
| [AT-3](../../docs/assessment/at-3.md) | Role-based Training | organization-inherited | inherited, or nothing to apply it to | statement |
| [AT-4](../../docs/assessment/at-4.md) | Training Records | organization-inherited | inherited, or nothing to apply it to | statement |
| [AU-1](../../docs/assessment/au-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [AU-11](../../docs/assessment/au-11.md) | Audit Record Retention | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-12(1)](../../docs/assessment/au-12.1.md) | System-wide and Time-correlated Audit Trail | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-12(3)](../../docs/assessment/au-12.3.md) | Changes by Authorized Individuals | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-4](../../docs/assessment/au-4.md) | Audit Log Storage Capacity | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-5](../../docs/assessment/au-5.md) | Response to Audit Logging Process Failures | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-5(1)](../../docs/assessment/au-5.1.md) | Storage Capacity Warning | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-5(2)](../../docs/assessment/au-5.2.md) | Real-time Alerts | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-6](../../docs/assessment/au-6.md) | Audit Record Review, Analysis, and Reporting | organization-inherited | inherited, or nothing to apply it to | statement |
| [AU-6(1)](../../docs/assessment/au-6.1.md) | Automated Process Integration | organization-inherited | inherited, or nothing to apply it to | statement |
| [AU-6(3)](../../docs/assessment/au-6.3.md) | Correlate Audit Record Repositories | organization-inherited | inherited, or nothing to apply it to | statement |
| [AU-6(4)](../../docs/assessment/au-6.4.md) | Central Review and Analysis | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-6(5)](../../docs/assessment/au-6.5.md) | Integrated Analysis of Audit Records | organization-inherited | inherited, or nothing to apply it to | statement |
| [AU-6(6)](../../docs/assessment/au-6.6.md) | Correlation with Physical Monitoring | organization-inherited | inherited, or nothing to apply it to | statement |
| [AU-7](../../docs/assessment/au-7.md) | Audit Record Reduction and Report Generation | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-7(1)](../../docs/assessment/au-7.1.md) | Automatic Processing | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-8](../../docs/assessment/au-8.md) | Time Stamps | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-9](../../docs/assessment/au-9.md) | Protection of Audit Information | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-9(2)](../../docs/assessment/au-9.2.md) | Store on Separate Physical Systems or Components | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-9(3)](../../docs/assessment/au-9.3.md) | Cryptographic Protection | host-inherited | inherited, or nothing to apply it to | statement |
| [AU-9(4)](../../docs/assessment/au-9.4.md) | Access by Subset of Privileged Users | host-inherited | inherited, or nothing to apply it to | statement |
| [CA-1](../../docs/assessment/ca-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-2](../../docs/assessment/ca-2.md) | Control Assessments | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-2(1)](../../docs/assessment/ca-2.1.md) | Independent Assessors | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-2(2)](../../docs/assessment/ca-2.2.md) | Specialized Assessments | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-3](../../docs/assessment/ca-3.md) | Information Exchange | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-3(6)](../../docs/assessment/ca-3.6.md) | Transfer Authorizations | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-5](../../docs/assessment/ca-5.md) | Plan of Action and Milestones | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-6](../../docs/assessment/ca-6.md) | Authorization | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-7](../../docs/assessment/ca-7.md) | Continuous Monitoring | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-7(1)](../../docs/assessment/ca-7.1.md) | Independent Assessment | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-7(4)](../../docs/assessment/ca-7.4.md) | Risk Monitoring | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-8](../../docs/assessment/ca-8.md) | Penetration Testing | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-8(1)](../../docs/assessment/ca-8.1.md) | Independent Penetration Testing Agent or Team | organization-inherited | inherited, or nothing to apply it to | statement |
| [CA-9](../../docs/assessment/ca-9.md) | Internal System Connections | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-1](../../docs/assessment/cm-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-10](../../docs/assessment/cm-10.md) | Software Usage Restrictions | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-12](../../docs/assessment/cm-12.md) | Information Location | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-12(1)](../../docs/assessment/cm-12.1.md) | Automated Tools to Support Information Location | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-2(7)](../../docs/assessment/cm-2.7.md) | Configure Systems and Components for High-risk Areas | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-3](../../docs/assessment/cm-3.md) | Configuration Change Control | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-3(1)](../../docs/assessment/cm-3.1.md) | Automated Documentation, Notification, and Prohibition of Changes | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-3(2)](../../docs/assessment/cm-3.2.md) | Testing, Validation, and Documentation of Changes | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-3(4)](../../docs/assessment/cm-3.4.md) | Security and Privacy Representatives | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-3(6)](../../docs/assessment/cm-3.6.md) | Cryptography Management | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-4](../../docs/assessment/cm-4.md) | Impact Analyses | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-4(1)](../../docs/assessment/cm-4.1.md) | Separate Test Environments | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-4(2)](../../docs/assessment/cm-4.2.md) | Verification of Controls | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-5](../../docs/assessment/cm-5.md) | Access Restrictions for Change | host-inherited | inherited, or nothing to apply it to | statement |
| [CM-6(2)](../../docs/assessment/cm-6.2.md) | Respond to Unauthorized Changes | host-inherited | inherited, or nothing to apply it to | statement |
| [CM-7(1)](../../docs/assessment/cm-7.1.md) | Periodic Review | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-7(2)](../../docs/assessment/cm-7.2.md) | Prevent Program Execution | host-inherited | inherited, or nothing to apply it to | statement |
| [CM-7(5)](../../docs/assessment/cm-7.5.md) | Authorized Software — Allow-by-exception | host-inherited | inherited, or nothing to apply it to | statement |
| [CM-8(3)](../../docs/assessment/cm-8.3.md) | Automated Unauthorized Component Detection | host-inherited | inherited, or nothing to apply it to | statement |
| [CM-8(4)](../../docs/assessment/cm-8.4.md) | Accountability Information | organization-inherited | inherited, or nothing to apply it to | statement |
| [CM-9](../../docs/assessment/cm-9.md) | Configuration Management Plan | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-1](../../docs/assessment/cp-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-10](../../docs/assessment/cp-10.md) | System Recovery and Reconstitution | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-10(2)](../../docs/assessment/cp-10.2.md) | Transaction Recovery | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-10(4)](../../docs/assessment/cp-10.4.md) | Restore Within Time Period | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-2](../../docs/assessment/cp-2.md) | Contingency Plan | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-2(1)](../../docs/assessment/cp-2.1.md) | Coordinate with Related Plans | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-2(2)](../../docs/assessment/cp-2.2.md) | Capacity Planning | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-2(3)](../../docs/assessment/cp-2.3.md) | Resume Mission and Business Functions | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-2(5)](../../docs/assessment/cp-2.5.md) | Continue Mission and Business Functions | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-2(8)](../../docs/assessment/cp-2.8.md) | Identify Critical Assets | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-3](../../docs/assessment/cp-3.md) | Contingency Training | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-3(1)](../../docs/assessment/cp-3.1.md) | Simulated Events | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-4](../../docs/assessment/cp-4.md) | Contingency Plan Testing | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-4(1)](../../docs/assessment/cp-4.1.md) | Coordinate with Related Plans | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-4(2)](../../docs/assessment/cp-4.2.md) | Alternate Processing Site | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-6](../../docs/assessment/cp-6.md) | Alternate Storage Site | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-6(1)](../../docs/assessment/cp-6.1.md) | Separation from Primary Site | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-6(2)](../../docs/assessment/cp-6.2.md) | Recovery Time and Recovery Point Objectives | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-6(3)](../../docs/assessment/cp-6.3.md) | Accessibility | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-7](../../docs/assessment/cp-7.md) | Alternate Processing Site | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-7(1)](../../docs/assessment/cp-7.1.md) | Separation from Primary Site | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-7(2)](../../docs/assessment/cp-7.2.md) | Accessibility | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-7(3)](../../docs/assessment/cp-7.3.md) | Priority of Service | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-7(4)](../../docs/assessment/cp-7.4.md) | Preparation for Use | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-8](../../docs/assessment/cp-8.md) | Telecommunications Services | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-8(1)](../../docs/assessment/cp-8.1.md) | Priority of Service Provisions | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-8(2)](../../docs/assessment/cp-8.2.md) | Single Points of Failure | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-8(3)](../../docs/assessment/cp-8.3.md) | Separation of Primary and Alternate Providers | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-8(4)](../../docs/assessment/cp-8.4.md) | Provider Contingency Plan | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-9](../../docs/assessment/cp-9.md) | System Backup | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-9(1)](../../docs/assessment/cp-9.1.md) | Testing for Reliability and Integrity | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-9(2)](../../docs/assessment/cp-9.2.md) | Test Restoration Using Sampling | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-9(3)](../../docs/assessment/cp-9.3.md) | Separate Storage for Critical Information | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-9(5)](../../docs/assessment/cp-9.5.md) | Transfer to Alternate Storage Site | organization-inherited | inherited, or nothing to apply it to | statement |
| [CP-9(8)](../../docs/assessment/cp-9.8.md) | Cryptographic Protection | organization-inherited | inherited, or nothing to apply it to | statement |
| [IA-1](../../docs/assessment/ia-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [IA-12](../../docs/assessment/ia-12.md) | Identity Proofing | organization-inherited | inherited, or nothing to apply it to | statement |
| [IA-12(2)](../../docs/assessment/ia-12.2.md) | Identity Evidence | organization-inherited | inherited, or nothing to apply it to | statement |
| [IA-12(3)](../../docs/assessment/ia-12.3.md) | Identity Evidence Validation and Verification | organization-inherited | inherited, or nothing to apply it to | statement |
| [IA-12(4)](../../docs/assessment/ia-12.4.md) | In-person Validation and Verification | organization-inherited | inherited, or nothing to apply it to | statement |
| [IA-12(5)](../../docs/assessment/ia-12.5.md) | Address Confirmation | organization-inherited | inherited, or nothing to apply it to | statement |
| [IA-3](../../docs/assessment/ia-3.md) | Device Identification and Authentication | host-inherited | inherited, or nothing to apply it to | statement |
| [IR-1](../../docs/assessment/ir-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-2](../../docs/assessment/ir-2.md) | Incident Response Training | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-2(1)](../../docs/assessment/ir-2.1.md) | Simulated Events | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-2(2)](../../docs/assessment/ir-2.2.md) | Automated Training Environments | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-3](../../docs/assessment/ir-3.md) | Incident Response Testing | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-3(2)](../../docs/assessment/ir-3.2.md) | Coordination with Related Plans | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-4](../../docs/assessment/ir-4.md) | Incident Handling | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-4(1)](../../docs/assessment/ir-4.1.md) | Automated Incident Handling Processes | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-4(11)](../../docs/assessment/ir-4.11.md) | Integrated Incident Response Team | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-4(4)](../../docs/assessment/ir-4.4.md) | Information Correlation | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-5](../../docs/assessment/ir-5.md) | Incident Monitoring | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-5(1)](../../docs/assessment/ir-5.1.md) | Automated Tracking, Data Collection, and Analysis | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-6](../../docs/assessment/ir-6.md) | Incident Reporting | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-6(1)](../../docs/assessment/ir-6.1.md) | Automated Reporting | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-6(3)](../../docs/assessment/ir-6.3.md) | Supply Chain Coordination | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-7](../../docs/assessment/ir-7.md) | Incident Response Assistance | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-7(1)](../../docs/assessment/ir-7.1.md) | Automation Support for Availability of Information and Support | organization-inherited | inherited, or nothing to apply it to | statement |
| [IR-8](../../docs/assessment/ir-8.md) | Incident Response Plan | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-1](../../docs/assessment/ma-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-2](../../docs/assessment/ma-2.md) | Controlled Maintenance | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-2(2)](../../docs/assessment/ma-2.2.md) | Automated Maintenance Activities | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-3](../../docs/assessment/ma-3.md) | Maintenance Tools | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-3(1)](../../docs/assessment/ma-3.1.md) | Inspect Tools | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-3(2)](../../docs/assessment/ma-3.2.md) | Inspect Media | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-3(3)](../../docs/assessment/ma-3.3.md) | Prevent Unauthorized Removal | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-4](../../docs/assessment/ma-4.md) | Nonlocal Maintenance | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-4(3)](../../docs/assessment/ma-4.3.md) | Comparable Security and Sanitization | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-5](../../docs/assessment/ma-5.md) | Maintenance Personnel | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-5(1)](../../docs/assessment/ma-5.1.md) | Individuals Without Appropriate Access | organization-inherited | inherited, or nothing to apply it to | statement |
| [MA-6](../../docs/assessment/ma-6.md) | Timely Maintenance | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-1](../../docs/assessment/mp-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-2](../../docs/assessment/mp-2.md) | Media Access | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-3](../../docs/assessment/mp-3.md) | Media Marking | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-4](../../docs/assessment/mp-4.md) | Media Storage | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-5](../../docs/assessment/mp-5.md) | Media Transport | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-6](../../docs/assessment/mp-6.md) | Media Sanitization | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-6(1)](../../docs/assessment/mp-6.1.md) | Review, Approve, Track, Document, and Verify | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-6(2)](../../docs/assessment/mp-6.2.md) | Equipment Testing | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-6(3)](../../docs/assessment/mp-6.3.md) | Nondestructive Techniques | organization-inherited | inherited, or nothing to apply it to | statement |
| [MP-7](../../docs/assessment/mp-7.md) | Media Use | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-1](../../docs/assessment/pe-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-10](../../docs/assessment/pe-10.md) | Emergency Shutoff | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-11](../../docs/assessment/pe-11.md) | Emergency Power | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-11(1)](../../docs/assessment/pe-11.1.md) | Alternate Power Supply — Minimal Operational Capability | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-12](../../docs/assessment/pe-12.md) | Emergency Lighting | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-13](../../docs/assessment/pe-13.md) | Fire Protection | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-13(1)](../../docs/assessment/pe-13.1.md) | Detection Systems — Automatic Activation and Notification | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-13(2)](../../docs/assessment/pe-13.2.md) | Suppression Systems — Automatic Activation and Notification | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-14](../../docs/assessment/pe-14.md) | Environmental Controls | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-15](../../docs/assessment/pe-15.md) | Water Damage Protection | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-15(1)](../../docs/assessment/pe-15.1.md) | Automation Support | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-16](../../docs/assessment/pe-16.md) | Delivery and Removal | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-17](../../docs/assessment/pe-17.md) | Alternate Work Site | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-18](../../docs/assessment/pe-18.md) | Location of System Components | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-2](../../docs/assessment/pe-2.md) | Physical Access Authorizations | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-3](../../docs/assessment/pe-3.md) | Physical Access Control | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-3(1)](../../docs/assessment/pe-3.1.md) | System Access | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-4](../../docs/assessment/pe-4.md) | Access Control for Transmission | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-5](../../docs/assessment/pe-5.md) | Access Control for Output Devices | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-6](../../docs/assessment/pe-6.md) | Monitoring Physical Access | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-6(1)](../../docs/assessment/pe-6.1.md) | Intrusion Alarms and Surveillance Equipment | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-6(4)](../../docs/assessment/pe-6.4.md) | Monitoring Physical Access to Systems | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-8](../../docs/assessment/pe-8.md) | Visitor Access Records | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-8(1)](../../docs/assessment/pe-8.1.md) | Automated Records Maintenance and Review | organization-inherited | inherited, or nothing to apply it to | statement |
| [PE-9](../../docs/assessment/pe-9.md) | Power Equipment and Cabling | organization-inherited | inherited, or nothing to apply it to | statement |
| [PL-1](../../docs/assessment/pl-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [PL-10](../../docs/assessment/pl-10.md) | Baseline Selection | organization-inherited | inherited, or nothing to apply it to | statement |
| [PL-11](../../docs/assessment/pl-11.md) | Baseline Tailoring | organization-inherited | inherited, or nothing to apply it to | statement |
| [PL-2](../../docs/assessment/pl-2.md) | System Security and Privacy Plans | organization-inherited | inherited, or nothing to apply it to | statement |
| [PL-4](../../docs/assessment/pl-4.md) | Rules of Behavior | organization-inherited | inherited, or nothing to apply it to | statement |
| [PL-4(1)](../../docs/assessment/pl-4.1.md) | Social Media and External Site/Application Usage Restrictions | organization-inherited | inherited, or nothing to apply it to | statement |
| [PL-8](../../docs/assessment/pl-8.md) | Security and Privacy Architectures | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-1](../../docs/assessment/ps-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-2](../../docs/assessment/ps-2.md) | Position Risk Designation | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-3](../../docs/assessment/ps-3.md) | Personnel Screening | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-4](../../docs/assessment/ps-4.md) | Personnel Termination | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-4(2)](../../docs/assessment/ps-4.2.md) | Automated Actions | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-5](../../docs/assessment/ps-5.md) | Personnel Transfer | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-6](../../docs/assessment/ps-6.md) | Access Agreements | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-7](../../docs/assessment/ps-7.md) | External Personnel Security | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-8](../../docs/assessment/ps-8.md) | Personnel Sanctions | organization-inherited | inherited, or nothing to apply it to | statement |
| [PS-9](../../docs/assessment/ps-9.md) | Position Descriptions | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-1](../../docs/assessment/ra-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-2](../../docs/assessment/ra-2.md) | Security Categorization | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-3](../../docs/assessment/ra-3.md) | Risk Assessment | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-3(1)](../../docs/assessment/ra-3.1.md) | Supply Chain Risk Assessment | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-5](../../docs/assessment/ra-5.md) | Vulnerability Monitoring and Scanning | host-inherited | inherited, or nothing to apply it to | statement |
| [RA-5(11)](../../docs/assessment/ra-5.11.md) | Public Disclosure Program | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-5(2)](../../docs/assessment/ra-5.2.md) | Update Vulnerabilities to Be Scanned | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-5(4)](../../docs/assessment/ra-5.4.md) | Discoverable Information | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-5(5)](../../docs/assessment/ra-5.5.md) | Privileged Access | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-7](../../docs/assessment/ra-7.md) | Risk Response | organization-inherited | inherited, or nothing to apply it to | statement |
| [RA-9](../../docs/assessment/ra-9.md) | Criticality Analysis | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-1](../../docs/assessment/sa-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-10](../../docs/assessment/sa-10.md) | Developer Configuration Management | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-11](../../docs/assessment/sa-11.md) | Developer Testing and Evaluation | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-15](../../docs/assessment/sa-15.md) | Development Process, Standards, and Tools | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-15(3)](../../docs/assessment/sa-15.3.md) | Criticality Analysis | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-16](../../docs/assessment/sa-16.md) | Developer-provided Training | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-17](../../docs/assessment/sa-17.md) | Developer Security and Privacy Architecture and Design | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-2](../../docs/assessment/sa-2.md) | Allocation of Resources | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-21](../../docs/assessment/sa-21.md) | Developer Screening | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-3](../../docs/assessment/sa-3.md) | System Development Life Cycle | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-4](../../docs/assessment/sa-4.md) | Acquisition Process | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-4(1)](../../docs/assessment/sa-4.1.md) | Functional Properties of Controls | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-4(10)](../../docs/assessment/sa-4.10.md) | Use of Approved PIV Products | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-4(2)](../../docs/assessment/sa-4.2.md) | Design and Implementation Information for Controls | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-4(5)](../../docs/assessment/sa-4.5.md) | System, Component, and Service Configurations | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-4(9)](../../docs/assessment/sa-4.9.md) | Functions, Ports, Protocols, and Services in Use | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-5](../../docs/assessment/sa-5.md) | System Documentation | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-8](../../docs/assessment/sa-8.md) | Security and Privacy Engineering Principles | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-9](../../docs/assessment/sa-9.md) | External System Services | organization-inherited | inherited, or nothing to apply it to | statement |
| [SA-9(2)](../../docs/assessment/sa-9.2.md) | Identification of Functions, Ports, Protocols, and Services | organization-inherited | inherited, or nothing to apply it to | statement |
| [SC-1](../../docs/assessment/sc-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [SC-20](../../docs/assessment/sc-20.md) | Secure Name/Address Resolution Service (Authoritative Source) | organization-inherited | inherited, or nothing to apply it to | statement |
| [SC-21](../../docs/assessment/sc-21.md) | Secure Name/Address Resolution Service (Recursive or Caching Resolver) | organization-inherited | inherited, or nothing to apply it to | statement |
| [SC-22](../../docs/assessment/sc-22.md) | Architecture and Provisioning for Name/Address Resolution Service | organization-inherited | inherited, or nothing to apply it to | statement |
| [SC-28](../../docs/assessment/sc-28.md) | Protection of Information at Rest | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-3](../../docs/assessment/sc-3.md) | Security Function Isolation | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-39](../../docs/assessment/sc-39.md) | Process Isolation | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-4](../../docs/assessment/sc-4.md) | Information in Shared System Resources | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-45](../../docs/assessment/sc-45.md) | System Time Synchronization | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-7(18)](../../docs/assessment/sc-7.18.md) | Fail Secure | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-7(21)](../../docs/assessment/sc-7.21.md) | Isolation of System Components | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-7(3)](../../docs/assessment/sc-7.3.md) | Access Points | host-inherited | inherited, or nothing to apply it to | statement |
| [SC-7(4)](../../docs/assessment/sc-7.4.md) | External Telecommunications Services | organization-inherited | inherited, or nothing to apply it to | statement |
| [SI-1](../../docs/assessment/si-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [SI-12](../../docs/assessment/si-12.md) | Information Management and Retention | organization-inherited | inherited, or nothing to apply it to | statement |
| [SI-16](../../docs/assessment/si-16.md) | Memory Protection | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-2(2)](../../docs/assessment/si-2.2.md) | Automated Flaw Remediation Status | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-3](../../docs/assessment/si-3.md) | Malicious Code Protection | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-4](../../docs/assessment/si-4.md) | System Monitoring | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-4(12)](../../docs/assessment/si-4.12.md) | Automated Organization-generated Alerts | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-4(14)](../../docs/assessment/si-4.14.md) | Wireless Intrusion Detection | organization-inherited | inherited, or nothing to apply it to | statement |
| [SI-4(2)](../../docs/assessment/si-4.2.md) | Automated Tools and Mechanisms for Real-time Analysis | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-4(20)](../../docs/assessment/si-4.20.md) | Privileged Users | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-4(22)](../../docs/assessment/si-4.22.md) | Unauthorized Network Services | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-4(4)](../../docs/assessment/si-4.4.md) | Inbound and Outbound Communications Traffic | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-4(5)](../../docs/assessment/si-4.5.md) | System-generated Alerts | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-5](../../docs/assessment/si-5.md) | Security Alerts, Advisories, and Directives | organization-inherited | inherited, or nothing to apply it to | statement |
| [SI-5(1)](../../docs/assessment/si-5.1.md) | Automated Alerts and Advisories | organization-inherited | inherited, or nothing to apply it to | statement |
| [SI-6](../../docs/assessment/si-6.md) | Security and Privacy Function Verification | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-7](../../docs/assessment/si-7.md) | Software, Firmware, and Information Integrity | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-7(1)](../../docs/assessment/si-7.1.md) | Integrity Checks | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-7(2)](../../docs/assessment/si-7.2.md) | Automated Notifications of Integrity Violations | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-7(5)](../../docs/assessment/si-7.5.md) | Automated Response to Integrity Violations | host-inherited | inherited, or nothing to apply it to | statement |
| [SI-7(7)](../../docs/assessment/si-7.7.md) | Integration of Detection and Response | host-inherited | inherited, or nothing to apply it to | statement |
| [SR-1](../../docs/assessment/sr-1.md) | Policy and Procedures | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-10](../../docs/assessment/sr-10.md) | Inspection of Systems or Components | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-11](../../docs/assessment/sr-11.md) | Component Authenticity | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-11(1)](../../docs/assessment/sr-11.1.md) | Anti-counterfeit Training | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-11(2)](../../docs/assessment/sr-11.2.md) | Configuration Control for Component Service and Repair | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-12](../../docs/assessment/sr-12.md) | Component Disposal | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-2](../../docs/assessment/sr-2.md) | Supply Chain Risk Management Plan | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-2(1)](../../docs/assessment/sr-2.1.md) | Establish SCRM Team | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-3](../../docs/assessment/sr-3.md) | Supply Chain Controls and Processes | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-5](../../docs/assessment/sr-5.md) | Acquisition Strategies, Tools, and Methods | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-6](../../docs/assessment/sr-6.md) | Supplier Assessments and Reviews | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-8](../../docs/assessment/sr-8.md) | Notification Agreements | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-9](../../docs/assessment/sr-9.md) | Tamper Resistance and Detection | organization-inherited | inherited, or nothing to apply it to | statement |
| [SR-9(1)](../../docs/assessment/sr-9.1.md) | Multiple Stages of System Development Life Cycle | organization-inherited | inherited, or nothing to apply it to | statement |

## Nothing to apply it to

Answered not-applicable: the thing the control governs is absent from this image.
This is the group to read most carefully, because it is the one that shrinks as
soon as an image does more. A reviewer confirms each absence.

| Control | Title | Who carries it | Inspect because | The image's part |
| --- | --- | --- | --- | --- |
| [AC-10](../../docs/assessment/ac-10.md) | Concurrent Session Control | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-11](../../docs/assessment/ac-11.md) | Device Lock | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-11(1)](../../docs/assessment/ac-11.1.md) | Pattern-hiding Displays | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-12](../../docs/assessment/ac-12.md) | Session Termination | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-18](../../docs/assessment/ac-18.md) | Wireless Access | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-18(1)](../../docs/assessment/ac-18.1.md) | Authentication and Encryption | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-18(3)](../../docs/assessment/ac-18.3.md) | Disable Wireless Networking | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-18(4)](../../docs/assessment/ac-18.4.md) | Restrict Configurations by Users | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-18(5)](../../docs/assessment/ac-18.5.md) | Antennas and Transmission Power Levels | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-19](../../docs/assessment/ac-19.md) | Access Control for Mobile Devices | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-19(5)](../../docs/assessment/ac-19.5.md) | Full Device or Container-based Encryption | not-applicable | inherited, or nothing to apply it to | statement |
| [AC-2](../../docs/assessment/ac-2.md) | Account Management | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-2(1)](../../docs/assessment/ac-2.1.md) | Automated System Account Management | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-2(11)](../../docs/assessment/ac-2.11.md) | Usage Conditions | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-2(12)](../../docs/assessment/ac-2.12.md) | Account Monitoring for Atypical Usage | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-2(2)](../../docs/assessment/ac-2.2.md) | Automated Temporary and Emergency Account Management | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-2(3)](../../docs/assessment/ac-2.3.md) | Disable Accounts | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-2(4)](../../docs/assessment/ac-2.4.md) | Automated Audit Actions | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-2(5)](../../docs/assessment/ac-2.5.md) | Inactivity Logout | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-6(1)](../../docs/assessment/ac-6.1.md) | Authorize Access to Security Functions | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-6(2)](../../docs/assessment/ac-6.2.md) | Non-privileged Access for Nonsecurity Functions | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-6(3)](../../docs/assessment/ac-6.3.md) | Network Access to Privileged Commands | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-6(5)](../../docs/assessment/ac-6.5.md) | Privileged Accounts | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-6(9)](../../docs/assessment/ac-6.9.md) | Log Use of Privileged Functions | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-7](../../docs/assessment/ac-7.md) | Unsuccessful Logon Attempts | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AC-8](../../docs/assessment/ac-8.md) | System Use Notification | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [AU-10](../../docs/assessment/au-10.md) | Non-repudiation | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-11](../../docs/assessment/ia-11.md) | Re-authentication | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-2](../../docs/assessment/ia-2.md) | Identification and Authentication (Organizational Users) | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-2(1)](../../docs/assessment/ia-2.1.md) | Multi-factor Authentication to Privileged Accounts | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-2(12)](../../docs/assessment/ia-2.12.md) | Acceptance of PIV Credentials | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-2(2)](../../docs/assessment/ia-2.2.md) | Multi-factor Authentication to Non-privileged Accounts | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-2(5)](../../docs/assessment/ia-2.5.md) | Individual Authentication with Group Authentication | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-2(8)](../../docs/assessment/ia-2.8.md) | Access to Accounts — Replay Resistant | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-4](../../docs/assessment/ia-4.md) | Identifier Management | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-4(4)](../../docs/assessment/ia-4.4.md) | Identify User Status | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-5(1)](../../docs/assessment/ia-5.1.md) | Password-based Authentication | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-5(2)](../../docs/assessment/ia-5.2.md) | Public Key-based Authentication | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-6](../../docs/assessment/ia-6.md) | Authentication Feedback | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-7](../../docs/assessment/ia-7.md) | Cryptographic Module Authentication | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-8](../../docs/assessment/ia-8.md) | Identification and Authentication (Non-organizational Users) | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-8(1)](../../docs/assessment/ia-8.1.md) | Acceptance of PIV Credentials from Other Agencies | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-8(2)](../../docs/assessment/ia-8.2.md) | Acceptance of External Authenticators | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [IA-8(4)](../../docs/assessment/ia-8.4.md) | Use of Defined Profiles | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [SC-15](../../docs/assessment/sc-15.md) | Collaborative Computing Devices and Applications | not-applicable | inherited, or nothing to apply it to | statement |
| [SC-7(7)](../../docs/assessment/sc-7.7.md) | Split Tunneling for Remote Devices | not-applicable | inherited, or nothing to apply it to | statement |
| [SI-4(10)](../../docs/assessment/si-4.10.md) | Visibility of Encrypted Communications | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [SI-8](../../docs/assessment/si-8.md) | Spam Protection | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
| [SI-8(2)](../../docs/assessment/si-8.2.md) | Automatic Updates | research-required | inherited, or nothing to apply it to | decided, **not yet reviewed** |
