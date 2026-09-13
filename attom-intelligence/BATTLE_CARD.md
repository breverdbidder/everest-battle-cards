# Battle card — ATTOM Intelligence vs SIGNAL$ (BidDeed.AI + ZoneWise.AI)

**Internal document.** The vendor's name never appears in customer-facing copy. Customer-facing substitute: *"national property-data plants answer what the house is; we answer what you should bid."*
Prepared 2026-09-11 (Fri) 2:30 PM ET · **refreshed 2026-09-12 (Sat) 11:15 PM ET** to the shipped lane outcomes (statuses re-read from main + Supabase at refresh time) · sources: attomdata.com agent pages + the 2026-08-18 announcement (fetched today) · live SIGNAL$ state re-queried from Supabase mocerqjnksmhcjzxrewo.
Pairing rule: BidDeed.AI (foreclosures) + ZoneWise.AI (tax deeds / zoning) — always measured together, always shipped together.

## 1. Who they are (verified from their own pages)

- **ATTOM Intelligence** — announced 2026-08-18: three specialized AI agents on the ATTOM property plant, delivered through an MCP server, Agent2Agent (A2A), enterprise chat tools (Claude, ChatGPT), a self-service workbench, and existing AI applications. Coverage claim: 160+ million U.S. properties, 99% of the U.S. population.
- **Property & Place Insights Agent** — "Trusted Data. Complete Insights. Property Intelligence." Six published capability families: Ownership Intelligence · Property Details · Value & Tax Information · Neighborhood Insights · Environmental Intelligence · Nearby Places.
- **Data Analyst Agent** — "AI-Powered Market Intelligence Through Natural Language": natural-language queries, research-grade analysis, market trends / portfolio evaluation / region comparison, enterprise-ready, every response grounded exclusively in ATTOM data. Named verticals: mortgage, insurance, real estate, banks, technology/data platforms, consulting.
- **Report Generation Agent** — six blocks: Executive Summary · Property Profile · Maps & Location Intelligence · Comparable Sales · Valuation Insights (AVMs, confidence scores, rental estimates, historical values) · Charts & Visualizations. "Customer-ready" reports "in seconds."
- **Pricing / access:** none published. Demo-request and contact-sales CTAs only — an enterprise data contract, not a $25 checkout.
- **Distressed:** the word "foreclosure" appears once, in the boilerplate company description. Zero mention of auctions, tax deeds, liens, lien survival, title, bidding, or zoning in the agent pages or the announcement.
- **Catalog recon (Grok, Sep 11):** ~76 tables in the cloud catalog; PropertyFeature ~249 fields; RETransaction ~219 fields; stable identity key ATTOM ID; geoId / geoIdV4 joins.

## 2. Where we stand today (live, not assumed)

| | ATTOM Intelligence | SIGNAL$ Property Report |
|---|---|---|
| Job | *what the house is* (any U.S. parcel) | *what to pay, which liens survive, what the dirt can become* (FL foreclosure + tax-deed auctions; nationwide is the roadmap, Florida the MVP) |
| Coverage | 160M+ U.S. properties | 10.5M FL parcels (67 counties); auction calendar 1,922 upcoming / 59 county slugs (Sep 12 6:39 AM ET); title engine 25 live OR counties |
| Price / access | enterprise contract, demo-gated | $25 one-time report · Investor $99 · Pro $199 · Pro Plus $399 · self-serve checkout |
| Speed | "in seconds" after onboarding | instant — pre-harvested T-14 / T-21 before the sale |
| Valuation | one AVM + confidence | TWO bands: distressed clearing band + retail ARV band; the spread is printed |
| Bid instruction | none | entry bid · SIGNAL$ Max Bid (net of surviving liens) · walk-away · BID / REVIEW / SKIP |
| Title / liens | none published | statute-cited lien hierarchy (§48.23 · §197.122 · §197.552 · §713.07 · §720.3085 · §718.116 · 26 USC §7425); joinder vs LP party list; UNRESOLVED never guessed |
| Zoning / envelope | none | ZoneWise §8: DOR land use, jurisdiction, district (or PENDING), envelope where built |
| Outcome loop | none | §18 post-sale writeback grades the report's own call |
| ML | none published | SIGNAL$ Models — tax deed PRINTS (td-soldvred-v1: OOT AUC 0.8625 vs 0.4841, n_test 1,624, verified outcomes); foreclosure **WITHHELD** in all three renderers (V4 prod 0.478; v5b 0.63; candidate fc-sold3p-po-v1 0.8765 vs 0.8291 on derived labels fails the DB +0.10 rule, passed=false, not wired — K6, owner decision) |
| Delivery | MCP + A2A + chat + workbench | mcp.biddeed.ai (36 tools / 7 streams) + HTML + PDF + JSON; A2A: not yet |
| Provenance | "grounded exclusively in ATTOM data" | every dollar carries a source; effective date; versioned title snapshot with sha256 |

## 3. Where they win (say it plainly)

1. **Density of context** — national coverage, non-flood hazards (K13, by decision), occupancy (K14, by design — no homeowner-data purchase), construction details not in the DOR roll. Schools (nearest + assigned), POI, aerial, rental estimate, value history, charts and the executive summary shipped Sep 11–12 and are no longer theirs.
2. **Live-market series** — appreciation, inventory, DOM. Layer 3 re-landed Sep 11 (live_market_metrics 12,775 rows · insurance_premiums 5,452); HAVE the first time it prints on a real report (K5 — no render since Sep 11 12:17 PM ET).
3. **A2A + workbench** — we have MCP only.
4. **Tax amount / delinquency** — Lane C shipped but every county tax-collector fetch is Turnstile-walled (66 attempts, 0 ok); prints "Pending — tax collector not reachable" (K1, route decision open).

## 4. Where we win (and must keep winning)

1. **The bid.** A number a bidder can take to the courthouse, already net of surviving liens, with the walk-away and the verdict on the page.
2. **The lien hierarchy.** Position + statute + joinder, per instrument, with UNRESOLVED as a first-class answer.
3. **Two-layer CMA + county clearing ratios** on verified auction outcomes (sold-to-assessed, sold-to-judgment, third-party share) — a distressed market question is answered with counts, not a housing chart.
4. **ZoneWise pairing** — what the dirt can become, on the same page as the bid.
5. **Outcome writeback** — the report grades itself after the sale.
6. **$25 and instant.** The customer ATTOM will not onboard.

## 5. Positioning lines

- Internal: *ATTOM gives a national property plant a chat window. SIGNAL$ gives a Florida bidder a number they can take to the auction and a statute for every lien that number already subtracted.*
- Customer-facing (no vendor name): *National property-data plants answer what the house is. We answer what you should bid.*

## 6. Rules

- Absorb their KPIs into our 18 sections; never become a national plant with a chat window.
- Never delete moat sections to look like six blocks; map six into eighteen.
- No licensed ATTOM data; samples are fictional reconstructions.
- No national AVM; no "Shapira AVM" rename.
- Every bid number ships behind the existing legal disclaimer.
- If a field is not live, print Pending / UNRESOLVED / WITHHELD. That is the feature.

## 7. Refresh protocol (Grok-owned once write access exists)

Re-crawl the three agent pages + announcement monthly or on any ATTOM press release; diff against §1; update `docs/KPI_PARITY_MATRIX.md` when a SIGNAL$ section moves PARTIAL → HAVE; keep `attom-intelligence/index.html` on everest-battle-cards in sync; never rewrite S5Report.tsx or pdf.js from the CI lane.
