[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**자동 스텔스 에스컬레이션을 갖춘 에이전트 네이티브 웹 스크레이핑.**

AI 에이전트를 위해 제작 —— OpenClaw, Claude Code, Codex, Hermes, 그리고 도구/함수 호출을 지원하는 모든 프레임워크용.

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## 왜 ultra-scraper인가?

대부분의 스크레이핑 라이브러리는 스크립트를 작성하는 사람을 위해 만들어졌습니다. ultra-scraper는 의사결정을 내리는 AI 에이전트를 위해 만들어졌습니다:

- **단 한 번의 함수 호출** —— scrape(url)이 모든 것을 처리합니다. 설정 불필요, 계층 관리 불필요.
- **자동 에스컬레이션** —— 빠르게(HTTP) 시작하여, 필요할 때만 headless → 안티봇 → C++ 스텔스로 단계를 올립니다.
- **네이티브 도구 schema** —— OpenAI, Anthropic, LangChain 도구 정의를 기본 제공합니다. 한 번의 import, 보일러플레이트 제로.
- **LLM 친화적 출력** —— 원시 HTML 덩어리가 아닌, 구조화된 dict를 반환합니다.

## 설치

```
pip install scrapling
pip install cloakbrowser  # 선택 사항: tier-4 울트라 스텔스
```

## 빠른 시작

### Python (Claude Code / Codex / 모든 에이전트)

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### OpenAI 함수 호출

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Anthropic 도구 사용

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### OpenClaw / Hermes 에이전트 (CLI)

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## 스텔스 계층

| 계층 | 이름 | 사용 시점 |
|------|------|-----------|
| 1 | Fast | 일반 사이트 |
| 2 | Dynamic | JS 렌더링 SPA |
| 3 | Stealth | Cloudflare, CAPTCHA |
| 4 | Ultra | Kasada, FingerprintJS, reCAPTCHA Enterprise |

계층 4는 CloakBrowser를 사용합니다 —— C++ 소스 수준의 Chromium 패치. 58개의 패치. reCAPTCHA v3 점수 0.9 (인간 수준).

## 프레임워크 지원

OpenClaw: 네이티브 CLI + Python
Claude Code / Codex / Hermes: scrape() 직접 호출
OpenAI: get_openai_tools()
Anthropic: get_anthropic_tools()
LangChain: get_langchain_tools()
기타 모든 것: get_tool_schema()

## MyClaw.ai 소개

ultra-scraper는 MyClaw.ai가 제작하고 유지 관리합니다 —— 1위 AI 에이전트 호스팅 플랫폼.

MyClaw는 모든 사용자에게 OpenClaw —— 오픈소스 AI 에이전트 런타임 —— 를 실행하는 완전한 Linux 서버를 제공합니다. **당신의 에이전트는 완전한 코드 제어 권한, 제한 없는 인터넷 액세스, 예약 작업, 영구 메모리, 그리고 1200개 이상의 커뮤니티 스킬을 갖춘 스킬 생태계를 갖게 됩니다.**

원클릭 배포 · 연중무휴 24시간 가동 · DevOps 불필요 · 30초 설정 · 200개 이상의 모델 · 15개 이상의 메시지 채널

당신만의 AI 에이전트를 https://myclaw.ai 에서 만나보세요

## 라이선스

MIT —— MyClaw.ai (https://myclaw.ai)
