<template>
  <div class="py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-gray-900 dark:text-gray-100">
        Tableau de bord
      </h1>
      
      <!-- Message de bienvenue personnalisé -->
      <div class="mt-4 bg-indigo-50 dark:bg-indigo-900 rounded-lg p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-6 w-6 text-indigo-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="ml-3">
            <h3 class="text-lg font-medium text-indigo-800 dark:text-indigo-200">
              {{ timeBasedGreeting }}, {{ user?.first_name || 'étudiant' }} 👋
            </h3>
            <div class="mt-2 text-sm text-indigo-700 dark:text-indigo-300">
              <p>{{ motivationalMessage }}</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Résumé de la progression -->
      <div class="mt-6 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
        <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <svg class="h-6 w-6 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                    Progression globale
                  </dt>
                  <dd class="flex items-baseline">
                    <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                      {{ progressStats.global || '0' }}%
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 dark:bg-dark-700 px-5 py-3">
            <div class="text-sm">
              <div class="font-medium text-indigo-700 dark:text-indigo-400 truncate">
                {{ progressStats.completedExercises || 0 }} exercices terminés sur {{ progressStats.totalExercises || 0 }}
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <svg class="h-6 w-6 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                    Temps de révision
                  </dt>
                  <dd class="flex items-baseline">
                    <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                      {{ progressStats.totalHours || 0 }}h
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 dark:bg-dark-700 px-5 py-3">
            <div class="text-sm">
              <div class="font-medium text-indigo-700 dark:text-indigo-400 truncate">
                Cette semaine
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <svg class="h-6 w-6 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6" />
                </svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                    Thèmes maîtrisés
                  </dt>
                  <dd class="flex items-baseline">
                    <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                      {{ progressStats.masteredTopics || 0 }}/{{ progressStats.totalTopics || 0 }}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 dark:bg-dark-700 px-5 py-3">
            <div class="text-sm">
              <div class="font-medium text-indigo-700 dark:text-indigo-400 truncate">
                Thèmes avec plus de 80% de réussite
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Liste des derniers exercices -->
      <div class="mt-8">
        <h2 class="text-lg font-medium text-gray-900 dark:text-gray-100">Derniers exercices</h2>
        <div class="mt-4 bg-white dark:bg-dark-800 shadow overflow-hidden sm:rounded-md">
          <ul role="list" class="divide-y divide-gray-200 dark:divide-dark-700">
            <li v-for="exercise in recentExercises" :key="exercise.id">
              <div class="px-4 py-4 sm:px-6">
                <div class="flex items-center justify-between">
                  <div class="flex items-center">
                    <div class="flex-shrink-0">
                      <div :class="[
                        exercise.status === 'completed' ? 'bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200' : 'bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200',
                        'h-8 w-8 rounded-full flex items-center justify-center'
                      ]">
                        <svg v-if="exercise.status === 'completed'" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                        </svg>
                        <svg v-else class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                      </div>
                    </div>
                    <div class="ml-4">
                      <h3 class="text-sm font-medium text-gray-900 dark:text-gray-100">
                        {{ exercise.title }}
                      </h3>
                      <div class="mt-1 flex items-center">
                        <span class="text-sm text-gray-500 dark:text-gray-400">{{ exercise.examPaper }}</span>
                        <span class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium" :class="[
                          exercise.status === 'completed' ? 'bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200' : 'bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200'
                        ]">
                          {{ exercise.status === 'completed' ? 'Terminé' : 'En cours' }}
                        </span>
                      </div>
                    </div>
                  </div>
                  <div class="ml-4 flex-shrink-0">
                    <button 
                      @click="updateExerciseStatus(exercise)"
                      class="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 dark:bg-indigo-500 hover:bg-indigo-700 dark:hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 dark:focus:ring-indigo-400"
                    >
                      {{ exercise.status === 'completed' ? 'Marquer comme à faire' : 'Marquer comme terminé' }}
                    </button>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

      <!-- Objectifs -->
      <div class="mt-8">
        <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100 mb-4">
          Objectifs de la semaine
        </h3>
        <div class="bg-white dark:bg-dark-800 shadow overflow-hidden sm:rounded-md">
          <ul class="divide-y divide-gray-200 dark:divide-gray-700">
            <li class="px-4 py-4 sm:px-6">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <div class="flex-shrink-0">
                    <svg class="h-8 w-8 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div class="ml-4">
                    <p class="text-sm font-medium text-gray-900 dark:text-gray-100">
                      Exercices à compléter
                    </p>
                    <p class="text-sm text-gray-500 dark:text-gray-400">
                      5 exercices cette semaine
                    </p>
                  </div>
                </div>
                <div class="ml-4">
                  <div class="text-sm text-gray-900 dark:text-gray-100">
                    {{ progressStats.completedExercises || 0 }}/5
                  </div>
                  <div class="w-32 h-2 bg-gray-200 dark:bg-gray-700 rounded-full mt-2">
                    <div 
                      class="h-full bg-green-500 rounded-full" 
                      :style="{ width: `${Math.min(100, (progressStats.completedExercises || 0) / 5 * 100)}%` }"
                    ></div>
                  </div>
                </div>
              </div>
            </li>
            <li class="px-4 py-4 sm:px-6">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <div class="flex-shrink-0">
                    <svg class="h-8 w-8 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <div class="ml-4">
                    <p class="text-sm font-medium text-gray-900 dark:text-gray-100">
                      Temps de révision quotidien
                    </p>
                    <p class="text-sm text-gray-500 dark:text-gray-400">
                      Objectif : 2 heures par jour
                    </p>
                  </div>
                </div>
                <div class="ml-4">
                  <div class="text-sm text-gray-900 dark:text-gray-100">
                    {{ progressStats.totalHours || 0 }}/14h
                  </div>
                  <div class="w-32 h-2 bg-gray-200 dark:bg-gray-700 rounded-full mt-2">
                    <div 
                      class="h-full bg-blue-500 rounded-full" 
                      :style="{ width: `${Math.min(100, (progressStats.totalHours || 0) / 14 * 100)}%` }"
                    ></div>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>

      <!-- Analyse des performances -->
      <div class="mt-8">
        <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100 mb-4">
          Analyse des performances
        </h3>
        <div class="grid grid-cols-1 gap-5 sm:grid-cols-2">
          <!-- Graphique des thèmes -->
          <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
            <div class="p-5">
              <div class="flex items-center justify-between mb-4">
                <h4 class="text-base font-medium text-gray-900 dark:text-gray-100">
                  Maîtrise par thème
                </h4>
              </div>
              <div class="relative h-64">
                <!-- Ici nous ajouterons un graphique radar avec Chart.js -->
                <p class="text-sm text-gray-500 dark:text-gray-400 text-center mt-8">
                  Graphique de progression par thème à venir
                </p>
              </div>
            </div>
          </div>

          <!-- Suggestions d'exercices -->
          <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
            <div class="p-5">
              <div class="flex items-center justify-between mb-4">
                <h4 class="text-base font-medium text-gray-900 dark:text-gray-100">
                  Suggestions d'exercices
                </h4>
              </div>
              <ul class="space-y-3">
                <li class="flex items-center space-x-3">
                  <span class="flex-shrink-0 w-2 h-2 bg-red-500 rounded-full"></span>
                  <span class="text-sm text-gray-700 dark:text-gray-300">Probabilités conditionnelles</span>
                </li>
                <li class="flex items-center space-x-3">
                  <span class="flex-shrink-0 w-2 h-2 bg-orange-500 rounded-full"></span>
                  <span class="text-sm text-gray-700 dark:text-gray-300">Suites numériques</span>
                </li>
                <li class="flex items-center space-x-3">
                  <span class="flex-shrink-0 w-2 h-2 bg-yellow-500 rounded-full"></span>
                  <span class="text-sm text-gray-700 dark:text-gray-300">Géométrie dans l'espace</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Dernières activités -->
      <div class="mt-8">
        <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100 mb-4">
          Dernières activités
        </h3>
        <div class="bg-white dark:bg-dark-800 shadow overflow-hidden sm:rounded-md">
          <ul class="divide-y divide-gray-200 dark:divide-gray-700">
            <li v-for="(activity, index) in recentActivities" :key="index" class="px-4 py-4 sm:px-6">
              <div class="flex items-center justify-between">
                <div class="flex items-center">
                  <div class="flex-shrink-0">
                    <svg class="h-6 w-6 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                    </svg>
                  </div>
                  <div class="ml-4">
                    <p class="text-sm font-medium text-gray-900 dark:text-gray-100">
                      {{ activity.title }}
                    </p>
                    <p class="text-sm text-gray-500 dark:text-gray-400">
                      {{ activity.description }}
                    </p>
                  </div>
                </div>
                <div class="ml-4 flex-shrink-0">
                  <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium" :class="activity.status === 'completed' ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200' : 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200'">
                    {{ activity.status === 'completed' ? 'Terminé' : 'En cours' }}
                  </span>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template> 

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRuntimeConfig } from '#app'

const config = useRuntimeConfig()
const user = ref(null)
const progressStats = ref({
  global: 0,
  completedExercises: 0,
  totalExercises: 0,
  totalHours: 0,
  masteredTopics: 0,
  totalTopics: 0
})

const recentExercises = ref([])
const recentActivities = ref([
  {
    title: 'Exercice sur les probabilités',
    description: 'Bac 2023 - Exercice 4',
    status: 'completed',
    date: new Date()
  },
  {
    title: 'Révision des suites',
    description: 'Chapitre 3 - Suites arithmétiques',
    status: 'in_progress',
    date: new Date()
  },
  {
    title: 'Exercice de géométrie',
    description: 'Bac 2022 - Exercice 2',
    status: 'completed',
    date: new Date()
  }
])

const timeBasedGreeting = computed(() => {
  const hour = new Date().getHours()
  
  if (hour < 12) {
    return 'Bonjour'
  } else if (hour < 18) {
    return 'Bon après-midi'
  } else {
    return 'Bonsoir'
  }
})

const motivationalMessage = computed(() => {
  if (!user.value) return 'Chargement de vos informations...'

  if (progressStats.value.completedExercises === 0) {
    return 'Prêt(e) à commencer ta première révision ? Découvre les exercices disponibles et lance-toi !'
  } else if (progressStats.value.global < 30) {
    return `Tu as déjà complété ${progressStats.value.completedExercises} exercice${progressStats.value.completedExercises > 1 ? 's' : ''}. Continue sur ta lancée !`
  } else if (progressStats.value.global < 60) {
    return 'Tu progresses bien ! Continue tes efforts, tu es sur la bonne voie.'
  } else if (progressStats.value.global < 80) {
    return 'Excellent travail ! Tu maîtrises de mieux en mieux les concepts. Le bac est à ta portée !'
  } else {
    return 'Bravo ! Tu as un excellent niveau. Continue à t\'entraîner pour maintenir ce cap !'
  }
})

definePageMeta({
  middleware: ['auth']
})

onMounted(async () => {
  try {
    // Charger les informations de l'utilisateur
    const userResponse = await useFetch('/api/auth/me', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (userResponse.error.value) {
      console.error('Erreur lors du chargement des informations utilisateur:', userResponse.error.value)
      return
    }
    
    user.value = userResponse.data.value?.user

    // Charger les statistiques de progression
    const statsResponse = await useFetch('/api/progress/stats', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (statsResponse.error.value) {
      console.error('Erreur lors du chargement des statistiques:', statsResponse.error.value)
      return
    }
    
    progressStats.value = statsResponse.data.value

    // Charger les exercices récents avec leurs détails
    const exercisesResponse = await useFetch('/api/progress/exercises', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (exercisesResponse.error.value) {
      console.error('Erreur lors du chargement des exercices:', exercisesResponse.error.value)
      return
    }
    
    recentExercises.value = exercisesResponse.data.value
  } catch (error) {
    console.error('Erreur lors du chargement des données:', error)
  }
})

async function updateExerciseStatus(exercise) {
  try {
    // S'assurer que nous avons un ID d'exercice valide
    const exerciseId = exercise.exercise_id || exercise.id
    if (!exerciseId) {
      console.error('ID d\'exercice manquant')
      return
    }

    const response = await useFetch(`/api/progress/${exerciseId}`, {
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
    exercise.status = exercise.status === 'completed' ? 'in_progress' : 'completed'

    // Recharger les statistiques immédiatement
    const statsResponse = await useFetch('/api/progress/stats', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (statsResponse.error.value) {
      console.error('Erreur lors du rechargement des statistiques:', statsResponse.error.value)
      return
    }

    // Mettre à jour les statistiques dans l'interface
    progressStats.value = statsResponse.data.value

    // Recharger la liste des exercices pour avoir les données à jour
    const exercisesResponse = await useFetch('/api/progress/exercises', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (exercisesResponse.error.value) {
      console.error('Erreur lors du rechargement des exercices:', exercisesResponse.error.value)
      return
    }

    recentExercises.value = exercisesResponse.data.value
  } catch (error) {
    console.error('Erreur lors de la mise à jour du statut:', error)
  }
}
</script> 