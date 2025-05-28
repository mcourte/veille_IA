
from transformers import pipeline
from newspaper import Article

# utilisation du modèle distilbartbart-cnn-12-6 ( version distillée, entraînée sur le DataSet CNN/Dailymail)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


# Permet de résumé l'article
def summarize_text(article_url):
    article = Article(article_url)
    article.download()
    article.parse()
    text = article.text
    if not text:
        raise ValueError("Article vide")
    result = summarizer(text[:1024], max_length=150, min_length=30, do_sample=False)
    return result[0]['summary_text']
