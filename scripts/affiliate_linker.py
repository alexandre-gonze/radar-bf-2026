"""
Radar BF - Módulo de Monetização Automática de Links ($0)
Executado via Antigravity / Python 3

Regras de Negócio:
1. Se houver tag de afiliado configurada no .env, injeta a comissão automaticamente.
2. Limpa URLs removendo parâmetros desnecessários, cookies de terceiros e lixo de rastreamento.
3. Se NÃO houver tag de afiliado configurada para a loja, faz o fallback inteligente para o link direto limpo da loja.
4. Se o link for inválido, faz o fallback para o seu próprio Hub na Vercel.
"""

import os
import sys
import re
import urllib.parse

# Garante suporte a UTF-8 no Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ENV_PATH = os.path.join(os.path.dirname(__file__), "..", ".env")

def load_env():
    env_vars = {
        "AMAZON_ASSOCIATE_TAG": "",
        "MERCADO_LIVRE_AFFILIATE_TAG": "",
        "SHOPEE_AFFILIATE_ID": "",
        "RADAR_HUB_URL": "https://radar-bf-2026.vercel.app"
    }
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    env_vars[key.strip()] = val.strip()
    return env_vars

ENV = load_env()

def clean_amazon_url(url: str, tag: str = "") -> str:
    """Extrai o ASIN ou normaliza a busca da Amazon com a tag de afiliado"""
    parsed = urllib.parse.urlparse(url)
    
    # Verifica se é link de produto direto com ASIN (/dp/B0... ou /gp/product/B0...)
    asin_match = re.search(r'/(?:dp|gp/product)/([A-Z0-9]{10})', parsed.path)
    if asin_match:
        asin = asin_match.group(1)
        base = f"https://www.amazon.com.br/dp/{asin}"
        return f"{base}?tag={tag}" if tag else base

    # Se for busca ou catálogo
    query_params = urllib.parse.parse_qs(parsed.query)
    clean_params = {}
    if "k" in query_params:
        clean_params["k"] = query_params["k"][0]
    
    if tag:
        clean_params["tag"] = tag
        
    query_string = urllib.parse.urlencode(clean_params)
    return f"https://www.amazon.com.br/s?{query_string}" if query_string else url

def clean_mercadolivre_url(url: str, tag: str = "") -> str:
    """Limpa e formata link do Mercado Livre"""
    parsed = urllib.parse.urlparse(url)
    
    # Remove UTMs externas e lixo de tracking
    query_params = urllib.parse.parse_qs(parsed.query)
    clean_params = {}
    
    # Mantém termos de pesquisa
    for key in ["q", "as_word"]:
        if key in query_params:
            clean_params[key] = query_params[key][0]

    if tag:
        clean_params["matt_tool"] = tag

    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    if clean_params:
        return f"{base_url}?{urllib.parse.urlencode(clean_params)}"
    return base_url

def clean_shopee_url(url: str, tag: str = "") -> str:
    """Formata link da Shopee"""
    parsed = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed.query)
    clean_params = {}

    if "keyword" in query_params:
        clean_params["keyword"] = query_params["keyword"][0]

    if tag:
        clean_params["af_id"] = tag

    base_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    if clean_params:
        return f"{base_url}?{urllib.parse.urlencode(clean_params)}"
    return base_url

def monetize_url(url: str, product_id: str = None) -> tuple[str, bool]:
    """
    Monetiza a URL dada.
    Retorna: (url_final, is_monetized: bool)
    """
    if not url:
        hub = ENV.get("RADAR_HUB_URL", "https://radar-bf-2026.vercel.app")
        return (f"{hub}/#{product_id}" if product_id else hub, False)

    lower_url = url.lower()

    # 1. Amazon
    if "amazon.com" in lower_url:
        tag = ENV.get("AMAZON_ASSOCIATE_TAG", "").strip()
        final_url = clean_amazon_url(url, tag)
        return (final_url, bool(tag))

    # 2. Mercado Livre
    if "mercadolivre.com" in lower_url or "mercadolivre.com.br" in lower_url:
        tag = ENV.get("MERCADO_LIVRE_AFFILIATE_TAG", "").strip()
        final_url = clean_mercadolivre_url(url, tag)
        return (final_url, bool(tag))

    # 3. Shopee
    if "shopee.com" in lower_url or "shopee.com.br" in lower_url:
        tag = ENV.get("SHOPEE_AFFILIATE_ID", "").strip()
        final_url = clean_shopee_url(url, tag)
        return (final_url, bool(tag))

    # 4. Outra loja / fallback
    return (url, False)

if __name__ == "__main__":
    print("=" * 65)
    print("⚡ RADAR BF - TESTE DO MONETIZADOR DE LINKS DE AFILIADO")
    print("=" * 65)
    
    test_urls = [
        ("Amazon Produto", "https://www.amazon.com.br/dp/B0CKZJ8V4P?ref_=cm_sw_r_cp_ud_dp"),
        ("Amazon Busca", "https://www.amazon.com.br/s?k=notebook+ryzen+5&crid=123&sprefix=note"),
        ("Mercado Livre", "https://lista.mercadolivre.com.br/lenovo-ideapad-ryzen-5?utm_source=teste"),
        ("Shopee", "https://shopee.com.br/search?keyword=airfryer+mondial&order=desc")
    ]

    print(f"⚙️ Tag Amazon configurada: '{ENV.get('AMAZON_ASSOCIATE_TAG') or 'NENHUMA (Modo Fallback Loja Direta)'}'")
    print(f"⚙️ Tag ML configurada: '{ENV.get('MERCADO_LIVRE_AFFILIATE_TAG') or 'NENHUMA (Modo Fallback Loja Direta)'}'")
    print("-" * 65)

    for label, raw_url in test_urls:
        final_url, is_affiliate = monetize_url(raw_url)
        status = "🟢 AFILIADO ATIVO" if is_affiliate else "⚪ FALLBACK LOJA DIRETA"
        print(f"[{status}] {label}:")
        print(f"   Original: {raw_url}")
        print(f"   Gerado:   {final_url}\n")

    print("=" * 65)
