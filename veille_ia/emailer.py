import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
# Récupérer la clé API SendGrid depuis la variable d'environnement
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

# Adresse email de l'expéditeur ( celle choisie sur SendGrid)
EMAIL_SENDER = "mcourte@outlook.fr"


# Création et envoie de l'email
def send_email_report(receiver_email, subject, html_content):
    message = Mail(
        from_email=EMAIL_SENDER,
        # receiver_email = email choisi par l'utilisateur
        to_emails=receiver_email,
        subject=subject,
        html_content=html_content,
        # Texte envoyé dans chaque début de mail
        plain_text_content=(
            "Bonjour,\n\n"
            "Veuillez trouver ci-joint le rapport de veille généré automatiquement."
        )
    )
    try:
        # Utilisation de l'API SendGrid pour permettre l'envoie de mail
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        # Vérification dans le terminal que l'envoie s'est bien déroulé
        print(f"Email envoyé avec statut : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")
