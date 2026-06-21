[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**Нативный для агентов веб-скрейпинг с автоматической эскалацией стелс-режима.**

Создан для ИИ-агентов — OpenClaw, Claude Code, Codex, Hermes и любого фреймворка, поддерживающего вызов инструментов/функций.

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## Почему ultra-scraper?

Большинство библиотек для скрейпинга создано для людей, пишущих скрипты. ultra-scraper создан для ИИ-агентов, принимающих решения:

- **Один вызов функции** — scrape(url) делает всё. Без настройки, без управления уровнями.
- **Автоэскалация** — стартует быстро (HTTP) и переходит к headless → анти-бот → C++-стелс только при необходимости.
- **Нативные схемы инструментов** — поставляется с определениями инструментов для OpenAI, Anthropic и LangChain. Один импорт, ноль шаблонного кода.
- **Вывод, удобный для LLM** — возвращает структурированные словари, а не сырую HTML-кашу.

## Установка

```
pip install scrapling
pip install cloakbrowser  # опционально: ультра-стелс уровня 4
```

## Быстрый старт

### Python (Claude Code / Codex / любой агент)

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### Вызов функций OpenAI

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Использование инструментов Anthropic

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### Агенты OpenClaw / Hermes (CLI)

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## Уровни стелс-режима

| Уровень | Название | Когда используется |
|---------|----------|--------------------|
| 1 | Fast | Обычные сайты |
| 2 | Dynamic | SPA с JS-рендерингом |
| 3 | Stealth | Cloudflare, CAPTCHA |
| 4 | Ultra | Kasada, FingerprintJS, reCAPTCHA Enterprise |

Уровень 4 использует CloakBrowser — патчи Chromium на уровне исходного кода C++. 58 патчей. Оценка reCAPTCHA v3 — 0,9 (человеческий уровень).

## Поддержка фреймворков

OpenClaw: нативный CLI + Python
Claude Code / Codex / Hermes: прямой вызов scrape()
OpenAI: get_openai_tools()
Anthropic: get_anthropic_tools()
LangChain: get_langchain_tools()
Любой другой: get_tool_schema()

## О MyClaw.ai

ultra-scraper создан и поддерживается MyClaw.ai — платформой хостинга ИИ-агентов №1.

MyClaw предоставляет каждому пользователю полноценный Linux-сервер с OpenClaw — открытой средой выполнения ИИ-агентов. **Ваш агент получает полный контроль над кодом, неограниченный доступ в интернет, запланированные задачи, постоянную память и экосистему из более чем 1200 сообществ-навыков.**

Развёртывание в один клик · Работа 24/7 · Ноль DevOps · Настройка за 30 секунд · Более 200 моделей · Более 15 каналов сообщений

Получите своего ИИ-агента на https://myclaw.ai

## Лицензия

MIT — MyClaw.ai (https://myclaw.ai)
