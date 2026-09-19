# CLAUDE.md

Guidance for coding agents working in this repository.

## Project overview

This repository defines the criteria, implementation, and controls used in
every Datopsis container build, and the expectations placed on the platform
those containers run on. One standard, applied across repositories, tailored
per application rather than reinvented per application.

Read [`docs/ROADMAP.md`](docs/ROADMAP.md) first. It states what this repository
is, what exists, and what remains.

## Non-negotiable properties

- **Source packages are never committed.** DISA packages are US Government
  works whose redistribution terms live inside the package. `.gitignore`
  excludes `U_*_SRG/`, `U_*_STIG/`, `sources/`, and `*.zip`. What is committed
  is generated Markdown plus the pinned identity of what generated it.
- **CIS benchmark text is never reproduced**, in any form. It may be cited by
  identifier only.
- **Every source is pinned by SHA-256 before anything maps against it.** A
  mapping is meaningless without a known revision.
- **A drifted source is a finding, not a digest to update.** `verify-sources.py`
  never edits the register. The correct response to a replaced DISA release is
  to read the per-rule diff and decide.
- **The three layers stay apart.** Image controls (GPOS SRG), platform controls
  (Container Platform SRG), and host controls (RHEL 9 STIG) have different
  owners. Conflating them is the failure this repository exists to prevent.
- Never claim STIG certification, FIPS validation, or an authorization. This
  repository produces a standard and a mapping, not an authorization package.

## Working with DISA packages

Extract into the repository root or `sources/`, then:

```sh
python scripts/build-srg-markdown.py            # regenerate docs/srg/
python scripts/build-srg-markdown.py --check    # fail if committed output is stale
python scripts/verify-sources.py                # re-verify every pinned digest
python -m unittest tests.test_sources -v
```

Three things that will otherwise cost you an hour:

- **A STIG ID is not unique.** GPOS V3R3 issues `SRG-OS-000132-GPOS-00067` as
  both `V-203655` and `V-278973`. Rule pages are filed by Group ID.
- **A `200` does not mean a release is current.** DISA serves superseded
  releases alongside current ones. Probe adjacent releases, and probe the whole
  range — a sweep that stopped at V2R3 concluded the Container Platform SRG was
  unavailable when V2R4 was published.
- **Filenames use DISA's abbreviation.** `U_GPOS_V3R3_SRG.zip`, not the
  expanded title. The download index is a JavaScript portal and cannot be
  scraped; direct URLs work once known.

## Conventions

Regenerating the catalogues touches hundreds of files. **Keep a regeneration in
its own commit**, separate from hand-written changes, or the diff buries them.

Completed roadmap items are deleted from `docs/ROADMAP.md` rather than checked
off, so the file is always the remaining work.

Decisions that are expensive to reverse, that give up something a reader would
expect, or whose reasoning is not recoverable from the code go in `docs/adr/`.
Where a decision is enforced by a test or CI gate, the record says so;
unenforced decisions decay quietly.

Use concise Conventional Commit subjects: `feat:`, `fix:`, `docs:`, `test:`,
`ci:`, `chore:`.

Do not add `Co-Authored-By`, AI, assistant, or tool-attribution trailers to
commit messages.
