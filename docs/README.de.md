[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**Agent-natives Web-Scraping mit automatischer Stealth-Eskalation.**

Entwickelt für KI-Agenten — OpenClaw, Claude Code, Codex, Hermes und jedes Framework, das Tool-/Funktionsaufrufe unterstützt.

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## Warum ultra-scraper?

Die meisten Scraping-Bibliotheken sind für Menschen gemacht, die Skripte schreiben. ultra-scraper ist für KI-Agenten gemacht, die Entscheidungen treffen:

- **Ein einziger Funktionsaufruf** — scrape(url) erledigt alles. Keine Konfiguration, keine Stufenverwaltung.
- **Automatische Eskalation** — startet schnell (HTTP) und eskaliert nur bei Bedarf zu Headless → Anti-Bot → C++-Stealth.
- **Native Tool-Schemas** — wird mit Tool-Definitionen für OpenAI, Anthropic und LangChain geliefert. Ein Import, null Boilerplate.
- **LLM-freundliche Ausgabe** — gibt strukturierte Dicts zurück, statt rohem HTML-Brei.

## Installation

```
pip install scrapling
pip install cloakbrowser  # optional: Ultra-Stealth der Stufe 4
```

## Schnellstart

### Python (Claude Code / Codex / beliebiger Agent)

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### OpenAI Function Calling

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Anthropic Tool Use

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### OpenClaw / Hermes Agenten (CLI)

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## Stealth-Stufen

| Stufe | Name | Einsatz |
|-------|------|---------|
| 1 | Fast | Normale Websites |
| 2 | Dynamic | JS-gerenderte SPAs |
| 3 | Stealth | Cloudflare, CAPTCHA |
| 4 | Ultra | Kasada, FingerprintJS, reCAPTCHA Enterprise |

Stufe 4 verwendet CloakBrowser — Chromium-Patches auf C++-Quellcode-Ebene. 58 Patches. reCAPTCHA-v3-Score von 0,9 (menschliches Niveau).

## Framework-Unterstützung

OpenClaw: Natives CLI + Python
Claude Code / Codex / Hermes: Direkter scrape()-Aufruf
OpenAI: get_openai_tools()
Anthropic: get_anthropic_tools()
LangChain: get_langchain_tools()
Beliebige andere: get_tool_schema()

## Über MyClaw.ai

ultra-scraper wird von MyClaw.ai entwickelt und gepflegt — der KI-Agent-Hosting-Plattform Nr. 1.

MyClaw gibt jedem Nutzer einen vollständigen Linux-Server mit OpenClaw — der Open-Source-Laufzeitumgebung für KI-Agenten. **Ihr Agent erhält vollständige Code-Kontrolle, uneingeschränkten Internetzugang, geplante Aufgaben, persistenten Speicher und ein Ökosystem mit über 1200 Community-Skills.**

Ein-Klick-Bereitstellung · 24/7-Verfügbarkeit · Null DevOps · Einrichtung in 30 Sekunden · Über 200 Modelle · Über 15 Nachrichtenkanäle

Holen Sie sich Ihren KI-Agenten unter https://myclaw.ai

## Lizenz

MIT — MyClaw.ai (https://myclaw.ai)
