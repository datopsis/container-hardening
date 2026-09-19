# Container Platform Security Requirements Guide

Release: 4 Benchmark Date: 28 Oct 2025. Accepted 2025-09-10.

| | |
| --- | --- |
| Benchmark | `Container_Platform_SRG` |
| Rules | **188** |
| CAT I | 8 |
| CAT II | 177 |
| CAT III | 3 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-233015`](rules/V-233015.md) | `SRG-APP-000014-CTR-000035` | CAT II | The container platform must use TLS 1.2 or greater for secure container image transport from trusted sources. |
| [`V-233016`](rules/V-233016.md) | `SRG-APP-000014-CTR-000040` | CAT II | The container platform must use TLS 1.2 or greater for secure communication. |
| [`V-233019`](rules/V-233019.md) | `SRG-APP-000023-CTR-000055` | CAT II | The container platform must use a centralized user management solution to support account management functions. |
| [`V-233020`](rules/V-233020.md) | `SRG-APP-000024-CTR-000060` | CAT II | The container platform must automatically remove or disable temporary user accounts after 72 hours. |
| [`V-233021`](rules/V-233021.md) | `SRG-APP-000025-CTR-000065` | CAT II | The container platform must automatically disable accounts after a 35-day period of account inactivity. |
| [`V-233022`](rules/V-233022.md) | `SRG-APP-000026-CTR-000070` | CAT II | The container platform must automatically audit account creation. |
| [`V-233023`](rules/V-233023.md) | `SRG-APP-000027-CTR-000075` | CAT II | The container platform must automatically audit account modification. |
| [`V-233024`](rules/V-233024.md) | `SRG-APP-000028-CTR-000080` | CAT II | The container platform must automatically audit account-disabling actions. |
| [`V-233025`](rules/V-233025.md) | `SRG-APP-000029-CTR-000085` | CAT II | The container platform must automatically audit account removal actions. |
| [`V-233026`](rules/V-233026.md) | `SRG-APP-000033-CTR-000090` | CAT II | Least privilege access and need-to-know must be required to access the container platform registry. |
| [`V-233027`](rules/V-233027.md) | `SRG-APP-000033-CTR-000095` | CAT II | Least privilege access and need-to-know must be required to access the container platform runtime. |
| [`V-233028`](rules/V-233028.md) | `SRG-APP-000033-CTR-000100` | CAT II | Least privilege access and need-to-know must be required to access the container platform keystore. |
| [`V-233029`](rules/V-233029.md) | `SRG-APP-000038-CTR-000105` | CAT II | The container platform must enforce approved authorizations for controlling the flow of information within the container platform based on organization-defined information flow control policies. |
| [`V-233030`](rules/V-233030.md) | `SRG-APP-000039-CTR-000110` | CAT II | The container platform must enforce approved authorizations for controlling the flow of information between interconnected systems and services based on organization-defined information flow control policies. |
| [`V-233031`](rules/V-233031.md) | `SRG-APP-000065-CTR-000115` | CAT II | The container platform must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period. |
| [`V-233032`](rules/V-233032.md) | `SRG-APP-000068-CTR-000120` | CAT III | The container platform must display the Standard Mandatory DoD Notice and Consent Banner before granting access to platform components. |
| [`V-233033`](rules/V-233033.md) | `SRG-APP-000069-CTR-000125` | CAT III | The container platform must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until users acknowledge the usage and conditions and take explicit actions to log on for further access. |
| [`V-233038`](rules/V-233038.md) | `SRG-APP-000089-CTR-000150` | CAT II | The container platform must generate audit records for all DoD-defined auditable events within all components in the platform. |
| [`V-233039`](rules/V-233039.md) | `SRG-APP-000090-CTR-000155` | CAT II | The container platform must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited. |
| [`V-233040`](rules/V-233040.md) | `SRG-APP-000091-CTR-000160` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to access privileges occur. |
| [`V-233041`](rules/V-233041.md) | `SRG-APP-000092-CTR-000165` | CAT II | The container platform must initiate session auditing upon startup. |
| [`V-233042`](rules/V-233042.md) | `SRG-APP-000095-CTR-000170` | CAT II | All audit records must identify what type of event has occurred within the container platform. |
| [`V-233043`](rules/V-233043.md) | `SRG-APP-000096-CTR-000175` | CAT II | The container platform audit records must have a date and time association with all events. |
| [`V-233044`](rules/V-233044.md) | `SRG-APP-000097-CTR-000180` | CAT II | All audit records must identify where in the container platform the event occurred. |
| [`V-233045`](rules/V-233045.md) | `SRG-APP-000098-CTR-000185` | CAT II | All audit records must identify the source of the event within the container platform. |
| [`V-233046`](rules/V-233046.md) | `SRG-APP-000099-CTR-000190` | CAT II | All audit records must generate the event results within the container platform. |
| [`V-233047`](rules/V-233047.md) | `SRG-APP-000100-CTR-000195` | CAT II | All audit records must identify any users associated with the event within the container platform. |
| [`V-233048`](rules/V-233048.md) | `SRG-APP-000100-CTR-000200` | CAT II | All audit records must identify any containers associated with the event within the container platform. |
| [`V-233049`](rules/V-233049.md) | `SRG-APP-000101-CTR-000205` | CAT II | The container platform must generate audit records containing the full-text recording of privileged commands or the individual identities of group account users. |
| [`V-233052`](rules/V-233052.md) | `SRG-APP-000111-CTR-000220` | CAT II | The container platform components must provide the ability to send audit logs to a central enterprise repository for review and analysis. |
| [`V-233055`](rules/V-233055.md) | `SRG-APP-000116-CTR-000235` | CAT II | The container platform must use internal system clocks to generate audit record time stamps. |
| [`V-233056`](rules/V-233056.md) | `SRG-APP-000118-CTR-000240` | CAT II | The container platform must protect audit information from any type of unauthorized read access. |
| [`V-233057`](rules/V-233057.md) | `SRG-APP-000119-CTR-000245` | CAT II | The container platform must protect audit information from unauthorized modification. |
| [`V-233058`](rules/V-233058.md) | `SRG-APP-000120-CTR-000250` | CAT II | The container platform must protect audit information from unauthorized deletion. |
| [`V-233059`](rules/V-233059.md) | `SRG-APP-000121-CTR-000255` | CAT II | The container platform must protect audit tools from unauthorized access. |
| [`V-233060`](rules/V-233060.md) | `SRG-APP-000122-CTR-000260` | CAT II | The container platform must protect audit tools from unauthorized modification. |
| [`V-233061`](rules/V-233061.md) | `SRG-APP-000123-CTR-000265` | CAT II | The container platform must protect audit tools from unauthorized deletion. |
| [`V-233063`](rules/V-233063.md) | `SRG-APP-000126-CTR-000275` | CAT II | The container platform must use FIPS validated cryptographic mechanisms to protect the integrity of log information. |
| [`V-233064`](rules/V-233064.md) | `SRG-APP-000131-CTR-000280` | CAT II | The container platform must be built from verified packages. |
| [`V-233065`](rules/V-233065.md) | `SRG-APP-000131-CTR-000285` | CAT II | The container platform must verify container images. |
| [`V-233066`](rules/V-233066.md) | `SRG-APP-000133-CTR-000290` | CAT II | The container platform must limit privileges to the container platform registry. |
| [`V-233067`](rules/V-233067.md) | `SRG-APP-000133-CTR-000295` | CAT II | The container platform must limit privileges to the container platform runtime. |
| [`V-233068`](rules/V-233068.md) | `SRG-APP-000133-CTR-000300` | CAT II | The container platform must limit privileges to the container platform keystore. |
| [`V-233069`](rules/V-233069.md) | `SRG-APP-000133-CTR-000305` | CAT II | Configuration files for the container platform must be protected. |
| [`V-233070`](rules/V-233070.md) | `SRG-APP-000133-CTR-000310` | CAT II | Authentication files for the container platform must be protected. |
| [`V-233071`](rules/V-233071.md) | `SRG-APP-000141-CTR-000315` | CAT II | The container platform must be configured with only essential configurations. |
| [`V-233072`](rules/V-233072.md) | `SRG-APP-000141-CTR-000320` | CAT II | The container platform registry must contain only container images for those capabilities being offered by the container platform. |
| [`V-233073`](rules/V-233073.md) | `SRG-APP-000142-CTR-000325` | CAT II | The container platform runtime must enforce ports, protocols, and services that adhere to the PPSM CAL. |
| [`V-233074`](rules/V-233074.md) | `SRG-APP-000142-CTR-000330` | CAT II | The container platform runtime must enforce the use of ports that are non-privileged. |
| [`V-233075`](rules/V-233075.md) | `SRG-APP-000148-CTR-000335` | CAT II | The container platform must uniquely identify and authenticate users. |
| [`V-233076`](rules/V-233076.md) | `SRG-APP-000148-CTR-000340` | CAT II | The container platform application program interface (API) must uniquely identify and authenticate users. |
| [`V-233077`](rules/V-233077.md) | `SRG-APP-000148-CTR-000345` | CAT II | The container platform must uniquely identify and authenticate processes acting on behalf of the users. |
| [`V-233078`](rules/V-233078.md) | `SRG-APP-000148-CTR-000350` | CAT II | The container platform application program interface (API) must uniquely identify and authenticate processes acting on behalf of the users. |
| [`V-233079`](rules/V-233079.md) | `SRG-APP-000149-CTR-000355` | CAT II | The container platform must use multifactor authentication for network access to privileged accounts. |
| [`V-233080`](rules/V-233080.md) | `SRG-APP-000150-CTR-000360` | CAT II | The container platform must use multifactor authentication for network access to non-privileged accounts. |
| [`V-233081`](rules/V-233081.md) | `SRG-APP-000151-CTR-000365` | CAT II | The container platform must use multifactor authentication for local access to privileged accounts. |
| [`V-233082`](rules/V-233082.md) | `SRG-APP-000152-CTR-000370` | CAT II | The container platform must use multifactor authentication for local access to nonprivileged accounts. |
| [`V-233083`](rules/V-233083.md) | `SRG-APP-000153-CTR-000375` | CAT II | The container platform must ensure users are authenticated with an individual authenticator prior to using a group authenticator. |
| [`V-233084`](rules/V-233084.md) | `SRG-APP-000156-CTR-000380` | CAT II | The container platform must use FIPS-validated SHA-1 or higher hash function to provide replay-resistant authentication mechanisms for network access to privileged accounts. |
| [`V-233085`](rules/V-233085.md) | `SRG-APP-000157-CTR-000385` | CAT II | The container platform must implement replay-resistant authentication mechanisms for network access to nonprivileged accounts. |
| [`V-233086`](rules/V-233086.md) | `SRG-APP-000158-CTR-000390` | CAT II | The container platform must uniquely identify all network-connected nodes before establishing any connection. |
| [`V-233087`](rules/V-233087.md) | `SRG-APP-000163-CTR-000395` | CAT II | The container platform must disable identifiers (individuals, groups, roles, and devices) after 35 days of inactivity. |
| [`V-233088`](rules/V-233088.md) | `SRG-APP-000164-CTR-000400` | CAT II | The container platform must enforce a minimum 15-character password length. |
| [`V-233090`](rules/V-233090.md) | `SRG-APP-000166-CTR-000410` | CAT II | The container platform must enforce password complexity by requiring that at least one uppercase character be used. |
| [`V-233091`](rules/V-233091.md) | `SRG-APP-000167-CTR-000415` | CAT II | The container platform must enforce password complexity by requiring that at least one lowercase character be used. |
| [`V-233092`](rules/V-233092.md) | `SRG-APP-000168-CTR-000420` | CAT II | The container platform must enforce password complexity by requiring that at least one numeric character be used. |
| [`V-233093`](rules/V-233093.md) | `SRG-APP-000169-CTR-000425` | CAT II | The container platform must enforce password complexity by requiring that at least one special character be used. |
| [`V-233094`](rules/V-233094.md) | `SRG-APP-000170-CTR-000430` | CAT II | The container platform must require the change of at least eight of the total number of characters when passwords are changed. |
| [`V-233095`](rules/V-233095.md) | `SRG-APP-000171-CTR-000435` | CAT II | For container platform using password authentication, the application must store only cryptographic representations of passwords. |
| [`V-233096`](rules/V-233096.md) | `SRG-APP-000172-CTR-000440` | CAT I | For accounts using password authentication, the container platform must use FIPS-validated SHA-2 or later protocol to protect the integrity of the password authentication process. |
| [`V-233097`](rules/V-233097.md) | `SRG-APP-000173-CTR-000445` | CAT II | The container platform must enforce 24 hours (one day) as the minimum password lifetime. |
| [`V-233098`](rules/V-233098.md) | `SRG-APP-000174-CTR-000450` | CAT II | The container platform must enforce a 60-day maximum password lifetime restriction. |
| [`V-233101`](rules/V-233101.md) | `SRG-APP-000177-CTR-000465` | CAT II | The container platform must map the authenticated identity to the individual user or group account for PKI-based authentication. |
| [`V-233102`](rules/V-233102.md) | `SRG-APP-000178-CTR-000470` | CAT II | The container platform must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals. |
| [`V-233105`](rules/V-233105.md) | `SRG-APP-000181-CTR-000485` | CAT II | The container platform must provide an audit reduction capability that supports on-demand reporting requirements. |
| [`V-233106`](rules/V-233106.md) | `SRG-APP-000185-CTR-000490` | CAT II | The container platform must employ strong authenticators in the establishment of non-local maintenance and diagnostic sessions. |
| [`V-233108`](rules/V-233108.md) | `SRG-APP-000190-CTR-000500` | CAT II | The application must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity. |
| [`V-233114`](rules/V-233114.md) | `SRG-APP-000211-CTR-000530` | CAT II | The container platform must separate user functionality (including user interface services) from information system management functionality. |
| [`V-233118`](rules/V-233118.md) | `SRG-APP-000219-CTR-000550` | CAT I | The container platform must protect authenticity of communications sessions with the use of FIPS-validated 140-2 or 140-3 security requirements for cryptographic modules. |
| [`V-233122`](rules/V-233122.md) | `SRG-APP-000225-CTR-000570` | CAT II | The container platform runtime must fail to a secure state if system initialization fails, shutdown fails, or aborts fail. |
| [`V-233123`](rules/V-233123.md) | `SRG-APP-000226-CTR-000575` | CAT II | The container platform must preserve any information necessary to determine the cause of the disruption or failure. |
| [`V-233125`](rules/V-233125.md) | `SRG-APP-000233-CTR-000585` | CAT II | The container platform runtime must isolate security functions from non-security functions. |
| [`V-233126`](rules/V-233126.md) | `SRG-APP-000234-CTR-000590` | CAT II | The container platform must never automatically remove or disable emergency accounts. |
| [`V-233127`](rules/V-233127.md) | `SRG-APP-000243-CTR-000595` | CAT II | The container platform must prohibit containers from accessing privileged resources. |
| [`V-233128`](rules/V-233128.md) | `SRG-APP-000243-CTR-000600` | CAT II | The container platform must prevent unauthorized and unintended information transfer via shared system resources. |
| [`V-233129`](rules/V-233129.md) | `SRG-APP-000246-CTR-000605` | CAT II | The container platform must restrict individuals' ability to launch organizationally defined denial-of-service (DoS) attacks against other information systems. |
| [`V-233133`](rules/V-233133.md) | `SRG-APP-000266-CTR-000625` | CAT II | The container platform must generate error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries. |
| [`V-233142`](rules/V-233142.md) | `SRG-APP-000290-CTR-000670` | CAT II | The container platform must use cryptographic mechanisms to protect the integrity of audit tools. |
| [`V-233143`](rules/V-233143.md) | `SRG-APP-000291-CTR-000675` | CAT II | The container platform must notify system administrators (SAs) and the information system security officer (ISSO) when accounts are created. |
| [`V-233144`](rules/V-233144.md) | `SRG-APP-000292-CTR-000680` | CAT II | The container platform must notify system administrators (SAs) and the information system security officer (ISSO) when accounts are modified. |
| [`V-233145`](rules/V-233145.md) | `SRG-APP-000293-CTR-000685` | CAT II | The container platform must notify system administrators and ISSO for account disabling actions. |
| [`V-233146`](rules/V-233146.md) | `SRG-APP-000294-CTR-000690` | CAT II | The container platform must notify system administrators and ISSO for account removal actions. |
| [`V-233149`](rules/V-233149.md) | `SRG-APP-000297-CTR-000705` | CAT III | Access to the container platform must display an explicit logout message to user indicating the reliable termination of authenticated communication sessions. |
| [`V-233155`](rules/V-233155.md) | `SRG-APP-000317-CTR-000735` | CAT II | The container platform must terminate shared/group account credentials when members leave the group. |
| [`V-233157`](rules/V-233157.md) | `SRG-APP-000319-CTR-000745` | CAT II | The container platform must automatically audit account-enabling actions. |
| [`V-233158`](rules/V-233158.md) | `SRG-APP-000320-CTR-000750` | CAT II | The container platform must notify the system administrator (SA) and information system security officer (ISSO) of account enabling actions. |
| [`V-233162`](rules/V-233162.md) | `SRG-APP-000340-CTR-000770` | CAT II | The container platform must prevent non-privileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures. |
| [`V-233163`](rules/V-233163.md) | `SRG-APP-000342-CTR-000775` | CAT II | Container images instantiated by the container platform must execute using least privileges. |
| [`V-233164`](rules/V-233164.md) | `SRG-APP-000343-CTR-000780` | CAT II | The container platform must audit the execution of privileged functions. |
| [`V-233165`](rules/V-233165.md) | `SRG-APP-000345-CTR-000785` | CAT II | The container platform must automatically lock an account until the locked account is released by an administrator when three unsuccessful login attempts in 15 minutes are exceeded. |
| [`V-233166`](rules/V-233166.md) | `SRG-APP-000516-CTR-000790` | CAT II | The container platform must provide the configuration for organization-identified individuals or roles to change the auditing to be performed on all components, based on all selectable event criteria within organization-defined time thresholds. |
| [`V-233168`](rules/V-233168.md) | `SRG-APP-000357-CTR-000800` | CAT II | The container platform must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements. |
| [`V-233169`](rules/V-233169.md) | `SRG-APP-000358-CTR-000805` | CAT II | Audit records must be stored at a secondary location. |
| [`V-233170`](rules/V-233170.md) | `SRG-APP-000359-CTR-000810` | CAT II | The container platform must provide an immediate warning to the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75 percent of repository maximum audit record storage capacity. |
| [`V-233171`](rules/V-233171.md) | `SRG-APP-000360-CTR-000815` | CAT II | The container platform must provide an immediate real-time alert to the SA and ISSO, at a minimum, of all audit failure events requiring real-time alerts. |
| [`V-233181`](rules/V-233181.md) | `SRG-APP-000374-CTR-000865` | CAT II | All audit records must use UTC or GMT time stamps. |
| [`V-233182`](rules/V-233182.md) | `SRG-APP-000375-CTR-000870` | CAT II | The container platform must record time stamps for audit records that meet a granularity of one second for a minimum degree of precision. |
| [`V-233184`](rules/V-233184.md) | `SRG-APP-000378-CTR-000880` | CAT II | The container platform must prohibit the installation of patches and updates without explicit privileged status. |
| [`V-233185`](rules/V-233185.md) | `SRG-APP-000378-CTR-000885` | CAT I | The container platform runtime must prohibit the instantiation of container images without explicit privileged status. |
| [`V-233186`](rules/V-233186.md) | `SRG-APP-000378-CTR-000890` | CAT II | The container platform registry must prohibit installation or modification of container images without explicit privileged status. |
| [`V-233188`](rules/V-233188.md) | `SRG-APP-000380-CTR-000900` | CAT II | The container platform must enforce access restrictions for container platform configuration changes. |
| [`V-233189`](rules/V-233189.md) | `SRG-APP-000381-CTR-000905` | CAT II | The container platform must enforce access restrictions and support auditing of the enforcement actions. |
| [`V-233190`](rules/V-233190.md) | `SRG-APP-000383-CTR-000910` | CAT II | All non-essential, unnecessary, and unsecure DoD ports, protocols, and services must be disabled in the container platform. |
| [`V-233191`](rules/V-233191.md) | `SRG-APP-000384-CTR-000915` | CAT II | The container platform must prevent component execution in accordance with organization-defined policies regarding software program usage and restrictions, and/or rules authorizing the terms and conditions of software program usage. |
| [`V-233192`](rules/V-233192.md) | `SRG-APP-000386-CTR-000920` | CAT II | The container platform registry must employ a deny-all, permit-by-exception (whitelist) policy to allow only authorized container images in the container platform. |
| [`V-233193`](rules/V-233193.md) | `SRG-APP-000389-CTR-000925` | CAT II | The container platform must require users to reauthenticate when organization-defined circumstances or situations require reauthentication. |
| [`V-233195`](rules/V-233195.md) | `SRG-APP-000391-CTR-000935` | CAT II | The container platform must be configured to use multi-factor authentication for user authentication. |
| [`V-233200`](rules/V-233200.md) | `SRG-APP-000400-CTR-000960` | CAT II | The container platform must prohibit the use of cached authenticators after an organization-defined time period. |
| [`V-233201`](rules/V-233201.md) | `SRG-APP-000401-CTR-000965` | CAT II | The container platform, for PKI-based authentication, must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network. |
| [`V-233202`](rules/V-233202.md) | `SRG-APP-000402-CTR-000970` | CAT II | The container platform must accept Personal Identity Verification (PIV) credentials from other federal agencies. |
| [`V-233206`](rules/V-233206.md) | `SRG-APP-000409-CTR-000990` | CAT II | The container platform must audit non-local maintenance and diagnostic sessions' organization-defined audit events associated with non-local maintenance. |
| [`V-233207`](rules/V-233207.md) | `SRG-APP-000411-CTR-000995` | CAT II | Container platform applications and Application Program Interfaces (API) used for nonlocal maintenance sessions must use FIPS-validated keyed-hash message authentication code (HMAC) to protect the integrity of nonlocal maintenance and diagnostic communications. |
| [`V-233208`](rules/V-233208.md) | `SRG-APP-000412-CTR-001000` | CAT II | The container platform must configure web management tools and Application Program Interfaces (API) with FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to protect the confidentiality of maintenance and diagnostic communications for nonlocal maintenance sessions. |
| [`V-233210`](rules/V-233210.md) | `SRG-APP-000414-CTR-001010` | CAT II | Vulnerability scanning applications must implement privileged access authorization to all container platform components, containers, and container images for selected organization-defined vulnerability scanning activities. |
| [`V-233211`](rules/V-233211.md) | `SRG-APP-000416-CTR-001015` | CAT II | The container platform must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards. |
| [`V-233220`](rules/V-233220.md) | `SRG-APP-000429-CTR-001060` | CAT I | The container platform keystore must implement encryption to prevent unauthorized disclosure of information at rest within the container platform. |
| [`V-233221`](rules/V-233221.md) | `SRG-APP-000431-CTR-001065` | CAT II | The container platform runtime must maintain separate execution domains for each container by assigning each container a separate address space. |
| [`V-233222`](rules/V-233222.md) | `SRG-APP-000435-CTR-001070` | CAT II | The container platform must protect against or limit the effects of all types of denial-of-service (DoS) attacks by employing organization-defined security safeguards. |
| [`V-233224`](rules/V-233224.md) | `SRG-APP-000439-CTR-001080` | CAT I | The application must protect the confidentiality and integrity of transmitted information. |
| [`V-233226`](rules/V-233226.md) | `SRG-APP-000441-CTR-001090` | CAT II | The container platform must maintain the confidentiality and integrity of information during preparation for transmission. |
| [`V-233227`](rules/V-233227.md) | `SRG-APP-000442-CTR-001095` | CAT II | The container platform must maintain the confidentiality and integrity of information during reception. |
| [`V-233228`](rules/V-233228.md) | `SRG-APP-000447-CTR-001100` | CAT II | The container platform must behave in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received. |
| [`V-233229`](rules/V-233229.md) | `SRG-APP-000450-CTR-001105` | CAT II | The container platform must implement organization-defined security safeguards to protect system CPU and memory from resource depletion and unauthorized code execution. |
| [`V-233230`](rules/V-233230.md) | `SRG-APP-000454-CTR-001110` | CAT II | The container platform must remove old components after updated versions have been installed. |
| [`V-233231`](rules/V-233231.md) | `SRG-APP-000454-CTR-001115` | CAT II | The container platform registry must remove old container images after updating versions have been made available. |
| [`V-233233`](rules/V-233233.md) | `SRG-APP-000456-CTR-001125` | CAT II | The container platform registry must contain the latest images with most recent security-relevant software updates within 30 days unless the time period is directed by an authoritative source (e.g., IAVM, CTOs, DTMs, STIGs). |
| [`V-233234`](rules/V-233234.md) | `SRG-APP-000456-CTR-001130` | CAT II | The container platform runtime must have security-relevant software updates installed within 30 days unless the time period is directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). |
| [`V-233242`](rules/V-233242.md) | `SRG-APP-000472-CTR-001170` | CAT II | The organization-defined role must verify correct operation of security functions in the container platform. |
| [`V-233243`](rules/V-233243.md) | `SRG-APP-000473-CTR-001175` | CAT II | The container platform must perform verification of the correct operation of security functions: upon system startup and/or restart; upon command by a user with privileged access; and/or every 30 days. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. |
| [`V-233244`](rules/V-233244.md) | `SRG-APP-000474-CTR-001180` | CAT II | The container platform must provide system notifications to the system administrator and operational staff when anomalies in the operation of the organization-defined security functions are discovered. |
| [`V-233252`](rules/V-233252.md) | `SRG-APP-000492-CTR-001220` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to access security objects occur. |
| [`V-233253`](rules/V-233253.md) | `SRG-APP-000493-CTR-001225` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to access security levels occur. |
| [`V-233254`](rules/V-233254.md) | `SRG-APP-000494-CTR-001230` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to access categories of information (e.g., classification levels) occur. |
| [`V-233255`](rules/V-233255.md) | `SRG-APP-000495-CTR-001235` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to modify privileges occur. |
| [`V-233256`](rules/V-233256.md) | `SRG-APP-000496-CTR-001240` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to modify security objects occur. |
| [`V-233257`](rules/V-233257.md) | `SRG-APP-000497-CTR-001245` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to modify security levels occur. |
| [`V-233258`](rules/V-233258.md) | `SRG-APP-000498-CTR-001250` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to modify categories of information (e.g., classification levels) occur. |
| [`V-233259`](rules/V-233259.md) | `SRG-APP-000499-CTR-001255` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to delete privileges occur. |
| [`V-233260`](rules/V-233260.md) | `SRG-APP-000500-CTR-001260` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to delete security levels occur. |
| [`V-233261`](rules/V-233261.md) | `SRG-APP-000501-CTR-001265` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to delete security objects occur. |
| [`V-233262`](rules/V-233262.md) | `SRG-APP-000502-CTR-001270` | CAT II | The container platform must generate audit records when successful/unsuccessful attempts to delete categories of information (e.g., classification levels) occur. |
| [`V-233263`](rules/V-233263.md) | `SRG-APP-000503-CTR-001275` | CAT II | The container platform must generate audit records when successful/unsuccessful logon attempts occur. |
| [`V-233264`](rules/V-233264.md) | `SRG-APP-000504-CTR-001280` | CAT II | The container platform must generate audit record for privileged activities. |
| [`V-233265`](rules/V-233265.md) | `SRG-APP-000505-CTR-001285` | CAT II | The container platform audit records must record user access start and end times. |
| [`V-233266`](rules/V-233266.md) | `SRG-APP-000506-CTR-001290` | CAT II | The container platform must generate audit records when concurrent logons from different workstations and systems occur. |
| [`V-233267`](rules/V-233267.md) | `SRG-APP-000507-CTR-001295` | CAT II | The container platform runtime must generate audit records when successful/unsuccessful attempts to access objects occur. |
| [`V-233268`](rules/V-233268.md) | `SRG-APP-000508-CTR-001300` | CAT II | Direct access to the container platform must generate audit records. |
| [`V-233269`](rules/V-233269.md) | `SRG-APP-000509-CTR-001305` | CAT II | The container platform must generate audit records for all account creations, modifications, disabling, and termination events. |
| [`V-233270`](rules/V-233270.md) | `SRG-APP-000510-CTR-001310` | CAT II | The container runtime must generate audit records for all container execution, shutdown, restart events, and program initiations. |
| [`V-233271`](rules/V-233271.md) | `SRG-APP-000514-CTR-001315` | CAT II | The container platform must use a valid FIPS 140-2 or FIPS 140-3 approved cryptographic module to generate hashes. |
| [`V-233273`](rules/V-233273.md) | `SRG-APP-000516-CTR-001325` | CAT II | Container platform components must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including SRGs, STIGs, NSA configuration guides, CTOs, and DTMs. |
| [`V-233274`](rules/V-233274.md) | `SRG-APP-000516-CTR-001330` | CAT II | The container platform must be able to store and instantiate industry standard container images. |
| [`V-233275`](rules/V-233275.md) | `SRG-APP-000516-CTR-001335` | CAT II | The container platform must continuously scan components, containers, and images for vulnerabilities. |
| [`V-233276`](rules/V-233276.md) | `SRG-APP-000560-CTR-001340` | CAT II | The container platform must prohibit communication using TLS versions 1.0 and 1.1, and SSL 2.0 and 3.0. |
| [`V-233284`](rules/V-233284.md) | `SRG-APP-000605-CTR-001380` | CAT II | The container platform must validate certificates used for Transport Layer Security (TLS) functions by performing an RFC 5280-compliant certification path validation. |
| [`V-233285`](rules/V-233285.md) | `SRG-APP-000610-CTR-001385` | CAT II | The container platform must use FIPS-validated SHA-2 or higher hash function for digital signature generation and verification (non-legacy use). |
| [`V-233289`](rules/V-233289.md) | `SRG-APP-000635-CTR-001405` | CAT I | The container platform must use a FIPS-validated cryptographic module to implement encryption services for unclassified information requiring confidentiality. |
| [`V-233290`](rules/V-233290.md) | `SRG-APP-000645-CTR-001410` | CAT I | The container platform must prohibit or restrict the use of protocols that transmit unencrypted authentication information or use flawed cryptographic algorithms for transmission. |
| [`V-257291`](rules/V-257291.md) | `SRG-APP-000318-CTR-000740` | CAT II | The container platform must enforce organization-defined circumstances and/or usage conditions for organization-defined accounts. |
| [`V-263586`](rules/V-263586.md) | `SRG-APP-000705-CTR-000110` | CAT II | The container platform must disable accounts when the accounts are no longer associated to a user. |
| [`V-263587`](rules/V-263587.md) | `SRG-APP-000745-CTR-000120` | CAT II | The container platform must implement the capability to centrally review and analyze audit records from multiple components within the system. |
| [`V-263588`](rules/V-263588.md) | `SRG-APP-000795-CTR-000130` | CAT II | The container platform must alert organization-defined personnel or roles upon detection of unauthorized access, modification, or deletion of audit information. |
| [`V-263589`](rules/V-263589.md) | `SRG-APP-000820-CTR-000170` | CAT II | The container platform must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access. |
| [`V-263590`](rules/V-263590.md) | `SRG-APP-000825-CTR-000180` | CAT II | The container platform must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements. |
| [`V-263591`](rules/V-263591.md) | `SRG-APP-000830-CTR-000190` | CAT II | The container platform must for password-based authentication, maintain a list of commonly used, expected, or compromised passwords on an organization-defined frequency. |
| [`V-263592`](rules/V-263592.md) | `SRG-APP-000835-CTR-000200` | CAT II | The container platform must for password-based authentication, update the list of passwords on an organization-defined frequency. |
| [`V-263593`](rules/V-263593.md) | `SRG-APP-000840-CTR-000210` | CAT II | The container platform must for password-based authentication, update the list of passwords when organizational passwords are suspected to have been compromised directly or indirectly. |
| [`V-263594`](rules/V-263594.md) | `SRG-APP-000845-CTR-000220` | CAT II | The container platform must for password-based authentication, verify when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a). |
| [`V-263595`](rules/V-263595.md) | `SRG-APP-000855-CTR-000240` | CAT II | The container platform must for password-based authentication, require immediate selection of a new password upon account recovery. |
| [`V-263596`](rules/V-263596.md) | `SRG-APP-000860-CTR-000250` | CAT II | The container platform must for password-based authentication, allow user selection of long passwords and passphrases, including spaces and all printable characters. |
| [`V-263597`](rules/V-263597.md) | `SRG-APP-000865-CTR-000260` | CAT II | The container platform must for password-based authentication, employ automated tools to assist the user in selecting strong password authenticators. |
| [`V-263598`](rules/V-263598.md) | `SRG-APP-000880-CTR-000290` | CAT II | The container platform must protect nonlocal maintenance sessions by separating the maintenance session from other network sessions with the system by logically separated communications paths. |
| [`V-263599`](rules/V-263599.md) | `SRG-APP-000910-CTR-000300` | CAT II | The container platform must include only approved trust anchors in trust stores or certificate stores managed by the organization. |
| [`V-263600`](rules/V-263600.md) | `SRG-APP-000915-CTR-000310` | CAT II | The container platform must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store. |
| [`V-263601`](rules/V-263601.md) | `SRG-APP-000920-CTR-000320` | CAT II | The container platform must synchronize system clocks within and between systems or system components. |
| [`V-270875`](rules/V-270875.md) | `SRG-APP-000247-CTR-000330` | CAT II | The container must have resource request limits set. |
| [`V-270876`](rules/V-270876.md) | `SRG-APP-000380-CTR-000340` | CAT II | The container root filesystem must be mounted as read-only. |
| [`V-278968`](rules/V-278968.md) | `SRG-APP-001035-CTR-000323` | CAT I | The container platform must be a version supported by the vendor. |
