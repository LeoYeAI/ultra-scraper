#!/usr/bin/env bash
# ultra-scraper — one-shot setup
# Installs scraping dependencies into /opt/scrapling-venv

set -e

VENV="/opt/scrapling-venv"
SCRAPLING_BIN="$VENV/bin/scrapling"

if [ -f "$SCRAPLING_BIN" ]; then
  echo "✅ Scraping engine already installed at $VENV"
  "$VENV/bin/python3" -c "import scrapling; print(f'  Version: {scrapling.__version__}')" 2>/dev/null || true
  exit 0
fi

echo "🔧 Installing system dependencies..."
apt-get update -qq
apt-get install -y -qq python3.12-venv python3-full \
  libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 \
  libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
  libgbm1 libcairo2 libpango-1.0-0 libasound2t64 2>/dev/null

echo "🐍 Creating virtualenv at $VENV..."
python3 -m venv "$VENV"

echo "📦 Installing scraping engine..."
"$VENV/bin/pip" install --quiet "scrapling[all]"

echo "🌐 Installing browsers..."
"$VENV/bin/scrapling" install

echo ""
echo "✅ Core setup complete!"
echo "   Scrapling $(\"$VENV/bin/python3\" -c 'import scrapling; print(scrapling.__version__)') ready"
echo ""
echo "Optional: Install CloakBrowser for tier-4 ultra-stealth (enterprise-grade anti-bot):"
echo "   pip install cloakbrowser   # ~200MB, one-time download"
