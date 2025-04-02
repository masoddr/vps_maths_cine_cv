<template>
      <div>
    <template v-if="isLoggedIn">
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

    <template v-else>
      <!-- Page d'accueil pour les visiteurs -->
      <div class="relative">
        <!-- Hero section avec fonctionnalités -->
        <div class="relative bg-gray-50 dark:bg-dark-900 overflow-hidden">
          <div class="max-w-7xl mx-auto">
            <div class="relative z-10 pb-8 bg-gray-50 dark:bg-dark-900 sm:pb-16 md:pb-20 lg:pb-28 xl:pb-32">
              <main class="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
                <div class="text-center">
                  <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 dark:text-gray-100 sm:text-5xl md:text-6xl animate-fade-in">
                    <span class="block bg-gradient-to-r from-indigo-600 to-purple-600 text-transparent bg-clip-text hover:scale-105 transform transition-transform duration-300">Réussis ton Bac de Maths</span>
                    <span class="block text-indigo-600 dark:text-indigo-400 animate-bounce-soft">sans stress et efficacement ! ✨</span>
                  </h1>
                  <p class="mt-3 text-base text-gray-500 dark:text-gray-400 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl">
                    Une plateforme complète pour préparer ton bac de maths avec :
                  </p>
                </div>

                <!-- Boutons d'action pour mobile -->
                <div class="mt-8 flex flex-col space-y-4 sm:hidden">
                  <div class="rounded-md shadow">
                    <NuxtLink to="/register" class="w-full flex items-center justify-center px-8 py-4 border border-transparent text-lg font-medium rounded-md text-white bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 transform hover:scale-105 transition-all duration-300 shadow-lg">
                      <span class="flex items-center">
                        <svg class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                        </svg>
                        Commence maintenant
                      </span>
                    </NuxtLink>
                  </div>
                  <div class="rounded-md">
                    <NuxtLink to="/presentation" class="group relative w-full flex items-center justify-center px-8 py-4 border-2 border-indigo-600 dark:border-indigo-400 text-lg font-medium rounded-md text-indigo-700 dark:text-indigo-300 bg-white dark:bg-dark-900 hover:bg-indigo-50 dark:hover:bg-dark-800 transform hover:scale-105 transition-all duration-300">
                      <span class="absolute -top-2 -right-2 bg-gradient-to-r from-red-500 to-pink-500 text-white text-xs px-2 py-1 rounded-full transform group-hover:scale-110 transition-transform duration-200 animate-pulse">Nouveau !</span>
                      <span class="flex items-center">
                        <svg class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                        </svg>
                        Cours particuliers 👨‍🏫
                      </span>
                    </NuxtLink>
                  </div>
                </div>

                <!-- Fonctionnalités principales -->
                <div class="mt-12 max-w-lg mx-auto grid gap-8 lg:grid-cols-3 lg:max-w-none">
                  <!-- Annales -->
                  <div class="flex flex-col rounded-lg shadow-lg overflow-hidden bg-white/50 dark:bg-dark-800/50 backdrop-blur-md hover:transform hover:scale-105 transition-all duration-300">
                    <div class="flex-1 p-6 flex flex-col justify-between">
                      <div class="flex-1">
                        <div class="flex items-center">
                          <div class="flex-shrink-0 h-10 w-10">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-gradient-to-br from-indigo-500 to-purple-600 text-white">
                              <svg class="h-6 w-6 animate-bounce-soft" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                              </svg>
                            </div>
                          </div>
                          <h3 class="ml-4 text-xl font-semibold text-gray-900 dark:text-gray-100">Annales corrigées</h3>
                        </div>
                        <div class="mt-3 text-base text-gray-500 dark:text-gray-400">
                          <ul class="space-y-2">
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Sujets des années précédentes
                            </li>
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Corrigés détaillés
                            </li>
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Classement par thème
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Suivi de progression -->
                  <div class="flex flex-col rounded-lg shadow-lg overflow-hidden bg-white/50 dark:bg-dark-800/50 backdrop-blur-md hover:transform hover:scale-105 transition-all duration-300">
                    <div class="flex-1 p-6 flex flex-col justify-between">
                      <div class="flex-1">
                        <div class="flex items-center">
                          <div class="flex-shrink-0 h-10 w-10">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-gradient-to-br from-indigo-500 to-purple-600 text-white">
                              <svg class="h-6 w-6 animate-chart" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                              </svg>
                            </div>
                          </div>
                          <h3 class="ml-4 text-xl font-semibold text-gray-900 dark:text-gray-100">Suivi personnalisé</h3>
                        </div>
                        <div class="mt-3 text-base text-gray-500 dark:text-gray-400">
                          <ul class="space-y-2">
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Tableau de bord interactif
                            </li>
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Statistiques détaillées
                            </li>
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Progression visualisée
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>

                  <!-- Exercices ciblés -->
                  <div class="flex flex-col rounded-lg shadow-lg overflow-hidden bg-white/50 dark:bg-dark-800/50 backdrop-blur-md hover:transform hover:scale-105 transition-all duration-300">
                    <div class="flex-1 p-6 flex flex-col justify-between">
                      <div class="flex-1">
                        <div class="flex items-center">
                          <div class="flex-shrink-0 h-10 w-10">
                            <div class="flex items-center justify-center h-12 w-12 rounded-md bg-gradient-to-br from-indigo-500 to-purple-600 text-white">
                              <svg class="h-6 w-6 animate-target" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                              </svg>
                            </div>
                          </div>
                          <h3 class="ml-4 text-xl font-semibold text-gray-900 dark:text-gray-100">Exercices ciblés</h3>
                        </div>
                        <div class="mt-3 text-base text-gray-500 dark:text-gray-400">
                          <ul class="space-y-2">
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Par chapitre du programme
                            </li>
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Difficulté progressive
                            </li>
                            <li class="flex items-center">
                              <svg class="h-5 w-5 text-green-500 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                              </svg>
                              Méthodologie détaillée
                            </li>
                          </ul>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Boutons d'action pour desktop -->
                <div class="mt-10 hidden sm:flex justify-center space-x-6">
                  <div class="rounded-md shadow hover:transform hover:scale-105 transition-all duration-300">
                    <NuxtLink to="/register" class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-700 hover:to-purple-700 md:py-4 md:text-lg md:px-10 transition-all duration-300">
                      <span class="animate-bounce-right">Commence maintenant →</span>
                    </NuxtLink>
                  </div>
                  <div class="rounded-md hover:transform hover:scale-105 transition-all duration-300">
                    <NuxtLink to="/presentation" class="group relative w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-indigo-700 dark:text-indigo-300 bg-indigo-100 dark:bg-indigo-900 hover:bg-indigo-200 dark:hover:bg-indigo-800 md:py-4 md:text-lg md:px-10 transition-all duration-300">
                      <span class="absolute -top-2 right-0 bg-gradient-to-r from-red-500 to-pink-500 text-white text-xs px-2 py-1 rounded-full transform group-hover:scale-110 transition-transform duration-200 animate-pulse">Nouveau !</span>
                      Cours particuliers 👨‍🏫
                    </NuxtLink>
                  </div>
                </div>
              </main>
            </div>
          </div>
          <!-- Image de l'étudiant -->
          <div class="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
            <img class="h-64 w-full object-contain sm:h-96 md:h-[32rem] lg:w-full lg:h-[calc(100%+4rem)] lg:-mt-8 transform lg:scale-110 transition-transform duration-300 hover:scale-105" src="/flat_student.png" alt="Étudiant qui révise">
          </div>
        </div>

        <!-- Bouton pour remonter en haut de page (mobile) -->
        <button 
          @click="scrollToTop"
          class="fixed bottom-6 right-6 sm:hidden bg-indigo-600 text-white p-3 rounded-full shadow-lg hover:bg-indigo-700 transition-all duration-200 z-50"
          :class="{ 'translate-y-0 opacity-100': showScrollTop, 'translate-y-16 opacity-0': !showScrollTop }"
        >
          <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
          </svg>
        </button>
      </div>
    </template>
  </div>
</template> 

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRuntimeConfig } from '#app'

const config = useRuntimeConfig()
const isLoggedIn = ref(false)
const user = ref(null)
const stats = ref({
  global: 0,
  completedExercises: 0,
  totalExercises: 0,
  totalHours: 0,
  masteredTopics: 0,
  totalTopics: 0
})
const showScrollTop = ref(false)

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

// Fonction pour remonter en haut de la page
function scrollToTop() {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

// Gestion de l'affichage du bouton de scroll
function handleScroll() {
  showScrollTop.value = window.scrollY > 300
}

onMounted(async () => {
  try {
    // Vérifier si l'utilisateur est connecté
    const authResponse = await useFetch('/api/auth/me', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    if (authResponse.data.value?.user) {
      isLoggedIn.value = true
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

    // Initialiser le gestionnaire de scroll
    window.addEventListener('scroll', handleScroll)
  } catch (error) {
    console.error('Erreur lors du chargement des données:', error)
  }
})

onUnmounted(() => {
  // Nettoyer le gestionnaire de scroll
  window.removeEventListener('scroll', handleScroll)
})
</script> 

<style scoped>
.animate-fade-in {
  animation: fadeIn 1s ease-in;
}

.animate-slide-up {
  animation: slideUp 0.8s ease-out;
}

.animate-bounce-soft {
  animation: bounceSoft 2s infinite;
}

.animate-bounce-right {
  animation: bounceRight 1s infinite;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideUp {
  from {
    transform: translateY(20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes bounceSoft {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-5px);
  }
}

@keyframes bounceRight {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(5px);
  }
}

/* Effet de hover élaboré pour les cartes */
.feature-card {
  transition: all 0.3s ease;
  backdrop-filter: blur(8px);
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(79, 70, 229, 0.1);
  background: rgba(255, 255, 255, 0.7);
}

:root.dark .feature-card:hover {
  background: rgba(17, 24, 39, 0.7);
}

/* Effet de gradient animé pour les boutons */
.gradient-hover {
  background-size: 200% auto;
  transition: all 0.3s ease;
}

.gradient-hover:hover {
  background-position: right center;
}

@keyframes chart {
  0% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-3px) scale(1.05);
  }
  100% {
    transform: translateY(0);
  }
}

@keyframes target {
  0% {
    transform: rotate(0deg);
  }
  25% {
    transform: rotate(-5deg);
  }
  75% {
    transform: rotate(5deg);
  }
  100% {
    transform: rotate(0deg);
  }
}

.animate-chart {
  animation: chart 3s ease-in-out infinite;
}

.animate-target {
  animation: target 2s ease-in-out infinite;
}
</style> 