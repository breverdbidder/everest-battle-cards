# biddeed-attom-parity

SIGNAL$ Property Report parity kit against ATTOM Intelligence's three agents (Property & Place Insights · Data Analyst · Report Generation, announced 2026-08-18) — and the beat on the only vertical that matters: Florida foreclosure + tax-deed auctions (BidDeed.AI + ZoneWise.AI, always paired).

**This kit maps onto production. It never forks it.** Production rendering is `pdf.js` + `S5Report.tsx` reading `public.s5_report_sections`; the live tools are at https://mcp.biddeed.ai.

```
schemas/   property_place_insights.json · data_analyst.json · report_generation.json · signals_18_section.json
mcp/       tools.py (7-tool stable registry) · server.py (stdio stub; forwards live when BIDDEED_MCP_URL/KEY are set)
reports/   illustrative ATTOM-twin PDF generators (reportlab) — bake-off scaffolding only
samples/   agent_payloads.json (fictional subject) + 3 illustrative PDFs
docs/      BATTLE_CARD.md · KPI_PARITY_MATRIX.md · ECOSYSTEM.md · PRIVATE_REPO_HANDOFF.md
```

Quick start

```bash
pip install reportlab mcp
python -m reports.property_place_insights && python -m reports.data_analyst && python -m reports.report_generation
python -m mcp.server --list
python -m mcp.server --call score_deal '{"county":"sample","case_number":"2026-CA-000000"}'
```

Rules: no licensed ATTOM data · no vendor name in customer copy · no national AVM · print Pending / UNRESOLVED / WITHHELD in-line · palette = biddeed.ai SSOT (#FFFFFF #E6F0FA #1A1A1A #0A2540 #D7E3F1 #005EB8 #004A92).

Board of record: the KPI parity issue in cli-anything-biddeed (linked from `docs/KPI_PARITY_MATRIX.md`).
