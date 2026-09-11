# Private repo handoff — biddeed-attom-agent-reports · biddeed-attom-mcp

**State (2026-09-11, 2:35 PM ET):** both private repos were created and populated by the AI architect through the vault PAT path (`gh_api_req` as breverdbidder) because BOTH the Grok GitHub connector and the Claude GitHub connector return `403 Resource not accessible by integration` on every write (repo create, Contents PUT, git push). This is a GitHub-App permission grant, not a code problem.

## Restore Grok write (Ariel, 6 lines)

1. github.com/settings/installations (as breverdbidder).
2. Configure the xAI / Grok app → Repository access: All repositories (or add everest-battle-cards, biddeed-attom-agent-reports, biddeed-attom-mcp, zonewise-web, cli-anything-biddeed).
3. Accept the Permissions review if offered (Contents: Read & write · Administration: Read & write). No banner → disconnect and reconnect the GitHub connector inside Grok and pick the write scope.
4. Repeat for the Anthropic / Claude app.
5. Reply to Grok: "write is live — finish the private repos and Pages push."
6. No write scope offered → Grok drafts issue briefs; Ariel pastes them into cli-anything-biddeed; cc-runner executes (SCOPE_GROK.md zero-Claude build path).

## What Grok owns after write is restored

- Re-crawl the three agent pages + the announcement; diff `docs/BATTLE_CARD.md` §1; push.
- Regenerate the illustrative samples if ATTOM's published block list changes (`python -m reports.<agent>` in biddeed-attom-agent-reports).
- Keep `attom-intelligence/index.html` + `BATTLE_CARD.md` on everest-battle-cards current; keep `index.html` competitor 07 status pill honest.
- Move KPI rows PARTIAL → HAVE in `docs/KPI_PARITY_MATRIX.md` ONLY on live evidence (a query, a rendered report), never on a merged PR alone.
- Extend `mcp/tools.py` when ATTOM ships A2A or new tools; keep the seven names stable.

## What Grok must not do

- Rewrite `S5Report.tsx`, `pdf.js`, `composer.js`, or `s5_report_sections`.
- Open a parallel ATTOM kit or a fourth renderer.
- Put the vendor's name in anything customer-facing.
- Push to `cli-anything-biddeed` main while a `cc:*` lease is held (see repo-push protocol).

## Verification commands

```bash
python -m mcp.server --list
python -m mcp.server --call report_generation '{"county":"sample","case_number":"2026-CA-000000"}'
python -m reports.report_generation && pdftotext samples/SIGNAL_twin_Report_Generation_SAMPLE.pdf - | grep -ci attom   # expect 0
```
