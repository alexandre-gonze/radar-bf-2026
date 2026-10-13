# 🚀 Radar BF 2026 — Hub de Recomendações & Automação de Afiliados

Plataforma rápida e moderna construída com **Next.js (App Router)**, **Tailwind CSS**, **TypeScript** e **Python**. Projetada especificamente para conversão em massa na Black Friday com custo zero ($0).

---

## 🌟 O Diferencial
Em vez de blogs genéricos ou fichas técnicas frias, cada produto possui uma **Matriz de Casos de Uso Reais**:
- 🟢 **Perfeito para:** quem tem o perfil ideal de uso.
- 🟡 **Quebra o galho para:** usos secundários toleráveis.
- 🔴 **NÃO compre se você precisa de:** evita devoluções e gera confiança imediata no comprador.

---

## 🛠️ Como rodar o projeto localmente

### 1. Iniciar o servidor de desenvolvimento:
```bash
npm run dev
```
Acesse no seu navegador: `http://localhost:3000`

### 2. Gerar build estático para produção:
```bash
npm run build
```

---

## 🤖 Automação no Antigravity / Scripts Python ($0)

### 1. Minerar as tendências e termos mais buscados por categoria:
```bash
python scripts/mine_trends.py
```
Gera a lista das principais dores e palavras-chave de busca no Brasil e salva o `trending_report.json`.

### 2. Gerar Roteiros de Vídeo (TikTok / YouTube Shorts), Pins e WhatsApp:
```bash
# Ver lista de produtos cadastrados:
python scripts/generate_product.py --list

# Gerar o kit completo de redes para um produto específico:
python scripts/generate_product.py --bundle notebook-lenovo-ideapad-ryzen-5
```
Isso gera instantaneamente:
- Roteiro de 35-45 segundos com gancho de retenção, quebra de objeção e chamada para ação.
- Título, descrição e hashtags de SEO para o Pinterest.
- Mensagem formatada com emojis e links pronta para disparar no canal do WhatsApp/Telegram.

---

## ☁️ Como colocar no ar gratuitamente (Vercel)

1. Crie um repositório no seu [GitHub](https://github.com).
2. Suba este código:
   ```bash
   git init
   git add .
   git commit -m "feat: radar bf initial release"
   git remote add origin <URL_DO_SEU_REPOSITORIO>
   git push -u origin main
   ```
3. Acesse [vercel.com](https://vercel.com), faça login com seu GitHub e clique em **"Add New Project"**.
4. Importe o repositório. O deploy é 100% automático e gratuito, fornecendo uma URL segura HTTPS (`.vercel.app`).
