import requests
from bs4 import BeautifulSoup
import json
import os

# Configuration : Simulation d'une navigation humaine (User-Agent)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_data(url):
    """
    Étape 1 : Récupération (Fetching)
    Initie une requête HTTP GET et valide la réponse.
    """
    try:
         # Requête avec User-Agent et timeout de sécurité
         response = requests.get(url, headers=HEADERS, timeout=10)
         # Validation du status_code (200 OK)
         response.raise_for_status()  
         return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur lors de la récupération : {e}")
    return None

def parse_html(html_content):
    """
    Étape 2 : Extraction (Parsing)
    Analyse le DOM et structure les données en objets (dictionnaires).
    """
    try:
        soup : BeautifulSoup = BeautifulSoup(html_content, 'html.parser')
        articles = []

        # Extraction ciblée : titleline : C'est le nom de la classe spécifique utilisée par le site Hacker News pour entourer le titre de chaque article.
        # <span class="titleline"><a href="https://example.com/article1">Titre de l'article 1</a></span>">
        items = soup.select('.titleline') 

        #boucle d'extraction
        for item in items:
            link = item.find('a')
            # Extraction de la source (site web d'origine) si disponible
            source_tag = item.find('span', class_='sitebit comhead')

            if link:
                # Mappage des données en dictionnaire Python
                object_data = {
                    "title": link.get_text(strip=True),
                    "url": link['href'],
                    "source": source_tag.get_text(strip=True) if source_tag else "N/A"
                }
                articles.append(object_data)
        print(f"✅ Extraction réussie : {len(articles)} articles trouvés.")
        # Affichage des données extraites
        print
        return articles

    except soup.exception.SoupException as e:
        print(f"❌ Erreur lors de l'analyse du DOM : {e}")
        return None


# --- Point d'entrée du script ---
if __name__ == "__main__":
    target_url = "https://news.ycombinator.com/"
    
    print(f"🚀 Lancement du pipeline rigoureux sur : {target_url}")
    
    # 📡 Étape 1 : Récupération
    html = fetch_data(target_url)
    
    if html:
        # 🔍 Étape 2 : Extraction
        extracted_data = parse_html(html)
        
        
    else:
        print("🛑 Arrêt du processus : impossible de récupérer le contenu source.")