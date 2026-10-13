"""
Radar BF - Gerador de Pins para Pinterest ($0)
Gera imagens verticais no formato ideal do Pinterest (1000x1500 px, proporção 2:3)
com títulos chamativos de alta taxa de clique (CTR) e SEO visual.
"""

import os
import sys
import json
from PIL import Image, ImageDraw, ImageFont

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

PINS_DIR = os.path.join(os.path.dirname(__file__), "..", "public", "pins")
os.makedirs(PINS_DIR, exist_ok=True)

def create_pin(product):
    width, height = 1000, 1500
    img = Image.new("RGB", (width, height), (11, 15, 25))
    draw = ImageDraw.Draw(img)

    # 1. Gradiente dark premium
    for y in range(height):
        ratio = y / height
        r = int(15 * (1 - ratio) + 26 * ratio)
        g = int(23 * (1 - ratio) + 36 * ratio)
        b = int(42 * (1 - ratio) + 56 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 2. Faixa superior de Alerta Black Friday
    draw.rectangle([0, 0, width, 140], fill=(220, 38, 38))
    
    try:
        font_header = ImageFont.truetype("arialbd.ttf", 42)
        font_hook = ImageFont.truetype("arialbd.ttf", 64)
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_badge = ImageFont.truetype("arialbd.ttf", 36)
        font_body = ImageFont.truetype("arial.ttf", 34)
        font_footer = ImageFont.truetype("arialbd.ttf", 32)
    except Exception:
        font_header = ImageFont.load_default()
        font_hook = ImageFont.load_default()
        font_title = ImageFont.load_default()
        font_badge = ImageFont.load_default()
        font_body = ImageFont.load_default()
        font_footer = ImageFont.load_default()

    draw.text((width // 2, 70), "🔥 GUIA BLACK FRIDAY 2026", fill=(255, 255, 255), font=font_header, anchor="mm")

    # 3. Gancho de Curiosidade (O que bomba no Pinterest)
    draw.text((width // 2, 230), "VALE A PENA", fill=(245, 158, 11), font=font_hook, anchor="mm")
    draw.text((width // 2, 310), "OU É CILADA?", fill=(255, 255, 255), font=font_hook, anchor="mm")

    # 4. Box Central com Nome do Produto
    draw.rounded_rectangle([60, 400, width - 60, 780], radius=32, fill=(17, 24, 39), outline=(220, 38, 38), width=3)
    
    # Categoria badge
    cat_text = product.get("categoryLabel", "").upper()
    draw.rounded_rectangle([width // 2 - 200, 430, width // 2 + 200, 485], radius=20, fill=(31, 41, 55))
    draw.text((width // 2, 458), cat_text, fill=(56, 189, 248), font=font_footer, anchor="mm")

    # Nome do produto
    words = product["name"].split()
    l1 = " ".join(words[:4])
    l2 = " ".join(words[4:8]) if len(words) > 4 else ""
    l3 = " ".join(words[8:12]) if len(words) > 8 else ""

    draw.text((width // 2, 560), l1, fill=(255, 255, 255), font=font_title, anchor="mm")
    if l2:
        draw.text((width // 2, 630), l2, fill=(209, 213, 219), font=font_title, anchor="mm")
    if l3:
        draw.text((width // 2, 700), l3, fill=(156, 163, 175), font=font_body, anchor="mm")

    # 5. Destaque de Preço e Desconto
    price = product.get("estimatedPrice", "")
    disc = product.get("discountPercentage", 0)
    draw.rounded_rectangle([120, 830, width - 120, 950], radius=24, fill=(16, 185, 129))
    draw.text((width // 2, 890), f"PREÇO ESTIMADO: {price} (-{disc}%)", fill=(255, 255, 255), font=font_badge, anchor="mm")

    # 6. Para quem serve (Diferencial)
    draw.rounded_rectangle([60, 1000, width - 60, 1320], radius=28, fill=(15, 23, 42), outline=(55, 65, 81), width=2)
    draw.text((100, 1040), "🟢 PARA QUEM É PERFEITO:", fill=(52, 211, 153), font=font_badge)
    
    y_offset = 1100
    for item in product["useCases"]["perfectFor"][:2]:
        draw.text((120, y_offset), f"• {item[:45]}...", fill=(229, 231, 235), font=font_body)
        y_offset += 55

    not_for = product["useCases"]["notRecommendedFor"][0] if product["useCases"]["notRecommendedFor"] else ""
    if not_for:
        draw.text((100, 1220), "🔴 NÃO COMPRE SE:", fill=(248, 113, 113), font=font_badge)
        draw.text((120, 1270), f"• {not_for[:45]}...", fill=(209, 213, 219), font=font_body)

    # 7. Rodapé com Chamada para Ação e Link
    draw.rectangle([0, height - 120, width, height], fill=(17, 24, 39))
    draw.text((width // 2, height - 60), "👉 CLIQUE PARA VER O COMPARADOR COMPLETO", fill=(245, 158, 11), font=font_footer, anchor="mm")

    pin_filename = f"pin-{product['id']}.jpg"
    pin_path = os.path.join(PINS_DIR, pin_filename)
    img.save(pin_path, "JPEG", quality=90)
    return pin_path

def main():
    json_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "products.json")
    with open(json_path, "r", encoding="utf-8") as f:
        products = json.load(f)

    print(f"📌 Gerando Pins verticais para Pinterest (Top 10 produtos)...")
    for idx, p in enumerate(products[:10], 1):
        path = create_pin(p)
        print(f"  [{idx:02d}/10] Pin criado: {os.path.basename(path)}")

    print("\n✅ Pins do Pinterest gerados em 'public/pins/' prontos para upload!")

if __name__ == "__main__":
    main()
