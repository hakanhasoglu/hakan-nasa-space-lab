import requests
import json
import os

# Mars Rover Photos API (Perseverance)
MARS_API = "https://api.nasa.gov/mars-photos/api/v1/rovers/perseverance/latest_photos?api_key=DEMO_KEY"

def fetch_mars_data():
    response = requests.get(MARS_API)
    if response.status_code == 200:
        data = response.json()
        latest_photo = data['latest_photos'][0] # En son çekilen ilk fotoğraf
        
        mars_data = {
            "earth_date": latest_photo['earth_date'],
            "sol": latest_photo['sol'],
            "img_url": latest_photo['img_src'],
            "camera": latest_photo['camera']['full_name'],
            "status": latest_photo['rover']['status']
        }
        
        os.makedirs('data', exist_ok=True)
        with open('data/mars_today.json', 'w') as f:
            json.dump(mars_data, f, indent=4)
        print("Mars verisi başarıyla güncellendi!")

if __name__ == "__main__":
    fetch_mars_data()
