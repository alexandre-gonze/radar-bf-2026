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

    # 4. Foto Real do Produto e Cena de Uso
    product_img_path = os.path.join(os.path.dirname(__file__), "..", "public", "products", f"{product['id']}.jpg")
    photo_box = (60, 380, width - 60, 820)
    
    if os.path.exists(product_img_path):
        try:
            prod_photo = Image.open(product_img_path).convert("RGB")
            # Redimensiona para caber perfeitamente no box mantendo aspecto
            target_w = photo_box[2] - photo_box[0]
            target_h = photo_box[3] - photo_box[1]
            prod_photo = prod_photo.resize((target_w, target_h), Image.Resampling.LANCZOS)
            img.paste(prod_photo, (photo_box[0], photo_box[1]))
            # Borda estilizada ao redor da foto
            draw.rectangle([photo_box[0], photo_box[1], photo_box[2], photo_box[3]], outline=(220, 38, 38), width=3)
        except Exception:
            draw.rounded_rectangle([photo_box[0], photo_box[1], photo_box[2], photo_box[3]], radius=24, fill=(17, 24, 39), outline=(220, 38, 38), width=3)
    else:
        draw.rounded_rectangle([photo_box[0], photo_box[1], photo_box[2], photo_box[3]], radius=24, fill=(17, 24, 39), outline=(220, 38, 38), width=3)

    # Categoria badge sobreposta na foto
    cat_text = product.get("categoryLabel", "").upper()
    draw.rounded_rectangle([80, 400, 360, 445], radius=12, fill=(15, 23, 42))
    draw.text((220, 422), cat_text, fill=(56, 189, 248), font=font_badge, anchor="mm")

    # Nome do produto abaixo da foto
    draw.rounded_rectangle([60, 840, width - 60, 940], radius=16, fill=(17, 24, 39))
    words = product["name"].split()
    l1 = " ".join(words[:5])
    l2 = " ".join(words[5:10]) if len(words) > 5 else ""
    draw.text((width // 2, 870), l1, fill=(255, 255, 255), font=font_title, anchor="mm")
    if l2:
        draw.text((width // 2, 912), l2, fill=(209, 213, 219), font=font_body, anchor="mm")

    # 5. Destaque de Preço e Desconto
    price = product.get("estimatedPrice", "")
    disc = product.get("discountPercentage", 0)
    draw.rounded_rectangle([120, 960, width - 120, 1050], radius=20, fill=(16, 185, 129))
    draw.text((width // 2, 1005), f"OFERTA BF: {price} (-{disc}%)", fill=(255, 255, 255), font=font_badge, anchor="mm")

    # 6. Para quem serve (Diferencial)
    draw.rounded_rectangle([60, 1070, width - 60, 1340], radius=24, fill=(15, 23, 42), outline=(55, 65, 81), width=2)
    draw.text((100, 1105), "🟢 PARA QUEM É PERFEITO:", fill=(52, 211, 153), font=font_badge)
    
    y_offset = 1155
    for item in product["useCases"]["perfectFor"][:2]:
        draw.text((120, y_offset), f"• {item[:45]}...", fill=(229, 231, 235), font=font_body)
        y_offset += 45

    not_for = product["useCases"]["notRecommendedFor"][0] if product["useCases"]["notRecommendedFor"] else ""
    if not_for:
        draw.text((100, 1255), "🔴 NÃO COMPRE SE:", fill=(248, 113, 113), font=font_badge)
        draw.text((120, 1295), f"• {not_for[:45]}...", fill=(209, 213, 219), font=font_body)

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

    print(f"📌 Gerando Pins verticais com fotos reais para todos os {len(products)} produtos...")
    for idx, p in enumerate(products, 1):
        path = create_pin(p)
        print(f"  [{idx:02d}/{len(products)}] Pin criado: {os.path.basename(path)}")

    print(f"\n✅ Todos os {len(products)} Pins do Pinterest gerados em 'public/pins/' prontos para upload!")

if __name__ == "__main__":
    main()
