"""Illustrative twin of the Property & Place Insights agent — single-parcel Q&A shape."""
from __future__ import annotations

from reportlab.platypus import Paragraph, Spacer

from ._common import BODY, H2, KPI, SAMPLES, build, kv_table, load_payloads


def main() -> None:
    p = load_payloads()["property_place_insights"]
    ident, own, ch, vt, tx, nb, env, prov = (p[k] for k in ("identity", "ownership", "characteristics", "value_and_tax", "transactions", "neighborhood", "environmental", "provenance"))
    sve = vt["signal_value_estimate"]
    story = [
        Paragraph(f"Verdict {sve['verdict']} · SIGNAL$ Max Bid {sve['signal_max_bid']:,} · spread {sve['spread']:,}", KPI), Spacer(1, 6),
        Paragraph("Identity", H2),
        kv_table([("Address", ident["address"]), ("County / parcel", f"{ident['county']} · {ident['parcel_id']}"), ("Legal", ident["legal_description"]),
                  ("Case / sale", f"{ident['stable_id']['case_number']} · {ident['sale_type']} · {ident['auction_date']}"), ("Lat / lon", f"{ident['lat']}, {ident['lon']}")]),
        Paragraph("Ownership", H2),
        kv_table([("Owner of record", own["owner_of_record"]), ("Homestead", own["homestead_status"]), ("Vesting per appraiser", own["vesting_per_appraiser"]),
                  ("Owner since", own["owner_since"]), ("Occupancy", own["occupancy"])]),
        Paragraph("Characteristics", H2),
        kv_table([("Type / DOR use", f"{ch['property_type']} · {ch['dor_land_use']}"), ("Beds / baths / GLA", f"{ch['beds']} / {ch['baths']} / {ch['living_area_sqft']} sqft"),
                  ("Lot / year built", f"{ch['lot_size_acres']} ac · {ch['year_built']}"), ("Stories", ch["stories"]), ("Construction", ch["construction"])]),
        Paragraph("Value & tax", H2),
        kv_table([("Just / assessed / taxable", f"{vt['just_value']:,} / {vt['assessed_value']:,} / {vt['taxable_value']:,}"), ("Exemptions", vt["exemptions"]),
                  ("Tax amount / status", f"{vt['tax_amount']} · {vt['tax_payment_status']}"),
                  ("SIGNAL$ clearing band", sve["clearing_band"]), ("SIGNAL$ retail ARV band", sve["market_band"])]),
        Paragraph("Transactions", H2),
        kv_table([(s["date"], f"{s['price']:,} · {s['doc_type']} · {s['source']}") for s in tx["prior_sales"]] + [("Chain of title", tx["chain_of_title_status"])]),
        Paragraph("Neighborhood · environmental · nearby", H2),
        kv_table([("Median income / ownership / poverty", f"{nb['median_income']:,} · {nb['ownership_rate']:.0%} · {nb['poverty_rate']:.0%} — {nb['source']}"),
                  ("Median rent / population", f"{nb['median_rent']:,} · {nb['population']:,}"), ("Appreciation", nb["appreciation"]),
                  ("Flood", env["flood"]), ("Other hazards", env["other_hazards"]),
                  ("Nearby places", p["nearby_places"]["reason"]), ("Schools", p["schools"]["reason"])]),
        Paragraph("Provenance & honest limits", H2),
        kv_table([("Sources", prov["sources"]), ("Pending / withheld", prov["honesty"])]),
        Spacer(1, 4), Paragraph("Every Pending line above is a lane in docs/KPI_PARITY_MATRIX.md, not a guess.", BODY),
    ]
    out = build(SAMPLES / "SIGNAL_twin_Property_Place_Insights_SAMPLE.pdf", "SIGNAL$ twin — Property & Place Insights (illustrative)",
                "One-parcel Q&A shape · BidDeed.AI + ZoneWise.AI · fictional subject", story)
    print(out)


if __name__ == "__main__":
    main()
