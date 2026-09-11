"""Illustrative twin of the Report Generation agent — the 18-section envelope with the six blocks mapped in."""
from __future__ import annotations

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

from ._common import BODY, H2, KPI, SAMPLES, build, grid_table, kv_table, load_payloads


def main() -> None:
    p = load_payloads()["report_generation"]
    c = p["cover"]
    story = [
        Paragraph(f"{c['verdict']} · grade {c['investment_grade']} · entry {c['entry_bid']:,} · SIGNAL$ Max Bid {c['shapira_max_bid']:,} · equity at ceiling {c['equity_at_ceiling']:,}", KPI), Spacer(1, 6),
        Paragraph("Cover", H2),
        kv_table([("Subject", c["property_address"]), ("County / case / parcel", f"{c['county']} · {c['case_number']} · {c['parcel_id']}"),
                  ("Sale", f"{c['sale_type']} · {c['auction_date']}"), ("Certification", c["cert_status"])]),
        Paragraph("Executive summary", H2),
        kv_table([("Status", p["executive_summary"]["status"])]),
        Paragraph("The 18 sections (live render contract order)", H2),
        grid_table(["§", "Section", "Status", "Detail"],
                   [[s["label"], s["title"], s["status"].upper(), s.get("data", {})] for s in p["sections"]],
                   [0.55 * inch, 2.4 * inch, 1.05 * inch, 2.7 * inch]),
        Paragraph("Six-block map (a customer asking for a branded report gets these — plus the bid)", H2),
        grid_table(["Block", "SIGNAL$ sections"], [[k, ", ".join(v)] for k, v in p["attom_block_map"].items()], [2.2 * inch, 4.5 * inch]),
        Paragraph("Provenance & honest limits", H2),
        kv_table([("Effective date", p["provenance"]["effective_date"]), ("Sources", p["provenance"]["sources"]), ("Model disclosure", p["provenance"]["model_disclosure"]),
                  ("Snapshot sha256", p["provenance"]["snapshot_sha256"]), ("Pending / withheld / unresolved", p["provenance"]["honesty"]),
                  ("Vendor-name mentions in customer copy", p["provenance"]["trademark_check"]["attom_mentions"])]),
        Spacer(1, 4), Paragraph("Formats: " + ", ".join(p["formats"]) + ". Production render is pdf.js + S5Report.tsx; this page shows the envelope only.", BODY),
    ]
    out = build(SAMPLES / "SIGNAL_twin_Report_Generation_SAMPLE.pdf", "SIGNAL$ twin — Report Generation (illustrative)",
                "18 sections · six blocks mapped in · BidDeed.AI + ZoneWise.AI · fictional subject", story)
    print(out)


if __name__ == "__main__":
    main()
