# Web Server Security Requirements Guide

Release: 3 Benchmark Date: 08 Apr 2024. Accepted 2024-04-09.

| | |
| --- | --- |
| Benchmark | `Web_Server_SRG` |
| Rules | **102** |
| CAT I | 3 |
| CAT II | 98 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-206350`](rules/V-206350.md) | `SRG-APP-000001-WSR-000001` | CAT II | The web server must limit the number of allowed simultaneous session requests. |
| [`V-206351`](rules/V-206351.md) | `SRG-APP-000001-WSR-000002` | CAT II | The web server must perform server-side session management. |
| [`V-206352`](rules/V-206352.md) | `SRG-APP-000014-WSR-000006` | CAT II | The web server must use encryption strength in accordance with the categorization of data hosted by the web server when remote connections are provided. |
| [`V-206353`](rules/V-206353.md) | `SRG-APP-000015-WSR-000014` | CAT II | The web server must use cryptography to protect the integrity of remote sessions. |
| [`V-206354`](rules/V-206354.md) | `SRG-APP-000016-WSR-000005` | CAT II | The web server must generate information to be used by external applications or entities to monitor and control remote access. |
| [`V-206355`](rules/V-206355.md) | `SRG-APP-000033-WSR-000169` | CAT II | The web server must enforce approved authorizations for logical access to hosted applications and resources in accordance with applicable access control policies. |
| [`V-206356`](rules/V-206356.md) | `SRG-APP-000089-WSR-000047` | CAT II | The web server must generate, at a minimum, log records for system startup and shutdown, system access, and system authentication events. |
| [`V-206357`](rules/V-206357.md) | `SRG-APP-000092-WSR-000055` | CAT II | The web server must initiate session logging upon start up. |
| [`V-206359`](rules/V-206359.md) | `SRG-APP-000095-WSR-000056` | CAT II | The web server must produce log records containing sufficient information to establish what type of events occurred. |
| [`V-206360`](rules/V-206360.md) | `SRG-APP-000096-WSR-000057` | CAT II | The web server must produce log records containing sufficient information to establish when (date and time) events occurred. |
| [`V-206361`](rules/V-206361.md) | `SRG-APP-000097-WSR-000058` | CAT II | The web server must produce log records containing sufficient information to establish where within the web server the events occurred. |
| [`V-206362`](rules/V-206362.md) | `SRG-APP-000098-WSR-000059` | CAT II | The web server must produce log records containing sufficient information to establish the source of events. |
| [`V-206363`](rules/V-206363.md) | `SRG-APP-000098-WSR-000060` | CAT II | A web server, behind a load balancer or proxy server, must produce log records containing the client IP information as the source and destination and not the load balancer or proxy IP information with each event. |
| [`V-206364`](rules/V-206364.md) | `SRG-APP-000099-WSR-000061` | CAT II | The web server must produce log records that contain sufficient information to establish the outcome (success or failure) of events. |
| [`V-206365`](rules/V-206365.md) | `SRG-APP-000100-WSR-000064` | CAT II | The web server must produce log records containing sufficient information to establish the identity of any user/subject or process associated with an event. |
| [`V-206366`](rules/V-206366.md) | `SRG-APP-000108-WSR-000166` | CAT II | The web server must use a logging mechanism that is configured to alert the ISSO and SA in the event of a processing failure. |
| [`V-206367`](rules/V-206367.md) | `SRG-APP-000116-WSR-000066` | CAT II | The web server must use the internal system clock to generate time stamps for log records. |
| [`V-206368`](rules/V-206368.md) | `SRG-APP-000118-WSR-000068` | CAT II | Web server log files must only be accessible by privileged users. |
| [`V-206369`](rules/V-206369.md) | `SRG-APP-000119-WSR-000069` | CAT II | The log information from the web server must be protected from unauthorized modification. |
| [`V-206370`](rules/V-206370.md) | `SRG-APP-000120-WSR-000070` | CAT II | The log information from the web server must be protected from unauthorized deletion. |
| [`V-206371`](rules/V-206371.md) | `SRG-APP-000125-WSR-000071` | CAT II | The log data and records from the web server must be backed up onto a different system or media. |
| [`V-206372`](rules/V-206372.md) | `SRG-APP-000131-WSR-000051` | CAT II | All web server files must be verified for their integrity (e.g., checksums and hashes) before becoming part of the production web server. |
| [`V-206373`](rules/V-206373.md) | `SRG-APP-000131-WSR-000073` | CAT II | Expansion modules must be fully reviewed, tested, and signed before they can exist on a production web server. |
| [`V-206374`](rules/V-206374.md) | `SRG-APP-000141-WSR-000015` | CAT II | The web server must not perform user management for hosted applications. |
| [`V-206375`](rules/V-206375.md) | `SRG-APP-000141-WSR-000075` | CAT II | The web server must only contain services and functions necessary for operation. |
| [`V-206376`](rules/V-206376.md) | `SRG-APP-000141-WSR-000076` | CAT II | The web server must not be a proxy server. |
| [`V-206377`](rules/V-206377.md) | `SRG-APP-000141-WSR-000077` | CAT II | The web server must provide install options to exclude the installation of documentation, sample code, example applications, and tutorials. |
| [`V-206378`](rules/V-206378.md) | `SRG-APP-000141-WSR-000078` | CAT II | Web server accounts not utilized by installed features (i.e., tools, utilities, specific services, etc.) must not be created and must be deleted when the web server feature is uninstalled. |
| [`V-206379`](rules/V-206379.md) | `SRG-APP-000141-WSR-000080` | CAT II | The web server must provide install options to exclude installation of utility programs, services, plug-ins, and modules not necessary for operation. |
| [`V-206380`](rules/V-206380.md) | `SRG-APP-000141-WSR-000081` | CAT II | The web server must have Multipurpose Internet Mail Extensions (MIME) that invoke OS shell programs disabled. |
| [`V-206381`](rules/V-206381.md) | `SRG-APP-000141-WSR-000082` | CAT II | The web server must allow the mappings to unused and vulnerable scripts to be removed. |
| [`V-206382`](rules/V-206382.md) | `SRG-APP-000141-WSR-000083` | CAT II | The web server must have resource mappings set to disable the serving of certain file types. |
| [`V-206383`](rules/V-206383.md) | `SRG-APP-000141-WSR-000085` | CAT II | The web server must have Web Distributed Authoring (WebDAV) disabled. |
| [`V-206384`](rules/V-206384.md) | `SRG-APP-000141-WSR-000086` | CAT II | The web server must protect system resources and privileged operations from hosted applications. |
| [`V-206385`](rules/V-206385.md) | `SRG-APP-000141-WSR-000087` | CAT II | Users and scripts running on behalf of users must be contained to the document root or home directory tree of the web server. |
| [`V-206386`](rules/V-206386.md) | `SRG-APP-000142-WSR-000089` | CAT II | The web server must be configured to use a specified IP address and port. |
| [`V-206387`](rules/V-206387.md) | `SRG-APP-000172-WSR-000104` | CAT II | The web server must encrypt passwords during transmission. |
| [`V-206388`](rules/V-206388.md) | `SRG-APP-000175-WSR-000095` | CAT II | The web server must perform RFC 5280-compliant certification path validation. |
| [`V-206389`](rules/V-206389.md) | `SRG-APP-000176-WSR-000096` | CAT II | Only authenticated system administrators or the designated PKI Sponsor for the web server must have access to the web servers private key. |
| [`V-206390`](rules/V-206390.md) | `SRG-APP-000179-WSR-000110` | CAT I | The web server must use cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting stored data. |
| [`V-206391`](rules/V-206391.md) | `SRG-APP-000179-WSR-000111` | CAT II | The web server must use cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for such authentication. |
| [`V-206392`](rules/V-206392.md) | `SRG-APP-000206-WSR-000128` | CAT II | A web server utilizing mobile code must meet DoD-defined mobile code requirements. |
| [`V-206393`](rules/V-206393.md) | `SRG-APP-000211-WSR-000030` | CAT II | Web server accounts accessing the directory tree, the shell, or other operating system functions and utilities must only be administrative accounts. |
| [`V-206394`](rules/V-206394.md) | `SRG-APP-000211-WSR-000031` | CAT II | Anonymous user access to the web server application directories must be prohibited. |
| [`V-206395`](rules/V-206395.md) | `SRG-APP-000211-WSR-000129` | CAT II | The web server must separate the hosted applications from hosted web server management functionality. |
| [`V-206396`](rules/V-206396.md) | `SRG-APP-000220-WSR-000201` | CAT II | The web server must invalidate session identifiers upon hosted application user logout or other session termination. |
| [`V-206397`](rules/V-206397.md) | `SRG-APP-000223-WSR-000011` | CAT II | Cookies exchanged between the web server and client, such as session cookies, must have security settings that disallow cookie access outside the originating web server and hosted application. |
| [`V-206398`](rules/V-206398.md) | `SRG-APP-000223-WSR-000145` | CAT II | The web server must accept only system-generated session identifiers. |
| [`V-206399`](rules/V-206399.md) | `SRG-APP-000224-WSR-000135` | CAT I | The web server must generate a unique session identifier for each session using a FIPS 140-2 approved random number generator. |
| [`V-206400`](rules/V-206400.md) | `SRG-APP-000224-WSR-000136` | CAT II | The web server must generate unique session identifiers that cannot be reliably reproduced. |
| [`V-206401`](rules/V-206401.md) | `SRG-APP-000224-WSR-000137` | CAT II | The web server must generate a session ID long enough that it cannot be guessed through brute force. |
| [`V-206402`](rules/V-206402.md) | `SRG-APP-000224-WSR-000138` | CAT II | The web server must generate a session ID using as much of the character set as possible to reduce the risk of brute force. |
| [`V-206403`](rules/V-206403.md) | `SRG-APP-000224-WSR-000139` | CAT II | The web server must generate unique session identifiers with definable entropy. |
| [`V-206404`](rules/V-206404.md) | `SRG-APP-000225-WSR-000074` | CAT II | The web server must augment re-creation to a stable and known baseline. |
| [`V-206405`](rules/V-206405.md) | `SRG-APP-000225-WSR-000140` | CAT II | The web server must be built to fail to a known safe state if system initialization fails, shutdown fails, or aborts fail. |
| [`V-206406`](rules/V-206406.md) | `SRG-APP-000225-WSR-000141` | CAT II | The web server must provide a clustering capability. |
| [`V-206407`](rules/V-206407.md) | `SRG-APP-000231-WSR-000144` | CAT II | Information at rest must be encrypted using a DoD-accepted algorithm to protect the confidentiality and integrity of the information. |
| [`V-206408`](rules/V-206408.md) | `SRG-APP-000233-WSR-000146` | CAT II | The web server document directory must be in a separate partition from the web servers system files. |
| [`V-206409`](rules/V-206409.md) | `SRG-APP-000246-WSR-000149` | CAT II | The web server must restrict the ability of users to launch Denial of Service (DoS) attacks against other information systems or networks. |
| [`V-206410`](rules/V-206410.md) | `SRG-APP-000251-WSR-000157` | CAT II | The web server must limit the character set used for data entry. |
| [`V-206411`](rules/V-206411.md) | `SRG-APP-000266-WSR-000142` | CAT II | The web server must display a default hosted application web page, not a directory listing, when a requested web page cannot be found. |
| [`V-206412`](rules/V-206412.md) | `SRG-APP-000266-WSR-000159` | CAT II | Warning and error messages displayed to clients must be modified to minimize the identity of the web server, patches, loaded modules, and directory paths. |
| [`V-206413`](rules/V-206413.md) | `SRG-APP-000266-WSR-000160` | CAT II | Debugging and trace information used to diagnose the web server must be disabled. |
| [`V-206414`](rules/V-206414.md) | `SRG-APP-000295-WSR-000012` | CAT II | The web server must set an absolute session timeout value of eight hours or less. |
| [`V-206415`](rules/V-206415.md) | `SRG-APP-000295-WSR-000134` | CAT II | The web server must set an inactive timeout for sessions. |
| [`V-206416`](rules/V-206416.md) | `SRG-APP-000315-WSR-000003` | CAT II | Remote access to the web server must follow access policy or work in conjunction with enterprise tools designed to enforce policy requirements. |
| [`V-206417`](rules/V-206417.md) | `SRG-APP-000315-WSR-000004` | CAT II | The web server must restrict inbound connections from nonsecure zones. |
| [`V-206418`](rules/V-206418.md) | `SRG-APP-000316-WSR-000170` | CAT II | The web server must provide the capability to immediately disconnect or disable remote access to the hosted applications. |
| [`V-206419`](rules/V-206419.md) | `SRG-APP-000340-WSR-000029` | CAT II | Non-privileged accounts on the hosting system must only access web server security-relevant information and functions through a distinct administrative account. |
| [`V-206420`](rules/V-206420.md) | `SRG-APP-000356-WSR-000007` | CAT II | A web server that is part of a web server cluster must route all remote management through a centrally managed access control point. |
| [`V-206421`](rules/V-206421.md) | `SRG-APP-000357-WSR-000150` | CAT II | The web server must use a logging mechanism that is configured to allocate log record storage capacity large enough to accommodate the logging requirements of the web server. |
| [`V-206422`](rules/V-206422.md) | `SRG-APP-000358-WSR-000063` | CAT II | The web server must not impede the ability to write specified log record content to an audit log server. |
| [`V-206423`](rules/V-206423.md) | `SRG-APP-000358-WSR-000163` | CAT II | The web server must be configurable to integrate with an organizations security infrastructure. |
| [`V-206424`](rules/V-206424.md) | `SRG-APP-000359-WSR-000065` | CAT II | The web server must use a logging mechanism that is configured to provide a warning to the ISSO and SA when allocated record storage volume reaches 75% of maximum log record storage capacity. |
| [`V-206425`](rules/V-206425.md) | `SRG-APP-000374-WSR-000172` | CAT II | The web server must generate log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT). |
| [`V-206426`](rules/V-206426.md) | `SRG-APP-000375-WSR-000171` | CAT II | The web server must record time stamps for log records to a minimum granularity of one second. |
| [`V-206427`](rules/V-206427.md) | `SRG-APP-000380-WSR-000072` | CAT II | The web server application, libraries, and configuration files must only be accessible to privileged users. |
| [`V-206428`](rules/V-206428.md) | `SRG-APP-000383-WSR-000175` | CAT II | The web server must prohibit or restrict the use of nonsecure or unnecessary ports, protocols, modules, and/or services. |
| [`V-206430`](rules/V-206430.md) | `SRG-APP-000427-WSR-000186` | CAT II | The web server must only accept client certificates (user and machine) issued by DOD PKI or DOD-approved PKI Certificate Authorities (CAs). |
| [`V-206431`](rules/V-206431.md) | `SRG-APP-000429-WSR-000113` | CAT II | The web server must encrypt user identifiers and passwords. |
| [`V-206432`](rules/V-206432.md) | `SRG-APP-000435-WSR-000147` | CAT II | The web server must be protected from being stopped by a non-privileged user. |
| [`V-206433`](rules/V-206433.md) | `SRG-APP-000435-WSR-000148` | CAT II | The web server must be tuned to handle the operational requirements of the hosted application. |
| [`V-206434`](rules/V-206434.md) | `SRG-APP-000439-WSR-000151` | CAT I | The web server must employ cryptographic mechanisms (TLS/DTLS/SSL) preventing the unauthorized disclosure of information during transmission. |
| [`V-206435`](rules/V-206435.md) | `SRG-APP-000439-WSR-000152` | CAT II | Web server session IDs must be sent to the client using SSL/TLS. |
| [`V-206436`](rules/V-206436.md) | `SRG-APP-000439-WSR-000153` | CAT II | Web server cookies, such as session cookies, sent to the client using SSL/TLS must not be compressed. |
| [`V-206437`](rules/V-206437.md) | `SRG-APP-000439-WSR-000154` | CAT II | Cookies exchanged between the web server and the client, such as session cookies, must have cookie properties set to prohibit client-side scripts from reading the cookie data. |
| [`V-206438`](rules/V-206438.md) | `SRG-APP-000439-WSR-000155` | CAT II | Cookies exchanged between the web server and the client, such as session cookies, must have cookie properties set to force the encryption of cookies. |
| [`V-206439`](rules/V-206439.md) | `SRG-APP-000439-WSR-000156` | CAT II | A web server must maintain the confidentiality of controlled information during transmission through the use of an approved TLS version. |
| [`V-206440`](rules/V-206440.md) | `SRG-APP-000439-WSR-000188` | CAT II | The web server must remove all export ciphers to protect the confidentiality and integrity of transmitted information. |
| [`V-206441`](rules/V-206441.md) | `SRG-APP-000441-WSR-000181` | CAT II | The web server must maintain the confidentiality and integrity of information during preparation for transmission. |
| [`V-206442`](rules/V-206442.md) | `SRG-APP-000442-WSR-000182` | CAT II | The web server must maintain the confidentiality and integrity of information during reception. |
| [`V-206443`](rules/V-206443.md) | `SRG-APP-000456-WSR-000187` | CAT II | The web server must install security-relevant software updates within the configured time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). |
| [`V-206444`](rules/V-206444.md) | `SRG-APP-000516-WSR-000079` | CAT II | All accounts installed with the web server software and tools must have passwords assigned and default passwords changed. |
| [`V-206445`](rules/V-206445.md) | `SRG-APP-000516-WSR-000174` | CAT II | The web server must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs. |
| [`V-239371`](rules/V-239371.md) | `SRG-APP-000416-WSR-000118` | CAT II | The web server must implement required cryptographic protections using cryptographic modules complying with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance when encrypting data that must be compartmentalized. |
| [`V-260896`](rules/V-260896.md) | `SRG-APP-000219-WSR-000190` | CAT II | The web server must restrict a consistent inbound source IP for the entire management session. |
| [`V-260897`](rules/V-260897.md) | `SRG-APP-000219-WSR-000191` | info | The web server must restrict a consistent inbound source IP for the entire user session. |
| [`V-260898`](rules/V-260898.md) | `SRG-APP-000439-WSR-000192` | CAT II | The web server must use HTTP/2, at a minimum. |
| [`V-260899`](rules/V-260899.md) | `SRG-APP-000439-WSR-000193` | CAT II | The web server must disable HTTP/1.x downgrading. |
| [`V-260900`](rules/V-260900.md) | `SRG-APP-000251-WSR-000194` | CAT II | The web server must interpret and normalize ambiguous HTTP requests or terminate the TCP connection. |
| [`V-260901`](rules/V-260901.md) | `SRG-APP-000251-WSR-000195` | CAT II | The web server must terminate the connection if server-level exceptions are triggered when handling requests to prevent HTTP request smuggling attacks. |
| [`V-260902`](rules/V-260902.md) | `SRG-APP-000439-WSR-000196` | CAT II | The web server must only use forward proxies that route HTTP/2 requests upstream. |
