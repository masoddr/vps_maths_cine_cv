<template>
  <div>
    <DaySelector v-if="!loading" @update:day="updateSelectedDay" />
    
    <div class="container mx-auto px-4 py-8">
      <!-- État de chargement -->
      <div v-if="loading" class="text-center py-12">
        <p class="text-xl text-gray-600">Chargement des séances...</p>
      </div>
      
      <!-- Message d'erreur -->
      <div v-else-if="error" class="text-center py-12">
        <p class="text-xl text-red-600">{{ error }}</p>
      </div>

      <!-- Contenu principal -->
      <div v-else>
        <!-- Filtres -->
        <div class="mb-8 space-y-4">
          <!-- Barre de recherche -->
          <div class="max-w-xl mx-auto">
            <div class="relative">
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Rechercher un film..."
                class="w-full px-4 py-2 pr-10 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none"
              >
              <span 
                class="absolute right-3 top-1/2 -translate-y-1/2 text-gray-400"
                v-if="searchQuery"
                @click="searchQuery = ''"
                role="button"
                title="Effacer la recherche"
              >
                ✕
              </span>
            </div>
          </div>

          <!-- Filtres par cinéma -->
          <div class="flex flex-wrap justify-center gap-2">
            <button
              class="px-4 py-2 rounded-full text-sm font-medium transition-colors"
              :class="selectedCinema === null ? 'bg-gray-800 text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'"
              @click="selectedCinema = null"
            >
              Tous les cinémas
            </button>
            <button
              v-for="cinema in cinemas"
              :key="cinema"
              class="px-4 py-2 rounded-full text-sm font-medium transition-colors"
              :class="selectedCinema === cinema ? 'text-white' : 'hover:bg-opacity-10'"
              :style="{
                backgroundColor: selectedCinema === cinema ? getCinemaColor(cinema) : getCinemaLightColor(cinema),
                color: selectedCinema === cinema ? 'white' : getCinemaColor(cinema)
              }"
              @click="selectedCinema = cinema"
            >
              {{ cinema }}
            </button>
          </div>
        </div>

        <div class="mb-4 flex justify-end">
          <select v-model="sortBy" class="p-2 border rounded-md">
            <option value="default">Tri par défaut</option>
            <option value="rating">Tri par note</option>
            <option value="duration">Tri par durée</option>
          </select>
        </div>

        <h1 class="text-3xl font-bold mb-8">Programme des séances</h1>
        
        <div v-if="filteredDayFilms.length > 0" class="grid grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 gap-3 sm:gap-4">
          <NuxtLink
            v-for="film in sortedMovies"
            :key="film.tmdb_id"
            :to="`/films/${film.tmdb_id}`"
            class="bg-white rounded-lg shadow-md overflow-hidden transform transition-all duration-300 hover:scale-[1.02] hover:shadow-xl group"
          >
            <!-- Image avec overlay au survol -->
            <div class="relative">
              <img :src="film.poster" :alt="film.titre" 
                   class="w-full aspect-[2/3] object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-black/70 via-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
              </div>
            </div>
            
            <!-- Informations du film -->
            <div class="p-2 sm:p-3 md:p-4">
              <h3 class="font-bold text-sm sm:text-base md:text-lg mb-1 sm:mb-2 group-hover:text-blue-600 transition-colors line-clamp-2">
                {{ film.titre }}
              </h3>

              <div class="flex items-center gap-1 sm:gap-2 text-xs sm:text-sm text-gray-600 mb-2 sm:mb-3">
                <span>{{ formatDuration(film.duree) }}</span>
                <span v-if="film.note" class="flex items-center">
                  <span class="text-yellow-400">★</span>
                  <span class="ml-1">{{ film.note.toFixed(1) }}</span>
                </span>
              </div>

              <!-- Séances par cinéma -->
              <div class="space-y-2 sm:space-y-3">
                <div 
                  v-for="(seances, cinema, index) in limitedSeances(filmSeancesByCinema(film.tmdb_id))" 
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
                      v-for="seance in seances.slice(0, 4)"
                      :key="seance.heure"
                      class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-sm transition-colors"
                      :style="{
                        backgroundColor: getCinemaLightColor(cinema),
                        color: getCinemaColor(cinema),
                        '--tw-ring-color': getCinemaColor(cinema)
                      }"
                    >
                      <span class="font-medium">{{ seance.heure }}</span>
                      <span 
                        class="text-xs opacity-75"
                        :style="{ color: getCinemaColor(cinema) }"
                      >
                        {{ seance.version }}
                      </span>
                    </div>
                    <div 
                      v-if="seances.length > 4"
                      class="inline-flex items-center px-2 py-0.5 rounded-full text-sm bg-gray-100 text-gray-600"
                    >
                      +{{ seances.length - 4 }}
                    </div>
                  </div>
                </div>
                
                <!-- Badge pour indiquer d'autres cinémas -->
                <div 
                  v-if="Object.keys(filmSeancesByCinema(film.tmdb_id)).length > 1"
                  class="mt-2 inline-flex items-center px-2 py-1 rounded-full text-sm bg-blue-50 text-blue-600"
                >
                  <span class="font-medium">
                    +{{ Object.keys(filmSeancesByCinema(film.tmdb_id)).length - 1 }} autres cinémas
                  </span>
                </div>
              </div>
            </div>
          </NuxtLink>
        </div>
        <div v-else class="text-center py-12 text-gray-500">
          Aucun film ne correspond à votre recherche
        </div>
      </div>
    </div>

    <ScrollToTop />
  </div>
</template>

<script setup lang="ts">
import { useSeancesStore } from '~/stores/seances'
import { useCinemasStore } from '~/stores/cinemas'
import { storeToRefs } from 'pinia'
import ScrollToTop from '~/components/ScrollToTop.vue'

const store = useSeancesStore()
const cinemaStore = useCinemasStore()
const { seancesByDay, loading, error, cinemas } = storeToRefs(store)

// États des filtres
const searchQuery = ref('')
const selectedCinema = ref<string | null>(null)
const sortBy = ref('default')

// État de la recherche
const selectedDay = ref('')
const selectedDaySeances = computed(() => 
  selectedDay.value ? seancesByDay.value[selectedDay.value] : []
)

// Obtenir les films uniques pour le jour sélectionné
const selectedDayFilms = computed(() => {
  if (!selectedDaySeances.value) return []
  
  const uniqueFilms = new Map()
  selectedDaySeances.value.forEach(seance => {
    if (!uniqueFilms.has(seance.tmdb_id)) {
      uniqueFilms.set(seance.tmdb_id, seance)
    }
  })
  return Array.from(uniqueFilms.values())
})

// Filtrer les films par titre et cinéma
const filteredDayFilms = computed(() => {
  let films = selectedDayFilms.value

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase().trim()
    films = films.filter(film => 
      film.titre.toLowerCase().includes(query)
    )
  }

  if (selectedCinema.value) {
    films = films.filter(film => {
      const seances = filmSeancesByCinema(film.tmdb_id)
      return seances[selectedCinema.value]?.length > 0
    })
  }

  return films
})

function filmSeancesByCinema(filmId: number) {
  if (!selectedDaySeances.value) return {}
  
  const filmSeances = selectedDaySeances.value.filter(s => s.tmdb_id === filmId)
  return filmSeances.reduce((acc, seance) => {
    if (!acc[seance.cinema]) {
      acc[seance.cinema] = []
    }
    acc[seance.cinema].push(seance)
    return acc
  }, {} as Record<string, typeof selectedDaySeances.value>)
}

function updateSelectedDay(day: string) {
  selectedDay.value = day
}

watch(seancesByDay, (newValue) => {
  if (!selectedDay.value && Object.keys(newValue).length > 0) {
    selectedDay.value = Object.keys(newValue).sort()[0]
  }
}, { immediate: true })

const getCinemaColor = (cinema: string) => cinemaStore.getColor(cinema)
const getCinemaLightColor = (cinema: string) => cinemaStore.getLightColor(cinema)

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

const sortedMovies = computed(() => {
  if (sortBy.value === 'rating') {
    return [...filteredDayFilms.value].sort((a, b) => b.note - a.note)
  }
  if (sortBy.value === 'duration') {
    return [...filteredDayFilms.value].sort((a, b) => a.duree - b.duree)
  }
  return filteredDayFilms.value
})

// Fonction pour limiter l'affichage à un seul cinéma
function limitedSeances(seances: Record<string, any[]>) {
  const firstCinema = Object.keys(seances)[0]
  if (!firstCinema) return {}
  return { [firstCinema]: seances[firstCinema] }
}

onMounted(() => {
  store.fetchSeances()
})
</script>

<style scoped>
.flex-wrap {
  margin: -0.25rem;
}
.flex-wrap > * {
  margin: 0.25rem;
}

.group {
  backface-visibility: hidden;
  -webkit-font-smoothing: subpixel-antialiased;
}

.hover\:ring-1:hover {
  box-shadow: 0 0 0 1px var(--tw-ring-color);
}

[role="button"] {
  cursor: pointer;
}

button {
  border: 1px solid transparent;
}

button:focus {
  outline: none;
  ring: 2px;
  ring-offset: 2px;
}

.duration {
  font-size: 0.9em;
  color: #666;
  margin: 4px 0;
}

/* Ajout de styles pour uniformiser la taille des cards */
.movie-card {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.movie-card > div:last-child {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

/* Hauteur fixe pour la section des séances */
.space-y-3 {
  min-height: 80px;
  max-height: 80px;
  overflow: hidden;
}

@media (min-width: 640px) {
  .space-y-3 {
    min-height: 90px;
    max-height: 90px;
  }
}

@media (min-width: 768px) {
  .space-y-3 {
    min-height: 100px;
    max-height: 100px;
  }
}

/* Ajustements pour les badges de séances en responsive */
.rounded-full {
  @media (max-width: 640px) {
    padding: 0.125rem 0.5rem;
    font-size: 0.75rem;
  }
}
</style> 