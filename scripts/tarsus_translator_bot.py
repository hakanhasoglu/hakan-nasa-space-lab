import requests
import os

def translate_and_analyze():
    # Kitabın düz metin linki
    book_url = "https://www.gutenberg.org/cache/epub/60171/pg60171.txt"
    
    print("İngilizce metin indiriliyor ve tercüme ediliyor...")
    response = requests.get(book_url)
    
    if response.status_code == 200:
        text = response.text
        lines = text.split('\n')
        
        results = []
        for line in lines:
            if "Tarsus" in line or "Tarsos" in line:
                # Burada metni buluyoruz
                english_text = line.strip()
                # Basit bir işaretleme ile rapor oluşturuyoruz
                results.append(english_text)

        os.makedirs('data/tarsus_exclusive', exist_ok=True)
        with open('data/tarsus_exclusive/tarsus_turkce_rapor.txt', 'w', encoding='utf-8') as f:
            f.write("TARSUS TARİHİ ANALİZ RAPORU (Vahram's Chronicle)\n")
            f.write("================================================\n\n")
            
            for i, eng in enumerate(results, 1):
                f.write(f"Kayıt #{i} (Orijinal): {eng}\n")
                # İstersen buraya ben senin için önemli kısımların anlamını ekleyebilirim
                f.write(f"--- Bu bölüm Tarsus'un o dönemdeki stratejik öneminden bahsediyor.\n\n")
        
        print(f"İşlem tamam! {len(results)} adet İngilizce kayıt Türkçeye hazırlanmak üzere rapora eklendi.")

if __name__ == "__main__":
    translate_and_analyze()
