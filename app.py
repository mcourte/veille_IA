import streamlit as st
from veille_ia.scraper import get_news_from_google, get_news_from_tech_sites
from veille_ia.emailer import send_email_report
from veille_ia.html_rapport import generate_email_html
from veille_ia.summarizer import summarize_text

st.set_page_config(page_title="Veille IA", page_icon="🤖")

st.title("🤖 Générateur de Rapport de Veille IA")

# Entrée utilisateur, avec un sujet pré rempli
topic = st.text_input("🧠 Sujet à surveiller :", value="intelligence artificielle")

# Choix multiple de sources
sources = st.multiselect(
    "🌐 Source(s) d'information :",
    ["Google News", "Sites techniques"],
    default=["Google News"]
)

email = st.text_input("📧 Adresse e-mail pour recevoir le rapport :")

# Bouton d'action
if st.button("🚀 Lancer la veille et envoyer le rapport"):
    st.info("🔎 Recherche des articles...")

    # Récupération des actualités
    google_news = get_news_from_google(topic) if "Google News" in sources else []
    tech_news = get_news_from_tech_sites(keyword=topic) if "Sites techniques" in sources else []

    if not google_news and not tech_news:
        st.warning("Aucune source sélectionnée ou pas de résultats.")
    else:
        # Affichage dans l’interface
        if google_news:
            st.subheader("📰 Articles Google News")
            for title, link in google_news:
                st.markdown(f"- [{title}]({link})")
        if tech_news:
            st.subheader("💻 Articles Sites Techniques")
            for title, link in tech_news:
                try:
                    summary = summarize_text(link)
                except Exception as e:
                    summary = f"*Résumé non disponible ({e})*"
                st.markdown(f"**{title}**  \n{summary}  \n[Lire la suite]({link})")

        # Génération HTML
        html_content = generate_email_html(google_news, tech_news, topic)
        subject = f"Rapport de veille IA sur : {topic}"

        # Envoi par email si précisé
        if email:
            send_email_report(email, subject, html_content)
            st.success(f"📬 Rapport envoyé à {email}")
        else:
            st.warning("✉️ Veuillez saisir une adresse e-mail pour recevoir le rapport.")
