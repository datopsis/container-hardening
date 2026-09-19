# General Purpose Operating System Security Requirements Guide

Release: 3 Benchmark Date: 28 Oct 2025. Accepted 2025-09-22.

| | |
| --- | --- |
| Benchmark | `General_Purpose_Operating_System` |
| Rules | **203** |
| CAT I | 20 |
| CAT II | 173 |
| CAT III | 10 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-203591`](rules/V-203591.md) | `SRG-OS-000001-GPOS-00001` | CAT II | The operating system must provide automated mechanisms for supporting account management functions. |
| [`V-203592`](rules/V-203592.md) | `SRG-OS-000002-GPOS-00002` | CAT II | The operating system must automatically remove or disable temporary user accounts after 72 hours. |
| [`V-203593`](rules/V-203593.md) | `SRG-OS-000004-GPOS-00004` | CAT II | The operating system must audit all account creations. |
| [`V-203594`](rules/V-203594.md) | `SRG-OS-000021-GPOS-00005` | CAT II | The operating system must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period. |
| [`V-203595`](rules/V-203595.md) | `SRG-OS-000023-GPOS-00006` | CAT II | The operating system must display the Standard Mandatory DoD Notice and Consent Banner before granting local or remote access to the system. |
| [`V-203596`](rules/V-203596.md) | `SRG-OS-000024-GPOS-00007` | CAT II | The operating system must display the Standard Mandatory DoD Notice and Consent Banner until users acknowledge the usage conditions and take explicit actions to log on for further access. |
| [`V-203597`](rules/V-203597.md) | `SRG-OS-000027-GPOS-00008` | CAT III | The operating system must limit the number of concurrent sessions to ten for all accounts and/or account types. |
| [`V-203598`](rules/V-203598.md) | `SRG-OS-000028-GPOS-00009` | CAT II | The operating system must retain a users session lock until that user reestablishes access using established identification and authentication procedures. |
| [`V-203599`](rules/V-203599.md) | `SRG-OS-000029-GPOS-00010` | CAT II | The operating system must initiate a session lock after a 15-minute period of inactivity for all connection types. |
| [`V-203600`](rules/V-203600.md) | `SRG-OS-000030-GPOS-00011` | CAT II | The operating system must provide the capability for users to directly initiate a session lock for all connection types. |
| [`V-203601`](rules/V-203601.md) | `SRG-OS-000031-GPOS-00012` | CAT II | The operating system must conceal, via the session lock, information previously visible on the display with a publicly viewable image. |
| [`V-203602`](rules/V-203602.md) | `SRG-OS-000032-GPOS-00013` | CAT II | The operating system must monitor remote access methods. |
| [`V-203603`](rules/V-203603.md) | `SRG-OS-000033-GPOS-00014` | CAT I | The operating system must implement DoD-approved encryption to protect the confidentiality of remote access sessions. |
| [`V-203604`](rules/V-203604.md) | `SRG-OS-000037-GPOS-00015` | CAT II | The operating system must produce audit records containing information to establish what type of events occurred. |
| [`V-203605`](rules/V-203605.md) | `SRG-OS-000038-GPOS-00016` | CAT II | The operating system must produce audit records containing information to establish when (date and time) the events occurred. |
| [`V-203606`](rules/V-203606.md) | `SRG-OS-000039-GPOS-00017` | CAT II | The operating system must produce audit records containing information to establish where the events occurred. |
| [`V-203607`](rules/V-203607.md) | `SRG-OS-000040-GPOS-00018` | CAT II | The operating system must produce audit records containing information to establish the source of the events. |
| [`V-203608`](rules/V-203608.md) | `SRG-OS-000041-GPOS-00019` | CAT II | The operating system must produce audit records containing information to establish the outcome of the events. |
| [`V-203609`](rules/V-203609.md) | `SRG-OS-000042-GPOS-00020` | CAT II | The operating system must generate audit records containing the full-text recording of privileged commands. |
| [`V-203610`](rules/V-203610.md) | `SRG-OS-000042-GPOS-00021` | CAT II | The operating system must produce audit records containing the individual identities of group account users. |
| [`V-203611`](rules/V-203611.md) | `SRG-OS-000046-GPOS-00022` | CAT II | The operating system must alert the ISSO and SA (at a minimum) in the event of an audit processing failure. |
| [`V-203613`](rules/V-203613.md) | `SRG-OS-000051-GPOS-00024` | CAT II | The operating system must provide the capability to centrally review and analyze audit records from multiple components within the system. |
| [`V-203614`](rules/V-203614.md) | `SRG-OS-000054-GPOS-00025` | CAT II | The operating system must provide the capability to filter audit records for events of interest based upon all audit fields within audit records. |
| [`V-203615`](rules/V-203615.md) | `SRG-OS-000055-GPOS-00026` | CAT II | The operating system must use internal system clocks to generate time stamps for audit records. |
| [`V-203616`](rules/V-203616.md) | `SRG-OS-000057-GPOS-00027` | CAT II | The operating system must protect audit information from unauthorized read access. |
| [`V-203617`](rules/V-203617.md) | `SRG-OS-000058-GPOS-00028` | CAT II | The operating system must protect audit information from unauthorized modification. |
| [`V-203618`](rules/V-203618.md) | `SRG-OS-000059-GPOS-00029` | CAT II | The operating system must protect audit information from unauthorized deletion. |
| [`V-203619`](rules/V-203619.md) | `SRG-OS-000062-GPOS-00031` | CAT II | The operating system must provide audit record generation capability for DoD-defined auditable events for all operating system components. |
| [`V-203620`](rules/V-203620.md) | `SRG-OS-000063-GPOS-00032` | CAT II | The operating system must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited. |
| [`V-203621`](rules/V-203621.md) | `SRG-OS-000064-GPOS-00033` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to access privileges occur. |
| [`V-203622`](rules/V-203622.md) | `SRG-OS-000066-GPOS-00034` | CAT II | The operating system, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor. |
| [`V-203623`](rules/V-203623.md) | `SRG-OS-000067-GPOS-00035` | CAT II | The operating system, for PKI-based authentication, must enforce authorized access to the corresponding private key. |
| [`V-203624`](rules/V-203624.md) | `SRG-OS-000068-GPOS-00036` | CAT II | The operating system must map the authenticated identity to the user or group account for PKI-based authentication. |
| [`V-203625`](rules/V-203625.md) | `SRG-OS-000069-GPOS-00037` | CAT II | The operating system must enforce password complexity by requiring that at least one uppercase character be used. |
| [`V-203626`](rules/V-203626.md) | `SRG-OS-000070-GPOS-00038` | CAT II | The operating system must enforce password complexity by requiring that at least one lowercase character be used. |
| [`V-203627`](rules/V-203627.md) | `SRG-OS-000071-GPOS-00039` | CAT II | The operating system must enforce password complexity by requiring that at least one numeric character be used. |
| [`V-203628`](rules/V-203628.md) | `SRG-OS-000072-GPOS-00040` | CAT II | The operating system must require the change of at least 50 percent of the total number of characters when passwords are changed. |
| [`V-203629`](rules/V-203629.md) | `SRG-OS-000073-GPOS-00041` | CAT I | The operating system must store only encrypted representations of passwords. |
| [`V-203630`](rules/V-203630.md) | `SRG-OS-000074-GPOS-00042` | CAT I | The operating system must transmit only encrypted representations of passwords. |
| [`V-203631`](rules/V-203631.md) | `SRG-OS-000075-GPOS-00043` | CAT II | Operating systems must enforce 24 hours/1 day as the minimum password lifetime. |
| [`V-203632`](rules/V-203632.md) | `SRG-OS-000076-GPOS-00044` | CAT II | Operating systems must enforce a 60-day maximum password lifetime restriction. |
| [`V-203634`](rules/V-203634.md) | `SRG-OS-000078-GPOS-00046` | CAT II | The operating system must enforce a minimum 15-character password length. |
| [`V-203635`](rules/V-203635.md) | `SRG-OS-000079-GPOS-00047` | CAT II | The operating system must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals. |
| [`V-203636`](rules/V-203636.md) | `SRG-OS-000080-GPOS-00048` | CAT II | The operating system must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. |
| [`V-203637`](rules/V-203637.md) | `SRG-OS-000095-GPOS-00049` | CAT II | The operating system must be configured to disable non-essential capabilities. |
| [`V-203638`](rules/V-203638.md) | `SRG-OS-000096-GPOS-00050` | CAT II | The operating system must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. |
| [`V-203639`](rules/V-203639.md) | `SRG-OS-000104-GPOS-00051` | CAT II | The operating system must uniquely identify and must authenticate organizational users (or processes acting on behalf of organizational users). |
| [`V-203640`](rules/V-203640.md) | `SRG-OS-000105-GPOS-00052` | CAT II | The operating system must use multifactor authentication for network access to privileged accounts. |
| [`V-203641`](rules/V-203641.md) | `SRG-OS-000106-GPOS-00053` | CAT II | The operating system must use multifactor authentication for network access to non-privileged accounts. |
| [`V-203642`](rules/V-203642.md) | `SRG-OS-000107-GPOS-00054` | CAT II | The operating system must use multifactor authentication for local access to privileged accounts. |
| [`V-203643`](rules/V-203643.md) | `SRG-OS-000108-GPOS-00055` | CAT II | The operating system must use multifactor authentication for local access to nonprivileged accounts. |
| [`V-203644`](rules/V-203644.md) | `SRG-OS-000109-GPOS-00056` | CAT II | The operating system must require individuals to be authenticated with an individual authenticator prior to using a group authenticator. |
| [`V-203645`](rules/V-203645.md) | `SRG-OS-000112-GPOS-00057` | CAT II | The operating system must implement replay-resistant authentication mechanisms for network access to privileged accounts. |
| [`V-203646`](rules/V-203646.md) | `SRG-OS-000113-GPOS-00058` | CAT II | The operating system must implement replay-resistant authentication mechanisms for network access to nonprivileged accounts. |
| [`V-203647`](rules/V-203647.md) | `SRG-OS-000114-GPOS-00059` | CAT II | The operating system must uniquely identify peripherals before establishing a connection. |
| [`V-203648`](rules/V-203648.md) | `SRG-OS-000118-GPOS-00060` | CAT II | The operating system must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity. |
| [`V-203649`](rules/V-203649.md) | `SRG-OS-000120-GPOS-00061` | CAT II | The operating system must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module. |
| [`V-203650`](rules/V-203650.md) | `SRG-OS-000121-GPOS-00062` | CAT II | The operating system must uniquely identify and must authenticate non-organizational users (or processes acting on behalf of non-organizational users). |
| [`V-203651`](rules/V-203651.md) | `SRG-OS-000122-GPOS-00063` | CAT II | The operating system must provide an audit reduction capability that supports on-demand reporting requirements. |
| [`V-203652`](rules/V-203652.md) | `SRG-OS-000123-GPOS-00064` | CAT II | The information system must automatically remove or disable emergency accounts after the crisis is resolved or 72 hours. |
| [`V-203653`](rules/V-203653.md) | `SRG-OS-000125-GPOS-00065` | CAT I | The operating system must employ strong authenticators in the establishment of nonlocal maintenance and diagnostic sessions. |
| [`V-203655`](rules/V-203655.md) | `SRG-OS-000132-GPOS-00067` | CAT II | The operating system must separate user functionality (including user interface services) from operating system management functionality. |
| [`V-203656`](rules/V-203656.md) | `SRG-OS-000134-GPOS-00068` | CAT II | The operating system must isolate security functions from nonsecurity functions. |
| [`V-203657`](rules/V-203657.md) | `SRG-OS-000138-GPOS-00069` | CAT II | Operating systems must prevent unauthorized and unintended information transfer via shared system resources. |
| [`V-203658`](rules/V-203658.md) | `SRG-OS-000142-GPOS-00071` | CAT II | The operating system must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of Denial of Service (DoS) attacks. |
| [`V-203659`](rules/V-203659.md) | `SRG-OS-000163-GPOS-00072` | CAT II | The operating system must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity, except to fulfill documented and validated mission requirements. |
| [`V-203660`](rules/V-203660.md) | `SRG-OS-000184-GPOS-00078` | CAT II | The operating system must fail to a secure state if system initialization fails, shutdown fails, or aborts fail. |
| [`V-203661`](rules/V-203661.md) | `SRG-OS-000185-GPOS-00079` | CAT II | The operating system must protect the confidentiality and integrity of all information at rest. |
| [`V-203663`](rules/V-203663.md) | `SRG-OS-000205-GPOS-00083` | CAT II | The operating system must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries. |
| [`V-203664`](rules/V-203664.md) | `SRG-OS-000206-GPOS-00084` | CAT II | The operating system must reveal error messages only to authorized users. |
| [`V-203665`](rules/V-203665.md) | `SRG-OS-000228-GPOS-00088` | CAT II | Any publically accessible connection to the operating system must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system. |
| [`V-203666`](rules/V-203666.md) | `SRG-OS-000239-GPOS-00089` | CAT II | The operating system must audit all account modifications. |
| [`V-203667`](rules/V-203667.md) | `SRG-OS-000240-GPOS-00090` | CAT II | The operating system must audit all account disabling actions. |
| [`V-203668`](rules/V-203668.md) | `SRG-OS-000241-GPOS-00091` | CAT II | The operating system must audit all account removal actions. |
| [`V-203669`](rules/V-203669.md) | `SRG-OS-000250-GPOS-00093` | CAT I | The operating system must implement cryptography to protect the integrity of remote access sessions. |
| [`V-203670`](rules/V-203670.md) | `SRG-OS-000254-GPOS-00095` | CAT II | The operating system must initiate session audits at system start-up. |
| [`V-203671`](rules/V-203671.md) | `SRG-OS-000255-GPOS-00096` | CAT II | The operating system must produce audit records containing information to establish the identity of any individual or process associated with the event. |
| [`V-203672`](rules/V-203672.md) | `SRG-OS-000256-GPOS-00097` | CAT II | The operating system must protect audit tools from unauthorized access. |
| [`V-203673`](rules/V-203673.md) | `SRG-OS-000257-GPOS-00098` | CAT II | The operating system must protect audit tools from unauthorized modification. |
| [`V-203674`](rules/V-203674.md) | `SRG-OS-000258-GPOS-00099` | CAT II | The operating system must protect audit tools from unauthorized deletion. |
| [`V-203675`](rules/V-203675.md) | `SRG-OS-000259-GPOS-00100` | CAT II | The operating system must limit privileges to change software resident within software libraries. |
| [`V-203676`](rules/V-203676.md) | `SRG-OS-000266-GPOS-00101` | CAT II | The operating system must enforce password complexity by requiring that at least one special character be used. |
| [`V-203677`](rules/V-203677.md) | `SRG-OS-000269-GPOS-00103` | CAT II | In the event of a system failure, the operating system must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes. |
| [`V-203678`](rules/V-203678.md) | `SRG-OS-000274-GPOS-00104` | CAT II | The operating system must notify system administrators and ISSOs when accounts are created. |
| [`V-203679`](rules/V-203679.md) | `SRG-OS-000275-GPOS-00105` | CAT II | The operating system must notify system administrators and ISSOs when accounts are modified. |
| [`V-203680`](rules/V-203680.md) | `SRG-OS-000276-GPOS-00106` | CAT II | The operating system must notify system administrators and ISSOs when accounts are disabled. |
| [`V-203681`](rules/V-203681.md) | `SRG-OS-000277-GPOS-00107` | CAT II | The operating system must notify system administrators and ISSOs when accounts are removed. |
| [`V-203682`](rules/V-203682.md) | `SRG-OS-000278-GPOS-00108` | CAT I | The operating system must use cryptographic mechanisms to protect the integrity of audit tools. |
| [`V-203683`](rules/V-203683.md) | `SRG-OS-000279-GPOS-00109` | CAT II | The operating system must automatically terminate a user session after inactivity time-outs have expired or at shutdown. |
| [`V-203684`](rules/V-203684.md) | `SRG-OS-000280-GPOS-00110` | CAT II | The operating system must provide a logoff capability for user-initiated communications sessions when requiring user access authentication. |
| [`V-203685`](rules/V-203685.md) | `SRG-OS-000281-GPOS-00111` | CAT II | The operating system must display an explicit logoff message to users indicating the reliable termination of authenticated communications sessions. |
| [`V-203686`](rules/V-203686.md) | `SRG-OS-000297-GPOS-00115` | CAT II | The operating system must control remote access methods. |
| [`V-203687`](rules/V-203687.md) | `SRG-OS-000298-GPOS-00116` | CAT II | The operating system must provide the capability to immediately disconnect or disable remote access to the operating system. |
| [`V-203688`](rules/V-203688.md) | `SRG-OS-000299-GPOS-00117` | CAT II | The operating system must protect wireless access to and from the system using encryption. |
| [`V-203689`](rules/V-203689.md) | `SRG-OS-000300-GPOS-00118` | CAT II | The operating system must protect wireless access to the system using authentication of users and/or devices. |
| [`V-203690`](rules/V-203690.md) | `SRG-OS-000303-GPOS-00120` | CAT II | The operating system must audit all account enabling actions. |
| [`V-203691`](rules/V-203691.md) | `SRG-OS-000304-GPOS-00121` | CAT II | The operating system must notify system administrators (SAs) and information system security officers (ISSOs) of account enabling actions. |
| [`V-203692`](rules/V-203692.md) | `SRG-OS-000312-GPOS-00122` | CAT II | The operating system must allow operating system admins to pass information to any other operating system admin or user. |
| [`V-203693`](rules/V-203693.md) | `SRG-OS-000312-GPOS-00123` | CAT II | The operating system must allow operating system admins to grant their privileges to other operating system admins. |
| [`V-203694`](rules/V-203694.md) | `SRG-OS-000312-GPOS-00124` | CAT II | The operating system must allow operating system admins to change security attributes on users, the operating system, or the operating systems components. |
| [`V-203695`](rules/V-203695.md) | `SRG-OS-000324-GPOS-00125` | CAT I | The operating system must prevent nonprivileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures. |
| [`V-203696`](rules/V-203696.md) | `SRG-OS-000326-GPOS-00126` | CAT II | The operating system must prevent all software from executing at higher privilege levels than users executing the software. |
| [`V-203697`](rules/V-203697.md) | `SRG-OS-000327-GPOS-00127` | CAT II | The operating system must audit the execution of privileged functions. |
| [`V-203698`](rules/V-203698.md) | `SRG-OS-000329-GPOS-00128` | CAT II | The operating system must automatically lock an account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes occur. |
| [`V-203699`](rules/V-203699.md) | `SRG-OS-000337-GPOS-00129` | CAT II | The operating system must provide the capability for assigned IMOs/ISSOs or designated SAs to change the auditing to be performed on all operating system components, based on all selectable event criteria in near real time. |
| [`V-203700`](rules/V-203700.md) | `SRG-OS-000341-GPOS-00132` | CAT III | The operating system must allocate audit record storage capacity to store at least one week's worth of audit records, when audit records are not immediately sent to a central audit record storage facility. |
| [`V-203701`](rules/V-203701.md) | `SRG-OS-000342-GPOS-00133` | CAT III | The operating system must offload audit records onto a different system or media from the system being audited. |
| [`V-203702`](rules/V-203702.md) | `SRG-OS-000343-GPOS-00134` | CAT III | The operating system must immediately notify the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity. |
| [`V-203703`](rules/V-203703.md) | `SRG-OS-000344-GPOS-00135` | CAT II | The operating system must provide an immediate real-time alert to the SA and ISSO, at a minimum, of all audit failure events requiring real-time alerts. |
| [`V-203704`](rules/V-203704.md) | `SRG-OS-000348-GPOS-00136` | CAT III | The operating system must provide an audit reduction capability that supports on-demand audit review and analysis. |
| [`V-203705`](rules/V-203705.md) | `SRG-OS-000349-GPOS-00137` | CAT III | The operating system must provide an audit reduction capability that supports after-the-fact investigations of security incidents. |
| [`V-203706`](rules/V-203706.md) | `SRG-OS-000350-GPOS-00138` | CAT III | The operating system must provide a report generation capability that supports on-demand audit review and analysis. |
| [`V-203707`](rules/V-203707.md) | `SRG-OS-000351-GPOS-00139` | CAT III | The operating system must provide a report generation capability that supports on-demand reporting requirements. |
| [`V-203708`](rules/V-203708.md) | `SRG-OS-000352-GPOS-00140` | CAT III | The operating system must provide a report generation capability that supports after-the-fact investigations of security incidents. |
| [`V-203709`](rules/V-203709.md) | `SRG-OS-000353-GPOS-00141` | CAT II | The operating system must not alter original content or time ordering of audit records when it provides an audit reduction capability. |
| [`V-203710`](rules/V-203710.md) | `SRG-OS-000354-GPOS-00142` | CAT II | The operating system must not alter original content or time ordering of audit records when it provides a report generation capability. |
| [`V-203711`](rules/V-203711.md) | `SRG-OS-000355-GPOS-00143` | CAT II | The operating system must, for networked systems, compare internal information system clocks at least every 24 hours with an authoritative time source. |
| [`V-203712`](rules/V-203712.md) | `SRG-OS-000356-GPOS-00144` | CAT II | The operating system must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second. |
| [`V-203713`](rules/V-203713.md) | `SRG-OS-000358-GPOS-00145` | CAT II | The operating system must record time stamps for audit records that meet a minimum granularity of one second for a minimum degree of precision. |
| [`V-203714`](rules/V-203714.md) | `SRG-OS-000359-GPOS-00146` | CAT III | The operating system must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT). |
| [`V-203715`](rules/V-203715.md) | `SRG-OS-000360-GPOS-00147` | CAT II | The operating system must enforce dual authorization for movement and/or deletion of all audit information, when such movement or deletion is not part of an authorized automatic process. |
| [`V-203716`](rules/V-203716.md) | `SRG-OS-000362-GPOS-00149` | CAT II | The operating system must prohibit user installation of system software without explicit privileged status. |
| [`V-203717`](rules/V-203717.md) | `SRG-OS-000363-GPOS-00150` | CAT II | The operating system must notify designated personnel if baseline configurations are changed in an unauthorized manner. |
| [`V-203718`](rules/V-203718.md) | `SRG-OS-000364-GPOS-00151` | CAT II | The operating system must enforce access restrictions. |
| [`V-203719`](rules/V-203719.md) | `SRG-OS-000365-GPOS-00152` | CAT II | The operating system must audit the enforcement actions used to restrict access associated with changes to the system. |
| [`V-203720`](rules/V-203720.md) | `SRG-OS-000366-GPOS-00153` | CAT I | The operating system must prevent the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization. |
| [`V-203721`](rules/V-203721.md) | `SRG-OS-000368-GPOS-00154` | CAT II | The operating system must prevent program execution in accordance with local policies regarding software program usage and restrictions and/or rules authorizing the terms and conditions of software program usage. |
| [`V-203722`](rules/V-203722.md) | `SRG-OS-000370-GPOS-00155` | CAT II | The operating system must employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs. |
| [`V-203723`](rules/V-203723.md) | `SRG-OS-000373-GPOS-00156` | CAT II | The operating system must require users to reauthenticate for privilege escalation. |
| [`V-203724`](rules/V-203724.md) | `SRG-OS-000373-GPOS-00157` | CAT II | The operating system must require users to reauthenticate when changing roles. |
| [`V-203725`](rules/V-203725.md) | `SRG-OS-000373-GPOS-00158` | CAT II | The operating system must require users to reauthenticate when changing authenticators. |
| [`V-203727`](rules/V-203727.md) | `SRG-OS-000375-GPOS-00160` | CAT II | The operating system must implement multifactor authentication for remote access to privileged accounts in such a way that one of the factors is provided by a device separate from the system gaining access. |
| [`V-203728`](rules/V-203728.md) | `SRG-OS-000376-GPOS-00161` | CAT II | The operating system must accept Personal Identity Verification (PIV) credentials. |
| [`V-203729`](rules/V-203729.md) | `SRG-OS-000377-GPOS-00162` | CAT II | The operating system must electronically verify Personal Identity Verification (PIV) credentials. |
| [`V-203730`](rules/V-203730.md) | `SRG-OS-000378-GPOS-00163` | CAT II | The operating system must authenticate peripherals before establishing a connection. |
| [`V-203731`](rules/V-203731.md) | `SRG-OS-000379-GPOS-00164` | CAT II | The operating system must authenticate all endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based. |
| [`V-203733`](rules/V-203733.md) | `SRG-OS-000383-GPOS-00166` | CAT II | The operating system must prohibit the use of cached authenticators after one day. |
| [`V-203734`](rules/V-203734.md) | `SRG-OS-000384-GPOS-00167` | CAT II | The operating system, for PKI-based authentication, must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network. |
| [`V-203735`](rules/V-203735.md) | `SRG-OS-000392-GPOS-00172` | CAT II | The operating system must audit all activities performed during nonlocal maintenance and diagnostic sessions. |
| [`V-203736`](rules/V-203736.md) | `SRG-OS-000393-GPOS-00173` | CAT I | The operating system must implement cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications, when used for nonlocal maintenance sessions. |
| [`V-203737`](rules/V-203737.md) | `SRG-OS-000394-GPOS-00174` | CAT I | The operating system must implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications, when used for nonlocal maintenance sessions. |
| [`V-203738`](rules/V-203738.md) | `SRG-OS-000395-GPOS-00175` | CAT II | The operating system must verify remote disconnection at the termination of nonlocal maintenance and diagnostic sessions, when used for nonlocal maintenance sessions. |
| [`V-203739`](rules/V-203739.md) | `SRG-OS-000396-GPOS-00176` | CAT I | The operating system must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards. |
| [`V-203744`](rules/V-203744.md) | `SRG-OS-000403-GPOS-00182` | CAT II | The operating system must only allow the use of DoD PKI-established certificate authorities for authentication in the establishment of protected sessions to the operating system. |
| [`V-203745`](rules/V-203745.md) | `SRG-OS-000404-GPOS-00183` | CAT I | The operating system must implement cryptographic mechanisms to prevent unauthorized modification of all information at rest on all operating system components. |
| [`V-203746`](rules/V-203746.md) | `SRG-OS-000405-GPOS-00184` | CAT I | The operating system must implement cryptographic mechanisms to prevent unauthorized disclosure of all information at rest on all operating system components. |
| [`V-203747`](rules/V-203747.md) | `SRG-OS-000420-GPOS-00186` | CAT II | The operating system must protect against or limit the effects of Denial of Service (DoS) attacks by ensuring the operating system is implementing rate-limiting measures on impacted network interfaces. |
| [`V-203748`](rules/V-203748.md) | `SRG-OS-000423-GPOS-00187` | CAT I | The operating system must protect the confidentiality and integrity of transmitted information. |
| [`V-203749`](rules/V-203749.md) | `SRG-OS-000424-GPOS-00188` | CAT I | The operating system must implement cryptographic mechanisms to prevent unauthorized disclosure of information and/or detect changes to information during transmission unless otherwise protected by alternative physical safeguards, such as, at a minimum, a Protected Distribution System (PDS). |
| [`V-203750`](rules/V-203750.md) | `SRG-OS-000425-GPOS-00189` | CAT II | The operating system must maintain the confidentiality and integrity of information during preparation for transmission. |
| [`V-203751`](rules/V-203751.md) | `SRG-OS-000426-GPOS-00190` | CAT II | The operating system must maintain the confidentiality and integrity of information during reception. |
| [`V-203752`](rules/V-203752.md) | `SRG-OS-000432-GPOS-00191` | CAT II | The operating system must behave in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received. |
| [`V-203753`](rules/V-203753.md) | `SRG-OS-000433-GPOS-00192` | CAT II | The operating system must implement non-executable data to protect its memory from unauthorized code execution. |
| [`V-203754`](rules/V-203754.md) | `SRG-OS-000433-GPOS-00193` | CAT II | The operating system must implement address space layout randomization to protect its memory from unauthorized code execution. |
| [`V-203755`](rules/V-203755.md) | `SRG-OS-000437-GPOS-00194` | CAT II | The operating system must remove all software components after updated versions have been installed. |
| [`V-203756`](rules/V-203756.md) | `SRG-OS-000445-GPOS-00199` | CAT II | The operating system must verify correct operation of all security functions. |
| [`V-203757`](rules/V-203757.md) | `SRG-OS-000446-GPOS-00200` | CAT II | The operating system must perform verification of the correct operation of security functions: upon system start-up and/or restart; upon command by a user with privileged access; and/or every 30 days. |
| [`V-203758`](rules/V-203758.md) | `SRG-OS-000447-GPOS-00201` | CAT II | The operating system must shut down the information system, restart the information system, and/or notify the system administrator when anomalies in the operation of any security functions are discovered. |
| [`V-203759`](rules/V-203759.md) | `SRG-OS-000458-GPOS-00203` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to access security objects occur. |
| [`V-203760`](rules/V-203760.md) | `SRG-OS-000461-GPOS-00205` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur. |
| [`V-203761`](rules/V-203761.md) | `SRG-OS-000462-GPOS-00206` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to modify privileges occur. |
| [`V-203762`](rules/V-203762.md) | `SRG-OS-000463-GPOS-00207` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to modify security objects occur. |
| [`V-203763`](rules/V-203763.md) | `SRG-OS-000465-GPOS-00209` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur. |
| [`V-203764`](rules/V-203764.md) | `SRG-OS-000466-GPOS-00210` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to delete privileges occur. |
| [`V-203765`](rules/V-203765.md) | `SRG-OS-000467-GPOS-00211` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to delete security levels occur. |
| [`V-203766`](rules/V-203766.md) | `SRG-OS-000468-GPOS-00212` | CAT II | The operating system must generate audit records when successful/unsuccessful attempts to delete security objects occur. |
| [`V-203767`](rules/V-203767.md) | `SRG-OS-000470-GPOS-00214` | CAT II | The operating system must generate audit records when successful/unsuccessful logon attempts occur. |
| [`V-203768`](rules/V-203768.md) | `SRG-OS-000471-GPOS-00215` | CAT II | The operating system must generate audit records for privileged activities or other system-level access. |
| [`V-203769`](rules/V-203769.md) | `SRG-OS-000471-GPOS-00216` | CAT II | The audit system must be configured to audit the loading and unloading of dynamic kernel modules. |
| [`V-203770`](rules/V-203770.md) | `SRG-OS-000472-GPOS-00217` | CAT II | The operating system must generate audit records showing starting and ending time for user access to the system. |
| [`V-203771`](rules/V-203771.md) | `SRG-OS-000473-GPOS-00218` | CAT II | The operating system must generate audit records when concurrent logons to the same account occur from different sources. |
| [`V-203772`](rules/V-203772.md) | `SRG-OS-000474-GPOS-00219` | CAT II | The operating system must generate audit records when successful/unsuccessful accesses to objects occur. |
| [`V-203773`](rules/V-203773.md) | `SRG-OS-000475-GPOS-00220` | CAT II | The operating system must generate audit records for all direct access to the information system. |
| [`V-203774`](rules/V-203774.md) | `SRG-OS-000476-GPOS-00221` | CAT II | The operating system must generate audit records for all account creations, modifications, disabling, and termination events. |
| [`V-203775`](rules/V-203775.md) | `SRG-OS-000477-GPOS-00222` | CAT II | The operating system must generate audit records for all kernel module load, unload, and restart actions, and also for all program initiations. |
| [`V-203776`](rules/V-203776.md) | `SRG-OS-000478-GPOS-00223` | CAT I | The operating system must implement NIST FIPS-validated cryptography for the following: to provision digital signatures, to generate cryptographic hashes, and to protect unclassified information requiring confidentiality and cryptographic protection in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards. |
| [`V-203777`](rules/V-203777.md) | `SRG-OS-000479-GPOS-00224` | CAT II | The operating system must, at a minimum, off-load audit data from interconnected systems in real time and off-load audit data from standalone systems weekly. |
| [`V-203778`](rules/V-203778.md) | `SRG-OS-000480-GPOS-00225` | CAT II | The operating system must prevent the use of dictionary words for passwords. |
| [`V-203779`](rules/V-203779.md) | `SRG-OS-000480-GPOS-00226` | CAT II | The operating system must enforce a delay of at least 4 seconds between logon prompts following a failed logon attempt. |
| [`V-203780`](rules/V-203780.md) | `SRG-OS-000480-GPOS-00227` | CAT II | The operating system must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs. |
| [`V-203781`](rules/V-203781.md) | `SRG-OS-000480-GPOS-00228` | CAT II | The operating system must define default permissions for all authenticated users in such a way that the user can only read and modify their own files. |
| [`V-203782`](rules/V-203782.md) | `SRG-OS-000480-GPOS-00229` | CAT I | The operating system must not allow an unattended or automatic logon to the system. |
| [`V-203783`](rules/V-203783.md) | `SRG-OS-000480-GPOS-00230` | CAT II | The operating system must limit the ability of non-privileged users to grant other users direct access to the contents of their home directories/folders. |
| [`V-203784`](rules/V-203784.md) | `SRG-OS-000480-GPOS-00232` | CAT II | The operating system must enable an application firewall, if available. |
| [`V-252688`](rules/V-252688.md) | `SRG-OS-000481-GPOS-00481` | CAT I | The operating system must protect the confidentiality and integrity of communications with wireless peripherals. |
| [`V-259333`](rules/V-259333.md) | `SRG-OS-000439-GPOS-00195` | CAT I | The operating system must install security-relevant software updates within 30 days unless the time period is directed by an authoritative source (e.g., IAVM, CTOs, DTMs, STIGs). |
| [`V-263650`](rules/V-263650.md) | `SRG-OS-000590-GPOS-00110` | CAT II | The operating system must disable accounts when the accounts are no longer associated to a user. |
| [`V-263651`](rules/V-263651.md) | `SRG-OS-000690-GPOS-00140` | CAT II | The operating system must prohibit the use or connection of unauthorized hardware components. |
| [`V-263652`](rules/V-263652.md) | `SRG-OS-000705-GPOS-00150` | CAT II | The operating system must implement multifactor authentication for local, network, and/or remote access to privileged accounts and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements. |
| [`V-263653`](rules/V-263653.md) | `SRG-OS-000710-GPOS-00160` | CAT II | The operating system must, for password-based authentication, verify when users create or update passwords the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a). |
| [`V-263654`](rules/V-263654.md) | `SRG-OS-000720-GPOS-00170` | CAT II | The operating system must for password-based authentication, require immediate selection of a new password upon account recovery. |
| [`V-263655`](rules/V-263655.md) | `SRG-OS-000725-GPOS-00180` | CAT II | The operating system must for password-based authentication, allow user selection of long passwords and passphrases, including spaces and all printable characters. |
| [`V-263656`](rules/V-263656.md) | `SRG-OS-000730-GPOS-00190` | CAT II | The operating system must, for password-based authentication, employ automated tools to assist the user in selecting strong password authenticators. |
| [`V-263657`](rules/V-263657.md) | `SRG-OS-000745-GPOS-00210` | CAT II | The operating system must accept only external credentials that are NIST-compliant. |
| [`V-263658`](rules/V-263658.md) | `SRG-OS-000755-GPOS-00220` | CAT II | The operating system must monitor the use of maintenance tools that execute with increased privilege. |
| [`V-263659`](rules/V-263659.md) | `SRG-OS-000775-GPOS-00230` | CAT II | The operating system must include only approved trust anchors in trust stores or certificate stores managed by the organization. |
| [`V-263660`](rules/V-263660.md) | `SRG-OS-000780-GPOS-00240` | CAT II | The operating system must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store. |
| [`V-263661`](rules/V-263661.md) | `SRG-OS-000785-GPOS-00250` | CAT II | The operating system must synchronize system clocks within and between systems or system components. |
| [`V-278973`](rules/V-278973.md) | `SRG-OS-000132-GPOS-00067` | CAT II | The operating system must separate user functionality (including user interface services) from operating system management functionality. |
| [`V-278974`](rules/V-278974.md) | `SRG-OS-000313-GPOS-00124` | CAT II | The operating system must enforce a role-based access control (RBAC) policy over defined subjects and objects. |
| [`V-278975`](rules/V-278975.md) | `SRG-OS-000550-GPOS-00100` | CAT II | The operating system must use a FIPS-validated cryptographic module to provision digital signatures. |
| [`V-278976`](rules/V-278976.md) | `SRG-OS-000835-GPOS-00305` | CAT II | The operating system must enforce attribute-based access control policy over defined subjects and objects based upon organization-defined attributes to assume access permissions. |
| [`V-278977`](rules/V-278977.md) | `SRG-OS-000830-GPOS-00300` | CAT I | The operating system must be a version supported by the vendor. |
