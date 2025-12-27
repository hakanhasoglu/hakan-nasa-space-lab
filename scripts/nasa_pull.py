import requests
import json
import os

def fetch_nasa_data():
    # NASA'dan günün astronomi bilgisini al
    URL = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    response = requests.get(URL)
    
    if response.status_code == 200:
        data = response.json()
        # Veriyi Oxford usulü 'data' klasörüne kaydet
        with open('data/nasa_today.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Oxford Standartlarında Veri Çekildi ve Kaydedildi!")
    else:
        print("Hata!")

if __name__ == "__main__":
    fetch_nasa_data()
