# The Datopsis container hardening standard

This is what a hardened Datopsis container image is, what it refuses to do, and
why. It is written to be read once, end to end, by an engineer who has never
opened an SRG, and then applied.

The testable form of each position is in [the criteria](criteria.md). What the
platform running the image must do is in [the platform expectations](platform.md).
It follows [NIST SP 800-190](nist-800-190.md), the Application Container
Security Guide, countermeasure by countermeasure. Where it departs from DISA's
process guidance is in [the process guide comparison](process-guide.md). Nothing here is a STIG,
an authorization, or a claim of compliance; see [what this standard does not
claim](#what-this-standard-does-not-claim).

## The short version

A hardened Datopsis image is built only from inputs it can name and verify,
assembled without the network, and shipped with nothing it does not need to run
its one function. It starts as an unprivileged user and stays one. It works
with every privilege the kernel can take away already taken away: no
capabilities, no new privileges, no writable root filesystem, no privileged
port. It takes secrets and trust material only as read-only files the operator
mounts. It has no way in for an administrator, and it says in advance exactly
what it will do when it runs. When something is wrong it stops and says what,
rather than guessing. It arrives with the evidence to check all of that: an
inventory, a bill of materials, a signature, provenance, and clean
vulnerability and malware scans.

Everything below is the reasoning.

## Three layers, and why they stay apart

A running container is three things stacked: an **image**, a **platform** that
runs it, and a **host** underneath. Each has its own DISA baseline and its own
owner.

| Layer | Assessed against | Owned by |
| --- | --- | --- |
| Image | DISA GPOS SRG, plus function-specific SRGs | The image repository |
| Platform | DISA Container Platform SRG | Whoever runs the orchestrator |
| Host | DISA RHEL 9 STIG | Whoever runs the host |

NIST SP 800-190 draws the same picture with five tiers instead of three: image,
registry, orchestrator, container, and host OS. The middle three are all run by
one party, so here they are one layer, the platform. Every one of SP 800-190's
countermeasures is assigned to a layer and to the criteria or expectations that
implement it, in [the SP 800-190 mapping](nist-800-190.md).

No container-specific STIG exists, so DoD guidance is to assess the image
against the General Purpose Operating System SRG. That is what this standard
does.

The failure this standard exists to prevent is **claiming one layer's control
on another layer's behalf.** The clearest case is the Container Platform SRG
itself. It says the container root filesystem must be mounted read-only
([V-270876](../srg/container-platform-srg/rules/V-270876.md)) and that the
runtime must enforce non-privileged ports
([V-233074](../srg/container-platform-srg/rules/V-233074.md)). Those are
platform rules. No image can satisfy them, because the image does not decide how
it is mounted or what the runtime allows.

But an image can make them impossible. An image that writes to `/usr` at
startup cannot run under a read-only root; an image that binds port 80 cannot
run where privileged ports are refused. So the working rule is:

> **The image makes a control achievable. The platform makes it true.**

Every runtime position below is written in that shape. The image criterion is
that it *works under* the restriction, tested by running it under the
restriction. The platform expectation is that the restriction is *imposed*. A
control is only met when both hold, and a Datopsis image never claims the
second half.

## How an image is built

### Every input is named and verified before it is used

The base image, every RPM, every upstream binary: each is pinned by digest in a
lock file committed to the repository, and verified against it before use. A
digest proves the bytes are the ones reviewed. Where the publisher signs its
artifacts, the signature is verified too, because a digest says nothing about
who published the bytes; it only says they have not changed since.

This is the property most worth defending, because every other one depends on
it. A package-manager-free image built from an unverified RPM is a smaller image
of unknown contents.

The base is pinned by manifest-list digest, and the build uses that digest
rather than a tag. A tag is a pointer the publisher can move.

### Refreshing an input is a change someone reviews

Automation may notice that a newer base or package exists. It may not act on
it. A refreshed lock is a pull request with the new digests in the diff, which
is the only point at which a person decides to accept new code into the image.
A bot that rewrites locks has made that decision on everyone's behalf.

### Assembly never touches the network

The build runs with networking disabled and image pulls refused. Everything it
needs was fetched and verified beforehand, in a separate step, and handed to the
build as a local context.

This is not belt-and-braces. If assembly can reach the network, then "every
input is verified" is a claim about the inputs you remembered to verify, and
nothing proves there were no others. A network-disabled build turns that into a
property the build enforces: an input nobody declared is an input that cannot
arrive. It also rules out a layer cache restored from outside the build, which
is the same problem with a different name.

### The base is kept current

A base pinned by digest stays exactly as it was reviewed, which is the point,
and also means it ages. The base is refreshed whenever its publisher ships a
security update and never falls more than 30 days behind. A pinned base that
nobody refreshes becomes a well-verified old one.

### Nothing secret enters the build

No credential is passed as a build argument, copied into a layer, or recorded in
a label. Build arguments are written into image history, so a secret passed that
way ships with every copy of the image.

## What the image contains

### Nothing it does not need

The final image holds the service, the libraries it links, and the files it
reads. There is no package manager, and no repository configuration or signing
keys a package manager would use. There are no compilers, no `curl`, no `wget`,
and no optional modules the function does not use.

A package manager in a running container is a way to change the software
without rebuilding the image, which defeats every verification above. The GPOS
SRG says the same thing from the other direction: software must not be
installable without explicit privilege
([V-203716](../srg/general-purpose-operating-system-srg/rules/V-203716.md)).
In an image with no package manager and no privilege, there is nothing to
install with.

The image carries an inventory of the packages it contains, written at build
time and checked against the lock, so what is inside can be established without
trusting the scanner that looked.

There is no SSH server, remote shell, or other remote administration service.
A container is administered by replacing it, or through the runtime's own
interface; a way to log into it is a way to change it that bypasses every
property above. NIST SP 800-190 says remote administration tools "should never
be enabled within containers", and this standard agrees without exception.

The shell is the obvious next thing to remove, and it is harder than it looks:
UBI Micro ships one, and entrypoints and healthchecks tend to lean on it. It is
a [target](criteria.md#targets), not a requirement: no runtime path may depend
on it, so that removing it later breaks nothing.

### Nothing that raises privilege

No file in the image is setuid or setgid, and nothing outside a declared
writable mount is world-writable. A setuid binary is a privilege transition
waiting for a caller.

### Nothing the runtime identity can rewrite

Executables, libraries, and configuration are owned by root and not writable by
the user the service runs as. If an attacker gets code execution as the
service, they should not also get the ability to change what the service is.
This holds even on a platform that forgets to mount the root filesystem
read-only.

## How the image runs

### As an unprivileged user, and only that

The image declares a numeric, non-zero user with primary group 0, and no process
in the container ever runs as UID 0. There is no root phase at startup: no
entrypoint that starts as root to fix permissions and then drops privilege, and
no `su`, `sudo`, or `gosu`.

A "drop privileges after setup" entrypoint is the common pattern and the one
this standard refuses. It makes the first seconds of every container run the
most privileged, and it requires the platform to permit root, which is the one
thing the platform should never have to permit.

The image also runs correctly under an arbitrary UID in group 0, because
OpenShift assigns one and a platform should not have to accommodate the image's
choice.

### With nothing left to take away

The image works with every Linux capability dropped and `no-new-privileges` set.
That is tested by running it that way and reading each process's effective
capability set and `NoNewPrivs` flag from `/proc`, not by passing the flags and
assuming they applied.

Every listener is on a port at or above 1024. This is tested by reading the
sockets the service actually opened, not by relying on a capability drop: Docker
lowers the privileged-port boundary to zero by default, so a service binding
port 80 under `--cap-drop ALL` succeeds there and proves nothing.

### On a read-only root filesystem

The image runs with the root filesystem mounted read-only. Every path it writes
is declared, and each declared temporary mount is expected as
`rw,noexec,nosuid,nodev`. If a declared mount is missing, the service exits
non-zero and names the path.

Declaring the writable paths is the part that matters. An image that works with
a read-only root "as long as you also mount these six things" is fine, provided
the six things are written down and the image fails clearly without them.

### With secrets and trust material as read-only files

Secrets reach the image only as files on a read-only mount. Never in an
environment variable, never on a command line, never in a layer, never in a log.
Where a service conventionally takes a secret from the environment, the image
offers a `_FILE` form and uses it. Trust material, meaning CA bundles and trust
stores the operator chooses, arrives the same way.

Environment variables are the usual way to hand a container a password, and
they are the wrong way. They are readable from `/proc/<pid>/environ`, inherited
by every child process, and routinely printed by diagnostics and orchestrator
tooling. A read-only file has one reader and cannot be rewritten by the process
that reads it. This is recorded in
[ADR-0003](../adr/0003-secrets-reach-an-image-only-as-read-only-files.md),
because it is the position most likely to be argued with.

### Failing closed

When configuration is invalid, a required mount is missing, or a secret is
absent or malformed, the service exits non-zero and says what is wrong. It does
not fall back to packaged defaults, create what is missing, or start a repair
shell. A service that starts with defaults its operator did not choose is
running a configuration nobody reviewed.

### Predictably

The image declares, in a file committed beside it, what it does when it runs:
which processes, which listening ports, which paths it writes, which
destinations it calls. The smoke suite checks the running image against that
declaration.

This is the image's contribution to runtime defence. A platform's runtime
monitor flags what an image does that it should not; it can only do that
against a description of what the image should do. SP 800-190 expects such
tools to learn that description by watching. An image that states it up front
removes the learning period, and makes a new process or an unexpected listener
evidence in itself.

### Observably

Logs go to standard output and standard error, where the platform collects them,
and never contain secrets. The image declares a healthcheck, and its
documentation says what the healthcheck proves, because "configuration parses"
and "service answers" are different claims. The service runs as PID 1 or under a
minimal init, and handles its declared stop signal so that a platform stopping
it gets a clean shutdown.

## How the image is shipped

A released image carries:

- **An SPDX bill of materials** generated from the built image, not the source
- **A signature** over the image digest, made in CI with a keyless identity
  bound to the release workflow
- **Provenance** stating which workflow built it, from which commit
- **OCI labels** naming the source, revision, version, creation time, base
  digest, and lock digest

It is published under an immutable version tag. There is no `latest`. A tag that
means something different tomorrow cannot be what a deployment pins.

The consumer's side of this is to deploy by digest and verify the signature and
provenance before the image is admitted. That is a
[platform expectation](platform.md), and it is the other half of digest pinning:
the image pins its base; the deployment pins the image.

## Vulnerabilities

The build fails on any Critical or High vulnerability for which a fix is
available. Every finding, fixed or not, is recorded with the release.

Once a fix is available, it ships within:

| Severity | Remediation |
| --- | --- |
| Critical, or listed in CISA KEV | 7 days |
| High | 14 days |
| Medium and Low | 30 days |

The 30-day ceiling is not arbitrary. The GPOS SRG requires security-relevant
updates within 30 days
([V-259333](../srg/general-purpose-operating-system-srg/rules/V-259333.md)),
and the Container Platform SRG requires the registry to hold images carrying
them within 30 days
([V-233233](../srg/container-platform-srg/rules/V-233233.md)). A platform
cannot meet its obligation if the image misses its own.

The image is also scanned for malware, as are the inputs it was built from,
with signatures refreshed in the same run. Verifying an input by digest proves
it is the file that was reviewed. It does not prove the file is benign, and both
NIST SP 800-190 and the DISA process guide ask for the second check.

A finding that will not be fixed in time is an exception: scoped to one image
digest, with a reason and an expiry. An exception without an expiry is a
permanent decision nobody made.

## What this standard refuses

Some refusals are about the image, and are described above: no root phase, no
package manager, no secrets in the environment, no repair shell, no mutable
tags. Others are about what is claimed:

- **No STIG certification.** A STIG is a DISA product for a specific technology.
  An image assessed against the GPOS SRG has been assessed against the GPOS SRG,
  and says exactly that.
- **No FIPS validation claim.** Using a FIPS-capable library inside an image does
  not create a validated cryptographic boundary, and the standard does not let
  an image imply one.
- **No authorization.** This produces a standard and a mapping. An authorization
  is a decision an authorizing official makes about a system, and an image is
  not a system.

## What this standard does not claim

It does not claim an image meets any control on its own. Under
[the control model](../ROADMAP.md#package-3-the-control-mapping), only a control
the image project can evidence is `image-owned`; everything else is a handoff
that names who must act. The criteria here are the image's half of those
handoffs, and each one cites the SRG rule and 800-53 control it serves, derived
through the [crosswalk](../crosswalk/README.md) rather than asserted.
