<template>
  <div>
    <TheNavbar />
    
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-3xl font-bold mb-8">Cinémas à Toulouse</h1>
      
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="cinema in cinemas" :key="cinema.id" class="bg-white rounded-lg shadow-lg overflow-hidden">
          <div class="aspect-video relative">
            <img 
              :src="cinema.image" 
              :alt="cinema.nom"
              class="w-full h-full object-cover"
            />
          </div>
          
          <div class="p-4">
            <h2 class="text-xl font-semibold mb-2">{{ cinema.nom }}</h2>
            <p class="text-gray-600 mb-4">{{ cinema.adresse }}</p>
            
            <div class="flex items-center gap-2 text-sm text-gray-500 mb-4">
              <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none">
                <path d="M12 6v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                <circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/>
              </svg>
              <span>{{ cinema.horaires }}</span>
            </div>
            
            <div class="flex items-center gap-4">
              <a 
                :href="cinema.itineraire" 
                target="_blank"
                class="text-purple-600 hover:text-purple-800 flex items-center gap-1"
              >
                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none">
                  <path d="M9 20l-5-5 5-5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                  <path d="M20 4v7a4 4 0 01-4 4H4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                Itinéraire
              </a>
              <a 
                :href="cinema.site" 
                target="_blank"
                class="text-purple-600 hover:text-purple-800 flex items-center gap-1"
              >
                <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none">
                  <path d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                </svg>
                Site web
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useCinemasStore } from '~/stores/cinemas'
import { storeToRefs } from 'pinia'
import { generateMeta } from '~/utils/seo'
import TheNavbar from '~/components/TheNavbar.vue'

const store = useCinemasStore()
const { cinemas } = storeToRefs(store)

// SEO
useHead({
  title: 'Cinémas à Toulouse - Liste des salles | Cinéphoria',
  meta: generateMeta({
    title: 'Cinémas à Toulouse - Liste des salles | Cinéphoria',
    description: 'Découvrez tous les cinémas de Toulouse : adresses, horaires, accès. Guide complet des salles de cinéma toulousaines.',
    url: 'https://cinephoria.fr/cinemas'
  })
})

// Chargement des données
onMounted(() => {
  if (cinemas.value.length === 0) {
    store.fetchCinemas()
  }
})
</script> 