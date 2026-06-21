"""Native tool definitions for AI agent frameworks.

Exports scrape() as tool/function calling schemas for:
- OpenAI (function calling / responses API)
- Anthropic (tool use)
- LangChain (Tool / StructuredTool)
- Generic (dict schema, works with any framework)
"""

from __future__ import annotations
from typing import Any
from .scraper import scrape, scrape_async

# ---------------------------------------------------------------------------
# Shared schema
# ---------------------------------------------------------------------------

_SCRAPE_PARAMS = {
    "url": {
        "type": "string",
        "description": "The URL to scrape.",
    },
    "css": {
        "type": "string",
        "description": "CSS selector to extract specific elements. Optional.",
    },
    "xpath": {
        "type": "string",
        "description": "XPath selector to extract specific elements. Optional.",
    },
    "tier": {
        "type": "string",
        "enum": ["auto", "fast", "dynamic", "stealth", "ultra"],
        "description": (
            "Stealth tier. Use 'auto' (default) to let the library escalate automatically. "
            "'fast'=HTTP only, 'dynamic'=headless browser, 'stealth'=anti-bot bypass, "
            "'ultra'=C++ source-level stealth (requires pip install cloakbrowser)."
        ),
    },
    "proxy": {
        "type": "string",
        "description": "Proxy URL, e.g. 'http://user:pass@host:port' or 'socks5://host:port'. Optional.",
    },
    "humanize": {
        "type": "boolean",
        "description": "Use human-like mouse and keyboard behavior. Only applies to tier='ultra'.",
    },
}

_SCRAPE_DESCRIPTION = (
    "Scrape a web page and return its content. "
    "Automatically escalates through stealth tiers (HTTP → headless → anti-bot → C++ stealth) "
    "until the page is successfully fetched. "
    "Returns html, text, and a list of extracted elements."
)


def _run_scrape(url: str, css: str | None = None, xpath: str | None = None,
                tier: str = "auto", proxy: str | None = None,
                humanize: bool = False) -> str:
    """Execute scrape and return JSON string (suitable for tool output)."""
    import json
    result = scrape(url, css=css, xpath=xpath, tier=tier,
                    proxy=proxy, humanize=humanize)
    # Trim html for LLM context efficiency
    output = {
        "url": result["url"],
        "tier_used": result["tier"],
        "text": result["text"][:8000] if result["text"] else "",
        "elements": result["elements"][:50],
    }
    return json.dumps(output, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# OpenAI function calling
# ---------------------------------------------------------------------------

def get_openai_tools() -> list[dict]:
    """Return tool definitions in OpenAI function calling format.

    Usage:
        from ultra_scraper import get_openai_tools
        from openai import OpenAI

        client = OpenAI()
        tools = get_openai_tools()

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Scrape https://example.com"}],
            tools=tools,
        )
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "scrape",
                "description": _SCRAPE_DESCRIPTION,
                "parameters": {
                    "type": "object",
                    "properties": _SCRAPE_PARAMS,
                    "required": ["url"],
                },
            },
        }
    ]


def handle_openai_tool_call(tool_call: Any) -> str:
    """Execute a tool call from an OpenAI response and return the result string."""
    import json
    args = json.loads(tool_call.function.arguments)
    return _run_scrape(**args)


# ---------------------------------------------------------------------------
# Anthropic tool use
# ---------------------------------------------------------------------------

def get_anthropic_tools() -> list[dict]:
    """Return tool definitions in Anthropic tool use format.

    Usage:
        from ultra_scraper import get_anthropic_tools
        import anthropic

        client = anthropic.Anthropic()
        tools = get_anthropic_tools()

        response = client.messages.create(
            model="claude-opus-4-5",
            max_tokens=1024,
            tools=tools,
            messages=[{"role": "user", "content": "Scrape https://example.com"}],
        )
    """
    return [
        {
            "name": "scrape",
            "description": _SCRAPE_DESCRIPTION,
            "input_schema": {
                "type": "object",
                "properties": _SCRAPE_PARAMS,
                "required": ["url"],
            },
        }
    ]


def handle_anthropic_tool_use(tool_use_block: Any) -> str:
    """Execute a tool_use block from an Anthropic response and return the result string."""
    return _run_scrape(**tool_use_block.input)


# ---------------------------------------------------------------------------
# LangChain
# ---------------------------------------------------------------------------

def get_langchain_tools() -> list:
    """Return a list of LangChain StructuredTool objects.

    Usage:
        from ultra_scraper import get_langchain_tools
        from langchain.agents import AgentExecutor, create_tool_calling_agent

        tools = get_langchain_tools()
    """
    try:
        from langchain.tools import StructuredTool
        from pydantic import BaseModel, Field

        class ScrapeInput(BaseModel):
            url: str = Field(description="The URL to scrape.")
            css: str | None = Field(default=None, description="CSS selector.")
            xpath: str | None = Field(default=None, description="XPath selector.")
            tier: str = Field(default="auto", description="Stealth tier: auto/fast/dynamic/stealth/ultra.")
            proxy: str | None = Field(default=None, description="Proxy URL.")
            humanize: bool = Field(default=False, description="Human-like behavior (ultra tier only).")

        return [
            StructuredTool(
                name="scrape",
                description=_SCRAPE_DESCRIPTION,
                args_schema=ScrapeInput,
                func=lambda **kw: _run_scrape(**kw),
                coroutine=lambda **kw: scrape_async(**kw),
            )
        ]
    except ImportError:
        raise ImportError("LangChain not installed. Run: pip install langchain")


# ---------------------------------------------------------------------------
# Generic (works with any framework that accepts dict schemas)
# ---------------------------------------------------------------------------

def get_tool_schema() -> dict:
    """Return the raw tool schema as a plain dict.

    Use this to manually integrate with any framework not listed above.
    """
    return {
        "name": "scrape",
        "description": _SCRAPE_DESCRIPTION,
        "parameters": {
            "type": "object",
            "properties": _SCRAPE_PARAMS,
            "required": ["url"],
        },
        "handler": _run_scrape,
    }
