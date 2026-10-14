'use client';

import React from 'react';
import { CategoryId } from '@/types/product';
import { 
  Sparkles, 
  GraduationCap, 
  Laptop, 
  Gamepad2, 
  UtensilsCrossed, 
  Baby, 
  Hammer, 
  Car 
} from 'lucide-react';

interface CategoryFilterProps {
  selectedCategory: CategoryId;
  onSelectCategory: (id: CategoryId) => void;
  counts: Record<CategoryId, number>;
}

const CATEGORIES: { id: CategoryId; label: string; icon: React.ComponentType<{ className?: string }> }[] = [
  { id: 'todos', label: 'Todos os Garimpos', icon: Sparkles },
  { id: 'estudantes', label: 'Estudantes & Faculdade', icon: GraduationCap },
  { id: 'ti-trabalho', label: 'TI & Produtividade', icon: Laptop },
  { id: 'gamers', label: 'Setup & Games', icon: Gamepad2 },
  { id: 'casa-cozinha', label: 'Casa & Cozinha', icon: UtensilsCrossed },
  { id: 'maes-bebes', label: 'Mães & Bebês', icon: Baby },
  { id: 'obra-ferramentas', label: 'Obra & Ferramentas', icon: Hammer },
  { id: 'carros', label: 'Carros & Garagem', icon: Car },
];

export const CategoryFilter: React.FC<CategoryFilterProps> = ({
  selectedCategory,
  onSelectCategory,
  counts,
}) => {
  const activeCategories = CATEGORIES.filter(cat => cat.id === 'todos' || (counts[cat.id] && counts[cat.id] > 0));

  return (
    <div className="w-full overflow-x-auto pb-2 scrollbar-none">
      <div className="flex items-center space-x-2 sm:space-x-3 min-w-max">
        {activeCategories.map((cat) => {
          const Icon = cat.icon;
          const isSelected = selectedCategory === cat.id;
          const count = counts[cat.id] || 0;

          return (
            <button
              key={cat.id}
              onClick={() => onSelectCategory(cat.id)}
              className={`flex items-center space-x-2 px-4 py-2.5 rounded-xl font-medium text-xs sm:text-sm transition-all border ${
                isSelected
                  ? 'bg-red-600 text-white border-red-500 shadow-md shadow-red-600/30'
                  : 'bg-gray-900/80 hover:bg-gray-800 text-gray-300 border-gray-800 hover:border-gray-700'
              }`}
            >
              <Icon className={`w-4 h-4 ${isSelected ? 'text-white' : 'text-gray-400'}`} />
              <span>{cat.label}</span>
              <span
                className={`text-[11px] px-1.5 py-0.5 rounded-full ${
                  isSelected ? 'bg-red-800 text-red-100' : 'bg-gray-800 text-gray-400'
                }`}
              >
                {count}
              </span>
            </button>
          );
        })}
      </div>
    </div>
  );
};
