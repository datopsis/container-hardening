#!/usr/bin/env python3
"""Render the reference-architecture diagrams as standalone SVG.

The diagrams are generated rather than hand-drawn, so that they share one
style and change by editing this file. Each carries its own light background,
so it reads the same in a light or dark viewer, and a <title> and <desc> for
screen readers. The criteria and expectations each stage maps to are drawn
beside it.

Usage:
    python scripts/build-diagrams.py            # regenerate
    python scripts/build-diagrams.py --check    # fail if a committed diagram differs
"""
import argparse
import sys
from pathlib import Path
from xml.sax.saxutils import escape

REPOSITORY = Path(__file__).resolve().parent.parent
OUT = REPOSITORY / "docs" / "architecture" / "diagrams"
RENDERED: dict[str, str] = {}

FONT = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"
INK, MUTED, LINE = "#1f2328", "#57606a", "#8c959f"
BOX, BOX_EDGE = "#f6f8fa", "#8c959f"
KEY, KEY_EDGE = "#ddf4ff", "#0969da"
MAP = "#8250df"


class SVG:
    def __init__(self, width, height, title, desc):
        self.w, self.h = width, height
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="t d">',
            f"<title id=\"t\">{escape(title)}</title>",
            f"<desc id=\"d\">{escape(desc)}</desc>",
            "<defs><marker id=\"a\" viewBox=\"0 0 10 10\" refX=\"9\" refY=\"5\" markerWidth=\"7\" "
            f"markerHeight=\"7\" orient=\"auto-start-reverse\"><path d=\"M0,0 L10,5 L0,10 z\" fill=\"{MUTED}\"/></marker></defs>",
            f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" fill="#ffffff" stroke="#d0d7de"/>',
        ]

    def text(self, x, y, s, size=13, weight="normal", fill=INK, anchor="start", italic=False):
        style = ' font-style="italic"' if italic else ""
        self.parts.append(
            f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{style}>{escape(s)}</text>'
        )

    def box(self, x, y, w, h, title, lines=(), key=False, columns=1, subtitle=None):
        fill, edge = (KEY, KEY_EDGE) if key else (BOX, BOX_EDGE)
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{edge}"/>')
        self.text(x + w / 2, y + 21, title, 14, "600", anchor="middle")
        top = y + 21
        if subtitle:
            self.text(x + w / 2, y + 38, subtitle, 11.5, fill=MUTED, anchor="middle", italic=True)
            top = y + 38
        per = -(-len(lines) // columns) if lines else 0
        for i, line in enumerate(lines):
            col, row = divmod(i, per) if per else (0, 0)
            cx = x + 14 + col * (w - 20) / columns
            self.text(cx, top + 21 + row * 18, line, 12.5, fill=INK)

    def arrow(self, x1, y1, x2, y2):
        self.parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{MUTED}" stroke-width="1.5" marker-end="url(#a)"/>'
        )

    def path(self, d):
        self.parts.append(f'<path d="{d}" fill="none" stroke="{MUTED}" stroke-width="1.5" marker-end="url(#a)"/>')

    def tag(self, x, y, s, anchor="start"):
        self.text(x, y, s, 11.5, "600", fill=MAP, anchor=anchor)

    def save(self, name):
        self.parts.append("</svg>")
        RENDERED[name] = "\n".join(self.parts) + "\n"


# 1. The workload's runtime stack ---------------------------------------------
s = SVG(760, 570, "Container workload runtime stack",
        "A container workload's security context is enforced by the OpenShift security context constraint, "
        "then by the CRI-O and OCI runtime, then by kernel mechanisms, on an RHCOS or Linux host.")
s.box(40, 20, 520, 180, "Container workload", [
    "runAsNonRoot", "arbitrary / random UID", "allowPrivilegeEscalation: false",
    "capabilities: drop [ALL]", "seccomp: RuntimeDefault", "SELinux enforcing",
    "no hostPID / hostIPC", "no hostPath unless approved", "no privileged container",
    "readOnlyRootFilesystem", "explicit resource limits", "user namespace (hostUsers: false)",
], columns=2, subtitle="securityContext the image must work under")
s.tag(575, 60, "IMG-11 to IMG-15")
s.tag(575, 78, "IMG-31, IMG-32")
s.tag(575, 96, "PLT-02, PLT-03, PLT-05")
s.arrow(300, 200, 300, 230)
s.box(40, 230, 520, 58, "OpenShift SCC", subtitle="restricted-v2, or restricted-v3 with user namespaces", key=True)
s.tag(575, 264, "PLT-02, IMG-31, IMG-32")
s.arrow(300, 288, 300, 318)
s.box(40, 318, 520, 44, "CRI-O / OCI runtime")
s.tag(575, 345, "PLT-08 (runtime patched)")
s.arrow(300, 362, 300, 392)
s.box(40, 392, 520, 90, "Kernel mechanisms", [
    "namespaces", "cgroups", "seccomp", "capabilities", "SELinux", "user namespaces"], columns=3)
s.tag(575, 435, "PLT-07, PLT-05")
s.arrow(300, 482, 300, 512)
s.box(40, 512, 520, 44, "RHCOS / Linux host")
s.tag(575, 539, "HST-01 to HST-05")
s.save("runtime-stack.svg")

# 2. The supply chain, before the container exists ----------------------------
steps = [
    ("Source", "IMG-33"), ("Dependencies", "IMG-02, IMG-34"), ("Reproducible, controlled build", "IMG-03, IMG-T2"),
    ("SBOM", "IMG-21"), ("SAST, dependency scan, secret scan", "IMG-34, IMG-05"),
    ("Build provenance", "IMG-22"), ("Image vulnerability and malware scan", "IMG-25, IMG-28"),
    ("Image signing", "IMG-22"), ("Registry (for example, Harbor)", "PLT-12"),
    ("Admission verification", "PLT-01"), ("Deployment (for example, OpenShift)", "PLT-02"),
    ("Runtime policy: SELinux, seccomp", "PLT-07"), ("Monitoring", "PLT-16, PLT-09"),
    ("Continuous vulnerability reassessment", "PLT-08"),
]
h = 20 + len(steps) * 46
s = SVG(640, h, "The container supply chain",
        "Security starts before the container exists: source, dependencies, a controlled build, SBOM, scanning, "
        "provenance, image scanning, signing, the registry, admission verification, deployment, runtime policy, "
        "monitoring, and continuous vulnerability reassessment, each mapped to the criteria or expectations "
        "that implement it.")
y = 16
for i, (label, tags) in enumerate(steps):
    s.box(40, y, 380, 32, "", key=i in (0, 9))
    s.text(230, y + 21, label, 13.5, "600", anchor="middle")
    s.tag(440, y + 21, tags)
    if i < len(steps) - 1:
        s.arrow(230, y + 32, 230, y + 46)
    y += 46
s.save("supply-chain.svg")

# 3a. The reference image's pipeline, as it actually runs ----------------------
stages = [
    ("Check the hardening profile and component definition", "IMG-26", False),
    ("Install the pinned, verified scanners", "IMG-02", False),
    ("Scan the source: secrets, dependencies, build definition", "IMG-34", False),
    ("Retrieve and verify every input (the only networked step)", "IMG-01, IMG-02", False),
    ("Show a tampered or missing input stops the build", "IMG-02, IMG-03", False),
    ("Build with networking disabled", "IMG-03", True),
    ("Run the image restricted; read every property back", "IMG-06 to IMG-20, IMG-30, IMG-32", False),
    ("Bill of materials; vulnerability and malware gates", "IMG-21, IMG-25, IMG-28", False),
    ("Fail on a base more than 30 days behind", "IMG-29", False),
    ("Re-verify the latest published release", "IMG-21, IMG-22, IMG-24", False),
    ("Conformance: validate the evidence and score it", "hardening amd64 31/34", True),
    ("On a version tag, if release eligible: publish, sign, attest", "IMG-21, IMG-22, IMG-24", False),
]
s = SVG(760, 60 + len(stages) * 46, "The reference image's pipeline",
        "The reference image's CI, in order: check the profile and component definition, install verified scanners, "
        "scan the source, retrieve and verify inputs, show a defective input stops the build, build with networking "
        "disabled, verify the running image, generate the bill of materials and run the vulnerability and malware "
        "gates, check the base is current, re-verify the latest release, then validate and score the evidence in the "
        "conformance workflow, and on a version tag, only if it is release eligible, publish, sign, attest, and verify.")
s.text(250, 30, ".github/workflows/reference-image.yml", 13, "600", fill=MUTED, anchor="middle")
y = 44
for i, (label, tags, key) in enumerate(stages):
    s.box(40, y, 420, 32, "", key=key)
    s.text(250, y + 21, label, 12.5, "600", anchor="middle")
    s.tag(478, y + 21, tags)
    if i < len(stages) - 1:
        s.arrow(250, y + 32, 250, y + 46)
    y += 46
s.save("reference-pipeline.svg")

# 3b. The same stages on another stack ----------------------------------------
s = SVG(760, 760, "Example implementation: GitLab, Nexus, Harbor, OpenShift",
        "An example implementation, not a requirement. GitLab source with protected branches, code review, and "
        "signed traceable source feeds a GitLab Runner that takes dependencies from Nexus and the UBI base from "
        "Harbor, produces a CycloneDX SBOM, scans, checks policy, attests in-toto SLSA provenance, and signs with "
        "cosign. Images go to Harbor, then through admission policy checks, then to OpenShift.")
s.text(380, 34, "Example implementation, not a requirement", 13, "600", fill=MUTED, anchor="middle", italic=True)
s.box(40, 52, 520, 96, "GitLab source", ["protected branches", "code review", "signed, traceable source"])
s.tag(575, 100, "IMG-33")
s.arrow(300, 148, 300, 172)
s.box(40, 172, 520, 170, "GitLab Runner", [
    "controlled dependencies from Nexus", "UBI base from Harbor", "SBOM: CycloneDX",
    "vulnerability scan", "policy checks", "in-toto / SLSA provenance", "cosign signature"])
s.tag(575, 215, "IMG-01 to IMG-03")
s.tag(575, 233, "IMG-21, IMG-22")
s.tag(575, 251, "IMG-25, IMG-28, IMG-34")
s.arrow(300, 342, 300, 366)
s.box(40, 366, 520, 44, "Harbor")
s.tag(575, 393, "PLT-12, PLT-08")
s.arrow(300, 410, 300, 434)
s.box(40, 434, 520, 170, "Admission policy", [
    "known registry?", "signature valid?", "approved signer?", "provenance valid?",
    "approved base?", "vulnerability threshold?", "securityContext acceptable?"], key=True)
s.tag(575, 520, "PLT-01, PLT-02")
s.arrow(300, 604, 300, 628)
s.box(40, 628, 520, 44, "OpenShift")
s.tag(575, 655, "PLT-02 to PLT-18")
s.text(40, 712, "Cosign verifies the image digest and in-toto attestations at the Harbor to OpenShift boundary.", 12, fill=MUTED)
s.text(40, 732, "Product names are one worked implementation of the properties the criteria state.", 12, fill=MUTED)
s.save("example-pipeline.svg")

# 4. What a control is, and how it is assessed ---------------------------------
s = SVG(640, 250, "SP 800-53 and SP 800-53A",
        "SP 800-53 states what security control must exist. SP 800-53A states how to assess whether it actually "
        "exists and works correctly.")
s.box(90, 24, 460, 72, "NIST SP 800-53", ["What security control must exist?"])
s.arrow(320, 96, 320, 138)
s.box(90, 138, 460, 90, "NIST SP 800-53A", ["How do I assess whether it actually exists", "and works correctly?"], key=True)
s.save("control-and-assessment.svg")

# 5. Traceability from requirement to evidence ---------------------------------
# Followed through the reference image, so every step names a real file.
chain = [
    ("Requirement", "IMG-13, stated by the image as RWS-013"),
    ("NIST SP 800-53 control", "AC-6(8)"),
    ("DISA CCI / SRG requirement", "CCI-002233, GPOS SRG V-203696"),
    ("Technical implementation", "Containerfile: USER 1001:0; nginx needs no capability"),
    ("Automated test", "tests/smoke.py reads CapEff and NoNewPrivs from /proc"),
    ("Evidence artifact", "evidence/smoke.json, per architecture, every CI run"),
    ("Continuous compliance result", "conformance.yml: hardening amd64 31/34, release eligible"),
]
s = SVG(700, 20 + len(chain) * 62, "Traceability from requirement to evidence",
        "A requirement maps to an 800-53 control, to a DISA CCI or SRG requirement, to a technical implementation, "
        "to an automated test, to an evidence artifact, and to a continuous compliance result. The example follows "
        "IMG-13 through each step.")
y = 16
for i, (label, example) in enumerate(chain):
    s.box(40, y, 300, 44, label, key=i == 0)
    s.text(360, y + 27, example, 12.5, fill=MAP)
    if i < len(chain) - 1:
        s.arrow(190, y + 44, 190, y + 62)
    y += 62
s.save("traceability.svg")

# 6. Ten control domains -------------------------------------------------------
s = SVG(820, 790, "Ten container security control domains",
        "Container security divides into ten domains. Source, Build, and Image feed Registry and Admission, "
        "which feed Runtime. Runtime divides into Kernel, Network, and Identity, which feed Monitoring and Response.")
s.box(300, 16, 220, 36, "Container security", key=True)
cols = [(40, "Source", ["review", "dependencies", "secrets"], "IMG-33, IMG-34"),
        (300, "Build", ["isolated", "reproducible", "provenance", "SBOM"], "IMG-02, 03, 21, 22"),
        (560, "Image", ["minimal", "non-root", "scanned", "signed"], "IMG-06 to IMG-32")]
for x, title, lines, tags in cols:
    s.path(f"M410,52 L410,70 L{x + 110},70 L{x + 110},86")
    s.box(x, 86, 220, 120, title, lines)
    s.tag(x + 110, 224, tags, anchor="middle")
s.path("M150,230 L150,250 L260,250 L260,264")
s.path("M410,230 L410,250 L300,250 L300,264")
s.path("M410,250 L520,250 L520,264")
s.path("M670,230 L670,250 L560,250 L560,264")
s.box(150, 264, 220, 100, "Registry", ["immutable", "RBAC", "scanning"])
s.tag(260, 382, "PLT-08, PLT-12, IMG-24", anchor="middle")
s.box(450, 264, 220, 100, "Admission", ["signature", "provenance", "policy"])
s.tag(560, 382, "PLT-01, PLT-02", anchor="middle")
s.path("M260,388 L260,404 L410,404 L410,420")
s.path("M560,388 L560,404 L410,404 L410,420")
s.box(300, 420, 220, 40, "Runtime", key=True)
for x, title, lines, tags in [(40, "Kernel", ["namespaces", "cgroups", "seccomp", "SELinux", "capabilities"], "PLT-07, IMG-13"),
                              (300, "Network", ["policies", "mTLS", "isolation"], "PLT-10, PLT-18"),
                              (560, "Identity", ["RBAC", "workload identity", "secrets"], "PLT-06, 13, 18")]:
    s.path(f"M410,460 L410,478 L{x + 110},478 L{x + 110},494")
    s.box(x, 494, 220, 130, title, lines)
    s.tag(x + 110, 642, tags, anchor="middle")
for x in (150, 410, 670):
    s.path(f"M{x},648 L{x},664 L410,664 L410,680")
s.box(250, 680, 320, 86, "Monitoring / Response", ["audit / SIEM", "runtime events", "CVE reassessment", "incident response"], columns=2)
s.tag(590, 728, "PLT-08, PLT-09, PLT-16")
s.save("control-domains.svg")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if a committed diagram differs")
    args = parser.parse_args()
    if args.check:
        stale = [
            name for name, body in RENDERED.items()
            if not (OUT / name).exists() or (OUT / name).read_text(encoding="utf-8") != body
        ]
        stale += ["orphaned " + p.name for p in OUT.glob("*.svg") if p.name not in RENDERED]
        if stale:
            print("the diagrams are stale: " + ", ".join(stale), file=sys.stderr)
            print("Regenerate: python scripts/build-diagrams.py", file=sys.stderr)
            return 1
        print("the diagrams are up to date (" + str(len(RENDERED)) + ")")
        return 0
    OUT.mkdir(parents=True, exist_ok=True)
    for name, body in RENDERED.items():
        (OUT / name).write_text(body, encoding="utf-8", newline="\n")
    print("wrote " + str(len(RENDERED)) + " diagrams")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
