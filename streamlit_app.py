import streamlit as st
from veille_ia.scraper import get_news_from_google, get_news_from_tech_sites
from veille_ia.summarizer import summarize_text
from veille_ia.reporter import create_report
from veille_ia.emailer import send_email_report
from veille_ia.html_rapport import generate_email_html


def run_streamlit_app():
    st.set_page_config(page_title="Veille IA", page_icon="🤖")

    st.title("🤖 Générateur de Rapport de Veille IA")

    # Entrée utilisateur
    topic = st.text_input("🧠 Sujet à surveiller :", value="intelligence artificielle")
    sources = st.multiselect(
        "🌐 Source(s) d'information (tu peux choisir plusieurs) :",
        ["Google News", "Sites techniques"],
        default=["Google News"]
    )
    email = st.text_input("📧 Adresse e-mail pour recevoir le rapport :")

    if st.button("🚀 Lancer la veille et envoyer le rapport"):

        st.info("Recherche en cours...")

        articles = []
        if "Google News" in sources:
            articles.extend(get_news_from_google(topic))
        if "Sites techniques" in sources:
            articles.extend(get_news_from_tech_sites(keyword=topic))

        if not articles:
            st.warning("Veuillez sélectionner au moins une source et vérifier le sujet.")
        else:
            # Résumé
            summaries = []
            for title, link in articles:
                try:
                    summary = summarize_text(link)
                except Exception as e:
                    summary = f"(Erreur de résumé : {e})"
                summaries.append((title, summary))

            # Création du rapport
            create_report(summaries, topic)
            st.success("✅ Rapport généré avec succès.")

            # Générer l’HTML pour l’email (à adapter selon ta fonction)
            # Par exemple, si tu as une fonction generate_email_html(google_news, tech_news, topic)
            google_news = [a for a in articles if "Google News" in sources]
            tech_news = [a for a in articles if "Sites techniques" in sources]
            html_content = generate_email_html(
                google_news if "Google News" in sources else [],
                tech_news if "Sites techniques" in sources else [],
                topic
            )
            subject = f"Rapport de veille sur : {topic}"

            if email:
                send_email_report(email, subject, html_content)
                st.success(f"📬 Rapport envoyé à {email}")
            else:
                st.warning("Veuillez saisir une adresse e-mail pour l'envoi.")


if __name__ == "__main__":
    run_streamlit_app()
