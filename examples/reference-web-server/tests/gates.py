#!/usr/bin/env python3
"""Run the supply-chain gates, and record what each found.

Two phases, because the standard puts them on either side of the build:

- ``source``, before the build (IMG-34): a committed-secret scan, and a
  dependency, secret, and build-definition scan of the image's source.
- ``image``, after it: a bill of materials from the built image (IMG-21), two
  independent vulnerability gates that fail on a fixed Critical or High
  finding while recording every finding (IMG-25), and a malware scan of the
  image and its inputs with signatures refreshed in the same run (IMG-28).

The tools are the ones pinned in tools.json and installed by
scripts/install_tools.py; BIN_DIR is where they were installed.

Usage:
    python tests/gates.py source --bin BIN_DIR
    python tests/gates.py image IMAGE --bundle BUNDLE_DIR --bin BIN_DIR
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
REPOSITORY = HERE.parent.parent
LOCK = json.loads((HERE / "lock.json").read_text(encoding="utf-8"))
TOOLS = json.loads((HERE / "tools.json").read_text(encoding="utf-8"))


class Gates:
    def __init__(self, bin_dir: Path, evidence: Path) -> None:
        self.bin = bin_dir
        self.evidence = evidence
        self.results: list[dict] = []
        evidence.mkdir(parents=True, exist_ok=True)

    def tool(self, name: str) -> str:
        return str(self.bin / TOOLS["tools"][name]["binary"])

    def run(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(list(args), text=True, capture_output=True)

    def record(self, criterion: str, check: str, passed: bool, detail: str = "", report: str | None = None) -> None:
        entry = {"criterion": criterion, "check": check, "passed": bool(passed), "detail": detail}
        if report:
            entry["report"] = report
        self.results.append(entry)
        print(("PASS " if passed else "FAIL ") + criterion + "  " + check + ("  (" + detail + ")" if detail and not passed else ""))

    def write(self, name: str) -> int:
        failed = [r for r in self.results if not r["passed"]]
        (self.evidence / name).write_text(json.dumps({
            "tools": {n: t["version"] for n, t in TOOLS["tools"].items()} | {"clamav": TOOLS["images"]["clamav"]["reference"]},
            "passed": len(self.results) - len(failed), "failed": len(failed), "results": self.results,
        }, indent=2) + "\n", encoding="utf-8")
        print(str(len(self.results) - len(failed)) + " passed, " + str(len(failed)) + " failed")
        return 1 if failed else 0


def source(gates: Gates) -> int:
    secrets = gates.evidence / "gitleaks.json"
    result = gates.run(gates.tool("gitleaks"), "dir", str(HERE), "--report-format", "json",
                       "--report-path", str(secrets), "--no-banner", "--redact")
    found = json.loads(secrets.read_text()) if secrets.exists() else []
    gates.record("IMG-34", "no committed secret in the image's source", result.returncode == 0 and not found,
                 str(len(found)) + " findings", "gitleaks.json")

    report = gates.evidence / "trivy-source.json"
    result = gates.run(gates.tool("trivy"), "fs", "--quiet", "--scanners", "vuln,secret,misconfig",
                       "--file-patterns", "dockerfile:Containerfile", "--severity", "HIGH,CRITICAL",
                       "--exit-code", "1", "--format", "json", "--output", str(report), str(HERE))
    gates.record("IMG-34", "no High or Critical dependency, secret, or build-definition finding",
                 result.returncode == 0, result.stderr.strip()[-200:], "trivy-source.json")
    return gates.write("gates-source.json")


def image(gates: Gates, reference: str, bundle: Path) -> int:
    with tempfile.TemporaryDirectory() as scratch:
        work = Path(scratch)
        archive = work / "image.tar"
        subprocess.run(["podman", "save", "--format", "oci-archive", "--output", str(archive), reference], check=True)

        sbom = gates.evidence / "sbom.spdx.json"
        result = gates.run(gates.tool("syft"), "scan", "oci-archive:" + str(archive), "--quiet",
                           "--output", "spdx-json=" + str(sbom))
        packages = set()
        if result.returncode == 0 and sbom.exists():
            document = json.loads(sbom.read_text())
            packages = {p.get("name") for p in document.get("packages", [])}
        missing = sorted(r["name"] for r in LOCK["rpms"] if r["name"] not in packages)
        gates.record("IMG-21", "a bill of materials is generated from the image and covers every locked package",
                     result.returncode == 0 and not missing, ", ".join(missing) or result.stderr.strip()[-200:],
                     "sbom.spdx.json")

        full = gates.evidence / "trivy-image.json"
        gates.run(gates.tool("trivy"), "image", "--quiet", "--input", str(archive), "--format", "json",
                  "--output", str(full))
        gate = gates.run(gates.tool("trivy"), "image", "--quiet", "--input", str(archive), "--ignore-unfixed",
                         "--severity", "HIGH,CRITICAL", "--exit-code", "1", "--format", "table")
        gates.record("IMG-25", "no fixed High or Critical vulnerability (Trivy, every finding recorded)",
                     gate.returncode == 0 and full.exists(), gate.stdout.strip()[-400:], "trivy-image.json")

        grype = gates.evidence / "grype.json"
        result = gates.run(gates.tool("grype"), "sbom:" + str(sbom), "--only-fixed", "--fail-on", "high",
                           "--output", "json", "--file", str(grype))
        gates.record("IMG-25", "no fixed High or Critical vulnerability (Grype, from the bill of materials)",
                     result.returncode == 0, result.stderr.strip()[-400:], "grype.json")

        # The exported filesystem and the verified inputs, as the scanner sees them.
        scan = work / "scan"
        scan.mkdir()
        container = subprocess.run(["podman", "create", reference], text=True, capture_output=True, check=True).stdout.strip()
        try:
            subprocess.run(["podman", "export", "--output", str(scan / "rootfs.tar"), container], check=True)
        finally:
            subprocess.run(["podman", "rm", "--force", container], capture_output=True)
        for rpm in bundle.glob("*.rpm"):
            (scan / rpm.name).write_bytes(rpm.read_bytes())
        report = gates.evidence / "clamav.txt"
        result = gates.run("podman", "run", "--rm", "--entrypoint", "sh", "--volume", str(scan) + ":/scan:ro,Z",
                           TOOLS["images"]["clamav"]["reference"], "-c",
                           "freshclam --stdout --quiet && sigtool --info /var/lib/clamav/daily.c[lv]d | head -4 && "
                           "clamscan --recursive --infected --alert-exceeds-max=yes "
                           "--max-filesize=200M --max-scansize=800M /scan")
        report.write_text(result.stdout + result.stderr)
        gates.record("IMG-28", "no malware in the image or its inputs, with signatures refreshed this run",
                     result.returncode == 0 and "Infected files: 0" in result.stdout,
                     (result.stdout + result.stderr).strip()[-300:], "clamav.txt")
    return gates.write("gates-image.json")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("phase", choices=("source", "image"))
    parser.add_argument("image", nargs="?")
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--bin", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, default=HERE / "evidence")
    args = parser.parse_args()
    gates = Gates(args.bin.resolve(), args.evidence)
    if args.phase == "source":
        return source(gates)
    if not args.image or not args.bundle:
        parser.error("the image phase needs an image and --bundle")
    return image(gates, args.image, args.bundle.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
