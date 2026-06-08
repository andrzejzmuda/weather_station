import "./globals.css";
import type { Metadata } from "next";
import { Navbar } from "./components/Navbar";


export const metadata: Metadata = {
  title: "Atari Weather Station",
  description: "Retro 8-bit weather dashboard",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pl">
      <body className="relative min-h-screen scanlines">
        <Navbar />
        <main className="px-4 py-8 max-w-6xl mx-auto">{children}</main>
      </body>
    </html>
  );
}
