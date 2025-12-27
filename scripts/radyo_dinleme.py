import requests
import json

def radyo_trafiği_izle():
    print("🌍 Küresel Radyo Anten Ağına Bağlanılıyor (WSPR Canlı)...\n")
    # Dünya çapındaki antenlerin son raporlarını çeken halka açık API
    url = "https://www.wsprnet.org/WSPRnet/sample_all.json"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        print(f"{'ZAMAN':<10} | {'ANTEN (DİNLEYEN)':<15} | {'SİNYAL SAHİBİ':<15} | {'FREKANS'}")
        print("-" * 65)
        
        # En son yakalanan 10 sinyali göster
        for i in range(10):
            r = data[i]
            zaman = r[0] # Zaman damgası
            dinleyen = r[1] # Sinyali yakalayan anten
            sahibi = r[2] # Sinyali gönderen (Gemi, uçak veya amatör istasyon)
            frekans = r[3] # Frekans (MHz)
            
            print(f"{zaman:<10} | {dinleyen:<15} | {sahibi:<15} | {frekans} MHz")
            
    except Exception as e:
        print(f"Hata: Veri çekilemedi. Bağlantını kontrol et: {e}")

if __name__ == "__main__":
    radyo_trafiği_izle()
