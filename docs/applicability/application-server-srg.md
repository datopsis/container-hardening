# Applicability: DISA Application Server SRG

What the DISA Application Server SRG presupposes about the component it
governs, so that an image can determine whether it applies against evidence
rather than against the source's title. An image's hardening profile cites
this page as the basis for its determination; see
[tailoring](../TAILORING.md#applicability).

| | |
| --- | --- |
| Source | `disa-application-server-srg` in the [register](../../artifacts/sources.json) |
| Revision | V4R5, the pinned XCCDF |
| Rules | 137, [rendered](../srg/application-server-srg/README.md) |

## Method

Each rule's title was read, and the rule was listed below if its title states
that it governs one of three things: a **management interface** for the
application server, **applications hosted** on it, or **user accounts and
identities** it manages. A rule that governs one of those only by implication
is not listed, so the counts are a floor, not a ceiling. A rule mentioning
"management" in another sense, such as key management or the expansion of
FICAM, is not counted as governing a management interface.

`tests/test_applicability.py` checks that every rule listed exists in the
rendered catalogue at this revision, and that the counts below are the lengths
of the lists. When the register's pin moves, this page must be redone against
the new revision, as must every determination that cites it.

## Summary

| The rule governs | Rules |
| --- | ---: |
| A management interface | 14 |
| Hosted applications | 2 |
| User accounts and identities | 12 |
| **Any of these** | **27** of 137 |

An image with no management interface, no hosted applications, and no user
accounts has none of the objects these 27 rules govern. They are not
merely unsatisfied; there is nothing for them to apply to. The remaining rules
state general requirements, such as logging, TLS, and session handling, that an
image serving or proxying HTTP takes from the
[Web Server SRG](../srg/web-server-srg/README.md) in terms that fit it.

This is what makes the Application Server SRG not applicable to such an image.
It is not what makes it not applicable to every image: an image that does host
an application runtime, or offers a management interface, should determine it
applicable.

## A management interface

| Group ID | Requirement |
| --- | --- |
| [`V-204709`](../srg/application-server-srg/rules/V-204709.md) | The application server must use encryption strength in accordance with the categorization of the management data during remote access management sessions. |
| [`V-204713`](../srg/application-server-srg/rules/V-204713.md) | The application server management interface must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system. |
| [`V-204714`](../srg/application-server-srg/rules/V-204714.md) | The application server management interface must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access. |
| [`V-204761`](../srg/application-server-srg/rules/V-204761.md) | The application server must separate hosted application functionality from application server management functionality. |
| [`V-204772`](../srg/application-server-srg/rules/V-204772.md) | The application server must check the validity of all data inputs to the management interface, except those specifically identified by the organization. |
| [`V-204778`](../srg/application-server-srg/rules/V-204778.md) | The application server management interface must provide a logout capability for user-initiated communication session. |
| [`V-204779`](../srg/application-server-srg/rules/V-204779.md) | The application server management interface must display an explicit logout message to users indicating the reliable termination of authenticated communications sessions. |
| [`V-204783`](../srg/application-server-srg/rules/V-204783.md) | The application server must provide the capability to immediately disconnect or disable remote access to the management interface. |
| [`V-204800`](../srg/application-server-srg/rules/V-204800.md) | The application server must accept Personal Identity Verification (PIV) credentials to access the management interface. |
| [`V-204801`](../srg/application-server-srg/rules/V-204801.md) | The application server must electronically verify Personal Identity Verification (PIV) credentials for access to the management interface. |
| [`V-204806`](../srg/application-server-srg/rules/V-204806.md) | The application server must accept Personal Identity Verification (PIV) credentials from other federal agencies to access the management interface. |
| [`V-204807`](../srg/application-server-srg/rules/V-204807.md) | The application server must electronically verify Personal Identity Verification (PIV) credentials from other federal agencies to access the management interface. |
| [`V-204828`](../srg/application-server-srg/rules/V-204828.md) | The application must generate log records showing starting and ending times for user access to the application server management interface. |
| [`V-204829`](../srg/application-server-srg/rules/V-204829.md) | The application server must generate log records when concurrent logons from different workstations occur to the application server management interface. |

## Hosted applications

| Group ID | Requirement |
| --- | --- |
| [`V-204761`](../srg/application-server-srg/rules/V-204761.md) | The application server must separate hosted application functionality from application server management functionality. |
| [`V-204767`](../srg/application-server-srg/rules/V-204767.md) | The application server must be configured to perform complete application deployments. |

## User accounts and identities

| Group ID | Requirement |
| --- | --- |
| [`V-204708`](../srg/application-server-srg/rules/V-204708.md) | The application server must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types. |
| [`V-204727`](../srg/application-server-srg/rules/V-204727.md) | The application server must generate log records containing the full-text recording of privileged commands or the individual identities of group account users. |
| [`V-204745`](../srg/application-server-srg/rules/V-204745.md) | The application server must use an approved DOD enterprise identity, credential, and access management (ICAM) solution to uniquely identify and authenticate users (or processes acting on behalf of organizational users). |
| [`V-204746`](../srg/application-server-srg/rules/V-204746.md) | The application server must use multifactor authentication for network access to privileged accounts. |
| [`V-204747`](../srg/application-server-srg/rules/V-204747.md) | The application server must use multifactor authentication for local access to privileged accounts. |
| [`V-204756`](../srg/application-server-srg/rules/V-204756.md) | The application server must map the authenticated identity to the individual user or group account for PKI-based authentication. |
| [`V-204808`](../srg/application-server-srg/rules/V-204808.md) | The application server must accept Federal Identity, Credential, and Access Management (FICAM)-approved third-party credentials. |
| [`V-204809`](../srg/application-server-srg/rules/V-204809.md) | The application server must conform to Federal Identity, Credential, and Access Management (FICAM)-issued profiles. |
| [`V-204830`](../srg/application-server-srg/rules/V-204830.md) | The application server must generate log records for all account creations, modifications, disabling, and termination events. |
| [`V-263549`](../srg/application-server-srg/rules/V-263549.md) | The application server must disable accounts when the accounts are no longer associated to a user. |
| [`V-263551`](../srg/application-server-srg/rules/V-263551.md) | The application server must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that one of the factors is provided by a device separate from the system gaining access. |
| [`V-263552`](../srg/application-server-srg/rules/V-263552.md) | The application server must implement multifactor authentication for local; network; and/or remote access to privileged accounts; and/or nonprivileged accounts such that the device meets organization-defined strength of mechanism requirements. |
