"""
Radar BF - Gerador da Tabela de Mineração para o Mercado Livre
Gera 'tabela_links_mercadolivre.md' com links diretos de busca para o usuário copiar os meli.la
"""

import os
import sys
import json
import urllib.parse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PRODUCTS_JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "data", "products.json")
OUTPUT_MD = os.path.join(os.path.dirname(__file__), "..", "tabela_links_mercadolivre.md")

def main():
    with open(PRODUCTS_JSON_PATH, "r", encoding="utf-8") as f:
        products = json.load(f)

    lines = []
    lines.append("# 📋 Lista de Garimpo Mercado Livre (35 Produtos Campeões BF)\n")
    lines.append("> **Como funciona:** Abra cada link de busca abaixo logado na sua conta de afiliado do Mercado Livre, clique em **'Compartilhar' / 'Copiar link'** para gerar o seu link curto `https://meli.la/...` e cole ao lado do produto.\n")
    lines.append("| # | Categoria | Produto | Abrir no Mercado Livre | Seu Link Afiliado (`meli.la`) |")
    lines.append("|---|---|---|---|---|")

    current_cat = ""
    for idx, p in enumerate(products, 1):
        cat = p["categoryLabel"]
        name = p["name"]
        ml_search_url = p["affiliateLinks"].get("mercadoLivre", "")
        current_ml = p["affiliateLinks"].get("mercadoLivre", "")
        has_meli = "meli.la" in current_ml
        meli_display = f"`{current_ml}`" if has_meli else "*(Aguardando link)*"

        lines.append(f"| {idx:02d} | **{cat}** | {name} | [🔍 Abrir Produto no ML]({ml_search_url}) | {meli_display} |")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ Tabela com os {len(products)} produtos gerada com sucesso em 'tabela_links_mercadolivre.md'!")

if __name__ == "__main__":
    main()
