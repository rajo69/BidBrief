import './globals.css';
import type { ReactNode } from 'react';

export const metadata = {
  title: 'BidBrief',
  description: 'From notice to brief in minutes.'
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}