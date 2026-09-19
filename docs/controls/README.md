# Control baseline

The origination every Datopsis image component starts from, for each control in the NIST SP 800-53 Rev 5 High baseline and each further control the [standard](../standard/README.md) reaches. What the values mean, and how an image repository uses this, is in [the control model](../CONTROL-MODEL.md).

Most of it is derived. A control an image criterion reaches through its anchors is `image-owned`; one only platform or host expectations reach takes their origination; some families have a default; the rest are `research-required`. Where derivation would be wrong, a [determination](#determinations) overrides it, with its reason.

| Origination | Controls | Responsible role |
| --- | ---: | --- |
| `image-owned` | 20 | `image-project` |
| `deployment-configured` | 13 | `deployment-profile` |
| `host-inherited` | 50 | `host-orchestrator` |
| `organization-inherited` | 228 | `organization` |
| `not-applicable` | 11 | none |
| `research-required` | 57 | `image-project` |
| **Total** | **379** | 370 in the High baseline |

`research-required` is not a gap in the standard. It marks controls whose answer depends on what the image does: a database authenticates users and a static file server does not. Each image determines them in its own component definition.

## By family

| Family | `image-owned` | `deployment-configured` | `host-inherited` | `organization-inherited` | `not-applicable` | `research-required` |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [AC](#ac) | 3 | 2 | 4 | 9 | 9 | 20 |
| [AT](#at) |  |  |  | 6 |  |  |
| [AU](#au) |  |  | 15 | 6 |  | 5 |
| [CA](#ca) |  |  |  | 14 |  |  |
| [CM](#cm) | 11 | 1 | 5 | 16 |  | 2 |
| [CP](#cp) |  |  |  | 35 |  |  |
| [IA](#ia) |  |  | 1 | 6 |  | 19 |
| [IR](#ir) |  |  |  | 18 |  |  |
| [MA](#ma) |  |  |  | 12 |  |  |
| [MP](#mp) |  |  |  | 10 |  |  |
| [PE](#pe) |  |  |  | 25 |  |  |
| [PL](#pl) |  |  |  | 7 |  |  |
| [PS](#ps) |  |  |  | 10 |  |  |
| [RA](#ra) |  |  | 1 | 10 |  |  |
| [SA](#sa) | 1 |  |  | 20 |  |  |
| [SC](#sc) | 2 | 10 | 8 | 5 | 2 | 6 |
| [SI](#si) | 3 |  | 16 | 5 |  | 5 |
| [SR](#sr) |  |  |  | 14 |  |  |

## Controls

**High** marks the control as selected by the High baseline. **Criteria** are the image criteria behind an `image-owned` control, or the image's contribution to someone else's. **Handoff** names what the platform or host must do.

<a id="ac"></a>

### AC

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| AC-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| AC-2 | Account Management | Yes | `research-required` |  |  | undetermined |
| AC-2(1) | Automated System Account Management | Yes | `research-required` |  |  | undetermined |
| AC-2(2) | Automated Temporary and Emergency Account Management | Yes | `research-required` |  |  | undetermined |
| AC-2(3) | Disable Accounts | Yes | `research-required` |  |  | undetermined |
| AC-2(4) | Automated Audit Actions | Yes | `research-required` |  |  | undetermined |
| AC-2(5) | Inactivity Logout | Yes | `research-required` |  |  | undetermined |
| AC-2(11) | Usage Conditions | Yes | `research-required` |  |  | undetermined |
| AC-2(12) | Account Monitoring for Atypical Usage | Yes | `research-required` |  |  | undetermined |
| AC-2(13) | Disable Accounts for High-risk Individuals | Yes | `organization-inherited` |  |  | determination |
| AC-3 | Access Enforcement | Yes | `research-required` |  | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| AC-4 | Information Flow Enforcement | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | expectation |
| AC-4(4) | Flow Control of Encrypted Information | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| AC-5 | Separation of Duties | Yes | `organization-inherited` |  |  | determination |
| AC-6 | Least Privilege | Yes | `image-owned` | [IMG-11](../standard/criteria.md#img-11-non-root-with-no-privilege-transition), [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed) | determination |
| AC-6(1) | Authorize Access to Security Functions | Yes | `research-required` |  |  | undetermined |
| AC-6(2) | Non-privileged Access for Nonsecurity Functions | Yes | `research-required` |  |  | undetermined |
| AC-6(3) | Network Access to Privileged Commands | Yes | `research-required` |  |  | undetermined |
| AC-6(5) | Privileged Accounts | Yes | `research-required` |  |  | undetermined |
| AC-6(7) | Review of User Privileges | Yes | `organization-inherited` |  |  | determination |
| AC-6(8) | Privilege Levels for Code Execution |  | `image-owned` | [IMG-09](../standard/criteria.md#img-09-no-privilege-raising-files), [IMG-11](../standard/criteria.md#img-11-non-root-with-no-privilege-transition), [IMG-12](../standard/criteria.md#img-12-runs-under-an-arbitrary-uid), [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed) | criterion |
| AC-6(9) | Log Use of Privileged Functions | Yes | `research-required` |  |  | undetermined |
| AC-6(10) | Prohibit Non-privileged Users from Executing Privileged Functions | Yes | `image-owned` | [IMG-11](../standard/criteria.md#img-11-non-root-with-no-privilege-transition) | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed) | criterion |
| AC-7 | Unsuccessful Logon Attempts | Yes | `research-required` |  |  | undetermined |
| AC-8 | System Use Notification | Yes | `research-required` |  |  | undetermined |
| AC-10 | Concurrent Session Control | Yes | `research-required` |  |  | undetermined |
| AC-11 | Device Lock | Yes | `not-applicable` |  |  | determination |
| AC-11(1) | Pattern-hiding Displays | Yes | `not-applicable` |  |  | determination |
| AC-12 | Session Termination | Yes | `research-required` |  |  | undetermined |
| AC-14 | Permitted Actions Without Identification or Authentication | Yes | `research-required` |  |  | undetermined |
| AC-17 | Remote Access | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| AC-17(1) | Monitoring and Control | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| AC-17(2) | Protection of Confidentiality and Integrity Using Encryption | Yes | `research-required` |  | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| AC-17(3) | Managed Access Control Points | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| AC-17(4) | Privileged Commands and Access | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| AC-18 | Wireless Access | Yes | `not-applicable` |  |  | determination |
| AC-18(1) | Authentication and Encryption | Yes | `not-applicable` |  |  | determination |
| AC-18(3) | Disable Wireless Networking | Yes | `not-applicable` |  |  | determination |
| AC-18(4) | Restrict Configurations by Users | Yes | `not-applicable` |  |  | determination |
| AC-18(5) | Antennas and Transmission Power Levels | Yes | `not-applicable` |  |  | determination |
| AC-19 | Access Control for Mobile Devices | Yes | `not-applicable` |  |  | determination |
| AC-19(5) | Full Device or Container-based Encryption | Yes | `not-applicable` |  |  | determination |
| AC-20 | Use of External Systems | Yes | `organization-inherited` |  |  | determination |
| AC-20(1) | Limits on Authorized Use | Yes | `organization-inherited` |  |  | determination |
| AC-20(2) | Portable Storage Devices — Restricted Use | Yes | `organization-inherited` |  |  | determination |
| AC-21 | Information Sharing | Yes | `organization-inherited` |  |  | determination |
| AC-22 | Publicly Accessible Content | Yes | `organization-inherited` |  |  | determination |

<a id="at"></a>

### AT

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| AT-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| AT-2 | Literacy Training and Awareness | Yes | `organization-inherited` |  |  | family |
| AT-2(2) | Insider Threat | Yes | `organization-inherited` |  |  | family |
| AT-2(3) | Social Engineering and Mining | Yes | `organization-inherited` |  |  | family |
| AT-3 | Role-based Training | Yes | `organization-inherited` |  |  | family |
| AT-4 | Training Records | Yes | `organization-inherited` |  |  | family |

<a id="au"></a>

### AU

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| AU-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| AU-2 | Event Logging | Yes | `research-required` |  |  | undetermined |
| AU-3 | Content of Audit Records | Yes | `research-required` |  |  | undetermined |
| AU-3(1) | Additional Audit Information | Yes | `research-required` |  |  | undetermined |
| AU-4 | Audit Log Storage Capacity | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-5 | Response to Audit Logging Process Failures | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-5(1) | Storage Capacity Warning | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-5(2) | Real-time Alerts | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-6 | Audit Record Review, Analysis, and Reporting | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| AU-6(1) | Automated Process Integration | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| AU-6(3) | Correlate Audit Record Repositories | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| AU-6(4) | Central Review and Analysis |  | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-6(5) | Integrated Analysis of Audit Records | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| AU-6(6) | Correlation with Physical Monitoring | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| AU-7 | Audit Record Reduction and Report Generation | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-7(1) | Automatic Processing | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-8 | Time Stamps | Yes | `host-inherited` |  | [HST-05](../standard/platform.md#hst-05-clocks-are-synchronized) | expectation |
| AU-9 | Protection of Audit Information | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | expectation |
| AU-9(2) | Store on Separate Physical Systems or Components | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-9(3) | Cryptographic Protection | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-9(4) | Access by Subset of Privileged Users | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-10 | Non-repudiation | Yes | `research-required` |  |  | undetermined |
| AU-11 | Audit Record Retention | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-12 | Audit Record Generation | Yes | `research-required` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| AU-12(1) | System-wide and Time-correlated Audit Trail | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| AU-12(3) | Changes by Authorized Individuals | Yes | `host-inherited` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |

<a id="ca"></a>

### CA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| CA-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| CA-2 | Control Assessments | Yes | `organization-inherited` |  |  | family |
| CA-2(1) | Independent Assessors | Yes | `organization-inherited` |  |  | family |
| CA-2(2) | Specialized Assessments | Yes | `organization-inherited` |  |  | family |
| CA-3 | Information Exchange | Yes | `organization-inherited` |  |  | family |
| CA-3(6) | Transfer Authorizations | Yes | `organization-inherited` |  |  | family |
| CA-5 | Plan of Action and Milestones | Yes | `organization-inherited` |  |  | family |
| CA-6 | Authorization | Yes | `organization-inherited` |  |  | family |
| CA-7 | Continuous Monitoring | Yes | `organization-inherited` |  |  | family |
| CA-7(1) | Independent Assessment | Yes | `organization-inherited` |  |  | family |
| CA-7(4) | Risk Monitoring | Yes | `organization-inherited` |  |  | family |
| CA-8 | Penetration Testing | Yes | `organization-inherited` |  |  | family |
| CA-8(1) | Independent Penetration Testing Agent or Team | Yes | `organization-inherited` |  |  | family |
| CA-9 | Internal System Connections | Yes | `organization-inherited` |  |  | family |

<a id="cm"></a>

### CM

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| CM-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| CM-2 | Baseline Configuration | Yes | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified), [IMG-23](../standard/criteria.md#img-23-identifying-labels) |  | determination |
| CM-2(2) | Automation Support for Accuracy and Currency | Yes | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified), [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change), [IMG-23](../standard/criteria.md#img-23-identifying-labels) |  | determination |
| CM-2(3) | Retention of Previous Configurations | Yes | `image-owned` | [IMG-23](../standard/criteria.md#img-23-identifying-labels), [IMG-24](../standard/criteria.md#img-24-immutable-tags) |  | determination |
| CM-2(7) | Configure Systems and Components for High-risk Areas | Yes | `organization-inherited` |  |  | determination |
| CM-3 | Configuration Change Control | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-3(1) | Automated Documentation, Notification, and Prohibition of Changes | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-3(2) | Testing, Validation, and Documentation of Changes | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-3(4) | Security and Privacy Representatives | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-3(6) | Cryptography Management | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-4 | Impact Analyses | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-4(1) | Separate Test Environments | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-4(2) | Verification of Controls | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-5 | Access Restrictions for Change | Yes | `host-inherited` | [IMG-06](../standard/criteria.md#img-06-no-package-manager), [IMG-10](../standard/criteria.md#img-10-software-and-configuration-not-writable-by-the-service) | [PLT-12](../standard/platform.md#plt-12-registry-access-is-controlled-and-audited), [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| CM-5(1) | Automated Access Enforcement and Audit Records | Yes | `deployment-configured` | [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-03](../standard/platform.md#plt-03-the-root-filesystem-is-read-only) | expectation |
| CM-5(6) | Limit Library Privileges |  | `image-owned` | [IMG-10](../standard/criteria.md#img-10-software-and-configuration-not-writable-by-the-service), [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-03](../standard/platform.md#plt-03-the-root-filesystem-is-read-only), [PLT-12](../standard/platform.md#plt-12-registry-access-is-controlled-and-audited) | criterion |
| CM-6 | Configuration Settings | Yes | `research-required` |  |  | determination |
| CM-6(1) | Automated Management, Application, and Verification | Yes | `research-required` |  |  | undetermined |
| CM-6(2) | Respond to Unauthorized Changes | Yes | `host-inherited` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| CM-7 | Least Functionality | Yes | `image-owned` | [IMG-06](../standard/criteria.md#img-06-no-package-manager), [IMG-07](../standard/criteria.md#img-07-only-what-the-function-needs), [IMG-14](../standard/criteria.md#img-14-unprivileged-ports), [IMG-27](../standard/criteria.md#img-27-no-remote-administration), [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-04](../standard/platform.md#plt-04-ports-are-non-privileged-and-declared), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | criterion |
| CM-7(1) | Periodic Review | Yes | `organization-inherited` |  |  | determination |
| CM-7(2) | Prevent Program Execution | Yes | `host-inherited` | [IMG-07](../standard/criteria.md#img-07-only-what-the-function-needs), [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| CM-7(5) | Authorized Software — Allow-by-exception | Yes | `host-inherited` | [IMG-07](../standard/criteria.md#img-07-only-what-the-function-needs) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | determination |
| CM-8 | System Component Inventory | Yes | `image-owned` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-21](../standard/criteria.md#img-21-bill-of-materials), [IMG-23](../standard/criteria.md#img-23-identifying-labels) |  | determination |
| CM-8(1) | Updates During Installation and Removal | Yes | `image-owned` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-21](../standard/criteria.md#img-21-bill-of-materials) |  | determination |
| CM-8(2) | Automated Maintenance | Yes | `image-owned` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-21](../standard/criteria.md#img-21-bill-of-materials) |  | determination |
| CM-8(3) | Automated Unauthorized Component Detection | Yes | `host-inherited` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| CM-8(4) | Accountability Information | Yes | `organization-inherited` |  |  | determination |
| CM-9 | Configuration Management Plan | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| CM-10 | Software Usage Restrictions | Yes | `organization-inherited` |  |  | determination |
| CM-11 | User-installed Software | Yes | `image-owned` | [IMG-06](../standard/criteria.md#img-06-no-package-manager), [IMG-10](../standard/criteria.md#img-10-software-and-configuration-not-writable-by-the-service) |  | determination |
| CM-11(2) | Software Installation with Privileged Status |  | `image-owned` | [IMG-06](../standard/criteria.md#img-06-no-package-manager) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-12](../standard/platform.md#plt-12-registry-access-is-controlled-and-audited) | criterion |
| CM-12 | Information Location | Yes | `organization-inherited` |  |  | determination |
| CM-12(1) | Automated Tools to Support Information Location | Yes | `organization-inherited` |  |  | determination |
| CM-14 | Signed Components |  | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified), [IMG-03](../standard/criteria.md#img-03-hermetic-assembly), [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change), [IMG-22](../standard/criteria.md#img-22-signed-with-provenance) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | criterion |

<a id="cp"></a>

### CP

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| CP-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| CP-2 | Contingency Plan | Yes | `organization-inherited` |  |  | family |
| CP-2(1) | Coordinate with Related Plans | Yes | `organization-inherited` |  |  | family |
| CP-2(2) | Capacity Planning | Yes | `organization-inherited` |  |  | family |
| CP-2(3) | Resume Mission and Business Functions | Yes | `organization-inherited` |  |  | family |
| CP-2(5) | Continue Mission and Business Functions | Yes | `organization-inherited` |  |  | family |
| CP-2(8) | Identify Critical Assets | Yes | `organization-inherited` |  |  | family |
| CP-3 | Contingency Training | Yes | `organization-inherited` |  |  | family |
| CP-3(1) | Simulated Events | Yes | `organization-inherited` |  |  | family |
| CP-4 | Contingency Plan Testing | Yes | `organization-inherited` |  |  | family |
| CP-4(1) | Coordinate with Related Plans | Yes | `organization-inherited` |  |  | family |
| CP-4(2) | Alternate Processing Site | Yes | `organization-inherited` |  |  | family |
| CP-6 | Alternate Storage Site | Yes | `organization-inherited` |  |  | family |
| CP-6(1) | Separation from Primary Site | Yes | `organization-inherited` |  |  | family |
| CP-6(2) | Recovery Time and Recovery Point Objectives | Yes | `organization-inherited` |  |  | family |
| CP-6(3) | Accessibility | Yes | `organization-inherited` |  |  | family |
| CP-7 | Alternate Processing Site | Yes | `organization-inherited` |  |  | family |
| CP-7(1) | Separation from Primary Site | Yes | `organization-inherited` |  |  | family |
| CP-7(2) | Accessibility | Yes | `organization-inherited` |  |  | family |
| CP-7(3) | Priority of Service | Yes | `organization-inherited` |  |  | family |
| CP-7(4) | Preparation for Use | Yes | `organization-inherited` |  |  | family |
| CP-8 | Telecommunications Services | Yes | `organization-inherited` |  |  | family |
| CP-8(1) | Priority of Service Provisions | Yes | `organization-inherited` |  |  | family |
| CP-8(2) | Single Points of Failure | Yes | `organization-inherited` |  |  | family |
| CP-8(3) | Separation of Primary and Alternate Providers | Yes | `organization-inherited` |  |  | family |
| CP-8(4) | Provider Contingency Plan | Yes | `organization-inherited` |  |  | family |
| CP-9 | System Backup | Yes | `organization-inherited` |  |  | family |
| CP-9(1) | Testing for Reliability and Integrity | Yes | `organization-inherited` |  |  | family |
| CP-9(2) | Test Restoration Using Sampling | Yes | `organization-inherited` |  |  | family |
| CP-9(3) | Separate Storage for Critical Information | Yes | `organization-inherited` |  |  | family |
| CP-9(5) | Transfer to Alternate Storage Site | Yes | `organization-inherited` |  |  | family |
| CP-9(8) | Cryptographic Protection | Yes | `organization-inherited` |  |  | family |
| CP-10 | System Recovery and Reconstitution | Yes | `organization-inherited` |  |  | family |
| CP-10(2) | Transaction Recovery | Yes | `organization-inherited` |  |  | family |
| CP-10(4) | Restore Within Time Period | Yes | `organization-inherited` |  |  | family |

<a id="ia"></a>

### IA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| IA-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| IA-2 | Identification and Authentication (Organizational Users) | Yes | `research-required` |  |  | undetermined |
| IA-2(1) | Multi-factor Authentication to Privileged Accounts | Yes | `research-required` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| IA-2(2) | Multi-factor Authentication to Non-privileged Accounts | Yes | `research-required` |  |  | undetermined |
| IA-2(5) | Individual Authentication with Group Authentication | Yes | `research-required` |  |  | undetermined |
| IA-2(8) | Access to Accounts — Replay Resistant | Yes | `research-required` |  |  | undetermined |
| IA-2(12) | Acceptance of PIV Credentials | Yes | `research-required` |  |  | undetermined |
| IA-3 | Device Identification and Authentication | Yes | `host-inherited` |  | [PLT-15](../standard/platform.md#plt-15-nodes-are-trusted-before-they-run-workloads) | expectation |
| IA-4 | Identifier Management | Yes | `research-required` |  |  | undetermined |
| IA-4(4) | Identify User Status | Yes | `research-required` |  |  | undetermined |
| IA-5 | Authenticator Management | Yes | `research-required` |  |  | undetermined |
| IA-5(1) | Password-based Authentication | Yes | `research-required` |  |  | undetermined |
| IA-5(2) | Public Key-based Authentication | Yes | `research-required` |  |  | undetermined |
| IA-5(6) | Protection of Authenticators | Yes | `research-required` |  |  | undetermined |
| IA-6 | Authentication Feedback | Yes | `research-required` |  |  | undetermined |
| IA-7 | Cryptographic Module Authentication | Yes | `research-required` |  |  | undetermined |
| IA-8 | Identification and Authentication (Non-organizational Users) | Yes | `research-required` |  |  | undetermined |
| IA-8(1) | Acceptance of PIV Credentials from Other Agencies | Yes | `research-required` |  |  | undetermined |
| IA-8(2) | Acceptance of External Authenticators | Yes | `research-required` |  |  | undetermined |
| IA-8(4) | Use of Defined Profiles | Yes | `research-required` |  |  | undetermined |
| IA-11 | Re-authentication | Yes | `research-required` |  |  | undetermined |
| IA-12 | Identity Proofing | Yes | `organization-inherited` |  |  | determination |
| IA-12(2) | Identity Evidence | Yes | `organization-inherited` |  |  | determination |
| IA-12(3) | Identity Evidence Validation and Verification | Yes | `organization-inherited` |  |  | determination |
| IA-12(4) | In-person Validation and Verification | Yes | `organization-inherited` |  |  | determination |
| IA-12(5) | Address Confirmation | Yes | `organization-inherited` |  |  | determination |

<a id="ir"></a>

### IR

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| IR-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| IR-2 | Incident Response Training | Yes | `organization-inherited` |  |  | family |
| IR-2(1) | Simulated Events | Yes | `organization-inherited` |  |  | family |
| IR-2(2) | Automated Training Environments | Yes | `organization-inherited` |  |  | family |
| IR-3 | Incident Response Testing | Yes | `organization-inherited` |  |  | family |
| IR-3(2) | Coordination with Related Plans | Yes | `organization-inherited` |  |  | family |
| IR-4 | Incident Handling | Yes | `organization-inherited` |  |  | family |
| IR-4(1) | Automated Incident Handling Processes | Yes | `organization-inherited` |  |  | family |
| IR-4(4) | Information Correlation | Yes | `organization-inherited` |  |  | family |
| IR-4(11) | Integrated Incident Response Team | Yes | `organization-inherited` |  |  | family |
| IR-5 | Incident Monitoring | Yes | `organization-inherited` |  |  | family |
| IR-5(1) | Automated Tracking, Data Collection, and Analysis | Yes | `organization-inherited` |  |  | family |
| IR-6 | Incident Reporting | Yes | `organization-inherited` |  |  | family |
| IR-6(1) | Automated Reporting | Yes | `organization-inherited` |  |  | family |
| IR-6(3) | Supply Chain Coordination | Yes | `organization-inherited` |  |  | family |
| IR-7 | Incident Response Assistance | Yes | `organization-inherited` |  |  | family |
| IR-7(1) | Automation Support for Availability of Information and Support | Yes | `organization-inherited` |  |  | family |
| IR-8 | Incident Response Plan | Yes | `organization-inherited` |  |  | family |

<a id="ma"></a>

### MA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| MA-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| MA-2 | Controlled Maintenance | Yes | `organization-inherited` |  |  | family |
| MA-2(2) | Automated Maintenance Activities | Yes | `organization-inherited` |  |  | family |
| MA-3 | Maintenance Tools | Yes | `organization-inherited` |  |  | family |
| MA-3(1) | Inspect Tools | Yes | `organization-inherited` |  |  | family |
| MA-3(2) | Inspect Media | Yes | `organization-inherited` |  |  | family |
| MA-3(3) | Prevent Unauthorized Removal | Yes | `organization-inherited` |  |  | family |
| MA-4 | Nonlocal Maintenance | Yes | `organization-inherited` |  |  | family |
| MA-4(3) | Comparable Security and Sanitization | Yes | `organization-inherited` |  |  | family |
| MA-5 | Maintenance Personnel | Yes | `organization-inherited` |  |  | family |
| MA-5(1) | Individuals Without Appropriate Access | Yes | `organization-inherited` |  |  | family |
| MA-6 | Timely Maintenance | Yes | `organization-inherited` |  |  | family |

<a id="mp"></a>

### MP

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| MP-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| MP-2 | Media Access | Yes | `organization-inherited` |  |  | family |
| MP-3 | Media Marking | Yes | `organization-inherited` |  |  | family |
| MP-4 | Media Storage | Yes | `organization-inherited` |  |  | family |
| MP-5 | Media Transport | Yes | `organization-inherited` |  |  | family |
| MP-6 | Media Sanitization | Yes | `organization-inherited` |  |  | family |
| MP-6(1) | Review, Approve, Track, Document, and Verify | Yes | `organization-inherited` |  |  | family |
| MP-6(2) | Equipment Testing | Yes | `organization-inherited` |  |  | family |
| MP-6(3) | Nondestructive Techniques | Yes | `organization-inherited` |  |  | family |
| MP-7 | Media Use | Yes | `organization-inherited` |  |  | family |

<a id="pe"></a>

### PE

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| PE-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| PE-2 | Physical Access Authorizations | Yes | `organization-inherited` |  |  | family |
| PE-3 | Physical Access Control | Yes | `organization-inherited` |  |  | family |
| PE-3(1) | System Access | Yes | `organization-inherited` |  |  | family |
| PE-4 | Access Control for Transmission | Yes | `organization-inherited` |  |  | family |
| PE-5 | Access Control for Output Devices | Yes | `organization-inherited` |  |  | family |
| PE-6 | Monitoring Physical Access | Yes | `organization-inherited` |  |  | family |
| PE-6(1) | Intrusion Alarms and Surveillance Equipment | Yes | `organization-inherited` |  |  | family |
| PE-6(4) | Monitoring Physical Access to Systems | Yes | `organization-inherited` |  |  | family |
| PE-8 | Visitor Access Records | Yes | `organization-inherited` |  |  | family |
| PE-8(1) | Automated Records Maintenance and Review | Yes | `organization-inherited` |  |  | family |
| PE-9 | Power Equipment and Cabling | Yes | `organization-inherited` |  |  | family |
| PE-10 | Emergency Shutoff | Yes | `organization-inherited` |  |  | family |
| PE-11 | Emergency Power | Yes | `organization-inherited` |  |  | family |
| PE-11(1) | Alternate Power Supply — Minimal Operational Capability | Yes | `organization-inherited` |  |  | family |
| PE-12 | Emergency Lighting | Yes | `organization-inherited` |  |  | family |
| PE-13 | Fire Protection | Yes | `organization-inherited` |  |  | family |
| PE-13(1) | Detection Systems — Automatic Activation and Notification | Yes | `organization-inherited` |  |  | family |
| PE-13(2) | Suppression Systems — Automatic Activation and Notification | Yes | `organization-inherited` |  |  | family |
| PE-14 | Environmental Controls | Yes | `organization-inherited` |  |  | family |
| PE-15 | Water Damage Protection | Yes | `organization-inherited` |  |  | family |
| PE-15(1) | Automation Support | Yes | `organization-inherited` |  |  | family |
| PE-16 | Delivery and Removal | Yes | `organization-inherited` |  |  | family |
| PE-17 | Alternate Work Site | Yes | `organization-inherited` |  |  | family |
| PE-18 | Location of System Components | Yes | `organization-inherited` |  |  | family |

<a id="pl"></a>

### PL

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| PL-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| PL-2 | System Security and Privacy Plans | Yes | `organization-inherited` |  |  | family |
| PL-4 | Rules of Behavior | Yes | `organization-inherited` |  |  | family |
| PL-4(1) | Social Media and External Site/Application Usage Restrictions | Yes | `organization-inherited` |  |  | family |
| PL-8 | Security and Privacy Architectures | Yes | `organization-inherited` |  |  | family |
| PL-10 | Baseline Selection | Yes | `organization-inherited` |  |  | family |
| PL-11 | Baseline Tailoring | Yes | `organization-inherited` |  |  | family |

<a id="ps"></a>

### PS

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| PS-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| PS-2 | Position Risk Designation | Yes | `organization-inherited` |  |  | family |
| PS-3 | Personnel Screening | Yes | `organization-inherited` |  |  | family |
| PS-4 | Personnel Termination | Yes | `organization-inherited` |  |  | family |
| PS-4(2) | Automated Actions | Yes | `organization-inherited` |  |  | family |
| PS-5 | Personnel Transfer | Yes | `organization-inherited` |  |  | family |
| PS-6 | Access Agreements | Yes | `organization-inherited` |  |  | family |
| PS-7 | External Personnel Security | Yes | `organization-inherited` |  |  | family |
| PS-8 | Personnel Sanctions | Yes | `organization-inherited` |  |  | family |
| PS-9 | Position Descriptions | Yes | `organization-inherited` |  |  | family |

<a id="ra"></a>

### RA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| RA-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| RA-2 | Security Categorization | Yes | `organization-inherited` |  |  | family |
| RA-3 | Risk Assessment | Yes | `organization-inherited` |  |  | family |
| RA-3(1) | Supply Chain Risk Assessment | Yes | `organization-inherited` |  |  | family |
| RA-5 | Vulnerability Monitoring and Scanning | Yes | `host-inherited` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | determination |
| RA-5(2) | Update Vulnerabilities to Be Scanned | Yes | `organization-inherited` |  |  | family |
| RA-5(4) | Discoverable Information | Yes | `organization-inherited` |  |  | family |
| RA-5(5) | Privileged Access | Yes | `organization-inherited` |  |  | family |
| RA-5(11) | Public Disclosure Program | Yes | `organization-inherited` |  |  | family |
| RA-7 | Risk Response | Yes | `organization-inherited` |  |  | family |
| RA-9 | Criticality Analysis | Yes | `organization-inherited` |  |  | family |

<a id="sa"></a>

### SA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| SA-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| SA-2 | Allocation of Resources | Yes | `organization-inherited` |  |  | family |
| SA-3 | System Development Life Cycle | Yes | `organization-inherited` |  |  | family |
| SA-4 | Acquisition Process | Yes | `organization-inherited` |  |  | family |
| SA-4(1) | Functional Properties of Controls | Yes | `organization-inherited` |  |  | family |
| SA-4(2) | Design and Implementation Information for Controls | Yes | `organization-inherited` |  |  | family |
| SA-4(5) | System, Component, and Service Configurations | Yes | `organization-inherited` |  |  | family |
| SA-4(9) | Functions, Ports, Protocols, and Services in Use | Yes | `organization-inherited` |  |  | family |
| SA-4(10) | Use of Approved PIV Products | Yes | `organization-inherited` |  |  | family |
| SA-5 | System Documentation | Yes | `organization-inherited` |  |  | family |
| SA-8 | Security and Privacy Engineering Principles | Yes | `organization-inherited` |  |  | family |
| SA-9 | External System Services | Yes | `organization-inherited` |  |  | family |
| SA-9(2) | Identification of Functions, Ports, Protocols, and Services | Yes | `organization-inherited` |  |  | family |
| SA-10 | Developer Configuration Management | Yes | `organization-inherited` |  |  | family |
| SA-11 | Developer Testing and Evaluation | Yes | `organization-inherited` |  |  | family |
| SA-15 | Development Process, Standards, and Tools | Yes | `organization-inherited` |  |  | family |
| SA-15(3) | Criticality Analysis | Yes | `organization-inherited` |  |  | family |
| SA-16 | Developer-provided Training | Yes | `organization-inherited` |  |  | family |
| SA-17 | Developer Security and Privacy Architecture and Design | Yes | `organization-inherited` |  |  | family |
| SA-21 | Developer Screening | Yes | `organization-inherited` |  |  | family |
| SA-22 | Unsupported System Components | Yes | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-29](../standard/criteria.md#img-29-base-kept-current) |  | criterion |

<a id="sc"></a>

### SC

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| SC-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| SC-2 | Separation of System and User Functionality | Yes | `image-owned` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) |  | criterion |
| SC-3 | Security Function Isolation | Yes | `host-inherited` | [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | expectation |
| SC-4 | Information in Shared System Resources | Yes | `host-inherited` |  | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed), [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | determination |
| SC-5 | Denial-of-service Protection | Yes | `deployment-configured` |  | [PLT-05](../standard/platform.md#plt-05-resources-are-bounded), [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| SC-5(2) | Capacity, Bandwidth, and Redundancy |  | `deployment-configured` |  | [PLT-05](../standard/platform.md#plt-05-resources-are-bounded) | expectation |
| SC-7 | Boundary Protection | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| SC-7(3) | Access Points | Yes | `host-inherited` |  | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| SC-7(4) | External Telecommunications Services | Yes | `organization-inherited` |  |  | determination |
| SC-7(5) | Deny by Default — Allow by Exception | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| SC-7(7) | Split Tunneling for Remote Devices | Yes | `not-applicable` |  |  | determination |
| SC-7(8) | Route Traffic to Authenticated Proxy Servers | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| SC-7(18) | Fail Secure | Yes | `host-inherited` |  | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| SC-7(21) | Isolation of System Components | Yes | `host-inherited` | [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated), [PLT-14](../standard/platform.md#plt-14-workloads-are-placed-by-sensitivity) | determination |
| SC-8 | Transmission Confidentiality and Integrity | Yes | `research-required` |  |  | undetermined |
| SC-8(1) | Cryptographic Protection | Yes | `research-required` |  |  | undetermined |
| SC-10 | Network Disconnect | Yes | `research-required` |  |  | undetermined |
| SC-12 | Cryptographic Key Establishment and Management | Yes | `deployment-configured` | [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files), [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| SC-12(1) | Availability | Yes | `deployment-configured` | [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files), [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| SC-13 | Cryptographic Protection | Yes | `research-required` |  |  | undetermined |
| SC-15 | Collaborative Computing Devices and Applications | Yes | `not-applicable` |  |  | determination |
| SC-17 | Public Key Infrastructure Certificates | Yes | `deployment-configured` | [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| SC-18 | Mobile Code | Yes | `research-required` |  |  | undetermined |
| SC-20 | Secure Name/Address Resolution Service (Authoritative Source) | Yes | `organization-inherited` |  |  | determination |
| SC-21 | Secure Name/Address Resolution Service (Recursive or Caching Resolver) | Yes | `organization-inherited` |  |  | determination |
| SC-22 | Architecture and Provisioning for Name/Address Resolution Service | Yes | `organization-inherited` |  |  | determination |
| SC-23 | Session Authenticity | Yes | `research-required` |  |  | undetermined |
| SC-24 | Fail in Known State | Yes | `image-owned` | [IMG-18](../standard/criteria.md#img-18-fails-closed) | [PLT-11](../standard/platform.md#plt-11-stops-are-given-time-to-finish) | criterion |
| SC-28 | Protection of Information at Rest | Yes | `host-inherited` | [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-17](../standard/platform.md#plt-17-data-volumes-are-encrypted-at-rest) | determination |
| SC-28(1) | Cryptographic Protection | Yes | `deployment-configured` | [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files), [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | expectation |
| SC-28(3) | Cryptographic Keys |  | `deployment-configured` | [IMG-05](../standard/criteria.md#img-05-no-secrets-in-the-build), [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| SC-39 | Process Isolation | Yes | `host-inherited` | [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | expectation |
| SC-45 | System Time Synchronization |  | `host-inherited` |  | [HST-05](../standard/platform.md#hst-05-clocks-are-synchronized) | expectation |

<a id="si"></a>

### SI

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| SI-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| SI-2 | Flaw Remediation | Yes | `image-owned` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation), [IMG-26](../standard/criteria.md#img-26-exceptions-expire), [IMG-29](../standard/criteria.md#img-29-base-kept-current) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | criterion |
| SI-2(2) | Automated Flaw Remediation Status | Yes | `host-inherited` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | determination |
| SI-2(6) | Removal of Previous Versions of Software and Firmware |  | `image-owned` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | criterion |
| SI-3 | Malicious Code Protection | Yes | `host-inherited` | [IMG-28](../standard/criteria.md#img-28-malware-scan) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | determination |
| SI-4 | System Monitoring | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-4(2) | Automated Tools and Mechanisms for Real-time Analysis | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-4(4) | Inbound and Outbound Communications Traffic | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-4(5) | System-generated Alerts | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-4(10) | Visibility of Encrypted Communications | Yes | `research-required` |  |  | undetermined |
| SI-4(12) | Automated Organization-generated Alerts | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-4(14) | Wireless Intrusion Detection | Yes | `organization-inherited` |  |  | determination |
| SI-4(20) | Privileged Users | Yes | `host-inherited` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| SI-4(22) | Unauthorized Network Services | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-5 | Security Alerts, Advisories, and Directives | Yes | `organization-inherited` |  |  | determination |
| SI-5(1) | Automated Alerts and Advisories | Yes | `organization-inherited` |  |  | determination |
| SI-6 | Security and Privacy Function Verification | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | expectation |
| SI-7 | Software, Firmware, and Information Integrity | Yes | `host-inherited` | [IMG-22](../standard/criteria.md#img-22-signed-with-provenance) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | determination |
| SI-7(1) | Integrity Checks | Yes | `host-inherited` | [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem), [IMG-22](../standard/criteria.md#img-22-signed-with-provenance) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-7(2) | Automated Notifications of Integrity Violations | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-7(5) | Automated Response to Integrity Violations | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-7(7) | Integration of Detection and Response | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| SI-7(15) | Code Authentication | Yes | `image-owned` | [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | determination |
| SI-8 | Spam Protection | Yes | `research-required` |  |  | undetermined |
| SI-8(2) | Automatic Updates | Yes | `research-required` |  |  | undetermined |
| SI-10 | Information Input Validation | Yes | `research-required` |  |  | undetermined |
| SI-11 | Error Handling | Yes | `research-required` |  |  | undetermined |
| SI-12 | Information Management and Retention | Yes | `organization-inherited` |  |  | determination |
| SI-16 | Memory Protection | Yes | `host-inherited` |  | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | determination |

<a id="sr"></a>

### SR

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| SR-1 | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| SR-2 | Supply Chain Risk Management Plan | Yes | `organization-inherited` |  |  | family |
| SR-2(1) | Establish SCRM Team | Yes | `organization-inherited` |  |  | family |
| SR-3 | Supply Chain Controls and Processes | Yes | `organization-inherited` |  |  | family |
| SR-5 | Acquisition Strategies, Tools, and Methods | Yes | `organization-inherited` |  |  | family |
| SR-6 | Supplier Assessments and Reviews | Yes | `organization-inherited` |  |  | family |
| SR-8 | Notification Agreements | Yes | `organization-inherited` |  |  | family |
| SR-9 | Tamper Resistance and Detection | Yes | `organization-inherited` |  |  | family |
| SR-9(1) | Multiple Stages of System Development Life Cycle | Yes | `organization-inherited` |  |  | family |
| SR-10 | Inspection of Systems or Components | Yes | `organization-inherited` |  |  | family |
| SR-11 | Component Authenticity | Yes | `organization-inherited` |  |  | family |
| SR-11(1) | Anti-counterfeit Training | Yes | `organization-inherited` |  |  | family |
| SR-11(2) | Configuration Control for Component Service and Repair | Yes | `organization-inherited` |  |  | family |
| SR-12 | Component Disposal | Yes | `organization-inherited` |  |  | family |

## Determinations

Where derivation would give the wrong answer. Each is held in [`artifacts/control-determinations.json`](../../artifacts/control-determinations.json), and the generator refuses one that repeats what derivation already gives.

- **AC-1** `organization-inherited`. Policy and procedures are written and maintained by the organization for the system. The standard is an input to them, not a substitute.
- **AC-2(13)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AC-3** `research-required`. Reached only through the platform keystore rule, but whether the image enforces access depends on its function: a database enforces access to its data and a static file server may not. The platform half, access to the keystore holding the image's secrets, is PLT-06.
- **AC-4(4)** `deployment-configured`. Boundary protection is network policy at the platform (PLT-10). The image declares the flows it needs (IMG-30), which is what lets the policy be deny-by-default.
- **AC-5** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AC-6** `image-owned`. The service runs as a non-root user with no capabilities and no way to gain privilege, which is least privilege for the process acting on a user's behalf. Least privilege for the image's own users, if it has any, is determined per image under AC-6 enhancements.
- **AC-6(7)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AC-11** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-11(1)** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-17** `host-inherited`. Remote access to the system is administration of the platform (PLT-13). The image offers no remote access of its own (IMG-27).
- **AC-17(1)** `host-inherited`. Remote access to the system is administration of the platform (PLT-13). The image offers no remote access of its own (IMG-27).
- **AC-17(2)** `research-required`. Cryptographic protection of remote sessions. The platform protects registry transport and traffic leaving it (PLT-01, PLT-10), but an image that terminates TLS itself, as nginx-ubi does, implements part of this. Which applies depends on the image.
- **AC-17(3)** `host-inherited`. Remote access to the system is administration of the platform (PLT-13). The image offers no remote access of its own (IMG-27).
- **AC-17(4)** `host-inherited`. Remote access to the system is administration of the platform (PLT-13). The image offers no remote access of its own (IMG-27).
- **AC-18** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-18(1)** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-18(3)** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-18(4)** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-18(5)** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-19** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-19(5)** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **AC-20** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AC-20(1)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AC-20(2)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AC-21** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AC-22** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **AU-1** `organization-inherited`. Policy and procedures are written and maintained by the organization for the system. The standard is an input to them, not a substitute.
- **AU-4** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-5** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-5(1)** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-5(2)** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-6** `organization-inherited`. Reviewing and analyzing audit records is done by the organization's people, using the platform's log store.
- **AU-6(1)** `organization-inherited`. Reviewing and analyzing audit records is done by the organization's people, using the platform's log store.
- **AU-6(3)** `organization-inherited`. Reviewing and analyzing audit records is done by the organization's people, using the platform's log store.
- **AU-6(4)** `host-inherited`. The image writes its logs to standard streams, which is what makes central review possible. The review itself happens in the platform's log store.
- **AU-6(5)** `organization-inherited`. Reviewing and analyzing audit records is done by the organization's people, using the platform's log store.
- **AU-6(6)** `organization-inherited`. Reviewing and analyzing audit records is done by the organization's people, using the platform's log store.
- **AU-7** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-7(1)** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-9(2)** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-9(3)** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-9(4)** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-11** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-12** `research-required`. The platform generates audit records for container creation and administration (PLT-13). Whether the image generates audit records of its own depends on its function: a database audits sessions and statements, a static file server has nothing to audit beyond its access log.
- **AU-12(1)** `host-inherited`. The image writes its records to standard streams and keeps none. Storing, protecting, retaining, and processing them is the platform's log store (PLT-09).
- **AU-12(3)** `host-inherited`. Deciding what is audited is a platform and organizational configuration; the image has no audit configuration a person changes at runtime.
- **CM-1** `organization-inherited`. Policy and procedures are written and maintained by the organization for the system. The standard is an input to them, not a substitute.
- **CM-2** `image-owned`. The image's baseline configuration is its lock, its build definition, and the labels that tie a built image to both. No SRG rule the standard cites reaches CM-2.
- **CM-2(2)** `image-owned`. The baseline is maintained automatically: the lock records every input, the build verifies it, and drift is reported without review being bypassed.
- **CM-2(3)** `image-owned`. Every released version is retained under an immutable tag, and the lock and build definition that produced it are in version control.
- **CM-2(7)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **CM-3** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-3(1)** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-3(2)** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-3(4)** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-3(6)** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-4** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-4(1)** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-4(2)** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-5** `host-inherited`. Access restrictions on changing the system are the platform's: who may deploy, and who may push to the registry. The image cannot be changed in place.
- **CM-6** `research-required`. Configuration settings are established by a DoD security configuration guide, which for an image means an agreed SCAP rule selection. That is target IMG-T3; until it is required this cannot be image-owned.
- **CM-6(2)** `host-inherited`. Detecting and responding to unauthorized changes or components at runtime is the platform's monitor. The image contributes an inventory and a read-only filesystem to compare against.
- **CM-7(1)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **CM-7(2)** `host-inherited`. Preventing unauthorized program execution is enforced by the platform admitting only authorized images and monitoring processes. The image contains only declared software.
- **CM-7(5)** `host-inherited`. Execution allow-listing is enforced by the platform admitting only authorized images. The image contributes by containing only declared software, but enforces nothing itself.
- **CM-8** `image-owned`. The image carries an inventory of its packages, an SBOM, and labels identifying its inputs. No SRG rule the standard cites reaches CM-8.
- **CM-8(1)** `image-owned`. The inventory is written at build time from what was actually installed, and regenerated with every build, so it cannot drift from the image.
- **CM-8(2)** `image-owned`. The inventory is written at build time from what was actually installed, and regenerated with every build, so it cannot drift from the image.
- **CM-8(3)** `host-inherited`. Detecting and responding to unauthorized changes or components at runtime is the platform's monitor. The image contributes an inventory and a read-only filesystem to compare against.
- **CM-8(4)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **CM-9** `organization-inherited`. Configuration change control, impact analysis, and the configuration management plan are organizational processes. The image contributes a reviewed change to its inputs (IMG-04), which is evidence for them, not the process itself.
- **CM-10** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **CM-11** `image-owned`. No software can be installed into a running image: it has no package manager and its software is not writable.
- **CM-12** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **CM-12(1)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **IA-1** `organization-inherited`. Policy and procedures are written and maintained by the organization for the system. The standard is an input to them, not a substitute.
- **IA-2(1)** `research-required`. Multifactor authentication for privileged accounts is the platform's for its administrators (PLT-13). An image with privileged accounts of its own, such as a database superuser, has to answer this for those accounts; one with no accounts does not.
- **IA-12** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **IA-12(2)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **IA-12(3)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **IA-12(4)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **IA-12(5)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **RA-5** `host-inherited`. The image is scanned at build, but vulnerability monitoring of the running system is the platform's continuous scanning.
- **SC-1** `organization-inherited`. Policy and procedures are written and maintained by the organization for the system. The standard is an input to them, not a substitute.
- **SC-4** `host-inherited`. Preventing information transfer through shared resources is namespace and privilege isolation, which the platform provides. The two platform expectations reaching it disagree on origination; isolation is the orchestrator's, so host-inherited.
- **SC-5** `deployment-configured`. Denial-of-service protection for a workload is its resource limits and the platform's network controls in front of it.
- **SC-7** `deployment-configured`. Boundary protection is network policy at the platform (PLT-10). The image declares the flows it needs (IMG-30), which is what lets the policy be deny-by-default.
- **SC-7(3)** `host-inherited`. Access points and the behaviour of boundary devices when they fail belong to the platform's network, not to a workload on it.
- **SC-7(4)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **SC-7(5)** `deployment-configured`. Boundary protection is network policy at the platform (PLT-10). The image declares the flows it needs (IMG-30), which is what lets the policy be deny-by-default.
- **SC-7(7)** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **SC-7(8)** `deployment-configured`. Boundary protection is network policy at the platform (PLT-10). The image declares the flows it needs (IMG-30), which is what lets the policy be deny-by-default.
- **SC-7(18)** `host-inherited`. Access points and the behaviour of boundary devices when they fail belong to the platform's network, not to a workload on it.
- **SC-7(21)** `host-inherited`. Isolating system components from one another is the platform's namespace isolation and placement by sensitivity.
- **SC-12** `deployment-configured`. The keys an image uses are established, stored, and rotated by the deployment's secret store and mounted read-only. The image holds none of its own.
- **SC-12(1)** `deployment-configured`. The keys an image uses are established, stored, and rotated by the deployment's secret store and mounted read-only. The image holds none of its own.
- **SC-15** `not-applicable`. Concerns a user's device or its radio, keyboard, or display. A container image has none, and runs on a server whose physical interfaces are the facility's.
- **SC-17** `deployment-configured`. The trust anchors a deployment relies on are chosen and mounted by the deployment. The image contributes by adding none of its own.
- **SC-20** `organization-inherited`. Name resolution is infrastructure the organization runs for the whole system; a container uses the resolver the platform gives it.
- **SC-21** `organization-inherited`. Name resolution is infrastructure the organization runs for the whole system; a container uses the resolver the platform gives it.
- **SC-22** `organization-inherited`. Name resolution is infrastructure the organization runs for the whole system; a container uses the resolver the platform gives it.
- **SC-28** `host-inherited`. Information at rest lives on volumes the platform provides and encrypts (PLT-17). The image confines persistent data to declared volumes.
- **SC-28(3)** `deployment-configured`. Protected storage for keys is the platform's secret store. The image contributes by never storing a secret itself and reading keys only from read-only mounts.
- **SI-1** `organization-inherited`. Policy and procedures are written and maintained by the organization for the system. The standard is an input to them, not a substitute.
- **SI-2(2)** `host-inherited`. Automated determination of whether running components are current is the platform's continuous scanning. The image records its findings with each release.
- **SI-3** `host-inherited`. Malicious code protection for the running system is the platform's continuous scanning. The image is scanned for malware before it is released (IMG-28), which is evidence for this control but not the control.
- **SI-4** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-4(2)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-4(4)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-4(5)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-4(12)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-4(14)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **SI-4(20)** `host-inherited`. Monitoring of privileged users is monitoring of the platform's administrators.
- **SI-4(22)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-5** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **SI-5(1)** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **SI-7** `host-inherited`. Integrity verification of software in use is the platform verifying the image signature at admission. The image contributes the signature.
- **SI-7(1)** `host-inherited`. Integrity of software in use is checked by the platform: signature verification at admission (PLT-01) and runtime monitoring of protected binaries (PLT-16). The image contributes its signature and a read-only, declared filesystem.
- **SI-7(2)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-7(5)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-7(7)** `host-inherited`. System monitoring is the platform's container-aware runtime monitor (PLT-16). The image contributes a declaration of expected behaviour to monitor against.
- **SI-7(15)** `image-owned`. Every component is authenticated by digest and, where the publisher signs, by signature before it is installed into the image. No SRG rule the standard cites reaches SI-7(15).
- **SI-12** `organization-inherited`. An organizational process, performed for the system rather than by any component of it.
- **SI-16** `host-inherited`. Memory protection, non-executable memory and address space randomization, is provided by the host kernel. It is reached through the platform's resource rule, which does not describe it.

### Family defaults

- **AT** `organization-inherited`. Awareness and training concern people, not a software component.
- **CA** `organization-inherited`. Assessment, authorization, and monitoring are performed on the system by the organization; an image is assessed, it does not assess.
- **CP** `organization-inherited`. Contingency planning, backup, and recovery are planned and exercised by the organization operating the system. An image holds no state of its own; its data lives on volumes the deployment provides.
- **IR** `organization-inherited`. Incident response is an organizational capability.
- **MA** `organization-inherited`. Maintenance of the system is performed by the organization. An image is not maintained in place; it is replaced.
- **MP** `organization-inherited`. Media protection concerns physical and removable media the organization handles.
- **PE** `organization-inherited`. Physical and environmental protection belongs to the facility.
- **PL** `organization-inherited`. Security and privacy planning is performed by the organization for the system.
- **PM** `organization-inherited`. Program management is organization-wide by definition.
- **PS** `organization-inherited`. Personnel security concerns people.
- **PT** `organization-inherited`. Processing of personally identifiable information is determined by the system's purpose, which the organization decides.
- **RA** `organization-inherited`. Risk assessment is performed by the organization for the system.
- **SA** `organization-inherited`. System and services acquisition concerns how the organization acquires and manages systems.
- **SR** `organization-inherited`. Supply chain risk management plans and processes are organizational. The image's own supply chain properties are recorded against CM-14, CM-2, CM-8, and SI-7(15).

---

Generated by `scripts/build-control-baseline.py` from the standard, the crosswalk, and the pinned NIST catalogue and High baseline. Do not edit by hand; the drift check fails.
