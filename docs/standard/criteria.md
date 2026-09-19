# Image criteria

The testable form of [the standard](README.md). Each criterion is a property of
a built image or of the repository that builds it, stated so that a test can
fail.

Each carries:

- **A level.** *Required* criteria apply to every Datopsis image now. A
  [*target*](#targets) is a direction no current image meets; it becomes
  required by amending this document, not by drift.
- **A test.** What a check must do to establish the property. A criterion
  whose only evidence is a sentence in a README is not met.
- **Anchors.** The SRG rules the criterion serves, and the 800-53 controls those
  rules reach through the [crosswalk](../crosswalk/README.md). A criterion
  that no rendered SRG rule reaches says so, rather than borrowing a rule that
  does not fit.

Anchors are checked: `tests/test_standard.py` fails if a cited control is not
one the cited rule actually reaches. A criterion's anchors say which obligations
it contributes to. They do not say the image satisfies those controls; under
the control model that is a separate, evidenced claim.

Criteria describe the image's half of a control. Where the platform must do the
other half, the criterion names the matching [platform expectation](platform.md).

## Build

### IMG-01 Base image pinned by digest

**Required.** Every base image, builder and runtime, is referenced by
manifest-list digest. The digest is recorded in the lock, and the build uses
that digest, not a tag.

- **Test:** every `FROM` carries `@sha256:`; each equals the lock's recorded
  digest; the build resolves the base from local storage without pulling
  ([IMG-03](#img-03-hermetic-assembly)).
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md); [V-278977](../srg/general-purpose-operating-system-srg/rules/V-278977.md) → [SA-22](../crosswalk/controls/sa-22.md)

### IMG-02 Every build input pinned and verified

**Required.** Every external input (base, RPM, upstream binary or archive) is
recorded in a committed lock with its size and SHA-256, and verified against it
before use. Where the publisher signs the input, the signature is verified
against a pinned key or identity as well. A checksum fetched from the same
origin as the artifact is not verification.

- **Test:** a mismatched digest, a missing input, and an unsigned or wrongly
  signed package each fail the build; after installation, the installed package
  set matches the lock.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-03 Hermetic assembly

**Required.** Image assembly runs with networking disabled and image pulls
refused. No package manager, `curl`, `wget`, or language installer runs inside
the build, and no layer cache restored from outside the build is used.

- **Test:** the build is invoked with `--network=none` (or the builder's
  equivalent) and `--pull=never`, and a negative test shows a build with a
  missing input fails rather than fetching it. A static check rejects network
  tools in the `Containerfile`.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-04 Input refresh is a reviewed change

**Required.** Only a reviewed change to the lock changes an input. Automation
may report that a newer input exists; it may not edit the lock or open a change
that merges without review.

- **Test:** drift automation has no write permission to the lock and reports
  rather than commits.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-29 Base kept current

**Required.** The base image is refreshed whenever its publisher releases a
security update, and never falls more than 30 days behind the publisher's
current release. A current base is not the same as a patched one: the base
carries fixes nobody has scanned for yet.

- **Test:** the drift report from [IMG-04](#img-04-input-refresh-is-a-reviewed-change)
  records the age of the pinned base against the publisher's current digest;
  a release whose base is more than 30 days behind fails.
- **Anchors:** [V-259333](../srg/general-purpose-operating-system-srg/rules/V-259333.md) → [SI-2](../crosswalk/controls/si-2.md); [V-278977](../srg/general-purpose-operating-system-srg/rules/V-278977.md) → [SA-22](../crosswalk/controls/sa-22.md)
- **Source:** [NIST SP 800-190 §4.1.2](nist-800-190.md#image)

### IMG-05 No secrets in the build

**Required.** No credential is passed as a build argument, copied into a layer,
or recorded in a label or in image history.

- **Test:** a static check rejects credential-shaped `ARG` and `ENV` names; image
  history and labels are searched for acquisition material and credentials.
- **Anchors:** [V-263660](../srg/general-purpose-operating-system-srg/rules/V-263660.md) → [SC-28(3)](../crosswalk/controls/sc-28.3.md)

## Contents

### IMG-06 No package manager

**Required.** The final image contains no package-management binary (`dnf`,
`microdnf`, `yum`, `rpm`), no repository configuration, and no imported
repository signing keys.

- **Test:** each binary is absent from `PATH`; `/etc/yum.repos.d` is absent; no
  `*.repo` or `RPM-GPG-KEY*` file exists.
- **Anchors:** [V-203716](../srg/general-purpose-operating-system-srg/rules/V-203716.md) → [CM-11(2)](../crosswalk/controls/cm-11.2.md); [V-203637](../srg/general-purpose-operating-system-srg/rules/V-203637.md) → [CM-7](../crosswalk/controls/cm-7.md)

### IMG-07 Only what the function needs

**Required.** The image contains no compiler, no network retrieval tool, and no
optional module or plugin the function does not use. Enabled modules or
features are declared and compared against the built image.

- **Test:** `curl`, `wget`, and compilers are absent; the service's reported
  feature or module set matches a committed declaration.
- **Anchors:** [V-203637](../srg/general-purpose-operating-system-srg/rules/V-203637.md) → [CM-7](../crosswalk/controls/cm-7.md); [V-203722](../srg/general-purpose-operating-system-srg/rules/V-203722.md) → [CM-7(5)](../crosswalk/controls/cm-7.5.md)

### IMG-27 No remote administration

**Required.** The image contains no SSH server, remote shell, or other remote
administration service, and the service it packages exposes no administrative
interface that is not part of its declared function. A container is
administered by replacing it, or through the runtime's own interface.

- **Test:** `sshd`, `telnetd`, and equivalent daemons are absent; the declared
  listeners in [IMG-30](#img-30-expected-behaviour-is-declared) contain no
  remote administration port.
- **Anchors:** [V-203655](../srg/general-purpose-operating-system-srg/rules/V-203655.md) → [SC-2](../crosswalk/controls/sc-2.md); [V-203637](../srg/general-purpose-operating-system-srg/rules/V-203637.md) → [CM-7](../crosswalk/controls/cm-7.md)
- **Source:** [NIST SP 800-190 §4.1.2](nist-800-190.md#image)

### IMG-08 Embedded package inventory

**Required.** The image carries a read-only inventory of its installed
packages, written at build time and matching the lock.

- **Test:** the inventory exists at a documented path, is mode `0444`, and
  matches the lock by hash.
- **Anchors:** No rendered SRG rule. Serves CM-8 (system component inventory).

### IMG-09 No privilege-raising files

**Required.** No file carries the setuid or setgid bit, and no file outside a
declared writable mount is world-writable.

- **Test:** `find / -xdev -perm /6000` and `find / -xdev -perm -0002` (outside
  declared mounts) return nothing.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md)

### IMG-10 Software and configuration not writable by the service

**Required.** Executables, libraries, and configuration are owned by root and
are not writable by the runtime identity.

- **Test:** as the runtime user, the service binary and its configuration fail
  `test -w`.
- **Anchors:** [V-203675](../srg/general-purpose-operating-system-srg/rules/V-203675.md) → [CM-5(6)](../crosswalk/controls/cm-5.6.md)

## Runtime

### IMG-11 Non-root, with no privilege transition

**Required.** The image declares a numeric, non-zero `USER` with primary group
0. No process in the container ever has UID 0. There is no root phase at
startup and no `su`, `sudo`, `gosu`, or equivalent in the image.

- **Test:** the image's configured user is non-zero; while running, every
  `/proc/*/status` reports a non-zero `Uid`.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md); [V-203695](../srg/general-purpose-operating-system-srg/rules/V-203695.md) → [AC-6(10)](../crosswalk/controls/ac-6.10.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)

### IMG-12 Runs under an arbitrary UID

**Required.** The image runs correctly when the platform assigns an arbitrary
non-root UID in group 0.

- **Test:** the smoke suite passes under `--user <arbitrary>:0`.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)

### IMG-13 Works with no capabilities and no new privileges

**Required.** The service operates with every Linux capability dropped and
`no-new-privileges` set.

- **Test:** under `--cap-drop ALL` and `no-new-privileges`, every process
  reports `CapEff` of zero and `NoNewPrivs` of 1 in `/proc/*/status`. Passing
  the flags is not evidence they applied. The suite also runs with the
  runtime's default seccomp profile in force, never `unconfined`, and, on an
  SELinux host, in enforcing mode with the default container type.
- **Source:** [NIST SP 800-190 §4.4.3](nist-800-190.md#container)
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)

### IMG-14 Unprivileged ports

**Required.** Every listening socket is on a port at or above 1024.

- **Test:** read the listening sockets from `/proc/net/tcp`, `tcp6`, `udp`, and
  `udp6` while the service runs, and assert each port is at least 1024. A
  capability drop alone proves nothing under Docker, which sets
  `net.ipv4.ip_unprivileged_port_start` to 0.
- **Anchors:** [V-203638](../srg/general-purpose-operating-system-srg/rules/V-203638.md) → [CM-7](../crosswalk/controls/cm-7.md)
- **Platform:** [PLT-04](platform.md#plt-04-ports-are-non-privileged-and-declared)

### IMG-15 Read-only root filesystem

**Required.** The service runs with the root filesystem mounted read-only.
Every writable path is declared in the image's documentation, and each declared
temporary mount is expected as `rw,noexec,nosuid,nodev`. A missing declared
mount makes the service exit non-zero naming the path.

- **Test:** the smoke suite runs under `--read-only` with only the declared
  mounts; a write to the root filesystem fails; running without a declared mount
  fails with the path in the error.
- **Anchors:** [V-203675](../srg/general-purpose-operating-system-srg/rules/V-203675.md) → [CM-5(6)](../crosswalk/controls/cm-5.6.md)
- **Platform:** [PLT-03](platform.md#plt-03-the-root-filesystem-is-read-only)

### IMG-16 Secrets only as read-only files

**Required.** Secrets are read only from files on a read-only mount. The image
accepts no secret through an environment variable or a command-line argument,
ships no default secret, and never writes a secret to a log. Where upstream
convention uses an environment variable, the image provides a `_FILE` form
instead. See [ADR-0003](../adr/0003-secrets-reach-an-image-only-as-read-only-files.md).

- **Test:** with secrets mounted, no secret value appears in any
  `/proc/*/cmdline`, in `/proc/1/environ`, or in the logs; the secret file is not
  writable by the runtime identity; a missing, empty, or group- or
  world-readable secret file fails startup.
- **Anchors:** [V-263660](../srg/general-purpose-operating-system-srg/rules/V-263660.md) → [SC-28(3)](../crosswalk/controls/sc-28.3.md)
- **Platform:** [PLT-06](platform.md#plt-06-secrets-are-delivered-as-read-only-files)

### IMG-17 Trust material supplied by the operator

**Required.** Certificates, keys, and trust stores the operator chooses are read
from read-only mounts. The image adds no trust anchor beyond those of its
base.

- **Test:** mounted trust material is not writable by the runtime identity; the
  image's trust store matches its base's.
- **Anchors:** [V-263659](../srg/general-purpose-operating-system-srg/rules/V-263659.md) → [SC-17](../crosswalk/controls/sc-17.md)
- **Platform:** [PLT-06](platform.md#plt-06-secrets-are-delivered-as-read-only-files)

### IMG-18 Fails closed

**Required.** Invalid configuration, a missing required mount, or an absent or
malformed secret makes the service exit non-zero with a message naming the
cause. It does not fall back to packaged defaults, create what is missing, or
start a shell.

- **Test:** negative cases for each start with a defect and assert a non-zero
  exit and a message naming it.
- **Anchors:** [V-203677](../srg/general-purpose-operating-system-srg/rules/V-203677.md) → [SC-24](../crosswalk/controls/sc-24.md)

### IMG-19 Logs to standard streams, without secrets

**Required.** All service logs are written to standard output or standard
error, for the platform to collect. No log line contains a secret.

- **Test:** log files in the image are absent or are links to `/dev/stdout` and
  `/dev/stderr`; the secret-leak check in [IMG-16](#img-16-secrets-only-as-read-only-files)
  covers the logs.
- **Anchors:** [V-203613](../srg/general-purpose-operating-system-srg/rules/V-203613.md) → [AU-6(4)](../crosswalk/controls/au-6.4.md)
- **Platform:** [PLT-09](platform.md#plt-09-logs-are-collected-centrally)

### IMG-20 Lifecycle is declared

**Required.** The image declares a `HEALTHCHECK` in exec form and a
`STOPSIGNAL`, and the service or a minimal init is PID 1 and handles it. The
image's documentation states what the healthcheck proves.

- **Test:** both are present in the image configuration; stopping the container
  produces a clean exit within the documented timeout.
- **Anchors:** No rendered SRG rule. Required by the
  [DISA process guide](process-guide.md), which asks for a healthcheck.

### IMG-30 Expected behaviour is declared

**Required.** The image declares, in a committed machine-readable file, what it
does when it runs: its processes, its listening ports and protocols, its
writable paths, and the outbound destinations it needs. The smoke suite runs
the image and compares what it actually does with the declaration.

A declaration is what lets the platform tell normal from anomalous. A runtime
monitor that has to learn an image's behaviour by watching it cannot tell a
compromise that happens during the learning period from the baseline.

- **Test:** while the service runs, the processes in `/proc`, the listening
  sockets, and the paths written match the declaration, and every declared port
  is at least 1024 ([IMG-14](#img-14-unprivileged-ports)).
- **Anchors:** [V-203638](../srg/general-purpose-operating-system-srg/rules/V-203638.md) → [CM-7](../crosswalk/controls/cm-7.md)
- **Platform:** [PLT-16](platform.md#plt-16-runtime-behaviour-is-monitored)
- **Source:** [NIST SP 800-190 §4.4.2, §4.4.4](nist-800-190.md#container)

## Release

### IMG-21 Bill of materials

**Required.** Each release carries an SPDX bill of materials generated from the
built image and attached to it as an attestation.

- **Test:** the release workflow generates, validates, and attests the SBOM, and
  a verification step retrieves it by digest.
- **Anchors:** No rendered SRG rule. Serves CM-8 and SR-4.

### IMG-22 Signed, with provenance

**Required.** Each released image digest is signed with a keyless identity bound
to the release workflow, and carries build provenance naming the workflow and
commit. The release workflow verifies both before it finishes.

- **Test:** the release verifies the signature against the expected identity and
  issuer, and retrieves the provenance attestation.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)
- **Platform:** [PLT-01](platform.md#plt-01-images-are-admitted-by-verified-digest)

### IMG-23 Identifying labels

**Required.** The image carries OCI labels for source, revision, version, and
creation time, plus the base digest and lock digest it was built from.

- **Test:** each label is present and the revision matches the release commit.
- **Anchors:** No rendered SRG rule. Serves CM-8.

### IMG-24 Immutable tags

**Required.** Releases are published under version tags that are never moved.
There is no `latest` tag.

- **Test:** the release workflow refuses to overwrite an existing tag and never
  pushes `latest`.
- **Anchors:** No rendered SRG rule. Serves CM-2 (baseline configuration).
- **Platform:** [PLT-01](platform.md#plt-01-images-are-admitted-by-verified-digest)

### IMG-25 Vulnerability gate and remediation

**Required.** The build fails on any Critical or High vulnerability with an
available fix, and every finding is recorded with the release. Once a fix is
available, it ships within 7 days for Critical or CISA KEV, 14 days for High,
and 30 days otherwise.

- **Test:** the scan step fails the build on fixed Critical or High findings;
  the full findings report is attached to the release. The scan covers every
  layer, not only the base's packages: an upstream binary or archive is scanned
  through the components the SBOM records for it.
- **Source:** [NIST SP 800-190 §4.1.1](nist-800-190.md#image)
- **Anchors:** [V-259333](../srg/general-purpose-operating-system-srg/rules/V-259333.md) → [SI-2](../crosswalk/controls/si-2.md); [V-203755](../srg/general-purpose-operating-system-srg/rules/V-203755.md) → [SI-2(6)](../crosswalk/controls/si-2.6.md)
- **Platform:** [PLT-08](platform.md#plt-08-images-are-scanned-and-replaced)

### IMG-28 Malware scan

**Required.** Each built image is scanned for malware, with signatures updated
before the scan, and so are the retrieved build inputs before assembly. A
detection fails the build. Verifying an input by digest establishes that it is
the file that was reviewed, not that the file is benign.

- **Test:** the build scans the retrieved inputs and the exported image
  filesystem with a malware scanner whose signature database was refreshed in
  the same run, and fails on any detection.
- **Anchors:** No rendered SRG rule. Serves SI-3 (malicious code protection).
- **Platform:** [PLT-08](platform.md#plt-08-images-are-scanned-and-replaced)
- **Source:** [NIST SP 800-190 §4.1.3](nist-800-190.md#image); DISA process
  guide §7.1 step 1f

### IMG-26 Exceptions expire

**Required.** A vulnerability or criterion that will not be met in time is an
exception: scoped to one image digest, with a reason, an owner, and an expiry
date. An expired exception fails the build.

- **Test:** exceptions are the `deviations` in the image's
  [hardening profile](../TAILORING.md#deviations), checked in CI by
  `check-profile.py`; an entry past its expiry, or recorded for longer than
  its kind allows, fails.
- **Anchors:** [V-259333](../srg/general-purpose-operating-system-srg/rules/V-259333.md) → [SI-2](../crosswalk/controls/si-2.md)

## Targets

Directions the standard sets but does not yet require. Each becomes required by
amending this document, once an image has shown it can be done.

### IMG-T1 No shell

The final image contains no shell. Until then, no runtime path (entrypoint,
healthcheck, stop handling) may depend on one, so that removing it breaks
nothing.

- **Anchors:** [V-203637](../srg/general-purpose-operating-system-srg/rules/V-203637.md) → [CM-7](../crosswalk/controls/cm-7.md)

### IMG-T2 Reproducible build

Two builds of the same commit and lock produce the same image digest, using
`SOURCE_DATE_EPOCH` and normalised timestamps.

- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-T3 Compliance scan

An OpenSCAP scan of the image against an agreed, GPOS-derived rule selection,
published with each release. It is a target rather than a requirement because
no agreed rule selection exists yet; scanning each image against its own
selection would make results incomparable.

- **Anchors:** [V-203780](../srg/general-purpose-operating-system-srg/rules/V-203780.md) → [CM-6](../crosswalk/controls/cm-6.md)
