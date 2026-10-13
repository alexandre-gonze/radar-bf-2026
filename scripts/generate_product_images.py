"""
Radar BF - Gerador de Imagens Originais dos Produtos ($0)
Cria imagens estéticas em alta resolução (800x600) para cada um dos 35 produtos.
100% original, sem problemas de direitos autorais ou links quebrados da internet.
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

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "public", "products")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Esquema de cores vibrantes por categoria
CATEGORY_THEMES = {
    "estudantes": {
        "gradient_start": (15, 23, 42),
        "gradient_end": (30, 41, 59),
        "accent": (56, 189, 248), # Sky blue
        "tag_bg": (3, 105, 161),
        "icon": "🎓"
    },
    "ti-trabalho": {
        "gradient_start": (15, 23, 42),
        "gradient_end": (20, 20, 35),
        "accent": (168, 85, 247), # Purple neon
        "tag_bg": (107, 33, 168),
        "icon": "💻"
    },
    "gamers": {
        "gradient_start": (20, 10, 30),
        "gradient_end": (10, 10, 20),
        "accent": (236, 72, 153), # Pink neon
        "tag_bg": (157, 23, 77),
        "icon": "🎮"
    },
    "casa-cozinha": {
        "gradient_start": (20, 25, 20),
        "gradient_end": (10, 18, 15),
        "accent": (52, 211, 153), # Emerald
        "tag_bg": (6, 95, 70),
        "icon": "🍳"
    },
    "maes-bebes": {
        "gradient_start": (30, 20, 25),
        "gradient_end": (20, 15, 20),
        "accent": (251, 146, 60), # Warm peach/orange
        "tag_bg": (154, 52, 18),
        "icon": "👶"
    },
    "obra-ferramentas": {
        "gradient_start": (30, 25, 15),
        "gradient_end": (20, 18, 12),
        "accent": (250, 204, 21), # Amber yellow
        "tag_bg": (161, 98, 7),
        "icon": "🔨"
    },
    "carros": {
        "gradient_start": (15, 20, 30),
        "gradient_end": (10, 15, 22),
        "accent": (239, 68, 68), # Racing red
        "tag_bg": (153, 27, 27),
        "icon": "🚗"
    }
}

def create_product_image(product):
    width, height = 800, 560
    img = Image.new("RGB", (width, height), (11, 15, 25))
    draw = ImageDraw.Draw(img)

    cat = product.get("category", "estudantes")
    theme = CATEGORY_THEMES.get(cat, CATEGORY_THEMES["estudantes"])

    # 1. Fundo com gradiente radial/suave
    for y in range(height):
        ratio = y / height
        r = int(theme["gradient_start"][0] * (1 - ratio) + theme["gradient_end"][0] * ratio)
        g = int(theme["gradient_start"][1] * (1 - ratio) + theme["gradient_end"][1] * ratio)
        b = int(theme["gradient_start"][2] * (1 - ratio) + theme["gradient_end"][2] * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 2. Círculo de brilho central (ambient glow)
    center_x, center_y = width // 2, height // 2 - 20
    for radius in range(220, 0, -5):
        alpha_ratio = (220 - radius) / 220
        glow_r = int(theme["accent"][0] * alpha_ratio * 0.25)
        glow_g = int(theme["accent"][1] * alpha_ratio * 0.25)
        glow_b = int(theme["accent"][2] * alpha_ratio * 0.25)
        draw.ellipse(
            [center_x - radius, center_y - radius, center_x + radius, center_y + radius],
            outline=(glow_r, glow_g, glow_b),
            width=3
        )

    # 3. Card central estilizado (Mockup pedestal)
    pedestal_box = [center_x - 220, center_y - 120, center_x + 220, center_y + 120]
    draw.rounded_rectangle(pedestal_box, radius=24, fill=(17, 24, 39), outline=theme["accent"], width=2)

    # 4. Desenho de anéis de radar no pedestal
    for r in [40, 80, 120]:
        draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r], outline=(31, 41, 55), width=1)

    # 5. Tentativa de usar fonte TTF do sistema (Arial ou Segoe UI no Windows)
    try:
        font_large = ImageFont.truetype("arial.ttf", 26)
        font_badge = ImageFont.truetype("arialbd.ttf", 16)
        font_cat = ImageFont.truetype("arialbd.ttf", 13)
        font_tagline = ImageFont.truetype("arial.ttf", 14)
    except Exception:
        font_large = ImageFont.load_default()
        font_badge = ImageFont.load_default()
        font_cat = ImageFont.load_default()
        font_tagline = ImageFont.load_default()

    # 6. Badge da Categoria no topo
    cat_label = product.get("categoryLabel", "").upper()
    draw.rounded_rectangle([center_x - 140, 40, center_x + 140, 72], radius=16, fill=theme["tag_bg"])
    draw.text((center_x, 56), cat_label, fill=(255, 255, 255), font=font_cat, anchor="mm")

    # 7. Nome resumido central no pedestal
    name = product.get("name", "")
    # Quebra em 2 linhas se for longo
    words = name.split()
    line1 = " ".join(words[:4])
    line2 = " ".join(words[4:8]) if len(words) > 4 else ""
    line3 = " ".join(words[8:12]) if len(words) > 8 else ""

    draw.text((center_x, center_y - 25), line1, fill=(255, 255, 255), font=font_large, anchor="mm")
    if line2:
        draw.text((center_x, center_y + 10), line2, fill=(209, 213, 219), font=font_large, anchor="mm")
    if line3:
        draw.text((center_x, center_y + 40), line3, fill=(156, 163, 175), font=font_tagline, anchor="mm")

    # 8. Badge do produto (ex: Campeão Custo-Benefício BF)
    badge_text = product.get("badge", "DESTAQUE BLACK FRIDAY")
    draw.rounded_rectangle([40, height - 70, 320, height - 35], radius=10, fill=(220, 38, 38))
    draw.text((180, height - 52), f"🔥 {badge_text}", fill=(255, 255, 255), font=font_badge, anchor="mm")

    # 9. Selo Radar BF Oficial no canto inferior direito
    draw.text((width - 40, height - 52), "RADAR BF • SELEÇÃO VERIFICADA", fill=(107, 114, 128), font=font_cat, anchor="rm")

    # Salva imagem
    filename = f"{product['id']}.jpg"
    filepath = os.path.join(OUTPUT_DIR, filename)
    img.save(filepath, "JPEG", quality=90)
    return filepath

def main():
    json_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "products.json")
    with open(json_path, "r", encoding="utf-8") as f:
        products = json.load(f)

    print(f"🎨 Gerando imagens originais para {len(products)} produtos...")
    for idx, p in enumerate(products, 1):
        path = create_product_image(p)
        print(f"  [{idx:02d}/{len(products):02d}] Criado: {os.path.basename(path)}")

    print("\n✅ Todas as imagens originais foram geradas com sucesso em 'public/products/'!")

if __name__ == "__main__":
    main()
