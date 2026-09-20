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

REPOSITORY = Path(__file__).resolve().parent.parent
OUT = REPOSITORY / "docs" / "architecture" / "diagrams"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from svg import INK, KEY, MAP, MUTED, RENDERED, SVG  # noqa: E402

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
    ("On each architecture, natively:", "amd64, arm64", False),
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
    ("Conformance: validate the evidence and score it", "amd64 and arm64 31/34", True),
    ("If release eligible: push by digest, test, index, sign, tag", "IMG-21, IMG-22, IMG-24", False),
]
s = SVG(760, 60 + len(stages) * 46, "The reference image's pipeline",
        "The reference image's CI, in order, on each architecture natively: check the profile and component definition, install verified scanners, "
        "scan the source, retrieve and verify inputs, show a defective input stops the build, build with networking "
        "disabled, verify the running image, generate the bill of materials and run the vulnerability and malware "
        "gates, check the base is current, re-verify the latest release, then validate and score the evidence in the "
        "conformance workflow, and on a version tag, only if it is release eligible, push each image by digest and test it "
        "there, push an index of those digests, sign and attest, add the version tag, and verify from a clean runner.")
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
        (300, "Build", ["isolated", "reproducible", "provenance", "SBOM"], "IMG-02, 03, 21, 22, 35"),
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

# 8. Which SRGs an image takes -------------------------------------------------
questions = [
    ("Does it serve or proxy HTTP, an API included?", "Web Server SRG", "worksheet: decide every rule"),
    ("Does it host an application runtime, offer a", "Application Server SRG", "worksheet: decide every rule"),
    ("Is it a database management system?", "Database SRG", "not pinned yet: record the gap"),
    ("Does it do something none of these govern?", "No source identified", "record it; ask for one to be pinned"),
]
s = SVG(760, 150 + len(questions) * 96 + 120, "Which SRGs an image takes",
        "Every image takes the General Purpose Operating System SRG for itself, the Container Platform SRG for its "
        "platform, and the RHEL 9 STIG for its host. Then, for each question, a yes adds a conditional source: serving "
        "or proxying HTTP adds the Web Server SRG; hosting an application runtime, a management interface, or user "
        "accounts adds the Application Server SRG; being a database adds the Database SRG, not yet pinned; doing "
        "something none of these govern is recorded as a gap. More than one can apply. Each conditional source is "
        "decided rule by rule in a worksheet, and the determination in the hardening profile follows from it.")
s.box(40, 20, 680, 92, "Every image", ["General Purpose OS SRG: the image", "Container Platform SRG: the platform",
                                        "RHEL 9 STIG: the host"], key=True, columns=2)
y = 150
for i, (question, source, then) in enumerate(questions):
    s.arrow(210, y - 38 if i == 0 else y - 22, 210, y)
    lines = [question] + (["management interface, or user accounts?"] if i == 1 else [])
    s.box(40, y, 340, 74 if i == 1 else 56, "", key=False)
    for j, line in enumerate(lines):
        s.text(210, y + 32 + j * 18, line, 12.5, "600", anchor="middle")
    height = 74 if i == 1 else 56
    s.arrow(380, y + height / 2, 450, y + height / 2)
    s.tag(392, y + height / 2 - 6, "yes")
    s.box(450, y, 270, height, source, [then])
    s.tag(222, y + height + 16, "no, or also")
    y += height + 40
s.box(40, y, 680, 74, "For each conditional source that may apply",
      ["generate its worksheet, decide every rule: applies, not-applicable, other-layer, or covered-by",
       "the profile's determination follows from the worksheet: it applies if any rule applies"], key=True)
s.save("srg-selection.svg")

# 9. Releasing an image ---------------------------------------------------------
person = [
    "Main is green, and conformance says release eligible",
    "No deviation expires before the next release",
    "Unfixed findings are inside their remediation window",
    "Inputs are current, or a refresh is under review",
    "Decisions and worksheets are reviewed and current",
    "Manual reviews that are due are done (ADR-0007)",
    "The version is new; the changelog says what changed",
]
automated = [
    ("Conformance: release eligible, or stop", "IMG-25, IMG-26"),
    ("The tagged commit is on main", "IMG-33"),
    ("Each image pushed by digest, tested there", "IMG-02, IMG-24"),
    ("Index of exactly those digests", "IMG-24"),
    ("Sign index and images; attest SBOMs, provenance", "IMG-21, IMG-22"),
    ("Tag the index's digest with the version", "IMG-24"),
    ("Verify from a clean runner", "IMG-21, IMG-22, IMG-24"),
]
s = SVG(920, 110 + len(person) * 44 + 40, "Releasing an image",
        "Before tagging, a person checks that main is green and conformance says release eligible, that no deviation "
        "expires before the next release, that unfixed findings are inside their remediation window, that inputs are "
        "current, that decisions and worksheets are reviewed, that due manual reviews are done, and that the version "
        "is new with a changelog. Tagging then starts what CI enforces: release eligibility, the commit on main, each "
        "image pushed by digest and tested there, an index of exactly those digests, signatures and attestations, the "
        "version tag on the index's digest, and verification from a clean runner.")
s.text(200, 34, "A person checks, then tags", 14, "600", anchor="middle")
s.text(580, 34, "CI enforces, or stops", 14, "600", anchor="middle")
y = 52
for i, line in enumerate(person):
    s.box(30, y, 340, 32, "")
    s.text(44, y + 21, line, 12)
    if i < len(person) - 1:
        s.arrow(200, y + 32, 200, y + 44)
    y += 44
for i, (line, tags) in enumerate(automated):
    top = 52 + i * 44
    s.box(410, top, 340, 32, "", key=i == 0)
    s.text(424, top + 21, line, 12)
    s.tag(762, top + 21, tags)
    if i < len(automated) - 1:
        s.arrow(580, top + 32, 580, top + 44)
s.path(f"M 370 {52 + (len(person) - 1) * 44 + 16} C 390 {52 + (len(person) - 1) * 44 + 16}, 390 68, 410 68")
s.text(390, 52 + len(person) * 44 + 20, "tag vX.Y.Z", 11.5, "600", fill=MUTED, anchor="middle")
s.save("releasing.svg")

# 10. Where the reference image's controls are applied --------------------------
s = SVG(920, 640, "Where the reference image's controls are applied",
        "A client reaches the reference web server through the platform, which admits the image by verified digest, "
        "imposes the security context, applies network policy, and mounts what the image needs read-only. Inside the "
        "container, nginx runs as an unprivileged user under a read-only root filesystem with one writable tmpfs, "
        "serving content on 8080 and, when key material is mounted, TLS on 8443, and writing its records to the "
        "standard streams, which the platform collects. Each box names the controls that box carries part of; a "
        "control named in more than one box is divided between them, and is satisfied only when every part is.")
s.box(40, 24, 380, 74, "Client", ["Anonymous. No credential is presented,", "and none is asked for."])
s.tag(430, 52, "AC-14, IA-2: nobody is identified")
s.tag(430, 70, "AC-3: what is reachable is the deployment's")
s.arrow(230, 98, 230, 126)
s.box(40, 126, 380, 128, "The deployment and the platform", [
    "Admits the image by verified digest; imposes the",
    "security context; network policy; mounts content,",
    "a server block, a certificate, and a key read-only.",
], key=True)
s.tag(430, 160, "PLT-01, PLT-02: admission and least privilege")
s.tag(430, 178, "PLT-06: secrets as read-only files")
s.tag(430, 196, "PLT-10: traffic controlled and encrypted")
s.tag(430, 214, "SC-8, SC-23, AC-17(2): TLS, when mounted")
s.tag(430, 232, "IA-5, IA-5(6): the key it supplies")
s.arrow(230, 254, 230, 282)
s.box(40, 282, 380, 190, "The container", [
    "nginx 1.26: one master, workers, UID 1001:0",
    "read-only root filesystem; one tmpfs on /tmp",
    "every capability dropped; no new privileges",
    "listeners 8080, and 8443 when TLS is mounted",
    "no package manager, shell service, or su",
    "serves only files under the document root",
])
s.tag(430, 316, "IMG-11 to IMG-15: user, capabilities, ports")
s.tag(430, 334, "AC-6, CM-7: least privilege and functionality")
s.tag(430, 352, "AC-3, SC-5: what it serves, and refuses")
s.tag(430, 370, "SI-10, SI-11: malformed requests, error detail")
s.tag(430, 388, "SC-18: no mobile code of its own")
s.tag(430, 406, "CM-6: the configuration it ships")
s.arrow(230, 472, 230, 500)
s.box(40, 500, 380, 108, "Its records", [
    "access records to standard output, combined",
    "format; errors to standard error; no log file.",
    "The platform collects and retains them.",
])
s.tag(430, 534, "AU-2, AU-3, AU-12: what is logged")
s.tag(430, 552, "AU-9, PLT-09: protected and collected there")
s.tag(430, 570, "AU-10: anonymous, so nothing to attribute")
s.text(480, 614, "A control named in more than one box is divided between them: each box carries part of it, and no part "
       "satisfies it alone.", 11.5, fill=MUTED, anchor="middle", italic=True)
s.save("reference-controls.svg")


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
