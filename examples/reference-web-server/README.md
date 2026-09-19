# Reference web server

[![hardening amd64](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/datopsis/container-hardening/badges/reference-web-server/shields-amd64.json)](https://github.com/datopsis/container-hardening/actions/workflows/reference-image.yml?query=branch%3Amain)
[![hardening arm64](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/datopsis/container-hardening/badges/reference-web-server/shields-arm64.json)](https://github.com/datopsis/container-hardening/actions/workflows/reference-image.yml?query=branch%3Amain)
[![hardening generic](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/datopsis/container-hardening/badges/reference-web-server/shields-generic.json)](https://github.com/datopsis/container-hardening/actions/workflows/reference-image.yml?query=branch%3Amain)

A generic, hardened HTTP server image, built to [the standard](../../docs/standard/README.md)
and verified against [its criteria](../../docs/standard/criteria.md). It is the
worked example of every file and check an image repository needs, and the
starting point for a new image: copy this directory, change what the image
runs, and keep the checks.

It serves static content with nginx 1.26 from Red Hat UBI 9 Micro, built
natively for amd64 and arm64. It has no management interface, no user
accounts, and hosts no application runtime.

## What is here

| File | What it is | Criteria |
| --- | --- | --- |
| [`lock.json`](lock.json) | Every input: both bases by manifest-list digest, the nginx 1.26 module stream, eight RPMs for each architecture by location, SHA-256, signer, and source package, the Red Hat release key by location, SHA-256, and full fingerprint, and the dependencies deliberately left out, with reasons | IMG-01, IMG-02, IMG-07 |
| [`scripts/acquire.py`](scripts/acquire.py) | The only step with network access: fetches exactly what the lock names, from where it says, over HTTPS from named hosts, resolving nothing, and admits the bundle only when all of it verifies; or with `--refresh`, the one step that resolves, rewrites the lock for review | IMG-02 to IMG-04 |
| [`Containerfile`](Containerfile) | Assembly from the verified bundle, with networking disabled | IMG-01 to IMG-23 |
| [`scripts/build.py`](scripts/build.py) | The only supported way to build it | IMG-03, IMG-23 |
| [`rootfs/`](rootfs/) | The configuration and content the image ships | IMG-10, IMG-14, IMG-15, IMG-19 |
| [`behaviour.json`](behaviour.json) | What it does when it runs: processes, listeners, writable paths, outbound destinations, mounts | IMG-30 |
| [`features.json`](features.json) | The nginx build flags and dynamic modules it declares | IMG-07 |
| [`hardening-profile.json`](hardening-profile.json) | Its applicability determinations and deviations | IMG-26 |
| [`tests/build_checks.py`](tests/build_checks.py) | Shows a tampered, missing, or extra input, or another key, stops the build; reads the build definition and the retrieval; checks each base is the architecture built | IMG-01 to IMG-05 |
| [`tests/pipeline_checks.py`](tests/pipeline_checks.py) | Reads the workflows that build and release the image: pins, permissions, credentials, and the release trigger | IMG-35 |
| [`tools.json`](tools.json), [`scripts/install_tools.py`](scripts/install_tools.py) | The scanners, pinned by archive digest for each architecture and verified before they are unpacked | IMG-02 |
| [`tests/gates.py`](tests/gates.py) | Source scans before the build; bill of materials, a scan of history, labels, and the bill of materials for acquisition material, two vulnerability gates, and a malware scan after it | IMG-05, IMG-21, IMG-25, IMG-28, IMG-34 |
| [`scripts/drift.py`](scripts/drift.py) | How far the inputs are behind their publishers; fails CI once a base is more than 30 days behind | IMG-04, IMG-29 |
| [`decisions.json`](decisions.json) | Its decision, rationale, owner, and review for each control the baseline leaves to the image | the control model |
| [`requirements.md`](requirements.md) | What the image commits to, one requirement per criterion, each naming its checks | the verification pointer |
| [`scripts/component.py`](scripts/component.py), [`oscal/component-definition.json`](oscal/component-definition.json) | Its OSCAL component definition: every baseline control, and its own decisions for the ones the baseline leaves open | the control model |
| [`tests/smoke.py`](tests/smoke.py) | Reads every runtime property back from the running image, and records the evidence | IMG-06 to IMG-20, IMG-27, IMG-30, IMG-32 |
| [`scripts/publish.py`](scripts/publish.py) | Pushes each tested image by digest, the index naming exactly those digests, and then the version tag, without rebuilding or re-encoding | IMG-22, IMG-24 |
| [`tests/release_checks.py`](tests/release_checks.py) | Verifies a published release as anyone pulling it would: the index, and each architecture's image | IMG-21, IMG-22, IMG-24 |
| [`tests/evidence.py`](tests/evidence.py) | Writes each check's results with the header the scorer requires: commit, run, architecture, and image | [Evidence](../../docs/EVIDENCE.md) |

## Building and verifying it

```sh
python scripts/acquire.py /tmp/bundle          # retrieve and verify every input
python tests/build_checks.py /tmp/bundle       # a defective input must stop the build
python scripts/build.py /tmp/bundle            # assemble with networking disabled
python tests/smoke.py localhost/reference-web-server:dev
python scripts/install_tools.py /tmp/tools     # pinned scanners, verified
python tests/gates.py source --bin /tmp/tools
python tests/gates.py image localhost/reference-web-server:dev --bundle /tmp/bundle --bin /tmp/tools
python scripts/drift.py --enforce
```

The gates need Linux, because the scanners are pinned as Linux binaries.

It needs Podman and Python 3. CI does the same on every change to this
directory, in [`reference-image.yml`](../../.github/workflows/reference-image.yml),
on a native runner for each architecture, keeps each architecture's evidence
separately, and passes it to the
[conformance workflow](../../.github/workflows/conformance.yml), which judges
this image exactly as it judges any other: `hardening amd64 32/35`,
`hardening arm64 32/35`. On main, that run publishes the badges above to this
repository's `badges` branch, exactly as an adopting image publishes its own;
see [Show the badges](../../docs/ADOPTING.md#8-show-the-badges).

## What it is not a template for

It is one process, one role, and one container, built from RPMs. Copy it for
that shape. It does not show:

- **An image with more than one role or topology**, such as a server and its
  workers, or a standalone and a clustered deployment. Such an image needs
  per-role evidence, and a single container's tests cannot show how its parts
  secure the traffic between them.
- **Inputs that are not RPMs**, such as an upstream binary or an upstream image.
  How those are verified is not how an RPM's signature is.
- **A release in any other registry**, or of any other architecture.

Its release path does show the pattern for more than one architecture, below.

## Running it

```sh
podman run --read-only --read-only-tmpfs=false \
    --tmpfs /tmp:rw,noexec,nosuid,nodev,size=16m \
    --cap-drop ALL --security-opt no-new-privileges \
    -p 8080:8080 reference-web-server
```

The tmpfs on `/tmp` is the one writable path, and it is required: without it,
nginx exits non-zero naming the path it could not create. Podman adds its own
tmpfs mounts under `--read-only` unless given `--read-only-tmpfs=false`, which
would hide a missing mount; the smoke suite always passes it.

To serve TLS on 8443, mount a server block into `/etc/nginx/conf.d/`, and the
certificate and key into `/etc/nginx/tls/`, all read-only. The key must be
readable by a group the server belongs to and by nobody else: owned `root:0`,
mode `0640`, under Podman, as the smoke suite mounts it, or `defaultMode: 0440`
with the pod's `fsGroup` under Kubernetes. Both are shown in
[group read, by example](../../docs/standard/criteria.md#group-read-by-example).
The image carries no trust anchors of its own; mount any the service needs.

The healthcheck, `nginx -t`, proves the configuration parses. It does not prove
the server answers; a platform's readiness probe should request a page.

## What the build found

Building this image to the criteria found four things a less strict build
would have shipped:

- **The default nginx carries a Critical vulnerability.** RHEL 9's default
  nginx stream, 1.20, is affected by CVE-2026-42945 (Critical) and eight High
  CVEs that Red Hat fixes only in the 1.24 and 1.26 module streams. Both
  vulnerability gates stopped the build; the image now enables the 1.26
  stream, recorded in the lock.

- **The base carries build residue.** UBI Micro contains a subscription-manager
  repository file, a package-manager history database, and a package-manager
  log. IMG-06 found the repository file; the build now removes all three.
- **A checkout's file modes leak into the image.** Copied from a Windows
  checkout, the configuration overlay arrived mode `0777`, and made `/etc` and
  `/usr` world-writable. IMG-09's check stopped the build; the overlay's modes
  are now set during assembly.
- **`--read-only` is not what it appears under Podman.** Podman mounts tmpfs on
  `/tmp`, `/var/tmp`, and `/run` by default, so a missing declared mount went
  unnoticed until the negative test hung. Every restricted run now passes
  `--read-only-tmpfs=false`.

## What it does not yet show

The criteria this image does not yet evidence are recorded as
[deviations](../../docs/TAILORING.md#deviations) in its profile, each with an
expiry: admission under Kubernetes and OpenShift, branch protection on this
repository, and refusing a world-readable key file.

## Releases

### Versions

A version is one tag on one index. The index names an image for each
architecture, and a client pulls the one for its own; there are no
per-architecture tags. To pin one architecture's image, pin its digest, which
the index lists. A version is published once and never replaced, and there is
no `latest`. The minor version rose to 0.2.0 when a release became an index
rather than a single amd64 image.

Released images are published as `ghcr.io/datopsis/reference-web-server`,
under version tags only, and only when the conformance workflow finds the
verified images release eligible. From 0.2.0, a version is an index of the
amd64 and arm64 images, released without rebuilding either:

1. Each architecture's verified image is pushed untagged, by the digest of its
   own manifest, pulled back, checked to be the image conformance judged, and
   tested again at that digest.
2. An index naming exactly those digests is pushed, untagged, by its own digest.
3. The index and each image are signed keylessly, each image's bill of
   materials is attested to it, and the index's SLSA provenance is attested.
4. Only then is the version tag added to the index's digest. A version that
   already exists is refused.
5. A fresh runner with no registry credentials verifies the result.

To verify one:

```sh
cosign verify ghcr.io/datopsis/reference-web-server:0.2.0 \
    --certificate-identity-regexp '^https://github.com/datopsis/container-hardening/.github/workflows/reference-image.yml@refs/tags/reference-web-server/v' \
    --certificate-oidc-issuer https://token.actions.githubusercontent.com
gh attestation verify oci://ghcr.io/datopsis/reference-web-server:0.2.0 --repo datopsis/container-hardening
```

For an index, verifying the tag verifies the index's own signature. Each
architecture's image is signed too; verify it the same way at the digest the
index names for it, which `skopeo inspect --raw` shows, and its bill of
materials with `cosign verify-attestation --type spdxjson` at that digest. CI
re-verifies the latest release this way on every run, with
[`tests/release_checks.py`](tests/release_checks.py). Versions 0.1.0 and 0.1.1
are amd64 images, not indexes; 0.1.0 has no provenance.
