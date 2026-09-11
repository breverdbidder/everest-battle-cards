# SIGNAL$ × ATTOM KPI parity — distressed AIaaS beat

**Scope:** every KPI family ATTOM's three Intelligence agents publish (Property & Place Insights · Data Analyst · Report Generation, announced 2026-08-18) mapped onto the SIGNAL$ Property Report (18 sections, BidDeed.AI + ZoneWise.AI, always paired).
**Renderers in scope:** `packages/biddeed-mcp/src/report/pdf.js` (PDF, canonical) and `zonewise-web/components/report/S5Report.tsx` (HTML twin). Composer: `composer.js`. Template SSOT: `public.s5_report_sections`.
**Status vocabulary:** HAVE · PARTIAL · GAP · OURS (no ATTOM twin) · DEFECT. Every PARTIAL/GAP names an owner lane. Nothing below is assumed — each status carries the query or file it was read from on 2026-09-11.
**Rule:** we absorb ATTOM's KPIs into our 18 sections; we do not become a national plant with a chat window. No national AVM. No licensed ATTOM data. ATTOM is never named in customer copy.

## A. Property & Place Insights agent → §1 §4 §5 §6 §8 §9-10 §11-14 §16

| # | ATTOM KPI family | SIGNAL$ section | Status | Evidence (2026-09-11) | Owner / closer lane |
|---|---|---|---|---|---|
| A1 | Identity: address, parcel/APN, legal, lat/lon, stable id | §1 subject, §9-10 record | **HAVE** (legal PARTIAL) | cover.property_address / parcel_id / case_number / coordinates render in both twins; legal description only via title snapshot `subject.legal_description` | stable id = `mca_id` + parcel_id + case_number + DOR co_no. Legal → title harvest lanes (#20255 + shards) |
| A2 | Ownership / vesting / occupancy / owner-since | §8, §16 | **PARTIAL** | owner of record (fl_parcels own_name) + homestead HAVE; vesting + owner-since from deed chain only where `title_search_snapshot` has a stack (25 live OR counties, 55 upcoming at parity); occupancy: no source | title lanes for vesting; occupancy = GAP by design (no homeowner data purchase; homestead is the printed proxy) |
| A3 | Characteristics: use, beds, baths, GLA, lot, year built, stories, construction | §9-10 | **HAVE** | property_record from DOR NAL; stories/construction not in NAL → prints Pending | none needed for auction GTM; print Pending, never infer |
| A4 | Value & tax: assessed, market, taxable, exemptions, tax amount, tax history, paid/delinquent | §1 §2-3 §16 tax block | **PARTIAL** | assessed/just HAVE; taxable + exemptions render in §16 tax block where snapshot exists; tax amount / history / paid-delinquent: **GAP** | **Lane C — tax collector (TaxSys) payment status**, feeds §16 CP3 and this row |
| A5 | Transaction history: prior sales, dates, prices, document types | §8 | **PARTIAL** | NAL gives last 2 sales (sale_prc1/yr1, sale_prc2/yr2); doc types + full chain only via title engine chain_of_title (status=delivered gate) | title harvest lanes; Tier 3 chain = Lane F |
| A6 | Neighborhood: income, owner-occupancy, appreciation context | §11-14 | **PARTIAL** | ACS 5-yr ZCTA LIVE (`context_layer_cache` acs_ok=4, last 2026-09-11 14:45Z): median income, ownership rate, poverty, median rent, population. Appreciation context: GAP (Layer 3 tables absent, see B1) | B1 lane |
| A7 | Environmental / flood / hazards | §11-14 | **HAVE** (flood) / GAP (other) | FEMA NFHL point query LIVE (fema_ok=5): zone, SFHA, BFE. Wind/wildfire/sinkhole/radon: not sourced | later; print "Pending — not sourced" |
| A8 | Nearby places / POI | §11-14 | **GAP** | nothing wired; composer has no POI field | **Lane D — OSM Overpass amenity radii** (free, no key): grocery, parks, medical, highway ramps, transit; 30-day cache like FEMA/ACS |
| A9 | Schools | §11-14 | **GAP** (by decision) | composer: `schools: {available:false, reason:'Pending — school layer not wired; source TBD'}`; GreatSchools is paid → rejected | **Lane E — NCES EDGE** public school points + SABS attendance boundaries (free federal); print school names + distance, no ratings |
| A10 | Maps / location intelligence | deal page, §9-10 | **PARTIAL** | biddeed.ai /deal/:county/:case renders aerial + parcel outline; PDF/HTML report has no map | static aerial thumbnail into §9-10 (Mapbox static or county PA aerial URL already on `aerial_tight_url`) |

## B. Data Analyst agent → §3 (two-layer CMA) · county clearing ratios · §12 outcomes · §18

| # | ATTOM KPI family | SIGNAL$ twin | Status | Evidence | Owner / closer lane |
|---|---|---|---|---|---|
| B1 | Home-price / appreciation series | CMA Layer 3 (`cma_layer3` in composer) | **GAP — REGRESSED** | composer.js references `cma_layer3` + `insurance_kpi`, but `public.live_market_metrics` and `public.insurance_premiums` **do not exist** (no table, no migration in `supabase_migrations.schema_migrations`) although #20115 was recorded as shipped 2026-09-07. Layer 3 renders Pending today | **Lane B1 — re-land #20115** (Zillow Research + Realtor.com research CSVs, ZIP→county→metro labelled); verify with `select count(*) from public.live_market_metrics` |
| B2 | Inventory / supply | Layer 3 | **GAP** | same as B1 | Lane B1 |
| B3 | Investor activity | §12 outcomes + buyer type | **OURS / PARTIAL** | 21,138 verified auction outcomes (tax_deed 15,396 + foreclosure 5,742); third-party vs plaintiff split; winner names from Bid History modal harvest (#19446) — fill still thin | outcome harvest lanes; Plaintiff Discount Index (plaintiff-discount.js, 11 composer refs) |
| B4 | Portfolio vs benchmark | — | **GAP (do not build)** | not an auction-GTM job | build only if a non-auction GTM needs it |
| B5 | Cross-market comparison | county clearing ratios | **OURS** | priors.js: median sold/assessed + sold/judgment per county, sale-type separated (tax deed 3.88 vs foreclosure 0.679 contamination fixed Aug 7); `auctions_summary_ssot()` 67 counties | keep; expose as `data_analyst` MCP tool |
| B6 | Charts | /radar calendar; report none | **PARTIAL** | radar calendar charts live; SIGNAL$ report has no chart | C7 generative UI (#19947); PDF sparkline of clearing ratio history |

## C. Report Generation agent → the 6 blocks inside our 18

| # | ATTOM block | SIGNAL$ | Status | Evidence | Lane |
|---|---|---|---|---|---|
| C1 | Executive Summary | cover KPI strip + verdict; §16 "Additional Comments" | **PARTIAL** | verdict/grade/max bid strip HAVE; narrative summary only for title (`title_analyst_summary`, #20270). No report-level narrative | **Lane G — one-paragraph report narrative** from the same facts (no LLM invention; template over verified fields) |
| C2 | Property Profile | §1 §8 §9-10 §16 | **HAVE** | | |
| C3 | Maps & Location Intelligence | §11-14 | **PARTIAL** | see A6–A10 | D, E, aerial |
| C4 | Comparable Sales | §4-7 | **HAVE + OURS** | Layer 1 distressed + Layer 2 retail (Patent Claim 7) | |
| C5 | Valuation Insights (AVM, confidence, rental estimate, history) | §2-3 | **HAVE + OURS** (rental PARTIAL, history GAP) | two bands with HIGH/MED/LOW confidence; rental: `rental_listings` 10,532 rows / 18 counties render on ZoneWise Comps tab, not in the report; historical values: GAP | rental line into §2-3; value history via NAL jv history is one query |
| C6 | Charts & Visualizations | — | **PARTIAL** | B6 | B6 |

## D. OURS — no ATTOM twin (the beat)

| Section | Status | Evidence | Note |
|---|---|---|---|
| §ML Shapira Models | **OURS — probability WITHHELD** | `shapira_model_validations` 2026-09-11: V4 prod OOT AUC **0.478 FC / 0.391 TD** (worse than chance); v5b candidate 0.63 FC / 0.885 TD, passed=false | print model_version + gate status; never print p until a validation row has passed=true. Rebuild #20240 |
| §ZW ZoneWise | OURS/PARTIAL | DOR land use + JV live; district per county PARTIAL | GIS mission #20246 |
| §15 Bid card | OURS HAVE | entry · SIGNAL$ Max Bid · walk-away · verdict; BID→REVIEW on junior-lien risk or low 3P probability | disclaimer seam stays |
| §16 Title + lien hierarchy | OURS/PARTIAL | 25 live OR counties; avg parity 30.8%; 55/1,890 upcoming at parity (1:29 PM ET); statute-cited survival; UNRESOLVED never guessed | 20 Turnstile counties deferred by Ariel |
| §18 Outcome writeback | OURS HAVE | outcome.js grades ceiling_call / value_band_call | harvest completeness governs |
| §17 sha256 snapshot | OURS/PARTIAL | `title_search_snapshots` versioned + sha256 (3 rows); no whole-report hash | small lane: hash the report JSON at purchase into s5_pdf_cache |

## E. Defects found while mapping (fix before "parity")

| # | Defect | Where | Fix |
|---|---|---|---|
| E1 | SSOT row `rehab_estimate` (§REHAB, sort 75, is_active=true) has **no renderer** in pdf.js (0 hits) or S5Report.tsx, and composer.js never emits `report.rehab` (0 hits) → paying customers see "no handler registered for section_key 'rehab_estimate'" | both twins | add an honest renderer ("Pending — rehab estimate engine not yet producing for this parcel") in both; golden test must compare against the LIVE template |
| E2 | S5Report.tsx `context_layers` reads `ctx.neighborhood` / `ctx.flood_zone` as strings; composer emits objects (`neighborhood.{median_income,ownership_rate,…}`, `fema.{zone,sfha,bfe}`) → HTML twin prints `[object Object]` and a permanent "FEMA not wired" | S5Report.tsx | mirror pdf.js context_layers (done in this PR) |
| E3 | S5Report.tsx `shapira_ml` hardcodes v14.0 text and the withheld logic is inverted (prints the withheld note only when a probability IS present) | S5Report.tsx | data-driven model_version; print p only when `ml.print_probability === true`, else WITHHELD with the gate named (done in this PR) |
| E4 | S5Report.tsx does not render `title_search` (§16 blocks 1-7b) — pdf.js does since #20254/#20270 | S5Report.tsx | port the block renderer (done in this PR) |
| E5 | Band colours in S5Report.tsx are the retired `#1E3A5F`/`#F59E0B` | S5Report.tsx | canon `#0A2540` / `#005EB8` (done in this PR) |

## F. Acceptance tests (a live Florida sale-day property must render ALL on one report)

1. ATTOM-equivalent profile + value + tax + history + comps.
2. Distressed comp set and retail ARV on the same page, spread named.
3. SIGNAL$ Max Bid, entry, walk-away, BID | REVIEW | SKIP.
4. ML block with model version; probability printed OR explicitly WITHHELD with the gate named.
5. Title stack classified with statutes; joinder failures = UNRESOLVED, never guessed.
6. ZoneWise district / DOR land use (or PARTIAL printed).
7. Provenance + effective date + sha256.
8. Zero ATTOM trademark in the customer PDF/HTML (`grep -ci attom` = 0).
9. A county/market question returns clearing ratio + outcome counts, not only an appreciation sentence.

## G. Do-not-build list

- No BuildingPermit / national LoanModel tables unless a non-auction GTM needs them.
- No national AVM; no "Shapira AVM" rename. Productize the two bands + the spread harder.
- No fourth renderer. No licensed ATTOM data. No ATTOM name in customer copy.
