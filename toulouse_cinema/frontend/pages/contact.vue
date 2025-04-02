<template>
  <div class="max-w-6xl mx-auto px-4 py-12">
    <!-- En-tête avec photo -->
    <div class="relative mb-24">
      <div class="absolute inset-0 bg-gradient-to-r from-primary/10 to-primary/5 rounded-3xl"></div>
      <div class="relative flex flex-col md:flex-row items-center gap-8 p-8 rounded-3xl">
        <div class="md:w-1/3">
          <img 
            src="/images/massyl.jpg" 
            alt="Massyl Ouaddour" 
            class="w-64 h-64 object-cover rounded-2xl shadow-xl transform hover:scale-105 transition-transform duration-300"
          />
        </div>
        <div class="md:w-2/3">
          <h1 class="text-4xl font-bold mb-4 bg-gradient-to-r from-primary to-primary-dark bg-clip-text text-transparent">
            Massyl Ouaddour
          </h1>
          <p class="text-xl text-gray-700 mb-6">Ingénieur Systèmes Spatiaux | Développeur Python</p>
          <div class="flex gap-4">
            <a 
              href="mailto:ouaddour.massyl@gmail.com"
              class="flex items-center gap-2 px-4 py-2 bg-white rounded-full shadow-md hover:shadow-lg transition-shadow duration-300"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <span>Me contacter</span>
            </a>
            <a 
              href="https://masoddr.github.io/portfolio_massyl/"
              target="_blank"
              rel="noopener noreferrer"
              class="flex items-center gap-2 px-4 py-2 bg-white rounded-full shadow-md hover:shadow-lg transition-shadow duration-300"
            >
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9" />
              </svg>
              <span>Mon portfolio</span>
            </a>
          </div>
        </div>
      </div>
    </div>

    <!-- Sections de compétences -->
    <div class="grid md:grid-cols-2 gap-8">
      <!-- Ingénierie Spatiale -->
      <div class="bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300">
        <div class="flex items-center gap-3 mb-4">
          <div class="p-2 bg-primary/10 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
            </svg>
          </div>
          <h3 class="text-xl font-bold">Ingénierie Spatiale</h3>
        </div>
        <p class="text-gray-600 mb-4">
          Je suis un ingénieur spécialisé dans l'ingénierie spatiale, avec une expertise dans la modélisation, 
          la simulation et l'optimisation de systèmes complexes pour le secteur spatial.
        </p>
        <div class="flex flex-wrap gap-2">
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Traitement de données</span>
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Modélisation</span>
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Simulation</span>
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Modélisation d'antennes</span>
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Bilans de liaison</span>
        </div>
      </div>

      <!-- Développement Web -->
      <div class="bg-white p-6 rounded-2xl shadow-lg hover:shadow-xl transition-shadow duration-300">
        <div class="flex items-center gap-3 mb-4">
          <div class="p-2 bg-primary/10 rounded-lg">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-primary" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 9l3 3-3 3m5 0h3M5 20h14a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
          </div>
          <h3 class="text-xl font-bold">Développement Web</h3>
        </div>
        <p class="text-gray-600 mb-4">
          Je développe des sites web modernes et performants, en utilisant les dernières technologies.
          Mon expertise couvre aussi bien le développement backend avec Python que le frontend avec Vue.js.
        </p>
        <div class="flex flex-wrap gap-2">
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Python</span>
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Flask API</span>
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">Vue.js</span>
          <span class="px-3 py-1 bg-primary/5 text-primary rounded-full text-sm">PostgreSQL</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.bg-gradient-to-r {
  background-size: 200% 200%;
  animation: gradient 15s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}
</style>

<script setup>
// Plus besoin du code du formulaire
</script> 