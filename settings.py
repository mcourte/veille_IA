from pathlib import Path

# Sujet et source par défaut
default_topic = "intelligence artificielle"
default_source = "Sites techniques"

# Rapport
report_file = Path("rapport.txt")

# Configuration e-mail par défaut
email_sender = "mcourte@outlook.fr"
email_subject = "Rapport de veille IA"
email_body = "Bonjour,\n\nVeuillez trouver ci-joint le rapport de veille généré automatiquement."
attachment_filename = "rapport.txt"


# Nom de pièce jointe
attachment_filename = "rapport.txt"

# Heure d'envoi automatique (pour tâche planifiée)
send_hour = 8
