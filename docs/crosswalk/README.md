# SRG to NIST SP 800-53 crosswalk

Every SRG rule cites one or more CCIs, and the DISA CCI list maps each CCI to NIST SP 800-53 Rev 5. This crosswalk is the join of the two. No cross-reference here is hand-authored: each follows from the pinned sources, and it inherits DISA's judgement, errors included.

| Input | Revision |
| --- | --- |
| DISA CCI list | 2025-01-23 |
| NIST SP 800-53 Rev 5 catalogue | 5.2.0 |
| Application Programming Interface (API) Security Requirements Guide | V1R1 |
| Application Security and Development Security Technical Implementation Guide | V6R5 |
| Application Server Security Requirements Guide | V4R6 |
| Container Platform Security Requirements Guide | V2R5 |
| Database Security Requirements Guide | V4R6 |
| General Purpose Operating System Security Requirements Guide | V3R4 |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | V2R10 |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | V2R7 |
| Web Server Security Requirements Guide | V4R5 |

Each input is pinned by SHA-256 in [`artifacts/sources.json`](../../artifacts/sources.json), and the generator refuses to map against one that does not match. The machine-readable form is [`artifacts/crosswalk.json`](../../artifacts/crosswalk.json).

## Coverage

| Catalogue | Rules | CCIs cited | Controls reached | Of which High baseline |
| --- | ---: | ---: | ---: | ---: |
| [Application Programming Interface (API) Security Requirements Guide](../srg/application-programming-interface-api-srg/README.md) | 65 | 41 | 28 | 17 |
| [Application Security and Development Security Technical Implementation Guide](../srg/application-security-and-development-stig/README.md) | 286 | 225 | 129 | 88 |
| [Application Server Security Requirements Guide](../srg/application-server-srg/README.md) | 137 | 117 | 81 | 53 |
| [Container Platform Security Requirements Guide](../srg/container-platform-srg/README.md) | 188 | 127 | 80 | 60 |
| [Database Security Requirements Guide](../srg/database-srg/README.md) | 142 | 100 | 62 | 40 |
| [General Purpose Operating System Security Requirements Guide](../srg/general-purpose-operating-system-srg/README.md) | 202 | 157 | 97 | 66 |
| [Red Hat Enterprise Linux 9 Security Technical Implementation Guide](../srg/red-hat-enterprise-linux-9-stig/README.md) | 445 | 161 | 81 | 60 |
| [Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide](../srg/red-hat-openshift-container-platform-4-x-stig/README.md) | 83 | 119 | 65 | 51 |
| [Web Server Security Requirements Guide](../srg/web-server-srg/README.md) | 126 | 83 | 54 | 37 |

## Findings

| Catalogue | Group ID | CCI | Finding |
| --- | --- | --- | --- |
| Application Security and Development Security Technical Implementation Guide | `V-222408` | `CCI-002142` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (10), which Rev 5 withdraws |
| Application Security and Development Security Technical Implementation Guide | `V-222417` | `CCI-001683` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Application Security and Development Security Technical Implementation Guide | `V-222418` | `CCI-001684` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Application Security and Development Security Technical Implementation Guide | `V-222419` | `CCI-001685` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Application Security and Development Security Technical Implementation Guide | `V-222420` | `CCI-001686` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Application Security and Development Security Technical Implementation Guide | `V-222422` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Application Security and Development Security Technical Implementation Guide | `V-222510` | `CCI-001812` | No Rev 5 reference; DISA maps it only to Rev 4 CM-11 (2) |
| Application Security and Development Security Technical Implementation Guide | `V-222512` | `CCI-001814` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (1) |
| Application Security and Development Security Technical Implementation Guide | `V-222513` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Application Security and Development Security Technical Implementation Guide | `V-222527` | `CCI-000767` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (3), which Rev 5 withdraws |
| Application Security and Development Security Technical Implementation Guide | `V-222528` | `CCI-000768` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (4), which Rev 5 withdraws |
| Application Security and Development Security Technical Implementation Guide | `V-222529` | `CCI-000770` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (5) |
| Application Security and Development Security Technical Implementation Guide | `V-222531` | `CCI-001942` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (9), which Rev 5 withdraws |
| Application Security and Development Security Technical Implementation Guide | `V-222535` | `CCI-000795` | No Rev 5 reference; DISA maps it only to Rev 4 IA-4 e |
| Application Security and Development Security Technical Implementation Guide | `V-222536` | `CCI-000205` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Application Security and Development Security Technical Implementation Guide | `V-222537` | `CCI-000192` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Application Security and Development Security Technical Implementation Guide | `V-222538` | `CCI-000193` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Application Security and Development Security Technical Implementation Guide | `V-222539` | `CCI-000194` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Application Security and Development Security Technical Implementation Guide | `V-222540` | `CCI-001619` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Application Security and Development Security Technical Implementation Guide | `V-222541` | `CCI-000195` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (b) |
| Application Security and Development Security Technical Implementation Guide | `V-222542` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Application Security and Development Security Technical Implementation Guide | `V-222544` | `CCI-000198` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Application Security and Development Security Technical Implementation Guide | `V-222545` | `CCI-000199` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Application Security and Development Security Technical Implementation Guide | `V-222553` | `CCI-001991` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (2) (d) |
| Application Security and Development Security Technical Implementation Guide | `V-222559` | `CCI-002011` | No Rev 5 reference; DISA maps it only to Rev 4 IA-8 (2) |
| Application Security and Development Security Technical Implementation Guide | `V-222560` | `CCI-002014` | No Rev 5 reference; DISA maps it only to Rev 4 IA-8 (4) |
| Application Security and Development Security Technical Implementation Guide | `V-222622` | `CCI-001872` | No Rev 5 reference; DISA maps it only to Rev 4 AU-6 (10), which Rev 5 withdraws |
| Application Security and Development Security Technical Implementation Guide | `V-222627` | `CCI-000363` | No Rev 5 reference; DISA maps it only to Rev 4 CM-6 a |
| Application Security and Development Security Technical Implementation Guide | `V-222639` | `CCI-000540` | No Rev 5 reference; DISA maps it only to Rev 4 CP-9 (d) |
| Application Security and Development Security Technical Implementation Guide | `V-222640` | `CCI-000540` | No Rev 5 reference; DISA maps it only to Rev 4 CP-9 (d) |
| Application Security and Development Security Technical Implementation Guide | `V-222642` | `CCI-002367` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (7) |
| Application Security and Development Security Technical Implementation Guide | `V-222655` | `CCI-003256` | No Rev 5 reference; DISA maps it only to Rev 4 SA-15 (4), which Rev 5 withdraws |
| Application Security and Development Security Technical Implementation Guide | `V-222660` | `CCI-003374` | No Rev 5 reference; DISA maps it only to Rev 4 SA-22 b |
| Application Security and Development Security Technical Implementation Guide | `V-222667` | `CCI-002386` | No Rev 5 reference; DISA maps it only to Rev 4 SC-5 |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257799` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257819` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257820` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257821` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257822` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257825` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257838` | `CCI-001948` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (11), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257943` | `CCI-001891` | No Rev 5 reference; DISA maps it only to Rev 4 AU-8 (1) (a), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257944` | `CCI-001891` | No Rev 5 reference; DISA maps it only to Rev 4 AU-8 (1) (a), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257945` | `CCI-001891` | No Rev 5 reference; DISA maps it only to Rev 4 AU-8 (1) (a), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257945` | `CCI-002046` | No Rev 5 reference; DISA maps it only to Rev 4 AU-8 (1) (b), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257983` | `CCI-000767` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257983` | `CCI-000768` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (4), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-257985` | `CCI-000770` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (5) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258019` | `CCI-000058` | No Rev 5 reference; DISA maps it only to Rev 4 AC-11 a |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258020` | `CCI-000058` | No Rev 5 reference; DISA maps it only to Rev 4 AC-11 a |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258021` | `CCI-000058` | No Rev 5 reference; DISA maps it only to Rev 4 AC-11 a |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258022` | `CCI-000058` | No Rev 5 reference; DISA maps it only to Rev 4 AC-11 a |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258041` | `CCI-000199` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258042` | `CCI-000199` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258049` | `CCI-000795` | No Rev 5 reference; DISA maps it only to Rev 4 IA-4 e |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258091` | `CCI-000192` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258097` | `CCI-000192` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258097` | `CCI-000193` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258099` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258100` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258101` | `CCI-000192` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258101` | `CCI-000193` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258101` | `CCI-000194` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258101` | `CCI-000195` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (b) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258101` | `CCI-000205` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258101` | `CCI-001619` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258102` | `CCI-000193` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258103` | `CCI-000194` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258104` | `CCI-000198` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258105` | `CCI-000198` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258107` | `CCI-000205` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258109` | `CCI-001619` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258111` | `CCI-000192` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258112` | `CCI-000195` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (b) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258113` | `CCI-000195` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (b) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258114` | `CCI-000195` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (b) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258115` | `CCI-000195` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (b) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258116` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258117` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258121` | `CCI-000767` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (3), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258121` | `CCI-000768` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (4), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258121` | `CCI-000770` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (5) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258121` | `CCI-001942` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (9), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258122` | `CCI-001948` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (11), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258123` | `CCI-001948` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (11), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258124` | `CCI-001948` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (11), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258125` | `CCI-001948` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (11), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258126` | `CCI-001948` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (11), which Rev 5 withdraws |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258131` | `CCI-001991` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (2) (d) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258151` | `CCI-001814` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (1) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258152` | `CCI-001814` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (1) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258217` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258218` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258219` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258220` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258221` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258222` | `CCI-001683` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258222` | `CCI-001684` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258222` | `CCI-001685` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258222` | `CCI-001686` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258222` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258223` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258231` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Red Hat Enterprise Linux 9 Security Technical Implementation Guide | `V-258233` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257511` | `CCI-001683` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257511` | `CCI-001684` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257511` | `CCI-001685` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257511` | `CCI-001686` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257511` | `CCI-002132` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (4) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257513` | `CCI-000770` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (5) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257513` | `CCI-001812` | No Rev 5 reference; DISA maps it only to Rev 4 CM-11 (2) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257537` | `CCI-001749` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (3), which Rev 5 withdraws |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000192` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000193` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000194` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000195` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (b) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000196` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (c) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000198` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000199` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (d) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000205` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000767` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (3), which Rev 5 withdraws |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000768` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (4), which Rev 5 withdraws |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-000795` | No Rev 5 reference; DISA maps it only to Rev 4 IA-4 e |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-001619` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (1) (a) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-001942` | No Rev 5 reference; DISA maps it only to Rev 4 IA-2 (9), which Rev 5 withdraws |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-001991` | No Rev 5 reference; DISA maps it only to Rev 4 IA-5 (2) (d) |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257543` | `CCI-002142` | No Rev 5 reference; DISA maps it only to Rev 4 AC-2 (10), which Rev 5 withdraws |
| Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | `V-257560` | `CCI-001814` | No Rev 5 reference; DISA maps it only to Rev 4 CM-5 (1) |

## Controls

Rule counts per catalogue. A control outside the High baseline is still reached by an SRG; the baseline does not select it.

| Control | Title | High | Application Programming Interface (API) Security Requirements Guide | Application Security and Development Security Technical Implementation Guide | Application Server Security Requirements Guide | Container Platform Security Requirements Guide | Database Security Requirements Guide | General Purpose Operating System Security Requirements Guide | Red Hat Enterprise Linux 9 Security Technical Implementation Guide | Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide | Web Server Security Requirements Guide |
| --- | --- | :-: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [AC-2](controls/ac-2.md) | Account Management | Yes |  | 1 |  |  |  |  |  |  |  |
| [AC-2(1)](controls/ac-2.1.md) | Automated System Account Management | Yes |  | 6 |  | 6 | 1 | 6 | 8 | 3 |  |
| [AC-2(2)](controls/ac-2.2.md) | Automated Temporary and Emergency Account Management | Yes |  | 1 |  | 2 |  | 2 | 1 | 1 |  |
| [AC-2(3)](controls/ac-2.3.md) | Disable Accounts | Yes |  | 3 | 2 | 3 | 2 | 2 | 1 | 1 | 2 |
| [AC-2(4)](controls/ac-2.4.md) | Automated Audit Actions | Yes |  | 5 |  | 5 |  | 5 | 7 | 4 |  |
| [AC-2(11)](controls/ac-2.11.md) | Usage Conditions | Yes |  |  |  | 1 |  |  |  | 1 |  |
| [AC-3](controls/ac-3.md) | Access Enforcement | Yes | 1 | 1 | 1 | 3 | 1 | 1 | 4 | 1 | 1 |
| [AC-3(4)](controls/ac-3.4.md) | Discretionary Access Control | No |  | 1 |  |  | 1 | 3 | 3 |  |  |
| [AC-3(7)](controls/ac-3.7.md) | Role-based Access Control | No |  |  | 1 |  |  | 1 |  |  |  |
| [AC-3(13)](controls/ac-3.13.md) | Attribute-based Access Control | No |  |  | 1 |  |  | 1 |  |  |  |
| [AC-4](controls/ac-4.md) | Information Flow Enforcement | Yes |  | 2 |  | 2 |  |  |  | 2 |  |
| [AC-4(17)](controls/ac-4.17.md) | Domain Authentication | No |  |  | 1 |  |  |  |  |  | 1 |
| [AC-6(4)](controls/ac-6.4.md) | Separate Processing Domains | No |  | 1 |  |  |  |  |  |  |  |
| [AC-6(8)](controls/ac-6.8.md) | Privilege Levels for Code Execution | No |  | 1 |  | 1 | 1 | 1 | 1 | 1 |  |
| [AC-6(9)](controls/ac-6.9.md) | Log Use of Privileged Functions | Yes |  | 1 | 1 | 1 |  | 1 | 1 | 1 |  |
| [AC-6(10)](controls/ac-6.10.md) | Prohibit Non-privileged Users from Executing Privileged Functions | Yes | 1 | 1 | 1 | 1 | 1 | 1 | 7 | 1 | 1 |
| [AC-7](controls/ac-7.md) | Unsuccessful Logon Attempts | Yes |  | 2 |  | 2 |  | 2 | 9 | 1 |  |
| [AC-8](controls/ac-8.md) | System Use Notification | Yes |  | 3 | 2 | 2 |  | 3 | 5 | 1 |  |
| [AC-9](controls/ac-9.md) | Previous Logon Notification | No |  | 1 |  |  |  |  |  |  |  |
| [AC-10](controls/ac-10.md) | Concurrent Session Control | Yes |  | 1 | 1 |  | 1 | 1 | 1 |  | 2 |
| [AC-11](controls/ac-11.md) | Device Lock | Yes |  |  |  |  |  | 3 | 9 |  |  |
| [AC-11(1)](controls/ac-11.1.md) | Pattern-hiding Displays | Yes |  |  |  |  |  | 1 | 3 |  |  |
| [AC-12](controls/ac-12.md) | Session Termination | Yes |  | 3 | 1 |  | 1 | 1 | 2 |  | 2 |
| [AC-12(1)](controls/ac-12.1.md) | User-initiated Logouts | No |  | 1 | 1 |  | 1 | 1 |  |  |  |
| [AC-12(2)](controls/ac-12.2.md) | Termination Message | No |  | 1 | 1 | 1 |  | 1 |  | 1 |  |
| [AC-16](controls/ac-16.md) | Security and Privacy Attributes | No |  | 3 | 2 |  | 3 |  |  |  |  |
| [AC-16(1)](controls/ac-16.1.md) | Dynamic Attribute Association | No |  |  | 2 |  |  |  |  |  |  |
| [AC-17(1)](controls/ac-17.1.md) | Monitoring and Control | Yes |  |  | 2 |  |  | 2 | 4 |  | 3 |
| [AC-17(2)](controls/ac-17.2.md) | Protection of Confidentiality and Integrity Using Encryption | Yes | 1 | 11 | 2 | 3 |  | 2 | 8 | 2 | 2 |
| [AC-17(9)](controls/ac-17.9.md) | Disconnect or Disable Access | No |  |  | 1 |  |  | 1 | 1 |  | 1 |
| [AC-17(10)](controls/ac-17.10.md) | Authenticate Remote Commands | No | 1 |  |  |  |  |  |  |  |  |
| [AC-18(1)](controls/ac-18.1.md) | Authentication and Encryption | Yes |  |  |  |  |  | 2 | 2 |  |  |
| [AC-23](controls/ac-23.md) | Data Mining Protection | No |  | 2 |  |  |  |  |  |  |  |
| [AT-3(3)](controls/at-3.3.md) | Practical Exercises | No |  | 1 |  |  |  |  |  |  |  |
| [AU-3](controls/au-3.md) | Content of Audit Records | Yes | 14 | 9 | 6 | 7 | 6 | 6 | 50 | 3 | 7 |
| [AU-3(1)](controls/au-3.1.md) | Additional Audit Information | Yes |  | 2 | 1 | 1 | 1 | 2 | 45 | 1 |  |
| [AU-4](controls/au-4.md) | Audit Log Storage Capacity | Yes |  |  | 1 | 1 | 1 | 1 | 3 | 2 | 1 |
| [AU-4(1)](controls/au-4.1.md) | Transfer to Alternate Storage | No |  | 2 | 2 | 1 | 1 | 2 | 9 | 1 | 2 |
| [AU-5](controls/au-5.md) | Response to Audit Logging Process Failures | Yes |  | 2 | 1 |  |  | 1 | 7 | 2 | 1 |
| [AU-5(1)](controls/au-5.1.md) | Storage Capacity Warning | Yes |  | 1 | 1 | 1 | 1 | 1 | 5 |  | 1 |
| [AU-5(2)](controls/au-5.2.md) | Real-time Alerts | Yes |  | 1 | 1 | 1 | 1 | 1 |  | 1 |  |
| [AU-6](controls/au-6.md) | Audit Record Review, Analysis, and Reporting | Yes |  | 1 |  |  |  |  |  |  |  |
| [AU-6(4)](controls/au-6.4.md) | Central Review and Analysis | No |  | 2 |  | 2 | 1 | 1 | 4 | 1 | 1 |
| [AU-7](controls/au-7.md) | Audit Record Reduction and Report Generation | Yes |  | 8 | 1 | 1 |  | 8 | 2 |  |  |
| [AU-7(1)](controls/au-7.1.md) | Automatic Processing | Yes |  | 1 |  |  |  | 1 | 2 |  |  |
| [AU-8](controls/au-8.md) | Time Stamps | Yes |  | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| [AU-9](controls/au-9.md) | Protection of Audit Information | Yes |  | 6 | 7 | 7 | 7 | 6 | 11 | 9 | 4 |
| [AU-9(2)](controls/au-9.2.md) | Store on Separate Physical Systems or Components | Yes |  | 1 | 1 |  |  |  |  |  | 1 |
| [AU-9(3)](controls/au-9.3.md) | Cryptographic Protection | Yes |  | 3 | 2 | 2 |  | 1 | 1 | 3 |  |
| [AU-9(5)](controls/au-9.5.md) | Dual Authorization | No |  |  |  |  |  | 1 |  |  |  |
| [AU-10](controls/au-10.md) | Non-repudiation | Yes |  | 1 | 1 |  | 1 |  |  |  |  |
| [AU-11](controls/au-11.md) | Audit Record Retention | Yes |  | 1 |  |  |  |  |  |  |  |
| [AU-12](controls/au-12.md) | Audit Record Generation | Yes | 3 | 28 | 10 | 22 | 31 | 20 | 57 | 12 | 1 |
| [AU-12(1)](controls/au-12.1.md) | System-wide and Time-correlated Audit Trail | Yes |  | 1 | 1 |  |  |  |  |  |  |
| [AU-12(3)](controls/au-12.3.md) | Changes by Authorized Individuals | Yes |  |  |  |  |  | 1 | 2 |  |  |
| [AU-14(1)](controls/au-14.1.md) | System Start-up | No |  | 1 | 1 | 1 | 1 | 1 | 4 | 2 | 1 |
| [CA-2(2)](controls/ca-2.2.md) | Specialized Assessments | Yes |  | 1 |  |  |  |  |  |  |  |
| [CM-3(5)](controls/cm-3.5.md) | Automated Security Response | No |  |  |  |  |  | 1 | 3 |  |  |
| [CM-4(2)](controls/cm-4.2.md) | Verification of Controls | Yes |  | 1 |  |  |  |  |  |  |  |
| [CM-5](controls/cm-5.md) | Access Restrictions for Change | Yes |  | 1 |  |  |  |  |  |  |  |
| [CM-5(1)](controls/cm-5.1.md) | Automated Access Enforcement and Audit Records | Yes |  | 2 | 2 | 3 | 2 | 2 | 4 | 2 | 2 |
| [CM-5(6)](controls/cm-5.6.md) | Limit Library Privileges | No |  | 1 | 1 | 5 | 5 | 1 | 9 | 1 |  |
| [CM-6](controls/cm-6.md) | Configuration Settings | Yes | 16 | 5 | 9 | 4 | 1 | 10 | 144 | 2 | 3 |
| [CM-7](controls/cm-7.md) | Least Functionality | Yes | 3 | 2 | 2 | 5 | 5 | 2 | 21 | 6 | 13 |
| [CM-7(1)](controls/cm-7.1.md) | Periodic Review | Yes |  |  |  | 1 | 1 |  |  |  | 1 |
| [CM-7(2)](controls/cm-7.2.md) | Prevent Program Execution | Yes |  | 1 |  | 1 |  | 1 | 25 | 1 |  |
| [CM-7(3)](controls/cm-7.3.md) | Registration Compliance | No |  | 2 |  |  |  |  |  |  |  |
| [CM-7(5)](controls/cm-7.5.md) | Authorized Software — Allow-by-exception | Yes |  | 1 |  | 1 |  | 1 | 2 | 1 |  |
| [CM-7(9)](controls/cm-7.9.md) | Prohibiting The Use of Unauthorized Hardware | No |  |  |  |  |  | 1 | 3 |  |  |
| [CM-9](controls/cm-9.md) | Configuration Management Plan | Yes |  | 4 |  |  |  |  |  |  |  |
| [CM-11(2)](controls/cm-11.2.md) | Software Installation with Privileged Status | No |  | 1 |  | 3 | 1 | 1 |  | 1 |  |
| [CM-14](controls/cm-14.md) | Signed Components | No |  | 1 | 1 | 2 | 1 | 1 | 6 | 1 | 2 |
| [CP-2](controls/cp-2.md) | Contingency Plan | Yes |  | 2 |  |  |  |  |  |  |  |
| [CP-2(8)](controls/cp-2.8.md) | Identify Critical Assets | Yes |  | 1 |  |  |  |  |  |  |  |
| [CP-9](controls/cp-9.md) | System Backup | Yes |  | 1 |  |  |  |  |  |  |  |
| [CP-11](controls/cp-11.md) | Alternate Communications Protocols | No |  | 1 |  |  |  |  |  |  |  |
| [IA-2](controls/ia-2.md) | Identification and Authentication (Organizational Users) | Yes | 1 | 1 | 1 | 4 | 1 | 1 | 4 | 2 |  |
| [IA-2(1)](controls/ia-2.1.md) | Multi-factor Authentication to Privileged Accounts | Yes |  | 2 | 2 | 2 |  | 2 | 4 | 2 |  |
| [IA-2(2)](controls/ia-2.2.md) | Multi-factor Authentication to Non-privileged Accounts | Yes |  | 2 |  | 2 |  | 2 | 3 | 2 |  |
| [IA-2(5)](controls/ia-2.5.md) | Individual Authentication with Group Authentication | Yes |  | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 1 |
| [IA-2(6)](controls/ia-2.6.md) | Access to Accounts —separate Device | No |  |  | 2 | 2 | 2 | 2 | 6 |  | 2 |
| [IA-2(8)](controls/ia-2.8.md) | Access to Accounts — Replay Resistant | Yes |  | 2 | 1 | 2 |  | 2 | 1 | 2 |  |
| [IA-2(12)](controls/ia-2.12.md) | Acceptance of PIV Credentials | Yes |  | 2 | 2 | 1 |  | 2 | 3 | 1 |  |
| [IA-3](controls/ia-3.md) | Device Identification and Authentication | Yes |  | 2 |  | 1 |  | 2 | 8 |  |  |
| [IA-3(1)](controls/ia-3.1.md) | Cryptographic Bidirectional Authentication | No |  | 1 |  |  |  | 1 |  |  |  |
| [IA-5](controls/ia-5.md) | Authenticator Management | Yes |  | 1 |  |  |  |  |  |  |  |
| [IA-5(1)](controls/ia-5.1.md) | Password-based Authentication | Yes |  | 11 | 3 | 17 | 10 | 14 | 23 | 1 | 10 |
| [IA-5(2)](controls/ia-5.2.md) | Public Key-based Authentication | Yes |  | 4 | 4 | 3 | 4 | 4 | 3 | 1 | 3 |
| [IA-5(6)](controls/ia-5.6.md) | Protection of Authenticators | Yes |  | 1 |  |  |  |  |  |  |  |
| [IA-5(13)](controls/ia-5.13.md) | Expiration of Cached Authenticators | No | 5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |  |
| [IA-6](controls/ia-6.md) | Authentication Feedback | Yes |  | 1 | 1 | 1 | 1 | 1 |  |  |  |
| [IA-7](controls/ia-7.md) | Cryptographic Module Authentication | Yes |  | 1 | 1 | 1 | 1 | 1 | 5 | 1 | 2 |
| [IA-8](controls/ia-8.md) | Identification and Authentication (Non-organizational Users) | Yes |  | 1 |  |  | 1 | 1 | 1 |  |  |
| [IA-8(1)](controls/ia-8.1.md) | Acceptance of PIV Credentials from Other Agencies | Yes |  | 2 | 2 | 1 |  |  |  | 1 |  |
| [IA-8(2)](controls/ia-8.2.md) | Acceptance of External Authenticators | Yes |  | 1 | 1 |  |  | 1 |  |  |  |
| [IA-8(4)](controls/ia-8.4.md) | Use of Defined Profiles | Yes |  | 1 | 1 |  |  |  |  |  |  |
| [IA-11](controls/ia-11.md) | Re-authentication | Yes | 1 | 2 | 1 | 1 | 1 | 3 | 5 | 1 |  |
| [IA-13(1)](controls/ia-13.1.md) | Protection of Cryptographic Keys | No | 1 |  |  |  |  |  |  |  |  |
| [IA-13(2)](controls/ia-13.2.md) | Verification of Identity Assertions and Access Tokens | No | 1 |  |  |  |  |  |  |  |  |
| [IA-13(3)](controls/ia-13.3.md) | Token Management | No | 11 |  |  |  |  |  |  |  |  |
| [MA-3(5)](controls/ma-3.5.md) | Execution with Privilege | No |  |  |  |  |  | 1 | 1 |  |  |
| [MA-4](controls/ma-4.md) | Nonlocal Maintenance | Yes |  | 2 |  | 1 |  | 1 | 2 | 1 |  |
| [MA-4(1)](controls/ma-4.1.md) | Logging and Review | No |  | 1 |  | 1 |  | 1 | 48 | 1 |  |
| [MA-4(4)](controls/ma-4.4.md) | Authentication and Separation of Maintenance Sessions | No |  |  | 1 | 1 | 1 |  |  |  | 1 |
| [MA-4(6)](controls/ma-4.6.md) | Cryptographic Protection | No |  | 2 |  | 2 |  | 2 | 3 | 1 |  |
| [MA-4(7)](controls/ma-4.7.md) | Disconnect Verification | No |  | 1 |  |  |  | 1 | 1 |  |  |
| [MP-3](controls/mp-3.md) | Media Marking | Yes |  | 1 |  |  |  |  |  |  |  |
| [PM-14](controls/pm-14.md) | Testing, Training, and Monitoring | No |  | 1 |  |  |  |  |  |  |  |
| [PT-2(1)](controls/pt-2.1.md) | Data Tagging | No |  |  | 1 |  |  |  |  |  |  |
| [PT-3(1)](controls/pt-3.1.md) | Data Tagging | No |  |  | 1 |  |  |  |  |  |  |
| [RA-5(5)](controls/ra-5.5.md) | Privileged Access | Yes |  |  |  | 1 |  |  |  | 1 |  |
| [SA-4(5)](controls/sa-4.5.md) | System, Component, and Service Configurations | Yes |  | 2 |  |  |  |  |  |  |  |
| [SA-5](controls/sa-5.md) | System Documentation | Yes |  | 2 |  |  |  |  |  |  |  |
| [SA-10](controls/sa-10.md) | Developer Configuration Management | Yes |  | 1 |  |  |  |  |  |  |  |
| [SA-10(1)](controls/sa-10.1.md) | Software and Firmware Integrity Verification | No |  | 1 |  |  |  |  |  |  |  |
| [SA-11](controls/sa-11.md) | Developer Testing and Evaluation | Yes |  | 3 |  |  |  |  |  |  |  |
| [SA-11(2)](controls/sa-11.2.md) | Threat Modeling and Vulnerability Analyses | No |  | 2 |  |  |  |  |  |  |  |
| [SA-11(4)](controls/sa-11.4.md) | Manual Code Reviews | No |  | 2 |  |  |  |  |  |  |  |
| [SA-15](controls/sa-15.md) | Development Process, Standards, and Tools | Yes |  | 2 |  |  |  |  |  |  |  |
| [SA-15(5)](controls/sa-15.5.md) | Attack Surface Reduction | No |  | 1 |  |  |  |  |  |  |  |
| [SA-15(10)](controls/sa-15.10.md) | Incident Response Plan | No |  | 1 |  |  |  |  |  |  |  |
| [SA-22](controls/sa-22.md) | Unsupported System Components | Yes |  | 2 | 1 | 1 | 1 | 1 |  |  | 1 |
| [SC-2](controls/sc-2.md) | Separation of System and User Functionality | Yes |  | 1 | 1 | 1 | 1 | 1 | 5 | 1 | 3 |
| [SC-3](controls/sc-3.md) | Security Function Isolation | Yes |  | 1 |  | 1 | 1 | 1 | 5 | 1 | 1 |
| [SC-4](controls/sc-4.md) | Information in Shared System Resources | Yes |  | 1 |  | 2 | 3 | 1 | 4 | 7 |  |
| [SC-5](controls/sc-5.md) | Denial-of-service Protection | Yes | 1 | 1 | 2 | 1 |  | 1 | 2 | 2 | 2 |
| [SC-5(1)](controls/sc-5.1.md) | Restrict Ability to Attack Other Systems | No |  | 1 |  | 1 |  |  |  | 3 | 1 |
| [SC-5(2)](controls/sc-5.2.md) | Capacity, Bandwidth, and Redundancy | No | 2 | 1 |  | 1 |  | 1 | 1 |  |  |
| [SC-7(13)](controls/sc-7.13.md) | Isolation of Security Tools, Mechanisms, and Support Components | No |  | 1 |  |  |  |  |  |  |  |
| [SC-8](controls/sc-8.md) | Transmission Confidentiality and Integrity | Yes | 2 | 1 | 2 | 1 |  | 2 | 6 | 1 | 10 |
| [SC-8(1)](controls/sc-8.1.md) | Cryptographic Protection | Yes |  | 1 | 1 |  |  | 1 | 4 |  |  |
| [SC-8(2)](controls/sc-8.2.md) | Pre- and Post-transmission Handling | No | 1 | 4 | 2 | 2 | 2 | 2 | 3 |  | 2 |
| [SC-10](controls/sc-10.md) | Network Disconnect | Yes |  | 1 |  | 1 |  | 1 | 4 | 2 |  |
| [SC-11](controls/sc-11.md) | Trusted Path | No |  | 1 |  |  |  |  | 5 | 1 |  |
| [SC-13](controls/sc-13.md) | Cryptographic Protection | Yes | 1 | 5 | 3 | 3 | 4 | 3 | 4 | 1 | 1 |
| [SC-16](controls/sc-16.md) | Transmission of Security and Privacy Attributes | No | 1 |  |  |  |  |  |  |  |  |
| [SC-17](controls/sc-17.md) | Public Key Infrastructure Certificates | Yes |  |  | 1 | 1 | 1 | 1 |  |  | 1 |
| [SC-18(1)](controls/sc-18.1.md) | Identify Unacceptable Code and Take Corrective Actions | No |  | 1 | 1 |  |  |  |  |  | 1 |
| [SC-18(2)](controls/sc-18.2.md) | Acquisition, Development, and Use | No |  | 1 |  |  |  |  |  |  |  |
| [SC-23](controls/sc-23.md) | Session Authenticity | Yes | 1 | 3 | 1 | 1 |  |  |  | 1 | 2 |
| [SC-23(1)](controls/sc-23.1.md) | Invalidate Session Identifiers at Logout | No |  | 1 | 1 |  | 1 |  |  |  | 1 |
| [SC-23(3)](controls/sc-23.3.md) | Unique System-generated Session Identifiers | No | 1 | 5 | 3 |  | 2 |  |  |  | 7 |
| [SC-23(5)](controls/sc-23.5.md) | Allowed Certificate Authorities | No |  | 1 | 1 |  | 1 | 1 |  |  | 1 |
| [SC-24](controls/sc-24.md) | Fail in Known State | Yes |  | 2 | 4 | 2 | 2 | 2 | 1 |  | 3 |
| [SC-28](controls/sc-28.md) | Protection of Information at Rest | Yes | 2 | 1 | 2 |  | 1 | 1 | 1 |  | 1 |
| [SC-28(1)](controls/sc-28.1.md) | Cryptographic Protection | Yes |  | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 |
| [SC-28(2)](controls/sc-28.2.md) | Offline Storage | No |  | 1 |  |  |  |  |  |  |  |
| [SC-28(3)](controls/sc-28.3.md) | Cryptographic Keys | No | 1 |  | 1 | 1 | 1 | 1 |  |  | 1 |
| [SC-39](controls/sc-39.md) | Process Isolation | Yes |  | 1 |  | 1 | 1 |  |  |  |  |
| [SC-45](controls/sc-45.md) | System Time Synchronization | No |  |  | 1 | 1 | 1 | 1 |  |  | 1 |
| [SC-45(1)](controls/sc-45.1.md) | Synchronization with Authoritative Time Source | No |  |  | 2 |  | 1 | 2 | 3 |  | 1 |
| [SI-2](controls/si-2.md) | Flaw Remediation | Yes |  | 1 | 1 | 2 | 1 | 1 |  | 2 | 1 |
| [SI-2(6)](controls/si-2.6.md) | Removal of Previous Versions of Software and Firmware | No |  | 1 | 1 | 2 | 1 | 1 | 1 | 1 |  |
| [SI-4(3)](controls/si-4.3.md) | Automated Tool and Mechanism Integration | No |  |  | 1 |  |  |  |  |  |  |
| [SI-4(12)](controls/si-4.12.md) | Automated Organization-generated Alerts | Yes |  | 1 |  |  |  |  |  |  |  |
| [SI-5](controls/si-5.md) | Security Alerts, Advisories, and Directives | Yes |  | 2 |  |  |  |  |  |  |  |
| [SI-6](controls/si-6.md) | Security and Privacy Function Verification | Yes | 1 | 3 |  | 3 |  | 3 | 4 | 3 |  |
| [SI-10](controls/si-10.md) | Information Input Validation | Yes | 1 | 7 | 1 |  | 3 |  |  |  | 3 |
| [SI-10(3)](controls/si-10.3.md) | Predictable Behavior | No | 2 | 1 | 1 | 1 | 1 | 1 |  |  |  |
| [SI-11](controls/si-11.md) | Error Handling | Yes | 1 | 2 | 3 | 1 | 2 | 2 | 9 |  | 3 |
| [SI-16](controls/si-16.md) | Memory Protection | Yes |  | 1 |  | 1 |  | 2 | 5 | 3 |  |

Regenerate with `python scripts/build-cci-crosswalk.py`. The weekly source verification runs `--check`, which fails if the committed crosswalk no longer matches the pinned sources.
