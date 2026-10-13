import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Radar BF 2026 | Guia de Compras sem Enrolação',
  description: 'Descubra quais produtos realmente valem a pena na Black Friday. Classificação por casos de uso: para quem serve e para quem NÃO serve.',
  openGraph: {
    title: 'Radar BF 2026 | Guia de Compras sem Enrolação',
    description: 'Descubra quais produtos realmente valem a pena na Black Friday com curadoria independente.',
    type: 'website',
  },
  icons: {
    icon: '/logo.jpg',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR" className="dark">
      <body className="min-h-screen bg-gray-950 text-gray-100 antialiased selection:bg-red-600 selection:text-white">
        {children}
      </body>
    </html>
  );
}
