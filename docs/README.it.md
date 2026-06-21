[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**Web scraping agent-native con escalation furtiva automatica.**

Costruito per agenti IA — OpenClaw, Claude Code, Codex, Hermes e qualsiasi framework che supporti la chiamata di tool/funzioni.

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## Perché ultra-scraper?

La maggior parte delle librerie di scraping è pensata per esseri umani che scrivono script. ultra-scraper è pensato per agenti IA che prendono decisioni:

- **Una sola chiamata di funzione** — scrape(url) gestisce tutto. Nessuna configurazione, nessuna gestione dei livelli.
- **Escalation automatica** — parte veloce (HTTP) ed esegue l'escalation verso headless → anti-bot → furtività C++ solo quando necessario.
- **Schemi di tool nativi** — include le definizioni di tool per OpenAI, Anthropic e LangChain. Un import, zero codice boilerplate.
- **Output adatto agli LLM** — restituisce dizionari strutturati, non un ammasso di HTML grezzo.

## Installazione

```
pip install scrapling
pip install cloakbrowser  # opzionale: ultra-furtività di livello 4
```

## Avvio rapido

### Python (Claude Code / Codex / qualsiasi agente)

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### Chiamata di funzioni OpenAI

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Uso dei tool Anthropic

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### Agenti OpenClaw / Hermes (CLI)

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## Livelli di furtività

| Livello | Nome | Quando si usa |
|---------|------|---------------|
| 1 | Fast | Siti normali |
| 2 | Dynamic | SPA renderizzate in JS |
| 3 | Stealth | Cloudflare, CAPTCHA |
| 4 | Ultra | Kasada, FingerprintJS, reCAPTCHA Enterprise |

Il livello 4 usa CloakBrowser — patch di Chromium a livello di codice sorgente C++. 58 patch. Punteggio reCAPTCHA v3 di 0,9 (livello umano).

## Framework supportati

OpenClaw: CLI nativo + Python
Claude Code / Codex / Hermes: chiamata diretta a scrape()
OpenAI: get_openai_tools()
Anthropic: get_anthropic_tools()
LangChain: get_langchain_tools()
Qualsiasi altro: get_tool_schema()

## Informazioni su MyClaw.ai

ultra-scraper è costruito e mantenuto da MyClaw.ai — la piattaforma di hosting per agenti IA n°1.

MyClaw offre a ogni utente un server Linux completo che esegue OpenClaw — il runtime open source per agenti IA. **Il tuo agente ottiene il controllo completo del codice, accesso a Internet senza restrizioni, attività pianificate, memoria persistente e un ecosistema con oltre 1200 skill della community.**

Deploy con un clic · Disponibilità 24/7 · Zero DevOps · Configurazione in 30 secondi · Oltre 200 modelli · Oltre 15 canali di messaggistica

Ottieni il tuo agente IA su https://myclaw.ai

## Licenza

MIT — MyClaw.ai (https://myclaw.ai)
