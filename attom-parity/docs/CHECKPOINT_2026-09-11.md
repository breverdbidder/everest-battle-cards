# SIGNAL$ × ATTOM parity — CHECKPOINT, Fri Sep 11 2026 7:20 PM ET

Board of record: cli-anything-biddeed #20287. Every number below was re-queried at 7:16 PM ET (Supabase mocerqjnksmhcjzxrewo) or read from `main`; nothing is carried from a run badge or an issue comment. Status vocabulary: HAVE · PARTIAL · GAP · BLOCKED · OURS (no ATTOM twin) · DEFECT.

## Closed today (for the record — not open)

E1 §REHAB renderer (b89233f9) · B1 Layer 3 re-land (50f92d72; 12,775 + 5,452 rows) · D POI (a993c776 + fix 2b22f957, verified against live OSM) · E schools nearest (99c5aee4) · G executive summary (7eba5097) · defects E1–E7 · HTML twin parity (5f141e36 → 02a8938d, deployed) · pdf.js/twin kill-list gate (0fceac18 / a9cf3972, other lane) · tax-deed model `td-soldvred-v1` validated and wired (74ca54fc, other lane) · battle card + private repos + /answers embed live · Cards Complete = 3.

## OPEN KPIs — one row per gap, with the live number and what closes it

| # | KPI (ATTOM family → SIGNAL$ section) | Status | Live evidence 7:16 PM ET | What moves it | Owner |
|---|---|---|---|---|---|
| K1 | Tax amount / paid-delinquent status (A4 → §16 tax block, title CP3) | **BLOCKED** | `tax_collector_results` 66 attempts, **66 blocked, 0 ok**; 13 Cloudflare Turnstile challenges; `title_search_snapshot.tax.payment_status` prints "Pending — tax collector not reachable"; CP3 statewide **0.86** unchanged | A decision, not code: (a) leave Pending (honest, current), (b) annual published delinquent-tax lists per county → "delinquent yes/no" only, no current amount, (c) a residential-IP fetch path — spend + a rule you set (no proxies / no captcha bypass) | **Ariel** |
| K2 | Title parity — vesting, chain, mortgages, encumbrances, lien priority (A2, A5 → §16) | **PARTIAL** | `v_title_parity_kpi_statewide` (computed 4:15 PM ET): 1,890 upcoming / 57 counties / avg parity **33.2%** / **71 at parity (3.8%)**; CP1 0.77 · CP2 0.97 · CP3 0.86 · CP4 0.49 · CP5 0.47 · CP6 0.42; `title_search_snapshots` = 3 | The 20 Turnstile counties stay deferred (your call, earlier). CP4/CP5/CP6 rise only with the OR harvest lanes already running under the shared cc lease (#20255 + shards) — not an ATTOM-kit item | CC lanes (running) |
| K3 | POI rendered on a real report (A8 → §11-14) | **HAVE — unrendered** | `context_layer_cache` layer poi = **0 rows** (purged after the E7 fix); fixed query verified against live OSM (61 elements, 10 grocery at 3 mi where the old query returned 0) | First real report render fills the cache; eyeball its POI rows once against a map, then A8 → HAVE | Architect (next render) |
| K4 | Assigned school (SABS) printed (A9 → §11-14) | **PARTIAL** | `schools` cache = 4 rows carrying `assigned.{elementary,middle,high}` (real name or honest Pending); **neither pdf.js nor S5Report.tsx prints it** | One row in each renderer, mirrored; no data work | Architect |
| K5 | Layer 3 appreciation / inventory rendered (A6, B1, B2 → §4-7 Layer 3 block) | **PARTIAL → HAVE pending a render** | tables present (12,775 / 5,452 rows, RLS on, 0 anon); composer references `cma_layer3` + `insurance_kpi`; no report rendered since the re-land (`s5_pdf_cache` last row 12:17 PM ET, before every lane) | First real report showing the Layer 3 block with a labelled geography | Architect (next render) |
| K6 | Foreclosure ML probability (D → §ML) | **OURS — WITHHELD** | `shapira_model_validations`: V4 prod OOT AUC **0.478** (below 0.547 baseline), v5b **0.63**, v5 logreg **0.59** — none ≥ 0.70, passed=false; tax deed is NOT open: `td-soldvred-v1` passed (0.8625 vs 0.4841, n_test 1,624) and prints | Foreclosure rebuild #20240 on verified outcomes; ships automatically through all three gates when a row passes | ML lane (#20240) |
| K7 | Whole-report sha256 at purchase (D → §17 provenance) | **GAP** | `s5_pdf_cache` has 8 rows, `report_json` stored, **no hash column**; only the title snapshot is hashed (`title_search_snapshots`, 3 rows) | Small lane: hash `report_json` at purchase into `s5_pdf_cache`, print in §17 | CC lane (not opened) |
| K8 | ZoneWise district per county (D → §ZW) | **OURS / PARTIAL** | DOR land use + just value live; district assignment prints "PENDING — district layer not built" outside the built counties | GIS mission #20246 (running, separate program) | CC lane (running) |
| K9 | Maps / aerial in the report (A10, C3) | **PARTIAL** | deal page renders aerial + parcel outline; PDF/HTML report has no map image | Static aerial thumbnail into §9-10 from `aerial_tight_url` already on the row | CC lane (not opened) |
| K10 | Charts in the report (B6, C6) | **PARTIAL** | /radar calendar charts live; SIGNAL$ report has **0** charts | Clearing-ratio history sparkline in §4-7 (C7 generative UI #19947 is the wider item) | CC lane (not opened) |
| K11 | Rental estimate + value history (C5 → §2-3) | **PARTIAL / GAP** | `rental_listings` 10,532 rows / 18 counties render on the ZoneWise Comps tab, not in the report; historical values not printed (NAL jv history is one query) | One rental line + one jv-history line in §2-3, both renderers | CC lane (not opened) |
| K12 | Investor activity depth (B3 → §12) | **OURS / PARTIAL** | 21,138 verified outcomes; winner names from the Bid History harvest (#19446) still thin | Outcome harvest lanes (separate program) | CC lanes (running) |
| K13 | Other hazards — wind / wildfire / sinkhole (A7) | **GAP by decision** | prints "Pending — not sourced" | Only if a customer asks; FEMA flood is live | — |
| K14 | Occupancy (A2) | **GAP by design** | no source; homestead status is the printed proxy | None — no homeowner-data purchase (compliance rule) | — |
| K15 | Rehab estimate engine (§REHAB) | **PARTIAL** | both renderers print "Pending — rehab estimate engine not yet producing for this parcel"; no engine | Pro Plus construction-management program (C12) feeds this, not the ATTOM kit | separate program |
| K16 | pdf.js layout defects (flagged by the kill-list lane, unfixed) | **DEFECT** | cover verdict/KPI strip drawn 44 pt above its band; `renderExecutiveSummary` paints over the verdict rect; `flagBox` writes code + text at the same x; §18 captured branch keys on legacy `outcome.result` the composer never emits → always Pending; `row()` page-break spills one row onto an empty page | One pdf.js layout pass with rendered-PNG proof; do it before the first customer PDF goes out | Architect or CC lane |
| K17 | Grok GitHub write (Mission 0) | **BLOCKED — your side** | both connectors 403 on every write; Grok cannot push | 6 steps in docs/PRIVATE_REPO_HANDOFF.md (GitHub App installation permissions); until then Grok drafts, cc-runner executes | **Ariel** |
| K18 | biddeed.ai homepage tile for the /answers embed | **OPTIONAL** | page is live and DB-driven; no homepage entry point | biddeed-web PR + your merge | Ariel (merge) |

## Decisions that are yours (everything else runs without asking)

1. **K1 tax collector** — leave Pending, published delinquent lists (yes/no only), or a paid residential-IP path (breaks your no-proxy rule).
2. **K17 Grok write** — the GitHub App permission grant.
3. **K18 homepage tile** — merge or skip.

## What the architect runs next without asking

K4 (assigned-school row in both renderers), K16 (pdf.js layout pass with PNG proof), K3 + K5 verification on the first real render. K7, K9, K10, K11 are small CC lanes that open on your "go" — none of them is in the customer's way today; the moat sections (two bands, SIGNAL$ Max Bid, statute-cited title stack, §18 writeback) already render.

Pairing rule holds: BidDeed.AI + ZoneWise.AI together. Vendor name count in customer output: 0. Honesty Protocol: every open row above prints Pending / UNRESOLVED / WITHHELD in-line today.
