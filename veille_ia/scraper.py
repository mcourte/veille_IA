import feedparser
from GoogleNews import GoogleNews


# Utilisation de la bibliothèque GoogleNews pour parcourir les données du site.
def get_news_from_google(topic):
    """
    Récupère des articles depuis Google News en français, selon un sujet donné.
    """
    gn = GoogleNews(lang='fr')
    gn.search(topic)
    results = gn.results(sort=True)
    return [(res['title'], res['link']) for res in results[:10]]


# Choix des sources dans laquelle aller chercher des articles
RSS_FEEDS = [
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "http://feeds.arstechnica.com/arstechnica/index",
    "https://hnrss.org/frontpage",
]

# La lanque de Google News est le français. Pour pouvoir trouver des articles
# sur des sites techniques, j'ai crée un petit dictionnaire de traduction
# pour quelques mots-clés


# Traduction et synonymes
KEYWORD_SYNONYMS = {
    "intelligence artificielle": ["AI", "artificial intelligence", "machine learning", "deep learning"],
    "apprentissage automatique": ["machine learning", "AI"],
    "apprentissage profond": ["deep learning", "neural networks"],
    "réseau de neurones": ["neural networks", "deep learning"],
    "données": ["data", "big data", "data science"],
}


def get_news_from_tech_sites(keyword=None):
    """
    Récupère les articles récents des sites techniques.
    Si un mot-clé est fourni, filtre les articles contenant ce mot-clé ou ses synonymes.
    """
    if keyword:
        keyword_lower = keyword.lower()
        # Inclure la clé elle-même + ses synonymes
        keywords = [keyword_lower] + KEYWORD_SYNONYMS.get(keyword_lower, [])
        # Mettre tout en minuscules aussi
        keywords = [k.lower() for k in keywords]
    else:
        keywords = []

    articles = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            title = entry.get("title", "")
            link = entry.get("link", "")

            if keywords:
                matched = any(k in title.lower() for k in keywords)
            else:
                matched = True

            if matched:
                articles.append((title, link))

    # Dans le cas où il ne trouve aucun article correspondant au mot-clé
    # Il affiche les derniers articles publiés sur les sites techniques.
    if not articles and keyword:
        return get_news_from_tech_sites(keyword=None)

    return articles
