import requests
import os
import json

def find_tarsus_maps():
    # Wikimedia ve Arşiv sitelerinde Tarsus haritaları araması
    url = "https://commons.wikimedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": "Tarsus ancient map engraving",
        "srlimit": 10
    }
    
    print("Dünya arşivlerinde antik Tarsus haritaları aranıyor...")
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        map_results = []
        
        for item in data['query']['search']:
            map_results.append({
                "baslik": item['title'],
                "link": f"https://commons.wikimedia.org/wiki/{item['title'].replace(' ', '_')}"
            })
            
        os.makedirs('data/tarsus_exclusive', exist_ok=True)
        with open('data/tarsus_exclusive/antik_haritalar.json', 'w', encoding='utf-8') as f:
            json.dump(map_results, f, ensure_ascii=False, indent=4)
        
        print(f"İşlem tamam! {len(map_results)} adet harita ve gravür linki kasana eklendi.")

if __name__ == "__main__":
    find_tarsus_maps()

