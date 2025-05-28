import streamlit as st
from veille_ia.scraper import get_news_from_google, get_news_from_tech_sites
from veille_ia.summarizer import summarize_text
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
        st.info("🔎 Recherche des articles en cours...")

        articles_google = get_news_from_google(topic) if "Google News" in sources else []
        articles_tech = get_news_from_tech_sites(keyword=topic) if "Sites techniques" in sources else []

        all_articles = articles_google + articles_tech

        if not all_articles:
            st.warning("Aucune source sélectionnée ou aucun article trouvé.")
            return

        # Affichage des articles et génération des résumés
        summaries = []
        if articles_google:
            st.subheader("📰 Articles Google News")
            for title, link in articles_google:
                st.markdown(f"- [{title}]({link})")

        if articles_tech:
            st.subheader("💻 Articles Sites Techniques")
            for title, link in articles_tech:
                try:
                    summary = summarize_text(link)
                except Exception as e:
                    summary = f"*Résumé indisponible : {e}*"
                summaries.append((title, summary))
                st.markdown(f"**{title}**\n\n{summary}\n\n[Lire l'article]({link})")

        # Génération HTML pour l'email
        html_content = generate_email_html(articles_google, articles_tech, topic)
        subject = f"Rapport de veille sur : {topic}"

        if email:
            send_email_report(email, subject, html_content)
            st.success(f"📬 Rapport envoyé à {email}")
        else:
            st.warning("✉️ Veuillez saisir une adresse e-mail pour recevoir le rapport.")


if __name__ == "__main__":
    run_streamlit_app()
