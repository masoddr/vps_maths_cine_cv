<template>
  <div class="max-w-4xl mx-auto px-4 py-12">
    <NuxtLink 
      to="/" 
      class="inline-flex items-center mb-8 text-gray-600 hover:text-blue-600 transition-colors duration-200"
    >
      <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
      </svg>
      Retour à l'accueil
    </NuxtLink>

    <h1 class="text-4xl font-bold mb-12 text-center text-gray-800">Mentions Légales</h1>
    
    <div class="prose prose-blue max-w-none space-y-8">
      <section>
        <h2 class="text-2xl font-semibold text-blue-600">Éditeur du site</h2>
        <p>
          Le site optimise-ton-cv.fr est édité par :<br>
          Massyl OUADDOUR<br>
          Email : ouaddour.massyl@gmail.com
        </p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-blue-600">Hébergement</h2>
        <p>
          Le site est hébergé par :<br>
          HOSTINGER INTERNATIONAL LTD<br>
          61 Lordou Vironos Street<br>
          6023 Larnaca, Chypre<br>
          Site web : <a href="https://www.hostinger.fr" class="text-blue-600 hover:text-blue-800">www.hostinger.fr</a>
        </p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-blue-600">Propriété intellectuelle</h2>
        <p>
          L'ensemble du contenu de ce site (textes, images, logos, etc.) est protégé par le droit d'auteur.
          Toute reproduction ou représentation, totale ou partielle, est interdite sans autorisation préalable.
        </p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-blue-600">Protection des données</h2>
        <p>
          Les données personnelles collectées sur ce site sont uniquement utilisées pour l'analyse des CV.
          Aucune donnée n'est stockée de manière permanente ni partagée avec des tiers.
          Conformément à la loi "Informatique et Libertés" du 6 janvier 1978, vous disposez d'un droit d'accès,
          de rectification et de suppression des données vous concernant.
        </p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-blue-600">Cookies</h2>
        <p>
          Ce site utilise des cookies techniques essentiels au fonctionnement du service.
          Aucun cookie publicitaire ou de traçage n'est utilisé.
        </p>
      </section>

      <section>
        <h2 class="text-2xl font-semibold text-blue-600">Technologies utilisées</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mt-6">
          <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-sm">
            <img 
              src="/FastAPI.svg" 
              alt="FastAPI" 
              class="h-12 dark:invert"
            />
            <h3 class="text-lg font-semibold mb-2">FastAPI</h3>
            <p class="text-sm text-center text-gray-600">
              Framework Python pour APIs performantes
            </p>
          </div>

          <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-sm">
            <img 
              src="/Nuxt JS.svg" 
              alt="Nuxt.js" 
              class="h-12 dark:invert"
            />
            <h3 class="text-lg font-semibold mb-2">Nuxt.js</h3>
            <p class="text-sm text-center text-gray-600">
              Framework Vue.js pour applications web modernes
            </p>
            <a 
              href="https://nuxt.com" 
              target="_blank" 
              rel="noopener noreferrer"
              class="text-blue-600 hover:text-blue-800 text-sm mt-2"
            >
              En savoir plus
            </a>
          </div>

          <div class="flex flex-col items-center p-6 bg-white rounded-lg shadow-sm">
            <img 
              src="/Tailwind CSS.svg" 
              alt="Tailwind CSS" 
              class="h-12"
            />
            <h3 class="text-lg font-semibold mb-2">Tailwind CSS</h3>
            <p class="text-sm text-center text-gray-600">
              Framework CSS utilitaire moderne
            </p>
          </div>
        </div>
      </section>
    </div>
  </div>
</template> 