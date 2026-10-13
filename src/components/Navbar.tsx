import React from 'react';
import { Flame, Bell, ShieldCheck } from 'lucide-react';

interface NavbarProps {
  onOpenVipModal?: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({ onOpenVipModal }) => {
  return (
    <header className="sticky top-0 z-50 bg-gray-950/90 backdrop-blur-md border-b border-gray-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Slogan */}
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-red-600 to-amber-500 flex items-center justify-center shadow-lg shadow-red-500/20">
              <Flame className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-extrabold text-xl tracking-tight text-white">
                  Radar<span className="text-red-500">BF</span>
                </span>
                <span className="px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider bg-red-950 text-red-400 border border-red-800/60 rounded-full">
                  Sem Enrolação
                </span>
              </div>
              <p className="text-xs text-gray-400 hidden sm:block">
                O que vale a pena e para quem realmente serve
              </p>
            </div>
          </div>

          {/* Right Action / VIP Community */}
          <div className="flex items-center space-x-3">
            <div className="hidden md:flex items-center text-xs text-emerald-400 bg-emerald-950/40 border border-emerald-800/50 px-3 py-1.5 rounded-lg">
              <ShieldCheck className="w-4 h-4 mr-1.5" />
              Preços e Estoques Verificados
            </div>
            <a
              href="#radar-vip"
              onClick={onOpenVipModal}
              className="flex items-center space-x-2 bg-gradient-to-r from-red-600 to-red-700 hover:from-red-500 hover:to-red-600 text-white font-semibold text-xs sm:text-sm px-4 py-2 rounded-xl shadow-lg shadow-red-600/30 transition-all transform hover:-translate-y-0.5 active:translate-y-0"
            >
              <Bell className="w-4 h-4 animate-bounce" />
              <span>Receber Ofertas no WhatsApp</span>
            </a>
          </div>
        </div>
      </div>
    </header>
  );
};
