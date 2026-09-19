#!/usr/bin/env python3
"""Verify the reference image against the criteria, and record the evidence.

Each check is labelled with the criterion it establishes. The image is run the
way the standard says a platform will run it: read-only, every capability
dropped, no new privileges, the declared tmpfs and nothing else. Passing those
flags is not taken as evidence they applied; every process's status is read
back from /proc.

HTTP is probed from a pinned probe container joined to the image's network
namespace, so the checks behave the same on a workstation and in CI.

Usage:
    python tests/smoke.py IMAGE [--evidence evidence/smoke.json] [--revision SHA]
"""

from __future__ import annotations

import argparse
import io
import json
import re
import subprocess
import sys
import tarfile
import tempfile
import time
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
LOCK = json.loads((HERE / "lock.json").read_text(encoding="utf-8"))
BEHAVIOUR = json.loads((HERE / "behaviour.json").read_text(encoding="utf-8"))
FEATURES = json.loads((HERE / "features.json").read_text(encoding="utf-8"))
PROBE = "registry.access.redhat.com/" + LOCK["bases"]["builder"]["repository"] + "@" + LOCK["bases"]["builder"]["digest"]
TMPFS = "/tmp:rw,noexec,nosuid,nodev,size=16m"
# Podman mounts its own tmpfs on /tmp, /var/tmp, and /run under --read-only
# unless told not to, which would hide a missing declared mount.
RESTRICTED = ["--read-only", "--read-only-tmpfs=false", "--cap-drop", "ALL", "--security-opt", "no-new-privileges"]
ABSENT = [
    "usr/bin/dnf", "usr/bin/microdnf", "usr/bin/yum", "usr/bin/rpm", "usr/bin/rpmkeys",
    "usr/bin/curl", "usr/bin/wget", "usr/bin/gcc", "usr/bin/cc", "usr/bin/make",
    "usr/sbin/sshd", "usr/bin/ssh", "usr/sbin/telnetd", "usr/bin/su", "usr/bin/sudo",
    "etc/yum.repos.d",
]


class Suite:
    def __init__(self, image: str) -> None:
        self.image = image
        self.results: list[dict] = []
        self.containers: list[str] = []

    def record(self, criterion: str, check: str, passed: bool | None, detail: str = "") -> None:
        """Record one check. None means it could not run here, which is not evidence either way."""
        outcome = None if passed is None else bool(passed)
        self.results.append({"criterion": criterion, "check": check, "passed": outcome, "detail": detail})
        label = "SKIP " if outcome is None else "PASS " if outcome else "FAIL "
        print(label + criterion + "  " + check + ("  (" + detail + ")" if detail and outcome is not True else ""))

    def podman(self, *args: str, check: bool = False, input: str | None = None) -> subprocess.CompletedProcess:
        return subprocess.run(["podman", *args], text=True, capture_output=True, check=check, input=input)

    def start(self, *extra: str, user: str | None = None, name: str | None = None) -> str:
        name = name or "rws-" + uuid.uuid4().hex[:8]
        args = ["run", "--detach", "--name", name, *RESTRICTED, "--tmpfs", TMPFS, *extra]
        if user:
            args += ["--user", user]
        self.podman(*args, self.image, check=True)
        self.containers.append(name)
        return name

    def http(self, container: str, url: str, insecure: bool = False) -> int:
        for _ in range(20):
            result = self.podman("run", "--rm", "--network", "container:" + container, PROBE,
                                 "curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", *(["-k"] if insecure else []), url)
            if result.stdout.strip() not in ("", "000"):
                return int(result.stdout.strip())
            time.sleep(0.5)
        return 0

    def exec(self, container: str, *command: str) -> subprocess.CompletedProcess:
        return self.podman("exec", container, *command)

    def cleanup(self) -> None:
        for name in self.containers:
            self.podman("rm", "--force", name)


def proc_status(suite: Suite, container: str) -> list[dict]:
    pids = [p for p in suite.exec(container, "ls", "/proc").stdout.split() if p.isdigit()]
    found = []
    for pid in pids:
        text = suite.exec(container, "cat", "/proc/" + pid + "/status").stdout
        if not text:
            continue
        fields = dict(line.split(":", 1) for line in text.splitlines() if ":" in line)
        found.append({k: v.strip() for k, v in fields.items() if k in ("Name", "Uid", "Gid", "CapEff", "NoNewPrivs", "Seccomp")} | {"Pid": pid})
    return found


def listening_ports(suite: Suite, container: str) -> set[int]:
    ports = set()
    for table in ("tcp", "tcp6"):
        for line in suite.exec(container, "cat", "/proc/net/" + table).stdout.splitlines()[1:]:
            fields = line.split()
            if len(fields) > 3 and fields[3] == "0A":
                ports.add(int(fields[1].rsplit(":", 1)[1], 16))
    return ports


def filesystem(suite: Suite) -> tarfile.TarFile:
    container = suite.podman("create", suite.image, check=True).stdout.strip()
    try:
        exported = subprocess.run(["podman", "export", container], capture_output=True, check=True).stdout
    finally:
        suite.podman("rm", "--force", container)
    return tarfile.open(fileobj=io.BytesIO(exported))


def static_checks(suite: Suite, revision: str | None) -> None:
    config = json.loads(suite.podman("image", "inspect", suite.image, check=True).stdout)[0]
    user = config["Config"].get("User", "")
    uid, _, gid = user.partition(":")
    suite.record("IMG-11", "configured user is numeric, non-zero, with group 0", uid.isdigit() and int(uid) != 0 and gid == "0", user)
    # Podman reports the healthcheck at the top level of the inspect output.
    health = (config.get("Healthcheck") or config["Config"].get("Healthcheck") or {}).get("Test") or []
    suite.record("IMG-20", "HEALTHCHECK is declared in exec form", bool(health) and health[0] == "CMD", str(health))
    suite.record("IMG-20", "STOPSIGNAL is declared", bool(config["Config"].get("StopSignal")), str(config["Config"].get("StopSignal")))
    ports = [int(p.split("/")[0]) for p in (config["Config"].get("ExposedPorts") or {})]
    suite.record("IMG-14", "every exposed port is 1024 or above", bool(ports) and min(ports) >= 1024, str(ports))
    labels = config["Config"].get("Labels") or {}
    required = ["org.opencontainers.image.source", "org.opencontainers.image.revision", "org.opencontainers.image.version",
                "org.opencontainers.image.created", "org.opencontainers.image.base.name",
                "org.opencontainers.image.base.digest", "reference-web-server.lock.sha256"]
    missing = [label for label in required if not labels.get(label) or labels[label] == "unknown"]
    suite.record("IMG-23", "identifying labels are present", not missing, ", ".join(missing))
    if revision:
        suite.record("IMG-23", "revision label equals the commit", labels.get("org.opencontainers.image.revision") == revision)

    archive = filesystem(suite)
    members = {m.name.rstrip("/"): m for m in archive.getmembers()}
    present = [path for path in ABSENT if path in members]
    suite.record("IMG-06", "no package manager or repository configuration", not any(p for p in present if "rpm" in p or "dnf" in p or "yum" in p), ", ".join(present))
    keys = [n for n in members if re.search(r"(RPM-GPG-KEY|\.repo$)", n)]
    suite.record("IMG-06", "no repository files or signing keys", not keys, ", ".join(keys[:5]))
    suite.record("IMG-07", "no retrieval tool or compiler", not any(p in members for p in ABSENT if p.split("/")[-1] in ("curl", "wget", "gcc", "cc", "make")))
    suite.record("IMG-27", "no remote administration daemon", not any(p in members for p in ABSENT if p.split("/")[-1] in ("sshd", "ssh", "telnetd")))
    suite.record("IMG-11", "no su or sudo", not any(p in members for p in ("usr/bin/su", "usr/bin/sudo")))
    privileged = [n for n, m in members.items() if m.isfile() and m.mode & 0o6000]
    suite.record("IMG-09", "no setuid or setgid file", not privileged, ", ".join(privileged[:5]))
    writable = [n for n, m in members.items() if not m.issym() and m.mode & 0o002 and n != "tmp"]
    suite.record("IMG-09", "nothing world-writable outside /tmp", not writable, ", ".join(writable[:5]))
    protected = [n for n in members if n == "usr/sbin/nginx" or n.startswith("etc/nginx/")]
    loose = [n for n in protected if members[n].uid != 0 or (not members[n].issym() and members[n].mode & 0o022)]
    suite.record("IMG-10", "software and configuration root-owned, not group- or world-writable", bool(protected) and not loose, ", ".join(loose[:5]))
    manifest = members.get("usr/share/reference-web-server/rpm-manifest.tsv")
    if manifest is None:
        suite.record("IMG-08", "package inventory present", False)
    else:
        body = archive.extractfile(manifest).read().decode()
        installed = {line.split("\t")[0] for line in body.splitlines()}
        missing = [r["nevra"] for r in LOCK["rpms"] if r["nevra"] not in installed]
        suite.record("IMG-08", "inventory is mode 0444", manifest.mode & 0o777 == 0o444, oct(manifest.mode))
        suite.record("IMG-08", "inventory covers every locked package", not missing, ", ".join(missing))
    bundles = [n for n in members if n.startswith("etc/pki/ca-trust/extracted/") and members[n].isfile()] + \
              [n for n in members if n.startswith("etc/pki/tls/certs/") and members[n].isfile()]
    suite.record("IMG-17", "the image adds no trust anchors", not bundles, ", ".join(bundles[:5]))
    log_files = [n for n, m in members.items() if n.startswith("var/log/") and m.isfile()]
    error_log = members.get("var/log/nginx/error.log")
    suite.record("IMG-19", "no log file in the image; the error log links to stderr",
                 not log_files and error_log is not None and error_log.issym() and error_log.linkname == "/dev/stderr")
    modules = [n for n in members if re.match(r"usr/(lib64|share)/nginx/modules/.+", n)]
    suite.record("IMG-07", "no dynamic module beyond those declared", sorted(modules) == sorted(FEATURES["dynamic_modules"]), ", ".join(modules))


def runtime_checks(suite: Suite) -> None:
    name = suite.start()
    code = suite.http(name, "http://127.0.0.1:8080/")
    suite.record("IMG-15", "serves under a read-only root with only the declared tmpfs", code == 200, str(code))

    processes = proc_status(suite, name)
    root = [p for p in processes if p["Uid"].split()[0] == "0"]
    suite.record("IMG-11", "no process runs as UID 0", bool(processes) and not root, str(root))
    caps = [p for p in processes if int(p["CapEff"], 16) != 0]
    suite.record("IMG-13", "every process has an empty effective capability set", bool(processes) and not caps, str(caps))
    nnp = [p for p in processes if p.get("NoNewPrivs") != "1"]
    suite.record("IMG-13", "every process has no_new_privs", bool(processes) and not nnp, str(nnp))
    seccomp = [p for p in processes if p.get("Seccomp") != "2"]
    suite.record("IMG-13", "every process runs under a seccomp filter", bool(processes) and not seccomp, str(seccomp))
    names = {p["Name"] for p in processes}
    suite.record("IMG-30", "running processes are the declared ones", names <= set(BEHAVIOUR["processes"]), str(sorted(names)))

    ports = listening_ports(suite, name)
    declared = {listener["port"] for listener in BEHAVIOUR["listeners"]}
    suite.record("IMG-14", "every listening socket is 1024 or above", bool(ports) and min(ports) >= 1024, str(sorted(ports)))
    suite.record("IMG-30", "listening sockets are declared", ports <= declared, str(sorted(ports)))

    write = suite.exec(name, "touch", "/usr/share/nginx/html/probe")
    suite.record("IMG-15", "a write to the root filesystem fails", write.returncode != 0, write.stderr.strip())
    config = suite.exec(name, "test", "-w", "/etc/nginx/nginx.conf")
    suite.record("IMG-10", "the runtime user cannot write configuration", config.returncode != 0)

    features = suite.exec(name, "/usr/sbin/nginx", "-V").stderr
    flags = sorted(set(f for f in re.findall(r"--with(?:out)?-[a-z0-9_]+(?:=dynamic)?", features)
                       if not f.startswith(("--with-cc-opt", "--with-ld-opt"))))
    suite.record("IMG-07", "built features equal the declaration", flags == FEATURES["configure_flags"],
                 str(sorted(set(flags) ^ set(FEATURES["configure_flags"]))))

    logs = suite.podman("logs", name).stdout + suite.podman("logs", name).stderr
    suite.record("IMG-19", "requests are logged to standard output", '"GET / HTTP' in logs)

    started = time.monotonic()
    stop = suite.podman("stop", "--time", "10", name)
    elapsed = time.monotonic() - started
    status = suite.podman("inspect", name, "--format", "{{.State.ExitCode}}").stdout.strip()
    suite.record("IMG-20", "stops cleanly within the timeout", stop.returncode == 0 and status == "0" and elapsed < 10,
                 "exit " + status + " after " + str(round(elapsed, 1)) + "s")


def arbitrary_uid(suite: Suite) -> None:
    # Any UID the image was not built for proves the point. This one fits the
    # 65,536 subordinate UIDs rootless Podman maps by default.
    try:
        name = suite.start(user="54321:0")
    except subprocess.CalledProcessError as error:
        suite.record("IMG-12", "serves under an arbitrary UID in group 0", False, error.stderr.strip()[-200:])
        return
    code = suite.http(name, "http://127.0.0.1:8080/")
    suite.record("IMG-12", "serves under an arbitrary UID in group 0", code == 200, str(code))


def user_namespace(suite: Suite) -> None:
    probe = suite.podman("run", "--rm", "--userns=auto", *RESTRICTED, "--tmpfs", TMPFS,
                         "--entrypoint", "/usr/bin/cat", suite.image, "/proc/self/uid_map")
    if probe.returncode != 0:
        suite.record("IMG-32", "runs in a user namespace", None, "user namespaces unavailable here: " + probe.stderr.strip()[:120])
        return
    first = probe.stdout.split()
    suite.record("IMG-32", "container UID 0 is not host UID 0", len(first) >= 2 and first[1] != "0", probe.stdout.strip())
    name = suite.start("--userns=auto")
    code = suite.http(name, "http://127.0.0.1:8080/")
    suite.record("IMG-32", "serves in a user namespace", code == 200, str(code))


def fails_closed(suite: Suite) -> None:
    missing = suite.podman("run", "--rm", *RESTRICTED, suite.image)
    output = missing.stdout + missing.stderr
    suite.record("IMG-15", "without the declared tmpfs it exits non-zero naming the path",
                 missing.returncode != 0 and "/tmp/" in output, output.strip()[-160:])

    with tempfile.TemporaryDirectory() as scratch:
        broken = Path(scratch) / "broken.conf"
        broken.write_text("server { listen 8081 \n}\n")
        result = suite.podman("run", "--rm", *RESTRICTED, "--tmpfs", TMPFS,
                              "--volume", str(broken) + ":/etc/nginx/conf.d/broken.conf:ro,Z", suite.image)
        output = result.stdout + result.stderr
        suite.record("IMG-18", "invalid configuration exits non-zero naming the file and line",
                     result.returncode != 0 and "broken.conf:" in output, output.strip()[-160:])


def tls(suite: Suite) -> None:
    with tempfile.TemporaryDirectory() as scratch:
        work = Path(scratch)
        (work / "tls").mkdir()
        # Mounted the way a platform mounts a secret for an arbitrary UID in
        # group 0: readable by the group, not by others (ADR-0003, amended).
        suite.podman("run", "--rm", "--volume", str(work / "tls") + ":/out:Z", PROBE, "bash", "-euc",
                     "openssl req -x509 -newkey rsa:2048 -nodes -days 1 -subj /CN=reference-web-server "
                     "-keyout /out/server.key -out /out/server.crt 2>/dev/null; "
                     "chown 0:0 /out/server.key /out/server.crt; chmod 0640 /out/server.key; chmod 0644 /out/server.crt",
                     check=True)
        (work / "tls.conf").write_text(
            "server {\n    listen 8443 ssl;\n    ssl_certificate /etc/nginx/tls/server.crt;\n"
            "    ssl_certificate_key /etc/nginx/tls/server.key;\n    ssl_protocols TLSv1.2 TLSv1.3;\n"
            "    root /usr/share/nginx/html;\n}\n")
        key = (work / "tls" / "server.key").read_text()
        secret = "".join(line for line in key.splitlines() if "PRIVATE KEY" not in line)[:64]
        name = suite.start("--volume", str(work / "tls") + ":/etc/nginx/tls:ro,Z",
                           "--volume", str(work / "tls.conf") + ":/etc/nginx/conf.d/tls.conf:ro,Z")
        code = suite.http(name, "https://127.0.0.1:8443/", insecure=True)
        suite.record("IMG-16", "serves TLS from read-only mounted key material", code == 200, str(code))
        writable = suite.exec(name, "test", "-w", "/etc/nginx/tls/server.key")
        suite.record("IMG-16", "the key is not writable by the runtime identity", writable.returncode != 0)
        leaks = []
        for pid in [p for p in suite.exec(name, "ls", "/proc").stdout.split() if p.isdigit()]:
            if secret in suite.exec(name, "cat", "/proc/" + pid + "/cmdline").stdout:
                leaks.append("cmdline of " + pid)
        if secret in suite.exec(name, "cat", "/proc/1/environ").stdout:
            leaks.append("environment of PID 1")
        logs = suite.podman("logs", name)
        if secret in logs.stdout + logs.stderr:
            leaks.append("logs")
        suite.record("IMG-16", "no key material in arguments, environment, or logs", not leaks, ", ".join(leaks))
        ports = listening_ports(suite, name)
        declared = {listener["port"] for listener in BEHAVIOUR["listeners"]}
        suite.record("IMG-30", "with TLS mounted, listening sockets are still declared", ports <= declared, str(sorted(ports)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("image")
    parser.add_argument("--evidence", type=Path, default=HERE / "evidence" / "smoke.json")
    parser.add_argument("--revision", help="the commit the image must be labelled with")
    args = parser.parse_args()

    suite = Suite(args.image)
    try:
        static_checks(suite, args.revision)
        runtime_checks(suite)
        arbitrary_uid(suite)
        user_namespace(suite)
        fails_closed(suite)
        tls(suite)
    finally:
        suite.cleanup()

    digest = suite.podman("image", "inspect", args.image, "--format", "{{.Digest}}").stdout.strip()
    version = suite.podman("version", "--format", "{{.Client.Version}}").stdout.strip()
    failed = [r for r in suite.results if r["passed"] is False]
    skipped = [r for r in suite.results if r["passed"] is None]
    args.evidence.parent.mkdir(parents=True, exist_ok=True)
    args.evidence.write_text(json.dumps({
        "image": args.image, "digest": digest, "podman": version,
        "passed": len(suite.results) - len(failed) - len(skipped), "failed": len(failed), "skipped": len(skipped),
        "results": suite.results,
    }, indent=2) + "\n", encoding="utf-8")
    print(str(len(suite.results) - len(failed) - len(skipped)) + " passed, " + str(len(failed)) + " failed, "
          + str(len(skipped)) + " skipped; evidence in " + str(args.evidence))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
