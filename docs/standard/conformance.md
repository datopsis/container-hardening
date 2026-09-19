# Conformance snapshot, 2026-09-18

Where each Datopsis image repository stood against [the criteria](criteria.md)
when they were first written. This is the starting point for adoption
(Package 5 of the [roadmap](../ROADMAP.md)), not a live status.

**It was established by reading each repository, not by running its tests.** A
*met* here means the repository contains a check that would establish the
property, not that the check passed. It will go stale, and it is not updated in
place: adoption is recorded in each image repository, against a criterion
identifier.

| | Meaning |
| --- | --- |
| Met | The property holds and a check in the repository establishes it |
| Partial | The property holds, or mostly holds, but nothing verifies it as the criterion requires |
| No | The property does not hold |
| ? | Not assessed |

## By criterion

| Criterion | nginx-ubi | postgresql-ubi | clickhouse-ubi | seaweedfs-ubi | lakekeeper-ubi |
| --- | --- | --- | --- | --- | --- |
| [IMG-01](criteria.md#img-01-base-image-pinned-by-digest) Base pinned | Met | Met | Partial | Met | Met |
| [IMG-02](criteria.md#img-02-every-build-input-pinned-and-verified) Inputs verified | Met | Met | No | Partial | Partial |
| [IMG-03](criteria.md#img-03-hermetic-assembly) Hermetic | Met | Met | No | Partial | Partial |
| [IMG-06](criteria.md#img-06-no-package-manager) No package manager | Met | Met | Partial | No | Partial |
| [IMG-09](criteria.md#img-09-no-privilege-raising-files) No setuid | No | Met | No | No | No |
| [IMG-10](criteria.md#img-10-software-and-configuration-not-writable-by-the-service) Not writable | Met | ? | No | ? | Met |
| [IMG-11](criteria.md#img-11-non-root-with-no-privilege-transition) Non-root | Met | Met | Partial | Partial | Met |
| [IMG-12](criteria.md#img-12-runs-under-an-arbitrary-uid) Arbitrary UID | Met | Met | Met | ? | Met |
| [IMG-13](criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges) No capabilities | Met | Met | Partial | Partial | Met |
| [IMG-14](criteria.md#img-14-unprivileged-ports) Unprivileged ports | Partial | Partial | Partial | Partial | Partial |
| [IMG-15](criteria.md#img-15-read-only-root-filesystem) Read-only root | Met | Met | Partial | Met | Met |
| [IMG-16](criteria.md#img-16-secrets-only-as-read-only-files) Secrets as files | Met | Met | No | Partial | No |
| [IMG-20](criteria.md#img-20-lifecycle-is-declared) Lifecycle | Met | Met | Partial | No | Met |
| [IMG-22](criteria.md#img-22-signed-with-provenance) Signed | Partial | Met | Met | No | No |
| [IMG-23](criteria.md#img-23-identifying-labels) Labels | Partial | Met | Partial | Partial | Partial |
| [IMG-25](criteria.md#img-25-vulnerability-gate-and-remediation) Vulnerabilities | Partial | Met | Partial | No | Partial |

Criteria not in the table were not assessed. IMG-27 to IMG-30 were added from
NIST SP 800-190 after this snapshot was taken and have not been assessed. None of the five images scans for malware (IMG-28).
seaweedfs-ubi already checks the sockets it opens, which is the start of
IMG-30.

## What the table shows

**No image meets IMG-14.** Every image listens above 1024, but none asserts it.
Several rely on running with `--cap-drop ALL`, which proves nothing under
Docker. seaweedfs-ubi comes closest: it already reads the sockets it opened,
and needs only to assert the port numbers.

**postgresql-ubi is the reference for most of the rest.** It is the only image
that strips setuid and setgid bits, removes repository signing keys, rejects
malformed secret files, carries complete labels, and states a remediation
timeline. The criteria's timelines are its timelines.

**nginx-ubi is the reference for the build.** Its lock, hermetic assembly, and
negative build tests are the model for IMG-01 to IMG-04. Its release workflow
exists but, by its own status document, has never run, which is why IMG-22 is
partial.

**clickhouse-ubi does not yet meet the build criteria.** It runs `dnf` and
`curl` during assembly, verifies its upstream archive only against a checksum
fetched from the same origin, installs unpinned packages, and restores a CI
layer cache. It also accepts its password from the environment, ships
`CLICKHOUSE_PASSWORD: change-me` in its example Compose file, and passes the
password on a command line. Its temporary mount omits `noexec,nosuid,nodev`.

**seaweedfs-ubi and lakekeeper-ubi have no release workflow**, so neither
publishes a signature, provenance, or attested SBOM. seaweedfs-ubi records
vulnerabilities as inventory without gating on them, and declares no
healthcheck or stop signal. lakekeeper-ubi takes its secrets only from the
environment.

**Verification that the restrictions applied** (IMG-11, IMG-13) is missing in
clickhouse-ubi and seaweedfs-ubi. Both pass `--cap-drop ALL` and
`no-new-privileges` to the runtime, but neither reads back `CapEff` and
`NoNewPrivs` for every process.

## Inconsistencies the standard settles

The five repositories used different vocabulary for the same things. The
standard now fixes one:

- **Control origination.** Five different vocabularies were in use across the
  repositories and within nginx-ubi itself. The six values of the nginx-ubi
  control model are the ones Package 3 carries forward.
- **Secret delivery.** One rule, read-only files only
  ([ADR-0003](../adr/0003-secrets-reach-an-image-only-as-read-only-files.md)).
- **Temporary mounts.** Always `rw,noexec,nosuid,nodev`.
- **Digest pinning.** Two obligations, named separately: the image pins its base
  ([IMG-01](criteria.md#img-01-base-image-pinned-by-digest)); the deployment
  pins the image ([PLT-01](platform.md#plt-01-images-are-admitted-by-verified-digest)).
- **Capabilities and `no-new-privileges`.** The image *works under* them and
  tests that ([IMG-13](criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges));
  the platform *imposes* them ([PLT-02](platform.md#plt-02-least-privilege-is-imposed)).
  nginx-ubi stated this both ways in different documents.
- **SCAP.** Two images claim SCAP evidence in their agent guidance that their CI
  does not produce, and two others scan against different rule selections. This
  stays a [target](criteria.md#img-t3-compliance-scan) until one selection is
  agreed.
