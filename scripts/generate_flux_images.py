"""
Radar BF - Gerador de Imagens Fotorrealistas Gratuitas com Flux / Pollinations ($0)
Gera fotos comerciais de produto e cenas reais de uso sem gastar nenhum token/crédito da sua cota.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse

# Garante suporte a UTF-8 no Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "public", "products")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Prompts fotorrealistas de produtos em uso real (em inglês para máxima fidelidade do modelo Flux)
PRODUCT_PROMPTS = {
    "tablet-samsung-galaxy-tab-s9-fe": (
        "Commercial lifestyle product photography of a Samsung Galaxy Tab S9 FE tablet on a clean wooden student desk. "
        "The S-Pen stylus is resting beside it with colorful handwritten digital study notes on the crisp screen. "
        "Warm natural morning window lighting, student notebooks and ceramic coffee mug nearby, 4k resolution."
    ),
    "fone-bluetooth-qcy-h3-anc": (
        "Commercial lifestyle photography of modern matte-black over-ear Bluetooth headphones with active noise cancelling. "
        "Resting on an aesthetic wooden desk next to a modern laptop and smartphone, with a student studying in the soft-focus background in a library. "
        "Warm cinematic lighting, crisp leather cushion textures, 4k."
    ),
    "mochila-impermeavel-antifurto-notebook": (
        "Lifestyle product photography of a sleek black waterproof anti-theft laptop backpack. "
        "A young professional wearing it outdoors in an urban modern city setting, water droplets beading off the waterproof fabric, "
        "ergonomic padded shoulder straps, clean aesthetic, 4k editorial."
    ),
    "cadeira-ergonomica-nr17-mesh": (
        "Architectural commercial photography of a high-end ergonomic black mesh office chair with lumbar support and headrest. "
        "Positioned neatly at a modern Scandinavian home office wooden desk with ultrawide monitor and potted plants, bright airy sunlight, 4k."
    ),
    "monitor-lg-ultrawide-29-polegadas": (
        "Commercial tech photography of an LG 29-inch 21:9 Ultrawide monitor on a clean minimalist desk. "
        "Screen displaying two large windows side-by-side with code and visual analytics, soft ambient LED backlighting, warm aesthetic."
    ),
    "teclado-mecanico-sem-fio-redragon": (
        "Close-up commercial product shot of a 60 percent compact mechanical wireless keyboard on a premium felt desk mat. "
        "Subtle tasteful RGB keycap backlighting, mechanical switches visible from the side, coffee cup and wireless mouse in soft focus, 4k."
    ),
    "hub-usb-c-7-em-1-hdmi-4k": (
        "Commercial product photography of an aluminum space-gray 7-in-1 USB-C hub plugged neatly into a sleek laptop. "
        "HDMI cable, USB flash drive, and SD card connected to the hub, clean desk surface, crisp metallic finish, professional studio lighting."
    ),
    "console-nintendo-switch-oled-64gb": (
        "Commercial lifestyle photography of a person's hands holding a white Nintendo Switch OLED in handheld mode. "
        "Vibrant colorful game on the 7-inch OLED screen, relaxing on a comfortable sofa in a sunlit living room, warm cozy atmosphere."
    ),
    "headset-hyperx-cloud-stinger-2": (
        "Commercial gaming lifestyle product photo of a HyperX Cloud Stinger 2 gaming headset. "
        "Resting on a premium RGB headphone stand next to a gaming keyboard with ambient neon red and purple lighting, 4k resolution."
    ),
    "mouse-gamer-logitech-g305-lightspeed": (
        "Dynamic commercial product photograph of a black Logitech G305 Lightspeed wireless gaming mouse on a large textured gaming mousepad. "
        "Crisp optical sensor details, ergonomic curvature, subtle blue ambient light accent, competitive gaming desk setup in soft focus."
    ),
    "monitor-gamer-aoc-hero-24-144hz": (
        "Commercial tech photography of a 24-inch 144Hz bezel-less gaming monitor on an adjustable ergonomic stand. "
        "Screen showing a high-fps fast-paced action esports game with fluid motion, dark gamer room with ambient backlighting."
    ),
    "robo-aspirador-wap-robot-w400": (
        "Commercial lifestyle photography of a sleek round smart robot vacuum cleaner operating on a gleaming light hardwood living room floor. "
        "Cleaning alongside a comfortable modern sofa, natural sunlight, spotless clean home interior, 4k resolution."
    ),
    "panela-pressao-eletrica-electrolux-5l": (
        "Commercial food and kitchen appliance photography of a modern digital 5L electric pressure cooker on a kitchen granite countertop. "
        "Stainless steel body with digital LED timer glowing, small appetizing steam rising, fresh herbs and wooden spoon nearby, 4k."
    ),
    "cafeteira-nespresso-essenza-mini": (
        "Commercial coffee advertising photography of a compact red and black Nespresso Essenza Mini espresso machine. "
        "Brewing rich crema into a transparent glass espresso cup on a modern kitchen counter, coffee beans scattered artfully, warm cafe lighting."
    ),
    "purificador-de-agua-consul-cpc31": (
        "Commercial clean home photography of a modern white water purifier mounted neatly on a clean kitchen subway tile wall. "
        "Pouring crystal-clear pure water into a tall transparent glass, fresh refreshing water droplets, bright airy kitchen."
    ),
    "carrinho-de-bebe-compacto-fechamento-automatico": (
        "Commercial parenting lifestyle photo of a modern ultra-compact folding baby stroller. "
        "Pushed smoothly on a paved park pathway by a parent on a sunny spring afternoon, trees in soft focus, lightweight premium design."
    ),
    "cadeirinha-auto-isofix-0-a-36kg": (
        "Commercial automotive interior photograph of a 360-degree rotating Isofix child safety car seat securely installed in the rear leather seat of an SUV. "
        "Plush padded headrest, 5-point harness safety buckles, natural light through the car window."
    ),
    "esterilizador-mamadeiras-philips-avent": (
        "Commercial clean health photograph of a steam baby bottle sterilizer on a kitchen counter with clean white bottles and pacifiers inside. "
        "Pure, hygienic, soft blue and white clean aesthetic, crystal clear plastic dome lid, spotless kitchen."
    ),
    "aspirador-nasal-eletrico-infantil": (
        "Commercial parenting product shot of a gentle electric baby nasal aspirator with soft silicone tip. "
        "Resting on a soft pastel nursery blanket next to a baby bottle and soothing wooden toy, gentle pastel morning light."
    ),
    "lavadora-alta-pressao-karcher-k2-turbo": (
        "Action commercial photography of a yellow and black high-pressure power washer in action outdoors. "
        "A high-pressure water jet spraying and powerfully cleaning outdoor stone pavers and driveway patio, water spray mist, dramatic clean contrast."
    ),
    "trena-laser-digital-40m-bosch-ou-dextools": (
        "Commercial construction and DIY photo of a digital laser distance meter held in hand. "
        "Bright red laser beam pointing at an interior room wall, illuminated digital LCD screen showing measurements, architectural blueprint nearby."
    ),
    "maleta-ferramentas-completa-110-pecas": (
        "Commercial hardware product photography of an open 110-piece chrome-vanadium tool set case on a sturdy wooden workbench. "
        "Gleaming ratchet wrenches, sockets, and pliers neatly organized in custom-molded slots, workshop tools in soft focus."
    ),
    "nivel-laser-360-linhas-verdes": (
        "Commercial construction product shot of a 360-degree self-leveling laser level mounted on a tripod in an interior room renovation. "
        "Vibrant bright green laser lines projecting across walls and tiled floors, professional construction atmosphere."
    ),
    "compressor-de-ar-digital-portatil-pneu": (
        "Commercial automotive photo of a compact handheld digital tire inflator connected to a car tire valve stem. "
        "Digital LED screen glowing showing tire PSI pressure, person kneeling beside the car on a clean driveway, modern portable gadget aesthetic."
    ),
    "camera-veicular-dashcam-frontal-traseira": (
        "Interior car photography showing a compact smart dashcam mounted neatly on the car windshield behind the rearview mirror. "
        "Screen showing a live road view, highway ahead visible through the windshield, modern dashboard interior."
    ),
    "suporte-celular-veicular-magsafe-inducao": (
        "Commercial automotive product photo of a magnetic wireless charging phone mount attached to a car air vent. "
        "Smartphone magnetically snapped on displaying GPS navigation, glowing charging ring, luxury car dashboard interior."
    ),
    "kit-lavagem-cera-carnauba-vonixx": (
        "Commercial auto detailing photography of car care products (shampoo bottle, carnauba wax jar, plush microfiber towel) "
        "resting beside a gleaming, mirror-finish black car hood with extreme water beading effect, professional detailing studio."
    )
}

# IDs que já possuem imagens de IA prontas e excelentes
ALREADY_GENERATED = {
    "notebook-lenovo-ideapad-ryzen-5",
    "airfryer-mondial-afn-40-ri",
    "parafusadeira-bosch-go-ou-gsb-180",
    "kindle-11-geracao-amazon",
    "aspirador-automotivo-portatil-sem-fio",
    "console-playstation-5-slim-1tb",
    "baba-eletronica-takdir-ou-motorola",
    "notebook-acer-nitro-v15-rtx3050",
    "tablet-samsung-galaxy-tab-s9-fe",
    "monitor-lg-ultrawide-29-polegadas",
    "headset-hyperx-cloud-stinger-2",
    "panela-pressao-eletrica-electrolux-5l",
    "cadeirinha-auto-isofix-0-a-36kg",
    "trena-laser-digital-40m-bosch-ou-dextools"
}

def generate_image_pollinations(product_id, prompt):
    filename = f"{product_id}.jpg"
    filepath = os.path.join(OUTPUT_DIR, filename)

    encoded_prompt = urllib.parse.quote(prompt)
    # Usa model=turbo que é 100% gratuito e não exige pagamento
    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=560&model=turbo&nologo=true"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    req = urllib.request.Request(url, headers=headers)

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=40) as response:
                data = response.read()
                if len(data) > 5000:
                    with open(filepath, "wb") as f:
                        f.write(data)
                    return True
        except Exception as e:
            if attempt == 2:
                print(f"    ⚠️ Erro ao gerar {product_id}: {e}")
            time.sleep(3)
    return False

def main():
    print("=" * 65)
    print("🚀 RADAR BF - GERAÇÃO FOTORREALISTA VIA FLUX (CUSTO $0)")
    print("Zero consumo de créditos da sua conta de IA • Totalmente gratuito")
    print("=" * 65)

    total = len(PRODUCT_PROMPTS)
    success_count = 0

    for idx, (prod_id, prompt) in enumerate(PRODUCT_PROMPTS.items(), 1):
        if prod_id in ALREADY_GENERATED:
            print(f"[{idx:02d}/{total}] Já gerado anteriormente: {prod_id}")
            continue

        print(f"[{idx:02d}/{total}] Gerando foto real via Flux: {prod_id}...")
        ok = generate_image_pollinations(prod_id, prompt)
        if ok:
            print(f"    ✅ Sucesso! Salvo em 'public/products/{prod_id}.jpg'")
            success_count += 1
        else:
            print(f"    ❌ Falha ao obter imagem para {prod_id}")
        time.sleep(1)

    print("\n" + "=" * 65)
    print(f"🎉 Finalizado! {success_count} novas fotos reais geradas com sucesso!")
    print("=" * 65)

if __name__ == "__main__":
    main()
