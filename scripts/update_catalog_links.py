"""
Atualiza todos os links do catálogo products.json aplicando as tags ativas do .env
"""

import os
import sys
import json

sys.path.append(os.path.dirname(__file__))
from affiliate_linker import monetize_url

def update_all_links():
    path = "src/data/products.json"
    with open(path, "r", encoding="utf-8") as f:
        products = json.load(f)

    for p in products:
        links = p.get("affiliateLinks", {})
        if "amazon" in links and links["amazon"]:
            links["amazon"], is_active = monetize_url(links["amazon"], p.get("id"))
        if "mercadoLivre" in links and links["mercadoLivre"]:
            links["mercadoLivre"], _ = monetize_url(links["mercadoLivre"], p.get("id"))
        if "shopee" in links and links["shopee"]:
            links["shopee"], _ = monetize_url(links["shopee"], p.get("id"))

    with open(path, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

    print(f"✅ Todos os {len(products)} produtos foram atualizados com a tag de afiliado no catálogo!")

if __name__ == "__main__":
    update_all_links()
