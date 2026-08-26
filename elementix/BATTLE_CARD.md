# Elementix — Competitive Battle Card

**Site**: elementix.com | **Category**: Borrower/investor intelligence for private lenders (adjacent, not identical, to Winner Data)
**Compiled**: 2026-08-26, from live pages (home, /prospecting, /underwriting, /investor-tracking, /technology, /faq, /careers, robots.txt). Sourced with Exa's fetch tool, not Firecrawl/Playwright — see "What's NOT in this pass" below.

## One-line positioning
"The borrower intelligence platform for private lenders" — identify active investor prospects, underwrite full portfolio risk across every entity a borrower controls, and reach decision-makers with verified contact data.

## Headline numbers (as stated on-site, unverified by us)
- 100M+ documents analyzed
- 5.6M investors tracked
- 5.1M entities mapped
- 99%+ US coverage
- 80% verified contact accuracy (self-benchmarked against "national lender CRM data")
- 250+ counties for signature/document coverage, refreshed weekly

## Core technical moat — how they build "ownership intelligence"
Three combined techniques, explicitly named on /technology and /faq:
1. **Signature analysis** — extract and analyze signatures from 100M+ recorded document images (deeds, mortgages). A signature on a document for an entity links that entity to the real person who controls it.
2. **Secretary-of-state filing data** — cross-referenced across all 50 states, explicitly filtering OUT registered agents and nominees to find the true beneficial owner.
3. **Automated AI research** — investigative techniques (cross-referencing, following ownership trails) applied at scale across millions of entities.

This is the *exact* workflow Winner Data did by hand today, one buyer at a time, over several hours (dancing homes, J&R Properties, Laxmi Land Investment, Greenback Assets Corp, Anthony C Scott Investments — each requiring individual Sunbiz pulls, name-collision checks, and manual cross-referencing). Elementix has industrialized it.

## Product surface (3 modules, all built on the same ownership graph)
- **Prospecting** — explicitly markets against the traditional "entity → registered agent → skip-trace" workflow (their own diagram calls this out as broken: "Registered Agent? Attorney? Wrong Person?"). Filters by loan history, recent activity, geography, experience level.
- **Underwriting** — surfaces undisclosed liabilities/foreclosures across ALL of a borrower's entities, not just the ones self-reported on an REO schedule. Has a real documented API: `GET /v1/entities?name=X&state=Y` returning entity, principals, exposure, connected_entities.
- **Investor Tracking** — portfolio-level signals: expansion, disposition, geographic shifts, new entity formation. **Explicitly markets to "service providers" who need to identify growing portfolios for insurance, property management, or legal services** — this is direct positioning into Winner Data's own insurance vertical, not just lending.

## Real, material risk found in their data (not theoretical)
Cross-checked one live match against Elementix's own screenshot (Anthony C Scott Investments LLC, our Aug 25 lead): the entity match was correct, but the associated contact email domain pattern ("@anthonytscott.com") traces in independent search to a **different, unrelated real person** — Anthony **T** Scott, an Orlando broker with a documented separate identity (DBPR license BK655005, different city, different middle initial) — already ruled out earlier the same day as not our buyer. This suggests their signature/automated-matching pipeline can plausibly conflate similarly-named individuals. Not proven at scale, but a real, specific, reproducible instance — worth watching for, and worth remembering as a genuine defensibility point for a slower, source-verified approach.

## Compliance posture
Sells at "the organization level" for insurance/legal/property-management service providers, not raw consumer data to individuals. FAQ text explicitly disclaims FCRA consumer-report status and states they may suppress contact info "where legally required or where appropriate for this consumer's privacy... governed by the Fair Credit Reporting Act." No public TCPA/DNC-specific claim found in this pass.

## Team signal
Careers page: "No jobs currently posted... If you're a good fit, we'll find a way to work together." Small/lean team plausible given the automation-heavy pipeline — worth revisiting if this changes.

## Robots.txt / crawl posture (real, verified)
Explicitly blocks AI-training crawlers by name: ClaudeBot, GPTBot, Google-Extended, Amazonbot, Bytespider, CCBot, Applebot-Extended, meta-externalagent, CloudflareBrowserRenderingCrawler. Confirms `Content-Signal: ai-train=no` at the site level. Allows traditional search indexing (`search=yes`) and AI grounding/retrieval at inference time (`ai-input=yes`) — i.e., they're fine being cited by an AI answering a question live, just not fine being used to train a model. `/api/` and `/admin/` explicitly disallowed from crawling. Real sitemap exists at elementix.com/sitemap.xml but wasn't retrievable with the tools available this pass (XML content-type isn't parseable by the fetch tool used).

## What's NOT in this pass — genuine gaps, not glossed over
Ariel asked for "all our artillery" — Firecrawl paid credentials, Playwright + Chromium screenshots per page/tab, full sitemap/endpoint discovery. None of that infrastructure is available in this chat session directly. This pass used Exa's fetch tool only, which got real content from 7 pages plus robots.txt, but:
- No actual sitemap.xml contents (blocked by content-type, not by the site)
- No visual/screenshot record of any page
- No deep API endpoint enumeration beyond the one documented example on /underwriting
- No pricing page found/checked
- No LinkedIn/team headcount cross-check
- No check of trust.elementix.com (referenced in footer, not fetched)

Dispatched separately to CC (which has the actual Firecrawl credentials and Playwright infrastructure used elsewhere in this pipeline) to complete the remainder properly.
