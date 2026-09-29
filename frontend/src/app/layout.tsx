import "./globals.css";
import React from "react";

export const metadata = {
  title: "Portale Tris",
  description: "Gioco Tris con debug e modalità spettatore",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="it">
      <body className="bg-gray-50 dark:bg-gray-800 min-h-screen font-sans">
        {children}
      </body>
    </html>
  );
}