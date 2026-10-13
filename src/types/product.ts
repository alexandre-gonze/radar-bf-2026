export type CategoryId = 
  | 'todos'
  | 'estudantes' 
  | 'ti-trabalho' 
  | 'gamers' 
  | 'casa-cozinha' 
  | 'maes-bebes' 
  | 'obra-ferramentas' 
  | 'carros';

export interface Product {
  id: string;
  name: string;
  tagline: string;
  category: CategoryId;
  categoryLabel: string;
  badge?: string; // ex: "Campeão Custo-Benefício", "Mais Vendido", "Recomendação BF"
  imageUrl: string;
  estimatedPrice: string;
  originalPrice?: string;
  discountPercentage?: number;
  
  // O Diferencial: Classificação por Casos de Uso Reais
  useCases: {
    perfectFor: string[];        // 🟢 Perfeito para...
    goodFor: string[];           // 🟡 Quebra o galho para...
    notRecommendedFor: string[]; // 🔴 NÃO compre se você precisa de...
  };

  specsSummary: {
    label: string;
    value: string;
  }[];

  // Links de Afiliados (Basta colar os códigos quando tiver aprovado)
  affiliateLinks: {
    amazon?: string;
    mercadoLivre?: string;
    shopee?: string;
  };

  // Selo de verificação
  verifiedDeal: boolean;
}
