---
status: accepted
date: 2026-09-18
decision-makers: Joey
---

# Derive SRG-to-800-53 cross-references from the DISA CCI list

## Context and Problem Statement

The control mapping needs to say which NIST SP 800-53 Rev 5 control each SRG
rule serves. The spine is 800-53, and the rules come from SRGs, so every
mapping, applicability decision, and handoff in the standard crosses that line.

Written by hand, that is 391 rules today and several hundred more once the RHEL
9 STIG and the conditional SRGs are rendered, repeated for every release. It
would also be a set of assertions made by this repository about what DISA
meant.

DISA already publishes the answer. Every SRG rule carries one or more
Control Correlation Identifiers as `<ident system="http://cyber.mil/cci">`,
and the DISA CCI list maps each CCI to 800-53 Rev 5, down to the part of the
control (`AC-2 a 1`, `AC-3 (15) (a)`). When the list was pinned, each of the
284 distinct CCIs cited by the Container Platform and GPOS SRGs resolved, was
current, and carried a Rev 5 reference to a control present and not withdrawn
in 800-53 5.2.0.

## Decision Drivers

* A cross-reference must be traceable to a pinned source, not to a person
* The mapping has to scale to every catalogue this standard will render
* A release upgrade of any input must show up as a reviewable diff
* The spine is 800-53 in OSCAL, so control identifiers must resolve in it

## Considered Options

* **Hand-author the cross-reference** — decide per rule which controls it
  serves
* **Derive it from the CCI list** — join each rule's CCIs to DISA's published
  Rev 5 references and resolve them against the pinned OSCAL catalogue
* **Derive it, with local overrides** — the join, plus a file of corrections
  where this repository disagrees with DISA

## Decision Outcome

Chosen option: **derive it from the CCI list**, with no local overrides.

Hand-authoring was rejected because it doesn't scale and because the result is
this repository's opinion presented as a mapping. DISA assigns the CCIs, and
the CCI list is DISA's own statement of what they mean in 800-53 terms.

Local overrides were a viable option. They lost because an override quietly
turns a derived mapping back into an asserted one, and nothing forces anyone to
revisit an override when the CCI list is next revised. If DISA's mapping is
wrong for a rule, the finding belongs in that rule's applicability or deviation
record (Package 4), where it has a reason and an expiry. It does not belong in
a silent edit to the crosswalk.

The join is kept at control and enhancement granularity (`ac-2.4`), which is
the level at which OSCAL, baselines, and component definitions operate. DISA's
part-level reference is carried alongside it, not discarded, because it is
often the most useful thing on the page.

### Consequences

* Good: every cross-reference names the revisions it came from, and a change
  in the CCI list, the catalogue, or an SRG regenerates as a diff
* Good: rendering a new catalogue adds it to the crosswalk for free
* Good: the crosswalk shows which controls an SRG reaches that the High
  baseline does not select, which hand-authoring would not have surfaced
* Bad: DISA's errors are inherited verbatim. The crosswalk is exactly as right
  as the CCI list
* Bad: the CCI list is published at an unversioned URL and replaced in place.
  Its revision is only its digest and its internal version date
* Bad: the crosswalk reports which controls a rule reaches, not whether an
  image satisfies them. It is an input to the control mapping, not the mapping

### Enforcement

`scripts/build-cci-crosswalk.py` refuses to generate if any input fails to
match its pinned digest, if an SRG cites a CCI the list does not define, or if
a CCI maps to a control the pinned catalogue does not contain or has withdrawn.
Deprecated CCIs, CCIs with no Rev 5 reference, and rules citing no CCI are
reported as findings on the crosswalk index. None of those is dropped.

`tests/test_crosswalk.py`, on every pull request, checks that the committed
crosswalk records the digests the register pins and covers exactly the rendered
rules, and that its data and pages agree. `verify-sources.yml`, weekly, runs
`build-cci-crosswalk.py --check` against the retrieved sources.

Nothing enforces the absence of local overrides except this record and review.
