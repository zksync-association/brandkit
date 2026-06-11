/**
 * ZKsync Association — Tailwind preset
 * Usage:  module.exports = { presets: [require('./tailwind.preset.js')] }
 * Mirrors tokens.css. Colors are exposed under `brand`, `neutral`, `salmon`, etc.
 */
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          25: '#F3F5FE', 50: '#E7ECFC', 100: '#D4DCFA', 200: '#ADB9F6',
          300: '#8897F2', 400: '#5C6CEC', 500: '#0C18EC', 600: '#0914C4',
          700: '#070FA0', 800: '#050B7D', 900: '#04085F', 950: '#02053C',
        },
        neutral: {
          50: '#F7F9FC', 100: '#E8ECF2', 200: '#DADDE5', 300: '#BEC2CC',
          400: '#A1A7B3', 500: '#858C99', 600: '#6C7380', 700: '#555A66',
          800: '#3D424D', 900: '#262B33', 950: '#11141A', 975: '#0A0C10',
        },
        salmon: { 10: '#F6B6A6', 50: '#EA9682', 100: '#EE6D50' },
        sand:   { 50: '#FFF6E5' },
        light:  { 100: '#EDF2FA', 200: '#DAE2F2' },
      },
      fontFamily: {
        sans:    ['Inter', 'system-ui', 'sans-serif'],
        display: ['"ES Allianz"', 'Inter', 'sans-serif'],
        mono:    ['"Avenue Mono"', 'ui-monospace', 'monospace'],
      },
      letterSpacing: { title: '-0.03em', mono: '0.04em' },
      backgroundImage: {
        'zk-hero': 'linear-gradient(180deg, #BFEAFF 0%, #A5C0EE 100%)',
      },
      borderRadius: { zk: '4px' },
    },
  },
};
