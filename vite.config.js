import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  root: "./client",
  server:{
    port: 5173
  },
  build:{
    outDir: 'dist',
  },
  plugins: [react()]
});