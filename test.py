# test_scraper.py
from scraper import get_news_from_google, get_news_from_tech_sites

print("=== Google News ===")
for title, link in get_news_from_google("intelligence artificielle"):
    print(f"- {title} -> {link}")

print("\n=== Sites Tech ===")
for title, link in get_news_from_tech_sites("intelligence artificielle"):
    print(f"- {title} -> {link}")
