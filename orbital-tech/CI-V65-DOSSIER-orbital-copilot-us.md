# CI V6.5 Dossier — Orbital (Copilot US)

**The AI-native title & legal-DD benchmark: what ZoneWise's spatial layer and PropertyOnion's human title desk look like when rebuilt as venture-scale AI**

Protocol: CI V6.5 (195 checkpoints / 13 phases) · Target: orbital.tech · Date: June 12, 2026
Requested by: Ariel (GO DOSSIER) · Honesty: [V] verified, [I] inferred, [A] assumed
Classification: SIGNAL_DOSSIER · Threat: 🟡 LOW-MEDIUM · Pairing companions: **mapwise** (ZoneWise benchmark), **propertyonion** (title-search incumbent), **housecanary-mcp** (data-owner benchmark)

---

## 1. One-line verdict

Orbital is a **workflow copilot, not a data owner**: $75M raised to replace attorney hours on *customer-supplied* documents (title & survey review, PSA/lease drafting, legal-description plotting, historic-deed OCR), sold to Am Law 100 / title companies with an **insurance policy on AI outputs** as the trust wedge. It does not touch foreclosure/tax-deed auctions, Florida county corpora, or investor decisions — but it is the proof-of-market for three capabilities BidDeed+ZoneWise should own natively: legal-description→polygon, degraded-document restoration, and productized chain-of-thought trust.

## 2. Corporate & funding [V]

- Founded 2018, London (as Orbital Witness; rebranded Orbital). Mishcon de Reya MDR Lab alum.
- Founders: **Will Pearce (CEO)** + **Ed Boulle** — space-industry origin, pivoted from satellite imagery monitoring to RE legal work after investor rejection of v1.
- **Series B Jan 26, 2026: $60M** led by Brighton Park Capital (NYC). New: REV (RELX/LexisNexis VC — strategic), LegalTech Fund, Moderne Ventures, Grosvenor (customer-investor). Existing: JLL Spark, Outward, Seedcamp. **Total raised ~$75M.**
- ~120 employees, plan to **double headcount in 12 months**, US-weighted. NYC office: 18 W 18th St.
- Scale: **200,000 transactions/yr**, 5,000+ professionals. Customers: A&O Shearman, Goodwin, Dentons, Greenberg Traurig, V&E, Polsinelli, Winstead, Seyfarth, Orrick, Cleary + Land Services USA, Essex Title (title cos), in-house, REITs.
- TAM claim: $140B (RE legal services).

## 3. Product surface (Copilot US) [V]

| Capability | What it does | BidDeed/ZoneWise relevance |
|---|---|---|
| Title & Survey review | Bulk-upload, extract, flag exceptions; claims 70% review-time cut | = PropertyOnion's human title desk, automated. Direct C/D-criterion analog |
| Property Visualizer | Legal description → digital polygon overlaid on survey/map | = ZoneWise spatial layer applied to deeds. STEAL |
| Doc Restorer | Handwritten/blurry/historic deed OCR where standard OCR fails | = exact capability needed for clerk/official-records C/D litmus (pre-authorized Arm) |
| First Drafts | Agreed terms → PSA/lease drafts on firm precedents | Out of scope for us |
| Chain-of-thought transparency | Shows reasoning path per conclusion | = Honesty Protocol V3, productized as marketing |
| **Insured AI outputs** | First legaltech with product-specific insurance on AI work | Trust-wedge playbook worth studying for PENCIL gold certification claims |

## 4. Data posture — the moat question [I]

Orbital owns **models + workflow, not corpus**. Its inputs are the customer's documents plus public registries (UK HM Land Registry heritage; US county records via customer upload). Contrast:
- **HouseCanary (parity 0.71):** owns AVM corpus + forecasts → repriced for agents. Data owner.
- **BidDeed:** owns 356K-row auction-outcome corpus + 10.5M parcels + Shapira models. Data owner.
- **Orbital:** value evaporates without the client's deal documents. Defensibility = workflow lock-in + precedent libraries + insurance + BigLaw logos.

**Parity score vs BidDeed+ZoneWise: 0.38** — high capability overlap on title/spatial mechanics, near-zero overlap on corpus, buyer, and decision product.

## 5. Threat model

- **Direct (today): LOW.** Buyer = law firms billing hours; ours = investors buying outcomes. No FL auction calendar, no outcome labels, no bid intelligence.
- **Vector (24mo): MEDIUM.** RELX/LexisNexis strategic money + title-company customers + Doc Restorer = the ingredients for an *investor-facing title-risk product on county records*. If Orbital ships that, it lands on the C/D moat. Watch trigger: any Orbital product consuming county official records directly (not customer uploads).
- **Defensive note:** Their 200K transactions/yr generate labeled legal-risk data as exhaust. Same compounding pattern as our outcome labels — they will eventually become a data owner.

## 6. Steal list (priority order)

1. **Doc Restorer pattern → clerk/official-records pipeline.** Brevard/Duval pre-2000 handwritten mortgages defeat tesseract; Orbital proves restoration is buildable and that $800/hr buyers pay for it. Slots directly into the pre-authorized C/D litmus expansion (gold-loop standing orders).
2. **Legal-description → polygon → ZoneWise feature.** Metes-and-bounds autoplot on parcel maps; ZoneWise already has the GIS substrate Mapwise lacks AI on. Investor-side wedge into the exact audience Orbital sells attorney-side.
3. **Insurance on AI outputs.** The single smartest trust move in the space. PENCIL gold certification + insured accuracy claims = category-defining for auction intelligence. Investigate E&O markets for AI outputs (their insurer partnership is public, 2025).
4. **Chain-of-thought as headline marketing.** Honesty Protocol V3 markers are already built — market them, don't bury them.

## 7. SSOT cross-refs

- `everest-battle-cards/mapwise/` — ZoneWise zoning benchmark (Orbital = the AI-native contrast case)
- `everest-battle-cards/propertyonion/` — title-search incumbent (Orbital = what their title desk becomes)
- `everest-battle-cards/housecanary-mcp/` — data-owner benchmark (Orbital = the non-data-owner contrast)
- `docs/plans/CI-DOSSIER-CHECKPOINT-PROTOCOL-v1-2.md` — protocol canonical

*Self-audit: funding/customers/products [V] from press + site probe Jun 12 2026; parity 0.38 [I] scored on V6.5 moat matrix; insurance detail [V] via CB Insights/Artificial Lawyer; threat vector [I].*
