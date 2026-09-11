"""
BidDeed.AI × ZoneWise.AI — MCP parity layer mapped to ATTOM Intelligence.

Tool NAMES are stable (do not rename — Grok's battle card and the KPI matrix
reference them). Three tools twin ATTOM's three agents; four tools have no
ATTOM twin — that is the beat.

Production surface remains https://mcp.biddeed.ai (36 tools / 7 streams).
This module is the MAPPING + a sample dispatcher. When a KPI is added to the
SIGNAL$ report, add it here AND to the live tool in the same PR.

Honesty Protocol: every field is a value with provenance or an explicit
'Pending — <reason>' / 'UNRESOLVED' / 'WITHHELD' string. Nothing is inferred.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

SAMPLES = Path(__file__).resolve().parent.parent / "samples" / "agent_payloads.json"
SCHEMAS = Path(__file__).resolve().parent.parent / "schemas"

# ── stable registry ─────────────────────────────────────────────────────────
TOOLS: dict[str, dict[str, Any]] = {
    # ATTOM twins
    "property_place_insights": {
        "twin_of": "ATTOM Property & Place Insights Agent",
        "description": "One-parcel Q&A: identity, ownership, characteristics, value & tax, transactions, neighborhood (ACS), flood (FEMA NFHL), POI, schools — plus the SIGNAL$ two-band value estimate and verdict.",
        "schema": "property_place_insights.json",
        "live": {"mcp": "https://mcp.biddeed.ai/api/mcp", "tools": ["get_property_detail", "get_lien_stack", "get_owner_intel", "get_zoning"], "rpc": ["title_search_snapshot"]},
        "sections": ["subject_identification", "transaction_history", "property_record", "context_layers", "zonewise", "judgment_encumbrance"],
        "input": {"type": "object", "properties": {"county": {"type": "string"}, "case_number": {"type": "string"}, "parcel_id": {"type": "string"}, "address": {"type": "string"}, "question": {"type": "string"}}, "required": []},
    },
    "data_analyst": {
        "twin_of": "ATTOM Data Analyst Agent",
        "description": "County / ZIP / metro aggregates. Distressed clearing ratios (sold-to-assessed, sold-to-judgment, third-party share) from verified FL auction outcomes; retail sale stats; Layer 3 live-market fields print Pending when the layer is absent.",
        "schema": "data_analyst.json",
        "live": {"mcp": "https://mcp.biddeed.ai/api/mcp", "tools": ["get_market_stats", "get_county_summary"], "rpc": ["auctions_summary_ssot", "auctions_calendar_counts"]},
        "sections": ["market_and_comps", "auction_outcome"],
        "input": {"type": "object", "properties": {"geography_level": {"enum": ["county", "zip", "metro", "state"]}, "geography": {"type": "string"}, "sale_type": {"enum": ["foreclosure", "tax_deed", "both"]}, "since": {"type": "string"}, "compare_to": {"type": "array", "items": {"type": "string"}}}, "required": ["geography_level", "geography"]},
    },
    "report_generation": {
        "twin_of": "ATTOM Report Generation Agent",
        "description": "The SIGNAL$ Property Report envelope (18 sections, HTML + PDF + JSON) with ATTOM's six blocks mapped in. Production render: predict_auction_outcome → composer.js → pdf.js / S5Report.tsx.",
        "schema": "report_generation.json",
        "live": {"mcp": "https://mcp.biddeed.ai/api/mcp", "tools": ["predict_auction_outcome"], "rpc": ["v_s5_report_template"]},
        "sections": ["*"],
        "input": {"type": "object", "properties": {"county": {"type": "string"}, "case_number": {"type": "string"}, "format": {"enum": ["json", "html", "pdf"]}}, "required": ["county", "case_number"]},
    },
    # SIGNAL$-only — no ATTOM twin
    "search_auctions": {
        "twin_of": None,
        "description": "Upcoming FL foreclosure + tax-deed auctions by county / window / price cap, with certification stamp per row.",
        "live": {"mcp": "https://mcp.biddeed.ai/api/mcp", "tools": ["search_auctions"], "rpc": ["auctions_calendar_counts"]},
        "input": {"type": "object", "properties": {"county": {"type": "string"}, "days": {"type": "integer"}, "sale_type": {"enum": ["foreclosure", "tax_deed", "both"]}, "max_opening_bid": {"type": "number"}}, "required": []},
    },
    "score_deal": {
        "twin_of": None,
        "description": "Verdict BID/REVIEW/SKIP, entry bid, SIGNAL$ Max Bid, walk-away, model id, probability (printed only when the validation gate has passed; else WITHHELD).",
        "live": {"mcp": "https://mcp.biddeed.ai/api/mcp", "tools": ["predict_auction_outcome"], "rpc": []},
        "sections": ["value_estimate", "bid_card", "shapira_ml"],
        "input": {"type": "object", "properties": {"county": {"type": "string"}, "case_number": {"type": "string"}}, "required": ["county", "case_number"]},
    },
    "title_lien_priority": {
        "twin_of": None,
        "description": "Ordered lien stack: FORECLOSING / SENIOR / JUNIOR / RELEASED / SUPER_PRIORITY + statute + joinder vs LP party list. UNRESOLVED is a first-class answer.",
        "live": {"mcp": "https://mcp.biddeed.ai/api/mcp", "tools": ["get_title_chain", "get_lien_stack"], "rpc": ["title_lien_priority", "title_search_snapshot"]},
        "sections": ["judgment_encumbrance"],
        "input": {"type": "object", "properties": {"mca_id": {"type": "string"}}, "required": ["mca_id"]},
    },
    "parcel_zoning": {
        "twin_of": None,
        "description": "ZoneWise.AI: DOR land use, jurisdiction, district assignment (or PENDING), just value, envelope where built.",
        "live": {"mcp": "https://mcp.biddeed.ai/api/mcp", "tools": ["get_zoning", "get_far"], "rpc": []},
        "sections": ["zonewise"],
        "input": {"type": "object", "properties": {"parcel_id": {"type": "string"}, "county": {"type": "string"}}, "required": ["parcel_id", "county"]},
    },
}

ATTOM_TWINS = [k for k, v in TOOLS.items() if v["twin_of"]]
SIGNAL_ONLY = [k for k, v in TOOLS.items() if not v["twin_of"]]


def load_samples() -> dict[str, Any]:
    return json.loads(SAMPLES.read_text(encoding="utf-8"))


def load_schema(name: str) -> dict[str, Any]:
    return json.loads((SCHEMAS / name).read_text(encoding="utf-8"))


def dispatch(tool: str, args: dict[str, Any] | None = None) -> dict[str, Any]:
    """Sample dispatcher. With BIDDEED_MCP_URL + BIDDEED_MCP_KEY set, forwards to
    the live surface; otherwise returns the illustrative sample so the shape can
    be exercised without credentials. The sample is labelled as such."""
    args = args or {}
    if tool not in TOOLS:
        return {"error": f"unknown tool '{tool}'", "known": sorted(TOOLS)}
    live_url, live_key = os.getenv("BIDDEED_MCP_URL"), os.getenv("BIDDEED_MCP_KEY")
    if live_url and live_key:
        return _forward_live(tool, args, live_url, live_key)
    samples = load_samples() if SAMPLES.exists() else {"_notice": "samples not vendored in this repo — see biddeed-attom-agent-reports"}
    if tool in samples:
        return {"_sample": True, "_notice": samples["_notice"], "tool": tool, "result": samples[tool]}
    return {"_sample": True, "tool": tool, "result": {"status": "Pending — sample payload not authored for this SIGNAL$-only tool; use the live surface"}}


def _forward_live(tool: str, args: dict[str, Any], url: str, key: str) -> dict[str, Any]:
    """Minimal JSON-RPC forward to mcp.biddeed.ai (tools/call). Kept dependency-free."""
    import urllib.request

    live_tool = TOOLS[tool]["live"]["tools"][0]
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": live_tool, "arguments": args}}).encode()
    req = urllib.request.Request(url, data=body, headers={"content-type": "application/json", "authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310 — operator-configured URL
        return {"_sample": False, "tool": tool, "live_tool": live_tool, "result": json.loads(r.read())}


def trademark_check(payload: Any) -> int:
    """Customer-facing gate: count of the national vendor's name in any payload. Must be 0."""
    return json.dumps(payload).lower().count("attom")
