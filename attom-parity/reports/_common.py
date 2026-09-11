"""
Shared PDF primitives for the three ILLUSTRATIVE ATTOM-twin sample reports.

These generators are bake-off scaffolding only. Production SIGNAL$ rendering
stays on pdf.js (PDF) and S5Report.tsx (HTML) — never fork a renderer.

Palette = biddeed.ai SSOT (scripts/palette-gate.mjs, biddeed-web main):
  #FFFFFF bg · #E6F0FA tint · #1A1A1A ink · #0A2540 navy · #D7E3F1 border ·
  #005EB8 brand · #004A92 brand hover. Nothing else.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

BG, TINT, INK, NAVY, BORDER, BRAND, BRAND_HOVER = (
    colors.HexColor("#FFFFFF"), colors.HexColor("#E6F0FA"), colors.HexColor("#1A1A1A"),
    colors.HexColor("#0A2540"), colors.HexColor("#D7E3F1"), colors.HexColor("#005EB8"), colors.HexColor("#004A92"),
)

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = ROOT / "samples"
NOTICE = ("ILLUSTRATIVE SAMPLE — fictional subject and numbers. Not official output of any data vendor, "
          "not licensed third-party data, not a BidDeed.AI underwriting. Do not underwrite from this document.")

H1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=NAVY, spaceAfter=4)
H2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=BG, backColor=NAVY,
                    leftIndent=0, borderPadding=(4, 6, 4, 6), spaceBefore=10, spaceAfter=6)
BODY = ParagraphStyle("body", fontName="Helvetica", fontSize=9, leading=12, textColor=INK)
MUTED = ParagraphStyle("muted", parent=BODY, fontSize=7.5, leading=10, textColor=colors.HexColor("#0A2540"))
NOTE = ParagraphStyle("note", parent=BODY, fontSize=7.5, leading=10, textColor=BRAND_HOVER, backColor=TINT, borderPadding=(4, 6, 4, 6))
KPI = ParagraphStyle("kpi", fontName="Helvetica-Bold", fontSize=13, leading=15, textColor=BRAND)


def load_payloads() -> dict[str, Any]:
    return json.loads((SAMPLES / "agent_payloads.json").read_text(encoding="utf-8"))


def fmt(v: Any) -> str:
    if v is None or v == "":
        return "Pending"
    if isinstance(v, bool):
        return "yes" if v else "no"
    if isinstance(v, (int, float)) and abs(v) >= 1000:
        return f"${v:,.0f}"
    if isinstance(v, float) and abs(v) < 1:
        return f"{v * 100:.1f}%"
    if isinstance(v, dict):
        return " · ".join(f"{k} {fmt(x)}" for k, x in v.items())
    if isinstance(v, list):
        return "; ".join(fmt(x) for x in v) if v else "None on file"
    return str(v)


def kv_table(rows: list[tuple[str, Any]], col=(2.1 * inch, 4.6 * inch)) -> Table:
    data = [[Paragraph(k, MUTED), Paragraph(fmt(v), BODY)] for k, v in rows]
    t = Table(data, colWidths=col)
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, BORDER),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    for i in range(0, len(data), 2):
        style.append(("BACKGROUND", (0, i), (-1, i), TINT))
    t.setStyle(TableStyle(style))
    return t


def grid_table(header: list[str], rows: list[list[Any]], widths: list[float]) -> Table:
    data = [[Paragraph(h, ParagraphStyle("th", parent=MUTED, fontName="Helvetica-Bold")) for h in header]]
    data += [[Paragraph(fmt(c), BODY) for c in r] for r in rows]
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), TINT), ("LINEBELOW", (0, 0), (-1, 0), 0.8, NAVY),
        ("LINEBELOW", (0, 1), (-1, -1), 0.4, BORDER), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def build(path: Path, title: str, subtitle: str, story_body: list) -> Path:
    doc = SimpleDocTemplate(str(path), pagesize=LETTER, leftMargin=0.7 * inch, rightMargin=0.7 * inch,
                            topMargin=0.7 * inch, bottomMargin=0.7 * inch, title=title, author="BidDeed.AI + ZoneWise.AI")
    story = [Paragraph(title, H1), Paragraph(subtitle, MUTED), Spacer(1, 4), Paragraph(NOTICE, NOTE), Spacer(1, 8)] + story_body
    story += [Spacer(1, 10), Paragraph("BidDeed.AI (foreclosures) + ZoneWise.AI (tax deeds / zoning) — always measured together, always shipped together. "
                                       "Decision-support only; not investment, legal or title advice. Obtain independent legal advice and/or title insurance.", MUTED)]
    doc.build(story)
    return path
