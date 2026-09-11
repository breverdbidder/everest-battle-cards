"""
biddeed-attom-mcp — stdio MCP server exposing the 7-tool parity map.

Run:   python -m mcp.server            (needs `pip install mcp`)
Env:   BIDDEED_MCP_URL / BIDDEED_MCP_KEY  → forward to the live surface
       (unset → illustrative samples, labelled `_sample: true`)

This is a STUB for mapping + bake-offs. Production stays at
https://mcp.biddeed.ai/api/mcp. Do not point customers here.
"""
from __future__ import annotations

import json
import sys

try:
    from mcp.server.fastmcp import FastMCP
except ImportError:  # keep the module importable for the tests without the SDK
    FastMCP = None  # type: ignore[assignment]

from .tools import TOOLS, dispatch, trademark_check

if FastMCP is not None:
    app = FastMCP("biddeed-attom-parity", instructions=(
        "SIGNAL$ Property Report parity layer. Three tools twin a national "
        "property-data vendor's agents; four have no twin (auction search, deal "
        "score with SIGNAL$ Max Bid, statute-cited lien priority, parcel zoning). "
        "Every answer prints Pending / UNRESOLVED / WITHHELD in-line where data is "
        "absent. Never invent coverage."
    ))

    def _make(tool_name: str):
        meta = TOOLS[tool_name]

        def _tool(arguments: dict | None = None) -> dict:
            out = dispatch(tool_name, arguments or {})
            out["_trademark_mentions"] = trademark_check(out)
            return out

        _tool.__name__ = tool_name
        _tool.__doc__ = meta["description"]
        return _tool

    for _name in TOOLS:
        app.tool(name=_name, description=TOOLS[_name]["description"])(_make(_name))


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if argv and argv[0] == "--list":
        print(json.dumps({k: {"twin_of": v["twin_of"], "sections": v.get("sections", [])} for k, v in TOOLS.items()}, indent=2))
        return 0
    if argv and argv[0] == "--call":
        tool = argv[1]
        args = json.loads(argv[2]) if len(argv) > 2 else {}
        print(json.dumps(dispatch(tool, args), indent=2))
        return 0
    if FastMCP is None:
        print("mcp SDK not installed: pip install mcp   (or use --list / --call)", file=sys.stderr)
        return 2
    app.run()  # stdio
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
