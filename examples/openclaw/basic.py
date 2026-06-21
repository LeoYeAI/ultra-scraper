"""Example: ultra-scraper with OpenClaw agents.

OpenClaw agents use the CLI via scripts/scrape.py, or call scrape() directly in Python tasks.
"""

from ultra_scraper import scrape

# Called by OpenClaw agent during a task
def agent_scrape_task(url: str, selector: str | None = None) -> dict:
    """Scrape a URL and return structured data for the agent."""
    result = scrape(url, css=selector)
    return {
        "success": True,
        "tier_used": result["tier"],
        "content": result["text"][:4000],
        "elements": result["elements"][:20],
    }
