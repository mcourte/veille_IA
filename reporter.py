def create_report(summaries, topic):
    with open("rapport.txt", "w", encoding="utf-8") as f:
        f.write(f"Rapport de veille sur : {topic}\n\n")
        for title, summary in summaries:
            f.write(f"Titre : {title}\n")
            f.write(f"Résumé : {summary}\n\n")
