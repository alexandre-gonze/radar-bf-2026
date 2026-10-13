'use client';

import React, { useState } from 'react';
import { Product } from '@/types/product';
import { 
  CheckCircle2, 
  AlertCircle, 
  XCircle, 
  ExternalLink, 
  ShieldCheck, 
  Sparkles,
  Share2,
  Check
} from 'lucide-react';

interface ProductCardProps {
  product: Product;
}

export const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  const [copied, setCopied] = useState(false);

  const handleShare = () => {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(window.location.href);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  return (
    <article className="flex flex-col bg-gray-900/90 rounded-2xl border border-gray-800 hover:border-gray-700 shadow-xl overflow-hidden transition-all duration-200 hover:-translate-y-1">
      {/* Top Banner / Badge */}
      <div className="relative h-56 bg-gray-950 overflow-hidden group">
        <img
          src={product.imageUrl}
          alt={product.name}
          className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-300"
          loading="lazy"
        />
        
        {/* Badges Overlay */}
        <div className="absolute top-3 left-3 flex flex-col gap-1.5 items-start">
          {product.badge && (
            <span className="flex items-center space-x-1 px-2.5 py-1 text-xs font-bold bg-amber-500/90 text-gray-950 rounded-lg shadow-md backdrop-blur-sm">
              <Sparkles className="w-3.5 h-3.5" />
              <span>{product.badge}</span>
            </span>
          )}
          {product.discountPercentage && (
            <span className="px-2 py-0.5 text-xs font-extrabold bg-red-600 text-white rounded-md shadow-md">
              -{product.discountPercentage}% OFF
            </span>
          )}
        </div>

        {/* Share Button */}
        <button
          onClick={handleShare}
          title="Copiar link da recomendação"
          className="absolute top-3 right-3 p-2 rounded-xl bg-gray-950/70 hover:bg-gray-900 text-gray-300 hover:text-white border border-gray-800 backdrop-blur-md transition-colors"
        >
          {copied ? <Check className="w-4 h-4 text-emerald-400" /> : <Share2 className="w-4 h-4" />}
        </button>

        {/* Verified Footer */}
        {product.verifiedDeal && (
          <div className="absolute bottom-2 left-3 flex items-center space-x-1.5 px-2 py-0.5 rounded-md bg-gray-950/80 backdrop-blur-sm text-[11px] text-emerald-400 font-medium border border-emerald-900/50">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>Curadoria Verificada</span>
          </div>
        )}
      </div>

      {/* Main Content */}
      <div className="p-5 flex-1 flex flex-col justify-between">
        <div>
          {/* Category Tag */}
          <span className="text-[11px] font-semibold uppercase tracking-wider text-red-400">
            {product.categoryLabel}
          </span>

          {/* Title & Tagline */}
          <h3 className="mt-1 font-bold text-lg text-white leading-snug line-clamp-2">
            {product.name}
          </h3>
          <p className="mt-1.5 text-xs text-gray-400 italic">
            "{product.tagline}"
          </p>

          {/* Pricing Highlight */}
          <div className="mt-4 p-3 rounded-xl bg-gray-950 border border-gray-800/80 flex items-baseline justify-between">
            <div>
              <span className="text-[11px] text-gray-400 block">Preço estimado BF</span>
              <div className="flex items-baseline space-x-2">
                <span className="text-xl font-extrabold text-white">
                  {product.estimatedPrice}
                </span>
                {product.originalPrice && (
                  <span className="text-xs text-gray-500 line-through">
                    {product.originalPrice}
                  </span>
                )}
              </div>
            </div>
            <span className="text-[10px] text-gray-500 text-right">
              Pode variar<br/>conforme estoque
            </span>
          </div>

          {/* THE CORE DIFFERENTIATOR: USE-CASE MATRIX */}
          <div className="mt-5 space-y-3">
            <h4 className="text-xs font-bold uppercase tracking-wider text-gray-300 flex items-center">
              <span>Para quem realmente serve?</span>
            </h4>

            {/* Perfect For */}
            <div className="p-3 rounded-xl bg-emerald-950/30 border border-emerald-900/40 text-xs">
              <div className="flex items-center space-x-1.5 font-bold text-emerald-400 mb-1.5">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                <span>🟢 Perfeito para:</span>
              </div>
              <ul className="space-y-1 text-gray-300 pl-5 list-disc marker:text-emerald-500">
                {product.useCases.perfectFor.map((item, idx) => (
                  <li key={idx} className="leading-relaxed">{item}</li>
                ))}
              </ul>
            </div>

            {/* Good For */}
            {product.useCases.goodFor && product.useCases.goodFor.length > 0 && (
              <div className="p-3 rounded-xl bg-amber-950/20 border border-amber-900/30 text-xs">
                <div className="flex items-center space-x-1.5 font-bold text-amber-400 mb-1.5">
                  <AlertCircle className="w-4 h-4 text-amber-400 shrink-0" />
                  <span>🟡 Quebra o galho para:</span>
                </div>
                <ul className="space-y-1 text-gray-300 pl-5 list-disc marker:text-amber-500">
                  {product.useCases.goodFor.map((item, idx) => (
                    <li key={idx} className="leading-relaxed">{item}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Not Recommended For */}
            <div className="p-3 rounded-xl bg-rose-950/30 border border-rose-900/40 text-xs">
              <div className="flex items-center space-x-1.5 font-bold text-rose-400 mb-1.5">
                <XCircle className="w-4 h-4 text-rose-400 shrink-0" />
                <span>🔴 NÃO compre se você precisa de:</span>
              </div>
              <ul className="space-y-1 text-gray-300 pl-5 list-disc marker:text-rose-500">
                {product.useCases.notRecommendedFor.map((item, idx) => (
                  <li key={idx} className="leading-relaxed">{item}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* Quick Specs Grid */}
          <div className="mt-4 grid grid-cols-2 gap-2 text-[11px] pt-3 border-t border-gray-800">
            {product.specsSummary.map((spec, idx) => (
              <div key={idx} className="bg-gray-950/60 p-2 rounded-lg border border-gray-800/60">
                <span className="text-gray-500 block text-[10px] uppercase">{spec.label}</span>
                <span className="text-gray-300 font-medium line-clamp-1">{spec.value}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Affiliate Action CTA Buttons */}
        <div className="mt-6 pt-4 border-t border-gray-800 space-y-2">
          <span className="text-[11px] font-semibold text-gray-400 block text-center">
            Onde encontrar pelo menor preço seguro:
          </span>

          <div className="flex flex-col gap-2">
            {product.affiliateLinks.amazon && (
              <a
                href={product.affiliateLinks.amazon}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-between px-4 py-2.5 rounded-xl bg-[#232F3E] hover:bg-[#2e3e52] text-amber-400 hover:text-amber-300 border border-gray-700 text-xs font-bold transition-all shadow-sm"
              >
                <span>📦 Ver Oferta na Amazon</span>
                <ExternalLink className="w-3.5 h-3.5 text-gray-400" />
              </a>
            )}

            {product.affiliateLinks.mercadoLivre && (
              <a
                href={product.affiliateLinks.mercadoLivre}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-between px-4 py-2.5 rounded-xl bg-[#ffe600] hover:bg-[#ecd600] text-[#2d3277] text-xs font-extrabold transition-all shadow-sm"
              >
                <span>⚡ Ver no Mercado Livre (Full)</span>
                <ExternalLink className="w-3.5 h-3.5 text-[#2d3277]" />
              </a>
            )}

            {product.affiliateLinks.shopee && (
              <a
                href={product.affiliateLinks.shopee}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center justify-between px-4 py-2.5 rounded-xl bg-[#ee4d2d] hover:bg-[#d44326] text-white text-xs font-bold transition-all shadow-sm"
              >
                <span>🛍️ Ver na Shopee Oficial</span>
                <ExternalLink className="w-3.5 h-3.5 text-white/80" />
              </a>
            )}
          </div>
        </div>
      </div>
    </article>
  );
};
