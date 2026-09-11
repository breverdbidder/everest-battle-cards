"""Illustrative twin of the Data Analyst agent — market / county aggregates, distressed first."""
from __future__ import annotations

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

from ._common import BODY, H2, KPI, SAMPLES, build, grid_table, kv_table, load_payloads


def main() -> None:
    p = load_payloads()["data_analyst"]
    sc, d, r, lm = p["scope"], p["distressed"], p["retail"], p["live_market"]
    story = [
        Paragraph(f"{sc['geography']} county · {sc['sale_type']} · {d['n_outcomes']} verified outcomes since {sc['since']} · confidence {d['confidence']}", KPI), Spacer(1, 6),
        Paragraph("Distressed clearing statistics (the beat)", H2),
        kv_table([("Median sold-to-assessed", d["median_sold_to_assessed"]), ("Median sold-to-judgment", d["median_sold_to_judgment"]),
                  ("Third-party share of sold lots", d["third_party_share"]), ("Upcoming auctions", d["n_upcoming"]), ("Min n for confidence", d["min_n_for_confidence"])]),
        Paragraph("Plaintiff Discount Index", H2),
        grid_table(["Plaintiff", "Median sold / judgment", "n"], [[x["plaintiff"], x["median_sold_to_judgment"], x["n"]] for x in d["plaintiff_discount_index"]],
                   [3.6 * inch, 1.8 * inch, 1.3 * inch]),
        Paragraph("Retail (Layer 2) sale statistics", H2),
        kv_table([("Arm's-length sales since", f"{r['n_sales']} since {r['since_year']}"), ("Median sale price", r["median_sale_price"]), ("Median $/sqft", r["median_price_per_sqft"])]),
        Paragraph("Live market (Layer 3)", H2),
        kv_table([("Status", lm["reason"] if not lm["available"] else "delivered")]),
        Paragraph("Cross-market comparison", H2),
        grid_table(["Geography", "Median sold-to-assessed", "n outcomes", "Confidence"],
                   [[c["geography"], c["median_sold_to_assessed"], c["n_outcomes"], c.get("confidence", d["confidence"])] for c in p["comparison"]],
                   [2.4 * inch, 1.8 * inch, 1.2 * inch, 1.3 * inch]),
        Paragraph("Provenance", H2),
        kv_table([("Sources", p["provenance"]["sources"]), ("Pending / low-confidence", p["provenance"]["honesty"])]),
        Spacer(1, 4), Paragraph("A county question answers with clearing ratio + outcome counts. An appreciation sentence alone is not an answer.", BODY),
    ]
    out = build(SAMPLES / "SIGNAL_twin_Data_Analyst_SAMPLE.pdf", "SIGNAL$ twin — Data Analyst (illustrative)",
                "County aggregates · distressed vs retail · BidDeed.AI + ZoneWise.AI", story)
    print(out)


if __name__ == "__main__":
    main()
