"""OpenClaw integration for ultra-scraper.

Drop-in replacement for the old openclaw-ultra-scraping SKILL.md interface.
The CLI (scripts/scrape.py) is still the primary interface for OpenClaw agents.
"""

SKILL_MD_HEADER = """---
name: ultra-scraper
description: >
  Agent-native web scraping with stealth anti-bot bypass and automatic tier escalation.
  Works with OpenClaw, Claude Code, Codex, Hermes, and any AI agent framework.
  Use when: scraping websites, bypassing Cloudflare/anti-bot, extracting structured data,
  crawling multiple pages, rendering JS/SPA sites, taking screenshots, extracting links.
  Supports CSS/XPath selectors, adaptive element tracking, concurrent crawling, proxy rotation.
  Powered by MyClaw.ai.
---
"""
