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

### IMG-33 Source is protected and traceable

**Required.** The image's source repository protects its default branch,
requires review before merge, and records who made each change. Releases are
cut only from reviewed commits on that branch.

- **Implementation:** Branch protection requires a reviewed pull request and
  passing checks; direct pushes to the default branch are refused; release tags
  are signed or created only by the release workflow.
- **Verification:** Attempt a direct push to the default branch, and a merge
  without review; check that the release commit is on the default branch.
- **Expected:** Both attempts are refused, and every release commit is reviewed.
- **Evidence:** The branch-protection settings and the release commit's review
  record.
- **Anchors:** No rendered SRG rule. Serves CM-3 and SA-10, and the SLSA v1.2
  Source Track.
- **Source:** [SLSA v1.2](../../artifacts/sources.json); NIST SP 800-218 (SSDF)

### IMG-34 Source and dependencies are scanned before build

**Required.** Before an image is built, its source is scanned for committed
secrets, its own code with static analysis where it has any, and the
dependencies it declares for known vulnerabilities.

- **Implementation:** The pipeline runs a secret scanner, a static analyser for
  any code the repository contains, and a dependency scanner, each before the
  build step.
- **Verification:** Commit a test secret and a known-vulnerable dependency on a
  branch.
- **Expected:** The pipeline fails before building.
- **Evidence:** The scanners' reports and the failed run.
- **Anchors:** No rendered SRG rule. Serves SA-11 and RA-5.
- **Source:** NIST SP 800-218 (SSDF)

### IMG-01 Base image pinned by digest

**Required.** Every base image, builder and runtime, is referenced by
manifest-list digest. The digest is recorded in the lock, and the build uses
that digest, not a tag.

- **Implementation:** Each `FROM` names the base by manifest-list digest, copied
  from the lock by the build script.
- **Verification:** Every `FROM` carries `@sha256:`; each equals the lock's
  recorded
  digest; the build resolves the base from local storage without pulling
  ([IMG-03](#img-03-hermetic-assembly)).
- **Expected:** Every `FROM` resolves to the locked digest, and the build pulls
  nothing.
- **Evidence:** The lock file; the build log showing the base resolved from
  local storage.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md); [V-278977](../srg/general-purpose-operating-system-srg/rules/V-278977.md) → [SA-22](../crosswalk/controls/sa-22.md)

### IMG-02 Every build input pinned and verified

**Required.** Every external input (base, RPM, upstream binary or archive) is
recorded in a committed lock with its size and SHA-256, and verified against it
before use. Where the publisher signs the input, the signature is verified
against a pinned key or identity as well. A checksum fetched from the same
origin as the artifact is not verification.

- **Implementation:** A committed lock records every input's size and SHA-256,
  and the signing key or identity where one exists; an install step verifies
  each before use and compares the installed set with the lock.
- **Verification:** A mismatched digest, a missing input, and an unsigned or
  wrongly
  signed package each fail the build; after installation, the installed package
  set matches the lock.
- **Expected:** Each defective input stops the build with the input named; a
  clean build's installed set equals the lock.
- **Evidence:** The lock; the negative-test results; the installed-versus-locked
  comparison from the build log.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-03 Hermetic assembly

**Required.** Image assembly runs with networking disabled and image pulls
refused. No package manager, `curl`, `wget`, or language installer runs inside
the build, and no layer cache restored from outside the build is used.

- **Implementation:** Inputs are retrieved and verified in a separate step and
  handed to a build that runs with networking disabled and pulls refused.
- **Verification:** The build is invoked with `--network=none` (or the builder's
  equivalent) and `--pull=never`, and a negative test shows a build with a
  missing input fails rather than fetching it. A static check rejects network
  tools in the `Containerfile`.
- **Expected:** The build succeeds offline with every declared input, and fails
  without fetching when one is missing.
- **Evidence:** The build invocation; the negative-build result; the static
  check's report.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-04 Input refresh is a reviewed change

**Required.** Only a reviewed change to the lock changes an input. Automation
may report that a newer input exists; it may not edit the lock or open a change
that merges without review.

- **Implementation:** A scheduled job compares the lock with upstream and opens
  a report; lock changes arrive only as reviewed pull requests.
- **Verification:** Drift automation has no write permission to the lock and
  reports
  rather than commits.
- **Expected:** The drift job reports newer inputs and changes nothing.
- **Evidence:** The drift job's permissions and report; the pull request that
  changed the lock.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-29 Base kept current

**Required.** The base image is refreshed whenever its publisher releases a
security update, and never falls more than 30 days behind the publisher's
current release. A current base is not the same as a patched one: the base
carries fixes nobody has scanned for yet.

- **Implementation:** The drift job records the pinned base's age against the
  publisher's current digest; the release checks it.
- **Verification:** The drift report from
  [IMG-04](#img-04-input-refresh-is-a-reviewed-change)
  records the age of the pinned base against the publisher's current digest;
  a release whose base is more than 30 days behind fails.
- **Expected:** No release is published with a base more than 30 days behind.
- **Evidence:** The drift report with the base age; the release check's result.
- **Anchors:** [V-259333](../srg/general-purpose-operating-system-srg/rules/V-259333.md) → [SI-2](../crosswalk/controls/si-2.md); [V-278977](../srg/general-purpose-operating-system-srg/rules/V-278977.md) → [SA-22](../crosswalk/controls/sa-22.md)
- **Source:** [NIST SP 800-190 §4.1.2](nist-800-190.md#image)

### IMG-05 No secrets in the build

**Required.** No credential is passed as a build argument, copied into a layer,
or recorded in a label or in image history.

- **Implementation:** Build arguments carry no credentials; a static check reads
  the build definition, and a post-build check reads history and labels.
- **Verification:** A static check rejects credential-shaped `ARG` and `ENV`
  names; image
  history and labels are searched for acquisition material and credentials.
- **Expected:** No credential-shaped name in the build definition, and no
  credential in history or labels.
- **Evidence:** The static check's report; the history and label scan output.
- **Anchors:** [V-263660](../srg/general-purpose-operating-system-srg/rules/V-263660.md) → [SC-28(3)](../crosswalk/controls/sc-28.3.md)

## Contents

### IMG-06 No package manager

**Required.** The final image contains no package-management binary (`dnf`,
`microdnf`, `yum`, `rpm`), no repository configuration, and no imported
repository signing keys.

- **Implementation:** The final stage removes package-management binaries,
  repository configuration, and imported keys.
- **Verification:** Each binary is absent from `PATH`; `/etc/yum.repos.d` is
  absent; no
  `*.repo` or `RPM-GPG-KEY*` file exists.
- **Expected:** None of the package-management binaries, repository files, or
  keys is present.
- **Evidence:** The smoke-test output listing each absence.
- **Anchors:** [V-203716](../srg/general-purpose-operating-system-srg/rules/V-203716.md) → [CM-11(2)](../crosswalk/controls/cm-11.2.md); [V-203637](../srg/general-purpose-operating-system-srg/rules/V-203637.md) → [CM-7](../crosswalk/controls/cm-7.md)

### IMG-07 Only what the function needs

**Required.** The image contains no compiler, no network retrieval tool, and no
optional module or plugin the function does not use. Enabled modules or
features are declared and compared against the built image.

- **Implementation:** The final stage installs only what the service needs;
  enabled modules or features are declared in a committed file.
- **Verification:** `curl`, `wget`, and compilers are absent; the service's
  reported
  feature or module set matches a committed declaration.
- **Expected:** No compiler or retrieval tool is present, and the reported
  feature set equals the declaration.
- **Evidence:** The smoke-test output; the declared and reported feature sets.
- **Anchors:** [V-203637](../srg/general-purpose-operating-system-srg/rules/V-203637.md) → [CM-7](../crosswalk/controls/cm-7.md); [V-203722](../srg/general-purpose-operating-system-srg/rules/V-203722.md) → [CM-7(5)](../crosswalk/controls/cm-7.5.md)

### IMG-27 No remote administration

**Required.** The image contains no SSH server, remote shell, or other remote
administration service, and the service it packages exposes no administrative
interface that is not part of its declared function. A container is
administered by replacing it, or through the runtime's own interface.

- **Implementation:** No remote administration daemon is installed; the
  behaviour declaration lists no administrative listener.
- **Verification:** `sshd`, `telnetd`, and equivalent daemons are absent; the
  declared
  listeners in [IMG-30](#img-30-expected-behaviour-is-declared) contain no
  remote administration port.
- **Expected:** No such daemon is present, and no declared or open port is an
  administrative one.
- **Evidence:** The smoke-test output; the behaviour declaration.
- **Anchors:** [V-203655](../srg/general-purpose-operating-system-srg/rules/V-203655.md) → [SC-2](../crosswalk/controls/sc-2.md); [V-203637](../srg/general-purpose-operating-system-srg/rules/V-203637.md) → [CM-7](../crosswalk/controls/cm-7.md)
- **Source:** [NIST SP 800-190 §4.1.2](nist-800-190.md#image)

### IMG-08 Embedded package inventory

**Required.** The image carries a read-only inventory of its installed
packages, written at build time and matching the lock.

- **Implementation:** The install step writes a package inventory into the image
  at build time and compares it with the lock.
- **Verification:** The inventory exists at a documented path, is mode `0444`,
  and
  matches the lock by hash.
- **Expected:** The inventory is present, read-only, and matches the lock by
  hash.
- **Evidence:** The inventory file; the build log's comparison.
- **Anchors:** No rendered SRG rule. Serves CM-8 (system component inventory).

### IMG-09 No privilege-raising files

**Required.** No file carries the setuid or setgid bit, and no file outside a
declared writable mount is world-writable.

- **Implementation:** The final stage strips setuid and setgid bits and fails
  the build on any world-writable file outside declared mounts.
- **Verification:** `find / -xdev -perm /6000` and `find / -xdev -perm -0002`
  (outside
  declared mounts) return nothing.
- **Expected:** Both searches return nothing.
- **Evidence:** The smoke-test output of both searches.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md)

### IMG-10 Software and configuration not writable by the service

**Required.** Executables, libraries, and configuration are owned by root and
are not writable by the runtime identity.

- **Implementation:** Executables, libraries, and configuration are installed
  owned by root with no write permission for the runtime user or group.
- **Verification:** As the runtime user, the service binary and its
  configuration fail
  `test -w`.
- **Expected:** Every write test fails for the runtime user.
- **Evidence:** The smoke-test output.
- **Anchors:** [V-203675](../srg/general-purpose-operating-system-srg/rules/V-203675.md) → [CM-5(6)](../crosswalk/controls/cm-5.6.md)

## Runtime

### IMG-11 Non-root, with no privilege transition

**Required.** The image declares a numeric, non-zero `USER` with primary group
0. No process in the container ever has UID 0. There is no root phase at
startup and no `su`, `sudo`, `gosu`, or equivalent in the image.

- **Implementation:** The image declares a numeric non-root `USER` with group 0,
  and the entrypoint execs the service directly.
- **Verification:** The image's configured user is non-zero; while running,
  every
  `/proc/*/status` reports a non-zero `Uid`.
- **Expected:** The configured user is non-zero, and no process ever runs as UID
  0.
- **Evidence:** The image configuration; the per-process `/proc` report from the
  smoke test.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md); [V-203695](../srg/general-purpose-operating-system-srg/rules/V-203695.md) → [AC-6(10)](../crosswalk/controls/ac-6.10.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)

### IMG-12 Runs under an arbitrary UID

**Required.** The image runs correctly when the platform assigns an arbitrary
non-root UID in group 0.

- **Implementation:** File ownership and permissions use group 0 rather than a
  fixed UID, so any UID in group 0 can run the service.
- **Verification:** The smoke suite passes under `--user <arbitrary>:0`.
- **Expected:** The smoke suite passes under an arbitrary UID.
- **Evidence:** The smoke-test output for the arbitrary-UID run.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)

### IMG-13 Works with no capabilities and no new privileges

**Required.** The service operates with every Linux capability dropped and
`no-new-privileges` set.

- **Implementation:** The service needs no capability and no privilege gain; the
  smoke suite runs it with every capability dropped, `no-new-privileges`, the
  default seccomp profile, and SELinux enforcing.
- **Verification:** Under `--cap-drop ALL` and `no-new-privileges`, every
  process
  reports `CapEff` of zero and `NoNewPrivs` of 1 in `/proc/*/status`. Passing
  the flags is not evidence they applied. The suite also runs with the
  runtime's default seccomp profile in force, never `unconfined`, and, on an
  SELinux host, in enforcing mode with the default container type.
- **Expected:** Every process reports `CapEff` of zero and `NoNewPrivs` of 1,
  and the service works.
- **Evidence:** The per-process `/proc` report; the runtime's recorded security
  options.
- **Source:** [NIST SP 800-190 §4.4.3](nist-800-190.md#container)
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)

### IMG-31 Admitted under the restricted-v2 SCC and the Restricted Pod Security Standard

**Required.** The image runs unmodified under OpenShift's `restricted-v2`
security context constraint and Kubernetes' Restricted Pod Security Standard:
a random non-root UID, every capability dropped, the `RuntimeDefault` seccomp
profile, privilege escalation disallowed, and no host namespace or host path.

- **Implementation:** The image needs nothing either profile forbids, so its
  deployment manifest can request none of it.
- **Verification:** Deploy the image with its reference manifest into a
  namespace
  enforcing the Restricted Pod Security Standard, and onto OpenShift under
  `restricted-v2`, and run the smoke suite in each.
- **Expected:** Both admit the workload unmodified, and the smoke suite passes.
- **Evidence:** The admission results, the smoke-test output, and the cluster
  and
  policy versions.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md); [V-203695](../srg/general-purpose-operating-system-srg/rules/V-203695.md) → [AC-6(10)](../crosswalk/controls/ac-6.10.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)
- **Source:** [Kubernetes Pod Security Standards](../../artifacts/sources.json);
  OpenShift security context constraints

### IMG-32 Runs in a user namespace under the restricted-v3 SCC

**Required.** The image runs unmodified under OpenShift's `restricted-v3`
security context constraint, in its own Linux user namespace
(`hostUsers: false`), so that UID 0 inside the container, were it ever
reached, is not UID 0 on the host.

- **Implementation:** The image depends on no host UID mapping: no file
  ownership assumes a host UID, and no mount requires one.
- **Verification:** Deploy the image with `hostUsers: false` onto OpenShift 4.20
  or later under `restricted-v3`, or under a runtime with user namespaces
  enabled, and run the smoke suite.
- **Expected:** The workload is admitted, runs in a user namespace, and the
  smoke
  suite passes.
- **Evidence:** The admission result, the container's `/proc/self/uid_map`, and
  the smoke-test output.
- **Anchors:** [V-203696](../srg/general-purpose-operating-system-srg/rules/V-203696.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md)
- **Platform:** [PLT-02](platform.md#plt-02-least-privilege-is-imposed)
- **Source:** OpenShift security context constraints, from 4.20

### IMG-14 Unprivileged ports

**Required.** Every listening socket is on a port at or above 1024.

- **Implementation:** Every listener is configured on a port of 1024 or above,
  and the behaviour declaration lists them.
- **Verification:** Read the listening sockets from `/proc/net/tcp`, `tcp6`,
  `udp`, and
  `udp6` while the service runs, and assert each port is at least 1024. A
  capability drop alone proves nothing under Docker, which sets
  `net.ipv4.ip_unprivileged_port_start` to 0.
- **Expected:** Every listening socket is at or above 1024 and is declared.
- **Evidence:** The socket report from `/proc/net`.
- **Anchors:** [V-203638](../srg/general-purpose-operating-system-srg/rules/V-203638.md) → [CM-7](../crosswalk/controls/cm-7.md)
- **Platform:** [PLT-04](platform.md#plt-04-ports-are-non-privileged-and-declared)

### IMG-15 Read-only root filesystem

**Required.** The service runs with the root filesystem mounted read-only.
Every writable path is declared in the image's documentation, and each declared
temporary mount is expected as `rw,noexec,nosuid,nodev`. A missing declared
mount makes the service exit non-zero naming the path.

- **Implementation:** The service writes only to declared paths, and checks at
  startup that each declared mount exists.
- **Verification:** The smoke suite runs under `--read-only` with only the
  declared
  mounts; a write to the root filesystem fails; running without a declared mount
  fails with the path in the error.
- **Expected:** The service runs read-only; a root write fails; a missing mount
  fails naming its path.
- **Evidence:** The smoke-test output for the read-only, write-probe, and
  missing-mount runs.
- **Anchors:** [V-203675](../srg/general-purpose-operating-system-srg/rules/V-203675.md) → [CM-5(6)](../crosswalk/controls/cm-5.6.md)
- **Platform:** [PLT-03](platform.md#plt-03-the-root-filesystem-is-read-only)

### IMG-16 Secrets only as read-only files

**Required.** Secrets are read only from files on a read-only mount. The image
accepts no secret through an environment variable or a command-line argument,
ships no default secret, and never writes a secret to a log. Where upstream
convention uses an environment variable, the image provides a `_FILE` form
instead. See [ADR-0003](../adr/0003-secrets-reach-an-image-only-as-read-only-files.md).

- **Implementation:** The service, or its entrypoint, reads each secret from a
  `_FILE` path and refuses the environment-variable form.
- **Verification:** With secrets mounted, no secret value appears in any
  `/proc/*/cmdline`, in `/proc/1/environ`, or in the logs; the secret file is not
  writable by the runtime identity; a missing, empty, or world-readable secret
  file fails startup. Group read is expected: an image running under an
  arbitrary UID in group 0 reads a mounted secret through its group.
- **Expected:** No secret value appears in any process's arguments, in PID 1's
  environment, or in the logs; a malformed secret file stops startup.
- **Evidence:** The secret-leak scan output; the negative-case results.
- **Anchors:** [V-263660](../srg/general-purpose-operating-system-srg/rules/V-263660.md) → [SC-28(3)](../crosswalk/controls/sc-28.3.md)
- **Platform:** [PLT-06](platform.md#plt-06-secrets-are-delivered-as-read-only-files)

### IMG-17 Trust material supplied by the operator

**Required.** Certificates, keys, and trust stores the operator chooses are read
from read-only mounts. The image adds no trust anchor beyond those of its
base.

- **Implementation:** Trust material is read from a documented read-only mount;
  the image adds nothing to its base's trust store.
- **Verification:** Mounted trust material is not writable by the runtime
  identity; the
  image's trust store matches its base's.
- **Expected:** Mounted trust material is not writable, and the trust store
  equals the base's.
- **Evidence:** The smoke-test output; the trust-store comparison.
- **Anchors:** [V-263659](../srg/general-purpose-operating-system-srg/rules/V-263659.md) → [SC-17](../crosswalk/controls/sc-17.md)
- **Platform:** [PLT-06](platform.md#plt-06-secrets-are-delivered-as-read-only-files)

### IMG-18 Fails closed

**Required.** Invalid configuration, a missing required mount, or an absent or
malformed secret makes the service exit non-zero with a message naming the
cause. It does not fall back to packaged defaults, create what is missing, or
start a shell.

- **Implementation:** The entrypoint validates configuration, mounts, and
  secrets before starting the service, and exits non-zero naming the defect.
- **Verification:** Negative cases for each start with a defect and assert a
  non-zero
  exit and a message naming it.
- **Expected:** Each defect produces a non-zero exit and a message naming it.
- **Evidence:** The negative-case results.
- **Anchors:** [V-203677](../srg/general-purpose-operating-system-srg/rules/V-203677.md) → [SC-24](../crosswalk/controls/sc-24.md)

### IMG-19 Logs to standard streams, without secrets

**Required.** All service logs are written to standard output or standard
error, for the platform to collect. No log line contains a secret.

- **Implementation:** Log destinations are standard output and standard error,
  directly or by links.
- **Verification:** Log files in the image are absent or are links to
  `/dev/stdout` and
  `/dev/stderr`; the secret-leak check in [IMG-16](#img-16-secrets-only-as-read-only-files)
  covers the logs.
- **Expected:** No log file is written inside the image, and no secret reaches
  the logs.
- **Evidence:** The smoke-test output; the secret-leak scan.
- **Anchors:** [V-203613](../srg/general-purpose-operating-system-srg/rules/V-203613.md) → [AU-6(4)](../crosswalk/controls/au-6.4.md)
- **Platform:** [PLT-09](platform.md#plt-09-logs-are-collected-centrally)

### IMG-20 Lifecycle is declared

**Required.** The image declares a `HEALTHCHECK` in exec form and a
`STOPSIGNAL`, and the service or a minimal init is PID 1 and handles it. The
image's documentation states what the healthcheck proves.

- **Implementation:** The image declares an exec-form `HEALTHCHECK` and a
  `STOPSIGNAL`, and the service or a minimal init is PID 1.
- **Verification:** Both are present in the image configuration; stopping the
  container
  produces a clean exit within the documented timeout.
- **Expected:** Both are present, and a stop exits cleanly within the documented
  timeout.
- **Evidence:** The image configuration; the stop-test result.
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

- **Implementation:** A committed behaviour declaration lists processes,
  listeners, writable paths, and outbound destinations.
- **Verification:** While the service runs, the processes in `/proc`, the
  listening
  sockets, and the paths written match the declaration, and every declared port
  is at least 1024 ([IMG-14](#img-14-unprivileged-ports)).
- **Expected:** Observed behaviour equals the declaration.
- **Evidence:** The declaration; the smoke test's comparison report.
- **Anchors:** [V-203638](../srg/general-purpose-operating-system-srg/rules/V-203638.md) → [CM-7](../crosswalk/controls/cm-7.md)
- **Platform:** [PLT-16](platform.md#plt-16-runtime-behaviour-is-monitored)
- **Source:** [NIST SP 800-190 §4.4.2, §4.4.4](nist-800-190.md#container)

## Release

### IMG-21 Bill of materials

**Required.** Each release carries a bill of materials, in SPDX or CycloneDX,
generated from the built image and attached to it as an attestation.

- **Implementation:** The release workflow generates an SBOM from the built
  image, validates it, and attests it to the digest.
- **Verification:** The release workflow generates, validates, and attests the
  SBOM, and
  a verification step retrieves it by digest.
- **Expected:** An SBOM attestation is retrievable by digest and validates.
- **Evidence:** The SBOM; its attestation; the verification step's output.
- **Anchors:** No rendered SRG rule. Serves CM-8 and SR-4.

### IMG-22 Signed, with provenance

**Required.** Each released image digest is signed with a keyless identity bound
to the release workflow, and carries SLSA v1.2 build provenance, in in-toto
format, naming the workflow and commit. The release workflow verifies both
before it finishes.

- **Implementation:** The release workflow signs the digest with a keyless
  identity and attests SLSA v1.2 build provenance in in-toto format.
- **Verification:** The release verifies the signature against the expected
  identity and
  issuer, and retrieves the provenance attestation.
- **Expected:** The signature and provenance verify against the expected
  identity and issuer.
- **Evidence:** The signature; the provenance attestation; the verification
  output.
- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)
- **Platform:** [PLT-01](platform.md#plt-01-images-are-admitted-by-verified-digest)

### IMG-23 Identifying labels

**Required.** The image carries OCI labels for source, revision, version, and
creation time, plus the base digest and lock digest it was built from.

- **Implementation:** The build sets OCI labels for source, revision, version,
  creation time, base digest, and lock digest.
- **Verification:** Each label is present and the revision matches the release
  commit.
- **Expected:** Every label is present and the revision equals the release
  commit.
- **Evidence:** The image configuration.
- **Anchors:** No rendered SRG rule. Serves CM-8.

### IMG-24 Immutable tags

**Required.** Releases are published under version tags that are never moved.
There is no `latest` tag.

- **Implementation:** The release workflow publishes only version tags and
  refuses one that exists.
- **Verification:** The release workflow refuses to overwrite an existing tag
  and never
  pushes `latest`.
- **Expected:** No tag is ever overwritten, and no `latest` tag exists.
- **Evidence:** The release workflow; the registry's tag list.
- **Anchors:** No rendered SRG rule. Serves CM-2 (baseline configuration).
- **Platform:** [PLT-01](platform.md#plt-01-images-are-admitted-by-verified-digest)

### IMG-25 Vulnerability gate and remediation

**Required.** The build fails on any Critical or High vulnerability with an
available fix, and every finding is recorded with the release. Once a fix is
available, it ships within 7 days for Critical or CISA KEV, 14 days for High,
and 30 days otherwise.

- **Implementation:** The build scans the image, every layer included, with a
  refreshed vulnerability database, and fails on fixed Critical or High
  findings.
- **Verification:** The scan step fails the build on fixed Critical or High
  findings;
  the full findings report is attached to the release. The scan covers every
  layer, not only the base's packages: an upstream binary or archive is scanned
  through the components the SBOM records for it.
- **Expected:** No fixed Critical or High finding in a released image, and every
  finding is recorded.
- **Evidence:** The scan report attached to the release.
- **Source:** [NIST SP 800-190 §4.1.1](nist-800-190.md#image)
- **Anchors:** [V-259333](../srg/general-purpose-operating-system-srg/rules/V-259333.md) → [SI-2](../crosswalk/controls/si-2.md); [V-203755](../srg/general-purpose-operating-system-srg/rules/V-203755.md) → [SI-2(6)](../crosswalk/controls/si-2.6.md)
- **Platform:** [PLT-08](platform.md#plt-08-images-are-scanned-and-replaced)

### IMG-28 Malware scan

**Required.** Each built image is scanned for malware, with signatures updated
before the scan, and so are the retrieved build inputs before assembly. A
detection fails the build. Verifying an input by digest establishes that it is
the file that was reviewed, not that the file is benign.

- **Implementation:** The build scans the retrieved inputs and the exported
  image filesystem with refreshed signatures.
- **Verification:** The build scans the retrieved inputs and the exported image
  filesystem with a malware scanner whose signature database was refreshed in
  the same run, and fails on any detection.
- **Expected:** No detection; a detection fails the build.
- **Evidence:** The scan reports with the signature database version.
- **Anchors:** No rendered SRG rule. Serves SI-3 (malicious code protection).
- **Platform:** [PLT-08](platform.md#plt-08-images-are-scanned-and-replaced)
- **Source:** [NIST SP 800-190 §4.1.3](nist-800-190.md#image); DISA process
  guide §7.1 step 1f

### IMG-26 Exceptions expire

**Required.** A vulnerability or criterion that will not be met in time is an
exception: scoped to one image digest, with a reason, an owner, and an expiry
date. An expired exception fails the build.

- **Implementation:** Exceptions are deviations in the hardening profile,
  checked by `check-profile.py`.
- **Verification:** Exceptions are the `deviations` in the image's
  [hardening profile](../TAILORING.md#deviations), checked in CI by
  `check-profile.py`; an entry past its expiry, or recorded for longer than
  its kind allows, fails.
- **Expected:** No expired or over-long deviation exists.
- **Evidence:** The profile; the checker's output.
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

### IMG-T4 SLSA Build Level 3

The build runs on a hardened, isolated builder whose provenance the build
itself cannot forge, meeting SLSA v1.2 Build Level 3. Required provenance
(IMG-22) meets Build Level 2.

- **Anchors:** [V-203720](../srg/general-purpose-operating-system-srg/rules/V-203720.md) → [CM-14](../crosswalk/controls/cm-14.md)

### IMG-T3 Compliance scan

An OpenSCAP scan of the image against an agreed, GPOS-derived rule selection,
published with each release. It is a target rather than a requirement because
no agreed rule selection exists yet; scanning each image against its own
selection would make results incomparable.

- **Anchors:** [V-203780](../srg/general-purpose-operating-system-srg/rules/V-203780.md) → [CM-6](../crosswalk/controls/cm-6.md)
