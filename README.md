# Projet Python : "Le Scraper d'Actualités Tech" 🚀

Objectif : Manipulation des données externes et utiliser des bibliothèques et automatiser des tâches répétitives. 

Le concept : Un script qui récupère les titres des derniers articles sur un site (Le Monde Informatique et/ou Hacker News) et les enregistre dans un fichier CSV ou JSON.

## 🛠 Technologies utilisées
* **Front-end :** JavaScript (ES6+), HTML5, CSS3 
* **Back-end :** Python avec la librerie BeautifulSoup pour le scraping web.
* **Base de données :** CSV ou JSON
* **Gestion de version :** Git & GitHub

## 📝 Fonctionnalités clés
* **Extraction de données (Web Scraping) :** Récupération automatisée des titres et liens depuis Hacker News en utilisant BeautifulSoup4. Analyse sélective du DOM pour isoler les informations pertinentes.
* **Persistance des données (Format JSON) :** Transformation des données HTML non structurées en un fichier JSON structuré. Gestion de l'encodage (UTF-8) et de l'indentation pour assurer l'interopérabilité avec d'autres langages (comme JavaScript).
* **Architecture Modulaire :** Découpage du code en fonctions distinctes (Fetch / Parse / Save) pour faciliter la maintenance et l'évolution du script.
* **Robustesse des requêtes :** Intégration de headers HTTP (User-Agent) pour simuler un navigateur réel et éviter les blocages serveurs, accompagnée d'une gestion d'erreurs sur les codes de statut HTTP (200, 404, 500).
* **Gestion de projet (Méthodologie) :** Utilisation de Git pour le versioning avec des messages de commit explicites. Organisation rigoureuse des dossiers (/data, /venv) pour un projet prêt pour la production.

## 🚀 Installation et Utilisation
1. Cloner le dépôt : `git clone https://github.com/oggixtag/python-scraper`
2. Configurer la base de données (voir dossier `/sql` ou `.env`)
3. Lancer le serveur local.

## 💡 Ce que j'ai appris
* Installation de packages (pip)
* Utilisation de BeautifulSoup ou Requests, manipulation de fichiers.
* Manipulation du DOM en JavaScript pur.


1. La structure
python-scraper/
├── data/               # Dossier pour stocker les résultats (CSV, JSON)
├── venv/               # Environnement virtuel (à ignorer dans Git)
├── .gitignore          # Fichier pour ne pas envoyer les fichiers inutiles
├── requirements.txt    # Liste des bibliothèques à installer
├── scraper.py          # Votre code principal
└── README.md           # Documentation du projet

2. Étape 1 : L'environnement virtuel (venv)
En Python, on n'installe jamais les bibliothèques "en vrac" sur son ordinateur. On crée un environnement isolé pour chaque projet.

Entrez dans votre projet :
cd mon_projet_web

Créez l'environnement :
python -m venv venv

Activez-le :
- Sur Windows : venv\Scripts\activate ou .\venv\Scripts\activate
- Sur macOS/Linux : source venv/bin/activate

3. Étape 2 : Installer les bibliothèques
a)pip install requests beautifulsoup4 ou pip install requests==2.31.0 beautifulsoup4==4.12.2 ou
pip install -r requirements.txt si vous avez déjà un fichier de dépendances.
b)pip freeze > requirements.txt

La commande pip freeze liste toutes les bibliothèques installées dans votre environnement virtuel avec leur numéro de version précis.




