/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.html",
    "./js/**/*.js"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          teal: '#044040',
          'teal-dark': '#022828',
          'teal-light': '#0a5c5c',
          'teal-subtle': '#eef5f5',
          gold: '#CF9D30',
          'gold-light': '#dfb24c',
          'gold-dark': '#a3781c',
          accent: '#C58B2B',
          dark: '#041B23',
          'dark-surface': '#082530',
          'dark-card': '#0c313f',
          surface: '#F8FAF9',
          'surface-card': '#ffffff',
          'border-light': '#e5ece9',
          'border-dark': '#153f4e'
        }
      },
      fontFamily: {
        heading: ['Outfit', 'sans-serif'],
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif']
      },
      boxShadow: {
        'glow': '0 0 25px -5px rgba(207, 157, 48, 0.3)',
        'glow-teal': '0 0 30px -5px rgba(4, 64, 64, 0.4)',
        'card': '0 10px 30px -5px rgba(4, 27, 35, 0.08)',
        'card-hover': '0 20px 40px -10px rgba(4, 27, 35, 0.14)'
      }
    }
  },
  plugins: []
}
