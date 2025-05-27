import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
# Récupérer la clé API SendGrid depuis la variable d'environnement
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

# Adresse email de l'expéditeur (celle validée dans ton compte SendGrid)
EMAIL_SENDER = "mcourte@outlook.fr"  # à remplacer par ton email SendGrid validé


def send_email_report(receiver_email, subject, html_content):
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails=receiver_email,
        subject=subject,
        html_content=html_content,
        plain_text_content=(
            "Bonjour,\n\n"
            "Veuillez trouver ci-joint le rapport de veille généré automatiquement."
        )
    )
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"Email envoyé avec statut : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de l'envoi : {e}")
