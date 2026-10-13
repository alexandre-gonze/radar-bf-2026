'use client';

import React, { useState, useMemo } from 'react';
import productsData from '@/data/products.json';
import { Product, CategoryId } from '@/types/product';
import { Navbar } from '@/components/Navbar';
import { CategoryFilter } from '@/components/CategoryFilter';
import { ProductCard } from '@/components/ProductCard';
import { VipBanner } from '@/components/VipBanner';
import { 
  Search, 
  Flame, 
  HelpCircle, 
  TrendingUp, 
  CheckCircle2, 
  X, 
  SlidersHorizontal 
} from 'lucide-react';

export default function Home() {
  const [selectedCategory, setSelectedCategory] = useState<CategoryId>('todos');
  const [searchQuery, setSearchQuery] = useState('');

  const products: Product[] = productsData as unknown as Product[];

  // Counts per category
  const categoryCounts = useMemo(() => {
    const counts: Record<CategoryId, number> = {
      'todos': products.length,
      'estudantes': 0,
      'ti-trabalho': 0,
      'gamers': 0,
      'casa-cozinha': 0,
      'maes-bebes': 0,
      'obra-ferramentas': 0,
      'carros': 0,
    };

    products.forEach((p) => {
      if (counts[p.category] !== undefined) {
        counts[p.category]++;
      }
    });

    return counts;
  }, [products]);

  // Filtered products by category and query
  const filteredProducts = useMemo(() => {
    return products.filter((p) => {
      const matchesCategory = selectedCategory === 'todos' || p.category === selectedCategory;
      
      const query = searchQuery.toLowerCase().trim();
      if (!query) return matchesCategory;

      const matchesSearch = 
        p.name.toLowerCase().includes(query) ||
        p.tagline.toLowerCase().includes(query) ||
        p.categoryLabel.toLowerCase().includes(query) ||
        p.useCases.perfectFor.some(item => item.toLowerCase().includes(query)) ||
        p.useCases.notRecommendedFor.some(item => item.toLowerCase().includes(query));

      return matchesCategory && matchesSearch;
    });
  }, [products, selectedCategory, searchQuery]);

  return (
    <div className="min-h-screen flex flex-col bg-gray-950">
      <Navbar />

      {/* Hero Section */}
      <section className="relative overflow-hidden pt-10 pb-8 sm:pt-16 sm:pb-12 border-b border-gray-900 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-red-950/40 via-gray-950 to-gray-950">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center space-y-4">
          <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-red-950/60 border border-red-800/60 text-red-400 text-xs font-semibold">
            <Flame className="w-4 h-4 animate-pulse text-red-500" />
            <span>Guia Oficial de Compras Black Friday 2026</span>
          </div>

          <h1 className="text-3xl sm:text-5xl lg:text-6xl font-black text-white tracking-tight max-w-4xl mx-auto leading-tight">
            Não caia na cilada da <span className="text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-amber-400 to-red-500">"metade do dobro"</span>.
          </h1>

          <p className="text-sm sm:text-lg text-gray-400 max-w-2xl mx-auto leading-relaxed">
            Nós analisamos os produtos mais buscados e dizemos a verdade: <strong className="text-gray-200">para o que ele realmente serve</strong> e <strong className="text-rose-400">quando NÃO vale a pena gastar seu dinheiro</strong>.
          </p>

          {/* Search Box */}
          <div className="pt-4 max-w-xl mx-auto">
            <div className="relative">
              <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-gray-500">
                <Search className="w-5 h-5" />
              </div>
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Busque por produto, finalidade (ex: notebook, office, render, airfryer)..."
                className="w-full pl-11 pr-10 py-3.5 rounded-2xl bg-gray-900/90 border border-gray-800 focus:border-red-500 focus:ring-2 focus:ring-red-500/30 text-sm text-white placeholder-gray-500 shadow-inner transition-all outline-none"
              />
              {searchQuery && (
                <button
                  onClick={() => setSearchQuery('')}
                  className="absolute inset-y-0 right-0 pr-3.5 flex items-center text-gray-400 hover:text-white"
                >
                  <X className="w-4 h-4" />
                </button>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* Main Catalog View */}
      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">
        {/* Category Selector */}
        <div className="space-y-3">
          <div className="flex items-center justify-between text-xs text-gray-400">
            <span className="font-semibold uppercase tracking-wider flex items-center space-x-1.5">
              <SlidersHorizontal className="w-3.5 h-3.5" />
              <span>Filtrar por Perfil / Necessidade:</span>
            </span>
            <span>{filteredProducts.length} itens encontrados</span>
          </div>
          <CategoryFilter
            selectedCategory={selectedCategory}
            onSelectCategory={setSelectedCategory}
            counts={categoryCounts}
          />
        </div>

        {/* Product Cards Grid */}
        {filteredProducts.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {filteredProducts.map((product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        ) : (
          <div className="p-12 text-center rounded-2xl bg-gray-900/50 border border-gray-800 space-y-3">
            <HelpCircle className="w-12 h-12 text-gray-500 mx-auto" />
            <h3 className="text-lg font-bold text-white">Nenhum produto encontrado</h3>
            <p className="text-sm text-gray-400 max-w-md mx-auto">
              Não encontramos resultados para "{searchQuery}". Tente outro termo ou limpe os filtros.
            </p>
            <button
              onClick={() => {
                setSelectedCategory('todos');
                setSearchQuery('');
              }}
              className="px-4 py-2 text-xs font-semibold rounded-xl bg-red-600 hover:bg-red-500 text-white transition-colors"
            >
              Ver todos os produtos
            </button>
          </div>
        )}

        {/* Conversion Banner for Alerts */}
        <VipBanner />

        {/* Methodology / Trust Section */}
        <section className="my-12 p-8 rounded-2xl bg-gray-900/40 border border-gray-800 space-y-4">
          <div className="flex items-center space-x-2 text-red-400 text-xs font-bold uppercase tracking-wider">
            <TrendingUp className="w-4 h-4" />
            <span>Nossa Metodologia Sem Enrolação</span>
          </div>
          <h3 className="text-xl font-bold text-white">Como escolhemos as recomendações?</h3>
          <p className="text-sm text-gray-400 leading-relaxed">
            Diferente de sites tradicionais que apenas copiam a ficha técnica do fabricante com jargões confusos, nós filtramos as centenas de comentários reais de compradores, testes práticos de estresse e histórico de preços nos últimos 6 meses.
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 pt-2 text-xs text-gray-300">
            <div className="p-3 rounded-xl bg-gray-950 border border-gray-800/60">
              <span className="font-bold text-white block mb-1">1. Histórico Real de Preço</span>
              Identificamos quando um desconto é genuíno e descartamos preços inflacionados na véspera.
            </div>
            <div className="p-3 rounded-xl bg-gray-950 border border-gray-800/60">
              <span className="font-bold text-white block mb-1">2. Transparência de Limites</span>
              Fazemos questão de dizer onde o produto NÃO atende, para você não ter dor de cabeça de devolução.
            </div>
            <div className="p-3 rounded-xl bg-gray-950 border border-gray-800/60">
              <span className="font-bold text-white block mb-1">3. Lojas Oficiais & Full</span>
              Priorizamos estoque com entrega rápida, garantia nacional e proteção total ao consumidor.
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-gray-900 bg-gray-950 py-8 text-xs text-gray-500">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row items-center justify-between gap-4">
          <div>
            <p className="font-semibold text-gray-400">Radar BF 2026 — Guia Independente de Compras</p>
            <p className="mt-1">
              Participamos dos programas de afiliados da Amazon, Mercado Livre e Shopee. As comissões não alteram o preço final para você.
            </p>
          </div>
          <div className="flex items-center space-x-4 text-gray-400">
            <a href="#radar-vip" className="hover:text-white transition-colors">Alertas VIP</a>
            <span>•</span>
            <a href="#" className="hover:text-white transition-colors">Termos</a>
            <span>•</span>
            <a href="#" className="hover:text-white transition-colors">Privacidade</a>
          </div>
        </div>
      </footer>
    </div>
  );
}
