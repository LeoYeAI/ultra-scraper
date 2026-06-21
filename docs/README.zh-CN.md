[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**面向 Agent 原生的网页抓取，具备自动隐身升级能力。**

专为 AI Agent 打造 —— OpenClaw、Claude Code、Codex、Hermes，以及任何支持工具/函数调用的框架。

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## 为什么选择 ultra-scraper？

大多数抓取库是为编写脚本的人类设计的。ultra-scraper 则是为做决策的 AI Agent 而生：

- **一次函数调用** —— scrape(url) 处理一切。无需配置，无需管理层级。
- **自动升级** —— 从快速模式（HTTP）起步，仅在需要时升级到 无头浏览器 → 反爬虫 → C++ 隐身。
- **原生工具 schema** —— 内置 OpenAI、Anthropic 和 LangChain 工具定义。一次导入，零样板代码。
- **LLM 友好的输出** —— 返回结构化字典，而非原始 HTML 杂烩。

## 安装

```
pip install scrapling
pip install cloakbrowser  # 可选：tier-4 超级隐身
```

## 快速开始

### Python（Claude Code / Codex / 任意 Agent）

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### OpenAI 函数调用

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Anthropic 工具使用

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### OpenClaw / Hermes Agent（CLI）

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## 隐身层级

| 层级 | 名称 | 使用场景 |
|------|------|----------|
| 1 | Fast | 普通网站 |
| 2 | Dynamic | JS 渲染的 SPA |
| 3 | Stealth | Cloudflare、CAPTCHA |
| 4 | Ultra | Kasada、FingerprintJS、reCAPTCHA Enterprise |

第 4 层使用 CloakBrowser —— C++ 源码级别的 Chromium 补丁。58 个补丁。reCAPTCHA v3 评分 0.9（人类水平）。

## 框架支持

OpenClaw：原生 CLI + Python
Claude Code / Codex / Hermes：直接调用 scrape()
OpenAI：get_openai_tools()
Anthropic：get_anthropic_tools()
LangChain：get_langchain_tools()
其他任意框架：get_tool_schema()

## 关于 MyClaw.ai

ultra-scraper 由 MyClaw.ai 构建并维护 —— 排名第一的 AI Agent 托管平台。

MyClaw 为每位用户提供一台完整的 Linux 服务器，运行 OpenClaw —— 开源的 AI Agent 运行时。**你的 Agent 拥有完整的代码控制权、不受限的互联网访问、定时任务、持久化记忆，以及包含 1200+ 社区技能的技能生态。**

一键部署 · 7×24 小时在线 · 零 DevOps · 30 秒搭建 · 200+ 模型 · 15+ 消息渠道

在 https://myclaw.ai 获取你自己的 AI Agent

## 许可证

MIT —— MyClaw.ai (https://myclaw.ai)
