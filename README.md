# Projet Python : "Le Scraper d'Actualites Tech" 🚀

Objectif : manipulation des donnees externes, utilisation de bibliotheques et automatisation de taches repetitives.

Concept : un script qui recupere les titres des derniers articles sur un site (Le Monde Informatique et/ou Hacker News) et les enregistre dans un fichier CSV ou JSON.

## 🛠 Technologies utilisees
- **Front-end :** JavaScript (ES6+), HTML5, CSS3
- **Back-end :** Python avec la librairie BeautifulSoup pour le scraping web
- **Base de donnees :** CSV ou JSON
- **Gestion de version :** Git & GitHub

## 💡 Ce que j'ai appris
- Installation de packages (pip)
- Utilisation de BeautifulSoup ou Requests, manipulation de fichiers
- Manipulation du DOM en JavaScript pur

## 📝 Fonctionnalites cles du projet
- **Extraction de donnees (Web Scraping) :** recuperation automatisee des titres et liens depuis Hacker News en utilisant BeautifulSoup4. Analyse selective du DOM pour isoler les informations pertinentes.
- **Persistance des donnees (Format JSON) :** transformation des donnees HTML non structurees en un fichier JSON structure. Gestion de l'encodage (UTF-8) et de l'indentation pour assurer l'interoperabilite avec d'autres langages (comme JavaScript).
- **Architecture modulaire :** decoupage du code en fonctions distinctes (Fetch / Parse / Save) pour faciliter la maintenance et l'evolution du script.
- **Robustesse des requetes :** integration de headers HTTP (User-Agent) pour simuler un navigateur reel et eviter les blocages serveurs, avec gestion des erreurs sur les codes de statut HTTP (200, 404, 500).
- **Gestion de projet (methodologie) :** utilisation de Git pour le versioning avec des messages de commit explicites. Organisation rigoureuse des dossiers (/data, /venv) pour un projet pret pour la production.

## 🚀 Installation et utilisation
1. Cloner le depot : `git clone https://github.com/oggixtag/python-scraper`
2. Configurer la base de donnees (voir dossier `/sql` ou `.env`)
3. Lancer le serveur local

## 📁 Structure du projet
```
python-scraper/
├── data/               # Dossier pour stocker les resultats (CSV, JSON)
├── venv/               # Environnement virtuel (a ignorer dans Git)
├── .gitignore          # Fichier pour ne pas envoyer les fichiers inutiles
├── requirements.txt    # Liste des bibliotheques a installer
├── scraper.py          # Code principal
└── README.md           # Documentation du projet
```

## 🧪 Etapes d'installation
### 1) Environnement virtuel (venv)
En Python, on n'installe jamais les bibliotheques "en vrac" sur son ordinateur. On cree un environnement isole pour chaque projet.

Entrez dans votre projet :
```
cd mon_projet_web
```

Creez l'environnement :
```
python -m venv venv
```

Activez-le :
```
# Windows : `venv\Scripts\activate` ou `.\venv\Scripts\activate`
# macOS/Linux : `source venv/bin/activate`
```


### 2) Installer les bibliotheques
Options possibles :
- `pip install requests beautifulsoup4`
- `pip install requests==2.31.0 beautifulsoup4==4.12.2`
- `pip install -r requirements.txt` (si vous avez deja un fichier de dependances)

Generer le fichier de dependances :
```
pip freeze > requirements.txt
```

La commande `pip freeze` liste toutes les bibliotheques installees dans votre environnement virtuel avec leur numero de version precis.

## ⚙️ Fonctionnement du script et exécution

Le projet suit un processus rigoureux en trois étapes pour garantir la fiabilité et la qualité des données collectées.

- **📡 Étape 1 : Récupération (Fetching)** Le script initie une requête HTTP GET vers l'URL cible via `requests`. Similitude navigateur : intégration d'un User-Agent personnalisé pour simuler une navigation humaine et prévenir les blocages serveurs. Sécurité : validation systématique du `status_code` (200 OK) avant de poursuivre le traitement, avec une gestion d'exception pour les erreurs réseau (Timeout, DNS).
- **🔍 Étape 2 : Extraction (Parsing)** Une fois le code source HTML récupéré, il est analysé par BeautifulSoup4. Analyse du DOM : utilisation de sélecteurs CSS précis (.titleline > a) pour isoler les informations pertinentes. Mappage de données : transformation des balises HTML en une liste de dictionnaires Python, structurant ainsi la donnée (titre, URL, source).
- **💾 Étape 3 : Sauvegarde (Persistance)** La phase finale assure que la donnée collectée est exploitable par d'autres systèmes (Web ou Mobile). Gestion d'arborescence : vérification et création automatique du répertoire /data via le module `os` pour garantir la portabilité du script. Standardisation JSON : export des données au format JSON avec encodage UTF-8 et indentation, facilitant une future intégration avec un front-end (React/Vue.js) ou une API Node.js.

### 1) Lancer le script
Entrez dans votre projet :
```
cd mon_projet_web
```

Activez l'environnement virtuel :
cf Environnement virtuel (venv)

Exécution du script :
```
python scraper.py
```