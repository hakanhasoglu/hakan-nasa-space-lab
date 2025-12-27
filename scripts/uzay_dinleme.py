import requests
import xml.etree.ElementTree as ET

def dsn_canli_dinle():
    print("📡 NASA Derin Uzay Ağına Alternatif Kanaldan Bağlanılıyor...\n")
    # Alternatif veri yolu
    url = "https://dsn.nasa.gov/dsn/data/dsn.xml"
    headers = {'User-Agent': 'Mozilla/5.0'} # Kendimizi tarayıcı gibi tanıtıyoruz
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        root = ET.fromstring(response.content)
        
        print(f"{'İSTASYON':<12} | {'HEDEF UZAY ARACI':<20} | {'SİNYAL'}")
        print("-" * 55)
        
        for dish in root.findall(".//dish"):
            name = dish.get("name")
            targets = dish.findall(".//target")
            
            for t in targets:
                target_name = t.get("name")
                if target_name and target_name.lower() != "none":
                    # Sinyal türünü alalım (yukarı veya aşağı link)
                    up = t.get("upMhz")
                    down = t.get("downMhz")
                    sinyal = "VERİ ALINIYOR" if down else "BAĞLANTI BEKLENİYOR"
                    
                    print(f"{name:<12} | {target_name:<20} | {sinyal}")
                    
    except Exception as e:
        print(f"Bağlantı sorunu devam ediyor: {e}")
        print("\nİpucu: NASA sunucuları bazen yoğunluktan cevap vermez. Birkaç dakika sonra tekrar dene.")

if __name__ == "__main__":
    dsn_canli_dinle()
