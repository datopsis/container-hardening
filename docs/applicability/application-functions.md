# Conditional sources for database, object storage, and API/catalog functions

This is source-selection guidance for a **draft reference standard**, reviewed
on **2026-11-08**. It does not require the image repositories to adopt a workflow,
profile, badge, or dependency on this repository. The assignments below follow
the stated image functions; they are not assessments of the images or their
deployments.

## Current authoritative sources

The [DISA STIGs Document Library](https://www.cyber.mil/stigs/downloads)
listed these releases during this review. Titles and benchmark dates were
checked inside the official packages; library upload dates are separate from
benchmark dates and XCCDF acceptance dates. All three package SHA-256 digests
are pinned in the [source register](../../artifacts/sources.json).

| Source and official package | Version | Release | Benchmark date | Library upload | Register ID | Pinned / rendered |
| --- | --- | --- | --- | --- | --- | --- |
| [Database Security Requirements Guide](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Database_V4R6_SRG.zip) | 4 | 6 | 2026-09-30 | 2026-10-06 | `disa-database-srg` | Yes / yes |
| [Application Programming Interface (API) Security Requirements Guide](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_API_V1R1_SRG.zip) | 1 | 1 | 2025-09-11 | 2025-11-25 | `disa-api-srg` | Yes / yes |
| [Application Security and Development Security Technical Implementation Guide](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_ASD_V6R5_STIG.zip) | 6 | 5 | 2026-09-30 | 2026-10-05 | `disa-application-security-development-stig` | Yes / yes |

The API SRG is the **final V1R1**, not the earlier V1R0.1 public draft.
The Database and API Overviews (§2.2) provide generic procedures where a
product-specific STIG is unavailable. The ASD Overview (§1.1) covers
network-connected enterprise applications, including RESTful services, in
conjunction with applicable technology SRGs. These scopes support the
conditional selections below; DISA does not name these Datopsis repositories.

## Function and repository mapping

| Function | Repositories | Conditional reference and boundary |
| --- | --- | --- |
| Relational database | `postgresql-ubi` | Database SRG V4R6 for the PostgreSQL DBMS, its identities, authorization, audit, and data protection. A vendor-specific PostgreSQL STIG needs a matching product and version. |
| Analytical database | `clickhouse-ubi` | Database SRG V4R6 for ClickHouse as a DBMS. API SRG V1R1 also fits any enabled HTTP or management API; native database protocol traffic is not automatically an HTTP API. |
| Graph database | `neo4j-ubi` | Database SRG V4R6 for the graph DBMS. API SRG V1R1 also fits exposed HTTP/management APIs; evaluate Bolt and database-specific controls separately. |
| Object storage | `seaweedfs-ubi` | No dedicated object-storage SRG or SeaweedFS STIG exists in the current public library. Nearest application-level fit: ASD STIG V6R5 for access control, data protection, validation, audit, and recovery. API SRG V1R1 covers the S3-compatible and administrative service interfaces. Neither supplies SeaweedFS-specific storage configuration checks. |
| Iceberg REST catalog | `lakekeeper-ubi` | API SRG V1R1 directly fits the catalog and management APIs. ASD STIG V6R5 is the nearest broader application reference. No Iceberg catalog or Lakekeeper STIG is listed. A PostgreSQL metadata backend is a separate Database SRG component; using one does not make the catalog itself a DBMS. |
| SQL query engine | `trino-ubi` | API SRG V1R1 for the client/coordinator HTTP API; ASD STIG V6R5 for query execution, authorization, connectors, and application behavior. No Trino/query-engine-specific guide is listed. SQL support alone does not make this federated query engine a database server; use Database SRG requirements only where the deployed component actually owns the corresponding DBMS function. |
| Spark-compatible compute | `sail-ubi` | API SRG V1R1 for a deployed Spark Connect/gRPC or other service API, with protocol-specific tailoring; ASD STIG V6R5 for compute/application behavior. No Sail or Spark-specific guide is listed. Worker-only processes do not inherit every server/API requirement, and reading data from a database or object store does not make a worker either service. |

No product-specific STIG was found for ClickHouse, Neo4j, SeaweedFS,
Lakekeeper, Trino, Sail, Spark, or Iceberg in the 417-entry public library.
This is a dated public-library finding, not a claim about unpublished or
CAC-restricted guidance.

For PostgreSQL, the library lists
[Crunchy Data Postgres 16 STIG V1R3](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_CD_Postgres_16_V1R3_STIG.zip)
and [EnterpriseDB Postgres Advanced Server STIG V2R2](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_EPAS_V2R2_STIG.zip).
Those products are not interchangeable with upstream PostgreSQL. The generic
PostgreSQL 9.x and older Crunchy Data PostgreSQL entries are marked **Sunset**.
No vendor distribution/version match has been verified for `postgresql-ubi`,
so the Database SRG is the selected reference; the vendor STIGs are not added
as selected sources.

The library's **Storage Area Network STIG V2R5 is Sunset**. Its current storage
product entries are HPE Nimble and HPE Alletra Storage ArcusOS STIGs. None is
a generic S3/object-storage baseline or a SeaweedFS product match. ASD is the
nearest fit because it addresses the networked application and its data, not
because an object store is a SAN or a relational DBMS. Object retention,
replication, erasure coding, and bucket policy behavior still need
product-specific analysis.

## Tailoring boundaries

Sources can overlap. The API SRG addresses service interfaces; ASD addresses
the application and development lifecycle. The Database SRG addresses DBMS
behavior. Existing Web Server and Application Server references remain useful
for HTTP serving and actual application-hosting/management functions. Merely
being written in Java or authenticating a request does not establish that a
service hosts separately deployed applications.

The API SRG includes gateway, WAF, token, caching, and HTTP/CORS requirements.
Separate endpoint-owned controls from deployment/gateway controls. Determine
whether each rule's technology is present, especially for Sail's gRPC
interface; do not infer that the container must contain its own gateway or
that every REST-specific check transfers to every protocol. ASD development
process, backup operations, and organizational requirements similarly need
owners beyond the image. These are reference boundaries, not completed
rule-by-rule determinations or conformance claims.

The new register entries use `role: conditional` and `reference_only: true`.
This marks an optional reference, so adding it does not demand new profile
determinations or invalidate an existing reference-image assessment. If a
profile voluntarily records a determination, the existing digest and basis
checks still apply. Changes to an existing source remain revision-sensitive.

## Verification and rendering limits

All three ZIPs were downloaded from the official `dl.dod.cyber.mil` URLs above
and their contents inspected: Database has **142** rules, API **65**, and ASD
**286**. The existing Markdown parser and renderer accept each XCCDF without
duplicate Group IDs. No package bytes are committed.

The 2026-11 DISA adoption restores the complete input set. All three XCCDFs
are now pinned, rendered, and joined to the CCI crosswalk with the existing
generators. The optional `reference_only` boundary is unchanged.

Web Server V4R5 and Application Server V4R6 are now the registered releases.
Rendering does not verify image implementations, product/version matches,
deployed roles, or individual rule determinations. See the
[adoption review](../drift/2026-11-disa-adoption.md) for the mechanical changes
and the decisions still left to owners.
