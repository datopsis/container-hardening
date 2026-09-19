# Rendered requirement catalogues

Generated from the DISA packages pinned in [`artifacts/sources.json`](../../artifacts/sources.json). The source packages themselves are not committed; see [the sources guide](../SOURCES.md).

| Catalogue | Release | Rules |
| --- | --- | ---: |
| [Container Platform Security Requirements Guide](container-platform-srg/README.md) | Release: 4 Benchmark Date: 28 Oct 2025 | 188 |
| [General Purpose Operating System Security Requirements Guide](general-purpose-operating-system-srg/README.md) | Release: 3 Benchmark Date: 28 Oct 2025 | 203 |

Regenerate with `python scripts/build-srg-markdown.py`. CI runs `--check`, which fails if the committed Markdown no longer matches the packages it was generated from.
