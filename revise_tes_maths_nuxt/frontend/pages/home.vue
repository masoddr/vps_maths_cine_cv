<template>
  <div class="py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- En-tête personnalisé -->
      <div class="text-center mb-12">
        <h1 class="text-4xl font-extrabold text-gray-900 dark:text-gray-100 sm:text-5xl">
          Bienvenue, {{ user?.first_name }} 👋
        </h1>
        <p class="mt-3 text-xl text-gray-500 dark:text-gray-400">
          Prêt à continuer ta progression ?
        </p>
      </div>

      <!-- Cartes de statistiques -->
      <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4 mb-12">
        <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <svg class="h-6 w-6 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
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
                      {{ stats.global }}%
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <svg class="h-6 w-6 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                    Exercices terminés
                  </dt>
                  <dd class="flex items-baseline">
                    <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                      {{ stats.completedExercises }}/{{ stats.totalExercises }}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <svg class="h-6 w-6 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
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
                      {{ stats.totalHours }}h
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0">
                <svg class="h-6 w-6 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
                </svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                    Thèmes maîtrisés
                  </dt>
                  <dd class="flex items-baseline">
                    <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                      {{ stats.masteredTopics }}/{{ stats.totalTopics }}
                    </div>
                  </dd>
                </dl>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Actions rapides -->
      <div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 mb-12">
        <NuxtLink to="/annales" class="relative group bg-white dark:bg-dark-800 p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-500 rounded-lg overflow-hidden hover:shadow-lg transition-all duration-200">
          <div>
            <span class="rounded-lg inline-flex p-3 bg-indigo-50 dark:bg-indigo-900 text-indigo-700 dark:text-indigo-300 ring-4 ring-white dark:ring-dark-800">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </span>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">
              Continuer les annales
              <span class="absolute inset-0" aria-hidden="true"></span>
            </h3>
            <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
              Accède à toutes les annales disponibles et continue ta progression.
            </p>
          </div>
          <span class="pointer-events-none absolute top-6 right-6 text-gray-300 dark:text-gray-700 group-hover:text-gray-400 dark:group-hover:text-gray-600" aria-hidden="true">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z" />
            </svg>
          </span>
        </NuxtLink>

        <NuxtLink to="/dashboard" class="relative group bg-white dark:bg-dark-800 p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-500 rounded-lg overflow-hidden hover:shadow-lg transition-all duration-200">
          <div>
            <span class="rounded-lg inline-flex p-3 bg-indigo-50 dark:bg-indigo-900 text-indigo-700 dark:text-indigo-300 ring-4 ring-white dark:ring-dark-800">
              <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
              </svg>
            </span>
          </div>
          <div class="mt-4">
            <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">
              Voir mon tableau de bord
              <span class="absolute inset-0" aria-hidden="true"></span>
            </h3>
            <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
              Consulte tes statistiques détaillées et ton historique.
            </p>
          </div>
          <span class="pointer-events-none absolute top-6 right-6 text-gray-300 dark:text-gray-700 group-hover:text-gray-400 dark:group-hover:text-gray-600" aria-hidden="true">
            <svg class="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
              <path d="M20 4h1a1 1 0 00-1-1v1zm-1 12a1 1 0 102 0h-2zM8 3a1 1 0 000 2V3zM3.293 19.293a1 1 0 101.414 1.414l-1.414-1.414zM19 4v12h2V4h-2zm1-1H8v2h12V3zm-.707.293l-16 16 1.414 1.414 16-16-1.414-1.414z" />
            </svg>
          </span>
        </NuxtLink>

        <div class="relative group bg-gradient-to-br from-indigo-500 to-purple-600 p-6 focus-within:ring-2 focus-within:ring-inset focus-within:ring-indigo-500 rounded-lg overflow-hidden hover:shadow-lg transition-all duration-200">
          <div class="absolute inset-0 bg-gradient-to-br from-indigo-500 to-purple-600"></div>
          <div class="relative">
            <div>
              <span class="rounded-lg inline-flex p-3 bg-white/10 text-white ring-4 ring-white/10">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </span>
            </div>
            <div class="mt-4">
              <h3 class="text-lg font-medium text-white">
                Prochaine étape
              </h3>
              <p class="mt-2 text-sm text-indigo-100">
                {{ nextStepMessage }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRuntimeConfig } from '#app'

const config = useRuntimeConfig()
const user = ref(null)
const stats = ref({
  global: 0,
  completedExercises: 0,
  totalExercises: 0,
  totalHours: 0,
  masteredTopics: 0,
  totalTopics: 0
})

definePageMeta({
  middleware: ['auth']
})

const nextStepMessage = computed(() => {
  if (stats.value.completedExercises === 0) {
    return "Commence par résoudre ton premier exercice !"
  }
  if (stats.value.global < 25) {
    return "Continue sur ta lancée, tu es sur la bonne voie !"
  }
  if (stats.value.global < 50) {
    return "Tu progresses bien, maintenant vise les 50% !"
  }
  if (stats.value.global < 75) {
    return "Excellent travail, le bac est à ta portée !"
  }
  return "Impressionnant ! Tu es prêt(e) pour le bac !"
})

onMounted(async () => {
  try {
    // Vérifier si l'utilisateur est connecté
    const authResponse = await useFetch('/api/auth/me', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    if (authResponse.data.value?.user) {
      user.value = authResponse.data.value.user

      // Charger les statistiques
      const statsResponse = await useFetch('/api/progress/stats', {
        baseURL: config.public.apiBase,
        credentials: 'include'
      })

      if (statsResponse.data.value) {
        stats.value = statsResponse.data.value
      }
    }
  } catch (error) {
    console.error('Erreur lors du chargement des données:', error)
  }
})
</script> 