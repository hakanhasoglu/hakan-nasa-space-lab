import requests
import os
import json

def search_tarsus_history():
    # Tarsus, Kilikya ve Aziz Paul üzerinden daha geniş bir arama yapıyoruz
    queries = ["Tarsus", "Cilicia", "Paul Tarsus"]
    all_results = []
    
    print("Tarsus ve Kilikya arşivleri derinlemesine taranıyor...")
    
    for query in queries:
        url = f"https://gutendex.com/books/?search={query}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for book in data.get('results', []):
                    # Aynı kitabı tekrar eklememek için kontrol
                    if not any(item['kitap_adi'] == book['title'] for item in all_results):
                        info = {
                            "kitap_adi": book['title'],
                            "yazar": book['authors'][0]['name'] if book['authors'] else "Bilinmiyor",
                            "link": f"https://www.gutenberg.org/ebooks/{book['id']}"
                        }
                        all_results.append(info)
        except Exception as e:
            print(f"{query} aranırken hata oluştu: {e}")

    os.makedirs('data/tarsus_exclusive', exist_ok=True)
    with open('data/tarsus_exclusive/deep_history.json', 'w', encoding='utf-8') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=4)
    
    print(f"Genişletilmiş sondaj tamamlandı! {len(all_results)} adet benzersiz kayıt bulundu.")

if __name__ == "__main__":
    search_tarsus_history()
