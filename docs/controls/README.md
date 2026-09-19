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
| [AC-1](../assessment/ac-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| [AC-2](../assessment/ac-2.md) | Account Management | Yes | `research-required` |  |  | undetermined |
| [AC-2(1)](../assessment/ac-2.1.md) | Automated System Account Management | Yes | `research-required` |  |  | undetermined |
| [AC-2(2)](../assessment/ac-2.2.md) | Automated Temporary and Emergency Account Management | Yes | `research-required` |  |  | undetermined |
| [AC-2(3)](../assessment/ac-2.3.md) | Disable Accounts | Yes | `research-required` |  |  | undetermined |
| [AC-2(4)](../assessment/ac-2.4.md) | Automated Audit Actions | Yes | `research-required` |  |  | undetermined |
| [AC-2(5)](../assessment/ac-2.5.md) | Inactivity Logout | Yes | `research-required` |  |  | undetermined |
| [AC-2(11)](../assessment/ac-2.11.md) | Usage Conditions | Yes | `research-required` |  |  | undetermined |
| [AC-2(12)](../assessment/ac-2.12.md) | Account Monitoring for Atypical Usage | Yes | `research-required` |  |  | undetermined |
| [AC-2(13)](../assessment/ac-2.13.md) | Disable Accounts for High-risk Individuals | Yes | `organization-inherited` |  |  | determination |
| [AC-3](../assessment/ac-3.md) | Access Enforcement | Yes | `research-required` |  | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| [AC-4](../assessment/ac-4.md) | Information Flow Enforcement | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | expectation |
| [AC-4(4)](../assessment/ac-4.4.md) | Flow Control of Encrypted Information | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [AC-5](../assessment/ac-5.md) | Separation of Duties | Yes | `organization-inherited` |  |  | determination |
| [AC-6](../assessment/ac-6.md) | Least Privilege | Yes | `image-owned` | [IMG-11](../standard/criteria.md#img-11-non-root-with-no-privilege-transition), [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed) | determination |
| [AC-6(1)](../assessment/ac-6.1.md) | Authorize Access to Security Functions | Yes | `research-required` |  |  | undetermined |
| [AC-6(2)](../assessment/ac-6.2.md) | Non-privileged Access for Nonsecurity Functions | Yes | `research-required` |  |  | undetermined |
| [AC-6(3)](../assessment/ac-6.3.md) | Network Access to Privileged Commands | Yes | `research-required` |  |  | undetermined |
| [AC-6(5)](../assessment/ac-6.5.md) | Privileged Accounts | Yes | `research-required` |  |  | undetermined |
| [AC-6(7)](../assessment/ac-6.7.md) | Review of User Privileges | Yes | `organization-inherited` |  |  | determination |
| [AC-6(8)](../assessment/ac-6.8.md) | Privilege Levels for Code Execution |  | `image-owned` | [IMG-09](../standard/criteria.md#img-09-no-privilege-raising-files), [IMG-11](../standard/criteria.md#img-11-non-root-with-no-privilege-transition), [IMG-12](../standard/criteria.md#img-12-runs-under-an-arbitrary-uid), [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges), [IMG-31](../standard/criteria.md#img-31-admitted-under-the-restricted-v2-scc-and-the-restricted-pod-security-standard), [IMG-32](../standard/criteria.md#img-32-runs-in-a-user-namespace-under-the-restricted-v3-scc) | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed) | criterion |
| [AC-6(9)](../assessment/ac-6.9.md) | Log Use of Privileged Functions | Yes | `research-required` |  |  | undetermined |
| [AC-6(10)](../assessment/ac-6.10.md) | Prohibit Non-privileged Users from Executing Privileged Functions | Yes | `image-owned` | [IMG-11](../standard/criteria.md#img-11-non-root-with-no-privilege-transition), [IMG-31](../standard/criteria.md#img-31-admitted-under-the-restricted-v2-scc-and-the-restricted-pod-security-standard) | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed) | criterion |
| [AC-7](../assessment/ac-7.md) | Unsuccessful Logon Attempts | Yes | `research-required` |  |  | undetermined |
| [AC-8](../assessment/ac-8.md) | System Use Notification | Yes | `research-required` |  |  | undetermined |
| [AC-10](../assessment/ac-10.md) | Concurrent Session Control | Yes | `research-required` |  |  | undetermined |
| [AC-11](../assessment/ac-11.md) | Device Lock | Yes | `not-applicable` |  |  | determination |
| [AC-11(1)](../assessment/ac-11.1.md) | Pattern-hiding Displays | Yes | `not-applicable` |  |  | determination |
| [AC-12](../assessment/ac-12.md) | Session Termination | Yes | `research-required` |  |  | undetermined |
| [AC-14](../assessment/ac-14.md) | Permitted Actions Without Identification or Authentication | Yes | `research-required` |  |  | undetermined |
| [AC-17](../assessment/ac-17.md) | Remote Access | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [AC-17(1)](../assessment/ac-17.1.md) | Monitoring and Control | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [AC-17(2)](../assessment/ac-17.2.md) | Protection of Confidentiality and Integrity Using Encryption | Yes | `research-required` |  | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [AC-17(3)](../assessment/ac-17.3.md) | Managed Access Control Points | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [AC-17(4)](../assessment/ac-17.4.md) | Privileged Commands and Access | Yes | `host-inherited` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [AC-18](../assessment/ac-18.md) | Wireless Access | Yes | `not-applicable` |  |  | determination |
| [AC-18(1)](../assessment/ac-18.1.md) | Authentication and Encryption | Yes | `not-applicable` |  |  | determination |
| [AC-18(3)](../assessment/ac-18.3.md) | Disable Wireless Networking | Yes | `not-applicable` |  |  | determination |
| [AC-18(4)](../assessment/ac-18.4.md) | Restrict Configurations by Users | Yes | `not-applicable` |  |  | determination |
| [AC-18(5)](../assessment/ac-18.5.md) | Antennas and Transmission Power Levels | Yes | `not-applicable` |  |  | determination |
| [AC-19](../assessment/ac-19.md) | Access Control for Mobile Devices | Yes | `not-applicable` |  |  | determination |
| [AC-19(5)](../assessment/ac-19.5.md) | Full Device or Container-based Encryption | Yes | `not-applicable` |  |  | determination |
| [AC-20](../assessment/ac-20.md) | Use of External Systems | Yes | `organization-inherited` |  |  | determination |
| [AC-20(1)](../assessment/ac-20.1.md) | Limits on Authorized Use | Yes | `organization-inherited` |  |  | determination |
| [AC-20(2)](../assessment/ac-20.2.md) | Portable Storage Devices — Restricted Use | Yes | `organization-inherited` |  |  | determination |
| [AC-21](../assessment/ac-21.md) | Information Sharing | Yes | `organization-inherited` |  |  | determination |
| [AC-22](../assessment/ac-22.md) | Publicly Accessible Content | Yes | `organization-inherited` |  |  | determination |

<a id="at"></a>

### AT

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [AT-1](../assessment/at-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [AT-2](../assessment/at-2.md) | Literacy Training and Awareness | Yes | `organization-inherited` |  |  | family |
| [AT-2(2)](../assessment/at-2.2.md) | Insider Threat | Yes | `organization-inherited` |  |  | family |
| [AT-2(3)](../assessment/at-2.3.md) | Social Engineering and Mining | Yes | `organization-inherited` |  |  | family |
| [AT-3](../assessment/at-3.md) | Role-based Training | Yes | `organization-inherited` |  |  | family |
| [AT-4](../assessment/at-4.md) | Training Records | Yes | `organization-inherited` |  |  | family |

<a id="au"></a>

### AU

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [AU-1](../assessment/au-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| [AU-2](../assessment/au-2.md) | Event Logging | Yes | `research-required` |  |  | undetermined |
| [AU-3](../assessment/au-3.md) | Content of Audit Records | Yes | `research-required` |  |  | undetermined |
| [AU-3(1)](../assessment/au-3.1.md) | Additional Audit Information | Yes | `research-required` |  |  | undetermined |
| [AU-4](../assessment/au-4.md) | Audit Log Storage Capacity | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-5](../assessment/au-5.md) | Response to Audit Logging Process Failures | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-5(1)](../assessment/au-5.1.md) | Storage Capacity Warning | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-5(2)](../assessment/au-5.2.md) | Real-time Alerts | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-6](../assessment/au-6.md) | Audit Record Review, Analysis, and Reporting | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| [AU-6(1)](../assessment/au-6.1.md) | Automated Process Integration | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| [AU-6(3)](../assessment/au-6.3.md) | Correlate Audit Record Repositories | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| [AU-6(4)](../assessment/au-6.4.md) | Central Review and Analysis |  | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-6(5)](../assessment/au-6.5.md) | Integrated Analysis of Audit Records | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| [AU-6(6)](../assessment/au-6.6.md) | Correlation with Physical Monitoring | Yes | `organization-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) |  | determination |
| [AU-7](../assessment/au-7.md) | Audit Record Reduction and Report Generation | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-7(1)](../assessment/au-7.1.md) | Automatic Processing | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-8](../assessment/au-8.md) | Time Stamps | Yes | `host-inherited` |  | [HST-05](../standard/platform.md#hst-05-clocks-are-synchronized) | expectation |
| [AU-9](../assessment/au-9.md) | Protection of Audit Information | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | expectation |
| [AU-9(2)](../assessment/au-9.2.md) | Store on Separate Physical Systems or Components | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-9(3)](../assessment/au-9.3.md) | Cryptographic Protection | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-9(4)](../assessment/au-9.4.md) | Access by Subset of Privileged Users | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-10](../assessment/au-10.md) | Non-repudiation | Yes | `research-required` |  |  | undetermined |
| [AU-11](../assessment/au-11.md) | Audit Record Retention | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-12](../assessment/au-12.md) | Audit Record Generation | Yes | `research-required` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [AU-12(1)](../assessment/au-12.1.md) | System-wide and Time-correlated Audit Trail | Yes | `host-inherited` | [IMG-19](../standard/criteria.md#img-19-logs-to-standard-streams-without-secrets) | [PLT-09](../standard/platform.md#plt-09-logs-are-collected-centrally) | determination |
| [AU-12(3)](../assessment/au-12.3.md) | Changes by Authorized Individuals | Yes | `host-inherited` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |

<a id="ca"></a>

### CA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [CA-1](../assessment/ca-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [CA-2](../assessment/ca-2.md) | Control Assessments | Yes | `organization-inherited` |  |  | family |
| [CA-2(1)](../assessment/ca-2.1.md) | Independent Assessors | Yes | `organization-inherited` |  |  | family |
| [CA-2(2)](../assessment/ca-2.2.md) | Specialized Assessments | Yes | `organization-inherited` |  |  | family |
| [CA-3](../assessment/ca-3.md) | Information Exchange | Yes | `organization-inherited` |  |  | family |
| [CA-3(6)](../assessment/ca-3.6.md) | Transfer Authorizations | Yes | `organization-inherited` |  |  | family |
| [CA-5](../assessment/ca-5.md) | Plan of Action and Milestones | Yes | `organization-inherited` |  |  | family |
| [CA-6](../assessment/ca-6.md) | Authorization | Yes | `organization-inherited` |  |  | family |
| [CA-7](../assessment/ca-7.md) | Continuous Monitoring | Yes | `organization-inherited` |  |  | family |
| [CA-7(1)](../assessment/ca-7.1.md) | Independent Assessment | Yes | `organization-inherited` |  |  | family |
| [CA-7(4)](../assessment/ca-7.4.md) | Risk Monitoring | Yes | `organization-inherited` |  |  | family |
| [CA-8](../assessment/ca-8.md) | Penetration Testing | Yes | `organization-inherited` |  |  | family |
| [CA-8(1)](../assessment/ca-8.1.md) | Independent Penetration Testing Agent or Team | Yes | `organization-inherited` |  |  | family |
| [CA-9](../assessment/ca-9.md) | Internal System Connections | Yes | `organization-inherited` |  |  | family |

<a id="cm"></a>

### CM

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [CM-1](../assessment/cm-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| [CM-2](../assessment/cm-2.md) | Baseline Configuration | Yes | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified), [IMG-23](../standard/criteria.md#img-23-identifying-labels) |  | determination |
| [CM-2(2)](../assessment/cm-2.2.md) | Automation Support for Accuracy and Currency | Yes | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified), [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change), [IMG-23](../standard/criteria.md#img-23-identifying-labels) |  | determination |
| [CM-2(3)](../assessment/cm-2.3.md) | Retention of Previous Configurations | Yes | `image-owned` | [IMG-23](../standard/criteria.md#img-23-identifying-labels), [IMG-24](../standard/criteria.md#img-24-immutable-tags) |  | determination |
| [CM-2(7)](../assessment/cm-2.7.md) | Configure Systems and Components for High-risk Areas | Yes | `organization-inherited` |  |  | determination |
| [CM-3](../assessment/cm-3.md) | Configuration Change Control | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-3(1)](../assessment/cm-3.1.md) | Automated Documentation, Notification, and Prohibition of Changes | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-3(2)](../assessment/cm-3.2.md) | Testing, Validation, and Documentation of Changes | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-3(4)](../assessment/cm-3.4.md) | Security and Privacy Representatives | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-3(6)](../assessment/cm-3.6.md) | Cryptography Management | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-4](../assessment/cm-4.md) | Impact Analyses | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-4(1)](../assessment/cm-4.1.md) | Separate Test Environments | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-4(2)](../assessment/cm-4.2.md) | Verification of Controls | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-5](../assessment/cm-5.md) | Access Restrictions for Change | Yes | `host-inherited` | [IMG-06](../standard/criteria.md#img-06-no-package-manager), [IMG-10](../standard/criteria.md#img-10-software-and-configuration-not-writable-by-the-service) | [PLT-12](../standard/platform.md#plt-12-registry-access-is-controlled-and-audited), [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [CM-5(1)](../assessment/cm-5.1.md) | Automated Access Enforcement and Audit Records | Yes | `deployment-configured` | [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-03](../standard/platform.md#plt-03-the-root-filesystem-is-read-only) | expectation |
| [CM-5(6)](../assessment/cm-5.6.md) | Limit Library Privileges |  | `image-owned` | [IMG-10](../standard/criteria.md#img-10-software-and-configuration-not-writable-by-the-service), [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-03](../standard/platform.md#plt-03-the-root-filesystem-is-read-only), [PLT-12](../standard/platform.md#plt-12-registry-access-is-controlled-and-audited) | criterion |
| [CM-6](../assessment/cm-6.md) | Configuration Settings | Yes | `research-required` |  |  | determination |
| [CM-6(1)](../assessment/cm-6.1.md) | Automated Management, Application, and Verification | Yes | `research-required` |  |  | undetermined |
| [CM-6(2)](../assessment/cm-6.2.md) | Respond to Unauthorized Changes | Yes | `host-inherited` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [CM-7](../assessment/cm-7.md) | Least Functionality | Yes | `image-owned` | [IMG-06](../standard/criteria.md#img-06-no-package-manager), [IMG-07](../standard/criteria.md#img-07-only-what-the-function-needs), [IMG-14](../standard/criteria.md#img-14-unprivileged-ports), [IMG-27](../standard/criteria.md#img-27-no-remote-administration), [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-04](../standard/platform.md#plt-04-ports-are-non-privileged-and-declared), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | criterion |
| [CM-7(1)](../assessment/cm-7.1.md) | Periodic Review | Yes | `organization-inherited` |  |  | determination |
| [CM-7(2)](../assessment/cm-7.2.md) | Prevent Program Execution | Yes | `host-inherited` | [IMG-07](../standard/criteria.md#img-07-only-what-the-function-needs), [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [CM-7(5)](../assessment/cm-7.5.md) | Authorized Software — Allow-by-exception | Yes | `host-inherited` | [IMG-07](../standard/criteria.md#img-07-only-what-the-function-needs) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | determination |
| [CM-8](../assessment/cm-8.md) | System Component Inventory | Yes | `image-owned` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-21](../standard/criteria.md#img-21-bill-of-materials), [IMG-23](../standard/criteria.md#img-23-identifying-labels) |  | determination |
| [CM-8(1)](../assessment/cm-8.1.md) | Updates During Installation and Removal | Yes | `image-owned` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-21](../standard/criteria.md#img-21-bill-of-materials) |  | determination |
| [CM-8(2)](../assessment/cm-8.2.md) | Automated Maintenance | Yes | `image-owned` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-21](../standard/criteria.md#img-21-bill-of-materials) |  | determination |
| [CM-8(3)](../assessment/cm-8.3.md) | Automated Unauthorized Component Detection | Yes | `host-inherited` | [IMG-08](../standard/criteria.md#img-08-embedded-package-inventory), [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [CM-8(4)](../assessment/cm-8.4.md) | Accountability Information | Yes | `organization-inherited` |  |  | determination |
| [CM-9](../assessment/cm-9.md) | Configuration Management Plan | Yes | `organization-inherited` | [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change) |  | determination |
| [CM-10](../assessment/cm-10.md) | Software Usage Restrictions | Yes | `organization-inherited` |  |  | determination |
| [CM-11](../assessment/cm-11.md) | User-installed Software | Yes | `image-owned` | [IMG-06](../standard/criteria.md#img-06-no-package-manager), [IMG-10](../standard/criteria.md#img-10-software-and-configuration-not-writable-by-the-service) |  | determination |
| [CM-11(2)](../assessment/cm-11.2.md) | Software Installation with Privileged Status |  | `image-owned` | [IMG-06](../standard/criteria.md#img-06-no-package-manager) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-12](../standard/platform.md#plt-12-registry-access-is-controlled-and-audited) | criterion |
| [CM-12](../assessment/cm-12.md) | Information Location | Yes | `organization-inherited` |  |  | determination |
| [CM-12(1)](../assessment/cm-12.1.md) | Automated Tools to Support Information Location | Yes | `organization-inherited` |  |  | determination |
| [CM-14](../assessment/cm-14.md) | Signed Components |  | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified), [IMG-03](../standard/criteria.md#img-03-hermetic-assembly), [IMG-04](../standard/criteria.md#img-04-input-refresh-is-a-reviewed-change), [IMG-22](../standard/criteria.md#img-22-signed-with-provenance) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | criterion |

<a id="cp"></a>

### CP

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [CP-1](../assessment/cp-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [CP-2](../assessment/cp-2.md) | Contingency Plan | Yes | `organization-inherited` |  |  | family |
| [CP-2(1)](../assessment/cp-2.1.md) | Coordinate with Related Plans | Yes | `organization-inherited` |  |  | family |
| [CP-2(2)](../assessment/cp-2.2.md) | Capacity Planning | Yes | `organization-inherited` |  |  | family |
| [CP-2(3)](../assessment/cp-2.3.md) | Resume Mission and Business Functions | Yes | `organization-inherited` |  |  | family |
| [CP-2(5)](../assessment/cp-2.5.md) | Continue Mission and Business Functions | Yes | `organization-inherited` |  |  | family |
| [CP-2(8)](../assessment/cp-2.8.md) | Identify Critical Assets | Yes | `organization-inherited` |  |  | family |
| [CP-3](../assessment/cp-3.md) | Contingency Training | Yes | `organization-inherited` |  |  | family |
| [CP-3(1)](../assessment/cp-3.1.md) | Simulated Events | Yes | `organization-inherited` |  |  | family |
| [CP-4](../assessment/cp-4.md) | Contingency Plan Testing | Yes | `organization-inherited` |  |  | family |
| [CP-4(1)](../assessment/cp-4.1.md) | Coordinate with Related Plans | Yes | `organization-inherited` |  |  | family |
| [CP-4(2)](../assessment/cp-4.2.md) | Alternate Processing Site | Yes | `organization-inherited` |  |  | family |
| [CP-6](../assessment/cp-6.md) | Alternate Storage Site | Yes | `organization-inherited` |  |  | family |
| [CP-6(1)](../assessment/cp-6.1.md) | Separation from Primary Site | Yes | `organization-inherited` |  |  | family |
| [CP-6(2)](../assessment/cp-6.2.md) | Recovery Time and Recovery Point Objectives | Yes | `organization-inherited` |  |  | family |
| [CP-6(3)](../assessment/cp-6.3.md) | Accessibility | Yes | `organization-inherited` |  |  | family |
| [CP-7](../assessment/cp-7.md) | Alternate Processing Site | Yes | `organization-inherited` |  |  | family |
| [CP-7(1)](../assessment/cp-7.1.md) | Separation from Primary Site | Yes | `organization-inherited` |  |  | family |
| [CP-7(2)](../assessment/cp-7.2.md) | Accessibility | Yes | `organization-inherited` |  |  | family |
| [CP-7(3)](../assessment/cp-7.3.md) | Priority of Service | Yes | `organization-inherited` |  |  | family |
| [CP-7(4)](../assessment/cp-7.4.md) | Preparation for Use | Yes | `organization-inherited` |  |  | family |
| [CP-8](../assessment/cp-8.md) | Telecommunications Services | Yes | `organization-inherited` |  |  | family |
| [CP-8(1)](../assessment/cp-8.1.md) | Priority of Service Provisions | Yes | `organization-inherited` |  |  | family |
| [CP-8(2)](../assessment/cp-8.2.md) | Single Points of Failure | Yes | `organization-inherited` |  |  | family |
| [CP-8(3)](../assessment/cp-8.3.md) | Separation of Primary and Alternate Providers | Yes | `organization-inherited` |  |  | family |
| [CP-8(4)](../assessment/cp-8.4.md) | Provider Contingency Plan | Yes | `organization-inherited` |  |  | family |
| [CP-9](../assessment/cp-9.md) | System Backup | Yes | `organization-inherited` |  |  | family |
| [CP-9(1)](../assessment/cp-9.1.md) | Testing for Reliability and Integrity | Yes | `organization-inherited` |  |  | family |
| [CP-9(2)](../assessment/cp-9.2.md) | Test Restoration Using Sampling | Yes | `organization-inherited` |  |  | family |
| [CP-9(3)](../assessment/cp-9.3.md) | Separate Storage for Critical Information | Yes | `organization-inherited` |  |  | family |
| [CP-9(5)](../assessment/cp-9.5.md) | Transfer to Alternate Storage Site | Yes | `organization-inherited` |  |  | family |
| [CP-9(8)](../assessment/cp-9.8.md) | Cryptographic Protection | Yes | `organization-inherited` |  |  | family |
| [CP-10](../assessment/cp-10.md) | System Recovery and Reconstitution | Yes | `organization-inherited` |  |  | family |
| [CP-10(2)](../assessment/cp-10.2.md) | Transaction Recovery | Yes | `organization-inherited` |  |  | family |
| [CP-10(4)](../assessment/cp-10.4.md) | Restore Within Time Period | Yes | `organization-inherited` |  |  | family |

<a id="ia"></a>

### IA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [IA-1](../assessment/ia-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| [IA-2](../assessment/ia-2.md) | Identification and Authentication (Organizational Users) | Yes | `research-required` |  | [PLT-18](../standard/platform.md#plt-18-workloads-have-identities-and-authenticate-each-other) | determination |
| [IA-2(1)](../assessment/ia-2.1.md) | Multi-factor Authentication to Privileged Accounts | Yes | `research-required` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [IA-2(2)](../assessment/ia-2.2.md) | Multi-factor Authentication to Non-privileged Accounts | Yes | `research-required` |  |  | undetermined |
| [IA-2(5)](../assessment/ia-2.5.md) | Individual Authentication with Group Authentication | Yes | `research-required` |  |  | undetermined |
| [IA-2(8)](../assessment/ia-2.8.md) | Access to Accounts — Replay Resistant | Yes | `research-required` |  |  | undetermined |
| [IA-2(12)](../assessment/ia-2.12.md) | Acceptance of PIV Credentials | Yes | `research-required` |  |  | undetermined |
| [IA-3](../assessment/ia-3.md) | Device Identification and Authentication | Yes | `host-inherited` |  | [PLT-15](../standard/platform.md#plt-15-nodes-are-trusted-before-they-run-workloads) | expectation |
| [IA-4](../assessment/ia-4.md) | Identifier Management | Yes | `research-required` |  |  | undetermined |
| [IA-4(4)](../assessment/ia-4.4.md) | Identify User Status | Yes | `research-required` |  |  | undetermined |
| [IA-5](../assessment/ia-5.md) | Authenticator Management | Yes | `research-required` |  |  | undetermined |
| [IA-5(1)](../assessment/ia-5.1.md) | Password-based Authentication | Yes | `research-required` |  |  | undetermined |
| [IA-5(2)](../assessment/ia-5.2.md) | Public Key-based Authentication | Yes | `research-required` |  |  | undetermined |
| [IA-5(6)](../assessment/ia-5.6.md) | Protection of Authenticators | Yes | `research-required` |  |  | undetermined |
| [IA-6](../assessment/ia-6.md) | Authentication Feedback | Yes | `research-required` |  |  | undetermined |
| [IA-7](../assessment/ia-7.md) | Cryptographic Module Authentication | Yes | `research-required` |  |  | undetermined |
| [IA-8](../assessment/ia-8.md) | Identification and Authentication (Non-organizational Users) | Yes | `research-required` |  |  | undetermined |
| [IA-8(1)](../assessment/ia-8.1.md) | Acceptance of PIV Credentials from Other Agencies | Yes | `research-required` |  |  | undetermined |
| [IA-8(2)](../assessment/ia-8.2.md) | Acceptance of External Authenticators | Yes | `research-required` |  |  | undetermined |
| [IA-8(4)](../assessment/ia-8.4.md) | Use of Defined Profiles | Yes | `research-required` |  |  | undetermined |
| [IA-11](../assessment/ia-11.md) | Re-authentication | Yes | `research-required` |  |  | undetermined |
| [IA-12](../assessment/ia-12.md) | Identity Proofing | Yes | `organization-inherited` |  |  | determination |
| [IA-12(2)](../assessment/ia-12.2.md) | Identity Evidence | Yes | `organization-inherited` |  |  | determination |
| [IA-12(3)](../assessment/ia-12.3.md) | Identity Evidence Validation and Verification | Yes | `organization-inherited` |  |  | determination |
| [IA-12(4)](../assessment/ia-12.4.md) | In-person Validation and Verification | Yes | `organization-inherited` |  |  | determination |
| [IA-12(5)](../assessment/ia-12.5.md) | Address Confirmation | Yes | `organization-inherited` |  |  | determination |

<a id="ir"></a>

### IR

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [IR-1](../assessment/ir-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [IR-2](../assessment/ir-2.md) | Incident Response Training | Yes | `organization-inherited` |  |  | family |
| [IR-2(1)](../assessment/ir-2.1.md) | Simulated Events | Yes | `organization-inherited` |  |  | family |
| [IR-2(2)](../assessment/ir-2.2.md) | Automated Training Environments | Yes | `organization-inherited` |  |  | family |
| [IR-3](../assessment/ir-3.md) | Incident Response Testing | Yes | `organization-inherited` |  |  | family |
| [IR-3(2)](../assessment/ir-3.2.md) | Coordination with Related Plans | Yes | `organization-inherited` |  |  | family |
| [IR-4](../assessment/ir-4.md) | Incident Handling | Yes | `organization-inherited` |  |  | family |
| [IR-4(1)](../assessment/ir-4.1.md) | Automated Incident Handling Processes | Yes | `organization-inherited` |  |  | family |
| [IR-4(4)](../assessment/ir-4.4.md) | Information Correlation | Yes | `organization-inherited` |  |  | family |
| [IR-4(11)](../assessment/ir-4.11.md) | Integrated Incident Response Team | Yes | `organization-inherited` |  |  | family |
| [IR-5](../assessment/ir-5.md) | Incident Monitoring | Yes | `organization-inherited` |  |  | family |
| [IR-5(1)](../assessment/ir-5.1.md) | Automated Tracking, Data Collection, and Analysis | Yes | `organization-inherited` |  |  | family |
| [IR-6](../assessment/ir-6.md) | Incident Reporting | Yes | `organization-inherited` |  |  | family |
| [IR-6(1)](../assessment/ir-6.1.md) | Automated Reporting | Yes | `organization-inherited` |  |  | family |
| [IR-6(3)](../assessment/ir-6.3.md) | Supply Chain Coordination | Yes | `organization-inherited` |  |  | family |
| [IR-7](../assessment/ir-7.md) | Incident Response Assistance | Yes | `organization-inherited` |  |  | family |
| [IR-7(1)](../assessment/ir-7.1.md) | Automation Support for Availability of Information and Support | Yes | `organization-inherited` |  |  | family |
| [IR-8](../assessment/ir-8.md) | Incident Response Plan | Yes | `organization-inherited` |  |  | family |

<a id="ma"></a>

### MA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [MA-1](../assessment/ma-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [MA-2](../assessment/ma-2.md) | Controlled Maintenance | Yes | `organization-inherited` |  |  | family |
| [MA-2(2)](../assessment/ma-2.2.md) | Automated Maintenance Activities | Yes | `organization-inherited` |  |  | family |
| [MA-3](../assessment/ma-3.md) | Maintenance Tools | Yes | `organization-inherited` |  |  | family |
| [MA-3(1)](../assessment/ma-3.1.md) | Inspect Tools | Yes | `organization-inherited` |  |  | family |
| [MA-3(2)](../assessment/ma-3.2.md) | Inspect Media | Yes | `organization-inherited` |  |  | family |
| [MA-3(3)](../assessment/ma-3.3.md) | Prevent Unauthorized Removal | Yes | `organization-inherited` |  |  | family |
| [MA-4](../assessment/ma-4.md) | Nonlocal Maintenance | Yes | `organization-inherited` |  |  | family |
| [MA-4(3)](../assessment/ma-4.3.md) | Comparable Security and Sanitization | Yes | `organization-inherited` |  |  | family |
| [MA-5](../assessment/ma-5.md) | Maintenance Personnel | Yes | `organization-inherited` |  |  | family |
| [MA-5(1)](../assessment/ma-5.1.md) | Individuals Without Appropriate Access | Yes | `organization-inherited` |  |  | family |
| [MA-6](../assessment/ma-6.md) | Timely Maintenance | Yes | `organization-inherited` |  |  | family |

<a id="mp"></a>

### MP

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [MP-1](../assessment/mp-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [MP-2](../assessment/mp-2.md) | Media Access | Yes | `organization-inherited` |  |  | family |
| [MP-3](../assessment/mp-3.md) | Media Marking | Yes | `organization-inherited` |  |  | family |
| [MP-4](../assessment/mp-4.md) | Media Storage | Yes | `organization-inherited` |  |  | family |
| [MP-5](../assessment/mp-5.md) | Media Transport | Yes | `organization-inherited` |  |  | family |
| [MP-6](../assessment/mp-6.md) | Media Sanitization | Yes | `organization-inherited` |  |  | family |
| [MP-6(1)](../assessment/mp-6.1.md) | Review, Approve, Track, Document, and Verify | Yes | `organization-inherited` |  |  | family |
| [MP-6(2)](../assessment/mp-6.2.md) | Equipment Testing | Yes | `organization-inherited` |  |  | family |
| [MP-6(3)](../assessment/mp-6.3.md) | Nondestructive Techniques | Yes | `organization-inherited` |  |  | family |
| [MP-7](../assessment/mp-7.md) | Media Use | Yes | `organization-inherited` |  |  | family |

<a id="pe"></a>

### PE

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [PE-1](../assessment/pe-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [PE-2](../assessment/pe-2.md) | Physical Access Authorizations | Yes | `organization-inherited` |  |  | family |
| [PE-3](../assessment/pe-3.md) | Physical Access Control | Yes | `organization-inherited` |  |  | family |
| [PE-3(1)](../assessment/pe-3.1.md) | System Access | Yes | `organization-inherited` |  |  | family |
| [PE-4](../assessment/pe-4.md) | Access Control for Transmission | Yes | `organization-inherited` |  |  | family |
| [PE-5](../assessment/pe-5.md) | Access Control for Output Devices | Yes | `organization-inherited` |  |  | family |
| [PE-6](../assessment/pe-6.md) | Monitoring Physical Access | Yes | `organization-inherited` |  |  | family |
| [PE-6(1)](../assessment/pe-6.1.md) | Intrusion Alarms and Surveillance Equipment | Yes | `organization-inherited` |  |  | family |
| [PE-6(4)](../assessment/pe-6.4.md) | Monitoring Physical Access to Systems | Yes | `organization-inherited` |  |  | family |
| [PE-8](../assessment/pe-8.md) | Visitor Access Records | Yes | `organization-inherited` |  |  | family |
| [PE-8(1)](../assessment/pe-8.1.md) | Automated Records Maintenance and Review | Yes | `organization-inherited` |  |  | family |
| [PE-9](../assessment/pe-9.md) | Power Equipment and Cabling | Yes | `organization-inherited` |  |  | family |
| [PE-10](../assessment/pe-10.md) | Emergency Shutoff | Yes | `organization-inherited` |  |  | family |
| [PE-11](../assessment/pe-11.md) | Emergency Power | Yes | `organization-inherited` |  |  | family |
| [PE-11(1)](../assessment/pe-11.1.md) | Alternate Power Supply — Minimal Operational Capability | Yes | `organization-inherited` |  |  | family |
| [PE-12](../assessment/pe-12.md) | Emergency Lighting | Yes | `organization-inherited` |  |  | family |
| [PE-13](../assessment/pe-13.md) | Fire Protection | Yes | `organization-inherited` |  |  | family |
| [PE-13(1)](../assessment/pe-13.1.md) | Detection Systems — Automatic Activation and Notification | Yes | `organization-inherited` |  |  | family |
| [PE-13(2)](../assessment/pe-13.2.md) | Suppression Systems — Automatic Activation and Notification | Yes | `organization-inherited` |  |  | family |
| [PE-14](../assessment/pe-14.md) | Environmental Controls | Yes | `organization-inherited` |  |  | family |
| [PE-15](../assessment/pe-15.md) | Water Damage Protection | Yes | `organization-inherited` |  |  | family |
| [PE-15(1)](../assessment/pe-15.1.md) | Automation Support | Yes | `organization-inherited` |  |  | family |
| [PE-16](../assessment/pe-16.md) | Delivery and Removal | Yes | `organization-inherited` |  |  | family |
| [PE-17](../assessment/pe-17.md) | Alternate Work Site | Yes | `organization-inherited` |  |  | family |
| [PE-18](../assessment/pe-18.md) | Location of System Components | Yes | `organization-inherited` |  |  | family |

<a id="pl"></a>

### PL

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [PL-1](../assessment/pl-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [PL-2](../assessment/pl-2.md) | System Security and Privacy Plans | Yes | `organization-inherited` |  |  | family |
| [PL-4](../assessment/pl-4.md) | Rules of Behavior | Yes | `organization-inherited` |  |  | family |
| [PL-4(1)](../assessment/pl-4.1.md) | Social Media and External Site/Application Usage Restrictions | Yes | `organization-inherited` |  |  | family |
| [PL-8](../assessment/pl-8.md) | Security and Privacy Architectures | Yes | `organization-inherited` |  |  | family |
| [PL-10](../assessment/pl-10.md) | Baseline Selection | Yes | `organization-inherited` |  |  | family |
| [PL-11](../assessment/pl-11.md) | Baseline Tailoring | Yes | `organization-inherited` |  |  | family |

<a id="ps"></a>

### PS

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [PS-1](../assessment/ps-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [PS-2](../assessment/ps-2.md) | Position Risk Designation | Yes | `organization-inherited` |  |  | family |
| [PS-3](../assessment/ps-3.md) | Personnel Screening | Yes | `organization-inherited` |  |  | family |
| [PS-4](../assessment/ps-4.md) | Personnel Termination | Yes | `organization-inherited` |  |  | family |
| [PS-4(2)](../assessment/ps-4.2.md) | Automated Actions | Yes | `organization-inherited` |  |  | family |
| [PS-5](../assessment/ps-5.md) | Personnel Transfer | Yes | `organization-inherited` |  |  | family |
| [PS-6](../assessment/ps-6.md) | Access Agreements | Yes | `organization-inherited` |  |  | family |
| [PS-7](../assessment/ps-7.md) | External Personnel Security | Yes | `organization-inherited` |  |  | family |
| [PS-8](../assessment/ps-8.md) | Personnel Sanctions | Yes | `organization-inherited` |  |  | family |
| [PS-9](../assessment/ps-9.md) | Position Descriptions | Yes | `organization-inherited` |  |  | family |

<a id="ra"></a>

### RA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [RA-1](../assessment/ra-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [RA-2](../assessment/ra-2.md) | Security Categorization | Yes | `organization-inherited` |  |  | family |
| [RA-3](../assessment/ra-3.md) | Risk Assessment | Yes | `organization-inherited` |  |  | family |
| [RA-3(1)](../assessment/ra-3.1.md) | Supply Chain Risk Assessment | Yes | `organization-inherited` |  |  | family |
| [RA-5](../assessment/ra-5.md) | Vulnerability Monitoring and Scanning | Yes | `host-inherited` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | determination |
| [RA-5(2)](../assessment/ra-5.2.md) | Update Vulnerabilities to Be Scanned | Yes | `organization-inherited` |  |  | family |
| [RA-5(4)](../assessment/ra-5.4.md) | Discoverable Information | Yes | `organization-inherited` |  |  | family |
| [RA-5(5)](../assessment/ra-5.5.md) | Privileged Access | Yes | `organization-inherited` |  |  | family |
| [RA-5(11)](../assessment/ra-5.11.md) | Public Disclosure Program | Yes | `organization-inherited` |  |  | family |
| [RA-7](../assessment/ra-7.md) | Risk Response | Yes | `organization-inherited` |  |  | family |
| [RA-9](../assessment/ra-9.md) | Criticality Analysis | Yes | `organization-inherited` |  |  | family |

<a id="sa"></a>

### SA

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [SA-1](../assessment/sa-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [SA-2](../assessment/sa-2.md) | Allocation of Resources | Yes | `organization-inherited` |  |  | family |
| [SA-3](../assessment/sa-3.md) | System Development Life Cycle | Yes | `organization-inherited` |  |  | family |
| [SA-4](../assessment/sa-4.md) | Acquisition Process | Yes | `organization-inherited` |  |  | family |
| [SA-4(1)](../assessment/sa-4.1.md) | Functional Properties of Controls | Yes | `organization-inherited` |  |  | family |
| [SA-4(2)](../assessment/sa-4.2.md) | Design and Implementation Information for Controls | Yes | `organization-inherited` |  |  | family |
| [SA-4(5)](../assessment/sa-4.5.md) | System, Component, and Service Configurations | Yes | `organization-inherited` |  |  | family |
| [SA-4(9)](../assessment/sa-4.9.md) | Functions, Ports, Protocols, and Services in Use | Yes | `organization-inherited` |  |  | family |
| [SA-4(10)](../assessment/sa-4.10.md) | Use of Approved PIV Products | Yes | `organization-inherited` |  |  | family |
| [SA-5](../assessment/sa-5.md) | System Documentation | Yes | `organization-inherited` |  |  | family |
| [SA-8](../assessment/sa-8.md) | Security and Privacy Engineering Principles | Yes | `organization-inherited` |  |  | family |
| [SA-9](../assessment/sa-9.md) | External System Services | Yes | `organization-inherited` |  |  | family |
| [SA-9(2)](../assessment/sa-9.2.md) | Identification of Functions, Ports, Protocols, and Services | Yes | `organization-inherited` |  |  | family |
| [SA-10](../assessment/sa-10.md) | Developer Configuration Management | Yes | `organization-inherited` |  |  | family |
| [SA-11](../assessment/sa-11.md) | Developer Testing and Evaluation | Yes | `organization-inherited` |  |  | family |
| [SA-15](../assessment/sa-15.md) | Development Process, Standards, and Tools | Yes | `organization-inherited` |  |  | family |
| [SA-15(3)](../assessment/sa-15.3.md) | Criticality Analysis | Yes | `organization-inherited` |  |  | family |
| [SA-16](../assessment/sa-16.md) | Developer-provided Training | Yes | `organization-inherited` |  |  | family |
| [SA-17](../assessment/sa-17.md) | Developer Security and Privacy Architecture and Design | Yes | `organization-inherited` |  |  | family |
| [SA-21](../assessment/sa-21.md) | Developer Screening | Yes | `organization-inherited` |  |  | family |
| [SA-22](../assessment/sa-22.md) | Unsupported System Components | Yes | `image-owned` | [IMG-01](../standard/criteria.md#img-01-base-image-pinned-by-digest), [IMG-29](../standard/criteria.md#img-29-base-kept-current) |  | criterion |

<a id="sc"></a>

### SC

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [SC-1](../assessment/sc-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| [SC-2](../assessment/sc-2.md) | Separation of System and User Functionality | Yes | `image-owned` | [IMG-27](../standard/criteria.md#img-27-no-remote-administration) |  | criterion |
| [SC-3](../assessment/sc-3.md) | Security Function Isolation | Yes | `host-inherited` | [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | expectation |
| [SC-4](../assessment/sc-4.md) | Information in Shared System Resources | Yes | `host-inherited` |  | [PLT-02](../standard/platform.md#plt-02-least-privilege-is-imposed), [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | determination |
| [SC-5](../assessment/sc-5.md) | Denial-of-service Protection | Yes | `deployment-configured` |  | [PLT-05](../standard/platform.md#plt-05-resources-are-bounded), [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [SC-5(2)](../assessment/sc-5.2.md) | Capacity, Bandwidth, and Redundancy |  | `deployment-configured` |  | [PLT-05](../standard/platform.md#plt-05-resources-are-bounded) | expectation |
| [SC-7](../assessment/sc-7.md) | Boundary Protection | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [SC-7(3)](../assessment/sc-7.3.md) | Access Points | Yes | `host-inherited` |  | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [SC-7(4)](../assessment/sc-7.4.md) | External Telecommunications Services | Yes | `organization-inherited` |  |  | determination |
| [SC-7(5)](../assessment/sc-7.5.md) | Deny by Default — Allow by Exception | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [SC-7(7)](../assessment/sc-7.7.md) | Split Tunneling for Remote Devices | Yes | `not-applicable` |  |  | determination |
| [SC-7(8)](../assessment/sc-7.8.md) | Route Traffic to Authenticated Proxy Servers | Yes | `deployment-configured` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [SC-7(18)](../assessment/sc-7.18.md) | Fail Secure | Yes | `host-inherited` |  | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted) | determination |
| [SC-7(21)](../assessment/sc-7.21.md) | Isolation of System Components | Yes | `host-inherited` | [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated), [PLT-14](../standard/platform.md#plt-14-workloads-are-placed-by-sensitivity) | determination |
| [SC-8](../assessment/sc-8.md) | Transmission Confidentiality and Integrity | Yes | `research-required` |  |  | undetermined |
| [SC-8(1)](../assessment/sc-8.1.md) | Cryptographic Protection | Yes | `research-required` |  |  | undetermined |
| [SC-10](../assessment/sc-10.md) | Network Disconnect | Yes | `research-required` |  |  | undetermined |
| [SC-12](../assessment/sc-12.md) | Cryptographic Key Establishment and Management | Yes | `deployment-configured` | [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files), [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| [SC-12(1)](../assessment/sc-12.1.md) | Availability | Yes | `deployment-configured` | [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files), [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| [SC-13](../assessment/sc-13.md) | Cryptographic Protection | Yes | `research-required` |  |  | undetermined |
| [SC-15](../assessment/sc-15.md) | Collaborative Computing Devices and Applications | Yes | `not-applicable` |  |  | determination |
| [SC-17](../assessment/sc-17.md) | Public Key Infrastructure Certificates | Yes | `deployment-configured` | [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| [SC-18](../assessment/sc-18.md) | Mobile Code | Yes | `research-required` |  |  | undetermined |
| [SC-20](../assessment/sc-20.md) | Secure Name/Address Resolution Service (Authoritative Source) | Yes | `organization-inherited` |  |  | determination |
| [SC-21](../assessment/sc-21.md) | Secure Name/Address Resolution Service (Recursive or Caching Resolver) | Yes | `organization-inherited` |  |  | determination |
| [SC-22](../assessment/sc-22.md) | Architecture and Provisioning for Name/Address Resolution Service | Yes | `organization-inherited` |  |  | determination |
| [SC-23](../assessment/sc-23.md) | Session Authenticity | Yes | `research-required` |  |  | undetermined |
| [SC-24](../assessment/sc-24.md) | Fail in Known State | Yes | `image-owned` | [IMG-18](../standard/criteria.md#img-18-fails-closed) | [PLT-11](../standard/platform.md#plt-11-stops-are-given-time-to-finish) | criterion |
| [SC-28](../assessment/sc-28.md) | Protection of Information at Rest | Yes | `host-inherited` | [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem) | [PLT-17](../standard/platform.md#plt-17-data-volumes-are-encrypted-at-rest) | determination |
| [SC-28(1)](../assessment/sc-28.1.md) | Cryptographic Protection | Yes | `deployment-configured` | [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files), [IMG-17](../standard/criteria.md#img-17-trust-material-supplied-by-the-operator) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | expectation |
| [SC-28(3)](../assessment/sc-28.3.md) | Cryptographic Keys |  | `deployment-configured` | [IMG-05](../standard/criteria.md#img-05-no-secrets-in-the-build), [IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files) | [PLT-06](../standard/platform.md#plt-06-secrets-are-delivered-as-read-only-files) | determination |
| [SC-39](../assessment/sc-39.md) | Process Isolation | Yes | `host-inherited` | [IMG-13](../standard/criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | expectation |
| [SC-45](../assessment/sc-45.md) | System Time Synchronization |  | `host-inherited` |  | [HST-05](../standard/platform.md#hst-05-clocks-are-synchronized) | expectation |

<a id="si"></a>

### SI

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [SI-1](../assessment/si-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | determination |
| [SI-2](../assessment/si-2.md) | Flaw Remediation | Yes | `image-owned` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation), [IMG-26](../standard/criteria.md#img-26-exceptions-expire), [IMG-29](../standard/criteria.md#img-29-base-kept-current) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | criterion |
| [SI-2(2)](../assessment/si-2.2.md) | Automated Flaw Remediation Status | Yes | `host-inherited` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | determination |
| [SI-2(6)](../assessment/si-2.6.md) | Removal of Previous Versions of Software and Firmware |  | `image-owned` | [IMG-25](../standard/criteria.md#img-25-vulnerability-gate-and-remediation) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | criterion |
| [SI-3](../assessment/si-3.md) | Malicious Code Protection | Yes | `host-inherited` | [IMG-28](../standard/criteria.md#img-28-malware-scan) | [PLT-08](../standard/platform.md#plt-08-images-are-scanned-and-replaced) | determination |
| [SI-4](../assessment/si-4.md) | System Monitoring | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-4(2)](../assessment/si-4.2.md) | Automated Tools and Mechanisms for Real-time Analysis | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-4(4)](../assessment/si-4.4.md) | Inbound and Outbound Communications Traffic | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-10](../standard/platform.md#plt-10-traffic-is-controlled-and-encrypted), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-4(5)](../assessment/si-4.5.md) | System-generated Alerts | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-4(10)](../assessment/si-4.10.md) | Visibility of Encrypted Communications | Yes | `research-required` |  |  | undetermined |
| [SI-4(12)](../assessment/si-4.12.md) | Automated Organization-generated Alerts | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-4(14)](../assessment/si-4.14.md) | Wireless Intrusion Detection | Yes | `organization-inherited` |  |  | determination |
| [SI-4(20)](../assessment/si-4.20.md) | Privileged Users | Yes | `host-inherited` |  | [PLT-13](../standard/platform.md#plt-13-orchestrator-administration-is-least-privilege-and-audited) | determination |
| [SI-4(22)](../assessment/si-4.22.md) | Unauthorized Network Services | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-5](../assessment/si-5.md) | Security Alerts, Advisories, and Directives | Yes | `organization-inherited` |  |  | determination |
| [SI-5(1)](../assessment/si-5.1.md) | Automated Alerts and Advisories | Yes | `organization-inherited` |  |  | determination |
| [SI-6](../assessment/si-6.md) | Security and Privacy Function Verification | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | expectation |
| [SI-7](../assessment/si-7.md) | Software, Firmware, and Information Integrity | Yes | `host-inherited` | [IMG-22](../standard/criteria.md#img-22-signed-with-provenance) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | determination |
| [SI-7(1)](../assessment/si-7.1.md) | Integrity Checks | Yes | `host-inherited` | [IMG-15](../standard/criteria.md#img-15-read-only-root-filesystem), [IMG-22](../standard/criteria.md#img-22-signed-with-provenance) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest), [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-7(2)](../assessment/si-7.2.md) | Automated Notifications of Integrity Violations | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-7(5)](../assessment/si-7.5.md) | Automated Response to Integrity Violations | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-7(7)](../assessment/si-7.7.md) | Integration of Detection and Response | Yes | `host-inherited` | [IMG-30](../standard/criteria.md#img-30-expected-behaviour-is-declared) | [PLT-16](../standard/platform.md#plt-16-runtime-behaviour-is-monitored) | determination |
| [SI-7(15)](../assessment/si-7.15.md) | Code Authentication | Yes | `image-owned` | [IMG-02](../standard/criteria.md#img-02-every-build-input-pinned-and-verified) | [PLT-01](../standard/platform.md#plt-01-images-are-admitted-by-verified-digest) | determination |
| [SI-8](../assessment/si-8.md) | Spam Protection | Yes | `research-required` |  |  | undetermined |
| [SI-8(2)](../assessment/si-8.2.md) | Automatic Updates | Yes | `research-required` |  |  | undetermined |
| [SI-10](../assessment/si-10.md) | Information Input Validation | Yes | `research-required` |  |  | undetermined |
| [SI-11](../assessment/si-11.md) | Error Handling | Yes | `research-required` |  |  | undetermined |
| [SI-12](../assessment/si-12.md) | Information Management and Retention | Yes | `organization-inherited` |  |  | determination |
| [SI-16](../assessment/si-16.md) | Memory Protection | Yes | `host-inherited` |  | [PLT-07](../standard/platform.md#plt-07-containers-are-isolated) | determination |

<a id="sr"></a>

### SR

| Control | Title | High | Origination | Criteria | Handoff | Basis |
| --- | --- | :-: | --- | --- | --- | --- |
| [SR-1](../assessment/sr-1.md) | Policy and Procedures | Yes | `organization-inherited` |  |  | family |
| [SR-2](../assessment/sr-2.md) | Supply Chain Risk Management Plan | Yes | `organization-inherited` |  |  | family |
| [SR-2(1)](../assessment/sr-2.1.md) | Establish SCRM Team | Yes | `organization-inherited` |  |  | family |
| [SR-3](../assessment/sr-3.md) | Supply Chain Controls and Processes | Yes | `organization-inherited` |  |  | family |
| [SR-5](../assessment/sr-5.md) | Acquisition Strategies, Tools, and Methods | Yes | `organization-inherited` |  |  | family |
| [SR-6](../assessment/sr-6.md) | Supplier Assessments and Reviews | Yes | `organization-inherited` |  |  | family |
| [SR-8](../assessment/sr-8.md) | Notification Agreements | Yes | `organization-inherited` |  |  | family |
| [SR-9](../assessment/sr-9.md) | Tamper Resistance and Detection | Yes | `organization-inherited` |  |  | family |
| [SR-9(1)](../assessment/sr-9.1.md) | Multiple Stages of System Development Life Cycle | Yes | `organization-inherited` |  |  | family |
| [SR-10](../assessment/sr-10.md) | Inspection of Systems or Components | Yes | `organization-inherited` |  |  | family |
| [SR-11](../assessment/sr-11.md) | Component Authenticity | Yes | `organization-inherited` |  |  | family |
| [SR-11(1)](../assessment/sr-11.1.md) | Anti-counterfeit Training | Yes | `organization-inherited` |  |  | family |
| [SR-11(2)](../assessment/sr-11.2.md) | Configuration Control for Component Service and Repair | Yes | `organization-inherited` |  |  | family |
| [SR-12](../assessment/sr-12.md) | Component Disposal | Yes | `organization-inherited` |  |  | family |

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
- **AC-17(2)** `research-required`. Cryptographic protection of remote sessions. The platform protects registry transport and traffic leaving it (PLT-01, PLT-10), but an image that terminates TLS itself, as a web server or reverse proxy usually does, implements part of this. Which applies depends on the image.
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
- **IA-2** `research-required`. The platform identifies and authenticates workloads acting on a user's behalf (PLT-18). Whether the image identifies and authenticates users of its own depends on its function: a database does, a static file server does not.
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
