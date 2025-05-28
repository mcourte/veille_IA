from veille_ia.scraper import get_news_from_google, get_news_from_tech_sites
from veille_ia.summarizer import summarize_text
from veille_ia.emailer import send_email_report
from settings import default_topic, default_source, attachment_filename


# A utiliser dans le futur, pour envoie par mail quotidien
def run_daily_report():
    topic = default_topic
    source = default_source

    if source == "Google News":
        articles = get_news_from_google(topic)
    else:
        articles = get_news_from_tech_sites(keyword=topic)

    summaries = []
    for title, link in articles:
        try:
            summary = summarize_text(link)
        except Exception as e:
            summary = f"(Erreur de résumé : {e})"
        summaries.append((title, summary))

    # Demander l'adresse email à l'utilisateur
    receiver_email = input("Entrez votre adresse e-mail pour recevoir le rapport : ").strip()

    if receiver_email:
        print(f"Envoi du rapport à {receiver_email} ...")
        send_email_report(receiver_email, filename=attachment_filename)
    else:
        print("Aucune adresse e-mail saisie. Rapport non envoyé.")


if __name__ == "__main__":
    run_daily_report()
