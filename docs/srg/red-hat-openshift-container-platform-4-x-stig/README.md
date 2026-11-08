# Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide

Release: 7 Benchmark Date: 30 Sep 2026. Accepted 2026-08-24.

| | |
| --- | --- |
| Benchmark | `RH_OpenShift_Container_Platform_4-x_STIG` |
| Rules | **83** |
| CAT I | 7 |
| CAT II | 73 |
| CAT III | 3 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-257505`](rules/V-257505.md) | `CNTR-OS-000010` | CAT II | OpenShift must use TLS 1.2 or greater for secure container image transport from trusted sources. |
| [`V-257506`](rules/V-257506.md) | `CNTR-OS-000020` | CAT II | OpenShift must use TLS 1.2 or greater for secure communication. |
| [`V-257507`](rules/V-257507.md) | `CNTR-OS-000030` | CAT II | OpenShift must use a centralized user management solution to support account management functions. |
| [`V-257508`](rules/V-257508.md) | `CNTR-OS-000040` | CAT II | The kubeadmin account must be disabled. |
| [`V-257509`](rules/V-257509.md) | `CNTR-OS-000050` | CAT II | OpenShift must automatically audit account creation. |
| [`V-257510`](rules/V-257510.md) | `CNTR-OS-000060` | CAT II | OpenShift must automatically audit account modification. |
| [`V-257511`](rules/V-257511.md) | `CNTR-OS-000070` | CAT II | OpenShift must generate audit rules to capture account related actions. |
| [`V-257512`](rules/V-257512.md) | `CNTR-OS-000080` | CAT II | Open Shift must automatically audit account removal actions. |
| [`V-257513`](rules/V-257513.md) | `CNTR-OS-000090` | CAT I | OpenShift role-based access controls (RBAC) must be enforced. |
| [`V-257514`](rules/V-257514.md) | `CNTR-OS-000100` | CAT II | OpenShift must enforce network policy on the namespace for controlling the flow of information within the container platform based on organization-defined information flow control policies. |
| [`V-257515`](rules/V-257515.md) | `CNTR-OS-000110` | CAT II | OpenShift must enforce approved authorizations for controlling the flow of information within the container platform based on organization-defined information flow control policies. |
| [`V-257516`](rules/V-257516.md) | `CNTR-OS-000130` | CAT III | OpenShift must display the Standard Mandatory DoW Notice and Consent Banner before granting access to platform components. |
| [`V-257517`](rules/V-257517.md) | `CNTR-OS-000150` | CAT II | OpenShift must generate audit records for all DoW-defined auditable events within all components in the platform. |
| [`V-257518`](rules/V-257518.md) | `CNTR-OS-000160` | CAT II | OpenShift must generate audit records when successful/unsuccessful attempts to access privileges occur. |
| [`V-257519`](rules/V-257519.md) | `CNTR-OS-000170` | CAT I | Red Hat Enterprise Linux CoreOS (RHCOS) must initiate session audits at system startup. |
| [`V-257520`](rules/V-257520.md) | `CNTR-OS-000180` | CAT II | All audit records must identify what type of event has occurred within OpenShift. |
| [`V-257521`](rules/V-257521.md) | `CNTR-OS-000190` | CAT II | OpenShift audit records must have a date and time association with all events. |
| [`V-257522`](rules/V-257522.md) | `CNTR-OS-000200` | CAT II | All audit records must generate the event results within OpenShift. |
| [`V-257523`](rules/V-257523.md) | `CNTR-OS-000210` | CAT II | OpenShift must take appropriate action upon an audit failure. |
| [`V-257524`](rules/V-257524.md) | `CNTR-OS-000220` | CAT II | OpenShift components must provide the ability to send audit logs to a central enterprise repository for review and analysis. |
| [`V-257525`](rules/V-257525.md) | `CNTR-OS-000230` | CAT II | OpenShift must use internal system clocks to generate audit record time stamps. |
| [`V-257526`](rules/V-257526.md) | `CNTR-OS-000240` | CAT II | The Red Hat Enterprise Linux CoreOS (RHCOS) chrony Daemon must use multiple NTP servers to generate audit record time stamps. |
| [`V-257527`](rules/V-257527.md) | `CNTR-OS-000250` | CAT II | OpenShift must protect audit logs from any type of unauthorized access. |
| [`V-257528`](rules/V-257528.md) | `CNTR-OS-000260` | CAT II | OpenShift must protect system journal file from any type of unauthorized access by setting file permissions. |
| [`V-257529`](rules/V-257529.md) | `CNTR-OS-000270` | CAT II | OpenShift must protect system journal file from any type of unauthorized access by setting owner permissions. |
| [`V-257530`](rules/V-257530.md) | `CNTR-OS-000280` | CAT II | OpenShift must protect log directory from any type of unauthorized access by setting file permissions. |
| [`V-257531`](rules/V-257531.md) | `CNTR-OS-000290` | CAT II | OpenShift must protect log directory from any type of unauthorized access by setting owner permissions. |
| [`V-257532`](rules/V-257532.md) | `CNTR-OS-000300` | CAT II | OpenShift must protect pod log files from any type of unauthorized access by setting owner permissions. |
| [`V-257533`](rules/V-257533.md) | `CNTR-OS-000310` | CAT II | OpenShift must protect audit information from unauthorized modification. |
| [`V-257534`](rules/V-257534.md) | `CNTR-OS-000320` | CAT II | OpenShift must prevent unauthorized changes to logon UIDs. |
| [`V-257535`](rules/V-257535.md) | `CNTR-OS-000330` | CAT II | OpenShift must protect audit tools from unauthorized access. |
| [`V-257536`](rules/V-257536.md) | `CNTR-OS-000340` | CAT II | OpenShift must use FIPS-validated cryptographic mechanisms to protect the integrity of log information. |
| [`V-257537`](rules/V-257537.md) | `CNTR-OS-000360` | CAT II | OpenShift must verify container images. |
| [`V-257538`](rules/V-257538.md) | `CNTR-OS-000380` | CAT II | OpenShift must contain only container images for those capabilities being offered by the container platform. |
| [`V-257539`](rules/V-257539.md) | `CNTR-OS-000390` | CAT II | OpenShift runtime must enforce ports, protocols, and services that adhere to the PPSM CAL. |
| [`V-257540`](rules/V-257540.md) | `CNTR-OS-000400` | CAT I | OpenShift must disable root and terminate network connections. |
| [`V-257541`](rules/V-257541.md) | `CNTR-OS-000430` | CAT II | OpenShift must use multifactor authentication for network access to accounts. |
| [`V-257542`](rules/V-257542.md) | `CNTR-OS-000440` | CAT II | OpenShift must use FIPS-validated SHA-1 or higher hash function to provide replay-resistant authentication mechanisms for network access to privileged accounts. |
| [`V-257543`](rules/V-257543.md) | `CNTR-OS-000460` | CAT I | OpenShift must use FIPS validated LDAP or OpenIDConnect. |
| [`V-257544`](rules/V-257544.md) | `CNTR-OS-000490` | CAT II | OpenShift must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity. |
| [`V-257545`](rules/V-257545.md) | `CNTR-OS-000500` | CAT II | OpenShift must separate user functionality (including user interface services) from information system management functionality. |
| [`V-257546`](rules/V-257546.md) | `CNTR-OS-000510` | CAT I | OpenShift must protect authenticity of communications sessions with the use of FIPS-validated 140-2 or 140-3 validated cryptography. |
| [`V-257547`](rules/V-257547.md) | `CNTR-OS-000540` | CAT II | OpenShift runtime must isolate security functions from nonsecurity functions. |
| [`V-257548`](rules/V-257548.md) | `CNTR-OS-000560` | CAT II | OpenShift must prevent unauthorized and unintended information transfer via shared system resources and enable page poisoning. |
| [`V-257549`](rules/V-257549.md) | `CNTR-OS-000570` | CAT II | OpenShift must disable virtual syscalls. |
| [`V-257550`](rules/V-257550.md) | `CNTR-OS-000580` | CAT II | OpenShift must enable poisoning of SLUB/SLAB objects. |
| [`V-257551`](rules/V-257551.md) | `CNTR-OS-000590` | CAT II | OpenShift must set the sticky bit for world-writable directories. |
| [`V-257552`](rules/V-257552.md) | `CNTR-OS-000600` | CAT II | OpenShift must restrict access to the kernel buffer. |
| [`V-257553`](rules/V-257553.md) | `CNTR-OS-000610` | CAT II | OpenShift must prevent kernel profiling. |
| [`V-257554`](rules/V-257554.md) | `CNTR-OS-000620` | CAT II | OpenShift must restrict individuals the ability to launch organizational-defined Denial-of-Service (DOS) attacks against other information systems by setting a default Resource Quota. |
| [`V-257555`](rules/V-257555.md) | `CNTR-OS-000630` | CAT II | OpenShift must restrict individuals' ability to launch organization-defined denial-of-service (DOS) attacks against other information systems by rate-limiting. |
| [`V-257556`](rules/V-257556.md) | `CNTR-OS-000650` | CAT III | OpenShift must display an explicit logout message indicating the reliable termination of authenticated communication sessions. |
| [`V-257557`](rules/V-257557.md) | `CNTR-OS-000660` | CAT I | Container images instantiated by OpenShift must execute using least privileges. |
| [`V-257558`](rules/V-257558.md) | `CNTR-OS-000670` | CAT III | Red Hat Enterprise Linux CoreOS (RHCOS) must allocate audit record storage capacity to store at least one weeks' worth of audit records, when audit records are not immediately sent to a central audit record storage facility. |
| [`V-257559`](rules/V-257559.md) | `CNTR-OS-000690` | CAT II | OpenShift must configure Alert Manger Receivers to notify SA and ISSO of all audit failure events requiring real-time alerts. |
| [`V-257560`](rules/V-257560.md) | `CNTR-OS-000720` | CAT II | OpenShift must enforce access restrictions and support auditing of the enforcement actions. |
| [`V-257561`](rules/V-257561.md) | `CNTR-OS-000740` | CAT II | OpenShift must prevent the installation of patches, service packs, device drivers, or operating system components without verification they have been digitally signed using a certificate that is recognized and approved by the organization. |
| [`V-257562`](rules/V-257562.md) | `CNTR-OS-000760` | CAT II | OpenShift must set server token max age no greater than eight hours. |
| [`V-257563`](rules/V-257563.md) | `CNTR-OS-000770` | CAT II | Vulnerability scanning applications must implement privileged access authorization to all OpenShift components, containers, and container images for selected organization-defined vulnerability scanning activities. |
| [`V-257564`](rules/V-257564.md) | `CNTR-OS-000780` | CAT II | OpenShift keystore must implement encryption to prevent unauthorized disclosure of information at rest within the container platform. |
| [`V-257565`](rules/V-257565.md) | `CNTR-OS-000800` | CAT II | OpenShift must protect against or limit the effects of all types of Denial-of-Service (DoS) attacks by employing organization-defined security safeguards by including a default resource quota. |
| [`V-257566`](rules/V-257566.md) | `CNTR-OS-000810` | CAT II | OpenShift must protect against or limit the effects of all types of Denial-of-Service (DoS) attacks by defining resource quotas on a namespace. |
| [`V-257567`](rules/V-257567.md) | `CNTR-OS-000820` | CAT II | OpenShift must protect the confidentiality and integrity of transmitted information. |
| [`V-257568`](rules/V-257568.md) | `CNTR-OS-000860` | CAT II | Red Hat Enterprise Linux CoreOS (RHCOS) must implement nonexecutable data to protect its memory from unauthorized code execution. |
| [`V-257569`](rules/V-257569.md) | `CNTR-OS-000870` | CAT II | Red Hat Enterprise Linux CoreOS (RHCOS) must implement ASLR (Address Space Layout Randomization) from unauthorized code execution. |
| [`V-257570`](rules/V-257570.md) | `CNTR-OS-000880` | CAT II | OpenShift must remove old components after updated versions have been installed. |
| [`V-257571`](rules/V-257571.md) | `CNTR-OS-000890` | CAT II | OpenShift must contain the latest images with most recent updates and execute within the container platform runtime as authorized by IAVM, CTOs, DTMs, and STIGs. |
| [`V-257572`](rules/V-257572.md) | `CNTR-OS-000900` | CAT II | OpenShift runtime must have updates installed within the period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). |
| [`V-257573`](rules/V-257573.md) | `CNTR-OS-000910` | CAT II | The Compliance Operator must be configured. |
| [`V-257574`](rules/V-257574.md) | `CNTR-OS-000920` | CAT II | OpenShift must perform verification of the correct operation of security functions: upon startup and/or restart; upon command by a user with privileged access; and/or every 30 days. |
| [`V-257575`](rules/V-257575.md) | `CNTR-OS-000930` | CAT II | OpenShift must generate audit records when successful/unsuccessful attempts to modify privileges occur. |
| [`V-257576`](rules/V-257576.md) | `CNTR-OS-000940` | CAT II | OpenShift must generate audit records when successful/unsuccessful attempts to modify security objects occur. |
| [`V-257577`](rules/V-257577.md) | `CNTR-OS-000950` | CAT II | OpenShift must generate audit records when successful/unsuccessful attempts to delete privileges occur. |
| [`V-257578`](rules/V-257578.md) | `CNTR-OS-000960` | CAT II | OpenShift must generate audit records when successful/unsuccessful attempts to delete security objects occur. |
| [`V-257579`](rules/V-257579.md) | `CNTR-OS-000970` | CAT II | OpenShift must generate audit records when successful/unsuccessful logon attempts occur. |
| [`V-257580`](rules/V-257580.md) | `CNTR-OS-000980` | CAT II | Red Hat Enterprise Linux CoreOS (RHCOS) must be configured to audit the loading and unloading of dynamic kernel modules. |
| [`V-257581`](rules/V-257581.md) | `CNTR-OS-000990` | CAT II | OpenShift audit records must record user access start and end times. |
| [`V-257582`](rules/V-257582.md) | `CNTR-OS-001000` | CAT II | OpenShift must generate audit records when concurrent logons from different workstations and systems occur. |
| [`V-257583`](rules/V-257583.md) | `CNTR-OS-001010` | CAT I | Red Hat Enterprise Linux CoreOS (RHCOS) must disable SSHD service. |
| [`V-257584`](rules/V-257584.md) | `CNTR-OS-001020` | CAT II | Red Hat Enterprise Linux CoreOS (RHCOS) must disable USB Storage kernel module. |
| [`V-257585`](rules/V-257585.md) | `CNTR-OS-001030` | CAT II | Red Hat Enterprise Linux CoreOS (RHCOS) must use USBGuard for hosts that include a USB Controller. |
| [`V-257586`](rules/V-257586.md) | `CNTR-OS-001060` | CAT II | OpenShift must continuously scan components, containers, and images for vulnerabilities. |
| [`V-257587`](rules/V-257587.md) | `CNTR-OS-001080` | CAT II | OpenShift must use FIPS-validated SHA-2 or higher hash function for digital signature generation and verification (nonlegacy use). |
