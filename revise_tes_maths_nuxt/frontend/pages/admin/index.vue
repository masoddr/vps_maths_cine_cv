<template>
  <div>
    <div class="md:flex md:items-center md:justify-between">
      <div class="flex-1 min-w-0">
        <h2 class="text-2xl font-bold leading-7 text-gray-900 dark:text-gray-100 sm:text-3xl sm:truncate">
          Tableau de bord administrateur
        </h2>
      </div>
    </div>

    <div class="mt-8 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
      <!-- Carte Utilisateurs -->
      <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
        <div class="p-5">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <svg class="h-6 w-6 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
              </svg>
            </div>
            <div class="ml-5 w-0 flex-1">
              <dl>
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                  Utilisateurs inscrits
                </dt>
                <dd class="flex items-baseline">
                  <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                    {{ stats.totalUsers }}
                  </div>
                </dd>
              </dl>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 dark:bg-dark-700 px-5 py-3">
          <div class="text-sm">
            <NuxtLink to="/admin/users" class="font-medium text-indigo-700 dark:text-indigo-400 hover:text-indigo-900 dark:hover:text-indigo-300">
              Voir tous les utilisateurs
            </NuxtLink>
          </div>
        </div>
      </div>

      <!-- Carte Annales -->
      <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
        <div class="p-5">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <svg class="h-6 w-6 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <div class="ml-5 w-0 flex-1">
              <dl>
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                  Annales disponibles
                </dt>
                <dd class="flex items-baseline">
                  <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                    {{ stats.totalExamPapers }}
                  </div>
                </dd>
              </dl>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 dark:bg-dark-700 px-5 py-3">
          <div class="text-sm">
            <NuxtLink to="/admin/annales" class="font-medium text-indigo-700 dark:text-indigo-400 hover:text-indigo-900 dark:hover:text-indigo-300">
              Gérer les annales
            </NuxtLink>
          </div>
        </div>
      </div>

      <!-- Carte Exercices -->
      <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
        <div class="p-5">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <svg class="h-6 w-6 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <div class="ml-5 w-0 flex-1">
              <dl>
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                  Exercices créés
                </dt>
                <dd class="flex items-baseline">
                  <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                    {{ stats.totalExercises }}
                  </div>
                </dd>
              </dl>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 dark:bg-dark-700 px-5 py-3">
          <div class="text-sm">
            <NuxtLink to="/admin/annales" class="font-medium text-indigo-700 dark:text-indigo-400 hover:text-indigo-900 dark:hover:text-indigo-300">
              Gérer les exercices
            </NuxtLink>
          </div>
        </div>
      </div>

      <!-- Carte Messages -->
      <div class="bg-white dark:bg-dark-800 overflow-hidden shadow rounded-lg">
        <div class="p-5">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <svg class="h-6 w-6 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="ml-5 w-0 flex-1">
              <dl>
                <dt class="text-sm font-medium text-gray-500 dark:text-gray-400 truncate">
                  Messages reçus
                </dt>
                <dd class="flex items-baseline">
                  <div class="text-2xl font-semibold text-gray-900 dark:text-gray-100">
                    {{ stats.totalMessages }}
                  </div>
                </dd>
              </dl>
            </div>
          </div>
        </div>
        <div class="bg-gray-50 dark:bg-dark-700 px-5 py-3">
          <div class="text-sm">
            <NuxtLink to="/admin/messages" class="font-medium text-indigo-700 dark:text-indigo-400 hover:text-indigo-900 dark:hover:text-indigo-300">
              Voir les messages
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'admin',
  middleware: ['auth', 'admin']
})

const config = useRuntimeConfig()
const stats = ref({
  totalUsers: 0,
  totalExamPapers: 0,
  totalExercises: 0,
  totalMessages: 0
})

// Charger les statistiques
onMounted(async () => {
  try {
    const [usersResponse, examPapersResponse, messagesResponse] = await Promise.all([
      useFetch('/api/admin/users', {
        baseURL: config.public.apiBase,
        credentials: 'include'
      }),
      useFetch('/api/exampapers', {
        baseURL: config.public.apiBase,
        credentials: 'include'
      }),
      useFetch('/api/admin/contact-messages', {
        baseURL: config.public.apiBase,
        credentials: 'include'
      })
    ])

    if (usersResponse.data.value) {
      stats.value.totalUsers = usersResponse.data.value.length
    }

    if (examPapersResponse.data.value) {
      stats.value.totalExamPapers = examPapersResponse.data.value.length
      stats.value.totalExercises = examPapersResponse.data.value.reduce(
        (total, paper) => total + (paper.exercises?.length || 0),
        0
      )
    }

    if (messagesResponse.data.value) {
      stats.value.totalMessages = messagesResponse.data.value.length
    }
  } catch (error) {
    console.error('Erreur lors du chargement des statistiques:', error)
  }
})
</script> 