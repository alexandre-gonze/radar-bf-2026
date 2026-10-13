"""
Radar BF - Construtor do Catálogo Expandido (35 Campeões de Black Friday)
Gera os 35 produtos com matriz de uso real e links Amazon monetizados (tag=radarbf-20).
"""

import sys
import json
import urllib.parse

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

AMAZON_TAG = "radarbf-20"

def make_amz(term):
    return f"https://www.amazon.com.br/s?k={urllib.parse.quote(term)}&tag={AMAZON_TAG}"

def make_ml(term):
    return f"https://lista.mercadolivre.com.br/{urllib.parse.quote(term)}"

def make_shp(term):
    return f"https://shopee.com.br/search?keyword={urllib.parse.quote(term)}"

PRODUCTS = [
    # ==========================================
    # 1. ESTUDANTES & FACULDADE
    # ==========================================
    {
        "id": "notebook-lenovo-ideapad-ryzen-5",
        "name": "Notebook Lenovo IdeaPad 1 AMD Ryzen 5 8GB 256GB SSD",
        "tagline": "O melhor equilíbrio para estudos, faculdade e home office com preço acessível",
        "category": "estudantes",
        "categoryLabel": "Estudantes & Faculdade",
        "badge": "Campeão Custo-Benefício BF",
        "imageUrl": "/products/notebook-lenovo-ideapad-ryzen-5.jpg",
        "estimatedPrice": "R$ 2.199,00",
        "originalPrice": "R$ 2.899,00",
        "discountPercentage": 24,
        "useCases": {
            "perfectFor": [
                "Aulas online, PDFs pesados e pesquisas com 20+ abas no navegador",
                "Pacote Office completo (Word, Excel com fórmulas, PowerPoint)",
                "Trabalho remoto leve e videochamadas no Google Meet/Teams",
                "Inicialização rápida em menos de 10 segundos com SSD NVMe"
            ],
            "goodFor": [
                "Edição de artes para redes sociais no Canva",
                "Assistir streaming em Full HD com boa autonomia de bateria"
            ],
            "notRecommendedFor": [
                "Jogos pesados modernos (Cyberpunk, Warzone, GTA V no alto)",
                "Renderização profissional de vídeos em 4K no Premiere/After Effects",
                "Modelagem 3D pesada em Blender ou AutoCAD volumoso"
            ]
        },
        "specsSummary": [
            {"label": "Processador", "value": "Ryzen 5 7520U"},
            {"label": "Memória RAM", "value": "8GB LPDDR5"},
            {"label": "Armazenamento", "value": "256GB NVMe SSD"},
            {"label": "Tela", "value": "15.6 polegadas Antirreflexo"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("lenovo ideapad 1 ryzen 5"),
            "mercadoLivre": make_ml("lenovo-ideapad-ryzen-5"),
            "shopee": make_shp("lenovo ideapad 1")
        },
        "verifiedDeal": True
    },
    {
        "id": "tablet-samsung-galaxy-tab-s9-fe",
        "name": "Tablet Samsung Galaxy Tab S9 FE 128GB com Caneta S-Pen",
        "tagline": "O melhor substituto do caderno tradicional para resumos e anotações digitais",
        "category": "estudantes",
        "categoryLabel": "Estudantes & Faculdade",
        "badge": "Top 1 em Produtividade",
        "imageUrl": "/products/tablet-samsung-galaxy-tab-s9-fe.jpg",
        "estimatedPrice": "R$ 2.399,00",
        "originalPrice": "R$ 3.299,00",
        "discountPercentage": 27,
        "useCases": {
            "perfectFor": [
                "Anotar em PDFs, livros e resumos com a caneta S-Pen inclusa (sem atraso)",
                "Levar para a sala de aula sem carregar peso (bateria para o dia todo)",
                "Modo Samsung DeX para usar como um mini-notebook com teclado",
                "Resistência à água e poeira (IP68)"
            ],
            "goodFor": [
                "Desenho e ilustração digital em apps como Clip Studio e Canva",
                "Assistir videoaulas com tela brilhante de 90Hz"
            ],
            "notRecommendedFor": [
                "Substituir 100% um computador se você usa softwares legados de Windows",
                "Jogos pesados com gráficos no ultra"
            ]
        },
        "specsSummary": [
            {"label": "Tela", "value": "10.9 polegadas 90Hz"},
            {"label": "Caneta", "value": "S-Pen inclusa na caixa"},
            {"label": "Armazenamento", "value": "128GB expansível via microSD"},
            {"label": "Proteção", "value": "IP68 contra água"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("samsung galaxy tab s9 fe"),
            "mercadoLivre": make_ml("samsung-galaxy-tab-s9-fe"),
            "shopee": make_shp("galaxy tab s9 fe")
        },
        "verifiedDeal": True
    },
    {
        "id": "kindle-11-geracao-amazon",
        "name": "Kindle 11ª Geração Amazon 16GB com Luz Embutida Ajustável",
        "tagline": "Milhares de livros e apostilas no bolso sem cansar a vista com reflexos de tela",
        "category": "estudantes",
        "categoryLabel": "Estudantes & Faculdade",
        "badge": "Mais Desejado Black Friday",
        "imageUrl": "/products/kindle-11-geracao-amazon.jpg",
        "estimatedPrice": "R$ 449,00",
        "originalPrice": "R$ 599,00",
        "discountPercentage": 25,
        "useCases": {
            "perfectFor": [
                "Leitura de livros, apostilas e artigos por horas sem cansaço visual (tela e-ink)",
                "Bateria que dura até 6 semanas com uma única recarga",
                "Leitura noturna na cama com iluminação embutida sem atrapalhar o sono",
                "Dicionário embutido e tradutor instantâneo ao tocar nas palavras"
            ],
            "goodFor": [
                "Leitura de arquivos PDF com texto corrido"
            ],
            "notRecommendedFor": [
                "PDFs técnicos complexos com tabelas e gráficos coloridos (a tela é em preto e branco)",
                "Navegação na internet (o foco é 100% leitura sem distrações)"
            ]
        },
        "specsSummary": [
            {"label": "Armazenamento", "value": "16GB (armazena milhares de e-books)"},
            {"label": "Tela", "value": "6 polegadas 300 ppi antirreflexo"},
            {"label": "Bateria", "value": "Até 6 semanas de duração"},
            {"label": "Conexão", "value": "USB-C e Wi-Fi"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("kindle 11 geracao 16gb"),
            "mercadoLivre": make_ml("kindle-11-geracao"),
            "shopee": make_shp("kindle 11 geracao")
        },
        "verifiedDeal": True
    },
    {
        "id": "fone-bluetooth-qcy-h3-anc",
        "name": "Fone de Ouvido Bluetooth QCY H3 com Cancelamento Ativo de Ruído (ANC)",
        "tagline": "Silêncio absoluto para estudar em ambientes barulhentos por uma fração do preço de marcas caras",
        "category": "estudantes",
        "categoryLabel": "Estudantes & Faculdade",
        "badge": "Sensação Custo-Benefício",
        "imageUrl": "/products/fone-bluetooth-qcy-h3-anc.jpg",
        "estimatedPrice": "R$ 219,00",
        "originalPrice": "R$ 349,00",
        "discountPercentage": 37,
        "useCases": {
            "perfectFor": [
                "Focar nos estudos na biblioteca, transporte público ou em casa isolando ruídos externos",
                "Videochamadas e aulas online com microfone limpo com redução de ruído",
                "Bateria monstruosa de até 60 horas de reprodução contínua",
                "Conexão multiponto (conecta no notebook e no celular ao mesmo tempo)"
            ],
            "goodFor": [
                "Ouvir músicas com graves encorpados e equalização via aplicativo oficial"
            ],
            "notRecommendedFor": [
                "Corridas intensas na chuva (resistência básica a suor)",
                "Audiófilos que buscam fones de estúdio de monitoramento profissional"
            ]
        },
        "specsSummary": [
            {"label": "Isolamento", "value": "ANC Híbrido até -43dB"},
            {"label": "Bateria", "value": "Até 60 horas (40h com ANC ativo)"},
            {"label": "Drivers", "value": "40mm com certificação Hi-Res"},
            {"label": "Conexão", "value": "Bluetooth 5.4 + Cabo P2"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("fone qcy h3 anc cancelamento ruido"),
            "mercadoLivre": make_ml("fone-qcy-h3"),
            "shopee": make_shp("qcy h3 anc")
        },
        "verifiedDeal": True
    },
    {
        "id": "mochila-impermeavel-antifurto-notebook",
        "name": "Mochila Impermeável Antifurto para Notebook 15.6 com Saída USB",
        "tagline": "Proteja seu notebook da chuva e de furtos no transporte público com divisórias inteligentes",
        "category": "estudantes",
        "categoryLabel": "Estudantes & Faculdade",
        "badge": "Essencial do Dia a Dia",
        "imageUrl": "/products/mochila-impermeavel-antifurto-notebook.jpg",
        "estimatedPrice": "R$ 119,00",
        "originalPrice": "R$ 199,00",
        "discountPercentage": 40,
        "useCases": {
            "perfectFor": [
                "Estudantes que usam ônibus, metrô e trem (zíper oculto antifurto nas costas)",
                "Dias de chuva forte sem molhar notebook, cadernos e eletrônicos",
                "Carregar o celular na rua usando o conector externo USB acoplado a um powerbank",
                "Organização de cabos, mouse, carregador e garrafa de água"
            ],
            "goodFor": [
                "Viagens curtas de fim de semana como mala de bordo"
            ],
            "notRecommendedFor": [
                "Trilhas pesadas de montanha ou camping (o foco é uso urbano/acadêmico)"
            ]
        },
        "specsSummary": [
            {"label": "Capacidade", "value": "Comporta notebooks de até 15.6 polegadas"},
            {"label": "Material", "value": "Tecido Oxford Impermeável e resistente a riscos"},
            {"label": "Recursos", "value": "Porta USB externa + Bolso antifurto traseiro"},
            {"label": "Alças", "value": "Acolchoadas e respiráveis em favo de mel"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("mochila antifurto impermeavel notebook 15.6"),
            "mercadoLivre": make_ml("mochila-antifurto-notebook"),
            "shopee": make_shp("mochila antifurto notebook")
        },
        "verifiedDeal": True
    },

    # ==========================================
    # 2. TI & PRODUTIVIDADE / HOME OFFICE
    # ==========================================
    {
        "id": "notebook-acer-nitro-v15-rtx3050",
        "name": "Notebook Gamer Acer Nitro V15 Intel i5 16GB 512GB RTX 3050",
        "tagline": "Máquina potente para programadores, criadores de conteúdo e gamers exigentes",
        "category": "ti-trabalho",
        "categoryLabel": "TI & Produtividade",
        "badge": "Mais Potência por Menor Preço",
        "imageUrl": "/products/notebook-acer-nitro-v15-rtx3050.jpg",
        "estimatedPrice": "R$ 4.299,00",
        "originalPrice": "R$ 5.499,00",
        "discountPercentage": 21,
        "useCases": {
            "perfectFor": [
                "Desenvolvedores de software (Docker, VS Code com dezenas de extensões, emuladores Android/iOS)",
                "Edição e renderização de vídeos em 1080p e 4K (GPU dedicada RTX com aceleração NVENC)",
                "Jogos modernos com taxa de quadros fluida (144Hz)",
                "Engenharia, arquitetura e softwares CAD / Revit"
            ],
            "goodFor": [
                "Substituir totalmente um PC Desktop em casa com monitor externo",
                "Lives e streaming de gameplay básica"
            ],
            "notRecommendedFor": [
                "Quem busca um notebook ultra leve para levar na bolsa o dia todo (pesa ~2.2 kg)",
                "Quem precisa de mais de 5 horas de bateria longe da tomada (notebook gamer exige fonte)"
            ]
        },
        "specsSummary": [
            {"label": "Processador", "value": "Intel Core i5 13ª Geração"},
            {"label": "Placa de Vídeo", "value": "NVIDIA GeForce RTX 3050 6GB"},
            {"label": "Memória RAM", "value": "16GB DDR5 (expansível)"},
            {"label": "Tela", "value": "15.6 IPS 144Hz"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("acer nitro v15 rtx 3050"),
            "mercadoLivre": make_ml("acer-nitro-v15-rtx-3050"),
            "shopee": make_shp("acer nitro v15")
        },
        "verifiedDeal": True
    },
    {
        "id": "cadeira-ergonomica-nr17-mesh",
        "name": "Cadeira Ergonômica de Escritório NR17 com Apoio Lombar e Braços 3D",
        "tagline": "Diga adeus às dores nas costas após 8 horas trabalhando sentado na frente do computador",
        "category": "ti-trabalho",
        "categoryLabel": "TI & Produtividade",
        "badge": "Saúde & Ergonomia",
        "imageUrl": "/products/cadeira-ergonomica-nr17-mesh.jpg",
        "estimatedPrice": "R$ 689,00",
        "originalPrice": "R$ 999,00",
        "discountPercentage": 31,
        "useCases": {
            "perfectFor": [
                "Profissionais de TI, designers e redatores que trabalham 8+ horas sentados",
                "Dias quentes de verão (encosto 100% em tela Mesh respirável que não esquenta)",
                "Ajuste personalizado: altura do apoio de cabeça, curvatura lombar e inclinação",
                "Atende integralmente à norma regulamentadora de ergonomia NR-17"
            ],
            "goodFor": [
                "Pessoas de 1,60m até 1,88m de altura com até 130 kg"
            ],
            "notRecommendedFor": [
                "Quem prefere cadeira gamer de couro sintético fechado (couro esquenta e descasca com o tempo)"
            ]
        },
        "specsSummary": [
            {"label": "Certificação", "value": "Norma Ergonômica NR-17"},
            {"label": "Material", "value": "Mesh respirável de alta densidade"},
            {"label": "Apoio de Braço", "value": "Ajuste 3D (altura, ângulo e profundidade)"},
            {"label": "Pistão", "value": "Gás Classe 4 reforçado até 130kg"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("cadeira ergonomica escritorio nr17 mesh"),
            "mercadoLivre": make_ml("cadeira-ergonomica-nr17"),
            "shopee": make_shp("cadeira ergonomica nr17")
        },
        "verifiedDeal": True
    },
    {
        "id": "monitor-lg-ultrawide-29-polegadas",
        "name": "Monitor LG Ultrawide 29 Polegadas IPS Full HD com HDR10 e 75Hz",
        "tagline": "O dobro de espaço na tela: trabalhe com duas janelas grandes abertas lado a lado",
        "category": "ti-trabalho",
        "categoryLabel": "TI & Produtividade",
        "badge": "O Queridinho dos Devs",
        "imageUrl": "/products/monitor-lg-ultrawide-29-polegadas.jpg",
        "estimatedPrice": "R$ 1.049,00",
        "originalPrice": "R$ 1.499,00",
        "discountPercentage": 30,
        "useCases": {
            "perfectFor": [
                "Programação (código aberto de um lado e documentação/preview do outro)",
                "Edição de vídeo (linha do tempo do Premiere/DaVinci esticada sem aperto)",
                "Planilhas gigantescas no Excel com dezenas de colunas visíveis sem rolar",
                "Painel IPS com cores precisas (sRGB 99%) para edição de fotos"
            ],
            "goodFor": [
                "Jogos imersivos com campo de visão 21:9 mais amplo"
            ],
            "notRecommendedFor": [
                "Mesas muito pequenas com menos de 70cm de largura",
                "Jogadores competitivos de CS2 ou Valorant que exigem 240Hz"
            ]
        },
        "specsSummary": [
            {"label": "Proporção", "value": "21:9 Ultrawide IPS"},
            {"label": "Resolução", "value": "Full HD 2560 x 1080"},
            {"label": "Cores", "value": "sRGB 99% + HDR10"},
            {"label": "Recursos", "value": "Modo Leitura antirreflexo e OnScreen Control"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("monitor lg ultrawide 29 polegadas ips"),
            "mercadoLivre": make_ml("monitor-lg-ultrawide-29"),
            "shopee": make_shp("monitor lg ultrawide 29")
        },
        "verifiedDeal": True
    },
    {
        "id": "teclado-mecanico-sem-fio-redragon",
        "name": "Teclado Mecânico Sem Fio RGB Bluetooth / 2.4Ghz Redragon Fizz Pro",
        "tagline": "Mesa limpa sem fios e digitação rápida e precisa para programar e jogar",
        "category": "ti-trabalho",
        "categoryLabel": "TI & Produtividade",
        "badge": "Setup Limpo",
        "imageUrl": "/products/teclado-mecanico-sem-fio-redragon.jpg",
        "estimatedPrice": "R$ 259,00",
        "originalPrice": "R$ 389,00",
        "discountPercentage": 33,
        "useCases": {
            "perfectFor": [
                "Trabalhar no notebook ou tablet alternando a conexão por Bluetooth com 1 tecla",
                "Digitação tátil e prazerosa sem atraso de resposta (conexão tri-mode)",
                "Setup compacto (60%) que libera muito espaço para movimentar o mouse",
                "Switches mecânicos removíveis (Hot-swap)"
            ],
            "goodFor": [
                "Jogos casuais e competitivos com cabo USB-C ou dongle 2.4GHz"
            ],
            "notRecommendedFor": [
                "Profissionais de contabilidade que precisam de teclado numérico físico dedicado à direita"
            ]
        },
        "specsSummary": [
            {"label": "Conexão", "value": "Tri-Mode: Bluetooth 5.0, 2.4GHz e Cabo USB-C"},
            {"label": "Layout", "value": "Compacto 60% com teclas de alta durabilidade"},
            {"label": "Switches", "value": "Mecânicos Red suaves e silenciosos"},
            {"label": "Bateria", "value": "Recarregável de longa autonomia"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("teclado mecanico sem fio redragon fizz pro"),
            "mercadoLivre": make_ml("teclado-redragon-fizz-pro"),
            "shopee": make_shp("redragon fizz pro sem fio")
        },
        "verifiedDeal": True
    },
    {
        "id": "hub-usb-c-7-em-1-hdmi-4k",
        "name": "Hub Adaptador USB-C 7 em 1 com Saída HDMI 4K e Carregamento PD 100W",
        "tagline": "Conecte monitor, teclado, mouse e pendrive no notebook moderno usando apenas 1 porta",
        "category": "ti-trabalho",
        "categoryLabel": "TI & Produtividade",
        "badge": "Acessório Indispensável",
        "imageUrl": "/products/hub-usb-c-7-em-1-hdmi-4k.jpg",
        "estimatedPrice": "R$ 139,00",
        "originalPrice": "R$ 229,00",
        "discountPercentage": 39,
        "useCases": {
            "perfectFor": [
                "Notebooks modernos (MacBook, Dell, Lenovo, Asus) que vêm com poucas portas USB",
                "Ligar o notebook a uma TV ou monitor externo em resolução 4K cristalina",
                "Carregar o notebook enquanto usa todos os periféricos (Power Delivery até 100W)",
                "Transferência veloz de fotos de câmera através do leitor de cartão SD e TF"
            ],
            "goodFor": [
                "Conectar no smartphone ou tablet compatível para espelhar a tela"
            ],
            "notRecommendedFor": [
                "Notebooks antigos que possuem apenas porta USB tradicional (USB-A quadrada)"
            ]
        },
        "specsSummary": [
            {"label": "Portas", "value": "1x HDMI 4K, 1x USB-C PD 100W, 3x USB 3.0, Leitores SD/TF"},
            {"label": "Construção", "value": "Alumínio aeroespacial com dissipação térmica"},
            {"label": "Compatibilidade", "value": "Windows, macOS, Linux, iPadOS, Android"},
            {"label": "Velocidade", "value": "USB 3.0 com transferência até 5Gbps"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("hub usb c 7 em 1 hdmi 4k power delivery"),
            "mercadoLivre": make_ml("hub-usb-c-7-em-1"),
            "shopee": make_shp("hub usb c 7 em 1")
        },
        "verifiedDeal": True
    },

    # ==========================================
    # 3. SETUP GAMER & CONSOLES
    # ==========================================
    {
        "id": "console-playstation-5-slim-1tb",
        "name": "Console PlayStation 5 Slim Edição com Leitor de Disco 1TB SSD",
        "tagline": "O console mais vendido da geração com gráficos ultra-realistas e jogos exclusivos",
        "category": "gamers",
        "categoryLabel": "Setup & Games",
        "badge": "Top Vendas Black Friday",
        "imageUrl": "/products/console-playstation-5-slim-1tb.jpg",
        "estimatedPrice": "R$ 3.599,00",
        "originalPrice": "R$ 4.299,00",
        "discountPercentage": 16,
        "useCases": {
            "perfectFor": [
                "Jogar os grandes lançamentos com ray tracing em 4K e até 120 FPS",
                "Exclusivos imperdíveis (Spider-Man 2, God of War Ragnarok, The Last of Us)",
                "Controle DualSense com gatilhos adaptáveis e resposta tátil revolucionária",
                "Carregamentos quase instantâneos com o SSD ultrarrápido customizado"
            ],
            "goodFor": [
                "Central multimídia da sala (Netflix, YouTube, Prime Video, Blu-ray 4K Ultra HD)"
            ],
            "notRecommendedFor": [
                "Quem busca jogos exclusivos da Nintendo (Mario, Zelda) ou portabilidade fora de casa"
            ]
        },
        "specsSummary": [
            {"label": "Armazenamento", "value": "1TB SSD NVMe de alta velocidade"},
            {"label": "Mídia", "value": "Leitor de disco Blu-ray Ultra HD incluso"},
            {"label": "Controle", "value": "1x DualSense sem fio com feedback háptico"},
            {"label": "Design", "value": "Slim mais compacto e leve que o PS5 original"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("playstation 5 slim com leitor 1tb"),
            "mercadoLivre": make_ml("playstation-5-slim"),
            "shopee": make_shp("playstation 5 slim")
        },
        "verifiedDeal": True
    },
    {
        "id": "console-nintendo-switch-oled-64gb",
        "name": "Console Nintendo Switch OLED 64GB com Joy-Con Branco",
        "tagline": "Diversão em qualquer lugar: jogue na TV da sala ou no modo portátil com tela OLED vibrante",
        "category": "gamers",
        "categoryLabel": "Setup & Games",
        "badge": "Favorito das Famílias",
        "imageUrl": "/products/console-nintendo-switch-oled-64gb.jpg",
        "estimatedPrice": "R$ 1.999,00",
        "originalPrice": "R$ 2.699,00",
        "discountPercentage": 26,
        "useCases": {
            "perfectFor": [
                "Jogar em viagens, transporte público ou na cama com cores pretas perfeitas (OLED 7 polegadas)",
                "Jogar com amigos e família na TV (Mario Kart, Mario Party, Smash Bros)",
                "Quem ama franquias consagradas (Zelda Tears of the Kingdom, Pokémon)",
                "Suporte traseiro ajustável muito mais estável para apoiar na mesa"
            ],
            "goodFor": [
                "Jogos indie e RPGs leves em qualquer lugar"
            ],
            "notRecommendedFor": [
                "Quem busca gráficos 4K ultra-pesados e jogos competitivos de tiro (Call of Duty)"
            ]
        },
        "specsSummary": [
            {"label": "Tela", "value": "7.0 polegadas OLED com cores intensas"},
            {"label": "Armazenamento", "value": "64GB interno (expansível via cartão microSD)"},
            {"label": "Áudio", "value": "Alto-falantes aprimorados no modo portátil"},
            {"label": "Dock", "value": "Base com porta LAN para internet cabeada"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("nintendo switch oled branco"),
            "mercadoLivre": make_ml("nintendo-switch-oled"),
            "shopee": make_shp("nintendo switch oled")
        },
        "verifiedDeal": True
    },
    {
        "id": "headset-hyperx-cloud-stinger-2",
        "name": "Headset Gamer HyperX Cloud Stinger 2 com Drivers de 50mm e Áudio Espacial",
        "tagline": "Ouça os passos dos inimigos com precisão sem ficar com a orelha doendo após horas de jogo",
        "category": "gamers",
        "categoryLabel": "Setup & Games",
        "badge": "Melhor Áudio Custo-Benefício",
        "imageUrl": "/products/headset-hyperx-cloud-stinger-2.jpg",
        "estimatedPrice": "R$ 189,00",
        "originalPrice": "R$ 299,00",
        "discountPercentage": 36,
        "useCases": {
            "perfectFor": [
                "Jogos competitivos de tiro (CS2, Valorant, Fortnite, Warzone) com áudio posicional 3D",
                "Quem joga por muitas horas (pesa menos de 275 gramas com almofadas macias de espuma viscoelástica)",
                "Microfone com cancelamento de ruído que muta automaticamente ao levantar a haste",
                "Compatível com PC, PlayStation, Xbox, Nintendo Switch e Celular"
            ],
            "goodFor": [
                "Aulas online e reuniões de trabalho no Discord/Teams"
            ],
            "notRecommendedFor": [
                "Quem exige conexão sem fio (este modelo possui cabo P3/P2 reforçado para zero latência)"
            ]
        },
        "specsSummary": [
            {"label": "Drivers", "value": "50mm direcionais com agudos limpos e graves fortes"},
            {"label": "Áudio", "value": "DTS Headphone:X Spatial Audio incluso"},
            {"label": "Microfone", "value": "Bidirecional com função Girar-para-Mutar"},
            {"label": "Peso", "value": "Ultraleve (apenas 275g)"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("hyperx cloud stinger 2 headset"),
            "mercadoLivre": make_ml("hyperx-cloud-stinger-2"),
            "shopee": make_shp("cloud stinger 2")
        },
        "verifiedDeal": True
    },
    {
        "id": "mouse-gamer-logitech-g305-lightspeed",
        "name": "Mouse Gamer Sem Fio Logitech G305 Lightspeed Sensor HERO 12K DPI",
        "tagline": "Desempenho de nível profissional sem nenhum fio na mesa e pilha que dura 9 meses",
        "category": "gamers",
        "categoryLabel": "Setup & Games",
        "badge": "Lenda dos E-Sports",
        "imageUrl": "/products/mouse-gamer-logitech-g305-lightspeed.jpg",
        "estimatedPrice": "R$ 199,00",
        "originalPrice": "R$ 299,00",
        "discountPercentage": 33,
        "useCases": {
            "perfectFor": [
                "Jogadores que não toleram delay (tecnologia Lightspeed de 1ms, mais rápida que mouse com fio)",
                "Esquecer de recarregar: 1 pilha AA comum dura até 250 horas de jogo contínuo (cerca de 9 meses no dia a dia)",
                "Sensor HERO de precisão cirúrgica sem aceleração indesejada",
                "Levar na mochila com o receptor USB guardado dentro do próprio corpo do mouse"
            ],
            "goodFor": [
                "Uso diário de trabalho e produtividade no escritório"
            ],
            "notRecommendedFor": [
                "Quem tem mãos muito grandes e gosta de pegada 'Palm' totalmente espalmada"
            ]
        },
        "specsSummary": [
            {"label": "Sensor", "value": "HERO óptico de 200 a 12.000 DPI"},
            {"label": "Conexão", "value": "Sem fio Lightspeed de 1ms de resposta"},
            {"label": "Bateria", "value": "Até 9 meses com 1 pilha AA"},
            {"label": "Botões", "value": "6 botões totalmente programáveis"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("logitech g305 sem fio lightspeed"),
            "mercadoLivre": make_ml("mouse-logitech-g305"),
            "shopee": make_shp("logitech g305")
        },
        "verifiedDeal": True
    },
    {
        "id": "monitor-gamer-aoc-hero-24-144hz",
        "name": "Monitor Gamer AOC Hero 24 Polegadas 144Hz 1ms IPS FreeSync",
        "tagline": "Fluidez total em jogos de tiro com base ajustável em altura e rotação vertical",
        "category": "gamers",
        "categoryLabel": "Setup & Games",
        "badge": "Campeão de Vendas E-Sports",
        "imageUrl": "/products/monitor-gamer-aoc-hero-24-144hz.jpg",
        "estimatedPrice": "R$ 879,00",
        "originalPrice": "R$ 1.249,00",
        "discountPercentage": 29,
        "useCases": {
            "perfectFor": [
                "Jogos de tiro em primeira pessoa (CS2, Valorant, Apex, Overwatch) com 144 quadros por segundo",
                "Painel IPS com cores vibrantes e ângulo de visão de 178° (sem distorção de cores)",
                "Base articulada completa (ajuste de altura, inclinação e giro de 90° em modo retrato)",
                "Tecnologia AMD FreeSync Premium que elimina cortes e engasgos na tela"
            ],
            "goodFor": [
                "Usar como segundo monitor na vertical para ler chat da Twitch ou código"
            ],
            "notRecommendedFor": [
                "Quem busca resolução 4K para consoles de nova geração (a resolução nativa é Full HD 1080p ideal para 24 polegadas)"
            ]
        },
        "specsSummary": [
            {"label": "Taxa de Atualização", "value": "144Hz ultrarrápido"},
            {"label": "Tempo de Resposta", "value": "1ms MPRT"},
            {"label": "Painel", "value": "24 polegadas IPS antirreflexo com bordas ultrafinas"},
            {"label": "Ergonomia", "value": "Base com ajuste de altura e giro pivot"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("monitor gamer aoc hero 24 144hz ips"),
            "mercadoLivre": make_ml("monitor-aoc-hero-24-144hz"),
            "shopee": make_shp("aoc hero 24 144hz")
        },
        "verifiedDeal": True
    },

    # ==========================================
    # 4. CASA & COZINHA INTELIGENTE
    # ==========================================
    {
        "id": "airfryer-mondial-afn-40-ri",
        "name": "Fritadeira Sem Óleo Airfryer Mondial Grand Family 4 Litros",
        "tagline": "A queridinha do Brasil: rápida, fácil de lavar e perfeita para famílias de até 4 pessoas",
        "category": "casa-cozinha",
        "categoryLabel": "Casa & Cozinha",
        "badge": "Top 1 Mais Vendido Brasil",
        "imageUrl": "/products/airfryer-mondial-afn-40-ri.jpg",
        "estimatedPrice": "R$ 249,00",
        "originalPrice": "R$ 389,00",
        "discountPercentage": 36,
        "useCases": {
            "perfectFor": [
                "Fritar batata, frango, legumes e esquentar pão sem pingar uma gota de óleo",
                "Casais e famílias pequenas (cesto quadrado de 4L que cabe até frango inteiro pequeno)",
                "Quem quer economia de gás e rapidez no almoço/jantar"
            ],
            "goodFor": [
                "Fazer bolos pequenos e pudins em formas compatíveis",
                "Descongelar alimentos rapidamente"
            ],
            "notRecommendedFor": [
                "Grandes churrascos ou famílias de 6+ pessoas (neste caso opte pelo modelo de 8L / Dual Zone)",
                "Quem não quer lavar a grelha manualmente após cada preparo"
            ]
        },
        "specsSummary": [
            {"label": "Capacidade", "value": "4 Litros"},
            {"label": "Potência", "value": "1500W"},
            {"label": "Timer", "value": "60 minutos com desligamento automático"},
            {"label": "Revestimento", "value": "Antiaderente Duraflon"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("airfryer mondial 4l"),
            "mercadoLivre": make_ml("airfryer-mondial-4-litros"),
            "shopee": make_shp("airfryer mondial")
        },
        "verifiedDeal": True
    },
    {
        "id": "robo-aspirador-wap-robot-w400",
        "name": "Robô Aspirador Inteligente WAP Robot W400 Varre, Aspira e Passa Pano",
        "tagline": "Casa sempre limpa sem esforço: recolhe pelos de animais e poeira sozinho enquanto você trabalha",
        "category": "casa-cozinha",
        "categoryLabel": "Casa & Cozinha",
        "badge": "Paz de Espírito no Lar",
        "imageUrl": "/products/robo-aspirador-wap-robot-w400.jpg",
        "estimatedPrice": "R$ 899,00",
        "originalPrice": "R$ 1.399,00",
        "discountPercentage": 35,
        "useCases": {
            "perfectFor": [
                "Donos de cães e gatos que soltam pelos diariamente pela casa",
                "Limpar embaixo de camas, sofás e armários onde a vassoura comum não alcança",
                "Passar pano úmido automático com reservatório de água embutido",
                "Sensores antiqueda e anticolisão para não bater nos móveis nem cair da escada"
            ],
            "goodFor": [
                "Pisos frios, porcelanato, laminados e carpetes baixos"
            ],
            "notRecommendedFor": [
                "Substituir faxina pesada pós-obra ou tapetes felpudos muito grossos"
            ]
        },
        "specsSummary": [
            {"label": "Funções", "value": "3 em 1: Varre, aspira e passa pano úmido"},
            {"label": "Filtro", "value": "HEPA lavável que retém ácaros e alérgenos"},
            {"label": "Bateria", "value": "Até 100 minutos com retorno automático à base"},
            {"label": "Controle", "value": "Controle remoto e sensores infravermelhos"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("robo aspirador wap robot passa pano hepa"),
            "mercadoLivre": make_ml("robo-aspirador-wap"),
            "shopee": make_shp("robo aspirador wap")
        },
        "verifiedDeal": True
    },
    {
        "id": "panela-pressao-eletrica-electrolux-5l",
        "name": "Panela de Pressão Elétrica Digital Electrolux 5 Litros com 10 Dispositivos de Segurança",
        "tagline": "Feijão e carnes desfiadas em 20 minutos com silêncio total e zero medo de explodir",
        "category": "casa-cozinha",
        "categoryLabel": "Casa & Cozinha",
        "badge": "Mais Segura do Mercado",
        "imageUrl": "/products/panela-pressao-eletrica-electrolux-5l.jpg",
        "estimatedPrice": "R$ 389,00",
        "originalPrice": "R$ 549,00",
        "discountPercentage": 29,
        "useCases": {
            "perfectFor": [
                "Quem tem pavor de panela de pressão convencional no fogão a gás (10 travas de segurança)",
                "Cozinhar feijão, costela e sopas rapidamente com timer digital programável",
                "Programar a comida de manhã para ficar pronta e aquecida na hora de voltar do trabalho",
                "Silenciosa: não faz aquele chiado alto nem espalha vapor gorduroso pela cozinha"
            ],
            "goodFor": [
                "Preparar arroz soltinho, legumes no vapor e pudim"
            ],
            "notRecommendedFor": [
                "Cozinhas sem nenhuma tomada livre de 10A/20A na bancada"
            ]
        },
        "specsSummary": [
            {"label": "Capacidade", "value": "5 Litros (refeições para até 6 pessoas)"},
            {"label": "Segurança", "value": "10 travas inteligentes com alívio seguro de pressão"},
            {"label": "Painel", "value": "Digital com 9 receitas pré-programadas"},
            {"label": "Recipiente", "value": "Antiaderente removível fácil de lavar"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("panela de pressao eletrica electrolux 5l digital"),
            "mercadoLivre": make_ml("panela-pressao-eletrica-electrolux"),
            "shopee": make_shp("panela pressao eletrica electrolux")
        },
        "verifiedDeal": True
    },
    {
        "id": "cafeteira-nespresso-essenza-mini",
        "name": "Cafeteira Nespresso Essenza Mini 110V/220V com Pressão de 19 Bar",
        "tagline": "Espresso cremoso de cafeteria em 30 segundos no conforto da sua cozinha",
        "category": "casa-cozinha",
        "categoryLabel": "Casa & Cozinha",
        "badge": "Design & Sabor",
        "imageUrl": "/products/cafeteira-nespresso-essenza-mini.jpg",
        "estimatedPrice": "R$ 399,00",
        "originalPrice": "R$ 589,00",
        "discountPercentage": 32,
        "useCases": {
            "perfectFor": [
                "Amantes de café que querem bebida com crema perfeita em 25 segundos",
                "Cozinhas compactas ou cantinho do café no home office (ocupa pouquíssimo espaço)",
                "Compatibilidade com cápsulas originais e cápsulas de terceiros vendidas em supermercados",
                "Desligamento automático inteligente após 9 minutos sem uso para economizar energia"
            ],
            "goodFor": [
                "Doses de Espresso (40ml) e Lungo (110ml) com um simples toque"
            ],
            "notRecommendedFor": [
                "Grandes famílias que bebem garrafas inteiras de café coado de 1 litro pela manhã"
            ]
        },
        "specsSummary": [
            {"label": "Pressão", "value": "Bomba de 19 Bar de alta extração"},
            {"label": "Aquecimento", "value": "Pronta para uso em apenas 25 segundos"},
            {"label": "Reservatório", "value": "600ml removível"},
            {"label": "Dimensões", "value": "Ultracompacta (8,4 cm de largura)"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("cafeteira nespresso essenza mini 19 bar"),
            "mercadoLivre": make_ml("nespresso-essenza-mini"),
            "shopee": make_shp("nespresso essenza mini")
        },
        "verifiedDeal": True
    },
    {
        "id": "purificador-de-agua-consul-cpc31",
        "name": "Purificador de Água Consul Facilite com Filtro Classe A Antibactérias",
        "tagline": "Água pura e sem gosto de cloro sem precisar carregar galões pesados de 20 litros",
        "category": "casa-cozinha",
        "categoryLabel": "Casa & Cozinha",
        "badge": "Saúde Familiar",
        "imageUrl": "/products/purificador-de-agua-consul-cpc31.jpg",
        "estimatedPrice": "R$ 289,00",
        "originalPrice": "R$ 419,00",
        "discountPercentage": 31,
        "useCases": {
            "perfectFor": [
                "Eliminar gosto de cloro, ferrugem e bactérias da água da torneira",
                "Máxima retenção de impurezas (Filtragem Classe A certificada pelo Inmetro)",
                "Instalação descomplicada: não gasta energia elétrica (funciona mesmo quando falta luz)",
                "Aviso visual inteligente de quando chegou a hora de trocar o refil do filtro"
            ],
            "goodFor": [
                "Pequenos apartamentos e cozinhas com instalação na parede ou sobre a bancada"
            ],
            "notRecommendedFor": [
                "Quem exige água gelada direto na torneira (este modelo fornece água natural purificada; para gelada opte pelo modelo refrigerado CPB36)"
            ]
        },
        "specsSummary": [
            {"label": "Filtragem", "value": "Classe A com proteção microbiológica"},
            {"label": "Energia", "value": "Zero consumo de luz (hidráulico)"},
            {"label": "Troca de Refil", "value": "Fácil com giro de 1 clique a cada 9 meses"},
            {"label": "Vazão", "value": "1,5 litros por minuto contínuo"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("purificador de agua consul classe a cpc31"),
            "mercadoLivre": make_ml("purificador-consul-cpc31"),
            "shopee": make_shp("purificador consul")
        },
        "verifiedDeal": True
    },

    # ==========================================
    # 5. MÃES, BEBÊS & PRIMEIRA INFÂNCIA
    # ==========================================
    {
        "id": "baba-eletronica-takdir-ou-motorola",
        "name": "Babá Eletrônica com Câmera Visão Noturna e Áudio Bidirecional",
        "tagline": "Paz de espírito total para os pais: monitore o sono do bebê com tela sem depender do Wi-Fi cair",
        "category": "maes-bebes",
        "categoryLabel": "Mães & Bebês",
        "badge": "Indispensável para Maternidade",
        "imageUrl": "/products/baba-eletronica-takdir-ou-motorola.jpg",
        "estimatedPrice": "R$ 289,00",
        "originalPrice": "R$ 420,00",
        "discountPercentage": 31,
        "useCases": {
            "perfectFor": [
                "Mães e pais monitorarem o berço de qualquer cômodo da casa em tempo real",
                "Noite inteira com visão noturna infravermelha automática",
                "Falar com o bebê pelo microfone (áudio bidirecional) e sensor de temperatura do quarto",
                "Famílias que não querem depender de Wi-Fi ou apps de celular que travam"
            ],
            "goodFor": [
                "Tocar canções de ninar embutidas para acalmar o bebê"
            ],
            "notRecommendedFor": [
                "Acessar a câmera quando estiver na rua / no trabalho (o monitor funciona por frequência direta de 2.4GHz até 200m dentro de casa)"
            ]
        },
        "specsSummary": [
            {"label": "Tela", "value": "LCD 3.2 polegadas colorida"},
            {"label": "Alcance", "value": "Até 260m em área aberta / 50m com paredes"},
            {"label": "Visão Noturna", "value": "Infravermelho até 5 metros"},
            {"label": "Bateria Monitor", "value": "Autonomia de até 24h no modo VOX econômico"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("baba eletronica com camera visao noturna"),
            "mercadoLivre": make_ml("baba-eletronica-com-camera"),
            "shopee": make_shp("baba eletronica")
        },
        "verifiedDeal": True
    },
    {
        "id": "carrinho-de-bebe-compacto-fechamento-automatico",
        "name": "Carrinho de Bebê Compacto com Fechamento Rápido tipo Pocket",
        "tagline": "Dobre o carrinho com apenas 1 mão e guarde no porta-malas pequeno ou bagageiro do avião",
        "category": "maes-bebes",
        "categoryLabel": "Mães & Bebês",
        "badge": "Praticidade Total",
        "imageUrl": "/products/carrinho-de-bebe-compacto-fechamento-automatico.jpg",
        "estimatedPrice": "R$ 799,00",
        "originalPrice": "R$ 1.199,00",
        "discountPercentage": 33,
        "useCases": {
            "perfectFor": [
                "Mães e pais que saem sozinhos com o bebê e precisam fechar o carrinho com 1 mão só",
                "Porta-malas pequenos de carros hatch e viagens de avião (entra como mala de mão)",
                "Caminhadas em calçadas irregulares e shopping com rodinhas com suspensão",
                "Assento reclinável até a posição berço para sonecas confortáveis"
            ],
            "goodFor": [
                "Crianças desde recém-nascidas até 15kg (cerca de 3 anos de idade)"
            ],
            "notRecommendedFor": [
                "Corridas esportivas de alta velocidade em terrenos de terra bruta"
            ]
        },
        "specsSummary": [
            {"label": "Fechamento", "value": "Automático com 1 botão na alça"},
            {"label": "Peso", "value": "Ultraleve (menos de 6,5 kg)"},
            {"label": "Cinto", "value": "5 pontos com almofadas acolchoadas"},
            {"label": "Capota", "value": "Retrátil com proteção solar UV50+"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("carrinho de bebe compacto fechamento automatico aviao"),
            "mercadoLivre": make_ml("carrinho-de-bebe-compacto"),
            "shopee": make_shp("carrinho bebe compacto")
        },
        "verifiedDeal": True
    },
    {
        "id": "cadeirinha-auto-isofix-0-a-36kg",
        "name": "Cadeirinha para Auto Isofix Rotativa 360 Graus 0 a 36kg Reclinável",
        "tagline": "A única cadeirinha que você vai comprar: acompanha seu filho do nascimento aos 10 anos",
        "category": "maes-bebes",
        "categoryLabel": "Mães & Bebês",
        "badge": "Máxima Proteção no Trânsito",
        "imageUrl": "/products/cadeirinha-auto-isofix-0-a-36kg.jpg",
        "estimatedPrice": "R$ 899,00",
        "originalPrice": "R$ 1.349,00",
        "discountPercentage": 33,
        "useCases": {
            "perfectFor": [
                "Colocar e tirar o bebê do carro sem forçar as costas (gira 360° virando para a porta)",
                "Instalação mais segura do mundo com ganchos Isofix + Top Tether",
                "Economia inteligente: atende todos os grupos (0+, 1, 2 e 3) do nascimento até 36 kg",
                "Reclina em múltiplas posições para a cabeça do bebê não cair para frente quando dormir"
            ],
            "goodFor": [
                "Carros modernos equipados com pontos de fixação Isofix no banco traseiro"
            ],
            "notRecommendedFor": [
                "Carros muito antigos que não possuem nenhum ponto de ancoragem Isofix"
            ]
        },
        "specsSummary": [
            {"label": "Capacidade", "value": "0 a 36 kg (Grupo 0+, 1, 2, 3)"},
            {"label": "Rotação", "value": "360 graus para facilitar embarque"},
            {"label": "Fixação", "value": "Isofix rígido + cinto de 5 pontos"},
            {"label": "Proteção", "value": "Proteção reforçada contra impactos laterais"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("cadeirinha auto isofix rotativa 360 0 a 36kg"),
            "mercadoLivre": make_ml("cadeirinha-auto-isofix-360"),
            "shopee": make_shp("cadeirinha isofix 360")
        },
        "verifiedDeal": True
    },
    {
        "id": "esterilizador-mamadeiras-philips-avent",
        "name": "Esterilizador a Vapor de Mamadeiras e Chupetas para Micro-ondas Philips Avent",
        "tagline": "Esterilize 4 mamadeiras e chupetas em apenas 2 minutos eliminando 99,9% dos germes",
        "category": "maes-bebes",
        "categoryLabel": "Mães & Bebês",
        "badge": "Higiene Garantida",
        "imageUrl": "/products/esterilizador-mamadeiras-philips-avent.jpg",
        "estimatedPrice": "R$ 129,00",
        "originalPrice": "R$ 189,00",
        "discountPercentage": 31,
        "useCases": {
            "perfectFor": [
                "Esterilizar mamadeiras, chupetas, bicos e bombas tira-leite em apenas 2 minutos",
                "Elimina 99,9% das bactérias e germes sem usar nenhum produto químico",
                "Mantém os itens estéreis por até 24 horas se a tampa permanecer fechada",
                "Cabe na grande maioria dos micro-ondas domésticos padrão"
            ],
            "goodFor": [
                "Levar em viagens e passeios de fim de semana na casa dos avós"
            ],
            "notRecommendedFor": [
                "Quem não possui micro-ondas em casa (neste caso opte pelo esterilizador elétrico de tomada)"
            ]
        },
        "specsSummary": [
            {"label": "Tempo", "value": "Esterilização completa em 2 minutos"},
            {"label": "Capacidade", "value": "Comporta até 4 mamadeiras Philips Avent simultâneas"},
            {"label": "Segurança", "value": "Fechamento com travas laterais e BPA Free"},
            {"label": "Compatibilidade", "value": "Mamadeiras de bocal largo e padrão"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("esterilizador mamadeira microondas philips avent"),
            "mercadoLivre": make_ml("esterilizador-philips-avent"),
            "shopee": make_shp("esterilizador avent")
        },
        "verifiedDeal": True
    },
    {
        "id": "aspirador-nasal-eletrico-infantil",
        "name": "Aspirador Nasal Elétrico Infantil com Sucção Suave, Luz e Música",
        "tagline": "Alívio imediato do nariz entupido do bebê para ele respirar e mamar sem chorar",
        "category": "maes-bebes",
        "categoryLabel": "Mães & Bebês",
        "badge": "Alívio Imediato",
        "imageUrl": "/products/aspirador-nasal-eletrico-infantil.jpg",
        "estimatedPrice": "R$ 89,00",
        "originalPrice": "R$ 149,00",
        "discountPercentage": 40,
        "useCases": {
            "perfectFor": [
                "Desentupir o nariz do bebê com secreção e catarro em noites de gripe ou resfriado",
                "Sucção contínua e segura com bicos macios de silicone de grau alimentício",
                "Músicas relaxantes e luz colorida que acalmam a criança durante a limpeza",
                "Bateria recarregável via USB sem precisar comprar pilhas"
            ],
            "goodFor": [
                "Bebês recém-nascidos até crianças de 4 anos de idade"
            ],
            "notRecommendedFor": [
                "Substituir lavagem com soro fisiológico (o ideal é aplicar o soro antes e depois aspirar)"
            ]
        },
        "specsSummary": [
            {"label": "Níveis de Sucção", "value": "3 intensidades ajustáveis"},
            {"label": "Bicos", "value": "2 pontas de silicone laváveis (cabaça e funil)"},
            {"label": "Alimentação", "value": "Bateria recarregável via USB Type-C"},
            {"label": "Higiene", "value": "Câmara de coleta removível anti-refluxo"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("aspirador nasal eletrico infantil recarregavel"),
            "mercadoLivre": make_ml("aspirador-nasal-eletrico-bebe"),
            "shopee": make_shp("aspirador nasal eletrico")
        },
        "verifiedDeal": True
    },

    # ==========================================
    # 6. OBRA, REFORMA & FERRAMENTAS
    # ==========================================
    {
        "id": "parafusadeira-bosch-go-ou-gsb-180",
        "name": "Parafusadeira e Furadeira de Impacto Bosch GSB 180-LI 18V",
        "tagline": "Ferramenta profissional durável para furar alvenaria, madeira e montar móveis sem esforço",
        "category": "obra-ferramentas",
        "categoryLabel": "Obra & Ferramentas",
        "badge": "Escolha dos Profissionais",
        "imageUrl": "/products/parafusadeira-bosch-go-ou-gsb-180.jpg",
        "estimatedPrice": "R$ 569,00",
        "originalPrice": "R$ 799,00",
        "discountPercentage": 28,
        "useCases": {
            "perfectFor": [
                "Instalar prateleiras, suportes de TV e quadros em parede de alvenaria e concreto leve",
                "Montagem rápida de móveis e marcenaria doméstica ou profissional",
                "Quem quer uma ferramenta sem fio que dura 10+ anos na caixa de ferramentas"
            ],
            "goodFor": [
                "Perfurações em metais e madeira grossa com brocas adequadas"
            ],
            "notRecommendedFor": [
                "Demolição pesada ou furar vigas de concreto armado maciço (necessita martelete rotativo SDS)",
                "Quem quer apenas apertar 1 parafuso por ano (neste caso uma de 12V simples de R$ 150 resolve)"
            ]
        },
        "specsSummary": [
            {"label": "Voltagem da Bateria", "value": "18V Íons de Lítio"},
            {"label": "Torque Máximo", "value": "54 Nm"},
            {"label": "Impacto", "value": "Função com percussão para alvenaria"},
            {"label": "Acompanha", "value": "Bateria + Carregador Bivolt + Maleta"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("parafusadeira bosch gsb 180"),
            "mercadoLivre": make_ml("parafusadeira-bosch-gsb-180"),
            "shopee": make_shp("bosch gsb 180")
        },
        "verifiedDeal": True
    },
    {
        "id": "lavadora-alta-pressao-karcher-k2-turbo",
        "name": "Lavadora de Alta Pressão Kärcher K2 Turbo 1600 PSI com Bico Turbo",
        "tagline": "Limpeza pesada de calçadas, muros, carros e telhados economizando até 80% de água",
        "category": "obra-ferramentas",
        "categoryLabel": "Obra & Ferramentas",
        "badge": "Líder em Limpeza",
        "imageUrl": "/products/lavadora-alta-pressao-karcher-k2-turbo.jpg",
        "estimatedPrice": "R$ 449,00",
        "originalPrice": "R$ 649,00",
        "discountPercentage": 30,
        "useCases": {
            "perfectFor": [
                "Arrancar limo e sujeira preta impregnada em pisos de quintal e calçadas",
                "Lavar carro, moto e bicicleta com jato leque potente sem riscar a pintura",
                "Economia real: gasta até 8 vezes menos água do que uma mangueira de jardim comum",
                "Bico turbo rotativo incluso para arrancar a sujeira mais pesada com facilidade"
            ],
            "goodFor": [
                "Limpeza de muros, grelhas de churrasqueira e fachadas"
            ],
            "notRecommendedFor": [
                "Lava-rápidos comerciais que funcionam 8 horas seguidas ininterruptas (uso residencial)"
            ]
        },
        "specsSummary": [
            {"label": "Pressão Máxima", "value": "1600 PSI"},
            {"label": "Vazão", "value": "280 litros por hora"},
            {"label": "Mangueira", "value": "3 metros com engate rápido"},
            {"label": "Acessórios", "value": "Lança de jato leque e lança turbo"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("lavadora alta pressao karcher k2 turbo"),
            "mercadoLivre": make_ml("lavadora-karcher-k2"),
            "shopee": make_shp("karcher k2 turbo")
        },
        "verifiedDeal": True
    },
    {
        "id": "trena-laser-digital-40m-bosch-ou-dextools",
        "name": "Trena a Laser Digital 40 Metros com Nível Eletrônico e Cálculo de Área",
        "tagline": "Meça cômodos inteiros em 1 segundo sem precisar de ninguém segurando a fita métrica",
        "category": "obra-ferramentas",
        "categoryLabel": "Obra & Ferramentas",
        "badge": "Precisão Milimétrica",
        "imageUrl": "/products/trena-laser-digital-40m-bosch-ou-dextools.jpg",
        "estimatedPrice": "R$ 139,00",
        "originalPrice": "R$ 219,00",
        "discountPercentage": 36,
        "useCases": {
            "perfectFor": [
                "Arquitetos, pedreiros, corretores de imóveis e instaladores de móveis planejados",
                "Calcular área quadrada (m²) de pisos e paredes para comprar piso ou tinta sem errar",
                "Cálculo automático de volume (m³) e Teorema de Pitágoras para medir alturas inacessíveis",
                "Cabe no bolso da calça ou da camisa (pesa menos de 80 gramas)"
            ],
            "goodFor": [
                "Medir terrenos internos e externos de até 40 metros de distância"
            ],
            "notRecommendedFor": [
                "Uso sob sol forte de meio-dia a mais de 30m em campo aberto (o ponto laser fica difícil de enxergar)"
            ]
        },
        "specsSummary": [
            {"label": "Alcance", "value": "0,05m até 40 metros"},
            {"label": "Precisão", "value": "± 2 milímetros"},
            {"label": "Funções", "value": "Distância contínua, Área, Volume, Pitágoras e Memória"},
            {"label": "Tela", "value": "Display retroiluminado com indicador de nível"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("trena laser 40 metros digital precisao"),
            "mercadoLivre": make_ml("trena-laser-40m"),
            "shopee": make_shp("trena laser 40m")
        },
        "verifiedDeal": True
    },
    {
        "id": "maleta-ferramentas-completa-110-pecas",
        "name": "Maleta de Ferramentas Completa 110 Peças em Aço Cromo-Vanádio com Catraca",
        "tagline": "Tudo o que você precisa para consertar qualquer coisa em casa ou no carro em uma só maleta",
        "category": "obra-ferramentas",
        "categoryLabel": "Obra & Ferramentas",
        "badge": "Kit Completo para a Vida",
        "imageUrl": "/products/maleta-ferramentas-completa-110-pecas.jpg",
        "estimatedPrice": "R$ 389,00",
        "originalPrice": "R$ 560,00",
        "discountPercentage": 30,
        "useCases": {
            "perfectFor": [
                "Manutenção automotiva, conserto de encanamentos, troca de chuveiro e montagem",
                "Chaves de catraca reversível com soquetes milimétricos que agilizam qualquer aperto",
                "Peças forjadas em aço Cromo-Vanádio (Cr-V) de alta resistência que não espanam",
                "Maleta rígida organizadora onde cada ferramenta tem seu encaixe moldado"
            ],
            "goodFor": [
                "Presente ideal para quem comprou ou alugou casa própria recente"
            ],
            "notRecommendedFor": [
                "Mecânica pesada de caminhões e tratores industriais"
            ]
        },
        "specsSummary": [
            {"label": "Quantidade", "value": "110 peças organizadas em maleta termoplástica"},
            {"label": "Material", "value": "Aço Cromo-Vanádio com acabamento fosfatizado"},
            {"label": "Catracas", "value": "Catracas 1/2 e 1/4 com botão de desengate rápido"},
            {"label": "Itens", "value": "Alicates, chaves combinadas, soquetes, bits e extensões"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("jogo ferramentas 110 pecas cromo vanadio maleta"),
            "mercadoLivre": make_ml("maleta-ferramentas-110-pecas"),
            "shopee": make_shp("maleta ferramentas 110 pecas")
        },
        "verifiedDeal": True
    },
    {
        "id": "nivel-laser-360-linhas-verdes",
        "name": "Nível a Laser Autonivelante 360 Graus com Linhas Verdes e Tripé",
        "tagline": "Alinhamento 100% perfeito de pisos, azulejos, gesso e drywall sem usar mangueira de nível",
        "category": "obra-ferramentas",
        "categoryLabel": "Obra & Ferramentas",
        "badge": "Instalação Perfeita",
        "imageUrl": "/products/nivel-laser-360-linhas-verdes.jpg",
        "estimatedPrice": "R$ 259,00",
        "originalPrice": "R$ 399,00",
        "discountPercentage": 35,
        "useCases": {
            "perfectFor": [
                "Assentamento de porcelanato e azulejos com alinhamento milimétrico nas 4 paredes",
                "Instalação de forro de gesso, sancas, drywall e papel de parede",
                "Feixe de laser verde que é até 4 vezes mais visível aos olhos do que o laser vermelho comum",
                "Autonivelamento automático com alarme sonoro se o aparelho estiver inclinado"
            ],
            "goodFor": [
                "Pendurar quadros e prateleiras perfeitamente nivelados"
            ],
            "notRecommendedFor": [
                "Topografia de grandes rodovias ou medições quilométricas"
            ]
        },
        "specsSummary": [
            {"label": "Laser", "value": "Verde 3D 12/16 Linhas 360 graus"},
            {"label": "Nivelamento", "value": "Autonivelante ± 3° em menos de 4 segundos"},
            {"label": "Alimentação", "value": "Baterias de Lítio recarregáveis inclusas"},
            {"label": "Acessórios", "value": "Base magnética, mini tripé, suporte e maleta"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("nivel a laser 360 linhas verdes autonivelante"),
            "mercadoLivre": make_ml("nivel-laser-360-verde"),
            "shopee": make_shp("nivel laser 360 verde")
        },
        "verifiedDeal": True
    },

    # ==========================================
    # 7. CARROS, GARAGEM & CUIDADOS AUTOMOTIVOS
    # ==========================================
    {
        "id": "aspirador-automotivo-portatil-sem-fio",
        "name": "Aspirador Automotivo Portátil Sem Fio 120W de Alta Sucção",
        "tagline": "Carro limpo sem pagar lava-rápido: suga farelos, terra e pelos de animais nos cantos mais difíceis",
        "category": "carros",
        "categoryLabel": "Carros & Garagem",
        "badge": "Viral no TikTok",
        "imageUrl": "/products/aspirador-automotivo-portatil-sem-fio.jpg",
        "estimatedPrice": "R$ 89,00",
        "originalPrice": "R$ 149,00",
        "discountPercentage": 40,
        "useCases": {
            "perfectFor": [
                "Limpar bancos, porta-copos, painel e assoalho rapidamente sem fios atrapalhando",
                "Motoristas de aplicativo (Uber/99) manterem o veículo impecável entre uma corrida e outra",
                "Guardar no porta-luvas ou porta-malas por ser compacto e recarregar via USB"
            ],
            "goodFor": [
                "Aspirar teclado de computador e cantos de sofá em casa"
            ],
            "notRecommendedFor": [
                "Aspirar lama densa ou água profunda (uso indicado para sujeira seca e farelos)",
                "Faxina pesada da casa inteira (capacidade de reservatório de 0.5L focada em automóveis)"
            ]
        },
        "specsSummary": [
            {"label": "Potência", "value": "120W com 9000Pa de sucção"},
            {"label": "Alimentação", "value": "Bateria recarregável via USB Type-C"},
            {"label": "Filtro", "value": "HEPA lavável e reutilizável"},
            {"label": "Acessórios", "value": "Bocal longo + escova para estofados"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("aspirador automotivo portatil sem fio"),
            "mercadoLivre": make_ml("aspirador-automotivo-sem-fio"),
            "shopee": make_shp("aspirador automotivo")
        },
        "verifiedDeal": True
    },
    {
        "id": "compressor-de-ar-digital-portatil-pneu",
        "name": "Compressor de Ar Digital Portátil Recarregável para Pneus e Calibragem",
        "tagline": "Nunca mais passe perrengue com pneu murcho na estrada nem enfrente fila de posto de gasolina",
        "category": "carros",
        "categoryLabel": "Carros & Garagem",
        "badge": "Salva-Vidas na Estrada",
        "imageUrl": "/products/compressor-de-ar-digital-portatil-pneu.jpg",
        "estimatedPrice": "R$ 149,00",
        "originalPrice": "R$ 239,00",
        "discountPercentage": 37,
        "useCases": {
            "perfectFor": [
                "Calibrar os 4 pneus do carro em casa sem precisar ir ao posto",
                "Encher pneu murcho de emergência no acostamento da estrada sem precisar trocar o estepe na chuva",
                "Display digital com desligamento automático na pressão exata configurada (PSI ou BAR)",
                "Encher pneus de moto, bicicleta, patinete elétrico e bolas de futebol/basquete"
            ],
            "goodFor": [
                "Lanterna LED embutida para emergências noturnas e powerbank para carregar o celular"
            ],
            "notRecommendedFor": [
                "Pneus gigantescos de caminhões de carga pesada ou tratores agrícolas"
            ]
        },
        "specsSummary": [
            {"label": "Pressão Máxima", "value": "Até 150 PSI com parada automática inteligente"},
            {"label": "Bateria", "value": "Recarregável de 6000mAh (enche até 4 pneus de carro)"},
            {"label": "Tela", "value": "Display digital LED de alta visibilidade"},
            {"label": "Acessórios", "value": "Bicos para pneu de carro, bico fino de bike e agulha de bola"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("compressor ar portatil digital recarregavel pneu carro"),
            "mercadoLivre": make_ml("compressor-ar-portatil-carro"),
            "shopee": make_shp("compressor de ar portatil")
        },
        "verifiedDeal": True
    },
    {
        "id": "camera-veicular-dashcam-frontal-traseira",
        "name": "Câmera Veicular Dashcam Frontal e Traseira Full HD com Visão Noturna e Sensor G",
        "tagline": "Sua testemunha ocular em caso de batidas, golpes de trânsito ou multas indevidas",
        "category": "carros",
        "categoryLabel": "Carros & Garagem",
        "badge": "Segurança Jurídica",
        "imageUrl": "/products/camera-veicular-dashcam-frontal-traseira.jpg",
        "estimatedPrice": "R$ 179,00",
        "originalPrice": "R$ 279,00",
        "discountPercentage": 35,
        "useCases": {
            "perfectFor": [
                "Gravação contínua em Full HD de qualquer acidente ou fechada para comprovar ao seguro",
                "Sensor G de impacto que trava o vídeo automaticamente para não ser apagado em colisão",
                "Monitoramento de estacionamento 24h: começa a gravar se alguém bater no seu carro parado",
                "Câmera traseira auxiliar que ajuda nas manobras de ré"
            ],
            "goodFor": [
                "Motoristas de aplicativo, entregadores e quem viaja muito por rodovias"
            ],
            "notRecommendedFor": [
                "Gravação de vlogs de cinema em 4K (o objetivo é segurança jurídica com nitidez de placas)"
            ]
        },
        "specsSummary": [
            {"label": "Resolução", "value": "Dual Cam: Frontal 1080p + Traseira 720p"},
            {"label": "Ângulo", "value": "Lente grande angular de 170 graus (cobre 3 pistas)"},
            {"label": "Gravação", "value": "Em loop contínuo (sobrescreve arquivos antigos quando enche)"},
            {"label": "Sensor", "value": "Sensor G com bloqueio de emergência"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("camera veicular dashcam frontal traseira visao noturna"),
            "mercadoLivre": make_ml("camera-veicular-dashcam"),
            "shopee": make_shp("camera veicular dashcam")
        },
        "verifiedDeal": True
    },
    {
        "id": "suporte-celular-veicular-magsafe-inducao",
        "name": "Suporte de Celular Veicular Magnético com Carregamento Sem Fio por Indução 15W",
        "tagline": "Coloque o celular com apenas 1 clique magnético na saída de ar e carregue sem cabos soltos",
        "category": "carros",
        "categoryLabel": "Carros & Garagem",
        "badge": "Conforto no Painel",
        "imageUrl": "/products/suporte-celular-veicular-magsafe-inducao.jpg",
        "estimatedPrice": "R$ 99,00",
        "originalPrice": "R$ 169,00",
        "discountPercentage": 41,
        "useCases": {
            "perfectFor": [
                "Fixar o celular firme mesmo passando em lombadas, buracos e ruas de paralelepípedo",
                "Carregar a bateria por indução (15W rápido) enquanto usa Waze e Spotify no trânsito",
                "Encaixe magnético com ímãs N52 ultrafortes (compatível com MagSafe de iPhone e anéis para Android)",
                "Giro de 360 graus para usar o GPS na horizontal ou vertical com uma mão só"
            ],
            "goodFor": [
                "Instalação na grade de ventilação do ar-condicionado de praticamente qualquer veículo"
            ],
            "notRecommendedFor": [
                "Celulares muito antigos que não possuem tecnologia de carregamento por indução Qi"
            ]
        },
        "specsSummary": [
            {"label": "Carregamento", "value": "Wireless Fast Charge 15W/10W/7.5W"},
            {"label": "Fixação", "value": "Gancho metálico com trava de segurança para grelha de ar"},
            {"label": "Ímãs", "value": "Anel de 16 ímãs de neodímio N52"},
            {"label": "Proteção", "value": "Controle inteligente de temperatura que não superaquece"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("suporte celular veicular magsafe carregador inducao 15w"),
            "mercadoLivre": make_ml("suporte-veicular-magsafe-inducao"),
            "shopee": make_shp("suporte veicular inducao")
        },
        "verifiedDeal": True
    },
    {
        "id": "kit-lavagem-cera-carnauba-vonixx",
        "name": "Kit Estética Automotiva Vonixx Shampoo V-Floc + Cera Blend Carnaúba e Toalha Microfibra",
        "tagline": "Brilho espelhado de concessionária e proteção hidro-repelente contra chuva ácida e poeira",
        "category": "carros",
        "categoryLabel": "Carros & Garagem",
        "badge": "Brilho Espelhado",
        "imageUrl": "/products/kit-lavagem-cera-carnauba-vonixx.jpg",
        "estimatedPrice": "R$ 129,00",
        "originalPrice": "R$ 189,00",
        "discountPercentage": 31,
        "useCases": {
            "perfectFor": [
                "Lavar o carro em casa sem criar micro-riscos na pintura (shampoo neutro V-Floc de alto rendimento)",
                "Cera Blend com Carnaúba brasileira e sílica (SiO2) que dura até 4 meses na lataria",
                "Efeito hidro-repelente extremo: a água e a sujeira escorregam sem grudar na pintura",
                "Toalha de microfibra de alta gramatura para secagem suave sem fiapos"
            ],
            "goodFor": [
                "Todas as cores de veículos (brancos, pratas, pretos e cores escuras metálicas)"
            ],
            "notRecommendedFor": [
                "Pinturas foscas ou carros envelopados em vinil sem verniz"
            ]
        },
        "specsSummary": [
            {"label": "Shampoo", "value": "Vonixx V-Floc 500ml com pH neutro e alta lubrificação"},
            {"label": "Cera", "value": "Vonixx Blend Ceramic Paste / Spray com Carnaúba + Sílica"},
            {"label": "Toalha", "value": "Microfibra especial de secagem ultra macia"},
            {"label": "Rendimento", "value": "Rende mais de 15 lavagens completas"}
        ],
        "affiliateLinks": {
            "amazon": make_amz("kit vonixx v-floc cera blend microfibra automotivo"),
            "mercadoLivre": make_ml("kit-vonixx-cera-blend"),
            "shopee": make_shp("kit vonixx automotivo")
        },
        "verifiedDeal": True
    }
]

def main():
    with open("src/data/products.json", "w", encoding="utf-8") as f:
        json.dump(PRODUCTS, f, indent=2, ensure_ascii=False)
    print(f"🎉 Sucesso! Catálogo atualizado com {len(PRODUCTS)} produtos campeões da Black Friday.")

if __name__ == "__main__":
    main()
