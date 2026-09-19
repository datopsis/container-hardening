# container-hardening

The criteria, implementation, and controls used in every Datopsis container
build, and the expectations placed on the platform those containers run on.

One standard, applied across repositories, tailored per application rather than
reinvented per application.

> **Status: draft standard.** The requirement catalogues render, the sources
> are pinned, the standard is written, and the control baseline is derived.
> Adoption in the image repositories is outstanding — see
> [the roadmap](docs/ROADMAP.md). Nothing here is an authorization package, and
> nothing here claims STIG certification.

## What is here

| | |
| --- | --- |
| [**The standard**](docs/standard/README.md) | What a hardened Datopsis image is, and why. Start here. |
| [Reference architecture](docs/architecture/README.md) | Where the standard sits across ten control domains, from source to response, with the sources behind it. |
| [Image criteria](docs/standard/criteria.md) | The standard as 34 testable properties, each with its implementation, verification, expected result, and evidence. |
| [Platform expectations](docs/standard/platform.md) | What the platform and host must impose for the image's properties to count. |
| [NIST SP 800-190](docs/standard/nist-800-190.md) | Every countermeasure of the Application Container Security Guide, and what implements it. |
| [Control baseline](docs/controls/README.md) | Every High-baseline control: who satisfies it, derived from the standard. |
| [Control model](docs/CONTROL-MODEL.md) | How an image states its controls, and the checker that holds it to them. |
| [Reference image](examples/reference-web-server/README.md) | A generic web server built and verified to the standard: the template for new images. |
| [Tailoring](docs/TAILORING.md) | How an image records which sources apply to it and where it deviates, with an expiry. |
| [Requirement catalogues](docs/srg/README.md) | DISA packages rendered to Markdown, one file per rule. 630 rules across four SRGs. |
| [SRG to 800-53 crosswalk](docs/crosswalk/README.md) | Every rendered rule joined to NIST SP 800-53 Rev 5 through its CCIs. Derived, not hand-authored. |
| [Adoption](docs/adoption/README.md) | How image repositories take the standard up, and the planned conformance badge. |
| [Source register](artifacts/sources.json) | Thirty sources recorded, twenty-eight pinned by SHA-256, with role, rendering state, and redistribution terms. |
| [Sources guide](docs/SOURCES.md) | How to obtain a package and regenerate the catalogue. |
| [Roadmap](docs/ROADMAP.md) | What this repository is, and what remains. |
| [Decisions](docs/adr/README.md) | Decisions that are expensive to reverse. |

## The three layers, kept apart

Conflating these is the failure this repository exists to prevent.

| Layer | Governed by | Who satisfies it |
| --- | --- | --- |
| **Image** | DISA GPOS SRG, plus function-specific SRGs | The image build |
| **Platform** | DISA Container Platform SRG | The orchestrator and its operators |
| **Host** | DISA RHEL 9 STIG | The host baseline |

Per DoD guidance the **GPOS SRG assesses image-level controls in the absence of
a container-specific STIG**, which is the situation for every image covered
here. The Container Platform SRG is not a substitute for it: that one governs
the platform, and an image cannot satisfy it.

## Source packages are not committed

DISA packages are US Government works whose distribution terms live inside the
package, and they are large binary-heavy trees. The repository commits the
**generated Markdown** and pins the **identity** of what generated it.

```sh
# Extract a DISA package into the repository root or sources/, then:
python scripts/build-srg-markdown.py            # regenerate docs/srg/
python scripts/build-srg-markdown.py --check    # fail if committed output is stale
python scripts/build-cci-crosswalk.py           # regenerate the 800-53 crosswalk
python scripts/build-control-baseline.py        # regenerate the control baseline
```

One file per rule is deliberate. When DISA publishes a new release the diff
shows exactly which rules changed, instead of one unreadable blob. That diff is
the review artifact.

## Two things worth knowing before you script against DISA

**A STIG ID is not a unique key.** GPOS V3R3 issues
`SRG-OS-000132-GPOS-00067` as two distinct rules, `V-203655` and `V-278973`.
Pages are filed by Group ID, and the generator refuses to overwrite rather than
silently dropping a rule.

**A `200` does not mean a release is current.** DISA serves superseded releases
alongside current ones — `U_GPOS_V2R7_SRG.zip` still resolves while V3R3 is
current. Only probing adjacent releases establishes currency.
