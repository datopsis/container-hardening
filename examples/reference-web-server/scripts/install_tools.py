#!/usr/bin/env python3
"""Install the pinned scanning tools, verifying each before it is unpacked.

Every archive in tools.json is downloaded, checked against its recorded size
and SHA-256, and only then extracted. A mismatch stops the install with the
tool named; nothing half-verified reaches the bin directory.

Usage:
    python scripts/install_tools.py BIN_DIR
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import tarfile
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOOLS = json.loads((HERE / "tools.json").read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("bin", type=Path, help="directory to install the tools into")
    args = parser.parse_args()
    args.bin.mkdir(parents=True, exist_ok=True)

    for name, tool in TOOLS["tools"].items():
        with urllib.request.urlopen(tool["url"], timeout=300) as response:
            payload = response.read()
        digest = hashlib.sha256(payload).hexdigest()
        if len(payload) != tool["size"] or digest != tool["sha256"]:
            print(name + ": does not match tools.json (" + digest + ", " + str(len(payload)) + " bytes)", file=sys.stderr)
            return 1
        target = args.bin / tool["binary"]
        if tool.get("archive", True):
            with tarfile.open(fileobj=io.BytesIO(payload)) as archive:
                target.write_bytes(archive.extractfile(archive.getmember(tool["binary"])).read())
        else:
            target.write_bytes(payload)
        target.chmod(0o755)
        print("verified and installed " + name + " " + tool["version"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
