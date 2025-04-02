<template>
  <div>
    <TheNavbar />
    
    <div v-if="film" class="container mx-auto px-4 py-8">
      <div class="flex flex-col lg:flex-row gap-8">
        <!-- Poster (caché sur mobile) -->
        <img 
          :src="film.poster" 
          :alt="film.titre" 
          class="hidden lg:block w-64 h-96 object-cover rounded-lg shadow-lg shrink-0"
        >
        
        <!-- Informations du film -->
        <div class="flex-1">
          <!-- En-tête mobile avec petite image -->
          <div class="flex items-center gap-4 mb-6 lg:hidden">
            <img 
              :src="film.poster" 
              :alt="film.titre" 
              class="w-20 h-30 object-cover rounded-lg shadow-md"
            >
            <div>
              <h1 class="text-2xl font-bold">{{ film.titre }}</h1>
              <div v-if="film.note" class="flex items-center mt-2">
                <span class="text-yellow-500">★</span>
                <span class="ml-1">{{ film.note.toFixed(1) }}/10</span>
              </div>
            </div>
          </div>

          <!-- Titre version desktop -->
          <h1 class="hidden lg:block text-3xl font-bold mb-4">{{ film.titre }}</h1>

          <div class="mb-6">
            <p class="text-gray-600"><strong><u>Durée</u></strong> : {{ formatDuration(film.duree) }}</p>
            <p class="text-gray-600"><strong><u>Date de sortie</u></strong> : {{ formatDate(film.date_sortie) }}</p>
            <p class="text-gray-600"><strong><u>Synopsis</u></strong> : {{ film.synopsis }}</p>
            <div v-if="film.note" class="flex items-center mt-2">
              <span class="text-yellow-500 text-2xl">★</span>
              <span class="ml-2 text-xl">{{ film.note.toFixed(1) }}/10</span>
            </div>

            <!-- Vignette YouTube -->
            <div v-if="trailerEmbedUrl" class="mt-4 max-w-xl">
              <div class="relative pt-[56.25%]">
                <iframe
                  :src="trailerEmbedUrl"
                  class="absolute top-0 left-0 w-full h-full rounded-lg shadow-md"
                  title="YouTube video player"
                  frameborder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowfullscreen
                ></iframe>
              </div>
            </div>
          </div>

          <h2 class="text-2xl font-semibold mb-4">Séances</h2>
          
          <!-- Séances groupées par jour -->
          <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div 
              v-for="(seances, day) in seancesByDay" 
              :key="day"
              class="bg-white p-4 rounded-lg shadow"
            >
              <h3 class="font-semibold mb-3">{{ formatDateShort(day) }}</h3>
              
              <div class="space-y-3">
                <div 
                  v-for="(cinemaSeances, cinema) in groupSeancesByCinema(seances)" 
                  :key="cinema"
                  class="border-t pt-2"
                >
                  <h4 
                    class="font-medium mb-2 flex items-center gap-2"
                    :style="{ color: getCinemaColor(cinema) }"
                  >
                    <span 
                      class="inline-block w-2 h-2 rounded-full"
                      :style="{ backgroundColor: getCinemaColor(cinema) }"
                    ></span>
                    {{ cinema }}
                  </h4>
                  
                  <div class="flex flex-wrap gap-1.5">
                    <div
                      v-for="seance in cinemaSeances"
                      :key="seance.heure"
                      class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-sm"
                      :style="{
                        backgroundColor: getCinemaLightColor(cinema),
                        color: getCinemaColor(cinema)
                      }"
                    >
                      <span class="font-medium">{{ seance.heure }}</span>
                      <span class="text-xs opacity-75">{{ seance.version }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bouton flottant de retour -->
    <NuxtLink 
      to="/films" 
      class="fixed bottom-6 right-6 bg-purple-600 hover:bg-purple-700 text-white px-4 py-3 rounded-full shadow-lg flex items-center gap-2 transition-all duration-300 hover:scale-105"
    >
      <svg 
        class="w-5 h-5 rotate-180" 
        viewBox="0 0 24 24" 
        fill="none" 
        xmlns="http://www.w3.org/2000/svg"
      >
        <path 
          d="M5 12H19M19 12L12 5M19 12L12 19" 
          stroke="currentColor" 
          stroke-width="1.5" 
          stroke-linecap="round" 
          stroke-linejoin="round"
        />
      </svg>
      <span>Retour aux séances</span>
    </NuxtLink>
  </div>
</template>

<script setup lang="ts">
import { useSeancesStore } from '~/stores/seances'
import { useCinemasStore } from '~/stores/cinemas'
import { storeToRefs } from 'pinia'
import TheNavbar from '~/components/TheNavbar.vue'
import { generateMeta } from '~/utils/seo'

const route = useRoute()
const store = useSeancesStore()
const cinemaStore = useCinemasStore()
const { seances } = storeToRefs(store)

// Charger les données au montage
onMounted(() => {
  if (seances.value.length === 0) {
    store.fetchSeances()
  }
})

// Obtenir le film et ses séances
const filmId = Number(route.params.id)
const film = computed(() => seances.value.find(s => s.tmdb_id === filmId))
const filmSeances = computed(() => 
  seances.value.filter(s => s.tmdb_id === filmId)
)

// Grouper les séances par jour
const seancesByDay = computed(() => {
  const grouped = {} as Record<string, typeof filmSeances.value>
  filmSeances.value.forEach(seance => {
    const day = seance.jour.split('T')[0]
    if (!grouped[day]) {
      grouped[day] = []
    }
    grouped[day].push(seance)
  })
  return grouped
})

// Grouper les séances par cinéma pour un jour donné
function groupSeancesByCinema(daySeances: typeof filmSeances.value) {
  return daySeances.reduce((acc, seance) => {
    if (!acc[seance.cinema]) {
      acc[seance.cinema] = []
    }
    acc[seance.cinema].push(seance)
    return acc
  }, {} as Record<string, typeof filmSeances.value>)
}

// Formater la date complète
const formatDate = (dateStr: string) => {
  return new Date(dateStr).toLocaleDateString('fr-FR', {
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  })
}

// Format court pour les dates des séances
const formatDateShort = (dateStr: string) => {
  return new Date(dateStr).toLocaleDateString('fr-FR', {
    weekday: 'long',
    day: 'numeric',
    month: 'long'
  })
}

// Formater la durée en heures et minutes
const formatDuration = (minutes: number) => {
  const hours = Math.floor(minutes / 60)
  const remainingMinutes = minutes % 60
  
  if (hours === 0) {
    return `${minutes}min`
  }
  
  if (remainingMinutes === 0) {
    return `${hours}h`
  }
  
  return `${hours}h${remainingMinutes.toString().padStart(2, '0')}`
}

// Couleurs des cinémas
const getCinemaColor = (cinema: string) => cinemaStore.getColor(cinema)
const getCinemaLightColor = (cinema: string) => cinemaStore.getLightColor(cinema)

// Convertir l'URL YouTube en URL d'intégration
const trailerEmbedUrl = computed(() => {
  if (!film.value?.trailer_url) return null
  
  const videoId = film.value.trailer_url.match(/(?:youtu\.be\/|youtube\.com(?:\/embed\/|\/v\/|\/watch\?v=|\/watch\?.+&v=))([\w-]{11})/)?.[1]
  
  if (!videoId) return null
  
  return `https://www.youtube.com/embed/${videoId}`
})

// SEO metadata
useHead(() => ({
  title: film.value ? `${film.value.titre} - Séances à Toulouse | Cinéphoria` : 'Film - Cinéphoria',
  meta: generateMeta({
    title: film.value ? `${film.value.titre} - Séances à Toulouse | Cinéphoria` : 'Film - Cinéphoria',
    description: film.value ? 
      `Retrouvez les horaires des séances de ${film.value.titre} dans les cinémas de Toulouse. ${film.value.synopsis?.slice(0, 150)}...` : 
      defaultMeta.description,
    image: film.value?.poster || defaultMeta.image,
    url: `https://cinephoria.fr/films/${filmId}`
  })
}))

// Schema.org markup
useHead({
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        '@context': 'https://schema.org',
        '@type': 'Movie',
        name: film.value?.titre,
        image: film.value?.poster,
        description: film.value?.synopsis,
        duration: `PT${film.value?.duree}M`,
        aggregateRating: film.value?.note ? {
          '@type': 'AggregateRating',
          ratingValue: film.value.note,
          bestRating: '10',
          worstRating: '0',
        } : undefined,
        trailer: film.value?.trailer_url ? {
          '@type': 'VideoObject',
          embedUrl: trailerEmbedUrl.value
        } : undefined
      })
    }
  ]
})
</script>

<style scoped>
/* Ajout des styles pour l'affichage responsive */
@media (max-width: 1023px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
}
</style> 