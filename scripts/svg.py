#!/usr/bin/env python3
"""A small SVG builder for generated diagrams.

Shared so the standard's diagrams and an image's own package diagrams look
alike and are written the same way: no dependency, one style, a <title> and
<desc> on every diagram for screen readers, and its own light background so it
reads the same in a light or dark viewer.

Beyond boxes and arrows it carries the shapes the other kinds of diagram need:
a dashed boundary for a trust boundary, an ellipse for a process and an open
store for data in a data-flow diagram, and lifelines and messages for a
sequence.
"""

from __future__ import annotations

from xml.sax.saxutils import escape

# Every diagram a run has rendered, by file name; the caller writes them out.
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

    def boundary(self, x, y, w, h, label, note=None):
        """A trust boundary: what crosses this line is not trusted the same on both sides."""
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" stroke="{KEY_EDGE}" '
            'stroke-width="1.5" stroke-dasharray="7 5"/>'
        )
        self.text(x + 12, y + 20, label, 12.5, "600", fill=KEY_EDGE)
        if note:
            self.text(x + w - 12, y + 20, note, 11.5, fill=KEY_EDGE, anchor="end", italic=True)

    def process(self, cx, cy, rx, ry, title, lines=()):
        """A process in a data-flow diagram: something that acts on data."""
        self.parts.append(
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{BOX}" stroke="{BOX_EDGE}"/>'
        )
        top = cy - (len(lines) * 16) / 2
        self.text(cx, top + 5, title, 13, "600", anchor="middle")
        for i, line in enumerate(lines):
            self.text(cx, top + 23 + i * 16, line, 11.5, fill=MUTED, anchor="middle")

    def store(self, x, y, w, h, title, lines=()):
        """A data store: open at the sides, as data-flow diagrams draw one."""
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{BOX}" stroke="none"/>')
        for edge in (y, y + h):
            self.parts.append(f'<line x1="{x}" y1="{edge}" x2="{x + w}" y2="{edge}" stroke="{BOX_EDGE}" stroke-width="1.5"/>')
        self.text(x + 12, y + 21, title, 13, "600")
        for i, line in enumerate(lines):
            self.text(x + 12, y + 40 + i * 16, line, 11.5, fill=MUTED)

    def flow(self, x1, y1, x2, y2, label, above=True, anchor="middle"):
        """A labelled data flow."""
        self.arrow(x1, y1, x2, y2)
        self.text((x1 + x2) / 2, (y1 + y2) / 2 + (-8 if above else 18), label, 11.5, fill=MUTED, anchor=anchor)

    def lifeline(self, x, y, height, title, subtitle=None):
        """A participant in a sequence, and the line beneath it."""
        self.box(x - 90, y, 180, 44 if not subtitle else 52, title, subtitle=subtitle)
        top = y + (44 if not subtitle else 52)
        self.parts.append(
            f'<line x1="{x}" y1="{top}" x2="{x}" y2="{y + height}" stroke="{LINE}" stroke-width="1.5" '
            'stroke-dasharray="4 4"/>'
        )

    def message(self, x1, x2, y, label, tag=None, dashed=False):
        """One message in a sequence, left to right or back."""
        dash = ' stroke-dasharray="5 4"' if dashed else ""
        self.parts.append(
            f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{MUTED}" stroke-width="1.5" '
            f'marker-end="url(#a)"{dash}/>'
        )
        self.text((x1 + x2) / 2, y - 8, label, 11.5, anchor="middle")
        if tag:
            self.tag((x1 + x2) / 2, y + 16, tag, anchor="middle")

    def note(self, x, y, w, text, lines=()):
        """A note beside something, for what a diagram cannot draw."""
        height = 30 + len(lines) * 16
        self.parts.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{height}" rx="6" fill="#fff8c5" stroke="#d4a72c"/>'
        )
        self.text(x + 12, y + 20, text, 12, "600")
        for i, line in enumerate(lines):
            self.text(x + 12, y + 38 + i * 16, line, 11.5, fill=MUTED)

    def save(self, name):
        self.parts.append("</svg>")
        RENDERED[name] = "\n".join(self.parts) + "\n"
