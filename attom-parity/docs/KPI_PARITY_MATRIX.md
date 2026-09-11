# SIGNAL$ × ATTOM KPI parity — distressed AIaaS beat

**Scope:** every KPI family ATTOM's three Intelligence agents publish (Property & Place Insights · Data Analyst · Report Generation, announced 2026-08-18) mapped onto the SIGNAL$ Property Report (18 sections, BidDeed.AI + ZoneWise.AI, always paired).
**Renderers in scope:** `packages/biddeed-mcp/src/report/pdf.js` (PDF, canonical) and `zonewise-web/components/report/S5Report.tsx` (HTML twin). Composer: `composer.js`. Template SSOT: `public.s5_report_sections`.
**Status vocabulary:** HAVE · PARTIAL · GAP · OURS (no ATTOM twin) · DEFECT. Every PARTIAL/GAP names an owner lane. Nothing below is assumed — each status carries the query or file it was read from on 2026-09-11.
**Board of record:** cli-anything-biddeed #20287 (lanes #20288 E1 · #20289 B1 · #20290 D · #20291 E · #20292 C · #20293 G). Title rebrand applied Sep 11 2026: SSOT band titles now "SIGNAL$ Bid Card" and "SIGNAL$ Models" (keys unchanged).
**Lane outcomes (verified on main + live tables, Sep 11 2026 4:50 PM ET, not from run badges — every cc-runner badge is red only on the pre-existing RLS-gate false-red):** E1 shipped b89233f9 · B1 shipped 50f92d72 · D shipped a993c776 (+ architect fix 2b22f957, defect E7) · E shipped 99c5aee4 · C shipped 4780ccb4 but **blocked at the collector wall** (0 of 66 fetches ok) · G shipped 7eba5097. Architect follow-ups: pdf.js E6 dfc8b87f, HTML twin 02a8938d (deployed to zonewise.ai).
**Rule:** we absorb ATTOM's KPIs into our 18 sections; we do not become a national plant with a chat window. No national AVM. No licensed ATTOM data. ATTOM is never named in customer copy.

## A. Property & Place Insights agent → §1 §4 §5 §6 §8 §9-10 §11-14 §16

| # | ATTOM KPI family | SIGNAL$ section | Status | Evidence (2026-09-11) | Owner / closer lane |
|---|---|---|---|---|---|
| A1 | Identity: address, parcel/APN, legal, lat/lon, stable id | §1 subject, §9-10 record | **HAVE** (legal PARTIAL) | cover.property_address / parcel_id / case_number / coordinates render in both twins; legal description only via title snapshot `subject.legal_description` | stable id = `mca_id` + parcel_id + case_number + DOR co_no. Legal → title harvest lanes (#20255 + shards) |
| A2 | Ownership / vesting / occupancy / owner-since | §8, §16 | **PARTIAL** | owner of record (fl_parcels own_name) + homestead HAVE; vesting + owner-since from deed chain only where `title_search_snapshot` has a stack (25 live OR counties, 55 upcoming at parity); occupancy: no source | title lanes for vesting; occupancy = GAP by design (no homeowner data purchase; homestead is the printed proxy) |
| A3 | Characteristics: use, beds, baths, GLA, lot, year built, stories, construction | §9-10 | **HAVE** | property_record from DOR NAL; stories/construction not in NAL → prints Pending | none needed for auction GTM; print Pending, never infer |
| A4 | Value & tax: assessed, market, taxable, exemptions, tax amount, tax history, paid/delinquent | §1 §2-3 §16 tax block | **PARTIAL** (tax amount / status: **GAP — BLOCKED at the collector wall**) | assessed/just HAVE; taxable + exemptions render in §16 tax block where snapshot exists. Lane C shipped 4780ccb4 (Sep 11 4:29 PM ET): `tax_collector_sources` 40 counties (RLS on, 0 anon), `tax_collector_results` 66 fetch attempts — **all `blocked`** (13 `cloudflare_turnstile_challenge`, rest headless-blocked), 0 ok; `title_search_snapshot.tax.payment_status` prints "Pending — tax collector not reachable (cloudflare_turnstile_challenge, verified 2026-09-11)"; CP3 statewide stays 0.86 | Grant Street TaxSys is Turnstile-walled to headless runners (same wall as the 20 deferred title counties). No proxy / captcha bypass by rule. Candidate non-scraping route: published delinquent-tax lists (annual, PDF/CSV per county) → delinquent yes/no only. Decision, not code |
| A5 | Transaction history: prior sales, dates, prices, document types | §8 | **PARTIAL** | NAL gives last 2 sales (sale_prc1/yr1, sale_prc2/yr2); doc types + full chain only via title engine chain_of_title (status=delivered gate) | title harvest lanes; Tier 3 chain = Lane F |
| A6 | Neighborhood: income, owner-occupancy, appreciation context | §11-14 | **PARTIAL** | ACS 5-yr ZCTA LIVE (`context_layer_cache` acs_ok=4, last 2026-09-11 14:45Z): median income, ownership rate, poverty, median rent, population. Appreciation context: Layer 3 tables re-landed (B1) — moves to HAVE once a rendered report shows the Layer 3 block with a labelled geography | verify on a rendered report |
| A7 | Environmental / flood / hazards | §11-14 | **HAVE** (flood) / GAP (other) | FEMA NFHL point query LIVE (fema_ok=5): zone, SFHA, BFE. Wind/wildfire/sinkhole/radon: not sourced | later; print "Pending — not sourced" |
| A8 | Nearby places / POI | §11-14 | **HAVE (verify after cache refill)** | Lane D shipped a993c776 (Sep 11 4:23 PM ET): `fetchNearbyPlaces` (OSM Overpass, 1 mi, 8 classes, 30-day cache `context_layer_cache` layer `poi`), composer `context_layers.nearby_places`, pdf.js one row per class; HTML twin mirrored 02a8938d. **Defect found on verification (E7):** the query was node-only and matched `amenity=supermarket` (tag does not exist) → grocery always 0, way-mapped hospitals/schools/parks missed, "none within 1 mi" printed as fact for Jacksonville 32256. Fixed 2b22f957 (`nwr` + `shop=supermarket` + `out center`), stale poi cache rows deleted | re-verify the first live report's POI rows against a map before calling it HAVE |
| A9 | Schools | §11-14 | **HAVE** (nearest) / **PARTIAL** (assigned) | Lane E shipped 99c5aee4 (Sep 11 4:36 PM ET): `fetchSchools` — NCES EDGE CCD 2024-25 nearest elementary/middle/high within 5 mi + SABS 2015-16 assigned boundary (Pending when 0 or >1 polygons; "Unassigned" placeholders never printed). Live rows: 32904 → W. Melbourne Elementary 0.84 mi, Central Middle; 33035/33036 → honest Pending. No ratings by rule | `assigned` is computed and cached but not yet printed by either renderer — one-row follow-up in pdf.js + twin |
| A10 | Maps / location intelligence | deal page, §9-10 | **PARTIAL** | biddeed.ai /deal/:county/:case renders aerial + parcel outline; PDF/HTML report has no map | static aerial thumbnail into §9-10 (Mapbox static or county PA aerial URL already on `aerial_tight_url`) |

## B. Data Analyst agent → §3 (two-layer CMA) · county clearing ratios · §12 outcomes · §18

| # | ATTOM KPI family | SIGNAL$ twin | Status | Evidence | Owner / closer lane |
|---|---|---|---|---|---|
| B1 | Home-price / appreciation series | CMA Layer 3 (`cma_layer3` in composer) | **PARTIAL → HAVE pending a rendered report** | Lane B1 shipped 50f92d72 (Sep 11 3:41 PM ET) as a tracked migration: `public.live_market_metrics` 12,775 rows + `public.insurance_premiums` 5,452 rows, RLS on, 0 anon policies (re-queried 4:20 PM ET). The Sep 7 #20115 "shipped" record was false — tables did not exist until this re-land | moves to HAVE on the first rendered report showing the Layer 3 block with a labelled geography |
| B2 | Inventory / supply | Layer 3 | **PARTIAL** | same tables as B1 | same as B1 |
| B3 | Investor activity | §12 outcomes + buyer type | **OURS / PARTIAL** | 21,138 verified auction outcomes (tax_deed 15,396 + foreclosure 5,742); third-party vs plaintiff split; winner names from Bid History modal harvest (#19446) — fill still thin | outcome harvest lanes; Plaintiff Discount Index (plaintiff-discount.js, 11 composer refs) |
| B4 | Portfolio vs benchmark | — | **GAP (do not build)** | not an auction-GTM job | build only if a non-auction GTM needs it |
| B5 | Cross-market comparison | county clearing ratios | **OURS** | priors.js: median sold/assessed + sold/judgment per county, sale-type separated (tax deed 3.88 vs foreclosure 0.679 contamination fixed Aug 7); `auctions_summary_ssot()` 67 counties | keep; expose as `data_analyst` MCP tool |
| B6 | Charts | /radar calendar; report none | **PARTIAL** | radar calendar charts live; SIGNAL$ report has no chart | C7 generative UI (#19947); PDF sparkline of clearing ratio history |

## C. Report Generation agent → the 6 blocks inside our 18

| # | ATTOM block | SIGNAL$ | Status | Evidence | Lane |
|---|---|---|---|---|---|
| C1 | Executive Summary | cover KPI strip + verdict; §16 "Additional Comments" | **HAVE** | Lane G shipped 7eba5097 (Sep 11 4:35 PM ET): `buildExecutiveSummary(report)` in composer.js — deterministic ≤8-clause paragraph over verified fields only (case/sale type/date · verdict+grade · entry / SIGNAL$ Max Bid / walk-away, skipped when ceiling null · clearing vs retail ARV spread · top risk flag · title one-liner or "Title: Pending." · ML probability or "WITHHELD — validation gate open" · certification line); pdf.js `renderExecutiveSummary` under the cover strip; new golden test `executive-summary.golden.test.js` (foreclosure BID + tax-deed REVIEW fixtures); HTML twin renders `report.executive_summary.text` (02a8938d). Zero model calls, zero vendor names | none |
| C2 | Property Profile | §1 §8 §9-10 §16 | **HAVE** | | |
| C3 | Maps & Location Intelligence | §11-14 | **PARTIAL → mostly HAVE** | A6 ACS + A7 FEMA + A8 POI + A9 schools live; no map image in the report (A10) | aerial thumbnail (A10) |
| C4 | Comparable Sales | §4-7 | **HAVE + OURS** | Layer 1 distressed + Layer 2 retail (Patent Claim 7) | |
| C5 | Valuation Insights (AVM, confidence, rental estimate, history) | §2-3 | **HAVE + OURS** (rental PARTIAL, history GAP) | two bands with HIGH/MED/LOW confidence; rental: `rental_listings` 10,532 rows / 18 counties render on ZoneWise Comps tab, not in the report; historical values: GAP | rental line into §2-3; value history via NAL jv history is one query |
| C6 | Charts & Visualizations | — | **PARTIAL** | B6 | B6 |

## D. OURS — no ATTOM twin (the beat)

| Section | Status | Evidence | Note |
|---|---|---|---|
| §ML SIGNAL$ Models | **OURS — probability WITHHELD** | `shapira_model_validations` 2026-09-11: V4 prod OOT AUC **0.478 FC / 0.391 TD** (worse than chance); v5b candidate 0.63 FC / 0.885 TD, passed=false | print model_version + gate status; never print p until a validation row has passed=true. Rebuild #20240 |
| §ZW ZoneWise | OURS/PARTIAL | DOR land use + JV live; district per county PARTIAL | GIS mission #20246 |
| §15 Bid card | OURS HAVE | entry · SIGNAL$ Max Bid · walk-away · verdict; BID→REVIEW on junior-lien risk or low 3P probability | disclaimer seam stays |
| §16 Title + lien hierarchy | OURS/PARTIAL | 25 live OR counties; avg parity 30.8%; 55/1,890 upcoming at parity (1:29 PM ET); statute-cited survival; UNRESOLVED never guessed | 20 Turnstile counties deferred by Ariel |
| §18 Outcome writeback | OURS HAVE | outcome.js grades ceiling_call / value_band_call | harvest completeness governs |
| §17 sha256 snapshot | OURS/PARTIAL | `title_search_snapshots` versioned + sha256 (3 rows); no whole-report hash | small lane: hash the report JSON at purchase into s5_pdf_cache |

## E. Defects found while mapping (fix before "parity")

| # | Defect | Where | Fix |
|---|---|---|---|
| E1 | SSOT row `rehab_estimate` (§REHAB, sort 75, is_active=true) has **no renderer** in pdf.js (0 hits) or S5Report.tsx, and composer.js never emits `report.rehab` (0 hits) → paying customers see "no handler registered for section_key 'rehab_estimate'" | both twins | **FIXED** — pdf.js b89233f9 (Sep 11 4:11 PM ET): `rehab_estimate` renderer prints "Pending — rehab estimate engine not yet producing for this parcel", composer emits `rehab:{available:false, reason}` on every branch, golden test +176 lines (Duval + Marion fixtures, rendered PNGs); HTML twin 5f141e36 carries the identical string. "no handler registered" = 0 hits in pdf.js |
| E2 | S5Report.tsx `context_layers` reads `ctx.neighborhood` / `ctx.flood_zone` as strings; composer emits objects (`neighborhood.{median_income,ownership_rate,…}`, `fema.{zone,sfha,bfe}`) → HTML twin prints `[object Object]` and a permanent "FEMA not wired" | S5Report.tsx | mirror pdf.js context_layers (shipped: zonewise-web main 5f141e36, deployed to zonewise.ai Sep 11 3:49 PM ET) |
| E3 | S5Report.tsx `shapira_ml` hardcodes v14.0 text and the withheld logic is inverted (prints the withheld note only when a probability IS present) | S5Report.tsx | data-driven model_version; print p only when the composer's gate passed (numeric probability and `ml.withheld !== true` — the composer never emits a `print_probability` flag, corrected 02a8938d), else WITHHELD with the gate named (shipped 5f141e36 + 02a8938d) |
| E4 | S5Report.tsx does not render `title_search` (§16 blocks 1-7b) — pdf.js does since #20254/#20270 | S5Report.tsx | port the block renderer (shipped: zonewise-web main 5f141e36, deployed to zonewise.ai Sep 11 3:49 PM ET) |
| E5 | Band colours in S5Report.tsx are the retired `#1E3A5F`/`#F59E0B` | S5Report.tsx | canon `#0A2540` / `#005EB8` (shipped: zonewise-web main 5f141e36, deployed to zonewise.ai Sep 11 3:49 PM ET) |
| E6 | pdf.js `shapira_ml` (the CANONICAL renderer) printed three hardcoded rows on every report — `Model: v14.0 XGBoost` fallback (a retired model), `Trained 2026-05-27 · 137,488 samples · 21 features`, `Accuracy / AUC acc 72.2% · AUC 0.783 · precision 0.716 · recall 0.909 · F1 0.801` — while `shapira_model_validations` (Sep 11 2026) shows the production model at out-of-time AUC 0.478 FC / 0.391 TD, probability withheld. The probability gate itself was sound; the training claims were not | pdf.js | **FIXED** dfc8b87f (Sep 11 4:41 PM ET): Model + Validation rows come from `ml.model_version` / `ml.withheld` / `ml.withheld_reason`; provenance `model_disclosure` fallback and the two fallback template titles rebranded to SIGNAL$ |
| E7 | Lane D's Overpass query scanned `node(...)` only and matched `amenity=supermarket` (no such tag) → grocery always 0, way-mapped hospitals/schools/parks under-counted, printed as "none within 1 mi" (e.g. Jacksonville 32256). The unit test enshrined the wrong tag | context-layers.js | **FIXED** 2b22f957 + 61c47d40 + f86a1deb: `nwr(around)` + `shop=supermarket|grocery|greengrocer` + `out center` (centroid read from `el.center` for ways/relations); test fixture uses the real tags and a way element; stale `poi` cache rows deleted so the next report re-fetches |

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
