import React from 'react';
import { Bell, Flame, CheckCircle2, Zap } from 'lucide-react';

export const VipBanner: React.FC = () => {
  return (
    <section id="radar-vip" className="my-12 relative overflow-hidden rounded-3xl bg-gradient-to-r from-red-950/80 via-gray-900 to-red-950/80 border border-red-800/60 p-6 sm:p-10 shadow-2xl">
      <div className="absolute top-0 right-0 -mt-6 -mr-6 w-52 h-52 bg-red-600/20 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-0 left-0 -mb-6 -ml-6 w-52 h-52 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />

      <div className="relative z-10 max-w-3xl mx-auto text-center space-y-4">
        <div className="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-red-900/50 border border-red-700/60 text-red-300 text-xs font-bold tracking-wide">
          <Flame className="w-4 h-4 text-amber-400" />
          <span>CANAL DE ALERTAS RELÂMPAGO BLACK FRIDAY</span>
        </div>

        <h2 className="text-2xl sm:text-4xl font-extrabold text-white tracking-tight">
          As melhores ofertas da Black Friday <span className="text-transparent bg-clip-text bg-gradient-to-r from-red-400 to-amber-300">acabam em minutos.</span>
        </h2>

        <p className="text-gray-300 text-sm sm:text-base leading-relaxed max-w-2xl mx-auto">
          Nosso robô monitora quedas reais de preço e cupons escondidos na Amazon, Mercado Livre e Shopee. Não enviamos spam: apenas ofertas verificadas de verdade.
        </p>

        <div className="pt-2 flex flex-col sm:flex-row items-center justify-center gap-3">
          <a
            href="https://whatsapp.com"
            target="_blank"
            rel="noopener noreferrer"
            className="w-full sm:w-auto flex items-center justify-center space-x-2 px-6 py-3.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm shadow-lg shadow-emerald-600/30 transition-transform hover:-translate-y-0.5"
          >
            <Zap className="w-4 h-4" />
            <span>Entrar no Canal do WhatsApp (Grátis)</span>
          </a>

          <a
            href="https://telegram.org"
            target="_blank"
            rel="noopener noreferrer"
            className="w-full sm:w-auto flex items-center justify-center space-x-2 px-6 py-3.5 rounded-xl bg-sky-600 hover:bg-sky-500 text-white font-bold text-sm shadow-lg shadow-sky-600/30 transition-transform hover:-translate-y-0.5"
          >
            <span>Canal no Telegram</span>
          </a>
        </div>

        <div className="pt-4 flex flex-wrap items-center justify-center gap-4 text-[12px] text-gray-400">
          <span className="flex items-center"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 mr-1" /> 100% Gratuito</span>
          <span className="flex items-center"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 mr-1" /> Sem spam ou conversas paralelas</span>
          <span className="flex items-center"><CheckCircle2 className="w-3.5 h-3.5 text-emerald-400 mr-1" /> Apenas cupons testados</span>
        </div>
      </div>
    </section>
  );
};
