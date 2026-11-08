# Red Hat Enterprise Linux 9 Security Technical Implementation Guide

Release: 10 Benchmark Date: 30 Sep 2026. Accepted 2026-09-29.

| | |
| --- | --- |
| Benchmark | `RHEL_9_STIG` |
| Rules | **445** |
| CAT I | 29 |
| CAT II | 401 |
| CAT III | 15 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-257777`](rules/V-257777.md) | `RHEL-09-211010` | CAT I | RHEL 9 must be a vendor-supported release. |
| [`V-257778`](rules/V-257778.md) | `RHEL-09-211015` | CAT II | RHEL 9 vendor packaged system security patches and updates must be installed and up to date. |
| [`V-257779`](rules/V-257779.md) | `RHEL-09-211020` | CAT II | RHEL 9 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a command line user logon. |
| [`V-257781`](rules/V-257781.md) | `RHEL-09-211030` | CAT II | The graphical display manager must not be the default target on RHEL 9 unless approved. |
| [`V-257782`](rules/V-257782.md) | `RHEL-09-211035` | CAT III | RHEL 9 must enable the hardware random number generator entropy gatherer service. |
| [`V-257783`](rules/V-257783.md) | `RHEL-09-211040` | CAT II | RHEL 9 systemd-journald service must be enabled. |
| [`V-257784`](rules/V-257784.md) | `RHEL-09-211045` | CAT I | The systemd Ctrl-Alt-Delete burst key sequence in RHEL 9 must be disabled. |
| [`V-257785`](rules/V-257785.md) | `RHEL-09-211050` | CAT I | The x86 Ctrl-Alt-Delete key sequence must be disabled on RHEL 9. |
| [`V-257786`](rules/V-257786.md) | `RHEL-09-211055` | CAT II | RHEL 9 debug-shell systemd service must be disabled. |
| [`V-257787`](rules/V-257787.md) | `RHEL-09-212010` | CAT II | RHEL 9 must require authentication upon booting into single-user and maintenance modes. |
| [`V-257788`](rules/V-257788.md) | `RHEL-09-212015` | CAT II | RHEL 9 must disable the ability of systemd to spawn an interactive boot process. |
| [`V-257789`](rules/V-257789.md) | `RHEL-09-212020` | CAT I | RHEL 9 must require a unique superusers name upon booting into single-user and maintenance modes. |
| [`V-257790`](rules/V-257790.md) | `RHEL-09-212025` | CAT II | RHEL 9 /boot/grub2/grub.cfg file must be group-owned by root. |
| [`V-257791`](rules/V-257791.md) | `RHEL-09-212030` | CAT II | RHEL 9 /boot/grub2/grub.cfg file must be owned by root. |
| [`V-257792`](rules/V-257792.md) | `RHEL-09-212035` | CAT II | RHEL 9 must disable virtual system calls. |
| [`V-257793`](rules/V-257793.md) | `RHEL-09-212040` | CAT II | RHEL 9 must clear the page allocator to prevent use-after-free attacks. |
| [`V-257794`](rules/V-257794.md) | `RHEL-09-212045` | CAT II | RHEL 9 must clear memory when it is freed to prevent use-after-free attacks. |
| [`V-257795`](rules/V-257795.md) | `RHEL-09-212050` | CAT III | RHEL 9 must enable mitigations against processor-based vulnerabilities. |
| [`V-257796`](rules/V-257796.md) | `RHEL-09-212055` | CAT III | RHEL 9 must enable auditing of processes that start prior to the audit daemon. |
| [`V-257797`](rules/V-257797.md) | `RHEL-09-213010` | CAT II | RHEL 9 must restrict access to the kernel message buffer. |
| [`V-257798`](rules/V-257798.md) | `RHEL-09-213015` | CAT II | RHEL 9 must prevent kernel profiling by nonprivileged users. |
| [`V-257799`](rules/V-257799.md) | `RHEL-09-213020` | CAT II | RHEL 9 must prevent the loading of a new kernel for later execution. |
| [`V-257800`](rules/V-257800.md) | `RHEL-09-213025` | CAT II | RHEL 9 must restrict exposed kernel pointer addresses access. |
| [`V-257801`](rules/V-257801.md) | `RHEL-09-213030` | CAT II | RHEL 9 must enable kernel parameters to enforce discretionary access control (DAC) on hardlinks. |
| [`V-257802`](rules/V-257802.md) | `RHEL-09-213035` | CAT II | RHEL 9 must enable kernel parameters to enforce discretionary access (DAC) control on symlinks. |
| [`V-257803`](rules/V-257803.md) | `RHEL-09-213040` | CAT II | RHEL 9 must disable the kernel.core_pattern. |
| [`V-257804`](rules/V-257804.md) | `RHEL-09-213045` | CAT II | RHEL 9 must be configured to disable the Asynchronous Transfer Mode kernel module. |
| [`V-257805`](rules/V-257805.md) | `RHEL-09-213050` | CAT II | RHEL 9 must be configured to disable the Controller Area Network kernel module. |
| [`V-257806`](rules/V-257806.md) | `RHEL-09-213055` | CAT II | RHEL 9 must be configured to disable the FireWire kernel module. |
| [`V-257807`](rules/V-257807.md) | `RHEL-09-213060` | CAT II | RHEL 9 must disable the Stream Control Transmission Protocol (SCTP) kernel module. |
| [`V-257808`](rules/V-257808.md) | `RHEL-09-213065` | CAT II | RHEL 9 must disable the Transparent Inter Process Communication (TIPC) kernel module. |
| [`V-257809`](rules/V-257809.md) | `RHEL-09-213070` | CAT II | RHEL 9 must implement address space layout randomization (ASLR) to protect its memory from unauthorized code execution. |
| [`V-257810`](rules/V-257810.md) | `RHEL-09-213075` | CAT II | RHEL 9 must disable access to network bpf system call from nonprivileged processes. |
| [`V-257811`](rules/V-257811.md) | `RHEL-09-213080` | CAT II | RHEL 9 must restrict usage of ptrace to descendant processes. |
| [`V-257812`](rules/V-257812.md) | `RHEL-09-213085` | CAT II | RHEL 9 must disable core dump backtraces. |
| [`V-257813`](rules/V-257813.md) | `RHEL-09-213090` | CAT II | RHEL 9 must disable storing core dumps. |
| [`V-257814`](rules/V-257814.md) | `RHEL-09-213095` | CAT II | RHEL 9 must disable core dumps for all users. |
| [`V-257815`](rules/V-257815.md) | `RHEL-09-213100` | CAT II | RHEL 9 must disable acquiring, saving, and processing core dumps. |
| [`V-257816`](rules/V-257816.md) | `RHEL-09-213105` | CAT II | RHEL 9 must disable the use of user namespaces. |
| [`V-257817`](rules/V-257817.md) | `RHEL-09-213110` | CAT II | RHEL 9 must implement nonexecutable data to protect its memory from unauthorized code execution. |
| [`V-257818`](rules/V-257818.md) | `RHEL-09-213115` | CAT II | The kdump service on RHEL 9 must be disabled. |
| [`V-257819`](rules/V-257819.md) | `RHEL-09-214010` | CAT II | RHEL 9 must ensure cryptographic verification of vendor software packages. |
| [`V-257820`](rules/V-257820.md) | `RHEL-09-214015` | CAT I | RHEL 9 must check the GPG signature of software packages originating from external software repositories before installation. |
| [`V-257821`](rules/V-257821.md) | `RHEL-09-214020` | CAT I | RHEL 9 must check the GPG signature of locally installed software packages before installation. |
| [`V-257822`](rules/V-257822.md) | `RHEL-09-214025` | CAT I | RHEL 9 must have GPG signature verification enabled for all software repositories. |
| [`V-257823`](rules/V-257823.md) | `RHEL-09-214030` | CAT II | RHEL 9 must be configured so that the cryptographic hashes of system files match vendor values. |
| [`V-257824`](rules/V-257824.md) | `RHEL-09-214035` | CAT III | RHEL 9 must remove all software components after updated versions have been installed. |
| [`V-257825`](rules/V-257825.md) | `RHEL-09-215010` | CAT II | RHEL 9 subscription-manager package must be installed. |
| [`V-257826`](rules/V-257826.md) | `RHEL-09-215015` | CAT I | RHEL 9 must not have a File Transfer Protocol (FTP) server package installed. |
| [`V-257827`](rules/V-257827.md) | `RHEL-09-215020` | CAT II | RHEL 9 must not have the sendmail package installed. |
| [`V-257828`](rules/V-257828.md) | `RHEL-09-215025` | CAT II | RHEL 9 must not have the nfs-utils package installed. |
| [`V-257830`](rules/V-257830.md) | `RHEL-09-215035` | CAT II | RHEL 9 must not install packages from the Extra Packages for Enterprise Linux (EPEL) repository. |
| [`V-257831`](rules/V-257831.md) | `RHEL-09-215040` | CAT II | RHEL 9 must not have the telnet-server package installed. |
| [`V-257832`](rules/V-257832.md) | `RHEL-09-215045` | CAT II | RHEL 9 must not have the gssproxy package installed. |
| [`V-257833`](rules/V-257833.md) | `RHEL-09-215050` | CAT II | RHEL 9 must not have the iprutils package installed. |
| [`V-257834`](rules/V-257834.md) | `RHEL-09-215055` | CAT II | RHEL 9 must not have the tuned package installed. |
| [`V-257835`](rules/V-257835.md) | `RHEL-09-215060` | CAT I | The Trivial File Transfer Protocol (TFTP) server must not be installed unless it is required, and if required, the RHEL 9 TFTP daemon must be configured to operate in secure mode. |
| [`V-257837`](rules/V-257837.md) | `RHEL-09-215070` | CAT II | A graphical display manager must not be installed on RHEL 9 unless approved. |
| [`V-257838`](rules/V-257838.md) | `RHEL-09-215075` | CAT II | RHEL 9 must have the openssl-pkcs11 package installed. |
| [`V-257839`](rules/V-257839.md) | `RHEL-09-215080` | CAT II | RHEL 9 must have the gnutls-utils package installed. |
| [`V-257840`](rules/V-257840.md) | `RHEL-09-215085` | CAT II | RHEL 9 must have the nss-tools package installed. |
| [`V-257841`](rules/V-257841.md) | `RHEL-09-215090` | CAT II | RHEL 9 must have the rng-tools package installed. |
| [`V-257842`](rules/V-257842.md) | `RHEL-09-215095` | CAT II | RHEL 9 must have the s-nail package installed. |
| [`V-257843`](rules/V-257843.md) | `RHEL-09-231010` | CAT II | A separate RHEL 9 file system must be used for user home directories (such as /home or an equivalent). |
| [`V-257844`](rules/V-257844.md) | `RHEL-09-231015` | CAT II | RHEL 9 must use a separate file system for /tmp. |
| [`V-257845`](rules/V-257845.md) | `RHEL-09-231020` | CAT III | RHEL 9 must use a separate file system for /var. |
| [`V-257846`](rules/V-257846.md) | `RHEL-09-231025` | CAT III | RHEL 9 must use a separate file system for /var/log. |
| [`V-257847`](rules/V-257847.md) | `RHEL-09-231030` | CAT III | RHEL 9 must use a separate file system for the system audit data path. |
| [`V-257848`](rules/V-257848.md) | `RHEL-09-231035` | CAT II | RHEL 9 must use a separate file system for /var/tmp. |
| [`V-257849`](rules/V-257849.md) | `RHEL-09-231040` | CAT II | The RHEL 9 file system automounter must be disabled. |
| [`V-257850`](rules/V-257850.md) | `RHEL-09-231045` | CAT II | RHEL 9 must prevent device files from being interpreted on file systems that contain user home directories. |
| [`V-257851`](rules/V-257851.md) | `RHEL-09-231050` | CAT II | RHEL 9 must prevent files with the setuid and setgid bit set from being executed on file systems that contain user home directories. |
| [`V-257852`](rules/V-257852.md) | `RHEL-09-231055` | CAT II | RHEL 9 must prevent code from being executed on file systems that contain user home directories. |
| [`V-257854`](rules/V-257854.md) | `RHEL-09-231065` | CAT II | RHEL 9 must prevent special devices on file systems that are imported via Network File System (NFS). |
| [`V-257855`](rules/V-257855.md) | `RHEL-09-231070` | CAT II | RHEL 9  must prevent code from being executed on file systems that are imported via Network File System (NFS). |
| [`V-257856`](rules/V-257856.md) | `RHEL-09-231075` | CAT II | RHEL 9 must prevent files with the setuid and setgid bit set from being executed on file systems that are imported via Network File System (NFS). |
| [`V-257857`](rules/V-257857.md) | `RHEL-09-231080` | CAT II | RHEL 9 must prevent code from being executed on file systems that are used with removable media. |
| [`V-257858`](rules/V-257858.md) | `RHEL-09-231085` | CAT II | RHEL 9 must prevent special devices on file systems that are used with removable media. |
| [`V-257859`](rules/V-257859.md) | `RHEL-09-231090` | CAT II | RHEL 9 must prevent files with the setuid and setgid bit set from being executed on file systems that are used with removable media. |
| [`V-257860`](rules/V-257860.md) | `RHEL-09-231095` | CAT II | RHEL 9 must mount /boot with the nodev option. |
| [`V-257861`](rules/V-257861.md) | `RHEL-09-231100` | CAT II | RHEL 9 must prevent files with the setuid and setgid bit set from being executed on the /boot directory. |
| [`V-257862`](rules/V-257862.md) | `RHEL-09-231105` | CAT II | RHEL 9 must prevent files with the setuid and setgid bit set from being executed on the /boot/efi directory. |
| [`V-257863`](rules/V-257863.md) | `RHEL-09-231110` | CAT II | RHEL 9 must mount /dev/shm with the nodev option. |
| [`V-257864`](rules/V-257864.md) | `RHEL-09-231115` | CAT II | RHEL 9 must mount /dev/shm with the noexec option. |
| [`V-257865`](rules/V-257865.md) | `RHEL-09-231120` | CAT II | RHEL 9 must mount /dev/shm with the nosuid option. |
| [`V-257866`](rules/V-257866.md) | `RHEL-09-231125` | CAT II | RHEL 9 must mount /tmp with the nodev option. |
| [`V-257867`](rules/V-257867.md) | `RHEL-09-231130` | CAT II | RHEL 9 must mount /tmp with the noexec option. |
| [`V-257868`](rules/V-257868.md) | `RHEL-09-231135` | CAT II | RHEL 9 must mount /tmp with the nosuid option. |
| [`V-257869`](rules/V-257869.md) | `RHEL-09-231140` | CAT II | RHEL 9 must mount /var with the nodev option. |
| [`V-257870`](rules/V-257870.md) | `RHEL-09-231145` | CAT II | RHEL 9 must mount /var/log with the nodev option. |
| [`V-257871`](rules/V-257871.md) | `RHEL-09-231150` | CAT II | RHEL 9 must mount /var/log with the noexec option. |
| [`V-257872`](rules/V-257872.md) | `RHEL-09-231155` | CAT II | RHEL 9 must mount /var/log with the nosuid option. |
| [`V-257873`](rules/V-257873.md) | `RHEL-09-231160` | CAT II | RHEL 9 must mount /var/log/audit with the nodev option. |
| [`V-257874`](rules/V-257874.md) | `RHEL-09-231165` | CAT II | RHEL 9 must mount /var/log/audit with the noexec option. |
| [`V-257875`](rules/V-257875.md) | `RHEL-09-231170` | CAT II | RHEL 9 must mount /var/log/audit with the nosuid option. |
| [`V-257876`](rules/V-257876.md) | `RHEL-09-231175` | CAT II | RHEL 9 must mount /var/tmp with the nodev option. |
| [`V-257877`](rules/V-257877.md) | `RHEL-09-231180` | CAT II | RHEL 9 must mount /var/tmp with the noexec option. |
| [`V-257878`](rules/V-257878.md) | `RHEL-09-231185` | CAT II | RHEL 9 must mount /var/tmp with the nosuid option. |
| [`V-257879`](rules/V-257879.md) | `RHEL-09-231190` | CAT I | RHEL 9 local disk partitions must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection. |
| [`V-257880`](rules/V-257880.md) | `RHEL-09-231195` | CAT III | RHEL 9 must disable mounting of cramfs. |
| [`V-257881`](rules/V-257881.md) | `RHEL-09-231200` | CAT II | RHEL 9 must prevent special devices on non-root local partitions. |
| [`V-257882`](rules/V-257882.md) | `RHEL-09-232010` | CAT II | RHEL 9 system commands must have mode 755 or less permissive. |
| [`V-257883`](rules/V-257883.md) | `RHEL-09-232015` | CAT II | RHEL 9 library directories must have mode 755 or less permissive. |
| [`V-257884`](rules/V-257884.md) | `RHEL-09-232020` | CAT II | RHEL 9 library files must have mode 755 or less permissive. |
| [`V-257885`](rules/V-257885.md) | `RHEL-09-232025` | CAT II | RHEL 9 /var/log directory must have mode 0755 or less permissive. |
| [`V-257886`](rules/V-257886.md) | `RHEL-09-232030` | CAT II | RHEL 9 /var/log/messages file must have mode 0640 or less permissive. |
| [`V-257887`](rules/V-257887.md) | `RHEL-09-232035` | CAT II | RHEL 9 audit tools must have a mode of 0755 or less permissive. |
| [`V-257888`](rules/V-257888.md) | `RHEL-09-232040` | CAT II | RHEL 9 permissions of cron configuration files and directories must not be modified from the operating system defaults. |
| [`V-257889`](rules/V-257889.md) | `RHEL-09-232045` | CAT II | All RHEL 9 local initialization files must have mode 0740 or less permissive. |
| [`V-257890`](rules/V-257890.md) | `RHEL-09-232050` | CAT II | All RHEL 9 local interactive user home directories must have mode 0750 or less permissive. |
| [`V-257891`](rules/V-257891.md) | `RHEL-09-232055` | CAT II | RHEL 9 /etc/group file must have mode 0644 or less permissive to prevent unauthorized access. |
| [`V-257892`](rules/V-257892.md) | `RHEL-09-232060` | CAT II | RHEL 9 /etc/group- file must have mode 0644 or less permissive to prevent unauthorized access. |
| [`V-257893`](rules/V-257893.md) | `RHEL-09-232065` | CAT II | RHEL 9 /etc/gshadow file must have mode 0000 or less permissive to prevent unauthorized access. |
| [`V-257894`](rules/V-257894.md) | `RHEL-09-232070` | CAT II | RHEL 9 /etc/gshadow- file must have mode 0000 or less permissive to prevent unauthorized access. |
| [`V-257895`](rules/V-257895.md) | `RHEL-09-232075` | CAT II | RHEL 9 /etc/passwd file must have mode 0644 or less permissive to prevent unauthorized access. |
| [`V-257896`](rules/V-257896.md) | `RHEL-09-232080` | CAT II | RHEL 9 /etc/passwd- file must have mode 0644 or less permissive to prevent unauthorized access. |
| [`V-257897`](rules/V-257897.md) | `RHEL-09-232085` | CAT II | RHEL 9 /etc/shadow- file must have mode 0000 or less permissive to prevent unauthorized access. |
| [`V-257898`](rules/V-257898.md) | `RHEL-09-232090` | CAT II | RHEL 9 /etc/group file must be owned by root. |
| [`V-257899`](rules/V-257899.md) | `RHEL-09-232095` | CAT II | RHEL 9 /etc/group file must be group-owned by root. |
| [`V-257900`](rules/V-257900.md) | `RHEL-09-232100` | CAT II | RHEL 9 /etc/group- file must be owned by root. |
| [`V-257901`](rules/V-257901.md) | `RHEL-09-232105` | CAT II | RHEL 9 /etc/group- file must be group-owned by root. |
| [`V-257902`](rules/V-257902.md) | `RHEL-09-232110` | CAT II | RHEL 9 /etc/gshadow file must be owned by root. |
| [`V-257903`](rules/V-257903.md) | `RHEL-09-232115` | CAT II | RHEL 9 /etc/gshadow file must be group-owned by root. |
| [`V-257904`](rules/V-257904.md) | `RHEL-09-232120` | CAT II | RHEL 9 /etc/gshadow- file must be owned by root. |
| [`V-257905`](rules/V-257905.md) | `RHEL-09-232125` | CAT II | RHEL 9 /etc/gshadow- file must be group-owned by root. |
| [`V-257906`](rules/V-257906.md) | `RHEL-09-232130` | CAT II | RHEL 9 /etc/passwd file must be owned by root. |
| [`V-257907`](rules/V-257907.md) | `RHEL-09-232135` | CAT II | RHEL 9 /etc/passwd file must be group-owned by root. |
| [`V-257908`](rules/V-257908.md) | `RHEL-09-232140` | CAT II | RHEL 9 /etc/passwd- file must be owned by root. |
| [`V-257909`](rules/V-257909.md) | `RHEL-09-232145` | CAT II | RHEL 9 /etc/passwd- file must be group-owned by root. |
| [`V-257910`](rules/V-257910.md) | `RHEL-09-232150` | CAT II | RHEL 9 /etc/shadow file must be owned by root. |
| [`V-257911`](rules/V-257911.md) | `RHEL-09-232155` | CAT II | RHEL 9 /etc/shadow file must be group-owned by root. |
| [`V-257912`](rules/V-257912.md) | `RHEL-09-232160` | CAT II | RHEL 9 /etc/shadow- file must be owned by root. |
| [`V-257913`](rules/V-257913.md) | `RHEL-09-232165` | CAT II | RHEL 9 /etc/shadow- file must be group-owned by root. |
| [`V-257914`](rules/V-257914.md) | `RHEL-09-232170` | CAT II | RHEL 9 /var/log directory must be owned by root. |
| [`V-257915`](rules/V-257915.md) | `RHEL-09-232175` | CAT II | RHEL 9 /var/log directory must be group-owned by root. |
| [`V-257916`](rules/V-257916.md) | `RHEL-09-232180` | CAT II | RHEL 9 /var/log/messages file must be owned by root. |
| [`V-257917`](rules/V-257917.md) | `RHEL-09-232185` | CAT II | RHEL 9 /var/log/messages file must be group-owned by root. |
| [`V-257918`](rules/V-257918.md) | `RHEL-09-232190` | CAT II | RHEL 9 system commands must be owned by root. |
| [`V-257919`](rules/V-257919.md) | `RHEL-09-232195` | CAT II | RHEL 9 system commands must be group-owned by root or a system account. |
| [`V-257920`](rules/V-257920.md) | `RHEL-09-232200` | CAT II | RHEL 9 library files must be owned by root. |
| [`V-257921`](rules/V-257921.md) | `RHEL-09-232205` | CAT II | RHEL 9 library files must be group-owned by root or a system account. |
| [`V-257922`](rules/V-257922.md) | `RHEL-09-232210` | CAT II | RHEL 9 library directories must be owned by root. |
| [`V-257923`](rules/V-257923.md) | `RHEL-09-232215` | CAT II | RHEL 9 library directories must be group-owned by root or a system account. |
| [`V-257924`](rules/V-257924.md) | `RHEL-09-232220` | CAT II | RHEL 9 audit tools must be owned by root. |
| [`V-257925`](rules/V-257925.md) | `RHEL-09-232225` | CAT II | RHEL 9 audit tools must be group-owned by root. |
| [`V-257926`](rules/V-257926.md) | `RHEL-09-232230` | CAT II | RHEL 9 cron configuration files directory must be owned by root. |
| [`V-257927`](rules/V-257927.md) | `RHEL-09-232235` | CAT II | RHEL 9 cron configuration files directory must be group-owned by root. |
| [`V-257928`](rules/V-257928.md) | `RHEL-09-232240` | CAT II | All RHEL 9 world-writable directories must be owned by root, sys, bin, or an application user. |
| [`V-257929`](rules/V-257929.md) | `RHEL-09-232245` | CAT II | A sticky bit must be set on all RHEL 9 public directories. |
| [`V-257930`](rules/V-257930.md) | `RHEL-09-232250` | CAT II | All RHEL 9 local files and directories must have a valid group owner. |
| [`V-257931`](rules/V-257931.md) | `RHEL-09-232255` | CAT II | All RHEL 9 local files and directories must have a valid owner. |
| [`V-257932`](rules/V-257932.md) | `RHEL-09-232260` | CAT II | RHEL 9 must be configured so that all system device files are correctly labeled to prevent unauthorized modification. |
| [`V-257934`](rules/V-257934.md) | `RHEL-09-232270` | CAT II | RHEL 9 /etc/shadow file must have mode 0000 to prevent unauthorized access. |
| [`V-257935`](rules/V-257935.md) | `RHEL-09-251010` | CAT II | RHEL 9 must have the firewalld package installed. |
| [`V-257936`](rules/V-257936.md) | `RHEL-09-251015` | CAT II | The firewalld service on RHEL 9 must be active. |
| [`V-257937`](rules/V-257937.md) | `RHEL-09-251020` | CAT II | The RHEL 9 firewall must employ a deny-all, allow-by-exception policy for allowing connections to other systems. |
| [`V-257939`](rules/V-257939.md) | `RHEL-09-251030` | CAT II | RHEL 9 must protect against or limit the effects of denial-of-service (DoS) attacks by ensuring rate-limiting measures on impacted network interfaces are implemented. |
| [`V-257940`](rules/V-257940.md) | `RHEL-09-251035` | CAT II | RHEL 9 must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management (PPSM) Category Assignments List (CAL) and vulnerability assessments. |
| [`V-257941`](rules/V-257941.md) | `RHEL-09-251040` | CAT II | RHEL 9 network interfaces must not be in promiscuous mode. |
| [`V-257942`](rules/V-257942.md) | `RHEL-09-251045` | CAT II | RHEL 9 must enable hardening for the Berkeley Packet Filter just-in-time compiler. |
| [`V-257943`](rules/V-257943.md) | `RHEL-09-252010` | CAT II | RHEL 9 must have the chrony package installed. |
| [`V-257944`](rules/V-257944.md) | `RHEL-09-252015` | CAT II | RHEL 9 chronyd service must be enabled. |
| [`V-257945`](rules/V-257945.md) | `RHEL-09-252020` | CAT II | RHEL 9 must securely compare internal information system clocks at least every 24 hours. |
| [`V-257946`](rules/V-257946.md) | `RHEL-09-252025` | CAT III | RHEL 9 must disable the chrony daemon from acting as a server. |
| [`V-257947`](rules/V-257947.md) | `RHEL-09-252030` | CAT III | RHEL 9 must disable network management of the chrony daemon. |
| [`V-257948`](rules/V-257948.md) | `RHEL-09-252035` | CAT II | RHEL 9 systems using Domain Name Servers (DNS) resolution must have at least two name servers configured. |
| [`V-257949`](rules/V-257949.md) | `RHEL-09-252040` | CAT II | RHEL 9 must configure a DNS processing mode in Network Manager. |
| [`V-257950`](rules/V-257950.md) | `RHEL-09-252045` | CAT II | RHEL 9 must not have unauthorized IP tunnels configured. |
| [`V-257951`](rules/V-257951.md) | `RHEL-09-252050` | CAT II | RHEL 9 must be configured to prevent unrestricted mail relaying. |
| [`V-257953`](rules/V-257953.md) | `RHEL-09-252060` | CAT II | RHEL 9 must forward mail from postmaster to the root account using a postfix alias. |
| [`V-257954`](rules/V-257954.md) | `RHEL-09-252065` | CAT II | RHEL 9 libreswan package must be installed. |
| [`V-257955`](rules/V-257955.md) | `RHEL-09-252070` | CAT I | There must be no shosts.equiv files on RHEL 9. |
| [`V-257956`](rules/V-257956.md) | `RHEL-09-252075` | CAT I | There must be no .shosts files on RHEL 9. |
| [`V-257957`](rules/V-257957.md) | `RHEL-09-253010` | CAT II | RHEL 9 must be configured to use TCP syncookies. |
| [`V-257958`](rules/V-257958.md) | `RHEL-09-253015` | CAT II | RHEL 9 must ignore Internet Protocol version 4 (IPv4) Internet Control Message Protocol (ICMP) redirect messages. |
| [`V-257959`](rules/V-257959.md) | `RHEL-09-253020` | CAT II | RHEL 9 must not forward Internet Protocol version 4 (IPv4) source-routed packets. |
| [`V-257960`](rules/V-257960.md) | `RHEL-09-253025` | CAT II | RHEL 9 must log IPv4 packets with impossible addresses. |
| [`V-257961`](rules/V-257961.md) | `RHEL-09-253030` | CAT II | RHEL 9 must log IPv4 packets with impossible addresses by default. |
| [`V-257962`](rules/V-257962.md) | `RHEL-09-253035` | CAT II | RHEL 9 must use reverse path filtering on all IPv4 interfaces. |
| [`V-257963`](rules/V-257963.md) | `RHEL-09-253040` | CAT II | RHEL 9 must prevent IPv4 Internet Control Message Protocol (ICMP) redirect messages from being accepted. |
| [`V-257964`](rules/V-257964.md) | `RHEL-09-253045` | CAT II | RHEL 9 must not forward IPv4 source-routed packets by default. |
| [`V-257965`](rules/V-257965.md) | `RHEL-09-253050` | CAT II | RHEL 9 must use a reverse-path filter for IPv4 network traffic when possible by default. |
| [`V-257966`](rules/V-257966.md) | `RHEL-09-253055` | CAT II | RHEL 9 must not respond to Internet Control Message Protocol (ICMP) echoes sent to a broadcast address. |
| [`V-257967`](rules/V-257967.md) | `RHEL-09-253060` | CAT II | RHEL 9 must limit the number of bogus Internet Control Message Protocol (ICMP) response errors logs. |
| [`V-257968`](rules/V-257968.md) | `RHEL-09-253065` | CAT II | RHEL 9 must not send Internet Control Message Protocol (ICMP) redirects. |
| [`V-257969`](rules/V-257969.md) | `RHEL-09-253070` | CAT II | RHEL 9 must not allow interfaces to perform Internet Control Message Protocol (ICMP) redirects by default. |
| [`V-257970`](rules/V-257970.md) | `RHEL-09-253075` | CAT II | RHEL 9 must not enable IPv4 packet forwarding unless the system is a router. |
| [`V-257971`](rules/V-257971.md) | `RHEL-09-254010` | CAT II | RHEL 9 must not accept router advertisements on all IPv6 interfaces. |
| [`V-257972`](rules/V-257972.md) | `RHEL-09-254015` | CAT II | RHEL 9 must ignore IPv6 Internet Control Message Protocol (ICMP) redirect messages. |
| [`V-257973`](rules/V-257973.md) | `RHEL-09-254020` | CAT II | RHEL 9 must not forward IPv6 source-routed packets. |
| [`V-257974`](rules/V-257974.md) | `RHEL-09-254025` | CAT II | RHEL 9 must not enable IPv6 packet forwarding unless the system is a router. |
| [`V-257975`](rules/V-257975.md) | `RHEL-09-254030` | CAT II | RHEL 9 must not accept router advertisements on all IPv6 interfaces by default. |
| [`V-257976`](rules/V-257976.md) | `RHEL-09-254035` | CAT II | RHEL 9 must prevent IPv6 Internet Control Message Protocol (ICMP) redirect messages from being accepted. |
| [`V-257977`](rules/V-257977.md) | `RHEL-09-254040` | CAT II | RHEL 9 must not forward IPv6 source-routed packets by default. |
| [`V-257978`](rules/V-257978.md) | `RHEL-09-255010` | CAT II | All RHEL 9 networked systems must have SSH installed. |
| [`V-257979`](rules/V-257979.md) | `RHEL-09-255015` | CAT II | All RHEL 9 networked systems must have and implement SSH to protect the confidentiality and integrity of transmitted and received information, as well as information during preparation for transmission. |
| [`V-257980`](rules/V-257980.md) | `RHEL-09-255020` | CAT II | RHEL 9 must have the openssh-clients package installed. |
| [`V-257981`](rules/V-257981.md) | `RHEL-09-255025` | CAT II | RHEL 9 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a SSH logon. |
| [`V-257982`](rules/V-257982.md) | `RHEL-09-255030` | CAT II | RHEL 9 must log SSH connection attempts and failures to the server. |
| [`V-257983`](rules/V-257983.md) | `RHEL-09-255035` | CAT II | RHEL 9 SSHD must accept public key authentication. |
| [`V-257984`](rules/V-257984.md) | `RHEL-09-255040` | CAT I | RHEL 9 SSHD must not allow blank passwords. |
| [`V-257985`](rules/V-257985.md) | `RHEL-09-255045` | CAT II | RHEL 9 must not permit direct logons to the root account using remote access via SSH. |
| [`V-257986`](rules/V-257986.md) | `RHEL-09-255050` | CAT I | RHEL 9 must enable the Pluggable Authentication Module (PAM) interface for SSHD. |
| [`V-257989`](rules/V-257989.md) | `RHEL-09-255065` | CAT I | The RHEL 9 SSH server must be configured to use only DoW-approved encryption ciphers employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections. |
| [`V-257991`](rules/V-257991.md) | `RHEL-09-255075` | CAT I | The RHEL 9 SSH server must be configured to use only Message Authentication Codes (MACs) employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH server connections. |
| [`V-257992`](rules/V-257992.md) | `RHEL-09-255080` | CAT II | RHEL 9 must not allow a noncertificate trusted host SSH logon to the system. |
| [`V-257993`](rules/V-257993.md) | `RHEL-09-255085` | CAT II | RHEL 9 must not allow users to override SSH environment variables. |
| [`V-257994`](rules/V-257994.md) | `RHEL-09-255090` | CAT II | RHEL 9 must force a frequent session key renegotiation for SSH connections to the server. |
| [`V-257995`](rules/V-257995.md) | `RHEL-09-255095` | CAT II | RHEL 9 must be configured so that all network connections associated with SSH traffic terminate after becoming unresponsive. |
| [`V-257996`](rules/V-257996.md) | `RHEL-09-255100` | CAT II | RHEL 9 must be configured so that all network connections associated with SSH traffic are terminated after 10 minutes of becoming unresponsive. |
| [`V-257997`](rules/V-257997.md) | `RHEL-09-255105` | CAT II | RHEL 9 SSH server configuration file must be group-owned by root. |
| [`V-257998`](rules/V-257998.md) | `RHEL-09-255110` | CAT II | The RHEL 9 SSH server configuration file must be owned by root. |
| [`V-257999`](rules/V-257999.md) | `RHEL-09-255115` | CAT II | RHEL 9 SSH server configuration files' permissions must not be modified. |
| [`V-258000`](rules/V-258000.md) | `RHEL-09-255120` | CAT II | RHEL 9 SSH private host key files must have mode 0600 or less permissive. |
| [`V-258001`](rules/V-258001.md) | `RHEL-09-255125` | CAT II | RHEL 9 SSH public host key files must have mode 0644 or less permissive. |
| [`V-258003`](rules/V-258003.md) | `RHEL-09-255135` | CAT II | RHEL 9 SSH daemon must not allow GSSAPI authentication. |
| [`V-258004`](rules/V-258004.md) | `RHEL-09-255140` | CAT II | RHEL 9 SSH daemon must not allow Kerberos authentication. |
| [`V-258005`](rules/V-258005.md) | `RHEL-09-255145` | CAT II | RHEL 9 SSH daemon must not allow rhosts authentication. |
| [`V-258006`](rules/V-258006.md) | `RHEL-09-255150` | CAT II | RHEL 9 SSH daemon must not allow known hosts authentication. |
| [`V-258007`](rules/V-258007.md) | `RHEL-09-255155` | CAT II | RHEL 9 SSH daemon must disable remote X connections for interactive users. |
| [`V-258008`](rules/V-258008.md) | `RHEL-09-255160` | CAT II | RHEL 9 SSH daemon must perform strict mode checking of home directory configuration files. |
| [`V-258009`](rules/V-258009.md) | `RHEL-09-255165` | CAT II | RHEL 9 SSH daemon must display the date and time of the last successful account logon upon an SSH logon. |
| [`V-258011`](rules/V-258011.md) | `RHEL-09-255175` | CAT II | RHEL 9 SSH daemon must prevent remote hosts from connecting to the proxy display. |
| [`V-258012`](rules/V-258012.md) | `RHEL-09-271010` | CAT II | RHEL 9 must enable the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a graphical user logon. |
| [`V-258013`](rules/V-258013.md) | `RHEL-09-271015` | CAT II | RHEL 9 must prevent a user from overriding the banner-message-enable setting for the graphical user interface. |
| [`V-258014`](rules/V-258014.md) | `RHEL-09-271020` | CAT II | RHEL 9 must disable the graphical user interface automount function unless required. |
| [`V-258015`](rules/V-258015.md) | `RHEL-09-271025` | CAT II | RHEL 9 must prevent a user from overriding the disabling of the graphical user interface automount function. |
| [`V-258016`](rules/V-258016.md) | `RHEL-09-271030` | CAT II | RHEL 9 must disable the graphical user interface autorun function unless required. |
| [`V-258017`](rules/V-258017.md) | `RHEL-09-271035` | CAT II | RHEL 9 must prevent a user from overriding the disabling of the graphical user interface autorun function. |
| [`V-258018`](rules/V-258018.md) | `RHEL-09-271040` | CAT I | RHEL 9 must not allow unattended or automatic logon via the graphical user interface. |
| [`V-258019`](rules/V-258019.md) | `RHEL-09-271045` | CAT II | RHEL 9 must be able to initiate directly a session lock for all connection types using smart card when the smart card is removed. |
| [`V-258020`](rules/V-258020.md) | `RHEL-09-271050` | CAT II | RHEL 9 must prevent a user from overriding the disabling of the graphical user smart card removal action. |
| [`V-258021`](rules/V-258021.md) | `RHEL-09-271055` | CAT II | RHEL 9 must enable a user session lock until that user re-establishes access using established identification and authentication procedures for graphical user sessions. |
| [`V-258022`](rules/V-258022.md) | `RHEL-09-271060` | CAT II | RHEL 9 must prevent a user from overriding the screensaver lock-enabled setting for the graphical user interface. |
| [`V-258023`](rules/V-258023.md) | `RHEL-09-271065` | CAT II | RHEL 9 must automatically lock graphical user sessions after 10 minutes of inactivity. |
| [`V-258024`](rules/V-258024.md) | `RHEL-09-271070` | CAT II | RHEL 9 must prevent a user from overriding the session idle-delay setting for the graphical user interface. |
| [`V-258025`](rules/V-258025.md) | `RHEL-09-271075` | CAT II | RHEL 9 must initiate a session lock for graphical user interfaces when the screensaver is activated. |
| [`V-258026`](rules/V-258026.md) | `RHEL-09-271080` | CAT II | RHEL 9 must prevent a user from overriding the session lock-delay setting for the graphical user interface. |
| [`V-258027`](rules/V-258027.md) | `RHEL-09-271085` | CAT II | RHEL 9 must conceal, via the session lock, information previously visible on the display with a publicly viewable image. |
| [`V-258028`](rules/V-258028.md) | `RHEL-09-271090` | CAT II | RHEL 9 effective dconf policy must match the policy keyfiles. |
| [`V-258029`](rules/V-258029.md) | `RHEL-09-271095` | CAT II | RHEL 9 must disable the ability of a user to restart the system from the login screen. |
| [`V-258030`](rules/V-258030.md) | `RHEL-09-271100` | CAT II | RHEL 9 must prevent a user from overriding the disable-restart-buttons setting for the graphical user interface. |
| [`V-258031`](rules/V-258031.md) | `RHEL-09-271105` | CAT II | RHEL 9 must disable the ability of a user to accidentally press Ctrl-Alt-Del and cause a system to shut down or reboot. |
| [`V-258032`](rules/V-258032.md) | `RHEL-09-271110` | CAT II | RHEL 9 must prevent a user from overriding the Ctrl-Alt-Del sequence settings for the graphical user interface. |
| [`V-258033`](rules/V-258033.md) | `RHEL-09-271115` | CAT II | RHEL 9 must disable the user list at logon for graphical user interfaces. |
| [`V-258034`](rules/V-258034.md) | `RHEL-09-291010` | CAT II | RHEL 9 must be configured to disable USB mass storage. |
| [`V-258035`](rules/V-258035.md) | `RHEL-09-291015` | CAT II | RHEL 9 must have the USBGuard package installed. |
| [`V-258036`](rules/V-258036.md) | `RHEL-09-291020` | CAT II | RHEL 9 must have the USBGuard package enabled. |
| [`V-258037`](rules/V-258037.md) | `RHEL-09-291025` | CAT III | RHEL 9 must enable Linux audit logging for the USBGuard daemon. |
| [`V-258038`](rules/V-258038.md) | `RHEL-09-291030` | CAT II | RHEL 9 must block unauthorized peripherals before establishing a connection. |
| [`V-258039`](rules/V-258039.md) | `RHEL-09-291035` | CAT II | RHEL 9 Bluetooth must be disabled. |
| [`V-258040`](rules/V-258040.md) | `RHEL-09-291040` | CAT II | RHEL 9 wireless network adapters must be disabled. |
| [`V-258041`](rules/V-258041.md) | `RHEL-09-411010` | CAT II | RHEL 9 user account passwords for new users or password changes must have a 180-day maximum password lifetime restriction in /etc/login.defs. |
| [`V-258042`](rules/V-258042.md) | `RHEL-09-411015` | CAT II | RHEL 9 user account passwords must have a 180-day maximum password lifetime restriction. |
| [`V-258043`](rules/V-258043.md) | `RHEL-09-411020` | CAT II | All RHEL 9 local interactive user accounts must be assigned a home directory upon creation. |
| [`V-258044`](rules/V-258044.md) | `RHEL-09-411025` | CAT II | RHEL 9 must set the umask value to 077 for all local interactive user accounts. |
| [`V-258045`](rules/V-258045.md) | `RHEL-09-411030` | CAT II | RHEL 9 duplicate User IDs (UIDs) must not exist for interactive users. |
| [`V-258046`](rules/V-258046.md) | `RHEL-09-411035` | CAT II | RHEL 9 system accounts must not have an interactive login shell. |
| [`V-258047`](rules/V-258047.md) | `RHEL-09-411040` | CAT II | RHEL 9 must automatically expire temporary accounts within 72 hours. |
| [`V-258048`](rules/V-258048.md) | `RHEL-09-411045` | CAT II | All RHEL 9 interactive users must have a primary group that exists. |
| [`V-258049`](rules/V-258049.md) | `RHEL-09-411050` | CAT II | RHEL 9 must disable account identifiers (individuals, groups, roles, and devices) after 35 days of inactivity. |
| [`V-258050`](rules/V-258050.md) | `RHEL-09-411055` | CAT II | Executable search paths within the initialization files of all local interactive RHEL 9 users must only contain paths that resolve to the system default or the users home directory. |
| [`V-258051`](rules/V-258051.md) | `RHEL-09-411060` | CAT II | All RHEL 9 local interactive users must have a home directory assigned in the /etc/passwd file. |
| [`V-258052`](rules/V-258052.md) | `RHEL-09-411065` | CAT II | All RHEL 9 local interactive user home directories defined in the /etc/passwd file must exist. |
| [`V-258053`](rules/V-258053.md) | `RHEL-09-411070` | CAT II | All RHEL 9 local interactive user home directories must be group-owned by the home directory owner's primary group. |
| [`V-258054`](rules/V-258054.md) | `RHEL-09-411075` | CAT II | RHEL 9 must automatically lock an account when three unsuccessful logon attempts occur. |
| [`V-258055`](rules/V-258055.md) | `RHEL-09-411080` | CAT II | RHEL 9 must automatically lock the root account until the root account is released by an administrator when three unsuccessful logon attempts occur during a 15-minute time period. |
| [`V-258056`](rules/V-258056.md) | `RHEL-09-411085` | CAT II | RHEL 9 must automatically lock an account when three unsuccessful logon attempts occur during a 15-minute time period. |
| [`V-258057`](rules/V-258057.md) | `RHEL-09-411090` | CAT II | RHEL 9 must maintain an account lock until the locked account is released by an administrator. |
| [`V-258058`](rules/V-258058.md) | `RHEL-09-411095` | CAT II | RHEL 9 must not have unauthorized accounts. |
| [`V-258059`](rules/V-258059.md) | `RHEL-09-411100` | CAT I | The root account must be the only account having unrestricted access to RHEL 9 system. |
| [`V-258060`](rules/V-258060.md) | `RHEL-09-411105` | CAT II | RHEL 9 must ensure account lockouts persist. |
| [`V-258061`](rules/V-258061.md) | `RHEL-09-411110` | CAT II | RHEL 9 groups must have unique Group ID (GID). |
| [`V-258068`](rules/V-258068.md) | `RHEL-09-412035` | CAT II | RHEL 9 must automatically exit interactive command shell user sessions after 10 minutes of inactivity. |
| [`V-258069`](rules/V-258069.md) | `RHEL-09-412040` | CAT III | RHEL 9 must limit the number of concurrent sessions to ten for all accounts and/or account types. |
| [`V-258070`](rules/V-258070.md) | `RHEL-09-412045` | CAT II | RHEL 9 must log username information when unsuccessful logon attempts occur. |
| [`V-258071`](rules/V-258071.md) | `RHEL-09-412050` | CAT II | RHEL 9 must enforce a delay of at least four seconds between logon prompts following a failed logon attempt. |
| [`V-258072`](rules/V-258072.md) | `RHEL-09-412055` | CAT II | RHEL 9 must define default permissions for the bash shell. |
| [`V-258073`](rules/V-258073.md) | `RHEL-09-412060` | CAT II | RHEL 9 must define default permissions for the c shell. |
| [`V-258074`](rules/V-258074.md) | `RHEL-09-412065` | CAT II | RHEL 9 must define default permissions for all authenticated users in such a way that the user can only read and modify their own files. |
| [`V-258075`](rules/V-258075.md) | `RHEL-09-412070` | CAT II | RHEL 9 must define default permissions for the system default profile. |
| [`V-258077`](rules/V-258077.md) | `RHEL-09-412080` | CAT II | RHEL 9 must terminate idle user sessions. |
| [`V-258078`](rules/V-258078.md) | `RHEL-09-431010` | CAT I | RHEL 9 must use a Linux Security Module configured to enforce limits on system services. |
| [`V-258079`](rules/V-258079.md) | `RHEL-09-431015` | CAT II | RHEL 9 must enable the SELinux targeted policy. |
| [`V-258080`](rules/V-258080.md) | `RHEL-09-431020` | CAT II | RHEL 9 must configure SELinux context type to allow the use of a nondefault faillock tally directory. |
| [`V-258081`](rules/V-258081.md) | `RHEL-09-431025` | CAT II | RHEL 9 must have policycoreutils package installed. |
| [`V-258082`](rules/V-258082.md) | `RHEL-09-431030` | CAT II | RHEL 9 policycoreutils-python-utils package must be installed. |
| [`V-258083`](rules/V-258083.md) | `RHEL-09-432010` | CAT II | RHEL 9 must have the sudo package installed. |
| [`V-258084`](rules/V-258084.md) | `RHEL-09-432015` | CAT II | RHEL 9 must require reauthentication when using the "sudo" command. |
| [`V-258085`](rules/V-258085.md) | `RHEL-09-432020` | CAT II | RHEL 9 must use the invoking user's password for privilege escalation when using "sudo". |
| [`V-258086`](rules/V-258086.md) | `RHEL-09-432025` | CAT II | RHEL 9 must require users to reauthenticate for privilege escalation. |
| [`V-258087`](rules/V-258087.md) | `RHEL-09-432030` | CAT II | RHEL 9 must restrict privilege elevation to authorized personnel. |
| [`V-258088`](rules/V-258088.md) | `RHEL-09-432035` | CAT II | RHEL 9 must restrict the use of the "su" command. |
| [`V-258089`](rules/V-258089.md) | `RHEL-09-433010` | CAT II | RHEL 9 fapolicy module must be installed. |
| [`V-258090`](rules/V-258090.md) | `RHEL-09-433015` | CAT II | RHEL 9 fapolicy module must be enabled. |
| [`V-258091`](rules/V-258091.md) | `RHEL-09-611010` | CAT II | RHEL 9 must ensure the password complexity module in the system-auth file is configured for three retries or less. |
| [`V-258094`](rules/V-258094.md) | `RHEL-09-611025` | CAT I | RHEL 9 must not allow blank or null passwords. |
| [`V-258095`](rules/V-258095.md) | `RHEL-09-611030` | CAT II | RHEL 9 must configure the use of the pam_faillock.so module in the /etc/pam.d/system-auth file. |
| [`V-258096`](rules/V-258096.md) | `RHEL-09-611035` | CAT II | RHEL 9 must configure the use of the pam_faillock.so module in the /etc/pam.d/password-auth file. |
| [`V-258097`](rules/V-258097.md) | `RHEL-09-611040` | CAT II | RHEL 9 must ensure the password complexity module is enabled in the password-auth file. |
| [`V-258098`](rules/V-258098.md) | `RHEL-09-611045` | CAT II | RHEL 9 must ensure the password complexity module is enabled in the system-auth file. |
| [`V-258099`](rules/V-258099.md) | `RHEL-09-611050` | CAT II | RHEL 9 password-auth must be configured to use a sufficient number of hashing rounds. |
| [`V-258100`](rules/V-258100.md) | `RHEL-09-611055` | CAT II | RHEL 9 system-auth must be configured to use a sufficient number of hashing rounds. |
| [`V-258101`](rules/V-258101.md) | `RHEL-09-611060` | CAT II | RHEL 9 must enforce password complexity rules for the root account. |
| [`V-258102`](rules/V-258102.md) | `RHEL-09-611065` | CAT II | RHEL 9 must enforce password complexity by requiring that at least one lowercase character be used. |
| [`V-258103`](rules/V-258103.md) | `RHEL-09-611070` | CAT II | RHEL 9 must enforce password complexity by requiring that at least one numeric character be used. |
| [`V-258104`](rules/V-258104.md) | `RHEL-09-611075` | CAT II | RHEL 9 passwords for new users or password changes must have a 24 hours minimum password lifetime restriction in /etc/login.defs. |
| [`V-258105`](rules/V-258105.md) | `RHEL-09-611080` | CAT II | RHEL 9 passwords must have a 24 hours minimum password lifetime restriction in /etc/shadow. |
| [`V-258106`](rules/V-258106.md) | `RHEL-09-611085` | CAT II | RHEL 9 must require users to provide a password for privilege escalation. |
| [`V-258107`](rules/V-258107.md) | `RHEL-09-611090` | CAT II | RHEL 9 passwords must be created with a minimum of 15 characters. |
| [`V-258109`](rules/V-258109.md) | `RHEL-09-611100` | CAT II | RHEL 9 must enforce password complexity by requiring that at least one special character be used. |
| [`V-258110`](rules/V-258110.md) | `RHEL-09-611105` | CAT II | RHEL 9 must prevent the use of dictionary words for passwords. |
| [`V-258111`](rules/V-258111.md) | `RHEL-09-611110` | CAT II | RHEL 9 must enforce password complexity by requiring that at least one uppercase character be used. |
| [`V-258112`](rules/V-258112.md) | `RHEL-09-611115` | CAT II | RHEL 9 must require the change of at least eight characters when passwords are changed. |
| [`V-258113`](rules/V-258113.md) | `RHEL-09-611120` | CAT II | RHEL 9 must require the maximum number of repeating characters of the same character class be limited to four when passwords are changed. |
| [`V-258114`](rules/V-258114.md) | `RHEL-09-611125` | CAT II | RHEL 9 must require the maximum number of repeating characters be limited to three when passwords are changed. |
| [`V-258115`](rules/V-258115.md) | `RHEL-09-611130` | CAT II | RHEL 9 must require the change of at least four character classes when passwords are changed. |
| [`V-258116`](rules/V-258116.md) | `RHEL-09-611135` | CAT II | RHEL 9 must be configured so that user and group account administration utilities are configured to store only encrypted representations of passwords. |
| [`V-258117`](rules/V-258117.md) | `RHEL-09-611140` | CAT II | RHEL 9 must be configured to use the shadow file to store only encrypted representations of passwords. |
| [`V-258118`](rules/V-258118.md) | `RHEL-09-611145` | CAT II | RHEL 9 must not be configured to bypass password requirements for privilege escalation. |
| [`V-258120`](rules/V-258120.md) | `RHEL-09-611155` | CAT II | RHEL 9 must not have accounts configured with blank or null passwords. |
| [`V-258121`](rules/V-258121.md) | `RHEL-09-611160` | CAT II | RHEL 9 must use the common access card (CAC) smart card driver. |
| [`V-258122`](rules/V-258122.md) | `RHEL-09-611165` | CAT II | RHEL 9 must enable certificate based smart card authentication. |
| [`V-258123`](rules/V-258123.md) | `RHEL-09-611170` | CAT II | RHEL 9 must implement certificate status checking for multifactor authentication. |
| [`V-258124`](rules/V-258124.md) | `RHEL-09-611175` | CAT II | RHEL 9 must have the pcsc-lite package installed. |
| [`V-258125`](rules/V-258125.md) | `RHEL-09-611180` | CAT II | The pcscd socket on RHEL 9 must be active. |
| [`V-258126`](rules/V-258126.md) | `RHEL-09-611185` | CAT II | RHEL 9 must have the opensc package installed. |
| [`V-258127`](rules/V-258127.md) | `RHEL-09-611190` | CAT II | RHEL 9, for PKI-based authentication, must enforce authorized access to the corresponding private key. |
| [`V-258128`](rules/V-258128.md) | `RHEL-09-611195` | CAT II | RHEL 9 must require authentication to access emergency mode. |
| [`V-258129`](rules/V-258129.md) | `RHEL-09-611200` | CAT II | RHEL 9 must require authentication to access single-user mode. |
| [`V-258131`](rules/V-258131.md) | `RHEL-09-631010` | CAT II | RHEL 9, for PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor. |
| [`V-258132`](rules/V-258132.md) | `RHEL-09-631015` | CAT II | RHEL 9 must map the authenticated identity to the user or group account for PKI-based authentication. |
| [`V-258133`](rules/V-258133.md) | `RHEL-09-631020` | CAT II | RHEL 9 must prohibit the use of cached authenticators after one day. |
| [`V-258134`](rules/V-258134.md) | `RHEL-09-651010` | CAT II | RHEL 9 must have the AIDE package installed. |
| [`V-258135`](rules/V-258135.md) | `RHEL-09-651015` | CAT II | RHEL 9 must routinely check the baseline configuration for unauthorized changes and notify the system administrator when anomalies in the operation of any security functions are discovered. |
| [`V-258136`](rules/V-258136.md) | `RHEL-09-651020` | CAT II | RHEL 9 must use a file integrity tool that is configured to use FIPS 140-3-approved cryptographic hashes for validating file contents and directories. |
| [`V-258137`](rules/V-258137.md) | `RHEL-09-651025` | CAT II | RHEL 9 must use cryptographic mechanisms to protect the integrity of audit tools. |
| [`V-258138`](rules/V-258138.md) | `RHEL-09-651030` | CAT III | RHEL 9 must be configured so that the file integrity tool verifies Access Control Lists (ACLs). |
| [`V-258139`](rules/V-258139.md) | `RHEL-09-651035` | CAT III | RHEL 9 must be configured so that the file integrity tool verifies extended attributes. |
| [`V-258140`](rules/V-258140.md) | `RHEL-09-652010` | CAT II | RHEL 9 must have the rsyslog package installed. |
| [`V-258141`](rules/V-258141.md) | `RHEL-09-652015` | CAT II | RHEL 9 must have the packages required for encrypting offloaded audit logs installed. |
| [`V-258142`](rules/V-258142.md) | `RHEL-09-652020` | CAT II | The rsyslog service on RHEL 9 must be active. |
| [`V-258143`](rules/V-258143.md) | `RHEL-09-652025` | CAT II | RHEL 9 must be configured so that the rsyslog daemon does not accept log messages from other servers unless the server is being used for log aggregation. |
| [`V-258144`](rules/V-258144.md) | `RHEL-09-652030` | CAT II | All RHEL 9 remote access methods must be monitored. |
| [`V-258146`](rules/V-258146.md) | `RHEL-09-652040` | CAT II | RHEL 9 must authenticate the remote logging server for offloading audit logs via rsyslog. |
| [`V-258147`](rules/V-258147.md) | `RHEL-09-652045` | CAT II | RHEL 9 must encrypt the transfer of audit records offloaded onto a different system or media from the system being audited via rsyslog. |
| [`V-258148`](rules/V-258148.md) | `RHEL-09-652050` | CAT II | RHEL 9 must encrypt via the gtls driver the transfer of audit records offloaded onto a different system or media from the system being audited via rsyslog. |
| [`V-258149`](rules/V-258149.md) | `RHEL-09-652055` | CAT II | RHEL 9 must be configured to forward audit records via TCP to a different system or media from the system being audited via rsyslog. |
| [`V-258150`](rules/V-258150.md) | `RHEL-09-652060` | CAT II | RHEL 9 must use cron logging. |
| [`V-258151`](rules/V-258151.md) | `RHEL-09-653010` | CAT II | RHEL 9 audit package must be installed. |
| [`V-258152`](rules/V-258152.md) | `RHEL-09-653015` | CAT II | RHEL 9 audit service must be enabled. |
| [`V-258153`](rules/V-258153.md) | `RHEL-09-653020` | CAT II | RHEL 9 audit system must take appropriate action when an error writing to the audit storage volume occurs. |
| [`V-258154`](rules/V-258154.md) | `RHEL-09-653025` | CAT II | RHEL 9 audit system must take appropriate action when the audit storage volume is full. |
| [`V-258155`](rules/V-258155.md) | `RHEL-09-653030` | CAT II | RHEL 9 must allocate audit record storage capacity to store at least one week's worth of audit records. |
| [`V-258156`](rules/V-258156.md) | `RHEL-09-653035` | CAT II | RHEL 9 must take action when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity. |
| [`V-258157`](rules/V-258157.md) | `RHEL-09-653040` | CAT II | RHEL 9 must notify the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated audit record storage volume reaches 75 percent utilization. |
| [`V-258158`](rules/V-258158.md) | `RHEL-09-653045` | CAT II | RHEL 9 must take action when allocated audit record storage volume reaches 95 percent of the audit record storage capacity. |
| [`V-258159`](rules/V-258159.md) | `RHEL-09-653050` | CAT II | RHEL 9 must take action when allocated audit record storage volume reaches 95 percent of the repository maximum audit record storage capacity. |
| [`V-258160`](rules/V-258160.md) | `RHEL-09-653055` | CAT II | RHEL 9 audit system must take appropriate action when the audit files have reached maximum size. |
| [`V-258161`](rules/V-258161.md) | `RHEL-09-653060` | CAT II | RHEL 9 must label all offloaded audit logs before sending them to the central log server. |
| [`V-258162`](rules/V-258162.md) | `RHEL-09-653065` | CAT II | RHEL 9 must take appropriate action when the internal event queue is full. |
| [`V-258163`](rules/V-258163.md) | `RHEL-09-653070` | CAT II | RHEL 9 System Administrator (SA) and/or information system security officer (ISSO) (at a minimum) must be alerted of an audit processing failure event. |
| [`V-258164`](rules/V-258164.md) | `RHEL-09-653075` | CAT II | RHEL 9 audit system must audit local events. |
| [`V-258165`](rules/V-258165.md) | `RHEL-09-653080` | CAT II | RHEL 9 audit logs must be group-owned by root or by a restricted logging group to prevent unauthorized read access. |
| [`V-258166`](rules/V-258166.md) | `RHEL-09-653085` | CAT II | RHEL 9 audit log directory must be owned by root to prevent unauthorized read access. |
| [`V-258167`](rules/V-258167.md) | `RHEL-09-653090` | CAT II | RHEL 9 audit logs file must have mode 0600 or less permissive to prevent unauthorized access to the audit log. |
| [`V-258168`](rules/V-258168.md) | `RHEL-09-653095` | CAT II | RHEL 9 must periodically flush audit records to disk to prevent the loss of audit records. |
| [`V-258169`](rules/V-258169.md) | `RHEL-09-653100` | CAT II | RHEL 9 must produce audit records containing information to establish the identity of any individual or process associated with the event. |
| [`V-258170`](rules/V-258170.md) | `RHEL-09-653105` | CAT II | RHEL 9 must write audit records to disk. |
| [`V-258171`](rules/V-258171.md) | `RHEL-09-653110` | CAT II | RHEL 9 must allow only the information system security manager (ISSM) (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited. |
| [`V-258173`](rules/V-258173.md) | `RHEL-09-653120` | CAT III | RHEL 9 must allocate an audit_backlog_limit of sufficient size to capture processes that start prior to the audit daemon. |
| [`V-258174`](rules/V-258174.md) | `RHEL-09-653125` | CAT II | RHEL 9 must have mail aliases to notify the information system security officer (ISSO) and system administrator (SA) (at a minimum) in the event of an audit processing failure. |
| [`V-258175`](rules/V-258175.md) | `RHEL-09-653130` | CAT II | RHEL 9 audispd-plugins package must be installed. |
| [`V-258176`](rules/V-258176.md) | `RHEL-09-654010` | CAT II | RHEL 9 must audit uses of the "execve" system call. |
| [`V-258177`](rules/V-258177.md) | `RHEL-09-654015` | CAT II | RHEL 9 must audit all uses of the chmod, fchmod, and fchmodat system calls. |
| [`V-258178`](rules/V-258178.md) | `RHEL-09-654020` | CAT II | RHEL 9 must audit all uses of the chown, fchown, fchownat, and lchown system calls. |
| [`V-258179`](rules/V-258179.md) | `RHEL-09-654025` | CAT II | RHEL 9 must audit all uses of the setxattr, fsetxattr, lsetxattr, removexattr, fremovexattr, and lremovexattr system calls. |
| [`V-258180`](rules/V-258180.md) | `RHEL-09-654030` | CAT II | RHEL 9 must audit all uses of umount system calls. |
| [`V-258181`](rules/V-258181.md) | `RHEL-09-654035` | CAT II | RHEL 9 must audit all uses of the chacl command. |
| [`V-258182`](rules/V-258182.md) | `RHEL-09-654040` | CAT II | RHEL 9 must audit all uses of the setfacl command. |
| [`V-258183`](rules/V-258183.md) | `RHEL-09-654045` | CAT II | RHEL 9 must audit all uses of the chcon command. |
| [`V-258184`](rules/V-258184.md) | `RHEL-09-654050` | CAT II | RHEL 9 must audit all uses of the semanage command. |
| [`V-258185`](rules/V-258185.md) | `RHEL-09-654055` | CAT II | RHEL 9 must audit all uses of the setfiles command. |
| [`V-258186`](rules/V-258186.md) | `RHEL-09-654060` | CAT II | RHEL 9 must audit all uses of the setsebool command. |
| [`V-258187`](rules/V-258187.md) | `RHEL-09-654065` | CAT II | RHEL 9 must audit all uses of the rename, unlink, rmdir, renameat, and unlinkat system calls. |
| [`V-258188`](rules/V-258188.md) | `RHEL-09-654070` | CAT II | RHEL 9 must audit all uses of the truncate, ftruncate, creat, open, openat, and open_by_handle_at system calls. |
| [`V-258189`](rules/V-258189.md) | `RHEL-09-654075` | CAT II | RHEL 9 must audit all uses of the delete_module system call. |
| [`V-258190`](rules/V-258190.md) | `RHEL-09-654080` | CAT II | RHEL 9 must audit all uses of the init_module and finit_module system calls. |
| [`V-258191`](rules/V-258191.md) | `RHEL-09-654085` | CAT II | RHEL 9 must audit all uses of the chage command. |
| [`V-258192`](rules/V-258192.md) | `RHEL-09-654090` | CAT II | RHEL 9 must audit all uses of the chsh command. |
| [`V-258193`](rules/V-258193.md) | `RHEL-09-654095` | CAT II | RHEL 9 must audit all uses of the crontab command. |
| [`V-258194`](rules/V-258194.md) | `RHEL-09-654100` | CAT II | RHEL 9 must audit all uses of the gpasswd command. |
| [`V-258195`](rules/V-258195.md) | `RHEL-09-654105` | CAT II | RHEL 9 must audit all uses of the kmod command. |
| [`V-258196`](rules/V-258196.md) | `RHEL-09-654110` | CAT II | RHEL 9 must audit all uses of the newgrp command. |
| [`V-258197`](rules/V-258197.md) | `RHEL-09-654115` | CAT II | RHEL 9 must audit all uses of the pam_timestamp_check command. |
| [`V-258198`](rules/V-258198.md) | `RHEL-09-654120` | CAT II | RHEL 9 must audit all uses of the passwd command. |
| [`V-258199`](rules/V-258199.md) | `RHEL-09-654125` | CAT II | RHEL 9 must audit all uses of the postdrop command. |
| [`V-258200`](rules/V-258200.md) | `RHEL-09-654130` | CAT II | RHEL 9 must audit all uses of the postqueue command. |
| [`V-258201`](rules/V-258201.md) | `RHEL-09-654135` | CAT II | RHEL 9 must audit all uses of the ssh-agent command. |
| [`V-258202`](rules/V-258202.md) | `RHEL-09-654140` | CAT II | RHEL 9 must audit all uses of the ssh-keysign command. |
| [`V-258203`](rules/V-258203.md) | `RHEL-09-654145` | CAT II | RHEL 9 must audit all uses of the su command. |
| [`V-258204`](rules/V-258204.md) | `RHEL-09-654150` | CAT II | RHEL 9 must audit all uses of the sudo command. |
| [`V-258205`](rules/V-258205.md) | `RHEL-09-654155` | CAT II | RHEL 9 must audit all uses of the sudoedit command. |
| [`V-258206`](rules/V-258206.md) | `RHEL-09-654160` | CAT II | RHEL 9 must audit all uses of the unix_chkpwd command. |
| [`V-258207`](rules/V-258207.md) | `RHEL-09-654165` | CAT II | RHEL 9 must audit all uses of the unix_update command. |
| [`V-258208`](rules/V-258208.md) | `RHEL-09-654170` | CAT II | RHEL 9 must audit all uses of the userhelper command. |
| [`V-258209`](rules/V-258209.md) | `RHEL-09-654175` | CAT II | RHEL 9 must audit all uses of the usermod command. |
| [`V-258210`](rules/V-258210.md) | `RHEL-09-654180` | CAT II | RHEL 9 must audit all uses of the mount command. |
| [`V-258211`](rules/V-258211.md) | `RHEL-09-654185` | CAT II | Successful/unsuccessful uses of the init command in RHEL 9 must generate an audit record. |
| [`V-258212`](rules/V-258212.md) | `RHEL-09-654190` | CAT II | Successful/unsuccessful uses of the poweroff command in RHEL 9 must generate an audit record. |
| [`V-258213`](rules/V-258213.md) | `RHEL-09-654195` | CAT II | Successful/unsuccessful uses of the reboot command in RHEL 9 must generate an audit record. |
| [`V-258214`](rules/V-258214.md) | `RHEL-09-654200` | CAT II | Successful/unsuccessful uses of the shutdown command in RHEL 9 must generate an audit record. |
| [`V-258215`](rules/V-258215.md) | `RHEL-09-654205` | CAT II | Successful/unsuccessful uses of the umount system call in RHEL 9 must generate an audit record. |
| [`V-258216`](rules/V-258216.md) | `RHEL-09-654210` | CAT II | Successful/unsuccessful uses of the umount2 system call in RHEL 9 must generate an audit record. |
| [`V-258217`](rules/V-258217.md) | `RHEL-09-654215` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers. |
| [`V-258218`](rules/V-258218.md) | `RHEL-09-654220` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/sudoers.d/directory. |
| [`V-258219`](rules/V-258219.md) | `RHEL-09-654225` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/group. |
| [`V-258220`](rules/V-258220.md) | `RHEL-09-654230` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/gshadow. |
| [`V-258221`](rules/V-258221.md) | `RHEL-09-654235` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/security/opasswd. |
| [`V-258222`](rules/V-258222.md) | `RHEL-09-654240` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/passwd. |
| [`V-258223`](rules/V-258223.md) | `RHEL-09-654245` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /etc/shadow. |
| [`V-258224`](rules/V-258224.md) | `RHEL-09-654250` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/faillock. |
| [`V-258225`](rules/V-258225.md) | `RHEL-09-654255` | CAT II | RHEL 9 must generate audit records for all account creations, modifications, disabling, and termination events that affect /var/log/lastlog. |
| [`V-258227`](rules/V-258227.md) | `RHEL-09-654265` | CAT II | RHEL 9 must take appropriate action when a critical audit processing failure occurs. |
| [`V-258228`](rules/V-258228.md) | `RHEL-09-654270` | CAT II | RHEL 9 audit system must protect logon UIDs from unauthorized change. |
| [`V-258229`](rules/V-258229.md) | `RHEL-09-654275` | CAT II | RHEL 9 audit system must protect auditing rules from unauthorized change. |
| [`V-258230`](rules/V-258230.md) | `RHEL-09-671010` | CAT I | RHEL 9 must enable FIPS mode. |
| [`V-258231`](rules/V-258231.md) | `RHEL-09-671015` | CAT II | RHEL 9 must employ FIPS 140-3-approved cryptographic hashing algorithms for all stored passwords. |
| [`V-258232`](rules/V-258232.md) | `RHEL-09-671020` | CAT I | RHEL 9 IP tunnels must use FIPS 140-3 approved cryptographic algorithms. |
| [`V-258233`](rules/V-258233.md) | `RHEL-09-671025` | CAT II | RHEL 9 pam_unix.so module must be configured in the password-auth file to use a FIPS 140-3 approved cryptographic hashing algorithm for system authentication. |
| [`V-258234`](rules/V-258234.md) | `RHEL-09-215100` | CAT I | RHEL 9 must have the crypto-policies package installed. |
| [`V-258236`](rules/V-258236.md) | `RHEL-09-672020` | CAT I | RHEL 9 cryptographic policy must not be overridden. |
| [`V-258241`](rules/V-258241.md) | `RHEL-09-215105` | CAT I | RHEL 9 must implement a FIPS 140-3-compliant systemwide cryptographic policy. |
| [`V-258242`](rules/V-258242.md) | `RHEL-09-672050` | CAT I | RHEL 9 must implement DoW-approved encryption in the bind package. |
| [`V-270174`](rules/V-270174.md) | `RHEL-09-271011` | CAT II | RHEL 9 must display the Standard Mandatory DoW Notice and Consent Banner before granting local or remote access to the system via a graphical user logon. |
| [`V-270175`](rules/V-270175.md) | `RHEL-09-232103` | CAT II | RHEL 9 "/etc/audit/" must be owned by root. |
| [`V-270176`](rules/V-270176.md) | `RHEL-09-232104` | CAT II | RHEL 9 "/etc/audit/" must be group-owned by root. |
| [`V-270177`](rules/V-270177.md) | `RHEL-09-255064` | CAT I | The RHEL 9 SSH client must be configured to use only DoW-approved encryption ciphers employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH client connections. |
| [`V-270178`](rules/V-270178.md) | `RHEL-09-255070` | CAT I | The RHEL 9 SSH client must be configured to use only DoW-approved Message Authentication Codes (MACs) employing FIPS 140-3 validated cryptographic hash algorithms to protect the confidentiality of SSH client connections. |
| [`V-270180`](rules/V-270180.md) | `RHEL-09-433016` | CAT II | The RHEL 9 fapolicy module must be configured to employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs. |
| [`V-272488`](rules/V-272488.md) | `RHEL-09-215101` | CAT II | RHEL 9 must have the Postfix package installed. |
| [`V-272496`](rules/V-272496.md) | `RHEL-09-431016` | CAT II | RHEL 9 must elevate the SELinux context when an administrator calls the sudo command. |
| [`V-279936`](rules/V-279936.md) | `RHEL-09-654097` | CAT II | RHEL 9 must audit any script or executable called by cron as root or by any privileged user. |
| [`V-288832`](rules/V-288832.md) | `RHEL-09-654176` | CAT II | RHEL 9 must audit all uses of the useradd command. |
| [`V-288833`](rules/V-288833.md) | `RHEL-09-672055` | CAT I | RHEL 9 must implement DoW-approved encryption in the OpenSSL package. |
