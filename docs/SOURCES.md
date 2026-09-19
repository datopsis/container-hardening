# Requirement sources

Every catalogue and guidance document this standard maps against is pinned by
SHA-256 in [`artifacts/sources.json`](../artifacts/sources.json) before any
mapping is made against it. A control mapping is meaningful only against a
known revision.

## Why the packages are not committed

DISA packages are US Government works whose redistribution terms are stated
inside the package itself, and they are large binary-heavy trees — logos,
stylesheets, release memos, and revision-history PDFs alongside the one file
that matters.

The repository commits the **generated Markdown** and pins the **identity** of
what generated it. `.gitignore` excludes `U_*_SRG/`, `U_*_STIG/`, `sources/`,
and `*.zip`.

CIS benchmarks are a stronger case: their terms forbid reproduction, so they
can be cited by identifier but must never be rendered here at all.

## Obtaining a package

DISA publishes at `https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/`,
with filenames of the form `U_<Name>_V<n>R<n>_SRG.zip`. The URL recorded for
each source in the register is the exact one it was retrieved from.

The download index at `https://public.cyber.mil/stigs/downloads/` **cannot be
scraped.** It is a JavaScript-rendered portal whose HTML contains no download
links, so a browser is required to browse; direct URLs work fine once known.

Two traps, both learned the hard way:

**Filenames use DISA's own abbreviation, not the expanded title.** The GPOS SRG
is `U_GPOS_V3R3_SRG.zip`; `U_General_Purpose_Operating_System_V3R3_SRG.zip`
returns 404 at every release.

**A `200` does not mean a release is current.** DISA serves superseded releases
alongside current ones. `U_GPOS_V2R7_SRG.zip` still resolves while V3R3 is
current. Establish currency by probing adjacent releases, and probe the full
range — a sweep of V2R1 through V2R3 concluded the Container Platform SRG was
unretrievable when V2R4 was sitting there the whole time.

## Recording a source

Add an entry to the register with the fields every other entry carries:
publisher, title, release, retrieval date, URL, SHA-256, size, status, role,
license, and redistribution flag.

Where a package has been rendered, record the digest of the **XCCDF actually
rendered** alongside the package digest. The package digest identifies what was
downloaded; the XCCDF digest identifies what the committed Markdown derives
from, and that is the one a reviewer needs to reproduce the output.

### Roles

| Role | Meaning |
| --- | --- |
| `spine` | The control catalogue everything maps onto |
| `baseline` | The selection from the spine |
| `image-controls` | Assessed against the image itself |
| `platform-controls` | Assessed against the orchestrator, not the image |
| `host-controls` | Assessed against the host baseline |
| `process-guide` | Prose guidance; informs the standard, produces no rules |
| `conditional` | Applies only to images of a particular function |
| `cross-reference` | Cited by identifier only |
| `crosswalk` | Joins other sources; produces no rules of its own |
| `not-applicable` | Assessed and ruled out, with the basis recorded |

A `not-applicable` determination is a claim in its own right. It must record
why, or it is indistinguishable from having forgotten the source.

## Regenerating

```sh
python scripts/build-srg-markdown.py            # regenerate docs/srg/
python scripts/build-srg-markdown.py --check    # fail if committed output is stale
```

The generator discovers any `U_*/**/*Manual-xccdf.xml` under the repository
root or `sources/` **whose XCCDF digest is pinned in the register**. A package
that is present but not pinned is skipped, and a pinned one that does not
match is refused. Rendering a new catalogue therefore starts by recording its
XCCDF digest, which is the decision; the rendering follows from it. It removes pages whose rule no longer exists, so a release
upgrade produces a diff of exactly what changed.

It will refuse to run rather than overwrite a rule page if two rules share a
Group ID. Rules are filed by Group ID because the STIG ID is not unique — GPOS
V3R3 issues `SRG-OS-000132-GPOS-00067` as both `V-203655` and `V-278973`.

## The CCI crosswalk

Every SRG rule cites one or more CCIs, and the DISA CCI list maps each to NIST
SP 800-53 Rev 5. [`docs/crosswalk/`](crosswalk/README.md) is the join of the
two, resolved against the pinned OSCAL catalogue and High baseline; the
machine-readable form is `artifacts/crosswalk.json`. See
[ADR-0002](adr/0002-derive-800-53-cross-references-from-cci.md).

```sh
python scripts/verify-sources.py --fetch sources/   # retrieve every pinned input
python scripts/build-cci-crosswalk.py               # regenerate the crosswalk
python scripts/build-cci-crosswalk.py --check       # fail if committed output is stale
```

The CCI list is `U_CCI_List.zip` at an **unversioned URL**, which DISA replaces
in place. Its register entry records the package digest and, under `input`,
the digest of the `U_CCI_List.xml` the generator reads. The weekly verification
is the only thing that notices a replacement.

The generator refuses to run against an input that does not match its pin, a
CCI the list does not define, or a control the catalogue lacks or has
withdrawn. Deprecated CCIs and CCIs with no Rev 5 reference are listed as
findings on the crosswalk index rather than dropped.
