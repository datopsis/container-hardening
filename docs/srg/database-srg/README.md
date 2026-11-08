# Database Security Requirements Guide

Release: 6 Benchmark Date: 30 Sep 2026. Accepted 2026-08-31.

| | |
| --- | --- |
| Benchmark | `Database_Generic` |
| Rules | **142** |
| CAT I | 14 |
| CAT II | 128 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-206519`](rules/V-206519.md) | `SRG-APP-000001-DB-000031` | CAT II | The DBMS must limit the number of concurrent sessions to an organization-defined number per user for all accounts and/or account types. |
| [`V-206520`](rules/V-206520.md) | `SRG-APP-000023-DB-000001` | CAT I | The DBMS must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals. |
| [`V-206521`](rules/V-206521.md) | `SRG-APP-000033-DB-000084` | CAT I | The DBMS must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies. |
| [`V-206522`](rules/V-206522.md) | `SRG-APP-000080-DB-000063` | CAT II | The DBMS must protect against a user falsely repudiating having performed organization-defined actions. |
| [`V-206523`](rules/V-206523.md) | `SRG-APP-000089-DB-000064` | CAT II | The DBMS must provide audit record generation capability for DoW-defined auditable events within all DBMS/database components. |
| [`V-206524`](rules/V-206524.md) | `SRG-APP-000090-DB-000065` | CAT II | The DBMS must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited. |
| [`V-206525`](rules/V-206525.md) | `SRG-APP-000091-DB-000066` | CAT II | The DBMS must be able to generate audit records when privileges/permissions are retrieved. |
| [`V-206526`](rules/V-206526.md) | `SRG-APP-000091-DB-000325` | CAT II | The DBMS must be able to generate audit records when unsuccessful attempts to retrieve privileges/permissions occur. |
| [`V-206527`](rules/V-206527.md) | `SRG-APP-000092-DB-000208` | CAT II | The DBMS must initiate session auditing upon startup. |
| [`V-206528`](rules/V-206528.md) | `SRG-APP-000095-DB-000039` | CAT II | The DBMS must produce audit records containing sufficient information to establish what type of events occurred. |
| [`V-206529`](rules/V-206529.md) | `SRG-APP-000096-DB-000040` | CAT II | The DBMS must produce audit records containing time stamps to establish when the events occurred. |
| [`V-206530`](rules/V-206530.md) | `SRG-APP-000097-DB-000041` | CAT II | The DBMS must produce audit records containing sufficient information to establish where the events occurred. |
| [`V-206531`](rules/V-206531.md) | `SRG-APP-000098-DB-000042` | CAT II | The DBMS must produce audit records containing sufficient information to establish the sources (origins) of the events. |
| [`V-206532`](rules/V-206532.md) | `SRG-APP-000099-DB-000043` | CAT II | The DBMS must produce audit records containing sufficient information to establish the outcome (success or failure) of the events. |
| [`V-206533`](rules/V-206533.md) | `SRG-APP-000100-DB-000201` | CAT II | The DBMS must produce audit records containing sufficient information to establish the identity of any user/subject or process associated with the event. |
| [`V-206534`](rules/V-206534.md) | `SRG-APP-000101-DB-000044` | CAT II | The DBMS must include additional, more detailed, organization-defined information in the audit records for audit events identified by type, location, or subject. |
| [`V-206537`](rules/V-206537.md) | `SRG-APP-000116-DB-000057` | CAT II | The DBMS must use system clocks to generate time stamps for use in audit records and application data. |
| [`V-206538`](rules/V-206538.md) | `SRG-APP-000118-DB-000059` | CAT II | The audit information produced by the DBMS must be protected from unauthorized read access. |
| [`V-206539`](rules/V-206539.md) | `SRG-APP-000119-DB-000060` | CAT II | The audit information produced by the DBMS must be protected from unauthorized modification. |
| [`V-206540`](rules/V-206540.md) | `SRG-APP-000120-DB-000061` | CAT II | The audit information produced by the DBMS must be protected from unauthorized deletion. |
| [`V-206541`](rules/V-206541.md) | `SRG-APP-000121-DB-000202` | CAT II | The DBMS must protect its audit features from unauthorized access. |
| [`V-206542`](rules/V-206542.md) | `SRG-APP-000122-DB-000203` | CAT II | The DBMS must protect its audit configuration from unauthorized modification. |
| [`V-206543`](rules/V-206543.md) | `SRG-APP-000123-DB-000204` | CAT II | The DBMS must protect its audit features from unauthorized removal. |
| [`V-206544`](rules/V-206544.md) | `SRG-APP-000133-DB-000179` | CAT II | The DBMS must limit privileges to change software modules, to include stored procedures, functions and triggers, and links to software external to the DBMS. |
| [`V-206545`](rules/V-206545.md) | `SRG-APP-000133-DB-000198` | CAT I | The DBMS software installation account must be restricted to authorized users. |
| [`V-206546`](rules/V-206546.md) | `SRG-APP-000133-DB-000199` | CAT II | Database software, including DBMS configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications. |
| [`V-206547`](rules/V-206547.md) | `SRG-APP-000133-DB-000200` | CAT II | Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to the DBMS, etc.) must be owned by database/DBMS principals authorized for ownership. |
| [`V-206548`](rules/V-206548.md) | `SRG-APP-000133-DB-000362` | CAT II | The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to the DBMS, etc.) must be restricted to authorized users. |
| [`V-206549`](rules/V-206549.md) | `SRG-APP-000141-DB-000090` | CAT II | Default demonstration and sample databases, database objects, and applications must be removed. |
| [`V-206550`](rules/V-206550.md) | `SRG-APP-000141-DB-000091` | CAT II | Unused database components, DBMS software, and database objects must be removed. |
| [`V-206551`](rules/V-206551.md) | `SRG-APP-000141-DB-000092` | CAT II | Unused database components that are integrated in the DBMS and cannot be uninstalled must be disabled. |
| [`V-206552`](rules/V-206552.md) | `SRG-APP-000141-DB-000093` | CAT II | Access to external executables must be disabled or restricted. |
| [`V-206553`](rules/V-206553.md) | `SRG-APP-000142-DB-000094` | CAT II | The DBMS must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. |
| [`V-206554`](rules/V-206554.md) | `SRG-APP-000148-DB-000103` | CAT II | The DBMS must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users). |
| [`V-206555`](rules/V-206555.md) | `SRG-APP-000164-DB-000401` | CAT I | If DBMS authentication, using passwords, is employed, the DBMS must enforce the DoW standards for password complexity and lifetime. |
| [`V-206556`](rules/V-206556.md) | `SRG-APP-000171-DB-000074` | CAT I | The DBMS must for password-based authentication, store passwords using an approved salted key derivation function, preferably using a keyed hash. |
| [`V-206557`](rules/V-206557.md) | `SRG-APP-000172-DB-000075` | CAT I | If passwords are used for authentication, the DBMS must transmit only encrypted representations of passwords. |
| [`V-206558`](rules/V-206558.md) | `SRG-APP-000175-DB-000067` | CAT II | The DBMS, when utilizing Public Key Infrastructure (PKI)-based authentication, must validate certificates by performing RFC 5280-compliant certification path validation. |
| [`V-206559`](rules/V-206559.md) | `SRG-APP-000176-DB-000068` | CAT I | The DBMS must enforce authorized access to all Public Key Infrastructure (PKI) private keys stored/utilized by the DBMS. |
| [`V-206560`](rules/V-206560.md) | `SRG-APP-000177-DB-000069` | CAT II | The DBMS must map the Public Key Infrastructure (PKI)-authenticated identity to an associated user account. |
| [`V-206561`](rules/V-206561.md) | `SRG-APP-000178-DB-000083` | CAT I | The DBMS must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals. |
| [`V-206562`](rules/V-206562.md) | `SRG-APP-000179-DB-000114` | CAT I | The DBMS must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations. |
| [`V-206563`](rules/V-206563.md) | `SRG-APP-000180-DB-000115` | CAT II | The DBMS must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users). |
| [`V-206564`](rules/V-206564.md) | `SRG-APP-000211-DB-000122` | CAT II | The DBMS must separate user functionality (including user interface services) from database management functionality. |
| [`V-206565`](rules/V-206565.md) | `SRG-APP-000220-DB-000149` | CAT II | The DBMS must invalidate session identifiers upon user logout or other session termination. |
| [`V-206566`](rules/V-206566.md) | `SRG-APP-000223-DB-000168` | CAT II | The DBMS must recognize only system-generated session identifiers. |
| [`V-206567`](rules/V-206567.md) | `SRG-APP-000224-DB-000384` | CAT II | The DBMS must maintain the authenticity of communications sessions by guarding against man-in-the-middle attacks that guess at Session ID values. |
| [`V-206568`](rules/V-206568.md) | `SRG-APP-000225-DB-000153` | CAT II | The DBMS must fail to a secure state if system initialization fails, shutdown fails, or aborts fail. |
| [`V-206569`](rules/V-206569.md) | `SRG-APP-000226-DB-000147` | CAT II | In the event of a system failure, the DBMS must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes. |
| [`V-206570`](rules/V-206570.md) | `SRG-APP-000231-DB-000154` | CAT I | The DBMS must protect the confidentiality and integrity of all information at rest. |
| [`V-206571`](rules/V-206571.md) | `SRG-APP-000233-DB-000124` | CAT II | The DBMS must isolate security functions from non-security functions. |
| [`V-206572`](rules/V-206572.md) | `SRG-APP-000243-DB-000128` | CAT II | Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy. |
| [`V-206573`](rules/V-206573.md) | `SRG-APP-000243-DB-000373` | CAT II | The DBMS must prevent unauthorized and unintended information transfer via shared system resources. |
| [`V-206574`](rules/V-206574.md) | `SRG-APP-000243-DB-000374` | CAT II | Access to database files must be limited to relevant processes and to authorized, administrative users. |
| [`V-206575`](rules/V-206575.md) | `SRG-APP-000251-DB-000160` | CAT II | The DBMS must check the validity of all data inputs except those specifically identified by the organization. |
| [`V-206576`](rules/V-206576.md) | `SRG-APP-000251-DB-000391` | CAT II | The DBMS and associated applications must reserve the use of dynamic code execution for situations that require it. |
| [`V-206577`](rules/V-206577.md) | `SRG-APP-000251-DB-000392` | CAT II | The DBMS and associated applications, when making use of dynamic code execution, must scan input data for invalid values that may indicate a code injection attack. |
| [`V-206578`](rules/V-206578.md) | `SRG-APP-000266-DB-000162` | CAT II | The DBMS must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries. |
| [`V-206579`](rules/V-206579.md) | `SRG-APP-000267-DB-000163` | CAT II | The DBMS must reveal detailed error messages only to the ISSO, ISSM, SA and DBA. |
| [`V-206580`](rules/V-206580.md) | `SRG-APP-000295-DB-000305` | CAT II | The DBMS must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect. |
| [`V-206581`](rules/V-206581.md) | `SRG-APP-000296-DB-000306` | CAT II | The DBMS must provide logout functionality to allow the user to manually terminate a session initiated by that user. |
| [`V-206582`](rules/V-206582.md) | `SRG-APP-000311-DB-000308` | CAT II | The DBMS must associate organization-defined types of security labels having organization-defined security label values with information in storage. |
| [`V-206583`](rules/V-206583.md) | `SRG-APP-000313-DB-000309` | CAT II | The DBMS must associate organization-defined types of security labels having organization-defined security label values with information in process. |
| [`V-206584`](rules/V-206584.md) | `SRG-APP-000314-DB-000310` | CAT II | The DBMS must associate organization-defined types of security labels having organization-defined security label values with information in transmission. |
| [`V-206585`](rules/V-206585.md) | `SRG-APP-000328-DB-000301` | CAT II | The DBMS must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects. |
| [`V-206586`](rules/V-206586.md) | `SRG-APP-000340-DB-000304` | CAT II | The DBMS must prevent non-privileged users from executing privileged functions, to include disabling, circumventing, or altering implemented security safeguards/countermeasures. |
| [`V-206587`](rules/V-206587.md) | `SRG-APP-000342-DB-000302` | CAT II | Execution of software modules (to include stored procedures, functions, and triggers) with elevated privileges must be restricted to necessary cases only. |
| [`V-206591`](rules/V-206591.md) | `SRG-APP-000357-DB-000316` | CAT II | The DBMS must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements. |
| [`V-206592`](rules/V-206592.md) | `SRG-APP-000359-DB-000319` | CAT II | The DBMS must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75% of maximum audit record storage capacity. |
| [`V-206593`](rules/V-206593.md) | `SRG-APP-000360-DB-000320` | CAT II | The DBMS must provide an immediate real-time alert to appropriate support staff of all audit log failures. |
| [`V-206594`](rules/V-206594.md) | `SRG-APP-000374-DB-000322` | CAT II | The DBMS must record time stamps, in audit records and application data, that can be mapped to Coordinated Universal Time (UTC, formerly GMT). |
| [`V-206595`](rules/V-206595.md) | `SRG-APP-000375-DB-000323` | CAT II | The DBMS must generate time stamps, for audit records and application data, with a minimum granularity of one second. |
| [`V-206596`](rules/V-206596.md) | `SRG-APP-000378-DB-000365` | CAT II | The DBMS must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status. |
| [`V-206597`](rules/V-206597.md) | `SRG-APP-000380-DB-000360` | CAT II | The DBMS must enforce access restrictions associated with changes to the configuration of the DBMS or database(s). |
| [`V-206598`](rules/V-206598.md) | `SRG-APP-000381-DB-000361` | CAT II | The DBMS must produce audit records of its enforcement of access restrictions associated with changes to the configuration of the DBMS or database(s). |
| [`V-206599`](rules/V-206599.md) | `SRG-APP-000383-DB-000364` | CAT II | The DBMS must disable network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accord with the Ports, Protocols, and Services Management (PPSM) guidance. |
| [`V-206600`](rules/V-206600.md) | `SRG-APP-000389-DB-000372` | CAT II | The DBMS must require users to reauthenticate when organization-defined circumstances or situations require reauthentication. |
| [`V-206601`](rules/V-206601.md) | `SRG-APP-000400-DB-000367` | CAT II | The DBMS must prohibit the use of cached authenticators after an organization-defined time period. |
| [`V-206603`](rules/V-206603.md) | `SRG-APP-000427-DB-000385` | CAT II | The DBMS must only accept end entity certificates issued by DoW Public Key Infrastructure (PKI) or DoW-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions. |
| [`V-206604`](rules/V-206604.md) | `SRG-APP-000428-DB-000386` | CAT I | The DBMS must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components. |
| [`V-206605`](rules/V-206605.md) | `SRG-APP-000429-DB-000387` | CAT I | The DBMS must implement cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components. |
| [`V-206606`](rules/V-206606.md) | `SRG-APP-000431-DB-000388` | CAT II | The DBMS must maintain a separate execution domain for each executing process. |
| [`V-206607`](rules/V-206607.md) | `SRG-APP-000441-DB-000378` | CAT II | The DBMS must maintain the confidentiality and integrity of information during preparation for transmission. |
| [`V-206608`](rules/V-206608.md) | `SRG-APP-000442-DB-000379` | CAT II | The DBMS must maintain the confidentiality and integrity of information during reception. |
| [`V-206609`](rules/V-206609.md) | `SRG-APP-000447-DB-000393` | CAT II | When invalid inputs are received, the DBMS must behave in a predictable and documented manner that reflects organizational and system objectives. |
| [`V-206610`](rules/V-206610.md) | `SRG-APP-000454-DB-000389` | CAT II | When updates are applied to the DBMS software, any software components that have been replaced or made unnecessary must be removed. |
| [`V-206611`](rules/V-206611.md) | `SRG-APP-000456-DB-000390` | CAT II | Security-relevant software updates to the DBMS must be installed within 30 days unless the time period is directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). |
| [`V-206612`](rules/V-206612.md) | `SRG-APP-000492-DB-000332` | CAT II | The DBMS must be able to generate audit records when security objects are accessed. |
| [`V-206613`](rules/V-206613.md) | `SRG-APP-000492-DB-000333` | CAT II | The DBMS must generate audit records when unsuccessful attempts to access security objects occur. |
| [`V-206614`](rules/V-206614.md) | `SRG-APP-000494-DB-000344` | CAT II | The DBMS must generate audit records when categories of information (e.g., classification levels/security levels) are accessed. |
| [`V-206615`](rules/V-206615.md) | `SRG-APP-000494-DB-000345` | CAT II | The DBMS must generate audit records when unsuccessful attempts to access categories of information (e.g., classification levels/security levels) occur. |
| [`V-206616`](rules/V-206616.md) | `SRG-APP-000495-DB-000326` | CAT II | The DBMS must generate audit records when privileges/permissions are added. |
| [`V-206617`](rules/V-206617.md) | `SRG-APP-000495-DB-000327` | CAT II | The DBMS must generate audit records when unsuccessful attempts to add privileges/permissions occur. |
| [`V-206618`](rules/V-206618.md) | `SRG-APP-000495-DB-000328` | CAT II | The DBMS must generate audit records when privileges/permissions are modified. |
| [`V-206619`](rules/V-206619.md) | `SRG-APP-000495-DB-000329` | CAT II | The DBMS must generate audit records when unsuccessful attempts to modify privileges/permissions occur. |
| [`V-206620`](rules/V-206620.md) | `SRG-APP-000496-DB-000334` | CAT II | The DBMS must generate audit records when security objects are modified. |
| [`V-206621`](rules/V-206621.md) | `SRG-APP-000496-DB-000335` | CAT II | The DBMS must generate audit records when unsuccessful attempts to modify security objects occur. |
| [`V-206622`](rules/V-206622.md) | `SRG-APP-000498-DB-000346` | CAT II | The DBMS must generate audit records when categories of information (e.g., classification levels/security levels) are modified. |
| [`V-206623`](rules/V-206623.md) | `SRG-APP-000498-DB-000347` | CAT II | The DBMS must generate audit records when unsuccessful attempts to modify categories of information (e.g., classification levels/security levels) occur. |
| [`V-206624`](rules/V-206624.md) | `SRG-APP-000499-DB-000330` | CAT II | The DBMS must generate audit records when privileges/permissions are deleted. |
| [`V-206625`](rules/V-206625.md) | `SRG-APP-000499-DB-000331` | CAT II | The DBMS must generate audit records when unsuccessful attempts to delete privileges/permissions occur. |
| [`V-206626`](rules/V-206626.md) | `SRG-APP-000501-DB-000336` | CAT II | The DBMS must generate audit records when security objects are deleted. |
| [`V-206627`](rules/V-206627.md) | `SRG-APP-000501-DB-000337` | CAT II | The DBMS must generate audit records when unsuccessful attempts to delete security objects occur. |
| [`V-206628`](rules/V-206628.md) | `SRG-APP-000502-DB-000348` | CAT II | The DBMS must generate audit records when categories of information (e.g., classification levels/security levels) are deleted. |
| [`V-206629`](rules/V-206629.md) | `SRG-APP-000502-DB-000349` | CAT II | The DBMS must generate audit records when unsuccessful attempts to delete categories of information (e.g., classification levels/security levels) occur. |
| [`V-206630`](rules/V-206630.md) | `SRG-APP-000503-DB-000350` | CAT II | The DBMS must generate audit records when successful logons or connections occur. |
| [`V-206631`](rules/V-206631.md) | `SRG-APP-000503-DB-000351` | CAT II | The DBMS must generate audit records when unsuccessful logons or connection attempts occur. |
| [`V-206632`](rules/V-206632.md) | `SRG-APP-000504-DB-000354` | CAT II | The DBMS must generate audit records for all privileged activities or other system-level access. |
| [`V-206633`](rules/V-206633.md) | `SRG-APP-000504-DB-000355` | CAT II | The DBMS must generate audit records when unsuccessful attempts to execute privileged activities or other system-level access occur. |
| [`V-206634`](rules/V-206634.md) | `SRG-APP-000505-DB-000352` | CAT II | The DBMS must generate audit records showing starting and ending time for user access to the database(s). |
| [`V-206635`](rules/V-206635.md) | `SRG-APP-000506-DB-000353` | CAT II | The DBMS must generate audit records when concurrent logons/connections by the same user from different workstations occur. |
| [`V-206636`](rules/V-206636.md) | `SRG-APP-000507-DB-000356` | CAT II | The DBMS must be able to generate audit records when successful accesses to objects occur. |
| [`V-206637`](rules/V-206637.md) | `SRG-APP-000507-DB-000357` | CAT II | The DBMS must generate audit records when unsuccessful accesses to objects occur. |
| [`V-206638`](rules/V-206638.md) | `SRG-APP-000508-DB-000358` | CAT II | The DBMS must generate audit records for all direct access to the database(s). |
| [`V-206639`](rules/V-206639.md) | `SRG-APP-000514-DB-000381` | CAT II | The DBMS must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to provision digital signatures. |
| [`V-206640`](rules/V-206640.md) | `SRG-APP-000514-DB-000382` | CAT II | The DBMS must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to generate and validate cryptographic hashes. |
| [`V-206641`](rules/V-206641.md) | `SRG-APP-000514-DB-000383` | CAT II | The DBMS must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to protect unclassified information requiring confidentiality and cryptographic protection, in accordance with the data owners requirements. |
| [`V-206642`](rules/V-206642.md) | `SRG-APP-000515-DB-000318` | CAT II | The DBMS must off-load audit data to a separate log management facility; this shall be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for stand-alone systems. |
| [`V-206643`](rules/V-206643.md) | `SRG-APP-000516-DB-000363` | CAT II | The DBMS must be configured in accordance with the security configuration settings based on DoW security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs. |
| [`V-233495`](rules/V-233495.md) | `SRG-APP-000416-DB-000380` | CAT I | The DBMS must use NSA-approved cryptography to protect classified information in accordance with the data owner's requirements. |
| [`V-263602`](rules/V-263602.md) | `SRG-APP-000700-DB-000100` | CAT II | The DBMS must disable accounts when the accounts have expired. |
| [`V-263603`](rules/V-263603.md) | `SRG-APP-000705-DB-000110` | CAT II | The DBMS must disable accounts when the accounts are no longer associated to a user. |
| [`V-263604`](rules/V-263604.md) | `SRG-APP-000745-DB-000120` | CAT II | The DBMS must implement the capability to centrally review and analyze audit records from multiple components within the system. |
| [`V-263605`](rules/V-263605.md) | `SRG-APP-000795-DB-000130` | CAT II | The DBMS must alert organization-defined personnel or roles upon detection of unauthorized access, modification, or deletion of audit information. |
| [`V-263606`](rules/V-263606.md) | `SRG-APP-000810-DB-000150` | CAT II | The DBMS must prevent the installation of organization-defined software and firmware components without verification that the component has been digitally signed using a certificate recognized and approved by the organization. |
| [`V-263607`](rules/V-263607.md) | `SRG-APP-000815-DB-000160` | CAT II | The DBMS must require users to be individually authenticated before granting access to the shared accounts or resources. |
| [`V-263608`](rules/V-263608.md) | `SRG-APP-000820-DB-000170` | CAT II | The DBMS must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access. |
| [`V-263609`](rules/V-263609.md) | `SRG-APP-000825-DB-000180` | CAT II | The DBMS must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements. |
| [`V-263610`](rules/V-263610.md) | `SRG-APP-000830-DB-000190` | CAT II | The DBMS must, for password-based authentication, maintain a list of commonly used, expected, or compromised passwords on an organization-defined frequency. |
| [`V-263611`](rules/V-263611.md) | `SRG-APP-000835-DB-000200` | CAT II | The DBMS must, for password-based authentication, update the list of passwords on an organization-defined frequency. |
| [`V-263612`](rules/V-263612.md) | `SRG-APP-000840-DB-000210` | CAT II | The DBMS must, for password-based authentication, update the list of passwords when organizational passwords are suspected to have been compromised directly or indirectly. |
| [`V-263613`](rules/V-263613.md) | `SRG-APP-000845-DB-000220` | CAT II | The DBMS must, for password-based authentication, verify that when users create or update passwords, the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a). |
| [`V-263614`](rules/V-263614.md) | `SRG-APP-000855-DB-000240` | CAT II | The DBMS must, for password-based authentication, require immediate selection of a new password upon account recovery. |
| [`V-263615`](rules/V-263615.md) | `SRG-APP-000860-DB-000250` | CAT II | The DBMS must, for password-based authentication, allow user selection of long passwords and passphrases, including spaces and all printable characters. |
| [`V-263616`](rules/V-263616.md) | `SRG-APP-000865-DB-000260` | CAT II | The DBMS must, for password-based authentication, employ automated tools to assist the user in selecting strong password authenticators. |
| [`V-263617`](rules/V-263617.md) | `SRG-APP-000875-DB-000280` | CAT II | The DBMS must, for public key-based authentication, implement a local cache of revocation data to support path discovery and validation. |
| [`V-263618`](rules/V-263618.md) | `SRG-APP-000880-DB-000290` | CAT II | The DBMS must protect nonlocal maintenance sessions by separating the maintenance session from other network sessions with the system by logically separated communications paths. |
| [`V-263619`](rules/V-263619.md) | `SRG-APP-000910-DB-000300` | CAT II | The DBMS must include only approved trust anchors in trust stores or certificate stores managed by the organization. |
| [`V-263620`](rules/V-263620.md) | `SRG-APP-000915-DB-000310` | CAT II | The DBMS must provide protected storage for cryptographic keys with organization-defined safeguards and/or hardware protected key store. |
| [`V-263621`](rules/V-263621.md) | `SRG-APP-000920-DB-000320` | CAT II | The DBMS must synchronize system clocks within and between systems or system components. |
| [`V-263622`](rules/V-263622.md) | `SRG-APP-000925-DB-000330` | CAT II | The DBMS must compare the internal system clocks on an organization-defined frequency with organization-defined authoritative time source. |
| [`V-278969`](rules/V-278969.md) | `SRG-APP-001035-DB-000323` | CAT I | The DBMS must be a version supported by the vendor. |
