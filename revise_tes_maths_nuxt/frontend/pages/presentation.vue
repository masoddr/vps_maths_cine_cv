<template>
  <div class="bg-white dark:bg-dark-800">
    <!-- Section Hero -->
    <div id="hero" class="relative overflow-hidden">
      <div class="max-w-7xl mx-auto">
        <div class="relative z-10 pb-8 sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32">
          <main class="mt-10 mx-auto max-w-7xl px-4 sm:mt-12 sm:px-6 md:mt-16 lg:mt-20 lg:px-8 xl:mt-28">
            <div class="sm:text-center lg:text-left">
              <h1 class="text-4xl tracking-tight font-extrabold text-gray-900 dark:text-gray-100 sm:text-5xl md:text-6xl">
                <span class="block">Cours particuliers</span>
                <span class="block text-indigo-600 dark:text-indigo-400">de Mathématiques</span>
              </h1>
              <p class="mt-3 text-base text-gray-500 dark:text-gray-400 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
                Professeur expérimenté, je propose des cours particuliers adaptés à chaque élève, en présentiel ou en visio, pour une préparation optimale du baccalauréat.
              </p>
            </div>
          </main>
        </div>
      </div>
      <div class="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2 flex items-center justify-center">
        <div class="relative w-64 h-64 sm:w-72 sm:h-72 md:w-96 md:h-96">
          <img 
            class="absolute inset-0 w-full h-full object-cover rounded-full border-4 border-indigo-600 dark:border-indigo-400 shadow-xl" 
            src="/images/massyl.jpeg" 
            alt="Massyl - Professeur de mathématiques"
          >
          <div class="absolute -inset-4 bg-indigo-600/10 dark:bg-indigo-400/10 rounded-full blur-lg"></div>
        </div>
      </div>
    </div>

    <!-- Section À propos -->
    <div id="about" class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 gap-10 lg:grid-cols-2">
          <!-- Expérience professionnelle -->
          <div class="bg-white dark:bg-dark-800 rounded-lg shadow-lg p-6">
            <div class="flex items-center mb-4">
              <div class="flex-shrink-0">
                <svg class="h-8 w-8 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" />
                </svg>
              </div>
              <h3 class="ml-4 text-xl font-bold text-gray-900 dark:text-gray-100">Ingénieur Systèmes Spatiaux</h3>
            </div>
            <p class="text-gray-600 dark:text-gray-400 mb-4">
              Actuellement Ingénieur en systèmes spatiaux et simulation, je travaille sur des projets de pointe en télécommunications par satellites et cryptographie quantique.
            </p>
            <ul class="space-y-2 text-gray-600 dark:text-gray-400">
              <li class="flex items-start">
                <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Expert en modélisation scientifique et simulation complexe
              </li>
              <li class="flex items-start">
                <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Maîtrise des mathématiques appliquées au domaine spatial
              </li>
            </ul>
            <div class="mt-6 pt-6 border-t border-gray-200 dark:border-gray-700">
              <h4 class="text-lg font-semibold text-gray-900 dark:text-gray-100 mb-3">Formation académique</h4>
              <ul class="space-y-2 text-gray-600 dark:text-gray-400">
                <li class="flex items-start">
                  <svg class="h-5 w-5 text-indigo-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  Master en Ingénierie Spatiale - Observatoire de Paris
                </li>
                <li class="flex items-start">
                  <svg class="h-5 w-5 text-indigo-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  Maîtrise en Physique Fondamentale
                </li>
                <li class="flex items-start">
                  <svg class="h-5 w-5 text-indigo-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  Licence en Mathématiques
                </li>
                <li class="flex items-start">
                  <svg class="h-5 w-5 text-indigo-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                  </svg>
                  Classes Préparatoires MPSI/MP*
                </li>
              </ul>
            </div>
          </div>

          <!-- Expérience d'enseignement -->
          <div class="bg-white dark:bg-dark-800 rounded-lg shadow-lg p-6">
            <div class="flex items-center mb-4">
              <div class="flex-shrink-0">
                <svg class="h-8 w-8 text-indigo-600 dark:text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
                </svg>
              </div>
              <h3 class="ml-4 text-xl font-bold text-gray-900 dark:text-gray-100">9+ ans d'expérience en enseignement</h3>
            </div>
            <p class="text-gray-600 dark:text-gray-400 mb-4">
              Depuis 2015, j'accompagne avec succès des élèves de la 5ᵉ à Bac +2, avec une approche pédagogique éprouvée et des résultats remarquables.
            </p>
            <ul class="space-y-2 text-gray-600 dark:text-gray-400">
              <li class="flex items-start">
                <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Plus de 23 élèves accompagnés avec succès
              </li>
              <li class="flex items-start">
                <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Excellents résultats aux examens (Brevet, Bac)
              </li>
              <li class="flex items-start">
                <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                </svg>
                Approche personnalisée et gain en confiance
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Services -->
    <div id="services" class="py-12 bg-gray-50 dark:bg-dark-900">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:text-center">
          <h2 class="text-base text-indigo-600 dark:text-indigo-400 font-semibold tracking-wide uppercase">Mes Services</h2>
          <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl">
            Une approche personnalisée et complète
          </p>
          <p class="mt-4 max-w-2xl text-xl text-gray-500 dark:text-gray-400 lg:mx-auto">
            Des solutions adaptées à chaque élève pour une progression optimale en mathématiques.
          </p>
        </div>

        <div class="mt-10">
          <div class="space-y-10 md:space-y-0 md:grid md:grid-cols-2 md:gap-x-8 md:gap-y-10">
            <!-- Cours à domicile -->
            <div class="relative bg-white dark:bg-dark-800 p-6 rounded-lg shadow-lg">
              <div class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 dark:bg-indigo-600 text-white">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
                </svg>
              </div>
              <div class="ml-16">
                <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">Cours à domicile</h3>
                <div class="mt-2 text-base text-gray-500 dark:text-gray-400 space-y-4">
                  <p>Cours particuliers dans un environnement familier et confortable.</p>
                  <ul class="space-y-2">
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Déplacement sur Toulouse et sa proche banlieue
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Matériel pédagogique fourni
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Exercices personnalisés et supports de cours
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Cours en visio -->
            <div class="relative bg-white dark:bg-dark-800 p-6 rounded-lg shadow-lg">
              <div class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 dark:bg-indigo-600 text-white">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14M5 18h8a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v8a2 2 0 002 2z" />
                </svg>
              </div>
              <div class="ml-16">
                <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">Cours en visio</h3>
                <div class="mt-2 text-base text-gray-500 dark:text-gray-400 space-y-4">
                  <p>Séances en ligne interactives avec des outils numériques performants.</p>
                  <ul class="space-y-2">
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Tableau blanc interactif
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Partage d'écran et documents en temps réel
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Enregistrement possible des séances
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Préparation aux examens -->
            <div class="relative bg-white dark:bg-dark-800 p-6 rounded-lg shadow-lg">
              <div class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 dark:bg-indigo-600 text-white">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <div class="ml-16">
                <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">Préparation aux examens</h3>
                <div class="mt-2 text-base text-gray-500 dark:text-gray-400 space-y-4">
                  <p>Programme spécifique pour réussir vos examens.</p>
                  <ul class="space-y-2">
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Entraînement avec des sujets types
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Méthodologie et gestion du temps
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Simulations d'examens
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- Suivi personnalisé -->
            <div class="relative bg-white dark:bg-dark-800 p-6 rounded-lg shadow-lg">
              <div class="absolute flex items-center justify-center h-12 w-12 rounded-md bg-indigo-500 dark:bg-indigo-600 text-white">
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                </svg>
              </div>
              <div class="ml-16">
                <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">Suivi personnalisé</h3>
                <div class="mt-2 text-base text-gray-500 dark:text-gray-400 space-y-4">
                  <p>Un accompagnement continu pour une progression optimale.</p>
                  <ul class="space-y-2">
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Bilan régulier des progrès
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Adaptation continue du programme
                    </li>
                    <li class="flex items-start">
                      <svg class="h-5 w-5 text-green-500 mr-2 mt-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                      </svg>
                      Communication régulière avec les parents
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Tarifs -->
    <div id="pricing" class="py-16 bg-white dark:bg-dark-800 overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="lg:grid lg:grid-cols-2 lg:gap-8">
          <div>
            <h2 class="text-base text-indigo-600 dark:text-indigo-400 font-semibold tracking-wide uppercase">Ma Méthode</h2>
            <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl">
              Un accompagnement sur mesure
            </p>
            <div class="mt-8 space-y-6 text-gray-500 dark:text-gray-400">
              <p class="text-lg">
                Mon approche pédagogique s'adapte à chaque élève, en identifiant ses points forts et ses difficultés pour construire un programme personnalisé.
              </p>
              <ul class="mt-8 space-y-4">
                <li class="flex items-center">
                  <svg class="h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <span class="ml-3">Évaluation initiale des besoins</span>
                </li>
                <li class="flex items-center">
                  <svg class="h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <span class="ml-3">Programme sur mesure</span>
                </li>
                <li class="flex items-center">
                  <svg class="h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                  <span class="ml-3">Suivi régulier des progrès</span>
                </li>
              </ul>
            </div>
          </div>
          <div class="mt-12 lg:mt-0">
            <h2 class="text-base text-indigo-600 dark:text-indigo-400 font-semibold tracking-wide uppercase">Tarifs</h2>
            <div class="mt-8 space-y-6">
              <!-- Cours individuels -->
              <div class="bg-gray-50 dark:bg-dark-900 rounded-lg p-6">
                <div class="flex items-center">
                  <svg class="h-8 w-8 text-indigo-600 dark:text-indigo-400 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
                  </svg>
                  <h3 class="text-2xl font-bold text-gray-900 dark:text-gray-100">Cours individuels</h3>
                </div>
                <div class="mt-6 grid grid-cols-1 gap-6 sm:grid-cols-2">
                  <!-- Cours à domicile -->
                  <div class="border-2 border-indigo-100 dark:border-indigo-900 rounded-lg p-4">
                    <h4 class="text-lg font-semibold text-gray-900 dark:text-gray-100">À domicile (Toulouse)</h4>
                    <div class="mt-2">
                      <div class="flex items-baseline">
                        <span class="text-2xl font-bold text-gray-900 dark:text-gray-100">60€</span>
                        <span class="ml-2 text-gray-500 dark:text-gray-400">/heure</span>
                      </div>
                      <p class="text-sm text-green-600 dark:text-green-400 mt-1">Soit 30€/h après avantage fiscal</p>
                    </div>
                  </div>
                  <!-- Cours en visio -->
                  <div class="border-2 border-indigo-100 dark:border-indigo-900 rounded-lg p-4">
                    <h4 class="text-lg font-semibold text-gray-900 dark:text-gray-100">En visio</h4>
                    <div class="mt-2">
                      <div class="flex items-baseline">
                        <span class="text-2xl font-bold text-gray-900 dark:text-gray-100">50€</span>
                        <span class="ml-2 text-gray-500 dark:text-gray-400">/heure</span>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="mt-6 p-4 bg-green-50 dark:bg-green-900 rounded-lg border-2 border-green-200 dark:border-green-700">
                  <h4 class="text-xl font-bold text-green-700 dark:text-green-300">
                    <span class="flex items-center">
                      <svg class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      Avantage fiscal pour les cours à domicile
                    </span>
                  </h4>
                  <div class="mt-3 text-sm text-green-600 dark:text-green-400">
                    <p class="font-medium">Comment ça marche ?</p>
                    <ul class="mt-2 space-y-2 list-disc list-inside">
                      <li>Pour les cours à domicile uniquement, grâce à l'Avance Immédiate du CESU, bénéficiez <span class="font-semibold">immédiatement</span> du crédit d'impôt de 50%</li>
                      <li>Vous ne payez que 30€/heure pour les cours à domicile, l'État prend en charge les 30€ restants</li>
                      <li>Aucune avance de frais, la réduction est immédiate</li>
                    </ul>
                    <a href="https://www.urssaf.fr/portail/home/particulier-employeur/beneficier-davantages/lavance-immediate-de-credit-dimp.html" 
                       target="_blank"
                       rel="noopener noreferrer" 
                       class="mt-4 inline-flex items-center text-sm font-medium text-green-700 dark:text-green-300 hover:underline">
                      En savoir plus sur l'Avance Immédiate
                      <svg class="ml-1 w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                      </svg>
                    </a>
                  </div>
                </div>
              </div>

              <!-- Tarifs de groupe -->
              <div class="bg-indigo-50 dark:bg-indigo-900/50 rounded-lg p-6 border-2 border-indigo-200 dark:border-indigo-700">
                <div class="flex items-center">
                  <svg class="h-8 w-8 text-indigo-600 dark:text-indigo-400 mr-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
                  </svg>
                  <h3 class="text-2xl font-bold text-indigo-900 dark:text-indigo-100">Tarifs pour petits groupes</h3>
                </div>
                <p class="mt-2 text-indigo-600 dark:text-indigo-300">Profitez de tarifs avantageux en vous regroupant avec d'autres élèves !</p>
                
                <div class="mt-4 space-y-4">
                  <div class="flex items-baseline justify-between border-b border-indigo-200 dark:border-indigo-700 pb-2">
                    <span class="text-indigo-700 dark:text-indigo-300">2 élèves</span>
                    <div class="text-right">
                      <span class="text-xl font-bold text-indigo-900 dark:text-indigo-100">40€</span>
                      <span class="text-indigo-600 dark:text-indigo-400">/heure/élève</span>
                      <p class="text-sm text-indigo-600 dark:text-indigo-400">Soit 20€/h après avantage fiscal</p>
                    </div>
                  </div>
                  
                  <div class="flex items-baseline justify-between border-b border-indigo-200 dark:border-indigo-700 pb-2">
                    <span class="text-indigo-700 dark:text-indigo-300">3 élèves</span>
                    <div class="text-right">
                      <span class="text-xl font-bold text-indigo-900 dark:text-indigo-100">35€</span>
                      <span class="text-indigo-600 dark:text-indigo-400">/heure/élève</span>
                      <p class="text-sm text-indigo-600 dark:text-indigo-400">Soit 17,50€/h après avantage fiscal</p>
                    </div>
                  </div>
                </div>

                <div class="mt-4 p-4 bg-white/50 dark:bg-black/20 rounded-lg">
                  <p class="text-sm text-indigo-700 dark:text-indigo-300">
                    <span class="font-semibold">💡 Astuce :</span> Regroupez-vous avec des camarades de classe pour bénéficier de tarifs réduits tout en gardant une attention personnalisée. L'avantage fiscal CESU s'applique également aux cours en groupe !
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Témoignages -->
    <div id="testimonials" class="py-16 bg-white dark:bg-dark-800">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center">
          <h2 class="text-base text-indigo-600 dark:text-indigo-400 font-semibold tracking-wide uppercase">Témoignages</h2>
          <p class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl">
            La réussite de mes élèves
          </p>
          <p class="mt-4 max-w-2xl mx-auto text-xl text-gray-500 dark:text-gray-400">
            Découvrez les retours d'expérience de mes élèves et de leurs parents
          </p>
        </div>
        
        <div class="mt-12 space-y-8 md:grid md:grid-cols-3 md:gap-12 md:space-y-0">
          <!-- Témoignage 1 -->
          <div class="bg-gradient-to-br from-white to-indigo-50 dark:from-dark-800 dark:to-indigo-900/30 rounded-xl p-8 relative transform hover:scale-105 transition-all duration-200 shadow-lg">
            <div class="absolute -top-4 -left-4">
              <span class="text-6xl text-indigo-200 dark:text-indigo-800">"</span>
            </div>
            <div class="relative">
              <p class="text-lg text-gray-600 dark:text-gray-300 mb-6">
                Grâce à Massyl, j'ai repris confiance en moi en maths. Ses explications sont claires et il s'adapte vraiment à mon rythme. J'ai progressé de 8 à 15 en quelques mois !
              </p>
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <img class="h-12 w-12 rounded-full ring-2 ring-indigo-500" src="/images/default-teacher.svg" alt="Sarah" />
                </div>
                <div class="ml-4">
                  <div class="text-base font-medium text-gray-900 dark:text-gray-100">Sarah L.</div>
                  <div class="text-sm text-indigo-600 dark:text-indigo-400">Terminale, mention Bien au bac</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Témoignage 2 -->
          <div class="bg-gradient-to-br from-white to-indigo-50 dark:from-dark-800 dark:to-indigo-900/30 rounded-xl p-8 relative transform hover:scale-105 transition-all duration-200 shadow-lg">
            <div class="absolute -top-4 -left-4">
              <span class="text-6xl text-indigo-200 dark:text-indigo-800">"</span>
            </div>
            <div class="relative">
              <p class="text-lg text-gray-600 dark:text-gray-300 mb-6">
                Un prof passionné qui sait transmettre son amour des maths. Les cours en visio sont super pratiques et tout aussi efficaces qu'en présentiel.
              </p>
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <img class="h-12 w-12 rounded-full ring-2 ring-indigo-500" src="/images/default-teacher.svg" alt="Thomas" />
                </div>
                <div class="ml-4">
                  <div class="text-base font-medium text-gray-900 dark:text-gray-100">Thomas M.</div>
                  <div class="text-sm text-indigo-600 dark:text-indigo-400">Première, 17 en maths</div>
                </div>
              </div>
            </div>
          </div>

          <!-- Témoignage 3 (Parent) -->
          <div class="bg-gradient-to-br from-white to-indigo-50 dark:from-dark-800 dark:to-indigo-900/30 rounded-xl p-8 relative transform hover:scale-105 transition-all duration-200 shadow-lg">
            <div class="absolute -top-4 -left-4">
              <span class="text-6xl text-indigo-200 dark:text-indigo-800">"</span>
            </div>
            <div class="relative">
              <p class="text-lg text-gray-600 dark:text-gray-300 mb-6">
                En tant que parent, j'apprécie particulièrement le suivi détaillé et les retours réguliers sur les progrès de ma fille. Les résultats sont là !
              </p>
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <img class="h-12 w-12 rounded-full ring-2 ring-indigo-500" src="/images/default-teacher.svg" alt="Marie" />
                </div>
                <div class="ml-4">
                  <div class="text-base font-medium text-gray-900 dark:text-gray-100">Marie P.</div>
                  <div class="text-sm text-indigo-600 dark:text-indigo-400">Parent d'élève de Terminale</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section Contact -->
    <div id="contact" class="bg-gray-50 dark:bg-dark-900">
      <div class="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:py-24 lg:px-8">
        <div class="lg:grid lg:grid-cols-2 lg:gap-8 lg:items-center">
          <!-- Colonne de gauche -->
          <div>
            <h2 class="text-3xl font-extrabold tracking-tight text-gray-900 dark:text-gray-100 sm:text-4xl">
              Commencez votre réussite maintenant
            </h2>
            <p class="mt-4 text-lg text-gray-500 dark:text-gray-400">
              Contactez-moi pour évaluer ensemble vos besoins et définir un programme personnalisé.
            </p>
            
            <div class="mt-8 space-y-4">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <p class="ml-3 text-lg text-gray-500 dark:text-gray-400">
                  Réponse garantie sous 24h
                </p>
              </div>
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <p class="ml-3 text-lg text-gray-500 dark:text-gray-400">
                  Programme personnalisé adapté à vos objectifs
                </p>
              </div>
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-green-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <p class="ml-3 text-lg text-gray-500 dark:text-gray-400">
                  Horaires flexibles 7j/7
                </p>
              </div>
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <svg class="h-6 w-6 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                  </svg>
                </div>
                <p class="ml-3 text-lg text-gray-500 dark:text-gray-400">
                  Vous pouvez aussi m'écrire directement à <a href="mailto:contact@revise-tes-maths.fr" class="text-indigo-600 hover:text-indigo-500 dark:text-indigo-400">contact@revise-tes-maths.fr</a>
                </p>
              </div>
            </div>
          </div>

          <!-- Colonne de droite - Formulaire de contact -->
          <div class="mt-12 lg:mt-0">
            <div class="bg-white dark:bg-dark-800 rounded-lg shadow-xl p-8">
              <form id="contact-form" @submit.prevent="handleSubmit" class="space-y-6">
                <div>
                  <label for="name" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                    Nom complet
                  </label>
                  <div class="mt-1">
                    <input 
                      type="text" 
                      name="name" 
                      id="name" 
                      v-model="contactForm.name"
                      required
                      class="block w-full rounded-md border-gray-300 dark:border-gray-700 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 dark:bg-dark-700 dark:text-gray-100" 
                    />
                  </div>
                </div>

                <div>
                  <label for="email" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                    Email
                  </label>
                  <div class="mt-1">
                    <input 
                      type="email" 
                      name="email" 
                      id="email" 
                      v-model="contactForm.email"
                      required
                      class="block w-full rounded-md border-gray-300 dark:border-gray-700 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 dark:bg-dark-700 dark:text-gray-100" 
                    />
                  </div>
                </div>

                <div>
                  <label for="phone" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                    Téléphone
                  </label>
                  <div class="mt-1">
                    <input 
                      type="tel" 
                      name="phone" 
                      id="phone" 
                      v-model="contactForm.phone"
                      class="block w-full rounded-md border-gray-300 dark:border-gray-700 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 dark:bg-dark-700 dark:text-gray-100" 
                    />
                  </div>
                </div>

                <div>
                  <label for="message" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                    Message
                  </label>
                  <div class="mt-1">
                    <textarea 
                      id="message" 
                      name="message" 
                      rows="4" 
                      v-model="contactForm.message"
                      required
                      class="block w-full rounded-md border-gray-300 dark:border-gray-700 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 dark:bg-dark-700 dark:text-gray-100"
                    ></textarea>
                  </div>
                </div>

                <!-- Message d'erreur -->
                <div v-if="contactError" class="rounded-md bg-red-50 dark:bg-red-900 p-4">
                  <div class="flex">
                    <div class="flex-shrink-0">
                      <svg class="h-5 w-5 text-red-400 dark:text-red-300" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
                      </svg>
                    </div>
                    <div class="ml-3">
                      <h3 class="text-sm font-medium text-red-800 dark:text-red-200">
                        {{ contactError }}
                      </h3>
                    </div>
                  </div>
                </div>

                <!-- Message de succès -->
                <div v-if="contactSuccess" class="rounded-md bg-green-50 dark:bg-green-900 p-4">
                  <div class="flex">
                    <div class="flex-shrink-0">
                      <svg class="h-5 w-5 text-green-400 dark:text-green-300" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                      </svg>
                    </div>
                    <div class="ml-3">
                      <h3 class="text-sm font-medium text-green-800 dark:text-green-200">
                        {{ contactSuccess }}
                      </h3>
                    </div>
                  </div>
                </div>

                <div>
                  <button 
                    type="submit" 
                    class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-colors duration-200"
                    :disabled="isSubmitting"
                  >
                    <svg v-if="isSubmitting" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8a8 8 0 01-8 8z"></path>
                    </svg>
                    {{ isSubmitting ? 'Envoi en cours...' : 'Réserver ma séance' }}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section FAQ -->
    <div id="faq" class="bg-white dark:bg-dark-800">
      <div class="max-w-7xl mx-auto py-16 px-4 sm:px-6 lg:py-20 lg:px-8">
        <div class="lg:grid lg:grid-cols-3 lg:gap-8">
          <div>
            <h2 class="text-3xl font-extrabold text-gray-900 dark:text-gray-100">
              Questions fréquentes
            </h2>
            <p class="mt-4 text-lg text-gray-500 dark:text-gray-400">
              Vous ne trouvez pas la réponse que vous cherchez ?
              <a href="mailto:contact@revise-tes-maths.fr" class="font-medium text-indigo-600 hover:text-indigo-500 dark:text-indigo-400">
                Contactez-moi directement
              </a>
            </p>
          </div>
          <div class="mt-12 lg:mt-0 lg:col-span-2">
            <dl class="space-y-12">
              <div>
                <dt class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">
                  Comment se déroule la première séance ?
                </dt>
                <dd class="mt-2 text-base text-gray-500 dark:text-gray-400">
                  La première séance permet d'évaluer le niveau, identifier les points à améliorer et définir ensemble un programme personnalisé. C'est aussi l'occasion de faire connaissance et de s'assurer que le courant passe bien.
                </dd>
              </div>

              <div>
                <dt class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">
                  Les cours en visio sont-ils aussi efficaces ?
                </dt>
                <dd class="mt-2 text-base text-gray-500 dark:text-gray-400">
                  Absolument ! J'utilise des outils numériques performants (tableau blanc interactif, partage d'écran) qui permettent une interaction aussi fluide qu'en présentiel. Certains élèves préfèrent même ce format qui leur permet de revoir les séances enregistrées.
                </dd>
              </div>

              <div>
                <dt class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">
                  Comment fonctionne l'avantage fiscal ?
                </dt>
                <dd class="mt-2 text-base text-gray-500 dark:text-gray-400">
                  Pour les cours à domicile uniquement, grâce au système CESU et à l'Avance Immédiate, vous ne payez que 50% du tarif. Le crédit d'impôt est appliqué directement, sans attente. Par exemple, pour un cours à domicile à 60€, vous ne payez que 30€, l'État prenant en charge les 30€ restants. Cette réduction ne s'applique pas aux cours en visio.
                </dd>
              </div>
            </dl>
          </div>
        </div>
      </div>
    </div>

    <!-- Bouton WhatsApp flottant -->
    <a href="https://wa.me/+33616635187" 
       target="_blank" 
       rel="noopener noreferrer" 
       class="fixed bottom-8 right-8 bg-green-500 text-white p-4 rounded-full shadow-lg hover:bg-green-600 transition-colors duration-200 z-50">
      <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
        <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.579-.579-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/>
      </svg>
    </a>

    <!-- Bouton CTA flottant -->
    <div class="fixed bottom-8 left-8 z-50">
      <button 
        @click="scrollToContact"
        class="group bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-full shadow-lg flex items-center space-x-2 transform hover:scale-105 transition-all duration-200"
      >
        <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
        <span>Réserver un cours</span>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// État du formulaire de contact
const contactForm = ref({
  name: '',
  email: '',
  phone: '',
  message: ''
})
const contactError = ref('')
const contactSuccess = ref('')
const isSubmitting = ref(false)

// Gestion de la soumission du formulaire
async function handleSubmit() {
  contactError.value = ''
  contactSuccess.value = ''
  isSubmitting.value = true

  try {
    const response = await fetch('http://localhost:5000/api/contact', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(contactForm.value)
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || 'Une erreur est survenue')
    }

    contactSuccess.value = 'Message envoyé avec succès ! Je vous recontacterai dans les plus brefs délais.'
    // Réinitialiser le formulaire
    contactForm.value = {
      name: '',
      email: '',
      phone: '',
      message: ''
    }
  } catch (error) {
    contactError.value = error.message
  } finally {
    isSubmitting.value = false
  }
}

// Fonction de défilement vers le formulaire de contact
function scrollToContact() {
  const contactSection = document.getElementById('contact')
  if (contactSection) {
    contactSection.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    })
  }
}
</script>

<style scoped>
/* Styles pour les transitions de section */
.section-enter-active,
.section-leave-active {
  transition: opacity 0.5s ease;
}

.section-enter-from,
.section-leave-to {
  opacity: 0;
}

/* Amélioration de l'accessibilité au focus */
button:focus-visible {
  outline: 2px solid #6366f1;
  outline-offset: 2px;
}

/* Animation au survol */
.hover-effect {
  transition: transform 0.2s ease;
}

.hover-effect:hover {
  transform: translateY(-2px);
}
</style> 