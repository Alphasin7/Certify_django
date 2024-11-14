/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}",  // Adjust path to match your template directory
    "./static/**/*.{html,js}",      // If you have JS in a static directory
    "./src/**/*.{html,js}",         // Keep this if you have a separate src folder
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
