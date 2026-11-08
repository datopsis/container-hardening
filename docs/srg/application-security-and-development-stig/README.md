# Application Security and Development Security Technical Implementation Guide

Release: 5 Benchmark Date: 30 Sep 2026. Accepted 2026-08-25.

| | |
| --- | --- |
| Benchmark | `Application_Security_Development_STIG` |
| Rules | **286** |
| CAT I | 34 |
| CAT II | 230 |
| CAT III | 22 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-222387`](rules/V-222387.md) | `APSC-DV-000010` | CAT II | The application must provide a capability to limit the number of logon sessions per user. |
| [`V-222388`](rules/V-222388.md) | `APSC-DV-000060` | CAT II | The application must clear temporary storage and cookies when the session is terminated. |
| [`V-222389`](rules/V-222389.md) | `APSC-DV-000070` | CAT II | The application must automatically terminate the non-privileged user session and log off non-privileged users after a 15 minute idle time period has elapsed. |
| [`V-222390`](rules/V-222390.md) | `APSC-DV-000080` | CAT II | The application must automatically terminate the admin user session and log off admin users after a 10 minute idle time period is exceeded. |
| [`V-222391`](rules/V-222391.md) | `APSC-DV-000090` | CAT II | Applications requiring user access authentication must provide a logoff capability for user initiated communication session. |
| [`V-222392`](rules/V-222392.md) | `APSC-DV-000100` | CAT III | The application must display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions. |
| [`V-222393`](rules/V-222393.md) | `APSC-DV-000110` | CAT II | The application must associate organization-defined types of security attributes having organization-defined security attribute values with information in storage. |
| [`V-222394`](rules/V-222394.md) | `APSC-DV-000120` | CAT II | The application must associate organization-defined types of security attributes having organization-defined security attribute values with information in process. |
| [`V-222395`](rules/V-222395.md) | `APSC-DV-000130` | CAT II | The application must associate organization-defined types of security attributes having organization-defined security attribute values with information in transmission. |
| [`V-222396`](rules/V-222396.md) | `APSC-DV-000160` | CAT II | The application must implement DoW-approved encryption to protect the confidentiality of remote access sessions. |
| [`V-222397`](rules/V-222397.md) | `APSC-DV-000170` | CAT II | The application must implement cryptographic mechanisms to protect the integrity of remote access sessions. |
| [`V-222398`](rules/V-222398.md) | `APSC-DV-000180` | CAT II | Applications with SOAP messages requiring integrity must include the following message elements:-Message ID-Service Request-Timestamp-SAML Assertion (optionally included in messages) and all elements of the message must be digitally signed. |
| [`V-222399`](rules/V-222399.md) | `APSC-DV-000190` | CAT I | Messages protected with WS_Security must use time stamps with creation and expiration times. |
| [`V-222400`](rules/V-222400.md) | `APSC-DV-000200` | CAT I | Validity periods must be verified on all application messages using WS-Security or SAML assertions. |
| [`V-222401`](rules/V-222401.md) | `APSC-DV-000210` | CAT II | The application must ensure each unique asserting party provides unique assertion ID references for each SAML assertion. |
| [`V-222402`](rules/V-222402.md) | `APSC-DV-000220` | CAT II | The application must ensure encrypted assertions, or equivalent confidentiality protections are used when assertion data is passed through an intermediary, and confidentiality of the assertion data is required when passing through the intermediary. |
| [`V-222403`](rules/V-222403.md) | `APSC-DV-000230` | CAT I | The application must use the NotOnOrAfter condition when using the SubjectConfirmation element in a SAML assertion. |
| [`V-222404`](rules/V-222404.md) | `APSC-DV-000240` | CAT I | The application must use both the NotBefore and NotOnOrAfter elements or OneTimeUse element when using the Conditions element in a SAML assertion. |
| [`V-222405`](rules/V-222405.md) | `APSC-DV-000250` | CAT II | The application must ensure if a OneTimeUse element is used in an assertion, there is only one of the same used in the Conditions element portion of an assertion. |
| [`V-222406`](rules/V-222406.md) | `APSC-DV-000260` | CAT II | The application must ensure messages are encrypted when the SessionIndex is tied to privacy data. |
| [`V-222407`](rules/V-222407.md) | `APSC-DV-000280` | CAT II | The application must provide automated mechanisms for supporting account management functions. |
| [`V-222408`](rules/V-222408.md) | `APSC-DV-000290` | CAT II | Shared/group account credentials must be terminated when members leave the group. |
| [`V-222409`](rules/V-222409.md) | `APSC-DV-000300` | CAT II | The application must automatically remove or disable temporary user accounts 72 hours after account creation. |
| [`V-222410`](rules/V-222410.md) | `APSC-DV-000310` | CAT III | The application must have a process, feature or function that prevents removal or disabling of emergency accounts. |
| [`V-222411`](rules/V-222411.md) | `APSC-DV-000320` | CAT III | The application must automatically disable accounts after a 35 day period of account inactivity. |
| [`V-222412`](rules/V-222412.md) | `APSC-DV-000330` | CAT II | Unnecessary application accounts must be disabled, or deleted. |
| [`V-222413`](rules/V-222413.md) | `APSC-DV-000340` | CAT II | The application must automatically audit account creation. |
| [`V-222414`](rules/V-222414.md) | `APSC-DV-000350` | CAT II | The application must automatically audit account modification. |
| [`V-222415`](rules/V-222415.md) | `APSC-DV-000360` | CAT II | The application must automatically audit account disabling actions. |
| [`V-222416`](rules/V-222416.md) | `APSC-DV-000370` | CAT II | The application must automatically audit account removal actions. |
| [`V-222417`](rules/V-222417.md) | `APSC-DV-000380` | CAT III | The application must notify system administrators (SAs) and information system security officers (ISSOs) when accounts are created. |
| [`V-222418`](rules/V-222418.md) | `APSC-DV-000390` | CAT III | The application must notify system administrators (SAs) and information system security officers (ISSOs) when accounts are modified. |
| [`V-222419`](rules/V-222419.md) | `APSC-DV-000400` | CAT III | The application must notify system administrators (SAs) and information system security officers (ISSOs) of account disabling actions. |
| [`V-222420`](rules/V-222420.md) | `APSC-DV-000410` | CAT III | The application must notify system administrators (SAs) and information system security officers (ISSOs) of account removal actions. |
| [`V-222421`](rules/V-222421.md) | `APSC-DV-000420` | CAT II | The application must automatically audit account enabling actions. |
| [`V-222422`](rules/V-222422.md) | `APSC-DV-000430` | CAT III | The application must notify system administrators (SAs) and information system security officers (ISSOs) of account enabling actions. |
| [`V-222423`](rules/V-222423.md) | `APSC-DV-000440` | CAT II | Application data protection requirements must be identified and documented. |
| [`V-222424`](rules/V-222424.md) | `APSC-DV-000450` | CAT II | The application must utilize organization-defined data mining detection techniques for organization-defined data storage objects to adequately detect data mining attempts. |
| [`V-222425`](rules/V-222425.md) | `APSC-DV-000460` | CAT I | The application must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. |
| [`V-222426`](rules/V-222426.md) | `APSC-DV-000470` | CAT II | The application must enforce organization-defined discretionary access control policies over defined subjects and objects. |
| [`V-222427`](rules/V-222427.md) | `APSC-DV-000480` | CAT II | The application must enforce approved authorizations for controlling the flow of information within the system based on organization-defined information flow control policies. |
| [`V-222428`](rules/V-222428.md) | `APSC-DV-000490` | CAT II | The application must enforce approved authorizations for controlling the flow of information between interconnected systems based on organization-defined information flow control policies. |
| [`V-222429`](rules/V-222429.md) | `APSC-DV-000500` | CAT II | The application must prevent non-privileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures. |
| [`V-222430`](rules/V-222430.md) | `APSC-DV-000510` | CAT I | The application must execute without excessive account permissions. |
| [`V-222431`](rules/V-222431.md) | `APSC-DV-000520` | CAT II | The application must audit the execution of privileged functions. |
| [`V-222432`](rules/V-222432.md) | `APSC-DV-000530` | CAT I | The application must enforce the limit of three consecutive invalid logon attempts by a user during a 15 minute time period. |
| [`V-222433`](rules/V-222433.md) | `APSC-DV-000540` | CAT II | The application administrator must follow an approved process to unlock locked user accounts. |
| [`V-222434`](rules/V-222434.md) | `APSC-DV-000550` | CAT III | The application must display the Standard Mandatory DoW Notice and Consent Banner before granting access to the application. |
| [`V-222435`](rules/V-222435.md) | `APSC-DV-000560` | CAT III | The application must retain the Standard Mandatory DoW Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access. |
| [`V-222436`](rules/V-222436.md) | `APSC-DV-000570` | CAT III | The publicly accessible application must display the Standard Mandatory DoW Notice and Consent Banner before granting access to the application. |
| [`V-222437`](rules/V-222437.md) | `APSC-DV-000580` | CAT III | The application must display the time and date of the users last successful logon. |
| [`V-222438`](rules/V-222438.md) | `APSC-DV-000590` | CAT II | The application must protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation. |
| [`V-222439`](rules/V-222439.md) | `APSC-DV-000600` | CAT II | For applications providing audit record aggregation, the application must compile audit records from organization-defined information system components into a system-wide audit trail that is time-correlated with an organization-defined level of tolerance for the relationship between time stamps of individual records in the audit trail. |
| [`V-222441`](rules/V-222441.md) | `APSC-DV-000620` | CAT II | The application must provide audit record generation capability for the creation of session IDs. |
| [`V-222442`](rules/V-222442.md) | `APSC-DV-000630` | CAT II | The application must provide audit record generation capability for the destruction of session IDs. |
| [`V-222443`](rules/V-222443.md) | `APSC-DV-000640` | CAT II | The application must provide audit record generation capability for the renewal of session IDs. |
| [`V-222444`](rules/V-222444.md) | `APSC-DV-000650` | CAT II | The application must not write sensitive data into the application logs. |
| [`V-222445`](rules/V-222445.md) | `APSC-DV-000660` | CAT II | The application must provide audit record generation capability for session timeouts. |
| [`V-222446`](rules/V-222446.md) | `APSC-DV-000670` | CAT II | The application must record a time stamp indicating when the event occurred. |
| [`V-222447`](rules/V-222447.md) | `APSC-DV-000680` | CAT II | The application must provide audit record generation capability for HTTP headers including User-Agent, Referer, GET, and POST. |
| [`V-222448`](rules/V-222448.md) | `APSC-DV-000690` | CAT II | The application must provide audit record generation capability for connecting system IP addresses. |
| [`V-222449`](rules/V-222449.md) | `APSC-DV-000700` | CAT II | The application must record the username or user ID of the user associated with the event. |
| [`V-222450`](rules/V-222450.md) | `APSC-DV-000710` | CAT II | The application must generate audit records when successful/unsuccessful attempts to grant privileges occur. |
| [`V-222451`](rules/V-222451.md) | `APSC-DV-000720` | CAT II | The application must generate audit records when successful/unsuccessful attempts to access security objects occur. |
| [`V-222452`](rules/V-222452.md) | `APSC-DV-000730` | CAT II | The application must generate audit records when successful/unsuccessful attempts to access security levels occur. |
| [`V-222453`](rules/V-222453.md) | `APSC-DV-000740` | CAT II | The application must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur. |
| [`V-222454`](rules/V-222454.md) | `APSC-DV-000750` | CAT II | The application must generate audit records when successful/unsuccessful attempts to modify privileges occur. |
| [`V-222455`](rules/V-222455.md) | `APSC-DV-000760` | CAT II | The application must generate audit records when successful/unsuccessful attempts to modify security objects occur. |
| [`V-222456`](rules/V-222456.md) | `APSC-DV-000770` | CAT II | The application must generate audit records when successful/unsuccessful attempts to modify security levels occur. |
| [`V-222457`](rules/V-222457.md) | `APSC-DV-000780` | CAT II | The application must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur. |
| [`V-222458`](rules/V-222458.md) | `APSC-DV-000790` | CAT II | The application must generate audit records when successful/unsuccessful attempts to delete privileges occur. |
| [`V-222459`](rules/V-222459.md) | `APSC-DV-000800` | CAT II | The application must generate audit records when successful/unsuccessful attempts to delete security levels occur. |
| [`V-222460`](rules/V-222460.md) | `APSC-DV-000810` | CAT II | The application must generate audit records when successful/unsuccessful attempts to delete application database security objects occur. |
| [`V-222461`](rules/V-222461.md) | `APSC-DV-000820` | CAT II | The application must generate audit records when successful/unsuccessful attempts to delete categories of information (e.g., classification levels) occur. |
| [`V-222462`](rules/V-222462.md) | `APSC-DV-000830` | CAT II | The application must generate audit records when successful/unsuccessful logon attempts occur. |
| [`V-222463`](rules/V-222463.md) | `APSC-DV-000840` | CAT II | The application must generate audit records for privileged activities or other system-level access. |
| [`V-222464`](rules/V-222464.md) | `APSC-DV-000850` | CAT II | The application must generate audit records showing starting and ending time for user access to the system. |
| [`V-222465`](rules/V-222465.md) | `APSC-DV-000860` | CAT II | The application must generate audit records when successful/unsuccessful accesses to objects occur. |
| [`V-222466`](rules/V-222466.md) | `APSC-DV-000870` | CAT II | The application must generate audit records for all direct access to the information system. |
| [`V-222467`](rules/V-222467.md) | `APSC-DV-000880` | CAT II | The application must generate audit records for all account creations, modifications, disabling, and termination events. |
| [`V-222468`](rules/V-222468.md) | `APSC-DV-000910` | CAT II | The application must initiate session auditing upon startup. |
| [`V-222469`](rules/V-222469.md) | `APSC-DV-000940` | CAT II | The application must log application shutdown events. |
| [`V-222470`](rules/V-222470.md) | `APSC-DV-000950` | CAT II | The application must log destination IP addresses. |
| [`V-222471`](rules/V-222471.md) | `APSC-DV-000960` | CAT II | The application must log user actions involving access to data. |
| [`V-222472`](rules/V-222472.md) | `APSC-DV-000970` | CAT II | The application must log user actions involving changes to data. |
| [`V-222473`](rules/V-222473.md) | `APSC-DV-000980` | CAT II | The application must produce audit records containing information to establish when (date and time) the events occurred. |
| [`V-222474`](rules/V-222474.md) | `APSC-DV-000990` | CAT II | The application must produce audit records containing enough information to establish which component, feature or function of the application triggered the audit event. |
| [`V-222475`](rules/V-222475.md) | `APSC-DV-001000` | CAT II | When using centralized logging; the application must include a unique identifier in order to distinguish itself from other application logs. |
| [`V-222476`](rules/V-222476.md) | `APSC-DV-001010` | CAT II | The application must produce audit records that contain information to establish the outcome of the events. |
| [`V-222477`](rules/V-222477.md) | `APSC-DV-001020` | CAT II | The application must generate audit records containing information that establishes the identity of any individual or process associated with the event. |
| [`V-222478`](rules/V-222478.md) | `APSC-DV-001030` | CAT II | The application must generate audit records containing the full-text recording of privileged commands or the individual identities of group account users. |
| [`V-222479`](rules/V-222479.md) | `APSC-DV-001040` | CAT II | The application must implement transaction recovery logs when transaction based. |
| [`V-222480`](rules/V-222480.md) | `APSC-DV-001050` | CAT II | The application must provide centralized management and configuration of the content to be captured in audit records generated by all application components. |
| [`V-222481`](rules/V-222481.md) | `APSC-DV-001070` | CAT II | The application must off-load audit records onto a different system or media than the system being audited. |
| [`V-222482`](rules/V-222482.md) | `APSC-DV-001080` | CAT II | The application must be configured to write application logs to a centralized log repository. |
| [`V-222483`](rules/V-222483.md) | `APSC-DV-001090` | CAT II | The application must provide an immediate warning to the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity. |
| [`V-222484`](rules/V-222484.md) | `APSC-DV-001100` | CAT II | Applications categorized as having a moderate or high impact must provide an immediate real-time alert to the SA and ISSO (at a minimum) for all audit failure events. |
| [`V-222485`](rules/V-222485.md) | `APSC-DV-001110` | CAT II | The application must alert the ISSO and SA (at a minimum) in the event of an audit processing failure. |
| [`V-222486`](rules/V-222486.md) | `APSC-DV-001120` | CAT II | The application must shut down by default upon audit failure (unless availability is an overriding concern). |
| [`V-222487`](rules/V-222487.md) | `APSC-DV-001130` | CAT II | The application must provide the capability to centrally review and analyze audit records from multiple components within the system. |
| [`V-222488`](rules/V-222488.md) | `APSC-DV-001140` | CAT II | The application must provide the capability to filter audit records for events of interest based upon organization-defined criteria. |
| [`V-222489`](rules/V-222489.md) | `APSC-DV-001150` | CAT II | The application must provide an audit reduction capability that supports on-demand reporting requirements. |
| [`V-222490`](rules/V-222490.md) | `APSC-DV-001160` | CAT II | The application must provide an audit reduction capability that supports on-demand audit review and analysis. |
| [`V-222491`](rules/V-222491.md) | `APSC-DV-001170` | CAT II | The application must provide an audit reduction capability that supports after-the-fact investigations of security incidents. |
| [`V-222492`](rules/V-222492.md) | `APSC-DV-001180` | CAT II | The application must provide a report generation capability that supports on-demand audit review and analysis. |
| [`V-222493`](rules/V-222493.md) | `APSC-DV-001190` | CAT II | The application must provide a report generation capability that supports on-demand reporting requirements. |
| [`V-222494`](rules/V-222494.md) | `APSC-DV-001200` | CAT II | The application must provide a report generation capability that supports after-the-fact investigations of security incidents. |
| [`V-222495`](rules/V-222495.md) | `APSC-DV-001210` | CAT II | The application must provide an audit reduction capability that does not alter original content or time ordering of audit records. |
| [`V-222496`](rules/V-222496.md) | `APSC-DV-001220` | CAT II | The application must provide a report generation capability that does not alter original content or time ordering of audit records. |
| [`V-222497`](rules/V-222497.md) | `APSC-DV-001250` | CAT II | The applications must use internal system clocks to generate time stamps for audit records. |
| [`V-222498`](rules/V-222498.md) | `APSC-DV-001260` | CAT II | The application must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT). |
| [`V-222499`](rules/V-222499.md) | `APSC-DV-001270` | CAT II | The application must record time stamps for audit records that meet a granularity of one second for a minimum degree of precision. |
| [`V-222500`](rules/V-222500.md) | `APSC-DV-001280` | CAT II | The application must protect audit information from any type of unauthorized read access. |
| [`V-222501`](rules/V-222501.md) | `APSC-DV-001290` | CAT II | The application must protect audit information from unauthorized modification. |
| [`V-222502`](rules/V-222502.md) | `APSC-DV-001300` | CAT II | The application must protect audit information from unauthorized deletion. |
| [`V-222503`](rules/V-222503.md) | `APSC-DV-001310` | CAT II | The application must protect audit tools from unauthorized access. |
| [`V-222504`](rules/V-222504.md) | `APSC-DV-001320` | CAT II | The application must protect audit tools from unauthorized modification. |
| [`V-222505`](rules/V-222505.md) | `APSC-DV-001330` | CAT II | The application must protect audit tools from unauthorized deletion. |
| [`V-222506`](rules/V-222506.md) | `APSC-DV-001340` | CAT II | The application must back up audit records at least every seven days onto a different system or system component than the system or component being audited. |
| [`V-222507`](rules/V-222507.md) | `APSC-DV-001350` | CAT II | The application must use cryptographic mechanisms to protect the integrity of audit information. |
| [`V-222508`](rules/V-222508.md) | `APSC-DV-001360` | CAT II | Application audit tools must be cryptographically hashed. |
| [`V-222509`](rules/V-222509.md) | `APSC-DV-001370` | CAT II | The integrity of the audit tools must be validated by checking the files for changes in the cryptographic hash value. |
| [`V-222510`](rules/V-222510.md) | `APSC-DV-001390` | CAT II | The application must prohibit user installation of software without explicit privileged status. |
| [`V-222511`](rules/V-222511.md) | `APSC-DV-001410` | CAT II | The application must enforce access restrictions associated with changes to application configuration. |
| [`V-222512`](rules/V-222512.md) | `APSC-DV-001420` | CAT II | The application must audit who makes configuration changes to the application. |
| [`V-222513`](rules/V-222513.md) | `APSC-DV-001430` | CAT II | The application must have the capability to prevent the installation of patches, service packs, or application components without verification the software component has been digitally signed using a certificate that is recognized and approved by the organization. |
| [`V-222514`](rules/V-222514.md) | `APSC-DV-001440` | CAT II | The applications must limit privileges to change the software resident within software libraries. |
| [`V-222515`](rules/V-222515.md) | `APSC-DV-001460` | CAT II | An application vulnerability assessment must be conducted. |
| [`V-222516`](rules/V-222516.md) | `APSC-DV-001480` | CAT II | The application must prevent program execution in accordance with organization-defined policies regarding software program usage and restrictions, and/or rules authorizing the terms and conditions of software program usage. |
| [`V-222517`](rules/V-222517.md) | `APSC-DV-001490` | CAT II | The application must employ a deny-all, permit-by-exception (whitelist) policy to allow the execution of authorized software programs. |
| [`V-222518`](rules/V-222518.md) | `APSC-DV-001500` | CAT II | The application must be configured to disable non-essential capabilities. |
| [`V-222519`](rules/V-222519.md) | `APSC-DV-001510` | CAT II | The application must be configured to use only functions, ports, and protocols permitted to it in the PPSM CAL. |
| [`V-222520`](rules/V-222520.md) | `APSC-DV-001520` | CAT II | The application must require users to reauthenticate when organization-defined circumstances or situations require reauthentication. |
| [`V-222521`](rules/V-222521.md) | `APSC-DV-001530` | CAT II | The application must require devices to reauthenticate when organization-defined circumstances or situations requiring reauthentication. |
| [`V-222522`](rules/V-222522.md) | `APSC-DV-001540` | CAT I | The application must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users). |
| [`V-222523`](rules/V-222523.md) | `APSC-DV-001550` | CAT II | The application must use multifactor (Alt. Token) authentication for network access to privileged accounts. |
| [`V-222524`](rules/V-222524.md) | `APSC-DV-001560` | CAT II | The application must accept Personal Identity Verification (PIV) credentials. |
| [`V-222525`](rules/V-222525.md) | `APSC-DV-001570` | CAT II | The application must electronically verify Personal Identity Verification (PIV) credentials. |
| [`V-222526`](rules/V-222526.md) | `APSC-DV-001580` | CAT II | The application must use multifactor (e.g., CAC, Alt. Token) authentication for network access to non-privileged accounts. |
| [`V-222527`](rules/V-222527.md) | `APSC-DV-001590` | CAT II | The application must use multifactor (Alt. Token) authentication for local access to privileged accounts. |
| [`V-222528`](rules/V-222528.md) | `APSC-DV-001600` | CAT II | The application must use multifactor (e.g., CAC, Alt. Token) authentication for local access to nonprivileged accounts. |
| [`V-222529`](rules/V-222529.md) | `APSC-DV-001610` | CAT II | The application must ensure users are authenticated with an individual authenticator prior to using a group authenticator. |
| [`V-222530`](rules/V-222530.md) | `APSC-DV-001620` | CAT II | The application must implement replay-resistant authentication mechanisms for network access to privileged accounts. |
| [`V-222531`](rules/V-222531.md) | `APSC-DV-001630` | CAT II | The application must implement replay-resistant authentication mechanisms for network access to nonprivileged accounts. |
| [`V-222532`](rules/V-222532.md) | `APSC-DV-001640` | CAT II | The application must utilize mutual authentication when endpoint device non-repudiation protections are required by DoW policy or by the data owner. |
| [`V-222533`](rules/V-222533.md) | `APSC-DV-001650` | CAT II | The application must authenticate all network connected endpoint devices before establishing any connection. |
| [`V-222534`](rules/V-222534.md) | `APSC-DV-001660` | CAT II | Service-Oriented Applications handling non-releasable data must authenticate endpoint devices via mutual SSL/TLS. |
| [`V-222535`](rules/V-222535.md) | `APSC-DV-001670` | CAT II | The application must disable device identifiers after 35 days of inactivity unless a cryptographic certificate is used for authentication. |
| [`V-222536`](rules/V-222536.md) | `APSC-DV-001680` | CAT I | The application must enforce a minimum 15-character password length. |
| [`V-222537`](rules/V-222537.md) | `APSC-DV-001690` | CAT II | The application must enforce password complexity by requiring that at least one uppercase character be used. |
| [`V-222538`](rules/V-222538.md) | `APSC-DV-001700` | CAT II | The application must enforce password complexity by requiring that at least one lowercase character be used. |
| [`V-222539`](rules/V-222539.md) | `APSC-DV-001710` | CAT II | The application must enforce password complexity by requiring that at least one numeric character be used. |
| [`V-222540`](rules/V-222540.md) | `APSC-DV-001720` | CAT II | The application must enforce password complexity by requiring that at least one special character be used. |
| [`V-222541`](rules/V-222541.md) | `APSC-DV-001730` | CAT II | The application must require the change of at least eight of the total number of characters when passwords are changed. |
| [`V-222542`](rules/V-222542.md) | `APSC-DV-001740` | CAT I | The application must only store cryptographic representations of passwords. |
| [`V-222543`](rules/V-222543.md) | `APSC-DV-001750` | CAT I | The application must transmit only cryptographically-protected passwords. |
| [`V-222544`](rules/V-222544.md) | `APSC-DV-001760` | CAT II | The application must enforce 24 hours/1 day as the minimum password lifetime. |
| [`V-222545`](rules/V-222545.md) | `APSC-DV-001770` | CAT II | The application must enforce a 180-day maximum password lifetime restriction. |
| [`V-222546`](rules/V-222546.md) | `APSC-DV-001780` | CAT II | The application must prohibit password reuse for a minimum of five generations. |
| [`V-222547`](rules/V-222547.md) | `APSC-DV-001790` | CAT II | The application must allow the use of a temporary password for system logons with an immediate change to a permanent password. |
| [`V-222548`](rules/V-222548.md) | `APSC-DV-001795` | CAT II | The application password must not be changeable by users other than the administrator or the user with which the password is associated. |
| [`V-222549`](rules/V-222549.md) | `APSC-DV-001800` | CAT II | The application must terminate existing user sessions upon account deletion. |
| [`V-222550`](rules/V-222550.md) | `APSC-DV-001810` | CAT I | The application, when utilizing PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor. |
| [`V-222551`](rules/V-222551.md) | `APSC-DV-001820` | CAT I | The application, when using PKI-based authentication, must enforce authorized access to the corresponding private key. |
| [`V-222552`](rules/V-222552.md) | `APSC-DV-001830` | CAT II | The application must map the authenticated identity to the individual user or group account for PKI-based authentication. |
| [`V-222553`](rules/V-222553.md) | `APSC-DV-001840` | CAT II | The application, for PKI-based authentication, must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network. |
| [`V-222554`](rules/V-222554.md) | `APSC-DV-001850` | CAT I | The application must not display passwords/PINs as clear text. |
| [`V-222555`](rules/V-222555.md) | `APSC-DV-001860` | CAT I | The application must use mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module. |
| [`V-222556`](rules/V-222556.md) | `APSC-DV-001870` | CAT II | The application must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users). |
| [`V-222557`](rules/V-222557.md) | `APSC-DV-001880` | CAT II | The application must accept Personal Identity Verification (PIV) credentials from other federal agencies. |
| [`V-222558`](rules/V-222558.md) | `APSC-DV-001890` | CAT II | The application must electronically verify Personal Identity Verification (PIV) credentials from other federal agencies. |
| [`V-222559`](rules/V-222559.md) | `APSC-DV-001900` | CAT II | The application must accept Federal Identity, Credential, and Access Management (FICAM)-approved third-party credentials. |
| [`V-222560`](rules/V-222560.md) | `APSC-DV-001910` | CAT II | The application must conform to Federal Identity, Credential, and Access Management (FICAM)-issued profiles. |
| [`V-222561`](rules/V-222561.md) | `APSC-DV-001930` | CAT II | Applications used for non-local maintenance sessions must audit non-local maintenance and diagnostic sessions for organization-defined auditable events. |
| [`V-222562`](rules/V-222562.md) | `APSC-DV-001940` | CAT II | Applications used for non-local maintenance sessions must implement cryptographic mechanisms to protect the integrity of non-local maintenance and diagnostic communications. |
| [`V-222563`](rules/V-222563.md) | `APSC-DV-001950` | CAT II | Applications used for non-local maintenance sessions must implement cryptographic mechanisms to protect the confidentiality of non-local maintenance and diagnostic communications. |
| [`V-222564`](rules/V-222564.md) | `APSC-DV-001960` | CAT II | Applications used for non-local maintenance sessions must verify remote disconnection at the termination of non-local maintenance and diagnostic sessions. |
| [`V-222565`](rules/V-222565.md) | `APSC-DV-001970` | CAT II | The application must employ strong authenticators in the establishment of non-local maintenance and diagnostic sessions. |
| [`V-222566`](rules/V-222566.md) | `APSC-DV-001980` | CAT II | The application must terminate all sessions and network connections when nonlocal maintenance is completed. |
| [`V-222567`](rules/V-222567.md) | `APSC-DV-001995` | CAT II | The application must not be vulnerable to race conditions. |
| [`V-222568`](rules/V-222568.md) | `APSC-DV-002000` | CAT II | The application must terminate all network connections associated with a communications session at the end of the session. |
| [`V-222570`](rules/V-222570.md) | `APSC-DV-002020` | CAT II | The application must utilize FIPS-validated cryptographic modules when signing application components. |
| [`V-222571`](rules/V-222571.md) | `APSC-DV-002030` | CAT II | The application must utilize FIPS-validated cryptographic modules when generating cryptographic hashes. |
| [`V-222572`](rules/V-222572.md) | `APSC-DV-002040` | CAT II | The application must utilize FIPS-validated cryptographic modules when protecting unclassified information that requires cryptographic protection. |
| [`V-222573`](rules/V-222573.md) | `APSC-DV-002050` | CAT II | Applications making SAML assertions must use FIPS-approved random numbers in the generation of SessionIndex in the SAML element AuthnStatement. |
| [`V-222574`](rules/V-222574.md) | `APSC-DV-002150` | CAT II | The application user interface must be either physically or logically separated from data storage and management interfaces. |
| [`V-222575`](rules/V-222575.md) | `APSC-DV-002210` | CAT II | The application must set the HTTPOnly flag on session cookies. |
| [`V-222576`](rules/V-222576.md) | `APSC-DV-002220` | CAT II | The application must set the secure flag on session cookies. |
| [`V-222577`](rules/V-222577.md) | `APSC-DV-002230` | CAT I | The application must not expose session IDs. |
| [`V-222578`](rules/V-222578.md) | `APSC-DV-002240` | CAT I | The application must destroy the session ID value and/or cookie on logoff or browser close. |
| [`V-222579`](rules/V-222579.md) | `APSC-DV-002250` | CAT II | Applications must use system-generated session identifiers that protect against session fixation. |
| [`V-222580`](rules/V-222580.md) | `APSC-DV-002260` | CAT II | Applications must validate session identifiers. |
| [`V-222581`](rules/V-222581.md) | `APSC-DV-002270` | CAT II | Applications must not use URL embedded session IDs. |
| [`V-222582`](rules/V-222582.md) | `APSC-DV-002280` | CAT II | The application must not re-use or recycle session IDs. |
| [`V-222583`](rules/V-222583.md) | `APSC-DV-002290` | CAT II | The application must generate a unique session identifier using a FIPS 140-2/140-3 approved random number generator. |
| [`V-222584`](rules/V-222584.md) | `APSC-DV-002300` | CAT II | The application must only allow the use of DoW-approved certificate authorities for verification of the establishment of protected sessions. |
| [`V-222585`](rules/V-222585.md) | `APSC-DV-002310` | CAT I | The application must fail to a secure state if system initialization fails, shutdown fails, or aborts fail. |
| [`V-222586`](rules/V-222586.md) | `APSC-DV-002320` | CAT II | In the event of a system failure, applications must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes. |
| [`V-222587`](rules/V-222587.md) | `APSC-DV-002330` | CAT II | The application must protect the confidentiality and integrity of stored information when required by DoW policy or the information owner. |
| [`V-222588`](rules/V-222588.md) | `APSC-DV-002340` | CAT I | The application must implement approved cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest on organization-defined information system components. |
| [`V-222589`](rules/V-222589.md) | `APSC-DV-002350` | CAT I | The application must use appropriate cryptography in order to protect stored DoW information when required by the information owner or DoW policy. |
| [`V-222590`](rules/V-222590.md) | `APSC-DV-002360` | CAT II | The application must isolate security functions from non-security functions. |
| [`V-222591`](rules/V-222591.md) | `APSC-DV-002370` | CAT II | The application must maintain a separate execution domain for each executing process. |
| [`V-222592`](rules/V-222592.md) | `APSC-DV-002380` | CAT II | Applications must prevent unauthorized and unintended information transfer via shared system resources. |
| [`V-222593`](rules/V-222593.md) | `APSC-DV-002390` | CAT II | XML-based applications must mitigate DoS attacks by using XML filters, parser options, or gateways. |
| [`V-222594`](rules/V-222594.md) | `APSC-DV-002400` | CAT II | The application must restrict the ability to launch Denial of Service (DoS) attacks against itself or other information systems. |
| [`V-222595`](rules/V-222595.md) | `APSC-DV-002410` | CAT II | The web service design must include redundancy mechanisms when used with high-availability systems. |
| [`V-222596`](rules/V-222596.md) | `APSC-DV-002440` | CAT I | The application must protect the confidentiality and integrity of transmitted information. |
| [`V-222597`](rules/V-222597.md) | `APSC-DV-002450` | CAT II | The application must implement cryptographic mechanisms to prevent unauthorized disclosure of information and/or detect changes to information during transmission unless otherwise protected by alternative physical safeguards, such as, at a minimum, a Protected Distribution System (PDS). |
| [`V-222598`](rules/V-222598.md) | `APSC-DV-002460` | CAT II | The application must maintain the confidentiality and integrity of information during preparation for transmission. |
| [`V-222599`](rules/V-222599.md) | `APSC-DV-002470` | CAT II | The application must maintain the confidentiality and integrity of information during reception. |
| [`V-222600`](rules/V-222600.md) | `APSC-DV-002480` | CAT II | The application must not disclose unnecessary information to users. |
| [`V-222601`](rules/V-222601.md) | `APSC-DV-002485` | CAT I | The application must not store sensitive information in hidden fields. |
| [`V-222602`](rules/V-222602.md) | `APSC-DV-002490` | CAT I | The application must protect from Cross-Site Scripting (XSS) vulnerabilities. |
| [`V-222603`](rules/V-222603.md) | `APSC-DV-002500` | CAT II | The application must protect from Cross-Site Request Forgery (CSRF) vulnerabilities. |
| [`V-222604`](rules/V-222604.md) | `APSC-DV-002510` | CAT I | The application must protect from command injection. |
| [`V-222605`](rules/V-222605.md) | `APSC-DV-002520` | CAT II | The application must protect from canonical representation vulnerabilities. |
| [`V-222606`](rules/V-222606.md) | `APSC-DV-002530` | CAT II | The application must validate all input. |
| [`V-222607`](rules/V-222607.md) | `APSC-DV-002540` | CAT I | The application must not be vulnerable to SQL Injection. |
| [`V-222608`](rules/V-222608.md) | `APSC-DV-002550` | CAT I | The application must not be vulnerable to XML-oriented attacks. |
| [`V-222609`](rules/V-222609.md) | `APSC-DV-002560` | CAT I | The application must not be subject to input handling vulnerabilities. |
| [`V-222610`](rules/V-222610.md) | `APSC-DV-002570` | CAT II | The application must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries. |
| [`V-222611`](rules/V-222611.md) | `APSC-DV-002580` | CAT II | The application must reveal error messages only to the ISSO, ISSM, or SA. |
| [`V-222612`](rules/V-222612.md) | `APSC-DV-002590` | CAT I | The application must not be vulnerable to overflow attacks. |
| [`V-222613`](rules/V-222613.md) | `APSC-DV-002610` | CAT II | The application must remove organization-defined software components after updated versions have been installed. |
| [`V-222614`](rules/V-222614.md) | `APSC-DV-002630` | CAT II | Security-relevant software updates and patches must be kept up to date. |
| [`V-222615`](rules/V-222615.md) | `APSC-DV-002760` | CAT II | The application performing organization-defined security functions must verify correct operation of security functions. |
| [`V-222616`](rules/V-222616.md) | `APSC-DV-002770` | CAT II | The application must perform verification of the correct operation of security functions: upon system startup and/or restart; upon command by a user with privileged access; and/or every 30 days. |
| [`V-222617`](rules/V-222617.md) | `APSC-DV-002780` | CAT III | The application must notify the ISSO and ISSM of failed security verification tests. |
| [`V-222618`](rules/V-222618.md) | `APSC-DV-002870` | CAT II | Unsigned Category 1A mobile code must not be used in the application in accordance with DoW policy. |
| [`V-222619`](rules/V-222619.md) | `APSC-DV-002880` | CAT II | The ISSO must ensure an account management process is implemented, verifying only authorized users can gain access to the application, and individual accounts designated as inactive, suspended, or terminated are promptly removed. |
| [`V-222620`](rules/V-222620.md) | `APSC-DV-002890` | CAT I | Application web servers must be on a separate network segment from the application and database servers if it is a tiered application operating in the DoW DMZ. |
| [`V-222621`](rules/V-222621.md) | `APSC-DV-002900` | CAT II | The ISSO must ensure application audit trails are retained for at least 30 months (12 months active + 18 months cold storage) for applications without SAMI data and five years for applications including SAMI data. |
| [`V-222622`](rules/V-222622.md) | `APSC-DV-002910` | CAT II | The ISSO must review audit trails periodically based on system documentation recommendations or immediately upon system security events. |
| [`V-222623`](rules/V-222623.md) | `APSC-DV-002920` | CAT II | The ISSO must report all suspected violations of IA policies in accordance with DoW information system IA procedures. |
| [`V-222624`](rules/V-222624.md) | `APSC-DV-002930` | CAT II | The ISSO must ensure active vulnerability testing is performed. |
| [`V-222625`](rules/V-222625.md) | `APSC-DV-002950` | CAT II | Execution flow diagrams and design documents must be created to show how deadlock and recursion issues in web services are being mitigated. |
| [`V-222626`](rules/V-222626.md) | `APSC-DV-002960` | CAT II | The designer must ensure the application does not store configuration and control files in the same directory as user data. |
| [`V-222627`](rules/V-222627.md) | `APSC-DV-002970` | CAT II | The ISSO must ensure if a DoW STIG or NSA guide is not available, a third-party product will be configured by following available guidance. |
| [`V-222628`](rules/V-222628.md) | `APSC-DV-002980` | CAT II | New IP addresses, data services, and associated ports used by the application must be submitted to the appropriate approving authority for the organization, which in turn will be submitted through the DoW Ports, Protocols, and Services Management (DoW PPSM) |
| [`V-222629`](rules/V-222629.md) | `APSC-DV-002990` | CAT II | The application must be registered with the DoW Ports and Protocols Database. |
| [`V-222630`](rules/V-222630.md) | `APSC-DV-002995` | CAT II | The Configuration Management (CM) repository must be properly patched and STIG compliant. |
| [`V-222631`](rules/V-222631.md) | `APSC-DV-003000` | CAT II | Access privileges to the Configuration Management (CM) repository must be reviewed every three months. |
| [`V-222632`](rules/V-222632.md) | `APSC-DV-003010` | CAT II | A Software Configuration Management (SCM) plan describing the configuration control and change management process of application objects developed by the organization and the roles and responsibilities of the organization must be created and maintained. |
| [`V-222633`](rules/V-222633.md) | `APSC-DV-003020` | CAT II | A Configuration Control Board (CCB) that meets at least every release cycle, for managing the Configuration Management (CM) process must be established. |
| [`V-222634`](rules/V-222634.md) | `APSC-DV-003030` | CAT II | The application services and interfaces must be compatible with and ready for IPv6 networks. |
| [`V-222635`](rules/V-222635.md) | `APSC-DV-003040` | CAT II | The application must not be hosted on a general purpose machine if the application is designated as critical or high availability by the ISSO. |
| [`V-222636`](rules/V-222636.md) | `APSC-DV-003050` | CAT II | A contingency plan must exist in accordance with DoW policy based on the application's availability requirements. |
| [`V-222637`](rules/V-222637.md) | `APSC-DV-003060` | CAT II | Recovery procedures and technical system features must exist so recovery is performed in a secure and verifiable manner. The ISSO will document circumstances inhibiting a trusted recovery. |
| [`V-222638`](rules/V-222638.md) | `APSC-DV-003070` | CAT II | Data backup must be performed at required intervals in accordance with DoW policy. |
| [`V-222639`](rules/V-222639.md) | `APSC-DV-003080` | CAT II | Back-up copies of the application software or source code must be stored in a fire-rated container or stored separately (offsite). |
| [`V-222640`](rules/V-222640.md) | `APSC-DV-003090` | CAT II | Procedures must be in place to assure the appropriate physical and technical protection of the backup and restoration of the application. |
| [`V-222641`](rules/V-222641.md) | `APSC-DV-003100` | CAT II | The application must use encryption to implement key exchange and authenticate endpoints prior to establishing a communication channel for key exchange. |
| [`V-222642`](rules/V-222642.md) | `APSC-DV-003110` | CAT I | The application must not contain embedded authentication data. |
| [`V-222643`](rules/V-222643.md) | `APSC-DV-003120` | CAT I | The application must have the capability to mark sensitive/classified output when required. |
| [`V-222644`](rules/V-222644.md) | `APSC-DV-003130` | CAT III | Prior to each release of the application, updates to system, or applying patches; tests plans and procedures must be created and executed. |
| [`V-222645`](rules/V-222645.md) | `APSC-DV-003140` | CAT II | Application files must be cryptographically hashed prior to deploying to DoW operational networks. |
| [`V-222646`](rules/V-222646.md) | `APSC-DV-003150` | CAT II | At least one tester must be designated to test for security flaws in addition to functional testing. |
| [`V-222647`](rules/V-222647.md) | `APSC-DV-003160` | CAT III | Test procedures must be created and at least annually executed to ensure system initialization, shutdown, and aborts are configured to verify the system remains in a secure state. |
| [`V-222648`](rules/V-222648.md) | `APSC-DV-003170` | CAT II | An application code review must be performed on the application. |
| [`V-222649`](rules/V-222649.md) | `APSC-DV-003180` | CAT III | Code coverage statistics must be maintained for each release of the application. |
| [`V-222650`](rules/V-222650.md) | `APSC-DV-003190` | CAT II | Flaws found during a code review must be tracked in a defect tracking system. |
| [`V-222651`](rules/V-222651.md) | `APSC-DV-003200` | CAT II | The changes to the application must be assessed for IA and accreditation impact prior to implementation. |
| [`V-222652`](rules/V-222652.md) | `APSC-DV-003210` | CAT II | Security flaws must be fixed or addressed in the project plan. |
| [`V-222653`](rules/V-222653.md) | `APSC-DV-003215` | CAT III | The application development team must follow a set of coding standards. |
| [`V-222654`](rules/V-222654.md) | `APSC-DV-003220` | CAT III | The designer must create and update the Design Document for each release of the application. |
| [`V-222655`](rules/V-222655.md) | `APSC-DV-003230` | CAT II | Threat models must be documented and reviewed for each application release and updated as required by design and functionality changes or when new threats are discovered. |
| [`V-222656`](rules/V-222656.md) | `APSC-DV-003235` | CAT II | The application must not be subject to error handling vulnerabilities. |
| [`V-222657`](rules/V-222657.md) | `APSC-DV-003236` | CAT II | The application development team must provide an application incident response plan. |
| [`V-222658`](rules/V-222658.md) | `APSC-DV-003240` | CAT I | All products must be supported by the vendor or the development team. |
| [`V-222659`](rules/V-222659.md) | `APSC-DV-003250` | CAT I | The application must be decommissioned when maintenance or support is no longer available. |
| [`V-222660`](rules/V-222660.md) | `APSC-DV-003260` | CAT III | Procedures must be in place to notify users when an application is decommissioned. |
| [`V-222661`](rules/V-222661.md) | `APSC-DV-003270` | CAT II | Unnecessary built-in application accounts must be disabled. |
| [`V-222662`](rules/V-222662.md) | `APSC-DV-003280` | CAT I | Default passwords must be changed. |
| [`V-222663`](rules/V-222663.md) | `APSC-DV-003285` | CAT II | An Application Configuration Guide must be created and included with the application. |
| [`V-222664`](rules/V-222664.md) | `APSC-DV-003290` | CAT II | If the application contains classified data, a Security Classification Guide must exist containing data elements and their classification. |
| [`V-222665`](rules/V-222665.md) | `APSC-DV-003300` | CAT II | The designer must ensure uncategorized or emerging mobile code is not used in applications. |
| [`V-222666`](rules/V-222666.md) | `APSC-DV-003310` | CAT II | Production database exports must have database administration credentials and sensitive data removed before releasing the export. |
| [`V-222667`](rules/V-222667.md) | `APSC-DV-003320` | CAT II | Protections against DoS attacks must be implemented. |
| [`V-222668`](rules/V-222668.md) | `APSC-DV-003330` | CAT II | The system must alert an administrator when low resource conditions are encountered. |
| [`V-222669`](rules/V-222669.md) | `APSC-DV-003340` | CAT III | At least one application administrator must be registered to receive update notifications, or security alerts, when automated alerts are available. |
| [`V-222670`](rules/V-222670.md) | `APSC-DV-003345` | CAT III | The application must provide notifications or alerts when product update and security related patches are available. |
| [`V-222671`](rules/V-222671.md) | `APSC-DV-003350` | CAT II | Connections between the DoW enclave and the Internet or other public or commercial wide area networks must require a DMZ. |
| [`V-222672`](rules/V-222672.md) | `APSC-DV-003360` | CAT III | The application must generate audit records when concurrent logons from different workstations occur. |
| [`V-222673`](rules/V-222673.md) | `APSC-DV-003400` | CAT II | The Program Manager must verify all levels of program management, designers, developers, and testers receive annual security training pertaining to their job function. |
| [`V-265634`](rules/V-265634.md) | `APSC-DV-002010` | CAT II | The application must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards. |
