# Reference web server

A generic, hardened HTTP server image, built to [the standard](../../docs/standard/README.md)
and verified against [its criteria](../../docs/standard/criteria.md). It is the
worked example of every file and check an image repository needs, and the
starting point for a new image: copy this directory, change what the image
runs, and keep the checks.

It serves static content with nginx from Red Hat UBI 9 Micro. It has no
management interface, no user accounts, and hosts no application runtime.

## What is here

| File | What it is | Criteria |
| --- | --- | --- |
| [`lock.json`](lock.json) | Every input: both bases by manifest-list digest, nine RPMs by SHA-256 and signing key, and the dependencies deliberately left out, with reasons | IMG-01, IMG-02, IMG-07 |
| [`scripts/acquire.py`](scripts/acquire.py) | The only step with network access: retrieves and verifies every input, or with `--refresh` rewrites the lock for review | IMG-02 to IMG-04 |
| [`Containerfile`](Containerfile) | Assembly from the verified bundle, with networking disabled | IMG-01 to IMG-23 |
| [`scripts/build.py`](scripts/build.py) | The only supported way to build it | IMG-03, IMG-23 |
| [`rootfs/`](rootfs/) | The configuration and content the image ships | IMG-10, IMG-14, IMG-15, IMG-19 |
| [`behaviour.json`](behaviour.json) | What it does when it runs: processes, listeners, writable paths, outbound destinations, mounts | IMG-30 |
| [`features.json`](features.json) | The nginx build flags and dynamic modules it declares | IMG-07 |
| [`hardening-profile.json`](hardening-profile.json) | Its applicability determinations and deviations | IMG-26 |
| [`tests/build_checks.py`](tests/build_checks.py) | Shows a tampered or missing input stops the build, and reads the build definition | IMG-01 to IMG-05 |
| [`tests/smoke.py`](tests/smoke.py) | Reads every runtime property back from the running image, and records the evidence | IMG-06 to IMG-20, IMG-27, IMG-30, IMG-32 |

## Building and verifying it

```sh
python scripts/acquire.py /tmp/bundle          # retrieve and verify every input
python tests/build_checks.py /tmp/bundle       # a defective input must stop the build
python scripts/build.py /tmp/bundle            # assemble with networking disabled
python tests/smoke.py localhost/reference-web-server:dev
```

It needs Podman and Python 3. CI does the same on every change to this
directory, in [`reference-image.yml`](../../.github/workflows/reference-image.yml),
and keeps the evidence files each step writes.

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

Building this image to the criteria found three things a less strict build
would have shipped:

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
expiry. The release criteria (bill of materials, signature and provenance,
immutable tags, vulnerability and malware gates) and the Kubernetes and
OpenShift admission tests are the next increments on the roadmap.
