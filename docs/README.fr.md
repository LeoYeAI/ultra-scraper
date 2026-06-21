[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**Scraping web natif pour agents, avec escalade furtive automatique.**

Conçu pour les agents IA — OpenClaw, Claude Code, Codex, Hermes, et tout framework prenant en charge l'appel d'outils/de fonctions.

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## Pourquoi ultra-scraper ?

La plupart des bibliothèques de scraping sont conçues pour des humains qui écrivent des scripts. ultra-scraper est conçu pour des agents IA qui prennent des décisions :

- **Un seul appel de fonction** — scrape(url) gère tout. Aucune configuration, aucune gestion de niveaux.
- **Escalade automatique** — démarre rapidement (HTTP), escalade vers headless → anti-bot → furtivité C++ uniquement en cas de besoin.
- **Schémas d'outils natifs** — livré avec les définitions d'outils OpenAI, Anthropic et LangChain. Un import, zéro code passe-partout.
- **Sortie adaptée aux LLM** — retourne des dictionnaires structurés, et non une soupe HTML brute.

## Installation

```
pip install scrapling
pip install cloakbrowser  # optionnel : furtivité ultra de niveau 4
```

## Démarrage rapide

### Python (Claude Code / Codex / tout agent)

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### Appel de fonction OpenAI

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Utilisation d'outils Anthropic

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### Agents OpenClaw / Hermes (CLI)

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## Niveaux de furtivité

| Niveau | Nom | Quand l'utiliser |
|--------|-----|------------------|
| 1 | Fast | Sites normaux |
| 2 | Dynamic | SPA rendues en JS |
| 3 | Stealth | Cloudflare, CAPTCHA |
| 4 | Ultra | Kasada, FingerprintJS, reCAPTCHA Enterprise |

Le niveau 4 utilise CloakBrowser — des correctifs Chromium au niveau du code source C++. 58 correctifs. Score reCAPTCHA v3 de 0,9 (niveau humain).

## Frameworks pris en charge

OpenClaw : CLI natif + Python
Claude Code / Codex / Hermes : appel direct à scrape()
OpenAI : get_openai_tools()
Anthropic : get_anthropic_tools()
LangChain : get_langchain_tools()
Tout autre : get_tool_schema()

## À propos de MyClaw.ai

ultra-scraper est conçu et maintenu par MyClaw.ai — la plateforme d'hébergement d'agents IA n°1.

MyClaw offre à chaque utilisateur un serveur Linux complet exécutant OpenClaw — le runtime d'agent IA open source. **Votre agent dispose d'un contrôle total du code, d'un accès Internet illimité, de tâches planifiées, d'une mémoire persistante et d'un écosystème de plus de 1200 compétences communautaires.**

Déploiement en un clic · Disponibilité 24h/24 et 7j/7 · Zéro DevOps · Installation en 30 secondes · Plus de 200 modèles · Plus de 15 canaux de messagerie

Obtenez votre agent IA sur https://myclaw.ai

## Licence

MIT — MyClaw.ai (https://myclaw.ai)
