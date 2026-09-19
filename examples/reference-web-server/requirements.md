# Reference web server requirements

What this image commits to, one requirement per criterion of the
[standard](../../docs/standard/criteria.md), each with the checks that verify it.
Its [component definition](oscal/component-definition.json) cites these
identifiers as the verification pointer for every control it claims.

### RWS-001

Both bases, the UBI 9 builder and the UBI 9 Micro runtime, are named by manifest-list digest in lock.json, and the Containerfile uses those digests.

- Criterion: IMG-01
- Verified by `tests/build_checks.py`: every base is referenced by its locked manifest-list digest

### RWS-002

Every RPM and signing key is fetched from the location lock.json records and verified by size and SHA-256 as it arrives, and the bundle holds exactly the lock. During assembly each is verified again: the Red Hat release key by SHA-256 and full fingerprint, each RPM by SHA-256, signature, signer, and the source package it was built from.

- Criterion: IMG-02
- Verified by `tests/build_checks.py`: a tampered input stops the build
- Verified by `tests/build_checks.py`: an input the lock does not name stops the build
- Verified by `tests/build_checks.py`: a signing key other than the pinned one stops the build

### RWS-003

Retrieval fetches only what lock.json names, from where it says, over HTTPS from the hosts it allows, and resolves nothing; each base pulled is the architecture being built. Assembly runs with networking disabled and pulls refused, from that bundle; a missing input stops it.

- Criterion: IMG-03
- Verified by `tests/build_checks.py`: the build definition runs no retrieval tool or package manager
- Verified by `tests/build_checks.py`: retrieval runs no package manager or resolver
- Verified by `tests/build_checks.py`: each base pulled is the architecture being built
- Verified by `tests/build_checks.py`: a missing input stops the build rather than being fetched

### RWS-004

Only a reviewed pull request changes lock.json; the drift job reports and holds read permission only.

- Criterion: IMG-04
- Verified by `tests/build_checks.py`: drift automation holds only read permission and changes nothing

### RWS-005

No credential is a build argument, environment variable, layer, or label, and nothing of how the inputs were acquired, such as a repository host, a signing key, or the bundle, reaches the image's history, labels, bill of materials, or provenance.

- Criterion: IMG-05
- Verified by `tests/build_checks.py`: no credential-shaped build argument or environment variable
- Verified by `tests/gates.py image`: no credential or acquisition material in history, labels, or the bill of materials
- Verified by `tests/release_checks.py`: no credential or acquisition material in the release's provenance

### RWS-006

The image contains no dnf, microdnf, yum, or rpm, no repository configuration or keys, and none of the base's package-manager residue.

- Criterion: IMG-06
- Verified by `tests/smoke.py`: no package manager or repository configuration
- Verified by `tests/smoke.py`: no repository files or signing keys

### RWS-007

The image contains nginx and the libraries it links, no compiler or retrieval tool, and exactly the nginx features features.json declares.

- Criterion: IMG-07
- Verified by `tests/smoke.py`: no retrieval tool or compiler
- Verified by `tests/smoke.py`: no dynamic module beyond those declared
- Verified by `tests/smoke.py`: built features equal the declaration

### RWS-008

The image carries a mode 0444 inventory of its packages, written from what was installed and covering the lock.

- Criterion: IMG-08
- Verified by `tests/smoke.py`: inventory is mode 0444
- Verified by `tests/smoke.py`: inventory covers every locked package

### RWS-009

No file in the image is setuid or setgid, and nothing outside /tmp is world-writable.

- Criterion: IMG-09
- Verified by `tests/smoke.py`: no setuid or setgid file
- Verified by `tests/smoke.py`: nothing world-writable outside /tmp

### RWS-010

nginx and its configuration are owned by root and not writable by the runtime user.

- Criterion: IMG-10
- Verified by `tests/smoke.py`: software and configuration root-owned, not group- or world-writable
- Verified by `tests/smoke.py`: the runtime user cannot write configuration

### RWS-011

The image runs as UID 1001 in group 0, and no process ever runs as UID 0.

- Criterion: IMG-11
- Verified by `tests/smoke.py`: configured user is numeric, non-zero, with group 0
- Verified by `tests/smoke.py`: no su or sudo
- Verified by `tests/smoke.py`: no process runs as UID 0

### RWS-012

The image serves under any UID in group 0.

- Criterion: IMG-12
- Verified by `tests/smoke.py`: serves under an arbitrary UID in group 0

### RWS-013

The image serves with every capability dropped, no new privileges, and the default seccomp profile, each read back from /proc.

- Criterion: IMG-13
- Verified by `tests/smoke.py`: every process has an empty effective capability set
- Verified by `tests/smoke.py`: every process has no_new_privs
- Verified by `tests/smoke.py`: every process runs under a seccomp filter

### RWS-014

nginx listens only on 8080, and on 8443 when TLS is mounted.

- Criterion: IMG-14
- Verified by `tests/smoke.py`: every exposed port is 1024 or above
- Verified by `tests/smoke.py`: every listening socket is 1024 or above

### RWS-015

The image serves on a read-only root with /tmp as its one writable mount, and exits naming the path when /tmp is missing.

- Criterion: IMG-15
- Verified by `tests/smoke.py`: serves under a read-only root with only the declared tmpfs
- Verified by `tests/smoke.py`: a write to the root filesystem fails
- Verified by `tests/smoke.py`: without the declared tmpfs it exits non-zero naming the path

### RWS-016

TLS keys are read only from a read-only mount and never reach arguments, environment, or logs. Refusing a world-readable key file is deviation DEV-011.

- Criterion: IMG-16
- Verified by `tests/smoke.py`: serves TLS from read-only mounted key material
- Verified by `tests/smoke.py`: the key is not writable by the runtime identity
- Verified by `tests/smoke.py`: no key material in arguments, environment, or logs

### RWS-017

The image adds no trust anchor; trust material is mounted read-only.

- Criterion: IMG-17
- Verified by `tests/smoke.py`: the image adds no trust anchors

### RWS-018

Invalid configuration or a missing mount stops nginx with a message naming the cause.

- Criterion: IMG-18
- Verified by `tests/smoke.py`: invalid configuration exits non-zero naming the file and line

### RWS-019

nginx logs every request to standard output and its errors to standard error, and writes no log file.

- Criterion: IMG-19
- Verified by `tests/smoke.py`: no log file in the image; the error log links to stderr
- Verified by `tests/smoke.py`: requests are logged to standard output

### RWS-020

The image declares an exec-form healthcheck and SIGQUIT as its stop signal, and stops cleanly within ten seconds.

- Criterion: IMG-20
- Verified by `tests/smoke.py`: HEALTHCHECK is declared in exec form
- Verified by `tests/smoke.py`: STOPSIGNAL is declared
- Verified by `tests/smoke.py`: stops cleanly within the timeout

### RWS-021

Each build produces an SPDX bill of materials covering every locked package, attested to the released digest.

- Criterion: IMG-21
- Verified by `tests/gates.py image`: a bill of materials is generated from the image and covers every locked package
- Verified by `release job`: the bill of materials is attested to the released digest and retrievable by it
- Verified by `tests/release_checks.py`: the latest release's bill of materials is attested and retrievable by digest

### RWS-022

Each released digest is signed keylessly by the release workflow and carries SLSA build provenance.

- Criterion: IMG-22
- Verified by `release job`: the released digest's keyless signature and SLSA provenance verify against the release identity
- Verified by `tests/release_checks.py`: the latest release's keyless signature and SLSA provenance verify against the release workflow

### RWS-023

The image is labelled with its source, revision, version, creation time, base, and lock digest.

- Criterion: IMG-23
- Verified by `tests/smoke.py`: identifying labels are present
- Verified by `tests/smoke.py`: revision label equals the commit

### RWS-024

Each version tag is published once and never moved; there is no latest tag.

- Criterion: IMG-24
- Verified by `release job`: the version tag did not exist before the release, and no latest tag is pushed
- Verified by `tests/release_checks.py`: the registry carries version tags only, and no latest

### RWS-025

No image is released with a fixed High or Critical vulnerability found by Trivy or Grype, and every finding is recorded.

- Criterion: IMG-25
- Verified by `tests/gates.py image`: no fixed High or Critical vulnerability (Trivy, every finding recorded)
- Verified by `tests/gates.py image`: no fixed High or Critical vulnerability (Grype, from the bill of materials)

### RWS-026

Every exception is a deviation in hardening-profile.json, and CI fails on an expired one.

- Criterion: IMG-26
- Verified by `scripts/check-profile.py --report`: every exception is a recorded deviation, none expired or over its limit

### RWS-027

The image contains no SSH, telnet, or other remote administration daemon.

- Criterion: IMG-27
- Verified by `tests/smoke.py`: no remote administration daemon

### RWS-028

The image and its inputs are scanned for malware with signatures refreshed in the same run.

- Criterion: IMG-28
- Verified by `tests/gates.py image`: no malware in the image or its inputs, with signatures refreshed this run

### RWS-029

No image is built on a base more than 30 days behind its publisher.

- Criterion: IMG-29
- Verified by `scripts/drift.py --enforce`: no base is more than 30 days behind its publisher

### RWS-030

The image's processes, listeners, writable paths, and outbound destinations match behaviour.json.

- Criterion: IMG-30
- Verified by `tests/smoke.py`: running processes are the declared ones
- Verified by `tests/smoke.py`: listening sockets are declared
- Verified by `tests/smoke.py`: with TLS mounted, listening sockets are still declared

### RWS-031

The image is admitted unmodified under the Restricted Pod Security Standard and the restricted-v2 SCC. Not yet shown: deviation DEV-008.

- Criterion: IMG-31

### RWS-032

The image serves in a user namespace, where its UID 0 is not the host's.

- Criterion: IMG-32
- Verified by `tests/smoke.py`: container UID 0 is not host UID 0
- Verified by `tests/smoke.py`: serves in a user namespace

### RWS-033

Releases are cut only from reviewed commits on a protected default branch. Branch protection is deviation DEV-009.

- Criterion: IMG-33

### RWS-034

The source is scanned for secrets, and for dependency and build-definition findings, before every build.

- Criterion: IMG-34
- Verified by `tests/gates.py source`: no committed secret in the image's source
- Verified by `tests/gates.py source`: no High or Critical dependency, secret, or build-definition finding

### RWS-035

The workflows that build and release this image pin every action to a full commit, default to read-only permissions, grant writes only to the jobs that publish, persist no checkout credentials, release only from a version tag on main, and are audited in CI.

- Criterion: IMG-35
- Verified by `tests/pipeline_checks.py`: every action is pinned to a full commit, or is this repository's own
- Verified by `tests/pipeline_checks.py`: every workflow's default permissions are read-only
- Verified by `tests/pipeline_checks.py`: only the jobs that must write hold write permissions, and only those they need
- Verified by `tests/pipeline_checks.py`: no checkout persists its credentials
- Verified by `tests/pipeline_checks.py`: a release starts only from a version tag, on a commit on the default branch
- Verified by `tests/pipeline_checks.py`: CI audits every workflow for security findings
