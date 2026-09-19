# AC-2 Account Management

| | |
| --- | --- |
| Origination | `research-required` |
| High baseline | Selected |
| Catalogue | NIST SP 800-53 Rev 5, 5.2.0, with SP 800-53A procedures |

Not yet determined for images in general. Whether the image implements this depends on its function; a database authenticates users and a static file server does not. Each image determines it in its own component definition.

## Control

- **a.** Define and document the types of accounts allowed and specifically prohibited for use within the system;
- **b.** Assign account managers;
- **c.** Require [*Assignment: prerequisites and criteria*] for group and role membership;
- **d.** Specify:
  - **1.** Authorized users of the system;
  - **2.** Group and role membership; and
  - **3.** Access authorizations (i.e., privileges) and [*Assignment: attributes (as required)*] for each account;
- **e.** Require approvals by [*Assignment: personnel or roles*] for requests to create accounts;
- **f.** Create, enable, modify, disable, and remove accounts in accordance with [*Assignment: policy, procedures, prerequisites, and criteria*];
- **g.** Monitor the use of accounts;
- **h.** Notify account managers and [*Assignment: personnel or roles*] within:
  - **1.** [*Assignment: time period*] when accounts are no longer required;
  - **2.** [*Assignment: time period*] when users are terminated or transferred; and
  - **3.** [*Assignment: time period*] when system usage or need-to-know changes for an individual;
- **i.** Authorize access to the system based on:
  - **1.** A valid access authorization;
  - **2.** Intended system usage; and
  - **3.** [*Assignment: attributes (as required)*];
- **j.** Review accounts for compliance with account management requirements [*Assignment: frequency*];
- **k.** Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and
- **l.** Align account management processes with personnel termination and transfer processes.

## Assessment objective

Determine if:

- **AC-02** 
  - **AC-02a.** 
    - **AC-02a.[01]** account types allowed for use within the system are defined and documented;
    - **AC-02a.[02]** account types specifically prohibited for use within the system are defined and documented;
  - **AC-02b.** account managers are assigned;
  - **AC-02c.** [*Assignment: prerequisites and criteria*] for group and role membership are required;
  - **AC-02d.** 
    - **AC-02d.01** authorized users of the system are specified;
    - **AC-02d.02** group and role membership are specified;
    - **AC-02d.03** 
      - **AC-02d.03[01]** access authorizations (i.e., privileges) are specified for each account;
      - **AC-02d.03[02]** [*Assignment: attributes (as required)*] are specified for each account;
  - **AC-02e.** approvals are required by [*Assignment: personnel or roles*] for requests to create accounts;
  - **AC-02f.** 
    - **AC-02f.[01]** accounts are created in accordance with [*Assignment: policy, procedures, prerequisites, and criteria*];
    - **AC-02f.[02]** accounts are enabled in accordance with [*Assignment: policy, procedures, prerequisites, and criteria*];
    - **AC-02f.[03]** accounts are modified in accordance with [*Assignment: policy, procedures, prerequisites, and criteria*];
    - **AC-02f.[04]** accounts are disabled in accordance with [*Assignment: policy, procedures, prerequisites, and criteria*];
    - **AC-02f.[05]** accounts are removed in accordance with [*Assignment: policy, procedures, prerequisites, and criteria*];
  - **AC-02g.** the use of accounts is monitored;
  - **AC-02h.** 
    - **AC-02h.01** account managers and [*Assignment: personnel or roles*] are notified within [*Assignment: time period*] when accounts are no longer required;
    - **AC-02h.02** account managers and [*Assignment: personnel or roles*] are notified within [*Assignment: time period*] when users are terminated or transferred;
    - **AC-02h.03** account managers and [*Assignment: personnel or roles*] are notified within [*Assignment: time period*] when system usage or the need to know changes for an individual;
  - **AC-02i.** 
    - **AC-02i.01** access to the system is authorized based on a valid access authorization;
    - **AC-02i.02** access to the system is authorized based on intended system usage;
    - **AC-02i.03** access to the system is authorized based on [*Assignment: attributes (as required)*];
  - **AC-02j.** accounts are reviewed for compliance with account management requirements [*Assignment: frequency*];
  - **AC-02k.** 
    - **AC-02k.[01]** a process is established for changing shared or group account authenticators (if deployed) when individuals are removed from the group;
    - **AC-02k.[02]** a process is implemented for changing shared or group account authenticators (if deployed) when individuals are removed from the group;
  - **AC-02l.** 
    - **AC-02l.[01]** account management processes are aligned with personnel termination processes;
    - **AC-02l.[02]** account management processes are aligned with personnel transfer processes.

## Assessment methods

### Examine

- Access control policy
- personnel termination policy and procedure
- personnel transfer policy and procedure
- procedures for addressing account management
- system design documentation
- system configuration settings and associated documentation
- list of active system accounts along with the name of the individual associated with each account
- list of recently disabled system accounts and the name of the individual associated with each account
- list of conditions for group and role membership
- notifications of recent transfers, separations, or terminations of employees
- access authorization records
- account management compliance reviews
- system monitoring records
- system audit records
- system security plan
- privacy plan
- other relevant documents or records

### Interview

- Organizational personnel with account management responsibilities
- system/network administrators
- organizational personnel with information security with information security and privacy responsibilities

### Test

- Organizational processes for account management on the system
- mechanisms for implementing account management

---

Generated by `scripts/build-control-baseline.py` from the pinned NIST catalogue, which carries the SP 800-53A procedures. Do not edit by hand.
