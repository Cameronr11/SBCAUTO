import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { About } from "@/components";


export const metadata: Metadata = {
  title: "SBC Auto",
  description: "Developed by Cameron Rader."
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

return (
    <html lang="en">
      <body className="relative">
      <About />
        {children}
        </body>
    </html>
  );
}