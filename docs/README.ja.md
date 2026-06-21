[English](../README.md) · [中文](README.zh-CN.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Русский](README.ru.md) · [日本語](README.ja.md) · [Italiano](README.it.md) · [Español](README.es.md) · [한국어](README.ko.md)

# ultra-scraper

**エージェントネイティブなウェブスクレイピング、自動ステルスエスカレーション搭載。**

AI エージェントのために構築 —— OpenClaw、Claude Code、Codex、Hermes、そしてツール/関数呼び出しをサポートするあらゆるフレームワーク向け。

[![Powered by MyClaw.ai](https://img.shields.io/badge/Powered%20by-MyClaw.ai-purple)](https://myclaw.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)

## なぜ ultra-scraper なのか？

ほとんどのスクレイピングライブラリは、スクリプトを書く人間のために作られています。ultra-scraper は、意思決定を行う AI エージェントのために作られています：

- **たった一度の関数呼び出し** —— scrape(url) がすべてを処理します。設定不要、階層管理不要。
- **自動エスカレーション** —— 高速（HTTP）で起動し、必要なときだけ headless → アンチボット → C++ ステルスへとエスカレートします。
- **ネイティブなツール schema** —— OpenAI、Anthropic、LangChain のツール定義を同梱。インポート一つ、ボイラープレートはゼロ。
- **LLM フレンドリーな出力** —— 生の HTML の寄せ集めではなく、構造化された dict を返します。

## インストール

```
pip install scrapling
pip install cloakbrowser  # オプション: tier-4 ウルトラステルス
```

## クイックスタート

### Python（Claude Code / Codex / 任意のエージェント）

```python
from ultra_scraper import scrape
result = scrape("https://example.com", css=".product")
result = scrape("https://protected.com", tier="stealth")
result = scrape("https://enterprise.com", tier="ultra", humanize=True)
```

### OpenAI 関数呼び出し

```python
from ultra_scraper import get_openai_tools
tools = get_openai_tools()
```

### Anthropic ツール使用

```python
from ultra_scraper import get_anthropic_tools
tools = get_anthropic_tools()
```

### OpenClaw / Hermes エージェント（CLI）

```
$PYTHON scripts/scrape.py fetch "https://example.com" --css ".content"
$PYTHON scripts/scrape.py fetch "https://protected.com" --stealth --solve-cloudflare
$PYTHON scripts/scrape.py fetch "https://enterprise.com" --ultra-stealth --humanize
```

## ステルス階層

| 階層 | 名称 | 使用場面 |
|------|------|----------|
| 1 | Fast | 通常のサイト |
| 2 | Dynamic | JS レンダリングの SPA |
| 3 | Stealth | Cloudflare、CAPTCHA |
| 4 | Ultra | Kasada、FingerprintJS、reCAPTCHA Enterprise |

階層 4 は CloakBrowser を使用 —— C++ ソースレベルの Chromium パッチ。58 個のパッチ。reCAPTCHA v3 スコア 0.9（人間レベル）。

## フレームワークサポート

OpenClaw: ネイティブ CLI + Python
Claude Code / Codex / Hermes: 直接 scrape() 呼び出し
OpenAI: get_openai_tools()
Anthropic: get_anthropic_tools()
LangChain: get_langchain_tools()
その他すべて: get_tool_schema()

## MyClaw.ai について

ultra-scraper は MyClaw.ai によって構築・保守されています —— ナンバーワンの AI エージェントホスティングプラットフォーム。

MyClaw はすべてのユーザーに、OpenClaw —— オープンソースの AI エージェントランタイム —— を実行する完全な Linux サーバーを提供します。**あなたのエージェントは、完全なコード制御、無制限のインターネットアクセス、スケジュールされたタスク、永続的なメモリ、そして 1200 以上のコミュニティスキルを持つスキルエコシステムを手に入れます。**

ワンクリックデプロイ · 24時間365日稼働 · DevOps 不要 · 30秒でセットアップ · 200以上のモデル · 15以上のメッセージチャネル

あなた専用の AI エージェントを https://myclaw.ai で手に入れましょう

## ライセンス

MIT —— MyClaw.ai (https://myclaw.ai)
