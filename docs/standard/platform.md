# Platform expectations

What the platform running a Datopsis image must do, for the image's
[criteria](criteria.md) to amount to anything.

An image criterion establishes that the image *works under* a restriction. The
platform expectation is that the restriction is *imposed*. Neither half meets a
control alone. An image that runs fine read-only, deployed where the root
filesystem is writable, is running with a writable root filesystem.

These are assessed against the DISA Container Platform SRG, and they belong to
whoever runs the orchestrator, not to the image repository. **An image cannot
satisfy any of them**, and no image repository may record one as
`image-owned`. Under the control model each is `deployment-configured` or
`host-inherited`, with the image's contribution named alongside it.

The host beneath the platform is assessed against the DISA RHEL 9 STIG and is
out of scope here, except where noted.

### PLT-01 Images are admitted by verified digest

The platform deploys images by digest, not tag, and admits an image only after
verifying its signature against the expected release identity and its
provenance. Only images from an allow-listed registry and repository run.

- **Image contribution:** [IMG-22](criteria.md#img-22-signed-with-provenance),
  [IMG-24](criteria.md#img-24-immutable-tags)
- **Anchors:** [V-233065](../srg/container-platform-srg/rules/V-233065.md) → [CM-14](../crosswalk/controls/cm-14.md); [V-233192](../srg/container-platform-srg/rules/V-233192.md) → [CM-7(5)](../crosswalk/controls/cm-7.5.md); [V-233185](../srg/container-platform-srg/rules/V-233185.md) → [CM-11(2)](../crosswalk/controls/cm-11.2.md)

### PLT-02 Least privilege is imposed

Containers run as non-root with privilege escalation disallowed, every
capability dropped, and no privileged mode. The platform refuses a workload
that asks for any of these rather than granting it.

- **Image contribution:** [IMG-11](criteria.md#img-11-non-root-with-no-privilege-transition),
  [IMG-12](criteria.md#img-12-runs-under-an-arbitrary-uid),
  [IMG-13](criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges)
- **Anchors:** [V-233163](../srg/container-platform-srg/rules/V-233163.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md); [V-233162](../srg/container-platform-srg/rules/V-233162.md) → [AC-6(10)](../crosswalk/controls/ac-6.10.md); [V-233127](../srg/container-platform-srg/rules/V-233127.md) → [SC-4](../crosswalk/controls/sc-4.md)

### PLT-03 The root filesystem is read-only

Containers run with a read-only root filesystem. The writable paths an image
declares are provided, and temporary ones are mounted `rw,noexec,nosuid,nodev`
with a size limit.

- **Image contribution:** [IMG-15](criteria.md#img-15-read-only-root-filesystem)
- **Anchors:** [V-270876](../srg/container-platform-srg/rules/V-270876.md) → [CM-5(1)](../crosswalk/controls/cm-5.1.md)

### PLT-04 Ports are non-privileged and declared

The runtime refuses privileged ports, and exposes only the ports, protocols,
and services the deployment declares.

- **Image contribution:** [IMG-14](criteria.md#img-14-unprivileged-ports)
- **Anchors:** [V-233074](../srg/container-platform-srg/rules/V-233074.md) → [CM-7](../crosswalk/controls/cm-7.md); [V-233073](../srg/container-platform-srg/rules/V-233073.md) → [CM-7](../crosswalk/controls/cm-7.md)

### PLT-05 Resources are bounded

Every container has CPU and memory limits, and a process count limit where the
runtime supports one.

- **Image contribution:** none. An image cannot bound its own resources.
- **Anchors:** [V-270875](../srg/container-platform-srg/rules/V-270875.md) → [SC-5(2)](../crosswalk/controls/sc-5.2.md); [V-233229](../srg/container-platform-srg/rules/V-233229.md) → [SI-16](../crosswalk/controls/si-16.md)

### PLT-06 Secrets are delivered as read-only files

Secrets and trust material come from a secret store and are mounted into the
container read-only, readable only by the container's identity. They are never
injected as environment variables.

- **Image contribution:** [IMG-16](criteria.md#img-16-secrets-only-as-read-only-files),
  [IMG-17](criteria.md#img-17-trust-material-supplied-by-the-operator)
- **Anchors:** [V-233028](../srg/container-platform-srg/rules/V-233028.md) → [AC-3](../crosswalk/controls/ac-3.md); [V-263600](../srg/container-platform-srg/rules/V-263600.md) → [SC-28(3)](../crosswalk/controls/sc-28.3.md); [V-263599](../srg/container-platform-srg/rules/V-263599.md) → [SC-17](../crosswalk/controls/sc-17.md)

### PLT-07 Containers are isolated

Each container runs in its own namespaces, with no host network, PID, or IPC
namespace and no container engine socket mounted. The runtime applies its
default seccomp profile, and SELinux is enforcing on the host.

- **Image contribution:** [IMG-13](criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges),
  which lets the image run under the tightest profile the platform offers.
- **Anchors:** [V-233221](../srg/container-platform-srg/rules/V-233221.md) → [SC-39](../crosswalk/controls/sc-39.md); [V-233128](../srg/container-platform-srg/rules/V-233128.md) → [SC-4](../crosswalk/controls/sc-4.md)

### PLT-08 Images are scanned and replaced

The platform scans the images it runs and holds for vulnerabilities
continuously, not only at build. It holds updated images within 30 days of a
security-relevant update, and removes superseded ones.

- **Image contribution:** [IMG-25](criteria.md#img-25-vulnerability-gate-and-remediation),
  which ships the updated image the platform must then adopt.
- **Anchors:** [V-233275](../srg/container-platform-srg/rules/V-233275.md) → [CM-6](../crosswalk/controls/cm-6.md); [V-233233](../srg/container-platform-srg/rules/V-233233.md) → [SI-2](../crosswalk/controls/si-2.md); [V-233231](../srg/container-platform-srg/rules/V-233231.md) → [SI-2(6)](../crosswalk/controls/si-2.6.md)

### PLT-09 Logs are collected centrally

The platform collects each container's standard output and standard error and
sends them to a central store for review, protected from modification by the
workload.

- **Image contribution:** [IMG-19](criteria.md#img-19-logs-to-standard-streams-without-secrets)
- **Anchors:** [V-233052](../srg/container-platform-srg/rules/V-233052.md) → [AU-6(4)](../crosswalk/controls/au-6.4.md); [V-233057](../srg/container-platform-srg/rules/V-233057.md) → [AU-9](../crosswalk/controls/au-9.md)

### PLT-10 Traffic is controlled and encrypted

Network policy permits only the flows the deployment declares, and traffic
leaving the platform uses TLS 1.2 or later.

- **Image contribution:** the image's documented listeners and TLS support.
- **Anchors:** [V-233029](../srg/container-platform-srg/rules/V-233029.md) → [AC-4](../crosswalk/controls/ac-4.md); [V-233016](../srg/container-platform-srg/rules/V-233016.md) → [AC-17(2)](../crosswalk/controls/ac-17.2.md)

### PLT-11 Stops are given time to finish

The platform's stop timeout is at least the drain time the image documents, so
that the image's stop signal handling can complete before a forced kill.

- **Image contribution:** [IMG-20](criteria.md#img-20-lifecycle-is-declared)
- **Anchors:** [V-233122](../srg/container-platform-srg/rules/V-233122.md) → [SC-24](../crosswalk/controls/sc-24.md)
