// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    '@nuxtjs/tailwindcss'
  ],
  compatibilityDate: '2025-02-05',
  
  // Configuration de l'application
  app: {
    head: {
      title: 'Révise Tes Maths',
      link: [
        { rel: 'icon', type: 'image/png', href: '/images/mascotte.png' }
      ],
      meta: [
        { name: 'description', content: 'Plateforme de révision des mathématiques' }
      ]
    }
  },

  // Configuration du routage
  router: {
    options: {
      linkActiveClass: 'active',
      linkExactActiveClass: 'exact-active'
    }
  },

  // Configuration de l'API
  runtimeConfig: {
    public: {
      apiBase: process.env.NODE_ENV === 'production' 
        ? 'https://revise-tes-maths.fr' 
        : 'http://localhost:5000'
    }
  }
})