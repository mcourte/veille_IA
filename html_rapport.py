def generate_email_html(google_news, tech_news, topic):
    """
    Génère un contenu HTML pour le mail avec les news Google et Tech, bien stylé.

    :param google_news: liste de tuples (titre, lien) depuis Google News
    :param tech_news: liste de tuples (titre, lien) depuis sites tech
    :param topic: sujet recherché, pour afficher dans le mail
    :return: chaîne HTML complète
    """
    def make_section(title, news_list):
        if not news_list:
            return ""
        items = "".join(f'<li><a href="{link}" target="_blank">{title}</a></li>' for title, link in news_list)
        return f"""
            <h2>{title}</h2>
            <ul>
                {items}
            </ul>
        """

    google_section = make_section("Google News", google_news)
    tech_section = make_section("Sites Tech", tech_news)

    html_template = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>Newsletter Tech - {topic}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f7f9;
                color: #333;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 20px auto;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #0078D7;
                text-align: center;
            }}
            h2 {{
                border-bottom: 2px solid #0078D7;
                padding-bottom: 6px;
                margin-top: 30px;
                color: #004a9f;
            }}
            ul {{
                list-style-type: none;
                padding-left: 0;
            }}
            li {{
                margin-bottom: 12px;
                line-height: 1.4;
            }}
            a {{
                text-decoration: none;
                color: #1a73e8;
            }}
            a:hover {{
                text-decoration: underline;
            }}
            .footer {{
                font-size: 0.85em;
                color: #999;
                text-align: center;
                margin-top: 40px;
                border-top: 1px solid #ddd;
                padding-top: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Newsletter Tech</h1>
            <p>Voici les dernières actualités sur le sujet : <strong>{topic}</strong></p>
            {google_section}
            {tech_section}
            <div class="footer">
                <p>Vous recevez ce mail car vous êtes abonné à la newsletter Tech.</p>
                <p>&copy; 2025 Tech News</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_template
