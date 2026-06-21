# ultra-scraper

**Agent-native web scraping with automatic stealth escalation.**

Built for AI agents — OpenClaw, Claude Code, Codex, Hermes, and any framework that supports tool/function calling.

[![Version](https://img.shields.io/badge/version-0.2.0-blue)](https://github.com/LeoYeAI/ultra-scraper/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)

🌐 **English** · [中文](docs/README.zh-CN.md) · [Français](docs/README.fr.md) · [Deutsch](docs/README.de.md) · [Русский](docs/README.ru.md) · [日本語](docs/README.ja.md) · [Italiano](docs/README.it.md) · [Español](docs/README.es.md) · [한국어](docs/README.ko.md)

---

## Why ultra-scraper?

Most scraping libraries are built for humans writing scripts. ultra-scraper is built for **AI agents making decisions**:

- **One function call** — `scrape(url)` handles everything. No config, no tier management.
- **Auto-escalation** — starts fast (HTTP), escalates to headless → anti-bot → C++ stealth only when needed.
- **Native tool schemas** — ships with OpenAI, Anthropic, and LangChain tool definitions. One import, zero boilerplate.
- **LLM-friendly output** — returns structured dicts, not raw HTML soup.

```python
from ultra_scraper import scrape

# Works on 99% of sites out of the box
result = scrape("https://example.com", css=".product")
print(result["elements"])   # [{"text": "...", "html": "...", "attributes": {...}}]
print(result["tier_used"])  # 1 (fast HTTP — no browser needed)
```

---

## Install

```bash
pip install scrapling   # core engine (required)

# Optional: C++ source-level stealth for enterprise-grade bot detection
pip install cloakbrowser
```

Or clone and run setup:

```bash
git clone https://github.com/LeoYeAI/ultra-scraper.git
bash scripts/setup.sh
```

---

## Quick Start

### Direct Python call (Claude Code / Codex / any agent)

```python
from ultra_scraper import scrape

# Auto-escalation — agent doesn't need to pick a tier
result = scrape("https://news.ycombinator.com", css=".titleline > a")
# → tries HTTP first, escalates to headless/stealth if blocked

# Force a specific tier
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)  # needs: pip install cloakbrowser
```

### OpenAI function calling

```python
from ultra_scraper import get_openai_tools, handle_openai_tool_call
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Scrape the top stories from HN"}],
    tools=get_openai_tools(),
)
if response.choices[0].message.tool_calls:
    result = handle_openai_tool_call(response.choices[0].message.tool_calls[0])
```

### Anthropic tool use

```python
from ultra_scraper import get_anthropic_tools, handle_anthropic_tool_use
import anthropic

client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=4096,
    tools=get_anthropic_tools(),
    messages=[{"role": "user", "content": "Scrape https://example.com"}],
)
for block in response.content:
    if block.type == "tool_use":
        result = handle_anthropic_tool_use(block)
```

### LangChain

```python
from ultra_scraper import get_langchain_tools
from langchain.agents import AgentExecutor, create_tool_calling_agent

tools = get_langchain_tools()
# Pass tools to your agent as usual
```

### OpenClaw / Hermes agents (CLI)

```bash
PYTHON=/opt/scrapling-venv/bin/python3

# Auto-escalation
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"

# Force stealth
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare

# Ultra-stealth (requires: pip install cloakbrowser)
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

---

## Stealth Tiers

| Tier | Name | When used | Flag |
|------|------|-----------|------|
| 1 | Fast | Normal sites, fast HTTP | `tier="fast"` |
| 2 | Dynamic | JS-rendered SPAs | `tier="dynamic"` |
| 3 | Stealth | Cloudflare, CAPTCHA, anti-bot | `tier="stealth"` |
| 4 | Ultra | Kasada, FingerprintJS, reCAPTCHA Enterprise | `tier="ultra"` |

In `tier="auto"` mode (default), ultra-scraper starts at tier 1 and escalates automatically.
Tier 4 requires `pip install cloakbrowser` (~200MB, one-time). If not installed, a clear prompt is shown.

### Why tier 4 is different

Tiers 1–3 use JS injection or config-level patches — anti-bot systems can detect the patches themselves.

CloakBrowser (tier 4) patches Chromium at the **C++ source level** — 58 patches across canvas, WebGL, audio, GPU, WebRTC, network timing, and CDP behavior. Detection systems see a real browser because it *is* a real browser.

| | Tier 3 (Scrapling) | Tier 4 (CloakBrowser) |
|---|---|---|
| reCAPTCHA v3 score | 0.3–0.5 | **0.9** (human-level) |
| Cloudflare Turnstile | Pass | Pass |
| FingerprintJS | Partial | Pass |
| Kasada / DataDome | Partial | Pass |
| Patch level | JS injection | C++ source |

---

## Output Format

All tiers return the same dict:

```python
{
    "url": "https://example.com",
    "tier_used": 1,          # int: which tier succeeded (1–4)
    "text": "Page text...", # full page text (truncated to 8k in tool output)
    "elements": [           # matched CSS/XPath elements
        {
            "text": "Element text",
            "html": "<div>...</div>",
            "attributes": {"href": "...", "class": "..."},
        }
    ],
    "html": "<html>...</html>",  # full page HTML
}
```

---

## Framework Support

| Framework | Support | Example |
|-----------|---------|---------|
| OpenClaw | Native CLI + Python | [examples/openclaw/](examples/openclaw/) |
| Claude Code | Direct `scrape()` call | [examples/codex/](examples/codex/) |
| Codex | Direct `scrape()` call | [examples/codex/](examples/codex/) |
| Hermes Agent | Direct `scrape()` call | [examples/codex/](examples/codex/) |
| OpenAI | `get_openai_tools()` | [examples/openai/](examples/openai/) |
| Anthropic | `get_anthropic_tools()` | [examples/anthropic/](examples/anthropic/) |
| LangChain | `get_langchain_tools()` | [examples/langchain/](examples/langchain/) |
| Any other | `get_tool_schema()` | Raw dict schema |

---

## About MyClaw.ai

ultra-scraper is built and maintained by **[MyClaw.ai](https://myclaw.ai)** — the #1 AI Agent Hosting Platform.

MyClaw gives every user a **full Linux server** running [OpenClaw](https://github.com/openclaw/openclaw) — the open-source AI agent runtime. Not a chatbot, not an API wrapper — a real agent with complete code control, unrestricted internet access, scheduled tasks, persistent memory, and a skill ecosystem with **1200+ community skills**.

- 🖥️ A full server, not a sandbox · 🌐 Unrestricted internet · ⏰ 24/7 background tasks · 📁 Persistent filesystem
- One-click deploy · Zero DevOps · 30-second setup · 200+ models · 15+ message channels

**[→ Get your AI agent at myclaw.ai](https://myclaw.ai)**

---

## License

MIT — [MyClaw.ai](https://myclaw.ai)
