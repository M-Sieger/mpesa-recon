/**
 * postcss.config.js – PostCSS Configuration
 *
 * Purpose: Configure PostCSS plugins for CSS processing
 * Why: Transforms modern CSS into browser-compatible code
 *
 * Plugins:
 * - tailwindcss: Processes Tailwind utility classes
 * - autoprefixer: Adds vendor prefixes for browser compatibility
 */
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
