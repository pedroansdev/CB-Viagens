/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,vue}"
  ],
  theme: {
    colors: {
      'cb-gray': '#2A3041',
      'cb-light-gray': '#F3F3F3',
      'cb-blue': '#03A8B5',
      'cb-yellow': '#F3A531',
      'cb-white': '#FFFFFF',
      'cb-gray-600': '#4B5563',
      'cb-gray-transparent': 'rgb(42, 48, 65, .3)'
    },
    extend: {},
  },
  plugins: [],
}