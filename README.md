# Everest Battle Cards

**Competitive intelligence dashboard for BidDeed.AI + ZoneWise.AI**

Live site: **https://breverdbidder.github.io/everest-battle-cards/**

Canonical delivery target for every competitor battle card produced by the Everest Capital Claude ecosystem. Each card is deployed as a GitHub Pages subpath and becomes a shareable URL for LinkedIn bake-off content, investor decks, internal CI review, and SEO.

## Structure

```
/                     → Dashboard index (all 11 competitors, status pills)
/dono-ai/             → Dono.ai v5 canonical template (Apr 11, Ariel approved)
/algoma/              → (Pending SUMMIT #406)
/propzone/            → (Queued)
/gridics/             → (Queued)
/propertyonion/       → (Queued — title-search scope live at /propertyonion-title-search/)
/reventure/           → (Queued)
/attom-intelligence/  → ATTOM Intelligence battle card (competitor 07, Sep 11 2026) + BATTLE_CARD.md
/attom-parity/        → SIGNAL$ × ATTOM parity kit: schemas/ (18-section map + 3 agent twins) · mcp/ (7-tool stable registry + stub server) · reports/ (illustrative generators) · samples/ · docs/KPI_PARITY_MATRIX.md (board of record mirror)
/{slug}/              → One directory per competitor, index.html inside
```

## Protocol (locked Apr 12, 2026 — PERMANENT)

Every competitor battle card MUST:

1. **Dispatch** via `claude-code-direct.yml` on `breverdbidder/cli-anything-biddeed` with the issue number.
2. **Execute** via Managed Agent Teams on Hetzner tmux. No inline sandbox execution.
3. **Follow phase-by-phase review** — 195-checkpoint v1.2 protocol, ≥90% green benchmark, no advance without Ariel approval.
4. **Inherit the Dono.ai v5 template** — 13-category review structure, 6 sections (moat, stack, pricing, quality parity, pipeline, 3-approach verification).
5. **Pass the EG14 gate** — 14-point enterprise gate, 30s poll, 15min timeout, 3 outcome branches. No Telegram until verdict.
6. **Push the final HTML** to this repo under `/{slug}/index.html` and update the root `index.html` status pill from Queued → Active → Complete.

## Template inheritance

Every new battle card copies the Dono.ai v5 structure. Agents receive the canonical HTML as a template input and replace content while preserving the 13-category grid, section IDs, and navigation pattern. This keeps every card visually and structurally consistent, which matters for:

- Side-by-side LinkedIn comparison posts
- Investor deck embedding
- SEO canonical structure across the subpath tree
- Internal CI review velocity (Ariel reads 11 cards with the same muscle memory)

## House brand — biddeed.ai SSOT palette (since Sep 11 2026)

Source of truth: `scripts/palette-gate.mjs` on `breverdbidder/biddeed-web` main. The old navy `#1E3A5F` / orange `#F59E0B` / slate `#020617` set is RETIRED.

- **Light (the seven):** bg/card `#FFFFFF` · tint `#E6F0FA` · ink `#1A1A1A` · navy/headings `#0A2540` · border `#D7E3F1` · brand `#005EB8` · brand hover `#004A92`
- **Dark:** `#0B1119` `#111B27` `#1B2737` `#EDEDED` `#9EB2C7` `#24344C` `#1A90FF` `#4DA6FF`
- **Type:** Inter · Source Serif 4 (display) · JetBrains Mono (data)

No other colours. Cards render light-first with a dark override; the dashboard index uses the dark set.

## Pairing rule

Every card mentions BidDeed.AI + ZoneWise.AI together. Foreclosures and tax deeds are always paired. This is a permanent messaging rule — no card ships mentioning only one side of the pair.

## Related

- **Mono-repo for competitors:** this repo
- **Author book launch cards** (separate pattern): [`mariam-blueprint`](https://github.com/breverdbidder/mariam-blueprint) — Mariam Shapira's Furnished Units Cashflow Blueprint, Apr 12 2026
- **CI Protocol SSOT:** `docs/CI-PROTOCOL.md` in `cli-anything-biddeed`
- **Battle card template source:** `dono_recon/dono-ai-battle-card.html` on Hetzner

## ATTOM parity (Sep 11 2026)

Private sister repos: `biddeed-attom-agent-reports` (generators, schemas, samples, KPI matrix) and `biddeed-attom-mcp` (7-tool parity map). Production renderers are untouched by the kit: `pdf.js` (cli-anything-biddeed) and `S5Report.tsx` (zonewise-web) reading `public.s5_report_sections`. Customer copy never names the vendor: *national property-data plants answer what the house is; we answer what you should bid.*

## Status (updated Sep 11, 2026 — launched Apr 12, 2026)

| # | Competitor | Status |
|---|---|---|
| 01 | Dono.ai | ✓ Canonical (v5, Apr 11) |
| 02 | Algoma | ⚡ Active (SUMMIT #406 dispatched) |
| 03 | PropZone | Queued |
| 04 | Gridics | Queued |
| 05 | PropertyOnion | ⚡ Partial — title-search card live (Sep 11 2026) |
| 06 | Reventure | Queued |
| 07 | ATTOM Intelligence | ✓ Complete (Sep 11 2026) — /attom-intelligence/ + /attom-parity/ |
| 08–11 | TBA | Queued |

---

Built by the Everest Capital Claude ecosystem.
