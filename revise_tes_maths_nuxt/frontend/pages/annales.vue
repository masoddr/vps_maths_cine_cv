<template>
  <div class="py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="lg:flex lg:items-center lg:justify-between">
        <div class="flex-1 min-w-0">
          <h2 class="text-2xl font-bold leading-7 text-gray-900 dark:text-gray-100 sm:text-3xl sm:truncate">
            Annales du Bac de Mathématiques
          </h2>
          <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">
            Trouve les sujets qui t'intéressent et entraîne-toi !
          </p>
        </div>
      </div>

      <!-- Barre de recherche -->
      <div class="mt-6">
        <div class="relative">
          <input
            type="text"
            id="search"
            v-model="searchQuery"
            class="block w-full pl-10 pr-3 py-2 border border-gray-300 dark:border-dark-600 rounded-md leading-5 bg-white dark:bg-dark-800 text-gray-900 dark:text-gray-100 placeholder-gray-500 dark:placeholder-gray-400 focus:outline-none focus:ring-indigo-500 dark:focus:ring-indigo-400 focus:border-indigo-500 dark:focus:border-indigo-400 sm:text-sm transition-colors duration-200"
            placeholder="Rechercher par titre, année ou thème..."
          />
          <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
            <svg class="h-5 w-5 text-gray-400 dark:text-gray-500" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd" />
            </svg>
          </div>
        </div>
      </div>

      <!-- Filtres et tri -->
      <div class="mt-6 flex flex-col sm:flex-row gap-4 mb-6">
        <div class="relative">
          <select v-model="selectedYear" class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md bg-white dark:bg-dark-800 text-gray-900 dark:text-gray-100">
            <option value="">Toutes les années</option>
            <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
          </select>
        </div>
        <div class="relative">
          <select v-model="selectedTheme" class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md bg-white dark:bg-dark-800 text-gray-900 dark:text-gray-100">
            <option value="">Tous les thèmes</option>
            <option v-for="theme in themes" :key="theme" :value="theme">{{ theme }}</option>
          </select>
        </div>
        <div class="relative">
          <select v-model="sortOrder" class="block w-full pl-3 pr-10 py-2 text-base border-gray-300 dark:border-gray-700 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md bg-white dark:bg-dark-800 text-gray-900 dark:text-gray-100">
            <option value="desc">Plus récent</option>
            <option value="asc">Plus ancien</option>
          </select>
        </div>
      </div>

      <!-- Message d'erreur -->
      <div v-if="error" class="mt-6 rounded-md bg-red-50 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="ml-3">
            <h3 class="text-sm font-medium text-red-800">
              {{ error }}
            </h3>
          </div>
        </div>
      </div>

      <!-- Indicateur de chargement -->
      <div v-if="loading" class="mt-6 flex justify-center">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
      </div>

      <!-- Contenu principal (masqué pendant le chargement) -->
      <div v-else>
        <!-- Liste des annales -->
        <div class="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <div v-for="annale in paginatedAnnales" :key="annale.id" class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg hover:shadow-lg transition-all duration-200">
            <div class="p-5">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                </div>
                <div class="ml-4">
                  <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">
                    {{ annale.title }}
                  </h3>
                  <p class="mt-1 text-sm text-gray-500 dark:text-gray-400">
                    {{ annale.year }}
                  </p>
                </div>
              </div>
              <div class="mt-4">
                <div v-for="exercise in annale.exercises" :key="exercise.id" class="mb-2">
                  <div class="flex items-center justify-between">
                    <div>
                      <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Exercice {{ exercise.number }}:</span>
                      <span v-for="theme in exercise.themes" :key="theme" class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 dark:bg-indigo-900 text-indigo-800 dark:text-indigo-200 mr-1">
                        {{ theme }}
                      </span>
                    </div>
                    <button
                      @click="updateExerciseStatus(exercise)"
                      :class="[
                        'px-2 py-1 rounded-md text-xs font-medium',
                        exercise.status === 'completed' ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' : 'bg-gray-100 text-gray-800 dark:bg-gray-900 dark:text-gray-200'
                      ]"
                    >
                      <span class="flex items-center">
                        <svg v-if="exercise.status === 'completed'" class="w-4 h-4 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        {{ exercise.status === 'completed' ? 'Terminé' : 'Marquer comme terminé' }}
                      </span>
                    </button>
                  </div>
                </div>
              </div>
              <div class="mt-4 flex justify-between items-center">
                <a 
                  :href="`${config.public.apiBase}/api/exampapers/${annale.id}/pdf`"
                  target="_blank"
                  class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Voir le sujet
                  <svg class="ml-2 h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                  </svg>
                </a>
              </div>
            </div>
          </div>
        </div>

        <!-- Pagination -->
        <div class="mt-6 flex items-center justify-between border-t border-gray-200 dark:border-gray-700 bg-white dark:bg-dark-800 px-4 py-3 sm:px-6">
          <div class="flex-1 flex justify-between sm:hidden">
            <button @click="previousPage" :disabled="currentPage === 1" class="relative inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-700 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-dark-800 hover:bg-gray-50 dark:hover:bg-dark-700 disabled:opacity-50">
              Précédent
            </button>
            <button @click="nextPage" :disabled="currentPage >= totalPages" class="ml-3 relative inline-flex items-center px-4 py-2 border border-gray-300 dark:border-gray-700 text-sm font-medium rounded-md text-gray-700 dark:text-gray-300 bg-white dark:bg-dark-800 hover:bg-gray-50 dark:hover:bg-dark-700 disabled:opacity-50">
              Suivant
            </button>
          </div>
          <div class="hidden sm:flex-1 sm:flex sm:items-center sm:justify-between">
            <div>
              <p class="text-sm text-gray-700 dark:text-gray-300">
                Affichage de <span class="font-medium">{{ paginationStart }}</span> à <span class="font-medium">{{ paginationEnd }}</span> sur <span class="font-medium">{{ filteredAnnales.length }}</span> résultats
              </p>
            </div>
            <div>
              <nav class="relative z-0 inline-flex rounded-md shadow-sm -space-x-px">
                <button @click="previousPage" :disabled="currentPage === 1" class="relative inline-flex items-center px-2 py-2 rounded-l-md border border-gray-300 dark:border-gray-700 bg-white dark:bg-dark-800 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-dark-700 disabled:opacity-50">
                  <span class="sr-only">Précédent</span>
                  <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
                </button>
                <button @click="nextPage" :disabled="currentPage >= totalPages" class="relative inline-flex items-center px-2 py-2 rounded-r-md border border-gray-300 dark:border-gray-700 bg-white dark:bg-dark-800 text-sm font-medium text-gray-500 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-dark-700 disabled:opacity-50">
                  <span class="sr-only">Suivant</span>
                  <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
                </button>
              </nav>
            </div>
          </div>
        </div>

        <!-- Message d'encouragement -->
        <SuccessMessage :show="showSuccessMessage" />
      </div>
    </div>

    <!-- Modal PDF -->
    <Teleport to="body">
      <div v-if="selectedPdf" class="modal" :class="{ 'with-zoom-controls': !isMobile }">
        <PdfViewer
          :pdf-url="selectedPdf"
          @close="selectedPdf = null"
        />
      </div>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRuntimeConfig } from '#app'
import PdfViewer from '~/components/PdfViewer.vue'
import ExerciseList from '~/components/ExerciseList.vue'
import SuccessMessage from '~/components/SuccessMessage.vue'
import { ChevronLeftIcon, ChevronRightIcon } from '@heroicons/vue/24/outline'

const config = useRuntimeConfig()
const searchQuery = ref('')
const selectedYear = ref('')
const selectedTheme = ref('')
const sortOrder = ref('desc')
const currentPage = ref(1)
const itemsPerPage = 9
const selectedPdf = ref(null)
const annales = ref([])
const loading = ref(true)
const error = ref(null)
const showSuccessMessage = ref(false)

const years = [2024, 2023]
const themes = [
  'Probabilités',
  'Géométrie dans l\'espace',
  'Suites numériques',
  'Fonctions',
  'Primitives',
  'Équations différentielles',
  'Logarithmes',
  'Nombres complexes',
  'Python'
]

definePageMeta({
  middleware: ['auth']
})

// Charger les annales depuis l'API
onMounted(async () => {
  try {
    loading.value = true
    error.value = null

    // Charger les annales
    const response = await useFetch('/api/exampapers', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    if (response.error.value) {
      throw new Error(response.error.value?.data?.error || 'Erreur lors du chargement des annales')
    }

    // Charger la progression des exercices
    const progressResponse = await useFetch('/api/progress', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    if (progressResponse.error.value) {
      console.error('Erreur lors du chargement de la progression:', progressResponse.error.value)
    }

    // Créer un map des statuts d'exercices
    const progressMap = new Map()
    if (progressResponse.data.value) {
      progressResponse.data.value.forEach(progress => {
        progressMap.set(progress.exercise_id, progress.status)
      })
    }

    // Ajouter le statut aux exercices
    annales.value = response.data.value.map(annale => ({
      ...annale,
      pdfUrl: `${config.public.apiBase}${annale.pdf_url}`,
      exercises: annale.exercises.map(exercise => ({
        ...exercise,
        status: progressMap.get(exercise.id) || 'not_started'
      }))
    }))
  } catch (err) {
    console.error('Erreur:', err)
    error.value = err.message
  } finally {
    loading.value = false
  }
})

// Filtrage et tri des annales
const filteredAnnales = computed(() => {
  let filtered = annales.value

  // Recherche par mot-clé
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(annale => {
      return annale.title.toLowerCase().includes(query) ||
             annale.exercises.some(ex => ex.description.toLowerCase().includes(query))
    })
  }

  // Filtres
  if (selectedYear.value) {
    filtered = filtered.filter(annale => annale.year === parseInt(selectedYear.value))
  }
  if (selectedTheme.value) {
    const selectedThemeLower = selectedTheme.value.toLowerCase()
    filtered = filtered.filter(annale => 
      annale.exercises.some(ex => 
        ex.themes.some(theme => theme.toLowerCase() === selectedThemeLower)
      )
    )
  }

  // Tri
  filtered = [...filtered].sort((a, b) => {
    switch (sortOrder.value) {
      case 'desc':
        return b.year - a.year
      case 'asc':
        return a.year - b.year
      default:
        return 0
    }
  })

  return filtered
})

// Pagination
const totalPages = computed(() => Math.ceil(filteredAnnales.value.length / itemsPerPage))
const startIndex = computed(() => (currentPage.value - 1) * itemsPerPage)
const endIndex = computed(() => Math.min(startIndex.value + itemsPerPage, filteredAnnales.value.length))

const paginatedAnnales = computed(() => {
  return filteredAnnales.value.slice(startIndex.value, endIndex.value)
})

// Détecter si on est sur mobile
const isMobile = computed(() => {
  if (process.client) {
    return window.innerWidth < 640
  }
  return false
})

// Ajouter la fonction de gestion de la mise à jour des exercices
async function handleExerciseUpdate(exercise) {
  // Recharger les statistiques de progression
  const statsResponse = await useFetch('/api/progress/stats', {
    baseURL: config.public.apiBase,
    credentials: 'include'
  })
  
  if (statsResponse.error.value) {
    console.error('Erreur lors du rechargement des statistiques:', statsResponse.error.value)
    return
  }

  // Mettre à jour l'exercice dans la liste des annales
  const annale = annales.value.find(a => a.exercises.some(e => e.id === exercise.id))
  if (annale) {
    const exerciseIndex = annale.exercises.findIndex(e => e.id === exercise.id)
    if (exerciseIndex !== -1) {
      annale.exercises[exerciseIndex] = { ...exercise }
    }
  }
}

// Fonction pour mettre à jour le statut d'un exercice
async function updateExerciseStatus(exercise) {
  try {
    const response = await useFetch(`/api/progress/${exercise.id}`, {
      method: 'POST',
      baseURL: config.public.apiBase,
      body: {
        status: exercise.status === 'completed' ? 'in_progress' : 'completed'
      },
      credentials: 'include'
    })

    if (response.error.value) {
      console.error('Erreur lors de la mise à jour du statut:', response.error.value)
      return
    }

    // Mettre à jour le statut localement
    const newStatus = exercise.status === 'completed' ? 'in_progress' : 'completed'
    exercise.status = newStatus

    // Afficher le message d'encouragement si l'exercice est marqué comme terminé
    if (newStatus === 'completed') {
      showSuccessMessage.value = true
      setTimeout(() => {
        showSuccessMessage.value = false
      }, 2000)
    }

    // Recharger les statistiques
    const statsResponse = await useFetch('/api/progress/stats', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (statsResponse.error.value) {
      console.error('Erreur lors du rechargement des statistiques:', statsResponse.error.value)
    }
  } catch (error) {
    console.error('Erreur lors de la mise à jour du statut:', error)
  }
}

// Réinitialiser la page courante quand les filtres changent
watch([searchQuery, selectedYear, selectedTheme, sortOrder], () => {
  currentPage.value = 1
})
</script>

<style scoped>
.modal {
  @apply fixed inset-0 z-50 bg-black bg-opacity-75;
}

.with-zoom-controls {
  @apply p-4;
}
</style> 