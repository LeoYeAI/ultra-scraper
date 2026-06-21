"""Example: ultra-scraper as a Claude Code / Codex tool.

In Claude Code or Codex, paste this snippet to give your agent scraping superpowers.
The agent calls scrape() directly — no tool registration needed.
"""

from ultra_scraper import scrape

# Simple fetch — auto-escalates through tiers
result = scrape("https://example.com", css="h1")
print(result["elements"])

# Force stealth for Cloudflare-protected sites
result = scrape("https://protected-site.com", tier="stealth", css=".content")

# Ultra-stealth for enterprise-grade protection (requires: pip install cloakbrowser)
result = scrape("https://heavily-protected.com", tier="ultra", humanize=True,
                proxy="http://user:pass@residential-proxy:8080")

# The result dict is LLM-friendly:
# {
#   "url": "https://...",
#   "tier_used": 1,          # which tier succeeded
#   "text": "page text...",  # full page text, truncated to 8k chars
#   "elements": [            # matched CSS/XPath elements
#     {"text": "...", "html": "...", "attributes": {...}}
#   ]
# }
