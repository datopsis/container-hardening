# Rendered requirement catalogues

Generated from the DISA packages pinned in [`artifacts/sources.json`](../../artifacts/sources.json). The source packages themselves are not committed; see [the sources guide](../SOURCES.md).

| Catalogue | Release | Rules |
| --- | --- | ---: |
| [Application Programming Interface (API) Security Requirements Guide](application-programming-interface-api-srg/README.md) | Release: 1 Benchmark Date: 11 Sep 2025 | 65 |
| [Application Security and Development Security Technical Implementation Guide](application-security-and-development-stig/README.md) | Release: 5 Benchmark Date: 30 Sep 2026 | 286 |
| [Application Server Security Requirements Guide](application-server-srg/README.md) | Release: 6 Benchmark Date: 30 Sep 2026 | 137 |
| [Container Platform Security Requirements Guide](container-platform-srg/README.md) | Release: 5 Benchmark Date: 30 Sep 2026 | 188 |
| [Database Security Requirements Guide](database-srg/README.md) | Release: 6 Benchmark Date: 30 Sep 2026 | 142 |
| [General Purpose Operating System Security Requirements Guide](general-purpose-operating-system-srg/README.md) | Release: 4 Benchmark Date: 30 Sep 2026 | 202 |
| [Red Hat Enterprise Linux 9 Security Technical Implementation Guide](red-hat-enterprise-linux-9-stig/README.md) | Release: 10 Benchmark Date: 30 Sep 2026 | 445 |
| [Red Hat OpenShift Container Platform 4.x Security Technical Implementation Guide](red-hat-openshift-container-platform-4-x-stig/README.md) | Release: 7 Benchmark Date: 30 Sep 2026 | 83 |
| [Web Server Security Requirements Guide](web-server-srg/README.md) | Release: 5 Benchmark Date: 01 Jul 2026 | 126 |

Regenerate with `python scripts/build-srg-markdown.py`. CI runs `--check`, which fails if the committed Markdown no longer matches the packages it was generated from.
