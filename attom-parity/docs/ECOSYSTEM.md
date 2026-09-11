# Ecosystem map — where the ATTOM parity work lives

```
breverdbidder/everest-battle-cards   (public, GitHub Pages)
├─ index.html                        competitor 07 = ATTOM Intelligence · Cards Complete = 3
├─ attom-intelligence/index.html     the battle card (biddeed.ai SSOT palette: Inter / Source Serif 4 / JetBrains Mono)
├─ attom-intelligence/BATTLE_CARD.md
└─ attom-parity/                     copy of the kit (schemas, mcp stub, generators, docs, samples)

breverdbidder/biddeed-attom-agent-reports   (private)
├─ reports/   illustrative ATTOM-twin PDF generators (bake-off only)
├─ schemas/   property_place_insights · data_analyst · report_generation · signals_18_section
├─ samples/   agent_payloads.json + 3 illustrative PDFs (fictional subject)
└─ docs/      BATTLE_CARD · ECOSYSTEM · KPI_PARITY_MATRIX · PRIVATE_REPO_HANDOFF

breverdbidder/biddeed-attom-mcp             (private)
├─ mcp/       tools.py (7-tool stable registry) · server.py (stdio stub, forwards to live when keyed)
├─ schemas/   same four schemas
└─ docs/      BATTLE_CARD · ECOSYSTEM

PRODUCTION (unchanged by this kit — the kit maps onto it, never forks it)
├─ breverdbidder/cli-anything-biddeed/packages/biddeed-mcp/src/report/composer.js   the report math
├─ …/report/pdf.js                                                                  canonical PDF renderer
├─ breverdbidder/zonewise-web/components/report/S5Report.tsx                        HTML twin
├─ https://mcp.biddeed.ai/api/mcp                                                   36 tools / 7 streams
├─ Supabase mocerqjnksmhcjzxrewo                                                    public.s5_report_sections (template SSOT),
│                                                                                   rpc/title_search_snapshot, rpc/title_lien_priority,
│                                                                                   context_layer_cache (FEMA, ACS), multi_county_auctions
└─ biddeed.ai                                                                       Worker router + biddeed-web (OpenNext on Cloudflare)
```

## Data flow for one report

1. `predict_auction_outcome(county, case)` on mcp.biddeed.ai → `composer.js` builds the 18-section object (Layer 1/2 CMA, priors, value bands, SIGNAL$ Max Bid, verdict, red flags, context layers, title snapshot, outcome).
2. `pdf.js` reads `v_s5_report_template` (5-min cache) and renders every active `section_key`; `S5Report.tsx` renders the same object as HTML on zonewise.ai/report.
3. The three MCP twins in `mcp/tools.py` are VIEWS over that object (plus the county aggregates for `data_analyst`) — no new math, no new source of truth.

## Ownership

| Lane | Owner | Notes |
|---|---|---|
| Battle card + KPI matrix freshness | Grok (once GitHub write is restored) | re-crawl, diff, refresh; never touches S5Report.tsx / pdf.js |
| Product wiring (PARTIAL → HAVE) | cc-runner lanes dispatched from cli-anything-biddeed issues | Lane B1 Layer 3 re-land · C tax collector · D OSM POI · E NCES schools · G narrative · E1 rehab renderer |
| Architecture / acceptance | Claude (AI architect) | KPI matrix issue is the board of record |

## Two repos, one kit — why the split

`biddeed-attom-agent-reports` holds anything that renders a PDF (bake-off samples, generators, schemas). `biddeed-attom-mcp` holds only the tool map and the stub server so it can be pip-installed or vendored into the MCP repo without pulling reportlab. Both carry BATTLE_CARD.md + ECOSYSTEM.md so either repo reads standalone.
