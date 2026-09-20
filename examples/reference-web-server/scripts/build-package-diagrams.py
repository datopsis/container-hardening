#!/usr/bin/env python3
"""Draw this image, for its cyber package.

One diagram cannot carry an architecture. These are the kinds a reader of the
package needs, each generated from the same description so they cannot drift
apart in style:

- **context** and **data flow**: what crosses which trust boundary, and where
  data rests. The boundaries are the point: they say where something stops
  being trusted.
- **request** and **TLS handshake**: what happens in order, and where each
  control acts.
- **lifecycle**: how the container starts, is judged healthy, and stops.
- **deployment**: what the platform gives it, and what it may write.
- **network**: what listens, and what it may reach.
- **identity**: who the processes are, and what privilege they hold.

Each names the criteria and controls that act at that point. A control named
in more than one place is divided between them: no one of them satisfies it.

Usage:
    python scripts/build-package-diagrams.py            # regenerate
    python scripts/build-package-diagrams.py --check    # fail if one differs
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE.parent.parent / "scripts"))
from svg import MUTED, RENDERED, SVG  # noqa: E402

OUT = HERE / "package" / "diagrams"


def context() -> None:
    s = SVG(900, 420, "Context: the reference web server and what surrounds it",
            "Anonymous clients reach the image through the platform's ingress and network policy. The platform "
            "admits the image by verified digest, imposes its security context, and mounts content, an optional "
            "server block, and optional key material. The image serves HTTP, and writes its records to the standard "
            "streams, which the platform collects. Nothing else crosses into the container.")
    s.boundary(20, 16, 860, 250, "Trust boundary: the platform", "everything inside is what the platform admits and imposes")
    s.box(40, 60, 240, 90, "Clients", ["anonymous, unauthenticated", "HTTP, or HTTPS when mounted"])
    s.tag(40, 176, "AC-14, IA-2: nobody is identified")
    s.arrow(280, 105, 360, 105)
    s.text(320, 96, "requests", 11.5, fill=MUTED, anchor="middle")
    s.box(360, 60, 240, 90, "The image", ["nginx 1.26, UID 1001:0", "read-only root, one tmpfs"], key=True)
    s.tag(360, 176, "IMG-06 to IMG-20: what it is")
    s.arrow(600, 105, 680, 105)
    s.text(640, 96, "records", 11.5, fill=MUTED, anchor="middle")
    s.box(680, 60, 180, 90, "Log collection", ["standard streams", "kept by the platform"])
    s.tag(680, 176, "AU-9, PLT-09")
    s.box(360, 196, 240, 56, "Mounted in, read-only", ["content, server block, key"])
    s.arrow(480, 196, 480, 150)
    s.tag(620, 226, "PLT-06, IMG-16, IMG-17")
    s.box(40, 300, 380, 96, "Its supply chain, before any of this", [
        "locked inputs, hermetic build, signed index,", "attested provenance and bill of materials"])
    s.tag(40, 412, "IMG-01 to IMG-05, IMG-21, IMG-22, IMG-35")
    s.box(460, 300, 400, 96, "What never crosses in", [
        "no package manager, shell service, or admin path",
        "no outbound connection of its own; no secrets in env"])
    s.tag(460, 412, "IMG-07, IMG-27, IMG-30, AC-6")
    s.save("context.svg")


def data_flow() -> None:
    s = SVG(900, 520, "Data flow: what moves, and where it rests",
            "A client's request crosses the platform boundary into the container boundary, where an nginx worker "
            "reads content from the read-only root filesystem and writes temporary files to a tmpfs. The response "
            "returns to the client; access and error records leave on the standard streams. Key material, when "
            "mounted, is read but never written, and never reaches the records.")
    s.boundary(20, 16, 860, 300, "Trust boundary: the container", "what is inside is what the image shipped, plus what was mounted")
    s.box(40, 60, 170, 70, "Client", ["anonymous"])
    s.flow(210, 95, 300, 95, "request", above=True)
    s.process(390, 95, 90, 40, "nginx worker", ["parses, routes, serves"])
    s.tag(310, 158, "SI-10: malformed requests refused")
    s.flow(480, 95, 580, 95, "response", above=True)
    s.box(580, 60, 170, 70, "Client", ["same connection"])
    s.store(40, 200, 250, 70, "Content, read-only", ["/usr/share/nginx/html, mounted or shipped"])
    s.flow(290, 235, 340, 185, "reads", above=False, anchor="start")
    s.store(330, 280, 250, 60, "tmpfs /tmp", ["the only writable path"])
    s.store(620, 200, 250, 70, "Key material, read-only", ["/etc/nginx/tls, when TLS is mounted"])
    s.flow(620, 235, 480, 150, "reads at startup", above=False, anchor="end")
    s.tag(600, 300, "IA-5, IA-5(6), IMG-16: never written, never logged")
    s.box(40, 360, 300, 86, "Access and error records", ["standard output and standard error", "combined format; no log file"])
    s.flow(390, 135, 190, 360, "writes", above=False, anchor="end")
    s.tag(40, 468, "AU-2, AU-3, AU-12, IMG-19")
    s.box(560, 360, 310, 86, "What does not flow", ["no outbound connection of its own", "no key material into records or arguments"])
    s.tag(560, 468, "IMG-30: declared behaviour; SC-8 on the wire")
    s.save("data-flow.svg")


def request_sequence() -> None:
    s = SVG(900, 470, "Sequence: one HTTP request",
            "A client opens a connection to port 8080, sends a request, and the worker resolves it against the "
            "document root: it answers with the file, or 404, and never reaches outside the root. It writes one "
            "access record. A malformed request is refused before any of that, and an error discloses no version.")
    for x, title, subtitle in ((150, "Client", "anonymous"), (450, "nginx worker", "UID 1001, no capabilities"),
                               (750, "Filesystem", "read-only root")):
        s.lifeline(x, 20, 400, title, subtitle)
    s.message(150, 450, 120, "connect to 8080, send request", "IMG-14: unprivileged port")
    s.message(450, 450, 165, "parse; refuse if malformed", "SI-10")
    s.message(450, 750, 215, "resolve under the document root only", "AC-3, SC-5")
    s.message(750, 450, 255, "the file, or nothing", dashed=True)
    s.message(450, 150, 300, "200 with the file, or 404", "SI-11: no version disclosed", dashed=True)
    s.message(450, 450, 350, "write one access record to stdout", "AU-2, AU-3, AU-12")
    s.note(560, 380, 320, "What cannot happen here", [
        "no code of the caller's runs (SC-18)",
        "no write outside /tmp (IMG-15)",
        "no privilege is gained (IMG-13, AC-6)"])
    s.save("request-sequence.svg")


def tls_sequence() -> None:
    s = SVG(900, 450, "Sequence: TLS, when a deployment mounts it",
            "The deployment mounts a server block, a certificate, and a private key read-only. nginx reads them at "
            "startup and never writes them; it refuses a missing or empty key. A client then completes a TLS 1.2 or "
            "1.3 handshake on port 8443 and the request proceeds as any other. The image authenticates no client.")
    for x, title, subtitle in ((140, "Deployment", "mounts, read-only"), (450, "nginx", "at startup, then serving"),
                               (760, "Client", "verifies the certificate")):
        s.lifeline(x, 20, 380, title, subtitle)
    s.message(140, 450, 120, "mount server block, certificate, key", "PLT-06, IMG-16, ADR-0003")
    s.message(450, 450, 165, "read at startup; refuse if missing or empty", "IMG-18: fails closed")
    s.message(760, 450, 215, "ClientHello to 8443", "SC-8: in transit")
    s.message(450, 760, 260, "certificate; TLS 1.2 or 1.3", "SC-8(1), SC-13, SC-23", dashed=True)
    s.message(760, 450, 305, "request over the established connection", "IA-2: no client certificate is asked for")
    s.note(40, 350, 380, "What the image does not do", [
        "it does not issue, renew, or revoke the certificate (IA-5)",
        "it sets no cipher policy of its own; the mounted block does",
        "it makes no FIPS claim (SC-13, IA-7)"])
    s.save("tls-sequence.svg")


def lifecycle() -> None:
    s = SVG(900, 400, "Lifecycle: start, healthy, stop",
            "The container starts by running nginx in the foreground; if the declared tmpfs is missing, or the "
            "configuration does not parse, it exits non-zero naming what was wrong rather than running degraded. "
            "While it runs, the healthcheck parses the configuration; a readiness probe is the platform's. On "
            "SIGQUIT it finishes what it is serving and exits zero.")
    states = [
        (40, "Created", ["image admitted by digest", "security context imposed"], "PLT-01, PLT-02"),
        (270, "Running", ["nginx in the foreground", "workers as UID 1001:0"], "IMG-11, IMG-13"),
        (500, "Stopping", ["SIGQUIT: finish in flight", "grace period from the platform"], "IMG-20, PLT-11"),
        (730, "Stopped", ["exit 0", "records already collected"], "AU-9"),
    ]
    for x, title, lines, tags in states:
        s.box(x, 60, 170, 96, title, lines)
        s.tag(x, 176, tags)
        if x < 730:
            s.arrow(x + 170, 108, x + 230, 108)
    s.box(270, 220, 400, 70, "Healthcheck: nginx -t every 30s", [
        "proves the configuration parses, not that it answers"])
    s.tag(690, 255, "IMG-20")
    s.arrow(355, 220, 355, 156)
    s.note(40, 310, 500, "Where it fails closed instead of starting", [
        "the declared tmpfs is missing: exits non-zero, naming the path (IMG-15)",
        "a mounted server block does not parse: exits non-zero, naming file and line (IMG-18)"])
    s.save("lifecycle.svg")


def deployment() -> None:
    s = SVG(900, 470, "Deployment: what the platform gives it, and what it may write",
            "The platform runs the image under a restricted security context, with a read-only root filesystem and "
            "one writable tmpfs on /tmp. Content, an optional server block, and optional key material are mounted "
            "read-only. Everything else the image needs it already carries.")
    s.boundary(20, 16, 860, 270, "The pod, as the platform runs it")
    s.box(40, 60, 250, 130, "Security context", [
        "runAsNonRoot, arbitrary UID", "allowPrivilegeEscalation: false",
        "capabilities: drop ALL", "readOnlyRootFilesystem: true", "seccomp: RuntimeDefault"])
    s.tag(40, 210, "PLT-02, IMG-11 to IMG-13, IMG-31")
    s.box(320, 60, 250, 130, "The container", [
        "nginx 1.26 on UBI 9 Micro", "listens 8080, and 8443 with TLS",
        "writes only under /tmp", "logs to the standard streams"], key=True)
    s.tag(320, 210, "IMG-14, IMG-15, IMG-19")
    s.box(600, 60, 260, 130, "Mounted in", [
        "content -> /usr/share/nginx/html", "server block -> /etc/nginx/conf.d",
        "certificate and key -> /etc/nginx/tls", "all read-only; key 0640 root:0"])
    s.tag(600, 210, "PLT-06, IMG-16, IMG-17, ADR-0003")
    s.box(40, 300, 400, 96, "Writable: exactly one path", [
        "tmpfs /tmp, rw, noexec, nosuid, nodev, 16m",
        "nginx's pid file and its temporary paths live there"])
    s.tag(40, 416, "IMG-15, IMG-10: nothing else is writable")
    s.box(470, 300, 390, 96, "Not given, and not needed", [
        "no persistent volume; the image stores nothing",
        "no service account token, no environment secrets"])
    s.tag(470, 416, "IMG-05, ADR-0003, SC-28: nothing at rest here")
    s.save("deployment.svg")


def network() -> None:
    s = SVG(900, 420, "Network: what listens, and what it reaches",
            "The image listens on 8080, and on 8443 when a deployment mounts TLS. It opens no outbound connection "
            "of its own: the declared behaviour lists no outbound destination, and the smoke suite reads the "
            "listening sockets back from /proc to confirm only the declared ports are open. Everything else is the "
            "platform's network policy.")
    s.box(40, 70, 220, 110, "Inbound", ["8080, HTTP", "8443, HTTPS when mounted", "both above 1024"])
    s.tag(40, 200, "IMG-14, IMG-30")
    s.arrow(260, 125, 340, 125)
    s.box(340, 70, 220, 110, "The image", ["one master, N workers", "no listener but the declared"])
    s.tag(340, 200, "IMG-30: declared behaviour")
    s.box(640, 70, 220, 110, "Outbound", ["none of its own", "no upstream, no telemetry"])
    s.arrow(560, 125, 640, 125)
    s.tag(640, 200, "IMG-30, PLT-10")
    s.box(40, 250, 820, 90, "What decides who may reach it", [
        "network policy, deny by default in both directions, and the service or ingress in front of it",
        "mutual authentication between services, where the platform provides it"], key=True)
    s.tag(40, 360, "PLT-10, PLT-18: the platform's half; the image imposes none of it")
    s.save("network.svg")


def identity() -> None:
    s = SVG(900, 430, "Identity and privilege: who the processes are",
            "Every process runs as the numeric, non-root user the image declares, or any arbitrary UID the platform "
            "assigns, always in group 0 so mounted files remain readable. No process holds a capability, none may "
            "gain privilege, and there is no su, sudo, or login path in the image at all.")
    s.box(40, 60, 260, 120, "The runtime identity", [
        "USER 1001:0 as declared", "or any arbitrary UID, group 0",
        "no login shell, no password", "no su, no sudo in the image"])
    s.tag(40, 200, "IMG-11, IMG-12, AC-6(5)")
    s.box(330, 60, 260, 120, "What it may do", [
        "read its configuration and content", "write under /tmp only",
        "bind 8080 and 8443", "nothing else"])
    s.tag(330, 200, "AC-3, AC-6, IMG-10, IMG-15")
    s.box(620, 60, 240, 120, "What it cannot do", [
        "gain privilege (no_new_privs)", "hold a capability (all dropped)",
        "escape seccomp or SELinux", "administer anything"])
    s.tag(620, 200, "IMG-13, IMG-27, AC-6(1) to AC-6(3)")
    s.box(40, 250, 400, 90, "Who the image authenticates", [
        "nobody: no accounts, no sessions, no credentials"])
    s.tag(40, 360, "AC-2, IA-2 and their enhancements: nothing to apply to")
    s.note(470, 250, 390, "This is the part that changes first", [
        "an image that verifies a token, terminates mutual TLS,",
        "or holds a client secret takes part in identity, and those",
        "controls become its own; see the inspection list"])
    s.save("identity.svg")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="fail if a committed diagram differs")
    args = parser.parse_args()
    for draw in (context, data_flow, request_sequence, tls_sequence, lifecycle, deployment, network, identity):
        draw()
    if args.check:
        stale = [name for name, body in RENDERED.items()
                 if not (OUT / name).exists() or (OUT / name).read_text(encoding="utf-8") != body]
        if stale:
            print("stale diagrams: " + ", ".join(sorted(stale)), file=sys.stderr)
            return 1
        print("the package diagrams are up to date (" + str(len(RENDERED)) + ")")
        return 0
    OUT.mkdir(parents=True, exist_ok=True)
    for name, body in RENDERED.items():
        (OUT / name).write_text(body, encoding="utf-8", newline="\n")
    print("wrote " + str(len(RENDERED)) + " diagrams to " + str(OUT.relative_to(HERE)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
