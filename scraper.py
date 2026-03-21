import requests
from bs4 import BeatifulSoup
import json
import os

# Configuration : Simulation d'une navigation humaine (User-Agent)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


# --- Point d'entrée du script ---
if __name__ == "__main__":
    target_url = "https://news.ycombinator.com/"
    
    print(f"🚀 Lancement du pipeline rigoureux sur : {target_url}")
    
    # 📡 Étape 1 : Récupération
    html = fetch_data(target_url)
    
    if html:
        # 🔍 Étape 2 : Extraction
        extracted_data = parse_html(html)
        
        if extracted_data:
            # 💾 Étape 3 : Sauvegarde
            if save_to_json(extracted_data):
                print(f"✅ Succès ! {len(extracted_data)} objets stockés dans 'data/results.json'")
                print("💡 Prêt pour une intégration Front-end ou API.")
        else:
            print("⚠️ Analyse du DOM terminée : aucune donnée pertinente trouvée.")
    else:
        print("🛑 Arrêt du processus : impossible de récupérer le contenu source.")