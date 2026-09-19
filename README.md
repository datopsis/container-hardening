# container-hardening

The criteria, implementation, and controls used in every Datopsis container
build, and the expectations placed on the platform those containers run on.

One standard, applied across repositories, tailored per application rather than
reinvented per application.

> **Status: scaffold.** The requirement catalogues render and the sources are
> pinned. The standard itself and the control mapping are outstanding — see
> [the roadmap](docs/ROADMAP.md). Nothing here is an authorization package, and
> nothing here claims STIG certification.

## What is here

| | |
| --- | --- |
| [Requirement catalogues](docs/srg/README.md) | DISA packages rendered to Markdown, one file per rule. 391 rules today. |
| [Source register](artifacts/sources.json) | Nine sources pinned by SHA-256, with role, rendering state, and redistribution terms. |
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

## Related

- [`datopsis/nginx-ubi`](https://github.com/datopsis/nginx-ubi) — the first
  adopting repository, and the source of the control model carried here.
