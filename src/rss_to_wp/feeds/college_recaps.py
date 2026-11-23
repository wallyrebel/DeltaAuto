"""Read completed-game releases from the Delta's two university athletics desks."""

from html import escape
from urllib.parse import urlsplit
import re

import requests
from bs4 import BeautifulSoup

FEEDS = {
    "https://gostatesmen.com/rss.aspx": "gostatesmen.com",
    "https://mvsusports.com/rss.aspx": "mvsusports.com",
}


def recap_text(feed_url, story_url):
    target = urlsplit(story_url or "")
    if (target.scheme != "https" or target.netloc != FEEDS[feed_url]
            or target.query or not re.fullmatch(r"/news/\d{4}/\d{1,2}/\d{1,2}/[a-zA-Z0-9-]+\.aspx", target.path)):
        return None
    response = requests.get(story_url, timeout=(5, 15), allow_redirects=False,
                            headers={"Accept-Encoding": "gzip, deflate", "User-Agent": "DeltaReport/1.0"})
    response.raise_for_status()
    if response.status_code != 200:
        raise ValueError("Athletics release unavailable")
    page = BeautifulSoup(response.content, "html.parser")
    canonical = page.select_one('link[rel="canonical"]')
    if not canonical or canonical.get("href") != story_url:
        raise ValueError("Athletics release identity changed")
    body = page.select_one('article[aria-label="Game Recap Story"] .sidearm-story-template-text')
    if (body is None and target.netloc == "mvsusports.com"
            and re.fullmatch(r"/news/\d{4}/\d{1,2}/\d{1,2}/general-this-week-in-valley-state-athletics(?:-\d+)?\.aspx", target.path)):
        body = page.select_one('article[aria-label="Main Story"] .sidearm-story-template-text')
    if body is None:
        return None
    for node in body.select("script, style, img, iframe, figure, form"):
        node.decompose()
    text = " ".join(body.stripped_strings)
    return escape(text) if len(text.split()) >= 60 else None
