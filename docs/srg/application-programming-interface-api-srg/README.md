# Application Programming Interface (API) Security Requirements Guide

Release: 1 Benchmark Date: 11 Sep 2025. Accepted 2025-09-24.

| | |
| --- | --- |
| Benchmark | `API_SRG` |
| Rules | **65** |
| CAT I | 3 |
| CAT II | 62 |

The source package is not committed. Its identity is pinned by SHA-256 in [`artifacts/sources.json`](../../../artifacts/sources.json).

## Rules

Pages are filed by Group ID, the only identifier DISA guarantees unique. A STIG ID can repeat across rules.

| Group ID | STIG ID | Severity | Requirement |
| --- | --- | --- | --- |
| [`V-274497`](rules/V-274497.md) | `SRG-APP-000014-API-000020` | CAT II | The API must encrypt data in transit. |
| [`V-274507`](rules/V-274507.md) | `SRG-APP-000033-API-000070` | CAT II | The API must be configured to use approved authorizations for access control. |
| [`V-274517`](rules/V-274517.md) | `SRG-APP-000089-API-000120` | CAT II | The API must enable monitoring and alerts. |
| [`V-274519`](rules/V-274519.md) | `SRG-APP-000091-API-001725` | CAT II | The API Gateway must generate audit records when successful/unsuccessful attempts to access privileges occur. |
| [`V-274520`](rules/V-274520.md) | `SRG-APP-000091-API-001730` | CAT II | The API must generate audit records when successful/unsuccessful attempts to access privileges occur. |
| [`V-274522`](rules/V-274522.md) | `SRG-APP-000095-API-001735` | CAT II | The API Gateway must generate audit records of what type of events occurred. |
| [`V-274523`](rules/V-274523.md) | `SRG-APP-000095-API-001740` | CAT II | The API must monitor the usage of API keys to detect any anomalies. |
| [`V-274524`](rules/V-274524.md) | `SRG-APP-000095-API-001745` | CAT II | The API must generate audit records of what type of events occurred. |
| [`V-274525`](rules/V-274525.md) | `SRG-APP-000095-API-001750` | CAT II | The API must audit rate-limiting events. |
| [`V-274526`](rules/V-274526.md) | `SRG-APP-000095-API-001755` | CAT II | The API Gateway must audit rate limiting events. |
| [`V-274527`](rules/V-274527.md) | `SRG-APP-000095-API-001760` | CAT II | The API Gateway must audit authentication and authorization information. |
| [`V-274528`](rules/V-274528.md) | `SRG-APP-000095-API-001765` | CAT II | The API must audit authentication and authorization information. |
| [`V-274529`](rules/V-274529.md) | `SRG-APP-000095-API-001770` | CAT II | The API Gateway must audit exceptions and errors that occur during the processing. |
| [`V-274530`](rules/V-274530.md) | `SRG-APP-000095-API-001775` | CAT II | The API must audit exceptions and errors that occur during the processing. |
| [`V-274531`](rules/V-274531.md) | `SRG-APP-000095-API-001780` | CAT II | The API Gateway must audit execution time and performance metrics. |
| [`V-274532`](rules/V-274532.md) | `SRG-APP-000095-API-001785` | CAT II | The API must audit execution time and performance metrics. |
| [`V-274533`](rules/V-274533.md) | `SRG-APP-000095-API-001790` | CAT II | The API Gateway must audit request and response details (such as method, URL, headers, body, status, etc.). |
| [`V-274534`](rules/V-274534.md) | `SRG-APP-000095-API-001795` | CAT II | The API must audit request and response details (such as method, URL, headers, body, status, etc.). |
| [`V-274537`](rules/V-274537.md) | `SRG-APP-000098-API-000145` | CAT II | All defined API elements must be documented. |
| [`V-274556`](rules/V-274556.md) | `SRG-APP-000141-API-000240` | CAT II | API keys must be configured with usage restrictions. |
| [`V-274557`](rules/V-274557.md) | `SRG-APP-000141-API-000245` | CAT II | The API must limit the exposure of endpoints. |
| [`V-274559`](rules/V-274559.md) | `SRG-APP-000148-API-000255` | CAT II | The API must use an approved DOD enterprise identity, credential, and access management (ICAM) solution to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users). |
| [`V-274600`](rules/V-274600.md) | `SRG-APP-000219-API-000460` | CAT II | The API must protect Session IDs via encryption. |
| [`V-274603`](rules/V-274603.md) | `SRG-APP-000224-API-000475` | CAT II | The API keys must be securely generated using a FIPS-validated Random Number Generator (RNG). |
| [`V-274606`](rules/V-274606.md) | `SRG-APP-000231-API-000490` | CAT II | The API implementation must use FIPS-validated encryption and hashing algorithms to protect the confidentiality and integrity of API keys. |
| [`V-274607`](rules/V-274607.md) | `SRG-APP-000231-API-000495` | CAT I | The API must encrypt sensitive cached data. |
| [`V-274612`](rules/V-274612.md) | `SRG-APP-000247-API-000520` | CAT II | The API must employ throttling. |
| [`V-274613`](rules/V-274613.md) | `SRG-APP-000251-API-000525` | CAT II | The API must specify allowed origins when using Cross-Origin Resource Sharing (CORS). |
| [`V-274615`](rules/V-274615.md) | `SRG-APP-000266-API-000535` | CAT II | The API must not disclose sensitive data in error messages. |
| [`V-274643`](rules/V-274643.md) | `SRG-APP-000340-API-000675` | CAT II | Access to API privileged features and functions must be restricted. |
| [`V-274672`](rules/V-274672.md) | `SRG-APP-000389-API-000820` | CAT II | The API must require periodic reauthentication. |
| [`V-274677`](rules/V-274677.md) | `SRG-APP-000400-API-000845` | CAT II | The API must have a mechanism for cache invalidation when using cache policy data. |
| [`V-274678`](rules/V-274678.md) | `SRG-APP-000400-API-000850` | CAT II | When stateless authentication tokens are used, the API must configure them with appropriate security settings. |
| [`V-274679`](rules/V-274679.md) | `SRG-APP-000400-API-000855` | CAT II | The API's internal authorization tokens must not be provided back to the user. |
| [`V-274680`](rules/V-274680.md) | `SRG-APP-000400-API-000860` | CAT II | API access tokens must be configured to expire. |
| [`V-274681`](rules/V-274681.md) | `SRG-APP-000400-API-000865` | CAT II | API refresh tokens must be configured to expire. |
| [`V-274682`](rules/V-274682.md) | `SRG-APP-000247-API-000870` | CAT II | The API must enforce per-client rate limits. |
| [`V-274697`](rules/V-274697.md) | `SRG-APP-000419-API-000945` | CAT II | Clients must be configured to route requests through a single API gateway that enforces the association and transmission of organization-defined security attributes with each request. |
| [`V-274707`](rules/V-274707.md) | `SRG-APP-000435-API-000995` | CAT II | The API must use a gateway. |
| [`V-274709`](rules/V-274709.md) | `SRG-APP-000439-API-001005` | CAT I | The amount of data returned by the API must be restricted. |
| [`V-274710`](rules/V-274710.md) | `SRG-APP-000439-API-001010` | CAT I | The API must use TLS version 1.2 at a minimum. |
| [`V-274712`](rules/V-274712.md) | `SRG-APP-000441-API-001020` | CAT II | The API must audience-restrict access tokens in accordance with organization-defined identification and authentication policy. |
| [`V-274714`](rules/V-274714.md) | `SRG-APP-000447-API-001030` | CAT II | The API must use parameterized queries. |
| [`V-274715`](rules/V-274715.md) | `SRG-APP-000447-API-001035` | CAT II | The API must provide input validation. |
| [`V-274723`](rules/V-274723.md) | `SRG-APP-000461-API-001075` | CAT II | The API must authenticate remote commands. |
| [`V-274767`](rules/V-274767.md) | `SRG-APP-000516-API-001295` | CAT II | The API must encode outputs. |
| [`V-274768`](rules/V-274768.md) | `SRG-APP-000516-API-001300` | CAT II | The API must use a static type of system. |
| [`V-274769`](rules/V-274769.md) | `SRG-APP-000516-API-001305` | CAT II | The API must use Web Application Firewall (WAF). |
| [`V-274783`](rules/V-274783.md) | `SRG-APP-000630-API-001375` | CAT II | The API must use a FIPS-validated cryptographic module to provision digital signatures for tokens. |
| [`V-274785`](rules/V-274785.md) | `SRG-APP-000645-API-001385` | CAT II | API services identified within the system as unnecessary and/or nonsecure must be disabled. |
| [`V-274830`](rules/V-274830.md) | `SRG-APP-000915-API-001610` | CAT II | The API must provide protected storage for API keys. |
| [`V-274835`](rules/V-274835.md) | `SRG-APP-000945-API-001635` | CAT II | API must use a circuit breaker pattern to handle failures and timeouts. |
| [`V-274839`](rules/V-274839.md) | `SRG-APP-000965-API-001655` | CAT II | Cryptographic keys that protect access tokens must be protected. |
| [`V-274840`](rules/V-274840.md) | `SRG-APP-000970-API-001660` | CAT II | The API must protect the private keys used to sign assertions and tokens. |
| [`V-274841`](rules/V-274841.md) | `SRG-APP-000975-API-001665` | CAT II | Generating assertions must be restricted. |
| [`V-274842`](rules/V-274842.md) | `SRG-APP-000980-API-001670` | CAT II | The API must issue assertions in accordance with organization-defined identification and authentication policy. |
| [`V-274843`](rules/V-274843.md) | `SRG-APP-000985-API-001675` | CAT II | The API must refresh assertions in accordance with organization-defined identification and authentication policy. |
| [`V-274844`](rules/V-274844.md) | `SRG-APP-000990-API-001680` | CAT II | The API must revoke assertions in accordance with organization-defined identification and authentication policy. |
| [`V-274845`](rules/V-274845.md) | `SRG-APP-000995-API-001685` | CAT II | The API must time-restrict assertions in accordance with organization-defined identification and authentication policy. |
| [`V-274846`](rules/V-274846.md) | `SRG-APP-001000-API-001690` | CAT II | The API must audience-restrict assertions in accordance with organization-defined identification and authentication policy. |
| [`V-274847`](rules/V-274847.md) | `SRG-APP-001005-API-001695` | CAT II | The API must generate access tokens in accordance with organization-defined identification and authentication policy. |
| [`V-274848`](rules/V-274848.md) | `SRG-APP-001010-API-001700` | CAT II | The API must issue access tokens in accordance with organization-defined identification and authentication policy. |
| [`V-274849`](rules/V-274849.md) | `SRG-APP-001015-API-001705` | CAT II | The API must refresh access tokens in accordance with organization-defined identification and authentication policy. |
| [`V-274850`](rules/V-274850.md) | `SRG-APP-001020-API-001710` | CAT II | The API must revoke access tokens in accordance with organization-defined identification and authentication policy. |
| [`V-274851`](rules/V-274851.md) | `SRG-APP-001025-API-001715` | CAT II | The API must time-restrict access tokens in accordance with organization-defined identification and authentication policy. |
