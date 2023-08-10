/** @type {import('tailwindcss').Config} */
module.exports = {
  mode: 'jit',
  content: ["./templates/**/*.{html,htm}"],
  theme: {
    extend: {},
    fontFamily: {
      'inter': ['Inter', 'sans-serif'],
      'exo': ['Exo', 'sans-serif'],
      'orbitron': ['Orbitron', 'sans-serif']
    }
  },
  plugins: [],
}

