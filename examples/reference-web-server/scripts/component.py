#!/usr/bin/env python3
"""Generate the reference image's OSCAL component definition.

Every control in the standard's baseline gets one entry. Where the baseline
settles a control, the entry takes its origination. Where the baseline leaves
it research-required, DECISIONS below says what this image does, with the
reason. An image-owned entry cites the criteria the baseline gives for it and
the requirements that state them, as requirements-crosswalk.json maps them,
which is the verification pointer; a criterion the profile records a
deviation from is not cited.

DECISIONS are this image's, a static web server's. An image with another
function decides each of them again; check-component.py warns on one copied
word for word.

The output is checked by scripts/check-component.py in the repository root.

Usage:
    python scripts/component.py            # write oscal/component-definition.json
    python scripts/component.py --check    # fail if it is stale, or the crosswalk
                                           # disagrees with requirements.md
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parent.parent
BASELINE = json.loads((ROOT / "artifacts" / "control-baseline.json").read_text(encoding="utf-8"))
PROFILE = json.loads((HERE / "hardening-profile.json").read_text(encoding="utf-8"))
OUTPUT = HERE / "oscal" / "component-definition.json"
MAP = json.loads((HERE / "requirements-crosswalk.json").read_text(encoding="utf-8"))
NS = BASELINE["model"]["namespace"]
SEED = uuid.UUID("6f1c0b52-3d1e-4c6a-9a55-2b6f3f0c7e10")

NO_ACCOUNTS = "The image has no user accounts, logon, sessions, or authenticators: it serves static content to anonymous clients."
DECISIONS = {
    **{c: ("not-applicable", NO_ACCOUNTS) for c in (
        "ac-2", "ac-2.1", "ac-2.2", "ac-2.3", "ac-2.4", "ac-2.5", "ac-2.11", "ac-2.12",
        "ac-6.1", "ac-6.2", "ac-6.3", "ac-6.5", "ac-6.9", "ac-7", "ac-8", "ac-10", "ac-12",
        "ia-2", "ia-2.1", "ia-2.2", "ia-2.5", "ia-2.8", "ia-2.12", "ia-4", "ia-4.4",
        "ia-5", "ia-5.1", "ia-5.2", "ia-5.6", "ia-6", "ia-8", "ia-8.1", "ia-8.2", "ia-8.4", "ia-11")},
    "ia-7": ("not-applicable", "The image authenticates to no cryptographic module; it makes no FIPS claim."),
    "au-10": ("not-applicable", "The image serves anonymous requests; there is no individual whose actions must be undeniable."),
    "si-4.10": ("not-applicable", "The image does not monitor traffic; that is the platform's (PLT-16)."),
    "si-8": ("not-applicable", "The image handles no mail."),
    "si-8.2": ("not-applicable", "The image handles no mail."),
    "ac-3": ("deployment-configured", "Which content is served, and to whom, is the deployment's mounted content and configuration."),
    "ac-14": ("deployment-configured", "The image serves its content without identification by design; the deployment decides what content that is."),
    "ac-17.2": ("deployment-configured", "TLS is enabled by mounting a server block, certificate, and key (IMG-16); the deployment chooses to."),
    "sc-8": ("deployment-configured", "TLS protects transmission when the deployment mounts it; the image serves plain HTTP on 8080 otherwise."),
    "sc-8.1": ("deployment-configured", "As SC-8: TLS 1.2 and 1.3, when the deployment mounts it."),
    "sc-10": ("deployment-configured", "Idle connections close after nginx's keepalive timeout; the deployment may set its own."),
    "sc-18": ("deployment-configured", "Any script in the served content is the deployment's content, not the image's."),
    "sc-23": ("deployment-configured", "Session authenticity is TLS, when the deployment mounts it."),
    "au-3.1": ("deployment-configured", "The deployment may extend nginx's log format with further fields."),
    "au-2": ("image-owned", "nginx logs every request to standard output and every error to standard error."),
    "au-3": ("image-owned", "Each access record states the client, time, request, status, size, referrer, and user agent."),
    "au-12": ("image-owned", "Audit records are generated for every request, with nothing to enable."),
    "cm-6": ("research-required", "The image ships a reviewed configuration, but no SCAP rule selection yet evidences its settings (IMG-T3)."),
    "cm-6.1": ("research-required", "As CM-6: automated verification of settings awaits the SCAP profile (IMG-T3)."),
    "sc-13": ("research-required", "nginx uses OpenSSL as shipped by Red Hat. The standard makes no FIPS claim, and its position on images that protect CUI is open."),
    "si-10": ("research-required", "nginx rejects malformed requests, but no criterion yet evidences it."),
    "si-11": ("research-required", "server_tokens is off, so errors do not disclose the version, but no criterion yet evidences error handling."),
}
LOGGING_CRITERIA = ["IMG-19"]


def requirements() -> dict[str, list[str]]:
    """The crosswalk: which requirements state each criterion."""
    return MAP["criteria"]


def stated_in_prose() -> dict[str, list[str]]:
    """The same map, as requirements.md states it, to keep the two in step."""
    by_criterion: dict[str, list[str]] = {}
    text = (HERE / "requirements.md").read_text(encoding="utf-8")
    for identifier, criterion in re.findall(r"^### (RWS-\d{3})\n.*?^- Criterion: (IMG-\d+)$", text, re.M | re.S):
        by_criterion.setdefault(criterion, []).append(identifier)
    return by_criterion


def prop(name: str, value: str) -> dict:
    return {"name": name, "ns": NS, "value": value}


def build() -> str:
    stated = requirements()
    deviated = {d["target"] for d in PROFILE["deviations"] if d["kind"] == "criterion"}
    roles = {k: v["responsible_role"] for k, v in BASELINE["model"]["originations"].items()}
    entries = []
    for control in BASELINE["controls"]:
        origination, remarks = control["origination"], control["reason"]
        criteria = list(control["criteria"]) if origination == "image-owned" else []
        if origination == "research-required":
            if control["id"] not in DECISIONS:
                raise SystemExit(control["id"] + " is research-required in the baseline and undecided here")
            origination, remarks = DECISIONS[control["id"]]
            criteria = LOGGING_CRITERIA if origination == "image-owned" else []
        props = [prop("origination", origination)]
        if origination == "image-owned" and control["origination"] == "image-owned":
            # An image-owned claim states what it rests on and where it stops.
            titles = "; ".join(c + " " + BASELINE["criteria"][c]["title"] for c in criteria)
            handoff = ", ".join(control["handoff"])
            remarks = ("Rests on " + titles + ". The image cannot constrain what a deployment mounts or how it runs "
                       "the image" + (": the platform's part is " + handoff + "." if handoff else "."))
        if origination == "image-owned":
            cited = [c for c in criteria if c not in deviated]
            pointers = sorted({r for c in cited for r in stated.get(c, [])})
            props += [prop("criterion", c) for c in cited]
            props += [prop("requirement", r) for r in pointers]
            props.append(prop("assessment-method", "test"))
        role = roles[origination]
        entries.append({
            "uuid": str(uuid.uuid5(SEED, control["id"])),
            "control-id": control["id"],
            "props": props,
            **({"responsible-roles": [{"role-id": role}]} if role else {}),
            "description": control["label"] + " " + control["title"] + ".",
            "remarks": remarks,
        })
    document = {"component-definition": {
        "uuid": str(uuid.uuid5(SEED, "component-definition")),
        "metadata": {
            "title": "reference-web-server component definition",
            "last-modified": "2026-09-19T00:00:00Z",
            "version": "0.1.0",
            "oscal-version": "1.1.2",
            "roles": [{"id": r, "title": r} for r in sorted({v for v in roles.values() if v})],
        },
        "components": [{
            "uuid": str(uuid.uuid5(SEED, "component")),
            "type": "software",
            "title": "reference-web-server",
            "description": "A static HTTP server image on UBI 9 Micro, built to the container hardening standard.",
            "control-implementations": [{
                "uuid": str(uuid.uuid5(SEED, "implementation")),
                "source": "https://raw.githubusercontent.com/usnistgov/oscal-content/v1.5.0/nist.gov/SP800-53/rev5/json/NIST_SP-800-53_rev5_catalog.json",
                "description": "Controls in the standard's baseline, as this image implements or hands them off.",
                "implemented-requirements": entries,
            }],
        }],
    }}
    return json.dumps(document, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    body = build()
    if args.check:
        prose = stated_in_prose()
        if {c: sorted(r) for c, r in prose.items()} != {c: sorted(r) for c, r in requirements().items()}:
            print("requirements-crosswalk.json and requirements.md map criteria to requirements differently", file=sys.stderr)
            return 1
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != body:
            print("the component definition is stale: python scripts/component.py", file=sys.stderr)
            return 1
        print("the component definition is up to date")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(body, encoding="utf-8", newline="\n")
    print("wrote " + str(OUTPUT.relative_to(HERE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
