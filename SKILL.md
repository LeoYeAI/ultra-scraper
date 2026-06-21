---
name: ultra-scraper
description: >
  Agent-native web scraping with stealth anti-bot bypass and automatic tier escalation.
  Works with OpenClaw, Claude Code, Codex, Hermes, and any AI agent framework.
  Use when: (1) scraping websites that block normal requests, (2) extracting structured
  data from web pages, (3) crawling multiple pages with concurrency, (4) taking
  screenshots of web pages, (5) extracting links, (6) any web scraping task that
  needs stealth/anti-detection, (7) user asks to scrape/crawl/extract from URLs,
  (8) need to bypass Cloudflare or other bot protection. Supports CSS/XPath selectors,
  adaptive element tracking, multi-session spiders, pause/resume crawls, proxy rotation,
  and async operations. Powered by MyClaw.ai.
---

# ultra-scraper

Agent-native web scraping. Handles everything from single-page extraction to full-scale concurrent crawls with automatic stealth escalation.

## Setup

Run once before first use:

```bash
bash scripts/setup.sh
```

## Quick Start — Python (Claude Code / Codex / Hermes)

```python
from ultra_scraper import scrape

# Auto-escalation — starts fast, escalates to stealth only if needed
result = scrape("https://example.com", css=".content")
print(result["elements"])
print(result["tier_used"])  # 1=fast, 2=dynamic, 3=stealth, 4=ultra
```

## Quick Start — CLI (OpenClaw / Hermes)

```bash
PYTHON=/opt/scrapling-venv/bin/python3

# Auto (default — escalates automatically)
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"

# Dynamic (full browser for JS/SPA sites)
$PYTHON scripts/scrape.py fetch "https://spa-site.com" --dynamic --css ".product"

# Stealth (bypass Cloudflare)
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare

# Ultra-stealth (Kasada / FingerprintJS / reCAPTCHA Enterprise)
# Requires: pip install cloakbrowser
$PYTHON scripts/scrape.py fetch "https://enterprise-protected.com" --ultra-stealth --humanize \
  --proxy "http://user:pass@residential:8080"

# Extract links
$PYTHON scripts/scrape.py links "https://example.com" --filter "\.pdf$"

# Multi-page crawl
$PYTHON scripts/scrape.py crawl "https://example.com" --depth 2 --concurrency 10 -o results.json

# Output formats: json, jsonl, csv, text, markdown, html
$PYTHON scripts/scrape.py fetch "https://example.com" -f markdown -o page.md
```

## Quick Start — Tool Calling (OpenAI / Anthropic)

```python
# OpenAI
from ultra_scraper import get_openai_tools
tools = get_openai_tools()  # pass to client.chat.completions.create(tools=...)

# Anthropic
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()  # pass to client.messages.create(tools=...)

# LangChain
from ultra_scraper import get_langchain_tools
tools = get_langchain_tools()
```

## Stealth Tier Guide

| Tier | Scenario | Python | CLI Flag |
|------|----------|--------|----------|
| 1 — Fast | Normal sites | `tier="fast"` | (default) |
| 2 — Dynamic | JS-rendered SPAs | `tier="dynamic"` | `--dynamic` |
| 3 — Stealth | Cloudflare / anti-bot | `tier="stealth"` | `--stealth` |
| 3 — Stealth+ | Cloudflare Turnstile | `tier="stealth"` | `--stealth --solve-cloudflare` |
| 4 — Ultra | Kasada / FingerprintJS / reCAPTCHA Enterprise | `tier="ultra"` | `--ultra-stealth` |

`tier="auto"` (default) starts at tier 1 and escalates automatically.

Tier 4 requires `pip install cloakbrowser` (~200MB, one-time).
When not installed, a clear install prompt is shown.

## Selector Cheat Sheet

```python
result = scrape("https://example.com", css=".class")
result = scrape("https://example.com", xpath='//div[@id="main"]')

# Via CLI
$PYTHON scripts/scrape.py fetch "url" --css ".class"
$PYTHON scripts/scrape.py fetch "url" --xpath '//div[@id="main"]'
```

## Output Format

```python
{
    "url": "https://...",
    "tier_used": 1,
    "text": "full page text",
    "elements": [{"text": "...", "html": "...", "attributes": {...}}],
    "html": "<html>...</html>",
}
```

For full API details: see `README.md` and `examples/`
