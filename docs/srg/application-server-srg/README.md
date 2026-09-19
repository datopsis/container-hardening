# Application Server Security Requirements Guide

Release: 5 Benchmark Date: 01 Jul 2026. Accepted 2026-06-29.

| | |
| --- | --- |
| Benchmark | `Application_Server_SRG` |
| Rules | **137** |
| CAT I | 13 |
| CAT II | 124 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-204708`](rules/V-204708.md) | `SRG-APP-000001-AS-000001` | CAT II | The application server must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types. |
| [`V-204709`](rules/V-204709.md) | `SRG-APP-000014-AS-000009` | CAT II | The application server must use encryption strength in accordance with the categorization of the management data during remote access management sessions. |
| [`V-204710`](rules/V-204710.md) | `SRG-APP-000015-AS-000010` | CAT II | The application server must implement cryptography mechanisms to protect the integrity of the remote access session. |
| [`V-204711`](rules/V-204711.md) | `SRG-APP-000016-AS-000013` | CAT II | The application server must ensure remote sessions for accessing security functions and security-relevant information are logged. |
| [`V-204712`](rules/V-204712.md) | `SRG-APP-000033-AS-000024` | CAT II | The application server must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. |
| [`V-204713`](rules/V-204713.md) | `SRG-APP-000068-AS-000035` | CAT II | The application server management interface must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system. |
| [`V-204714`](rules/V-204714.md) | `SRG-APP-000069-AS-000036` | CAT II | The application server management interface must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access. |
| [`V-204715`](rules/V-204715.md) | `SRG-APP-000080-AS-000045` | CAT II | The application server must protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation. |
| [`V-204716`](rules/V-204716.md) | `SRG-APP-000086-AS-000048` | CAT II | For application servers providing log record aggregation, the application server must compile log records from organization-defined information system components into a system-wide log trail that is time-correlated with an organization-defined level of tolerance for the relationship between time stamps of individual records in the log trail. |
| [`V-204717`](rules/V-204717.md) | `SRG-APP-000089-AS-000050` | CAT II | The application server must generate log records for access and authentication events. |
| [`V-204718`](rules/V-204718.md) | `SRG-APP-000090-AS-000051` | CAT II | The application server must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which logable events are to be logged. |
| [`V-204719`](rules/V-204719.md) | `SRG-APP-000091-AS-000052` | CAT II | The application server must generate log records when successful/unsuccessful attempts to access subject privileges occur. |
| [`V-204720`](rules/V-204720.md) | `SRG-APP-000092-AS-000053` | CAT II | The application server must initiate session logging upon startup. |
| [`V-204721`](rules/V-204721.md) | `SRG-APP-000095-AS-000056` | CAT II | The application server must produce log records containing information to establish what type of events occurred. |
| [`V-204722`](rules/V-204722.md) | `SRG-APP-000096-AS-000059` | CAT II | The application server must produce log records containing sufficient information to establish when (date and time) the events occurred. |
| [`V-204723`](rules/V-204723.md) | `SRG-APP-000097-AS-000060` | CAT II | The application server must produce log records containing sufficient information to establish where the events occurred. |
| [`V-204724`](rules/V-204724.md) | `SRG-APP-000098-AS-000061` | CAT II | The application server must produce log records containing sufficient information to establish the sources of the events. |
| [`V-204725`](rules/V-204725.md) | `SRG-APP-000099-AS-000062` | CAT II | The application server must produce log records that contain sufficient information to establish the outcome of events. |
| [`V-204726`](rules/V-204726.md) | `SRG-APP-000100-AS-000063` | CAT II | The application server must generate log records containing information that establishes the identity of any individual or process associated with the event. |
| [`V-204727`](rules/V-204727.md) | `SRG-APP-000101-AS-000072` | CAT II | The application server must generate log records containing the full-text recording of privileged commands or the individual identities of group account users. |
| [`V-204728`](rules/V-204728.md) | `SRG-APP-000108-AS-000067` | CAT II | The application server must alert the SA and ISSO, at a minimum, in the event of a log processing failure. |
| [`V-204731`](rules/V-204731.md) | `SRG-APP-000116-AS-000076` | CAT II | The application server must use internal system clocks to generate time stamps for log records. |
| [`V-204732`](rules/V-204732.md) | `SRG-APP-000118-AS-000078` | CAT II | The application server must protect log information from any type of unauthorized read access. |
| [`V-204733`](rules/V-204733.md) | `SRG-APP-000119-AS-000079` | CAT II | The application server must protect log information from unauthorized modification. |
| [`V-204734`](rules/V-204734.md) | `SRG-APP-000120-AS-000080` | CAT II | The application server must protect log information from unauthorized deletion. |
| [`V-204735`](rules/V-204735.md) | `SRG-APP-000121-AS-000081` | CAT II | The application server must protect log tools from unauthorized access. |
| [`V-204736`](rules/V-204736.md) | `SRG-APP-000122-AS-000082` | CAT II | The application server must protect log tools from unauthorized modification. |
| [`V-204737`](rules/V-204737.md) | `SRG-APP-000123-AS-000083` | CAT II | The application server must protect log tools from unauthorized deletion. |
| [`V-204738`](rules/V-204738.md) | `SRG-APP-000125-AS-000084` | CAT II | The application server must back up log records at least every seven days onto a different system or system component than the system or component being logged. |
| [`V-204739`](rules/V-204739.md) | `SRG-APP-000126-AS-000085` | CAT II | The application server must use cryptographic mechanisms to protect the integrity of log information. |
| [`V-204740`](rules/V-204740.md) | `SRG-APP-000131-AS-000002` | CAT II | The application server must prevent the installation of patches, service packs, or application components without verification the software component has been digitally signed using a certificate recognized and approved by the organization. |
| [`V-204741`](rules/V-204741.md) | `SRG-APP-000133-AS-000092` | CAT II | The application server must limit privileges to change the software resident within software libraries. |
| [`V-204742`](rules/V-204742.md) | `SRG-APP-000133-AS-000093` | CAT II | The application server must be capable of reverting to the last known good configuration in the event of failed installations and upgrades. |
| [`V-204743`](rules/V-204743.md) | `SRG-APP-000141-AS-000095` | CAT II | The application server must adhere to the principles of least functionality by providing only essential capabilities. |
| [`V-204744`](rules/V-204744.md) | `SRG-APP-000142-AS-000014` | CAT II | The application server must prohibit or restrict the use of nonsecure ports, protocols, modules, and/or services as defined in the PPSM CAL and vulnerability assessments. |
| [`V-204745`](rules/V-204745.md) | `SRG-APP-000148-AS-000101` | CAT II | The application server must use an approved DOD enterprise identity, credential, and access management (ICAM) solution to uniquely identify and authenticate users (or processes acting on behalf of organizational users). |
| [`V-204746`](rules/V-204746.md) | `SRG-APP-000149-AS-000102` | CAT I | The application server must use multifactor authentication for network access to privileged accounts. |
| [`V-204747`](rules/V-204747.md) | `SRG-APP-000151-AS-000103` | CAT I | The application server must use multifactor authentication for local access to privileged accounts. |
| [`V-204748`](rules/V-204748.md) | `SRG-APP-000153-AS-000104` | CAT II | The application server must authenticate users individually prior to using a group authenticator. |
| [`V-204749`](rules/V-204749.md) | `SRG-APP-000156-AS-000106` | CAT II | The application server must provide security extensions to extend the SOAP protocol and provide secure authentication when accessing sensitive data. |
| [`V-204750`](rules/V-204750.md) | `SRG-APP-000163-AS-000111` | CAT II | The application server must disable identifiers (individuals, groups, roles, and devices) after 35 days of inactivity. |
| [`V-204751`](rules/V-204751.md) | `SRG-APP-000171-AS-000119` | CAT II | The application server must for password-based authentication, store passwords using an approved salted key derivation function, preferably using a keyed hash. |
| [`V-204752`](rules/V-204752.md) | `SRG-APP-000172-AS-000120` | CAT I | The application server must transmit only encrypted representations of passwords. |
| [`V-204753`](rules/V-204753.md) | `SRG-APP-000172-AS-000121` | CAT I | The application server must utilize encryption when using LDAP for authentication. |
| [`V-204754`](rules/V-204754.md) | `SRG-APP-000175-AS-000124` | CAT II | The application server must perform RFC 5280-compliant certification path validation. |
| [`V-204755`](rules/V-204755.md) | `SRG-APP-000176-AS-000125` | CAT II | Only authenticated system administrators or the designated PKI Sponsor for the application server must have access to the web servers private key. |
| [`V-204756`](rules/V-204756.md) | `SRG-APP-000177-AS-000126` | CAT II | The application server must map the authenticated identity to the individual user or group account for PKI-based authentication. |
| [`V-204757`](rules/V-204757.md) | `SRG-APP-000178-AS-000127` | CAT II | The application server must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals. |
| [`V-204758`](rules/V-204758.md) | `SRG-APP-000179-AS-000129` | CAT I | The application server must utilize FIPS 140-2 approved encryption modules when authenticating users and processes. |
| [`V-204759`](rules/V-204759.md) | `SRG-APP-000181-AS-000255` | CAT II | The application server must provide a log reduction capability that supports on-demand reporting requirements. |
| [`V-204760`](rules/V-204760.md) | `SRG-APP-000206-AS-000145` | CAT II | The application server must identify prohibited mobile code. |
| [`V-204761`](rules/V-204761.md) | `SRG-APP-000211-AS-000146` | CAT II | The application server must separate hosted application functionality from application server management functionality. |
| [`V-204762`](rules/V-204762.md) | `SRG-APP-000219-AS-000147` | CAT II | The application server must be configured to mutually authenticate connecting proxies, application servers or gateways. |
| [`V-204763`](rules/V-204763.md) | `SRG-APP-000220-AS-000148` | CAT II | The application server must invalidate session identifiers upon user logout or other session termination. |
| [`V-204764`](rules/V-204764.md) | `SRG-APP-000223-AS-000150` | CAT II | The application server must generate a unique session identifier for each session. |
| [`V-204765`](rules/V-204765.md) | `SRG-APP-000223-AS-000151` | CAT II | The application server must recognize only system-generated session identifiers. |
| [`V-204766`](rules/V-204766.md) | `SRG-APP-000224-AS-000152` | CAT I | The application server must generate a unique session identifier using a FIPS 140-2 approved random number generator. |
| [`V-204767`](rules/V-204767.md) | `SRG-APP-000225-AS-000153` | CAT II | The application server must be configured to perform complete application deployments. |
| [`V-204768`](rules/V-204768.md) | `SRG-APP-000225-AS-000154` | CAT II | The application server must provide a clustering capability. |
| [`V-204769`](rules/V-204769.md) | `SRG-APP-000225-AS-000166` | CAT II | The application server must fail to a secure state if system initialization fails, shutdown fails, or aborts fail. |
| [`V-204770`](rules/V-204770.md) | `SRG-APP-000231-AS-000133` | CAT II | The application server must protect the confidentiality and integrity of all information at rest. |
| [`V-204771`](rules/V-204771.md) | `SRG-APP-000231-AS-000156` | CAT II | The application server must employ cryptographic mechanisms to ensure confidentiality and integrity of all information at rest when stored off-line. |
| [`V-204772`](rules/V-204772.md) | `SRG-APP-000251-AS-000165` | CAT II | The application server must check the validity of all data inputs to the management interface, except those specifically identified by the organization. |
| [`V-204773`](rules/V-204773.md) | `SRG-APP-000266-AS-000168` | CAT II | The application server must identify potentially security-relevant error conditions. |
| [`V-204774`](rules/V-204774.md) | `SRG-APP-000266-AS-000169` | CAT II | The application server must only generate error messages that provide information necessary for corrective actions without revealing sensitive or potentially harmful information in error logs and administrative messages. |
| [`V-204775`](rules/V-204775.md) | `SRG-APP-000267-AS-000170` | CAT II | The application server must restrict error messages only to authorized users. |
| [`V-204776`](rules/V-204776.md) | `SRG-APP-000290-AS-000174` | CAT II | The application server must use cryptographic mechanisms to protect the integrity of log tools. |
| [`V-204777`](rules/V-204777.md) | `SRG-APP-000295-AS-000263` | CAT II | The application server must automatically terminate a user session after organization-defined conditions or trigger events requiring a session disconnect. |
| [`V-204778`](rules/V-204778.md) | `SRG-APP-000296-AS-000201` | CAT II | The application server management interface must provide a logout capability for user-initiated communication session. |
| [`V-204779`](rules/V-204779.md) | `SRG-APP-000297-AS-000188` | CAT II | The application server management interface must display an explicit logout message to users indicating the reliable termination of authenticated communications sessions. |
| [`V-204780`](rules/V-204780.md) | `SRG-APP-000313-AS-000003` | CAT II | The application server must associate organization-defined types of security attributes having organization-defined security attribute values with information in process. |
| [`V-204781`](rules/V-204781.md) | `SRG-APP-000314-AS-000005` | CAT II | The application server must associate organization-defined types of security attributes having organization-defined security attribute values with information in transmission. |
| [`V-204782`](rules/V-204782.md) | `SRG-APP-000315-AS-000094` | CAT II | The application server must control remote access methods. |
| [`V-204783`](rules/V-204783.md) | `SRG-APP-000316-AS-000199` | CAT II | The application server must provide the capability to immediately disconnect or disable remote access to the management interface. |
| [`V-204784`](rules/V-204784.md) | `SRG-APP-000340-AS-000185` | CAT II | The application server must prevent non-privileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures. |
| [`V-204785`](rules/V-204785.md) | `SRG-APP-000343-AS-000030` | CAT II | The application server must provide access logging that ensures users who are granted a privileged role (or roles) have their privileged activity logged. |
| [`V-204788`](rules/V-204788.md) | `SRG-APP-000357-AS-000038` | CAT II | The application server must allocate log record storage capacity in accordance with organization-defined log record storage requirements. |
| [`V-204789`](rules/V-204789.md) | `SRG-APP-000358-AS-000064` | CAT II | The application server must off-load log records onto a different system or media from the system being logged. |
| [`V-204790`](rules/V-204790.md) | `SRG-APP-000359-AS-000065` | CAT II | The application server must provide an immediate warning to the SA and ISSO, at a minimum, when allocated log record storage volume reaches 75% of maximum log record storage capacity. |
| [`V-204791`](rules/V-204791.md) | `SRG-APP-000360-AS-000066` | CAT II | The application server must provide an immediate real-time alert to authorized users of all log failure events requiring real-time alerts. |
| [`V-204792`](rules/V-204792.md) | `SRG-APP-000371-AS-000077` | CAT II | The application server must compare internal application server clocks at least every 24 hours with an authoritative time source. |
| [`V-204793`](rules/V-204793.md) | `SRG-APP-000372-AS-000212` | CAT II | The application server must synchronize internal application server clocks to an authoritative time source when the time difference is greater than the organization-defined time period. |
| [`V-204794`](rules/V-204794.md) | `SRG-APP-000374-AS-000210` | CAT II | The application server must record time stamps for log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT). |
| [`V-204795`](rules/V-204795.md) | `SRG-APP-000375-AS-000211` | CAT II | The application server must record time stamps for log records that meet a granularity of one second for a minimum degree of precision. |
| [`V-204796`](rules/V-204796.md) | `SRG-APP-000380-AS-000088` | CAT II | The application server must enforce access restrictions associated with changes to application server configuration. |
| [`V-204797`](rules/V-204797.md) | `SRG-APP-000381-AS-000089` | CAT II | The application server must log the enforcement actions used to restrict access associated with changes to the application server. |
| [`V-204798`](rules/V-204798.md) | `SRG-APP-000389-AS-000253` | CAT II | The application server must require users to reauthenticate when organization-defined circumstances or situations require reauthentication. |
| [`V-204800`](rules/V-204800.md) | `SRG-APP-000391-AS-000239` | CAT I | The application server must accept Personal Identity Verification (PIV) credentials to access the management interface. |
| [`V-204801`](rules/V-204801.md) | `SRG-APP-000392-AS-000240` | CAT I | The application server must electronically verify Personal Identity Verification (PIV) credentials for access to the management interface. |
| [`V-204804`](rules/V-204804.md) | `SRG-APP-000400-AS-000246` | CAT II | The application server must prohibit the use of cached authenticators after an organization-defined time period. |
| [`V-204805`](rules/V-204805.md) | `SRG-APP-000401-AS-000243` | CAT II | The application server, for PKI-based authentication, must implement a local cache of revocation data to support path discovery and validation in case of the inability to access revocation information via the network. |
| [`V-204806`](rules/V-204806.md) | `SRG-APP-000402-AS-000247` | CAT II | The application server must accept Personal Identity Verification (PIV) credentials from other federal agencies to access the management interface. |
| [`V-204807`](rules/V-204807.md) | `SRG-APP-000403-AS-000248` | CAT II | The application server must electronically verify Personal Identity Verification (PIV) credentials from other federal agencies to access the management interface. |
| [`V-204808`](rules/V-204808.md) | `SRG-APP-000404-AS-000249` | CAT II | The application server must accept Federal Identity, Credential, and Access Management (FICAM)-approved third-party credentials. |
| [`V-204809`](rules/V-204809.md) | `SRG-APP-000405-AS-000250` | CAT II | The application server must conform to Federal Identity, Credential, and Access Management (FICAM)-issued profiles. |
| [`V-204811`](rules/V-204811.md) | `SRG-APP-000427-AS-000264` | CAT II | The application server must only allow the use of DoD PKI-established certificate authorities for verification of the establishment of protected sessions. |
| [`V-204812`](rules/V-204812.md) | `SRG-APP-000428-AS-000265` | CAT I | The application server must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest on organization-defined information system components. |
| [`V-204813`](rules/V-204813.md) | `SRG-APP-000429-AS-000157` | CAT I | The application must implement cryptographic mechanisms to prevent unauthorized disclosure of organization-defined information at rest on organization-defined information system components. |
| [`V-204814`](rules/V-204814.md) | `SRG-APP-000435-AS-000069` | CAT II | The application server, when a MAC I system, must be in a high-availability (HA) cluster. |
| [`V-204815`](rules/V-204815.md) | `SRG-APP-000435-AS-000163` | CAT II | The application server must protect against or limit the effects of all types of Denial of Service (DoS) attacks by employing organization-defined security safeguards. |
| [`V-204816`](rules/V-204816.md) | `SRG-APP-000439-AS-000155` | CAT I | The application server must protect the confidentiality and integrity of transmitted information through the use of an approved TLS version. |
| [`V-204817`](rules/V-204817.md) | `SRG-APP-000439-AS-000274` | CAT I | The application server must remove all export ciphers to protect the confidentiality and integrity of transmitted information. |
| [`V-204818`](rules/V-204818.md) | `SRG-APP-000440-AS-000167` | CAT II | The application server must employ approved cryptographic mechanisms to prevent unauthorized disclosure of information and/or detect changes to information during transmission. |
| [`V-204819`](rules/V-204819.md) | `SRG-APP-000441-AS-000258` | CAT II | The application server must maintain the confidentiality and integrity of information during preparation for transmission. |
| [`V-204820`](rules/V-204820.md) | `SRG-APP-000442-AS-000259` | CAT II | The application server must maintain the confidentiality and integrity of information during reception. |
| [`V-204821`](rules/V-204821.md) | `SRG-APP-000447-AS-000273` | CAT II | The application server must behave in a predictable and documented manner that reflects organizational and system objectives when invalid inputs are received. |
| [`V-204822`](rules/V-204822.md) | `SRG-APP-000454-AS-000268` | CAT II | The application server must remove organization-defined software components after updated versions have been installed. |
| [`V-204823`](rules/V-204823.md) | `SRG-APP-000456-AS-000266` | CAT II | The application server must install security-relevant software updates within 30 days unless the time period is directed by an authoritative source (e.g., IAVM, CTOs, DTMs, STIGs). |
| [`V-204824`](rules/V-204824.md) | `SRG-APP-000495-AS-000220` | CAT II | The application server must generate log records when successful/unsuccessful attempts to modify privileges occur. |
| [`V-204825`](rules/V-204825.md) | `SRG-APP-000499-AS-000224` | CAT II | The application server must generate log records when successful/unsuccessful attempts to delete privileges occur. |
| [`V-204826`](rules/V-204826.md) | `SRG-APP-000503-AS-000228` | CAT II | The application server must generate log records when successful/unsuccessful logon attempts occur. |
| [`V-204827`](rules/V-204827.md) | `SRG-APP-000504-AS-000229` | CAT II | The application server must generate log records for privileged activities. |
| [`V-204828`](rules/V-204828.md) | `SRG-APP-000505-AS-000230` | CAT II | The application must generate log records showing starting and ending times for user access to the application server management interface. |
| [`V-204829`](rules/V-204829.md) | `SRG-APP-000506-AS-000231` | CAT II | The application server must generate log records when concurrent logons from different workstations occur to the application server management interface. |
| [`V-204830`](rules/V-204830.md) | `SRG-APP-000509-AS-000234` | CAT II | The application server must generate log records for all account creations, modifications, disabling, and termination events. |
| [`V-204831`](rules/V-204831.md) | `SRG-APP-000514-AS-000136` | CAT II | Application servers must use NIST-approved or NSA-approved key management technology and processes. |
| [`V-204832`](rules/V-204832.md) | `SRG-APP-000514-AS-000137` | CAT II | The application server must use DOD- or CNSS-approved PKI Class 3 or Class 4 certificates. |
| [`V-204833`](rules/V-204833.md) | `SRG-APP-000515-AS-000203` | CAT II | The application server must, at a minimum, transfer the logs of interconnected systems in real time, and transfer the logs of standalone systems weekly. |
| [`V-204834`](rules/V-204834.md) | `SRG-APP-000516-AS-000237` | CAT II | The application server must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs. |
| [`V-240925`](rules/V-240925.md) | `SRG-APP-000416-AS-000140` | CAT II | The application server must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards. |
| [`V-263549`](rules/V-263549.md) | `SRG-APP-000705-AS-000110` | CAT II | The application server must disable accounts when the accounts are no longer associated to a user. |
| [`V-263550`](rules/V-263550.md) | `SRG-APP-000795-AS-000130` | CAT II | The application server must alert organization-defined personnel or roles upon detection of unauthorized access, modification, or deletion of audit information. |
| [`V-263551`](rules/V-263551.md) | `SRG-APP-000820-AS-000170` | CAT II | The application server must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access. |
| [`V-263552`](rules/V-263552.md) | `SRG-APP-000825-AS-000180` | CAT II | The application server must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements. |
| [`V-263553`](rules/V-263553.md) | `SRG-APP-000880-AS-000290` | CAT II | The application server must protect nonlocal maintenance sessions by separating the maintenance session from other network sessions with the system by logically separated communications paths. |
| [`V-263554`](rules/V-263554.md) | `SRG-APP-000910-AS-000300` | CAT II | The application server must include only approved trust anchors in trust stores or certificate stores managed by the organization. |
| [`V-263555`](rules/V-263555.md) | `SRG-APP-000915-AS-000310` | CAT II | The application server must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store. |
| [`V-263556`](rules/V-263556.md) | `SRG-APP-000920-AS-000320` | CAT II | The application server must synchronize system clocks within and between systems or system components. |
| [`V-278959`](rules/V-278959.md) | `SRG-APP-000009-AS-000321` | CAT II | The application server must dynamically associate security attributes with organization-defined subjects in accordance with organization-defined security policies as information is created and combined. |
| [`V-278960`](rules/V-278960.md) | `SRG-APP-000334-AS-000322` | CAT II | The application server must uniquely identify and authenticate source by organization, system, application, and/or individual for information transfer. |
| [`V-278961`](rules/V-278961.md) | `SRG-APP-001040-AS-000324` | CAT II | The application server must enforce attribute-based control access over defined subjects and objects based upon organization-defined attributes to assume access permissions. |
| [`V-278962`](rules/V-278962.md) | `SRG-APP-001045-AS-000325` | CAT II | The application server must attach data tags containing organization-defined authorized processing to organization-defined elements of personally identifiable information. |
| [`V-278963`](rules/V-278963.md) | `SRG-APP-001050-AS-000326` | CAT II | The application server must attach data tags containing organization-defined processing purposes to organization-defined elements of personally identifiable information. |
| [`V-278964`](rules/V-278964.md) | `SRG-APP-001055-AS-000327` | CAT II | The application server must employ automated mechanisms to integrate intrusion detection mechanisms into access control mechanisms. |
| [`V-278965`](rules/V-278965.md) | `SRG-APP-000298-AS-000190` | CAT II | The application server must dynamically associate security attributes with organization-defined objects in accordance with organization-defined security policies as information is created and combined. |
| [`V-278966`](rules/V-278966.md) | `SRG-APP-000329-AS-000200` | CAT II | The application server must enforce a role-based access control (RBAC) policy over defined subjects and objects. |
| [`V-278967`](rules/V-278967.md) | `SRG-APP-001035-AS-000323` | CAT I | The application server must be a version supported by the vendor. |
