---
status: accepted
date: 2026-09-18
decision-makers: Joey
---

# Secrets reach an image only as read-only files

## Context and Problem Statement

Every service a Datopsis image packages needs at least one secret: a database
password, an S3 identity, an encryption key, a TLS private key. Three
patterns are common in container images, and each is found in practice:

* **Files only.** The image reads secrets only from `_FILE` paths, rejects a
  symlink, an empty file, or a permissive mode, and tests that no secret
  appears in any process's arguments, in PID 1's environment, or in the logs.
* **Environment only.** The image takes its secrets only from environment
  variables and has no file interface.
* **Either.** The image accepts both. Its examples ship a default password such
  as `change-me` in an environment variable, and its entrypoint passes the
  password to a client on the command line.
* The DISA Container Hardening Process Guide says secrets belong in a secret
  store, and elsewhere suggests base64 to "obfuscate and encrypt" them. Base64
  is an encoding.

A standard applied across repositories has to pick one rule.

## Decision Drivers

* A secret should have exactly one reader, and that reader should not be able
  to alter it
* Environment variables are visible in `/proc/<pid>/environ`, inherited by
  every child process, and printed by diagnostics and orchestrator tooling
* Command-line arguments are visible to every process on the host that can
  list processes
* Upstream images and documentation overwhelmingly use environment variables,
  so any other rule costs compatibility
* The Container Platform SRG expects secrets to come from a protected keystore
  ([V-233028](../srg/container-platform-srg/rules/V-233028.md))

## Considered Options

* **Environment variables** — the upstream convention
* **Either, file preferred** — accept both, document the file form as better
* **Read-only files only** — accept a secret only from a file on a read-only
  mount, with a `_FILE` form wherever upstream uses an environment variable

## Decision Outcome

Chosen option: **read-only files only.**

Environment variables were rejected because of where they end up. The risk is
not an attacker reading the environment of a compromised process, which they
can do whatever the mechanism. It is the ordinary, non-malicious routes by
which environments are copied, logged, and displayed. An orchestrator's
describe command, a crash dump, a support bundle, and a child process that
logs its environment are each a disclosure nobody chose.

*Either, file preferred* was the real alternative. It keeps upstream
compatibility, and it is the most common pattern. It lost
because a preference is not testable. An image that accepts both will be
deployed with the environment variable, because that is what the upstream
documentation shows, and the image's own tests cannot tell whether a given
deployment chose well. Refusing the environment variable is the only form of
the rule the image itself can enforce.

The file must be on a read-only mount, not writable by the runtime identity,
and not world-readable. Otherwise the process that reads the secret could also
replace it, or anything else on the host could read it. See the amendment
below on group read.

### Consequences

* Good: a secret has one reader and cannot be rewritten by it, and a test can
  prove no secret reached arguments, environment, or logs
* Good: one rule across every image, so a platform delivers secrets the same
  way to all of them
* Bad: breaks compatibility with upstream documentation and with deployments
  that set the upstream environment variable. An image that takes secrets
  from the environment must change, and so must its users
* Bad: some upstream programs accept a secret only from the environment. There
  the image's entrypoint must read the file and pass the value on. That
  reintroduces the environment for one process, and it must be recorded as a
  limitation rather than hidden

### Enforcement

[IMG-16](../standard/criteria.md#img-16-secrets-only-as-read-only-files) states
the test each image must carry. Nothing in this repository runs it: it is
enforced in each adopting image repository, and adoption is tracked under
Package 5 of the roadmap. Until an image carries the test, this decision is
unenforced for that image.

## Amendment, 2026-09-19

This record first said a secret file must be neither group- nor
world-readable. That contradicts
[IMG-12](../standard/criteria.md#img-12-runs-under-an-arbitrary-uid): an image
running under an arbitrary UID in group 0 cannot own a mounted secret, so it
reads one through its group, and Kubernetes mounts secrets group-readable with
an `fsGroup` for exactly that reason. Building the reference image found it:
its TLS key, mounted owner-only, was unreadable to the server.

The rule is now: not writable by the runtime identity, not world-readable, and
readable by no group the runtime process does not belong to. Under Podman that
group is the process's primary group 0; under Kubernetes it is the pod's
`fsGroup`, which the platform adds to the process's supplementary groups. Both
are shown in [IMG-16](../standard/criteria.md#group-read-by-example). The
decision itself, files and never the environment, is unchanged.
