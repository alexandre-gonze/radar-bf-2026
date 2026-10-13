"""
Radar BF - Gerador de Produtos & Máquina de Conteúdo Multi-Canal ($0)
Executado via Antigravity / Python 3

Adiciona produto ao catálogo e gera:
1. Roteiro pronto para TikTok / YouTube Shorts (30-45 segundos)
2. Copy e tags prontas para Pinterest
3. Mensagem formatada para canal de ofertas do WhatsApp / Telegram
"""

import os
import sys
import json
import argparse

# Garante suporte a emojis no console do Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PRODUCTS_JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "data", "products.json")

def load_products():
    if os.path.exists(PRODUCTS_JSON_PATH):
        with open(PRODUCTS_JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_products(products):
    with open(PRODUCTS_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(products, f, indent=2, ensure_ascii=False)

def generate_social_bundle(product):
    """Gera o kit completo de conteúdo para redes sociais e mensageiros"""
    name = product["name"]
    price = product["estimatedPrice"]
    category = product["categoryLabel"]
    perfect_for = ", ".join(product["useCases"]["perfectFor"][:2])
    not_for = product["useCases"]["notRecommendedFor"][0] if product["useCases"]["notRecommendedFor"] else "Quem busca topo de linha"
    
    # 1. Roteiro para TikTok / YouTube Shorts / Reels
    video_script = f"""
================================================================================
🎬 ROTEIRO DE VÍDEO VERTICAL (TikTok / YouTube Shorts / Reels) - [35-45s]
================================================================================
🎯 PRODUTO: {name}
💰 PREÇO MÉDIO: {price}

⏱️ [00s - 04s] GANCHO (Prender a atenção imediatamente):
(Mostre a imagem ou o produto na tela)
"NÃO compre nada de {category} na Black Friday antes de ver isso aqui!"

⏱️ [04s - 15s] O PROBLEMA / DOR DO CONSUMIDOR:
"Muita gente gasta mais de 3 mil reais achando que precisa de uma máquina cara, ou compra o mais barato e passa raiva porque trava até para abrir o navegador..."

⏱️ [15s - 30s] A CLASSIFICAÇÃO SEM ENROLAÇÃO:
"Esse modelo aqui é PERFEITO para: {perfect_for}.
MAS ATENÇÃO: Ele NÃO serve se você precisa de: {not_for}!"

⏱️ [30s - 40s] CHAMADA PARA AÇÃO (CTA DE ALTA CONVERSÃO):
"Eu separei a lista verificada das melhores lojas oficiais com menor preço e garantia.
👉 O link com o comparador tá fixado no perfil do canal/bio! Corre antes que o estoque acabe."
================================================================================
"""

    # 2. Copy para Pinterest (SEO visual)
    pinterest_copy = f"""
================================================================================
📌 COPY OTIMIZADA PARA PINTEREST (Busca Visual Passiva)
================================================================================
📍 Título do Pin:
{name} Vale a Pena em 2026? Guia Sem Enrolação

📝 Descrição do Pin:
Está em dúvida se o {name} vale a pena na Black Friday? Veja o guia direto ao ponto: para quem realmente serve ({perfect_for}) e quando NÃO vale a pena comprar ({not_for}). Acesse o comparador completo e veja onde encontrar pelo menor preço seguro com entrega rápida.

🏷️ Hashtags / Tags de Busca:
#blackfriday #achadinhos #{product['category'].replace('-', '')} #comprasinteligentes #ofertasbrasil #tecnologia
================================================================================
"""

    # 3. Mensagem para WhatsApp / Telegram (Canal de Ofertas)
    wa_message = f"""
================================================================================
📲 MENSAGEM PARA CANAL VIP (WhatsApp / Telegram)
================================================================================
🚨 ACHADO BLACK FRIDAY VERIFICADO! 🚨

🔥 *{name}*
🏷️ Categoria: {category}
💰 Por apenas: *{price}*

🟢 *Para quem é perfeito:*
{chr(10).join(['• ' + item for item in product['useCases']['perfectFor']])}

🔴 *NÃO compre se você precisa de:*
• {not_for}

🛒 *ONDE GARANTIR PELO MENOR PREÇO COM SEGURANÇA:*
📦 Amazon: {product['affiliateLinks'].get('amazon', 'Link')}
⚡ Mercado Livre: {product['affiliateLinks'].get('mercadoLivre', 'Link')}
🛍️ Shopee: {product['affiliateLinks'].get('shopee', 'Link')}

⚠️ _Preço e estoque podem esgotar a qualquer momento!_
================================================================================
"""

    return video_script + "\n" + pinterest_copy + "\n" + wa_message

def main():
    parser = argparse.ArgumentParser(description="Radar BF - Gerador de Fichas e Conteúdo")
    parser.add_argument("--list", action="store_true", help="Lista produtos já cadastrados")
    parser.add_argument("--bundle", type=str, help="Gera o kit de redes sociais para um ID de produto")
    args = parser.parse_args()

    products = load_products()

    if args.list:
        print(f"📦 Total de produtos cadastrados: {len(products)}")
        for idx, p in enumerate(products, 1):
            print(f"{idx}. [{p['category']}] {p['name']} - {p['estimatedPrice']} (ID: {p['id']})")
        return

    if args.bundle:
        match = next((p for p in products if p["id"] == args.bundle), None)
        if match:
            print(generate_social_bundle(match))
        else:
            print(f"❌ Produto com ID '{args.bundle}' não encontrado.")
        return

    # Se nenhum argumento, demonstra o bundle do primeiro produto
    if products:
        print(f"💡 Dica: Use '--bundle <id>' para gerar os roteiros. Exibindo exemplo para: {products[0]['id']}")
        print(generate_social_bundle(products[0]))

if __name__ == "__main__":
    main()
