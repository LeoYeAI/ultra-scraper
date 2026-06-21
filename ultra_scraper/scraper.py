"""Core scraping engine with 4-tier auto-escalation.

Tier 1: Fetcher          — fast HTTP, TLS fingerprint impersonation
Tier 2: DynamicFetcher   — full headless browser, JS/SPA rendering
Tier 3: StealthyFetcher  — anti-bot bypass (Cloudflare Turnstile, CAPTCHA)
Tier 4: CloakBrowser     — C++ source-level Chromium patches (optional)
                           install: pip install cloakbrowser
"""

from __future__ import annotations

import sys
import base64
import json
from typing import Any

VENV_SITE = "/opt/scrapling-venv/lib/python3.12/site-packages"
if VENV_SITE not in sys.path:
    sys.path.insert(0, VENV_SITE)

CLOAKBROWSER_INSTALL_MSG = """
┌─────────────────────────────────────────────────────────────┐
│  CloakBrowser not installed — ultra-stealth unavailable     │
│                                                             │
│  This site uses enterprise-grade bot detection              │
│  (Kasada / FingerprintJS / reCAPTCHA Enterprise) that       │
│  requires C++ source-level Chromium patches to bypass.      │
│                                                             │
│  Install CloakBrowser (one-time, ~200MB):                   │
│                                                             │
│    pip install cloakbrowser                                 │
│                                                             │
│  Then retry with:  tier="ultra"                             │
└─────────────────────────────────────────────────────────────┘
"""

BLOCKED_SIGNALS = [
    "cloudflare", "turnstile", "captcha", "forbidden", "403",
    "access denied", "blocked", "challenge", "kasada", "datadome",
]


def is_cloakbrowser_available() -> bool:
    try:
        import importlib.util
        return importlib.util.find_spec("cloakbrowser") is not None
    except Exception:
        return False


def _fetch_tier1(url: str, **kwargs) -> Any:
    from scrapling.fetchers import Fetcher
    impersonate = kwargs.pop("impersonate", "chrome")
    return Fetcher.get(url, impersonate=impersonate, **kwargs)


def _fetch_tier2(url: str, **kwargs) -> Any:
    from scrapling.fetchers import DynamicFetcher
    kwargs.setdefault("headless", True)
    kwargs.setdefault("network_idle", True)
    return DynamicFetcher.fetch(url, **kwargs)


def _fetch_tier3(url: str, solve_cloudflare: bool = True, **kwargs) -> Any:
    from scrapling.fetchers import StealthyFetcher
    kwargs.setdefault("headless", True)
    return StealthyFetcher.fetch(url, solve_cloudflare=solve_cloudflare, **kwargs)


def _fetch_tier4(url: str, css: str | None = None, xpath: str | None = None,
                 proxy: str | None = None, humanize: bool = False,
                 headless: bool = True, timeout: int | None = None) -> dict:
    try:
        from cloakbrowser import launch
    except ImportError:
        raise ImportError("cloakbrowser is not installed. Run: pip install cloakbrowser")

    launch_kwargs: dict = {"headless": headless, "humanize": humanize}
    if proxy:
        launch_kwargs["proxy"] = proxy

    browser = launch(**launch_kwargs)
    try:
        page = browser.new_page()
        nav_kwargs = {}
        if timeout:
            nav_kwargs["timeout"] = timeout * 1000
        page.goto(url, **nav_kwargs)
        page.wait_for_load_state("networkidle", timeout=15000)

        html = page.content()
        text = page.inner_text("body") if page.query_selector("body") else ""
        elements = []

        if css:
            for h in page.query_selector_all(css):
                elements.append({
                    "text": (h.inner_text() or "").strip(),
                    "html": h.inner_html(),
                })
        elif xpath:
            for h in page.query_selector_all(f"xpath={xpath}"):
                elements.append({
                    "text": (h.inner_text() or "").strip(),
                    "html": h.inner_html(),
                })

        return {"html": html, "text": text, "elements": elements, "tier": 4}
    finally:
        browser.close()


def scrape(
    url: str,
    *,
    css: str | None = None,
    xpath: str | None = None,
    tier: str = "auto",
    proxy: str | None = None,
    humanize: bool = False,
    headless: bool = True,
    timeout: int | None = None,
    solve_cloudflare: bool = True,
) -> dict:
    """Scrape a URL with automatic tier escalation.

    Args:
        url: Target URL to scrape.
        css: CSS selector to extract elements.
        xpath: XPath selector to extract elements.
        tier: Stealth tier — "auto" (default), "fast", "dynamic", "stealth", "ultra".
              "auto" starts at tier 1 and escalates on failure.
        proxy: Proxy URL (e.g. "http://user:pass@host:port" or "socks5://...").
        humanize: Human-like mouse/keyboard behavior (tier 4 only).
        headless: Run browser headless (tiers 2-4).
        timeout: Request timeout in seconds.
        solve_cloudflare: Attempt to solve Cloudflare challenges (tier 3).

    Returns:
        dict with keys: html, text, elements (list), tier (int), url.

    Examples:
        # Auto-escalation (recommended for agents)
        result = scrape("https://example.com", css=".product")

        # Force ultra-stealth
        result = scrape("https://protected.com", tier="ultra", humanize=True)

        # With proxy
        result = scrape("https://example.com", proxy="http://user:pass@host:8080")
    """
    tier_map = {"fast": 1, "dynamic": 2, "stealth": 3, "ultra": 4}

    # Explicit tier
    if tier != "auto":
        t = tier_map.get(tier, 1)
        return _run_tier(t, url, css=css, xpath=xpath, proxy=proxy,
                         humanize=humanize, headless=headless, timeout=timeout,
                         solve_cloudflare=solve_cloudflare)

    # Auto-escalation: try tiers 1 → 2 → 3 → 4
    last_error = None
    for t in [1, 2, 3]:
        try:
            result = _run_tier(t, url, css=css, xpath=xpath, headless=headless,
                               timeout=timeout, solve_cloudflare=solve_cloudflare)
            return result
        except Exception as e:
            last_error = e
            err_lower = str(e).lower()
            is_blocked = any(s in err_lower for s in BLOCKED_SIGNALS)
            if not is_blocked and t == 1:
                # Non-block error on tier 1 (network issue etc.) — still escalate
                pass
            import sys as _sys
            print(f"[ultra-scraper] Tier {t} failed: {e} — escalating...", file=_sys.stderr)

    # Tier 4
    if is_cloakbrowser_available():
        print("[ultra-scraper] Trying tier 4 (CloakBrowser)...", file=sys.stderr)
        return _fetch_tier4(url, css=css, xpath=xpath, proxy=proxy,
                            humanize=humanize, headless=headless, timeout=timeout)
    else:
        print(CLOAKBROWSER_INSTALL_MSG, file=sys.stderr)
        raise RuntimeError(
            f"All tiers failed. Last error: {last_error}. "
            "Install CloakBrowser for tier-4 ultra-stealth: pip install cloakbrowser"
        )


async def scrape_async(url: str, **kwargs) -> dict:
    """Async version of scrape(). Same arguments."""
    import asyncio
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, lambda: scrape(url, **kwargs))


def _run_tier(tier: int, url: str, **kwargs) -> dict:
    css = kwargs.pop("css", None)
    xpath = kwargs.pop("xpath", None)

    if tier == 1:
        page = _fetch_tier1(url, **{k: v for k, v in kwargs.items()
                                     if k in ("impersonate", "timeout")})
        return _page_to_dict(page, css, xpath, tier=1, url=url)
    elif tier == 2:
        kw = {k: v for k, v in kwargs.items() if k in ("headless", "timeout", "network_idle")}
        page = _fetch_tier2(url, **kw)
        return _page_to_dict(page, css, xpath, tier=2, url=url)
    elif tier == 3:
        kw = {k: v for k, v in kwargs.items() if k in ("headless", "timeout", "solve_cloudflare")}
        page = _fetch_tier3(url, **kw)
        return _page_to_dict(page, css, xpath, tier=3, url=url)
    elif tier == 4:
        return _fetch_tier4(url, css=css, xpath=xpath,
                            proxy=kwargs.get("proxy"),
                            humanize=kwargs.get("humanize", False),
                            headless=kwargs.get("headless", True),
                            timeout=kwargs.get("timeout"))
    raise ValueError(f"Unknown tier: {tier}")


def _page_to_dict(page: Any, css: str | None, xpath: str | None,
                  tier: int, url: str) -> dict:
    elements = []
    if css:
        for el in page.css(css):
            elements.append({
                "text": (el.text or "").strip() if hasattr(el, "text") else str(el),
                "html": el.html if hasattr(el, "html") else str(el),
                "attributes": dict(el.attrib) if hasattr(el, "attrib") else {},
            })
    elif xpath:
        for el in page.xpath(xpath):
            elements.append({
                "text": (el.text or "").strip() if hasattr(el, "text") else str(el),
                "html": el.html if hasattr(el, "html") else str(el),
                "attributes": dict(el.attrib) if hasattr(el, "attrib") else {},
            })

    body_html = ""
    body_text = ""
    if hasattr(page, "body"):
        body_html = page.body.html if hasattr(page.body, "html") else ""
        body_text = page.body.text if hasattr(page.body, "text") else ""
    elif hasattr(page, "get_all_text"):
        body_text = page.get_all_text()

    return {
        "url": url,
        "tier": tier,
        "html": body_html,
        "text": body_text,
        "elements": elements,
    }
