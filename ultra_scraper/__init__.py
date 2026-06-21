"""ultra-scraper — Agent-native web scraping library.

Stealth anti-bot bypass with automatic tier escalation and native tool calling
for OpenClaw, Claude Code, Codex, Hermes, and any AI agent framework.
"""

from .scraper import scrape, scrape_async
from .tools import get_openai_tools, get_anthropic_tools, get_langchain_tools

__version__ = "0.2.0"
__all__ = [
    "scrape",
    "scrape_async",
    "get_openai_tools",
    "get_anthropic_tools",
    "get_langchain_tools",
]
