/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // SACCO-friendly brand colors
        primary: {
          50: '#e6f7f5',
          100: '#b3e8e0',
          200: '#80d9cb',
          300: '#4dcab6',
          400: '#1abba1',
          500: '#0B7285', // Main brand color (teal/green - trust & growth)
          600: '#095b6a',
          700: '#07444f',
          800: '#052d34',
          900: '#031619',
        },
        secondary: {
          50: '#e6f4ff',
          100: '#b3dcff',
          200: '#80c4ff',
          300: '#4dacff',
          400: '#1a94ff',
          500: '#014D40', // Dark green (professional)
          600: '#013d33',
          700: '#012e26',
          800: '#001f1a',
          900: '#000f0d',
        },
        success: {
          50: '#e8f5e9',
          500: '#4caf50',
          700: '#388e3c',
        },
        warning: {
          50: '#fff3e0',
          500: '#ff9800',
          700: '#f57c00',
        },
        error: {
          50: '#ffebee',
          500: '#f44336',
          700: '#d32f2f',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        heading: ['Poppins', 'Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 2px 8px rgba(0, 0, 0, 0.08)',
        'medium': '0 4px 16px rgba(0, 0, 0, 0.12)',
        'strong': '0 8px 24px rgba(0, 0, 0, 0.16)',
      },
      borderRadius: {
        'card': '12px',
      },
    },
  },
  plugins: [],
}
