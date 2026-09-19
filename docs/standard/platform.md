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
`host-inherited`, with the image's contribution named alongside it. Each
expectation states which: `deployment-configured` where the deployment's own
manifest must set it, `host-inherited` where the orchestrator or host provides
it for every workload.

The host beneath the platform is assessed against the DISA RHEL 9 STIG. Its
expectations are listed [at the end](#host-expectations), because NIST SP
800-190 treats the host as one of the five tiers a container depends on.

Each expectation cites the [NIST SP 800-190](nist-800-190.md) countermeasures it
implements.

### PLT-01 Images are admitted by verified digest

The platform deploys images by digest, not tag, and admits an image only when
every one of these holds:

- it comes from a known, allow-listed registry and repository
- its signature is valid
- the signer is an approved release identity
- its provenance is valid and names an approved build
- it is built on an approved base
- it is within the vulnerability threshold
- its requested security context is acceptable
Every pull and push travels over TLS between authenticated endpoints.

- **Origination:** `host-inherited`
- **Implementation:** Admission policy in the orchestrator verifies each image's
  registry, signature, signer, provenance, approved base, vulnerability status,
  and security context before it runs.
- **Verification:** Attempt to deploy an unsigned image, one signed by an
  unexpected identity, one without provenance, one from an unlisted registry,
  and one by tag.
- **Expected:** Every attempt is denied, and a correctly signed image by digest
  is admitted.
- **Evidence:** The admission-test results, the policy version, and the cluster
  version, with a timestamp.
- **Image contribution:** [IMG-22](criteria.md#img-22-signed-with-provenance),
  [IMG-24](criteria.md#img-24-immutable-tags)
- **Anchors:** [V-233065](../srg/container-platform-srg/rules/V-233065.md) → [CM-14](../crosswalk/controls/cm-14.md); [V-233192](../srg/container-platform-srg/rules/V-233192.md) → [CM-7(5)](../crosswalk/controls/cm-7.5.md); [V-233185](../srg/container-platform-srg/rules/V-233185.md) → [CM-11(2)](../crosswalk/controls/cm-11.2.md); [V-233015](../srg/container-platform-srg/rules/V-233015.md) → [AC-17(2)](../crosswalk/controls/ac-17.2.md)
- **Source:** [SP 800-190 §4.1.5, §4.2.1, §4.4.5](nist-800-190.md#registry)

### PLT-02 Least privilege is imposed

Containers run as non-root with privilege escalation disallowed, every
capability dropped, and no privileged mode. The platform refuses a workload
that asks for any of these rather than granting it.

- **Origination:** `deployment-configured`
- **Implementation:** Admission enforces the restricted-v3 SCC on OpenShift, or
  the Restricted Pod Security Standard with user namespaces elsewhere.
- **Verification:** Attempt to deploy a workload that is privileged, runs as
  root, adds a capability, or allows privilege escalation.
- **Expected:** Every attempt is denied.
- **Evidence:** The admission-test results, the policy version, and the cluster
  version, with a timestamp.
- **Image contribution:** [IMG-11](criteria.md#img-11-non-root-with-no-privilege-transition),
  [IMG-12](criteria.md#img-12-runs-under-an-arbitrary-uid),
  [IMG-13](criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges)
- **Anchors:** [V-233163](../srg/container-platform-srg/rules/V-233163.md) → [AC-6(8)](../crosswalk/controls/ac-6.8.md); [V-233162](../srg/container-platform-srg/rules/V-233162.md) → [AC-6(10)](../crosswalk/controls/ac-6.10.md); [V-233127](../srg/container-platform-srg/rules/V-233127.md) → [SC-4](../crosswalk/controls/sc-4.md)

### PLT-03 The root filesystem is read-only

Containers run with a read-only root filesystem. The writable paths an image
declares are provided, and temporary ones are mounted `rw,noexec,nosuid,nodev`
with a size limit.

- **Origination:** `deployment-configured`
- **Implementation:** Workload manifests set `readOnlyRootFilesystem`, and
  admission requires it.
- **Verification:** Attempt to deploy a workload with a writable root
  filesystem.
- **Expected:** The attempt is denied.
- **Evidence:** The admission-test result and policy version.
- **Image contribution:** [IMG-15](criteria.md#img-15-read-only-root-filesystem)
- **Anchors:** [V-270876](../srg/container-platform-srg/rules/V-270876.md) → [CM-5(1)](../crosswalk/controls/cm-5.1.md)

### PLT-04 Ports are non-privileged and declared

The runtime refuses privileged ports, and exposes only the ports, protocols,
and services the deployment declares.

- **Origination:** `deployment-configured`
- **Implementation:** The runtime refuses ports below 1024, and network policy
  exposes only declared ports.
- **Verification:** Attempt to bind a privileged port, and to reach an
  undeclared one.
- **Expected:** Both fail.
- **Evidence:** The test results and the policy version.
- **Image contribution:** [IMG-14](criteria.md#img-14-unprivileged-ports)
- **Anchors:** [V-233074](../srg/container-platform-srg/rules/V-233074.md) → [CM-7](../crosswalk/controls/cm-7.md); [V-233073](../srg/container-platform-srg/rules/V-233073.md) → [CM-7](../crosswalk/controls/cm-7.md)

### PLT-05 Resources are bounded

Every container has CPU and memory limits, and a process count limit where the
runtime supports one.

- **Origination:** `deployment-configured`
- **Implementation:** Admission requires CPU, memory, and process limits on
  every container.
- **Verification:** Attempt to deploy a container without limits.
- **Expected:** The attempt is denied.
- **Evidence:** The admission-test result.
- **Image contribution:** none. An image cannot bound its own resources.
- **Anchors:** [V-270875](../srg/container-platform-srg/rules/V-270875.md) → [SC-5(2)](../crosswalk/controls/sc-5.2.md); [V-233229](../srg/container-platform-srg/rules/V-233229.md) → [SI-16](../crosswalk/controls/si-16.md)

### PLT-06 Secrets are delivered as read-only files

Secrets and trust material come from a secret store and are mounted into the
container read-only, readable only by the container's user or a group it
belongs to, and never by others: on Kubernetes, `defaultMode: 0440` with the
pod's `fsGroup`, since the default mode is world-readable (see
[group read, by example](criteria.md#group-read-by-example)). They are never
injected as environment variables. The secret store encrypts them at rest and
in transit with FIPS 140 approved algorithms in a validated module, and
provides each secret only to the workloads that require it.

- **Origination:** `deployment-configured`
- **Implementation:** A secret store mounts secrets read-only, per workload,
  encrypted at rest with a validated module.
- **Verification:** Attempt to inject a secret as an environment variable, and
  to read another workload's secret.
- **Expected:** Both fail.
- **Evidence:** The test results and the store's configuration.
- **Image contribution:** [IMG-16](criteria.md#img-16-secrets-only-as-read-only-files),
  [IMG-17](criteria.md#img-17-trust-material-supplied-by-the-operator)
- **Anchors:** [V-233028](../srg/container-platform-srg/rules/V-233028.md) → [AC-3](../crosswalk/controls/ac-3.md); [V-263600](../srg/container-platform-srg/rules/V-263600.md) → [SC-28(3)](../crosswalk/controls/sc-28.3.md); [V-263599](../srg/container-platform-srg/rules/V-263599.md) → [SC-17](../crosswalk/controls/sc-17.md); [V-233220](../srg/container-platform-srg/rules/V-233220.md) → [SC-28(1)](../crosswalk/controls/sc-28.1.md)
- **Source:** [SP 800-190 §4.1.4](nist-800-190.md#image)

### PLT-07 Containers are isolated

Each container runs in its own namespaces, with no host network, PID, or IPC
namespace and no container engine socket mounted. The runtime applies at least
its default seccomp profile, and SELinux is enforcing on the host. Containers
mount no host path other than volumes allocated for them, and never a host
configuration directory; the platform refuses a workload that asks.

- **Origination:** `host-inherited`
- **Implementation:** Admission forbids host namespaces, host paths outside
  allocated volumes, the engine socket, and unconfined seccomp; SELinux is
  enforcing.
- **Verification:** Attempt each forbidden setting.
- **Expected:** Every attempt is denied.
- **Evidence:** The admission-test results and the host's SELinux status.
- **Image contribution:** [IMG-13](criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges),
  which lets the image run under the tightest profile the platform offers.
- **Anchors:** [V-233221](../srg/container-platform-srg/rules/V-233221.md) → [SC-39](../crosswalk/controls/sc-39.md); [V-233128](../srg/container-platform-srg/rules/V-233128.md) → [SC-4](../crosswalk/controls/sc-4.md); [V-233125](../srg/container-platform-srg/rules/V-233125.md) → [SC-3](../crosswalk/controls/sc-3.md)
- **Source:** [SP 800-190 §4.4.3, §4.5.5](nist-800-190.md#container)

### PLT-08 Images are scanned and replaced

The platform scans the images it runs and holds for vulnerabilities
continuously, not only at build, for vulnerabilities and for malware. It holds
updated images within 30 days of a security-relevant update, and removes
superseded ones. The container runtime itself is patched on the same timeline,
and the orchestrator schedules workloads only onto maintained runtimes.

- **Origination:** `host-inherited`
- **Implementation:** The registry and cluster scan images and runtimes
  continuously, for vulnerabilities and malware.
- **Verification:** Introduce an image with a known vulnerability, and one with
  a test malware signature.
- **Expected:** Both are reported, and the policy acts on them.
- **Evidence:** The scan reports and the resulting action.
- **Image contribution:** [IMG-25](criteria.md#img-25-vulnerability-gate-and-remediation),
  which ships the updated image the platform must then adopt.
- **Anchors:** [V-233275](../srg/container-platform-srg/rules/V-233275.md) → [CM-6](../crosswalk/controls/cm-6.md); [V-233233](../srg/container-platform-srg/rules/V-233233.md) → [SI-2](../crosswalk/controls/si-2.md); [V-233231](../srg/container-platform-srg/rules/V-233231.md) → [SI-2(6)](../crosswalk/controls/si-2.6.md); [V-233234](../srg/container-platform-srg/rules/V-233234.md) → [SI-2](../crosswalk/controls/si-2.md)
- **Source:** [SP 800-190 §4.1.1, §4.1.3, §4.2.2, §4.4.1](nist-800-190.md#image)

### PLT-09 Logs are collected centrally

The platform collects each container's standard output and standard error and
sends them to a central store for review, protected from modification by the
workload.

- **Origination:** `host-inherited`
- **Implementation:** Container output is forwarded to a central log store and
  SIEM that workloads cannot modify.
- **Verification:** Emit a marker line from a container, then attempt to alter
  the stored copy.
- **Expected:** The marker arrives, and the alteration fails.
- **Evidence:** The log store's record of the marker, and the denied change.
- **Image contribution:** [IMG-19](criteria.md#img-19-logs-to-standard-streams-without-secrets)
- **Anchors:** [V-233052](../srg/container-platform-srg/rules/V-233052.md) → [AU-6(4)](../crosswalk/controls/au-6.4.md); [V-233057](../srg/container-platform-srg/rules/V-233057.md) → [AU-9](../crosswalk/controls/au-9.md)

### PLT-10 Traffic is controlled and encrypted

Network policy permits only the flows the deployment declares, inbound and
outbound. Workloads of different sensitivity are on separate virtual networks
and communicate only through declared interfaces. Egress is denied by default.
Traffic leaving the platform uses TLS 1.2 or later.

- **Origination:** `deployment-configured`
- **Implementation:** Network policy is deny-by-default in both directions,
  segmented by sensitivity; external traffic uses TLS 1.2 or later.
- **Verification:** Attempt an undeclared connection inbound and outbound, and
  an external connection below TLS 1.2.
- **Expected:** All three fail.
- **Evidence:** The test results and the policy version.
- **Image contribution:** [IMG-30](criteria.md#img-30-expected-behaviour-is-declared),
  which declares the image's listeners and outbound destinations.
- **Anchors:** [V-233029](../srg/container-platform-srg/rules/V-233029.md) → [AC-4](../crosswalk/controls/ac-4.md); [V-233016](../srg/container-platform-srg/rules/V-233016.md) → [AC-17(2)](../crosswalk/controls/ac-17.2.md); [V-233030](../srg/container-platform-srg/rules/V-233030.md) → [AC-4](../crosswalk/controls/ac-4.md)
- **Source:** [SP 800-190 §4.3.3, §4.4.2](nist-800-190.md#orchestrator)

### PLT-11 Stops are given time to finish

The platform's stop timeout is at least the drain time the image documents, so
that the image's stop signal handling can complete before a forced kill.

- **Origination:** `deployment-configured`
- **Implementation:** Each deployment's termination grace period is at least the
  image's documented drain time.
- **Verification:** Compare each deployment's grace period with the image's
  documentation.
- **Expected:** No deployment is shorter.
- **Evidence:** The comparison report.
- **Image contribution:** [IMG-20](criteria.md#img-20-lifecycle-is-declared)
- **Anchors:** [V-233122](../srg/container-platform-srg/rules/V-233122.md) → [SC-24](../crosswalk/controls/sc-24.md)

### PLT-12 Registry access is controlled and audited

Every write to the registry requires authentication, and write access is
scoped to the repositories a publisher is responsible for. Only the release
workflow pushes, and only after its scans have passed. Writes, and reads of
non-public images, are audited.

- **Origination:** `host-inherited`
- **Implementation:** The registry requires authentication for writes, scopes
  them per repository, and audits them.
- **Verification:** Attempt an unauthenticated push, and a push to another
  team's repository.
- **Expected:** Both fail and are audited.
- **Evidence:** The registry audit log entries.
- **Image contribution:** [IMG-22](criteria.md#img-22-signed-with-provenance),
  [IMG-25](criteria.md#img-25-vulnerability-gate-and-remediation)
- **Anchors:** [V-233026](../srg/container-platform-srg/rules/V-233026.md) → [AC-3](../crosswalk/controls/ac-3.md); [V-233066](../srg/container-platform-srg/rules/V-233066.md) → [CM-5(6)](../crosswalk/controls/cm-5.6.md); [V-233186](../srg/container-platform-srg/rules/V-233186.md) → [CM-11(2)](../crosswalk/controls/cm-11.2.md)
- **Source:** [SP 800-190 §4.2.3](nist-800-190.md#registry)

### PLT-13 Orchestrator administration is least-privilege and audited

Administrative access to the orchestrator is scoped to the hosts, namespaces,
and images each role requires, authenticated with multiple factors, and
federated with the organization's directory. Every container creation is tied
to an individual identity and logged. Development, test, and production are
separate environments.

- **Origination:** `host-inherited`
- **Implementation:** Orchestrator administration uses least-privilege roles,
  multifactor authentication, and directory federation, and logs every container
  creation with its identity.
- **Verification:** Attempt an action outside a role's scope, and a login
  without a second factor.
- **Expected:** Both fail; container creations are logged with identities.
- **Evidence:** The audit log entries.
- **Image contribution:** none. An image has no say in who administers the
  platform that runs it.
- **Anchors:** [V-233027](../srg/container-platform-srg/rules/V-233027.md) → [AC-3](../crosswalk/controls/ac-3.md); [V-233079](../srg/container-platform-srg/rules/V-233079.md) → [IA-2(1)](../crosswalk/controls/ia-2.1.md); [V-233270](../srg/container-platform-srg/rules/V-233270.md) → [AU-12](../crosswalk/controls/au-12.md)
- **Source:** [SP 800-190 §4.3.1, §4.3.2, §4.4.5](nist-800-190.md#orchestrator)

### PLT-14 Workloads are placed by sensitivity

Workloads of different sensitivity levels do not share a host kernel. The
orchestrator pins each sensitivity level to its own set of hosts, or to its own
cluster, so that a compromise at one level does not reach data cached at
another.

- **Origination:** `host-inherited`
- **Implementation:** Scheduling rules pin each sensitivity level to its own
  hosts or cluster.
- **Verification:** Attempt to schedule a workload onto a host of another
  sensitivity level.
- **Expected:** The attempt is refused.
- **Evidence:** The scheduling-test result and the rules' version.
- **Image contribution:** none.
- **Anchors:** No rendered SRG rule. Serves SC-4 and SC-7.
- **Source:** [SP 800-190 §4.3.4](nist-800-190.md#orchestrator)

### PLT-15 Nodes are trusted before they run workloads

Nodes are introduced to the cluster securely, keep a persistent identity, and
are inventoried. Cluster members authenticate each other, and traffic between
them is encrypted end to end. A compromised node can be isolated without
disrupting the cluster.

- **Origination:** `host-inherited`
- **Implementation:** Nodes join through an attested bootstrap, keep persistent
  identities, and communicate over mutually authenticated, encrypted channels.
- **Verification:** Attempt to join an unapproved node, and to read cluster
  traffic in transit.
- **Expected:** Both fail.
- **Evidence:** The test results and the node inventory.
- **Image contribution:** none.
- **Anchors:** [V-233086](../srg/container-platform-srg/rules/V-233086.md) → [IA-3](../crosswalk/controls/ia-3.md)
- **Source:** [SP 800-190 §4.3.5](nist-800-190.md#orchestrator)

### PLT-16 Runtime behaviour is monitored

A container-aware runtime monitor compares what each container does with what
it is expected to do, and alerts on unexpected processes, system calls, writes,
listeners, and outbound connections, and on changes to protected binaries and
configuration.

- **Origination:** `host-inherited`
- **Implementation:** A container-aware runtime monitor compares each
  container's behaviour with its image's declaration and alerts on differences.
- **Verification:** Start an undeclared process and open an undeclared listener
  in a test container.
- **Expected:** Both raise alerts.
- **Evidence:** The alerts.
- **Image contribution:** [IMG-30](criteria.md#img-30-expected-behaviour-is-declared),
  which supplies the expected behaviour instead of leaving the monitor to learn it
- **Anchors:** [V-233244](../srg/container-platform-srg/rules/V-233244.md) → [SI-6](../crosswalk/controls/si-6.md)
- **Source:** [SP 800-190 §4.4.4](nist-800-190.md#container)

### PLT-17 Data volumes are encrypted at rest

Volumes that hold a container's persistent data are encrypted at rest, with the
same barriers to unauthorized access wherever the container is scheduled.

- **Origination:** `host-inherited`
- **Implementation:** Persistent volumes are provisioned from encrypted storage
  classes.
- **Verification:** Inspect every storage class persistent volumes use.
- **Expected:** Every one encrypts at rest.
- **Evidence:** The storage-class configuration.
- **Image contribution:** [IMG-15](criteria.md#img-15-read-only-root-filesystem),
  which confines persistent data to declared volumes
- **Anchors:** No rendered SRG rule. Serves SC-28.
- **Source:** [SP 800-190 §4.3.2](nist-800-190.md#orchestrator)

### PLT-18 Workloads have identities and authenticate each other

Each workload has a cryptographic identity issued by the platform, and
service-to-service traffic is mutually authenticated and encrypted with it.
Authorization between services is by identity, not network location.

- **Origination:** `host-inherited`
- **Implementation:** The platform issues workload identities and enforces
  mutual TLS between services, through a service mesh or equivalent.
- **Verification:** Attempt a connection between two services without a valid
  workload identity.
- **Expected:** The connection is refused.
- **Evidence:** The test result and the identity issuer's configuration.
- **Image contribution:** [IMG-17](criteria.md#img-17-trust-material-supplied-by-the-operator),
  which lets the platform supply the trust material identity depends on
- **Anchors:** [V-233077](../srg/container-platform-srg/rules/V-233077.md) → [IA-2](../crosswalk/controls/ia-2.md); [V-233078](../srg/container-platform-srg/rules/V-233078.md) → [IA-2](../crosswalk/controls/ia-2.md)
- **Source:** NIST SP 800-207, SP 800-207A

## Host expectations

The host is assessed against the DISA RHEL 9 STIG, which this repository has
pinned but not yet rendered, so these cite no SRG rule. They are the host
countermeasures of NIST SP 800-190, stated as expectations the host owner must
meet for any Datopsis image's properties to count.

### HST-01 The host runs containers and nothing else

The host is a minimal or container-specific operating system. It runs no
application outside a container and no service a container host does not need.

- **Origination:** `host-inherited`
- **Implementation:** Hosts run a minimal or container-specific operating system
  and no workload outside containers.
- **Verification:** List the host's running services and installed applications.
- **Expected:** Nothing runs beyond the container runtime and its dependencies.
- **Evidence:** The host inventory.
- **Image contribution:** none.
- **Anchors:** No rendered SRG rule. Serves CM-7.
- **Source:** [SP 800-190 §4.5.1, §4.5.2](nist-800-190.md#host-os)

### HST-02 The host is current and immutable

Host components, the kernel and container runtime above all, are kept current
with the vendor's security and component updates. The host stores no unique
persistent state, so it can be replaced rather than repaired.

- **Origination:** `host-inherited`
- **Implementation:** Hosts are updated from the vendor on a schedule and
  replaced rather than repaired.
- **Verification:** Compare each host's kernel and runtime versions with the
  vendor's current release.
- **Expected:** No host is behind by more than the organization's patch window.
- **Evidence:** The version report.
- **Image contribution:** none.
- **Anchors:** No rendered SRG rule. Serves SI-2.
- **Source:** [SP 800-190 §4.5.3](nist-800-190.md#host-os)

### HST-03 Host access is audited

Every authentication to the host is audited, login anomalies are monitored, and
every privilege escalation is logged.

- **Origination:** `host-inherited`
- **Implementation:** Host authentication and privilege escalation are audited
  and forwarded centrally.
- **Verification:** Log in to a host and escalate privilege.
- **Expected:** Both are recorded centrally.
- **Evidence:** The audit records.
- **Image contribution:** none.
- **Anchors:** No rendered SRG rule. Serves AU-2 and AC-6(9).
- **Source:** [SP 800-190 §4.5.4](nist-800-190.md#host-os)

### HST-04 Trust is rooted in hardware

Where the hardware supports it, the host boots with measured or secure boot,
and the chain of trust extends from a hardware root of trust through the
kernel to the container runtime. This is a recommendation in SP 800-190, and it
is one here.

- **Origination:** `host-inherited`
- **Implementation:** Hosts boot with measured or secure boot where the hardware
  supports it.
- **Verification:** Read each host's boot attestation.
- **Expected:** The measurements match the expected values.
- **Evidence:** The attestation records.
- **Image contribution:** [IMG-22](criteria.md#img-22-signed-with-provenance),
  the signature the chain of trust extends to
- **Anchors:** No rendered SRG rule. Serves SI-7.
- **Source:** [SP 800-190 §4.6](nist-800-190.md#hardware)

### HST-05 Clocks are synchronized

The host synchronizes its clock with an authoritative time source, so that the
timestamps on every container's logs, and on the platform's audit records, can
be correlated. A container reads the host's clock; it has none of its own.

- **Origination:** `host-inherited`
- **Implementation:** Hosts synchronize with an authoritative time source.
- **Verification:** Compare each host's clock with the source.
- **Expected:** The offset is within the organization's tolerance.
- **Evidence:** The synchronization status.
- **Image contribution:** none.
- **Anchors:** [V-233055](../srg/container-platform-srg/rules/V-233055.md) → [AU-8](../crosswalk/controls/au-8.md); [V-263601](../srg/container-platform-srg/rules/V-263601.md) → [SC-45](../crosswalk/controls/sc-45.md)
