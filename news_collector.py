import feedparser
from GoogleNews import GoogleNews


def get_news_from_google(topic):
    gn = GoogleNews(lang='fr')
    gn.search(topic)
    results = gn.results(sort=True)
    return [(res['title'], res['link']) for res in results[:5]]


def get_news_from_tech_sites(keyword=None):
    RSS_FEEDS = [
        "https://techcrunch.com/feed/",
        "https://www.theverge.com/rss/index.xml",
        "http://feeds.arstechnica.com/arstechnica/index",
        "https://hnrss.org/frontpage"
    ]

    articles = []
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:
            if keyword is None or keyword.lower() in entry.title.lower():
                articles.append((entry.title, entry.link))
    return articles[:10]
