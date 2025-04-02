// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Mode statique
  ssr: true,

  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/']
    },
    server: {
      port: process.env.PORT
    },
    routeRules: {
      '/': { prerender: true },
      '/films': { prerender: true },
      '/cinemas': { prerender: true }
    }
  },

  // Modules utiles
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],

  // Configuration des répertoires publics
  dir: {
    public: 'public'
  },

  // Configuration de Leaflet
  plugins: [
    '~/plugins/leaflet.client.ts'
  ],

  build: {
    transpile: ['@vue-leaflet/vue-leaflet']
  },

  compatibilityDate: '2025-03-20',

  app: {
    head: {
      htmlAttrs: {
        lang: 'fr'
      },
      title: 'Cinéma Toulouse - Guide des séances et films | Cinéphoria',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'format-detection', content: 'telephone=no' },
        { name: 'robots', content: 'index, follow' },
        { name: 'theme-color', content: '#6B46C1' },
        { name: 'geo.region', content: 'FR-31' },
        { name: 'geo.placename', content: 'Toulouse' },
        { name: 'geo.position', content: '43.604652;1.444209' },
        { name: 'ICBM', content: '43.604652, 1.444209' }
      ],
      link: [
        { 
          rel: 'icon', 
          type: 'image/png', 
          href: '/favicon-16x16.png',
          sizes: '16x16'
        },
        { 
          rel: 'icon', 
          type: 'image/png', 
          href: '/favicon-32x32.png',
          sizes: '32x32'
        },
        // Pour les appareils Apple
        { 
          rel: 'apple-touch-icon', 
          href: '/apple-touch-icon.png',
          sizes: '180x180'
        },
        { rel: 'canonical', href: 'https://cinephoria.fr' }
      ]
    }
  }
})