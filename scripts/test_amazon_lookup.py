"""
Teste de busca de ASIN direto e imagem oficial na Amazon Brasil
"""
import urllib.request
import urllib.parse
import re

def search_amazon_product(term):
    url = f"https://www.amazon.com.br/s?k={urllib.parse.quote(term)}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
            # Procura por cards de produto com data-asin
            asins = re.findall(r'data-asin="([A-Z0-9]{10})"', html)
            # Remove ASINs vazios
            valid_asins = [a for a in asins if a and not a.startswith("0")]
            
            # Procura imagens de produto da CDN da Amazon
            images = re.findall(r'https://m\.media-amazon\.com/images/I/([a-zA-Z0-9\-_%]+?)\.jpg', html)
            
            return {
                "asin": valid_asins[0] if valid_asins else None,
                "image": f"https://m.media-amazon.com/images/I/{images[0]}.jpg" if images else None
            }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    term = "Lenovo IdeaPad 1 Ryzen 5"
    res = search_amazon_product(term)
    print("Resultado para:", term)
    print(res)
