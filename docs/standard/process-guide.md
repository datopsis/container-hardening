# The DISA Container Hardening Process Guide

DISA's **Container Hardening Process Guide, Version 1, Release 2** (24 August
2022, Distribution Statement A) is the closest thing DoD publishes to guidance
on hardening a container image. It is pinned in
[`artifacts/sources.json`](../../artifacts/sources.json) as
`dod-container-hardening-guide`. The file is published as
`Final_DevSecOps_Enterprise_Container_Hardening_Guide_1.2.pdf`, but the title
on its cover is the one above.

It is a process guide, not a rule catalogue, and most of it describes how to get
an image into **Iron Bank**, DoD's hardened container registry, through
**Repo One** and Platform One's pipeline. This page separates the parts that
are general practice from the parts that are Iron Bank process, and says where
this standard follows the guide, where it goes further, and where it
deliberately differs.

Section references are the guide's own; page numbers are its printed ones.

## What does not apply

A Datopsis image is not submitted to Iron Bank, so the guide's Iron Bank and
Platform One machinery does not apply as written:

- the Repo One and Iron Bank folder layouts and branching strategy
  (Appendix A; the second Appendix E)
- the approver roles, the Vulnerability Assessment Tracker, and the four
  approval outcomes (§2.5; §7.1)
- the mandated scanner products, Prisma or StackRox together with Anchore
  (Table 2-2)
- Keycloak, CAC, and ADFS authentication (§2.8; Table 2-3 item 1g)
- the FedRAMP+ IL6 and RMF documentation package (Appendix B)
- GPG signing by Iron Bank (Table 2-4; Figure 7-1)

Where a piece of that machinery has a general purpose, the standard keeps the
purpose and chooses its own mechanism, as below.

## Where the standard follows the guide

| Guide | Says | Standard |
| --- | --- | --- |
| §2.1 steps 6–7; §7.1 steps 1–2 | Declare every dependency in a download manifest, validate signatures and checksums, and build with no egress | [IMG-02](criteria.md#img-02-every-build-input-pinned-and-verified), [IMG-03](criteria.md#img-03-hermetic-assembly). The lock is the manifest. |
| Table 2-3 1e; Appendix B | Do not run as UID 0 | [IMG-11](criteria.md#img-11-non-root-with-no-privilege-transition) |
| Table 2-3 1j | Remove setuid and setgid permissions | [IMG-09](criteria.md#img-09-no-privilege-raising-files) |
| Table 2-3 1i; §2.1 step 5 | Remove anything not core to the container | [IMG-06](criteria.md#img-06-no-package-manager), [IMG-07](criteria.md#img-07-only-what-the-function-needs) |
| Table 2-3 1d | Logs to stdout | [IMG-19](criteria.md#img-19-logs-to-standard-streams-without-secrets) |
| Table 2-3 step 2 | Declare a `HEALTHCHECK` | [IMG-20](criteria.md#img-20-lifecycle-is-declared) |
| Table 2-3 1l | Beware injection through `ENV` and `ARG` in `RUN` | [IMG-05](criteria.md#img-05-no-secrets-in-the-build), and no network tool runs in the build at all |
| Table 2-3 1m | Secrets live in a secret store | [IMG-16](criteria.md#img-16-secrets-only-as-read-only-files), [PLT-06](platform.md#plt-06-secrets-are-delivered-as-read-only-files) |
| Table 2-4 steps 1, 3 | Sign the image and publish a SHA-256 checksum | [IMG-22](criteria.md#img-22-signed-with-provenance). The digest is the checksum. |
| p13 note | A changed Dockerfile goes through hardening again | Every change runs the full criteria in CI |
| §2.2; Appendix C | Containers inherit many controls from the platform and host | The [three layers](README.md#three-layers-and-why-they-stay-apart), made control-by-control through the [crosswalk](../crosswalk/README.md) |
| Appendix D §6.1 | Evaluate findings; remediate true positives; document false positives | [IMG-25](criteria.md#img-25-vulnerability-gate-and-remediation), [IMG-26](criteria.md#img-26-exceptions-expire) |
| §2.6 | Stop the build on a new CVE | [IMG-25](criteria.md#img-25-vulnerability-gate-and-remediation), for fixed Critical and High |

## Where the standard goes further

**Root is never acceptable.** The guide allows UID 0 "unless risk accepted and
documented" (Table 2-3 1e) and prohibits root "whenever possible"
(Appendix B). This standard has no such exception, and also forbids a root
phase at startup, which the guide does not address.

**Privilege is removed, not only avoided.** The guide says nothing about
capabilities, `no-new-privileges`, or a read-only root filesystem. The standard
requires the image to work under all three
([IMG-13](criteria.md#img-13-works-with-no-capabilities-and-no-new-privileges),
[IMG-15](criteria.md#img-15-read-only-root-filesystem)) and tests that they
applied.

**Ports are unprivileged, not merely unusual.** The guide recommends ports
other than 80 and 443 (Table 2-3 1a). The standard requires every listener at
or above 1024 and tests the sockets actually opened
([IMG-14](criteria.md#img-14-unprivileged-ports)).

**No package manager at all.** The guide asks for unnecessary packages to be
removed. The standard removes the means of adding any
([IMG-06](criteria.md#img-06-no-package-manager)).

**Inputs are pinned by digest.** The guide asks for inputs to be declared and
their checksums validated at download. It does not say they are pinned, or that
a refresh is reviewed. The standard does both
([IMG-01](criteria.md#img-01-base-image-pinned-by-digest),
[IMG-04](criteria.md#img-04-input-refresh-is-a-reviewed-change)).

**Remediation has deadlines.** The guide leaves remediation time "dependent upon
the organization directive" (§2.5). The standard sets 7, 14, and 30 days,
bounded by the GPOS SRG's 30-day requirement.

**Secrets are never environment variables.** The guide suggests base64 to
"obfuscate and encrypt" YAML secrets (Table 2-3 1f). Base64 is an encoding, not
encryption, and this standard does not adopt that advice. Secrets reach an
image only as read-only files
([ADR-0003](../adr/0003-secrets-reach-an-image-only-as-read-only-files.md)).

**Release evidence.** The guide asks for a signature and a checksum. The
standard also requires an SBOM, build provenance, identifying labels, and
immutable tags ([IMG-21](criteria.md#img-21-bill-of-materials) to
[IMG-24](criteria.md#img-24-immutable-tags)). The guide does not mention SBOMs.

## Where the standard deliberately differs

**The base image comes from Red Hat, not Iron Bank.** The guide ranks Iron Bank
as the only trusted source and lists Red Hat's registry among the "untrusted"
ones, usable with review (§1.2.7; §2.1 step 3). Datopsis images build on Red Hat
UBI 9 pulled from Red Hat, pinned by digest and verified. The guide also names
only UBI 7 and 8; it predates UBI 9 in practice. An image intended for Iron Bank
would need to rebase onto Iron Bank's hardened UBI.

**The image is assessed against the GPOS SRG, not an OS STIG.** The guide asks
for the base OS image to be "STIGed" and scanned with OpenSCAP (Appendix B;
Table 2-1 step 3). It does not mention the GPOS SRG or the Container Platform
SRG. This standard follows the DoD guidance, recorded in the source register, that
in the absence of a container-specific STIG, the GPOS SRG assesses image-level controls, and keeps
the RHEL 9 STIG for the host. An OpenSCAP scan of the image is a
[target](criteria.md#img-t3-compliance-scan), not yet a requirement.

**The mechanisms are our own.** Where the guide names a product (Prisma,
StackRox, Anchore, ClamAV, GPG, Jenkins), the standard names the property and
leaves the product to the image repository. Current images use Trivy and Grype
for scanning and keyless cosign for signing.

## What the guide asks for that the standard does not yet cover

- **Antivirus scanning of downloaded inputs** (§7.1 step 1f). Verifying inputs by
  digest and signature establishes they are the reviewed bytes; it does not
  establish those bytes are benign. Not yet adopted.
- **Scanning candidate base images before choosing one** (§2.1 step 4). Each
  base refresh is scanned in CI once it is proposed, which is later than the
  guide asks.
- **Static and dynamic analysis of application code before containerisation**
  (§1.1). Datopsis images package upstream software they do not write; that
  analysis belongs to the upstream project.
