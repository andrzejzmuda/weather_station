/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        atari: {
          black: "#000000",
          blue: "#003B6F",
          cyan: "#6FC3DF",
          yellow: "#F2E85C",
          white: "#FFFFFF",
          green: "#00FF66",
        },
      },
      fontFamily: {
        pixel: ["'Press Start 2P'", "monospace"],
      },
      boxShadow: {
        pixel: "0 0 0 4px #003B6F, 0 0 0 8px #6FC3DF",
      },
    },
  },
  plugins: [],
};
