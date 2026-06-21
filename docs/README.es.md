[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**Web scraping nativo para agentes con escalado furtivo automático.**

Creado para agentes de IA — OpenClaw, Claude Code, Codex, Hermes y cualquier framework que admita la invocación de herramientas/funciones.

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## ¿Por qué ultra-scraper?

La mayoría de las bibliotecas de scraping están hechas para humanos que escriben scripts. ultra-scraper está hecho para agentes de IA que toman decisiones:

- **Una sola llamada de función** — scrape(url) lo gestiona todo. Sin configuración, sin gestión de niveles.
- **Escalado automático** — empieza rápido (HTTP) y escala a headless → anti-bot → furtividad en C++ solo cuando es necesario.
- **Esquemas de herramientas nativos** — incluye definiciones de herramientas para OpenAI, Anthropic y LangChain. Una importación, cero código repetitivo.
- **Salida apta para LLM** — devuelve diccionarios estructurados, no una sopa de HTML en bruto.

## Instalación

```
pip install scrapling
pip install cloakbrowser  # opcional: ultra-furtividad de nivel 4
```

## Inicio rápido

### Python (Claude Code / Codex / cualquier agente)

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### Invocación de funciones de OpenAI

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Uso de herramientas de Anthropic

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### Agentes OpenClaw / Hermes (CLI)

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## Niveles de furtividad

| Nivel | Nombre | Cuándo se usa |
|-------|--------|---------------|
| 1 | Fast | Sitios normales |
| 2 | Dynamic | SPA renderizadas con JS |
| 3 | Stealth | Cloudflare, CAPTCHA |
| 4 | Ultra | Kasada, FingerprintJS, reCAPTCHA Enterprise |

El nivel 4 usa CloakBrowser — parches de Chromium a nivel de código fuente C++. 58 parches. Puntuación reCAPTCHA v3 de 0,9 (nivel humano).

## Frameworks compatibles

OpenClaw: CLI nativo + Python
Claude Code / Codex / Hermes: llamada directa a scrape()
OpenAI: get_openai_tools()
Anthropic: get_anthropic_tools()
LangChain: get_langchain_tools()
Cualquier otro: get_tool_schema()

## Acerca de MyClaw.ai

ultra-scraper está creado y mantenido por MyClaw.ai — la plataforma de hosting de agentes de IA n.º 1.

MyClaw ofrece a cada usuario un servidor Linux completo que ejecuta OpenClaw — el runtime de agentes de IA de código abierto. **Tu agente obtiene control total del código, acceso ilimitado a Internet, tareas programadas, memoria persistente y un ecosistema con más de 1200 skills de la comunidad.**

Despliegue con un clic · Disponibilidad 24/7 · Cero DevOps · Configuración en 30 segundos · Más de 200 modelos · Más de 15 canales de mensajería

Consigue tu agente de IA en https://myclaw.ai

## Licencia

MIT — MyClaw.ai (https://myclaw.ai)
