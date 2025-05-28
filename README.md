# 🤖 Veille IA – Générateur de Rapport d’Actualités

Une application Streamlit qui vous permet de générer un **rapport personnalisé sur un sujet choisi** (par défaut : l'intelligence artificielle) en sélectionnant les sources d'actualité souhaitées. Le rapport est affiché dans l'interface et peut être envoyé par e-mail au format HTML.

---

## 🚀 Fonctionnalités

- 🔎 Recherche d'articles depuis :
  - Google News
  - Sites techniques spécialisés (TechCrunch, Wired, The Verge, etc.)
- 📬 Génération d’un rapport stylisé en HTML
- 🖥️ Affichage direct des articles dans l’interface Streamlit
- ✉️ Envoi du rapport par e-mail

---


## 🛠️ Installation

### 1. Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/veille-ia.git
cd veille-ia
```
### 2. Créer un environnement virtuel

```
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
```
### 3. Installer les dépendances

```
pip install -r requirements.txt
```

### 4. Lancer l'application
```
streamlit run app.py --logger.level=error
```