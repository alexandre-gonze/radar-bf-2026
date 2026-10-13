"""
Radar BF - Minerador de Tendências & Produtos Mais Buscados ($0)
Executado localmente via Antigravity / Python 3
"""

import sys
import json
import urllib.request
import urllib.parse
from datetime import datetime

# Garante suporte a emojis no console do Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Categorias mapeadas para alta conversão na Black Friday Brasil
NICHE_CATEGORIES = {
    "estudantes": {
        "title": "Estudantes & Faculdade",
        "search_terms": [
            "notebook barato para estudo",
            "tablet para estudar com caneta",
            "mochila impermeavel notebook",
            "kindle 11 geracao",
            "fone com cancelamento de ruido"
        ],
        "ticket_medio": "R$ 1.500 - R$ 2.800"
    },
    "ti-trabalho": {
        "title": "TI & Produtividade / Home Office",
        "search_terms": [
            "notebook rtx 3050 ryzen",
            "cadeira ergonomica nr17",
            "monitor ultrawide 29 lg",
            "teclado mecanico sem fio",
            "hub usb-c 7 em 1"
        ],
        "ticket_medio": "R$ 3.000 - R$ 5.500"
    },
    "gamers": {
        "title": "Setup Gamer & Consoles",
        "search_terms": [
            "playstation 5 slim",
            "nintendo switch oled",
            "headset hyperx cloud",
            "mouse logitech g pro",
            "monitor gamer 144hz 1ms"
        ],
        "ticket_medio": "R$ 150 - R$ 3.800"
    },
    "casa-cozinha": {
        "title": "Casa & Cozinha Inteligente",
        "search_terms": [
            "airfryer 4 litros mondial",
            "robo aspirador com mapeamento",
            "panela de pressao eletrica inox",
            "liquidificador potente 1200w",
            "filtro purificador de agua consul"
        ],
        "ticket_medio": "R$ 200 - R$ 1.200"
    },
    "maes-bebes": {
        "title": "Mães, Pais & Primeira Infância",
        "search_terms": [
            "baba eletronica com camera visao noturna",
            "carrinho de bebe compacto aviao",
            "cadeirinha auto isofix 0 a 36kg",
            "esterilizador mamadeira microondas",
            "aspirador nasal eletrico infantil"
        ],
        "ticket_medio": "R$ 180 - R$ 1.500"
    },
    "obra-ferramentas": {
        "title": "Obra, Reforma & Ferramentas",
        "search_terms": [
            "parafusadeira furadeira impacto 18v bosch",
            "lavadora alta pressao karcher",
            "trena a laser 40m",
            "jogo de chaves soquete catraca",
            "maleta de ferramentas completa"
        ],
        "ticket_medio": "R$ 150 - R$ 800"
    },
    "carros": {
        "title": "Carros, Garagem & Cuidados Automotivos",
        "search_terms": [
            "aspirador automotivo portatil 120w",
            "compressor de ar portatil pneu",
            "camera veicular dashcam",
            "suporte celular veicular magsafe",
            "shampoo automotivo cera vonixx"
        ],
        "ticket_medio": "R$ 80 - R$ 400"
    }
}

def generate_trend_report():
    print("=" * 65)
    print("🔥 RADAR BF - RELATÓRIO DE TERMOS MAIS BUSCADOS POR CATEGORIA")
    print(f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')} | Modo: Custo Zero ($0)")
    print("=" * 65)
    
    report_data = []

    for cat_id, data in NICHE_CATEGORIES.items():
        print(f"\n📂 CATEGORIA: {data['title'].upper()} ({cat_id})")
        print(f"   💰 Faixa de Ticket Recomendada: {data['ticket_medio']}")
        print("   🔍 Termos Quentes & Produtos para Garimpar:")
        for term in data["search_terms"]:
            # Gera URL de pesquisa direta nos 3 marketplaces
            amazon_url = f"https://www.amazon.com.br/s?k={urllib.parse.quote(term)}"
            ml_url = f"https://lista.mercadolivre.com.br/{urllib.parse.quote(term)}"
            shopee_url = f"https://shopee.com.br/search?keyword={urllib.parse.quote(term)}"
            print(f"      • {term}")
        
        report_data.append({
            "category_id": cat_id,
            "title": data["title"],
            "ticket_medio": data["ticket_medio"],
            "terms": data["search_terms"]
        })

    # Salva relatório para consumo de outros scripts
    with open("trending_report.json", "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 65)
    print("✅ Relatório salvo em 'trending_report.json' com sucesso!")
    print("💡 Próximo passo: Escolha um produto e use 'python scripts/generate_product.py' para cadastrar e criar os roteiros.")
    print("=" * 65)

if __name__ == "__main__":
    generate_trend_report()
