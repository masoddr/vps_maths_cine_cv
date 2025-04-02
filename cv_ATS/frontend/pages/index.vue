<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-blue-50 dark:from-gray-950 dark:via-gray-900 dark:to-gray-950">
    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white/80 dark:bg-gray-950/90 backdrop-blur-sm border-b border-gray-100 dark:border-gray-800">
      <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
          <!-- Logo/Brand -->
          <div class="flex items-center">
            <a href="/" class="text-xl font-bold text-gray-900 dark:text-white">
              Optimise-ton-CV
            </a>
          </div>

          <!-- Navigation Items -->
          <div class="flex items-center space-x-4">
            <!-- Dark Mode Toggle -->
            <button 
              @click="toggleDarkMode"
              class="p-2 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors duration-200"
              :title="isDarkMode ? 'Passer en mode clair' : 'Passer en mode sombre'"
            >
              <!-- Sun icon for dark mode -->
              <svg 
                v-if="isDarkMode"
                class="w-5 h-5 text-gray-600" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path 
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  stroke-width="2" 
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
                />
              </svg>
              <!-- Moon icon for light mode -->
              <svg 
                v-else
                class="w-5 h-5 text-gray-600" 
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path 
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  stroke-width="2" 
                  d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </nav>

    <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Hero Section -->
      <div class="h-screen flex flex-col justify-center py-16 md:py-20 dark:text-white">
        <div class="text-center flex-grow flex flex-col justify-center">
          <p class="text-xl mb-8">
            Analysez et améliorez instantanément votre CV pour les recruteurs et les ATS.
            Simple, rapide et gratuit.
          </p>

          <h1 class="text-4xl md:text-7xl font-bold mb-8 text-gray-900 dark:text-white">
            Optimisez votre CV avec
            <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              l'IA
            </span>
          </h1>

          <div class="inline-block px-4 py-2 bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm border border-gray-100 dark:border-gray-700 rounded-full font-medium text-gray-600 dark:text-gray-300 mb-8">
            ✨ 100% Gratuit - Aucune inscription requise
          </div>

          <!-- CTA Button -->
          <div>
            <button
              @click="scrollToAnalysis"
              class="group px-8 py-4 bg-gray-900 hover:bg-gray-800 text-white rounded-lg font-medium text-lg transition-all duration-300 flex items-center justify-center mx-auto"
            >
              <span class="flex items-center justify-center group-hover:translate-x-1 transition-transform duration-300">
                Commencer l'analyse
                <svg 
                  class="w-5 h-5 ml-2"
                  fill="none" 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path 
                    stroke-linecap="round" 
                    stroke-linejoin="round" 
                    stroke-width="2" 
                    d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3"
                  />
                </svg>
              </span>
            </button>
          </div>
        </div>

        <!-- Scroll Indicator -->
        <div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-bounce">
          <svg 
            class="w-6 h-6 text-gray-400" 
            fill="none" 
            stroke="currentColor" 
            viewBox="0 0 24 24"
          >
            <path 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M19 14l-7 7m0 0l-7-7m7 7V3"
            />
          </svg>
        </div>
      </div>

      <!-- How it works Section -->
      <div class="text-center flex flex-col justify-center py-16 md:py-20">
        <h2 class="text-4xl md:text-7xl font-bold mb-8 text-gray-900 dark:text-white">
          Comment ça 
          <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
            marche ?
          </span>
        </h2>
        
        <p class="text-lg md:text-xl text-gray-600 dark:text-gray-300 mb-16 max-w-2xl mx-auto leading-relaxed">
          Trois étapes simples pour optimiser votre CV et augmenter vos chances d'être sélectionné.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <!-- Step 1 -->
          <div 
            class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm p-8 rounded-2xl border border-gray-100 dark:border-gray-700 hover:border-blue-200 dark:hover:border-blue-500 transition-all duration-300 transform hover:-translate-y-1 cursor-pointer"
            @click="importMode = 'text'"
          >
            <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-6 mx-auto">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-center mb-4 text-gray-800 dark:text-white">1. Importez votre CV</h3>
            <p class="text-gray-600 dark:text-gray-300 text-center text-lg">
              Copiez-collez votre CV ou uploadez-le au format PDF
            </p>
          </div>

          <!-- Step 2 -->
          <div 
            class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm p-8 rounded-2xl border border-gray-100 dark:border-gray-700 hover:border-blue-200 dark:hover:border-blue-500 transition-all duration-300 transform hover:-translate-y-1 cursor-pointer"
            @click="$refs.jobOfferInput?.focus()"
          >
            <div class="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mb-6 mx-auto">
              <svg class="w-6 h-6 text-indigo-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-center mb-4 text-gray-800 dark:text-white">2. Ajoutez l'offre d'emploi (optionnel)</h3>
            <p class="text-gray-600 dark:text-gray-300 text-center text-lg">
              Copiez-collez le descriptif du poste pour une analyse personnalisée
            </p>
          </div>

          <!-- Step 3 -->
          <div class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm p-8 rounded-2xl border border-gray-100 dark:border-gray-700 hover:border-blue-200 dark:hover:border-blue-500 transition-all duration-300 transform hover:-translate-y-1">
            <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mb-6 mx-auto">
              <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 class="text-2xl font-bold text-center mb-4 text-gray-800 dark:text-white">3. Obtenez des conseils</h3>
            <p class="text-gray-600 dark:text-gray-300 text-center text-lg">
              Recevez une analyse détaillée et des suggestions d'amélioration
            </p>
          </div>
        </div>
      </div>

      <!-- Features Section -->
      <div class="text-center flex flex-col justify-center py-16 md:py-20">
        <h2 class="text-4xl md:text-7xl font-bold mb-8 text-gray-900 dark:text-white">
          Nos 
          <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
            avantages
          </span>
        </h2>
        
        <p class="text-lg md:text-xl text-gray-600 dark:text-gray-300 mb-16 max-w-2xl mx-auto leading-relaxed">
          Des fonctionnalités puissantes pour optimiser votre candidature.
        </p>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <div class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm p-8 rounded-2xl border border-gray-100 dark:border-gray-700 hover:border-blue-200 dark:hover:border-blue-500 transition-all duration-300 transform hover:-translate-y-1">
            <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-6 mx-auto">
              <span class="text-2xl">🎯</span>
            </div>
            <h3 class="text-2xl font-bold text-center mb-4 text-gray-800 dark:text-white">Analyse ATS</h3>
            <p class="text-gray-600 dark:text-gray-300 text-center text-lg">
              Vérification de la compatibilité avec les systèmes de recrutement
            </p>
          </div>

          <div class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm p-8 rounded-2xl border border-gray-100 dark:border-gray-700 hover:border-blue-200 dark:hover:border-blue-500 transition-all duration-300 transform hover:-translate-y-1">
            <div class="w-16 h-16 bg-indigo-100 rounded-full flex items-center justify-center mb-6 mx-auto">
              <span class="text-2xl">💡</span>
            </div>
            <h3 class="text-2xl font-bold text-center mb-4 text-gray-800 dark:text-white">Recommandations</h3>
            <p class="text-gray-600 dark:text-gray-300 text-center text-lg">
              Suggestions d'amélioration personnalisées
            </p>
          </div>

          <div class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm p-8 rounded-2xl border border-gray-100 dark:border-gray-700 hover:border-blue-200 dark:hover:border-blue-500 transition-all duration-300 transform hover:-translate-y-1">
            <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mb-6 mx-auto">
              <span class="text-2xl">⚡</span>
            </div>
            <h3 class="text-2xl font-bold text-center mb-4 text-gray-800 dark:text-white">Instantané</h3>
            <p class="text-gray-600 dark:text-gray-300 text-center text-lg">
              Résultats en quelques secondes
            </p>
          </div>
        </div>
      </div>

      <!-- Main Content with ID for scrolling -->
      <div id="analysis-section" class="scroll-mt-16">
        <div class="text-center flex flex-col justify-center py-16 md:py-20">
          <h2 class="text-4xl md:text-7xl font-bold mb-8 text-gray-900 dark:text-white">
            Analysez votre 
            <span class="bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
              CV
            </span>
          </h2>
          
          <p class="text-lg md:text-xl text-gray-600 dark:text-gray-300 mb-16 max-w-2xl mx-auto leading-relaxed">
            Importez votre CV et obtenez une analyse détaillée en quelques secondes.
          </p>
          
          <div class="bg-white/80 dark:bg-gray-900/80 backdrop-blur-sm p-8 rounded-2xl border border-gray-100 dark:border-gray-700 max-w-4xl mx-auto w-full">
            <!-- Import Tabs -->
            <div class="flex justify-center space-x-6 mb-12">
              <button 
                @click="importMode = 'text'"
                :class="[
                  'px-8 py-4 rounded-full text-base font-medium transition-all duration-300',
                  importMode === 'text' 
                    ? 'bg-gray-900 dark:bg-blue-600 text-white shadow-lg'
                    : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-700'
                ]"
              >
                Copier-coller
              </button>
              <button 
                @click="importMode = 'file'"
                :class="[
                  'px-8 py-4 rounded-full text-base font-medium transition-all duration-300',
                  importMode === 'file' 
                    ? 'bg-gray-900 dark:bg-blue-600 text-white shadow-lg'
                    : 'bg-white dark:bg-gray-800 text-gray-600 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 border border-gray-200 dark:border-gray-700'
                ]"
              >
                Upload PDF
              </button>
            </div>

            <!-- Import Content -->
            <div class="max-w-2xl mx-auto">
              <!-- Text Import -->
              <div v-if="importMode === 'text'" class="space-y-6">
                <textarea
                  v-model="cvContent"
                  placeholder="Collez le contenu de votre CV ici..."
                  class="w-full h-64 p-6 bg-white/90 dark:bg-gray-800/90 backdrop-blur-sm border border-gray-200 dark:border-gray-700 rounded-xl resize-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-base text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400"
                ></textarea>
              </div>

              <!-- File Import -->
              <div v-else class="space-y-6">
                <div 
                  class="border-2 border-dashed border-gray-300 rounded-xl p-12 text-center hover:border-blue-500 transition-colors cursor-pointer bg-white/90 dark:bg-gray-800/90 backdrop-blur-sm"
                  @click="$refs.fileInput.click()"
                  @dragover.prevent
                  @drop.prevent="handleFileDrop"
                >
                  <input
                    ref="fileInput"
                    type="file"
                    accept=".pdf"
                    class="hidden"
                    @change="handleFileSelect"
                  >
                  <div v-if="!selectedFile">
                    <svg class="w-16 h-16 mx-auto text-gray-400 mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                    </svg>
                    <p class="text-gray-600 dark:text-gray-300 text-lg">Glissez votre fichier PDF ici ou cliquez pour sélectionner</p>
                  </div>
                  <div v-else class="text-blue-600 font-medium">
                    {{ selectedFile.name }}
                  </div>
                </div>
              </div>

              <!-- Job Offer Input -->
              <div class="mt-8">
                <textarea
                  ref="jobOfferInput"
                  v-model="jobOffer"
                  placeholder="Pour une analyse plus pertinente, collez l'offre d'emploi ici (optionnel)..."
                  class="w-full h-32 p-6 bg-white/90 dark:bg-gray-800/90 backdrop-blur-sm border border-gray-200 dark:border-gray-700 rounded-xl resize-none focus:ring-2 focus:ring-blue-500 focus:border-transparent text-base text-gray-900 dark:text-white placeholder-gray-500 dark:placeholder-gray-400"
                ></textarea>
              </div>

              <!-- Analyze Button -->
              <div class="mt-8 flex justify-center">
                <button
                  @click="analyzeCV"
                  :disabled="!canAnalyze || isAnalyzing"
                  class="group relative px-8 py-4 bg-gray-900 dark:bg-blue-600 hover:bg-gray-800 dark:hover:bg-blue-700 text-white rounded-xl font-medium text-lg transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed min-w-[200px]"
                >
                  <!-- Badge Gratuit -->
                  <span class="absolute -top-2 -right-2 px-2 py-1 bg-green-500 text-white text-xs rounded-full">
                    Gratuit
                  </span>
                  
                  <!-- Loading State -->
                  <span v-if="isAnalyzing" class="flex items-center justify-center">
                    <svg class="animate-spin w-5 h-5 mr-3" fill="none" viewBox="0 0 24 24">
                      <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
                      <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                    </svg>
                    Analyse en cours...
                  </span>
                  
                  <!-- Normal State -->
                  <span v-else class="flex items-center justify-center group-hover:translate-x-1 transition-transform duration-300">
                    {{ jobOffer.trim() ? 'Analyser mon CV et sa compatibilité' : 'Analyser mon CV' }}
                    <svg class="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.5 4.5L21 12m0 0l-7.5 7.5M21 12H3" />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Results Section -->
      <div v-if="analysisResults" class="bg-white p-6 rounded-xl shadow-lg animate-fadeIn">
        <h2 class="text-2xl font-bold mb-6 text-gray-800">Résultats de l'analyse</h2>
        
        <!-- Format et Structure -->
        <div class="mb-8">
          <div class="flex items-center mb-4">
            <h3 class="text-xl font-semibold text-gray-700">Format et Structure</h3>
            <div class="relative ml-2 group">
              <span class="cursor-help text-gray-400 hover:text-gray-600">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-8-3a1 1 0 00-.867.5 1 1 0 11-1.731-1A3 3 0 0113 8a3.001 3.001 0 01-2 2.83V11a1 1 0 11-2 0v-1a1 1 0 011-1 1 1 0 100-2zm0 8a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" />
                </svg>
              </span>
              <div class="opacity-0 group-hover:opacity-100 transition-opacity bg-gray-800 text-sm text-white rounded-md absolute z-10 px-4 py-2 w-64 bottom-full left-1/2 transform -translate-x-1/2 -translate-y-2">
                La structure de votre CV est cruciale pour les systèmes ATS.
                <div class="absolute w-2 h-2 bg-gray-800 transform rotate-45 left-1/2 -translate-x-1/2 -bottom-1"></div>
              </div>
            </div>
          </div>

          <!-- Titre et Structure -->
          <div class="space-y-4">
            <div class="flex items-start">
              <div :class="analysisResults.hasTitle ? 'text-green-500' : 'text-red-500'" class="mr-2 mt-1">
                {{ analysisResults.hasTitle ? '✓' : '✗' }}
              </div>
              <div>
                <p class="font-medium">Titre</p>
                <p class="text-gray-600 text-sm">{{ analysisResults.titleFeedback }}</p>
              </div>
            </div>
            
            <div class="flex items-start">
              <div :class="analysisResults.hasGoodStructure ? 'text-green-500' : 'text-red-500'" class="mr-2 mt-1">
                {{ analysisResults.hasGoodStructure ? '✓' : '✗' }}
              </div>
              <div>
                <p class="font-medium">Structure</p>
                <p class="text-gray-600 text-sm">{{ analysisResults.structureFeedback }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Analyse des mots-clés -->
        <div class="mb-8">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-xl font-semibold text-gray-700">Analyse des mots-clés</h3>
            <div class="flex gap-2">
              <button
                @click="copyMissingKeywords"
                class="flex items-center px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition-colors duration-200"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
                </svg>
                Copier les mots-clés
              </button>
              <button
                @click="exportKeywords"
                class="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors duration-200"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                </svg>
                Exporter l'analyse
              </button>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <!-- Statistiques -->
            <div class="bg-white p-6 rounded-lg shadow">
              <h4 class="font-medium text-gray-800 mb-4">Vue d'ensemble</h4>
              <div class="grid grid-cols-3 gap-4">
                <div class="text-center p-4 bg-blue-50 rounded-lg">
                  <div class="text-2xl font-bold text-blue-600">{{ analysisResults.topKeywords.length }}</div>
                  <div class="text-sm text-gray-600">Total</div>
                </div>
                <div class="text-center p-4 bg-green-50 rounded-lg">
                  <div class="text-2xl font-bold text-green-600">{{ analysisResults.presentKeywords.length }}</div>
                  <div class="text-sm text-gray-600">Présents</div>
                </div>
                <div class="text-center p-4 bg-yellow-50 rounded-lg">
                  <div class="text-2xl font-bold text-yellow-600">{{ analysisResults.missingKeywords.length }}</div>
                  <div class="text-sm text-gray-600">Manquants</div>
                </div>
              </div>
            </div>

            <!-- Mots-clés manquants -->
            <div class="bg-yellow-50 p-6 rounded-lg">
              <h4 class="font-medium text-yellow-800 mb-4 flex items-center">
                <span class="text-xl mr-2">⚠️</span>
                Mots-clés manquants prioritaires
              </h4>
              <div class="flex flex-wrap gap-2">
                <span 
                  v-for="keyword in analysisResults.missingKeywords" 
                  :key="keyword"
                  class="bg-yellow-100 text-yellow-800 px-3 py-1 rounded-full text-sm flex items-center group relative"
                >
                  {{ keyword }}
                  <span class="ml-2 cursor-pointer hover:text-yellow-600" @click="copyKeyword(keyword)">📋</span>
                  <span class="opacity-0 group-hover:opacity-100 absolute -top-8 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white text-xs px-2 py-1 rounded whitespace-nowrap transition-opacity">
                    Cliquer pour copier
                  </span>
                </span>
              </div>
            </div>
          </div>

          <!-- Suggestions de formulation -->
          <div class="bg-white p-6 rounded-lg shadow">
            <h4 class="font-medium text-gray-800 mb-4">Suggestions de formulation alternatives</h4>
            <div class="space-y-4">
              <div 
                v-for="(alternatives, keyword) in analysisResults.keywordSuggestions" 
                :key="keyword"
                class="bg-gray-50 p-4 rounded-lg"
              >
                <div class="font-medium text-gray-700 mb-2">{{ keyword }}</div>
                <div class="flex flex-wrap gap-2">
                  <span 
                    v-for="(alt, index) in alternatives" 
                    :key="index"
                    class="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm cursor-pointer hover:bg-blue-200 transition-colors duration-200"
                    @click="copyKeyword(alt)"
                  >
                    {{ alt }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Scores d'évaluation -->
        <div class="mb-8">
          <h3 class="text-xl font-semibold text-gray-700 mb-4">Scores d'évaluation</h3>
          <div class="bg-white rounded-lg shadow overflow-hidden">
            <table class="min-w-full">
              <thead class="bg-gray-50">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Critère</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Note sur 5</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Barre de progression</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="(score, criterion) in analysisResults.scores" :key="criterion">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
                    {{ criterion.charAt(0).toUpperCase() + criterion.slice(1).replace('_', ' ') }}
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {{ score.toFixed(1) }}/5
                  </td>
                  <td class="px-6 py-4">
                    <div class="w-full bg-gray-200 rounded-full h-2.5">
                      <div class="bg-blue-600 h-2.5 rounded-full" 
                           :style="{ width: `${(score/5)*100}%` }"
                           :class="{
                             'bg-red-600': score < 2.5,
                             'bg-yellow-600': score >= 2.5 && score < 3.5,
                             'bg-green-600': score >= 3.5
                           }">
                      </div>
                    </div>
                  </td>
                </tr>
                <!-- Score total -->
                <tr class="bg-gray-50">
                  <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">Score Total</td>
                  <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900 font-bold">
                    {{ analysisResults.totalScore.toFixed(1) }}/20
                  </td>
                  <td class="px-6 py-4">
                    <div class="w-full bg-gray-200 rounded-full h-2.5">
                      <div class="bg-blue-600 h-2.5 rounded-full" 
                           :style="{ width: `${(analysisResults.totalScore/20)*100}%` }"
                           :class="{
                             'bg-red-600': analysisResults.totalScore < 10,
                             'bg-yellow-600': analysisResults.totalScore >= 10 && analysisResults.totalScore < 14,
                             'bg-green-600': analysisResults.totalScore >= 14
                           }">
                      </div>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Points forts et améliorations -->
        <div class="mb-8">
          <h3 class="text-xl font-semibold text-gray-700 mb-4">Analyse du contenu</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Points forts -->
            <div class="bg-green-50 p-6 rounded-lg">
              <h4 class="font-medium text-green-800 mb-4 flex items-center">
                <span class="text-xl mr-2">💪</span>
                Points forts
              </h4>
              <ul class="space-y-2">
                <li 
                  v-for="(point, index) in analysisResults.contentFeedback.points_forts" 
                  :key="index"
                  class="flex items-start"
                >
                  <span class="text-green-600 mr-2">✓</span>
                  <span class="text-green-900">{{ point }}</span>
                </li>
              </ul>
            </div>

            <!-- Points d'amélioration -->
            <div class="bg-yellow-50 p-6 rounded-lg">
              <h4 class="font-medium text-yellow-800 mb-4 flex items-center">
                <span class="text-xl mr-2">💡</span>
                Suggestions d'amélioration
              </h4>
              <ul class="space-y-2">
                <li 
                  v-for="(point, index) in analysisResults.contentFeedback.points_amelioration" 
                  :key="index"
                  class="flex items-start"
                >
                  <span class="text-yellow-600 mr-2">→</span>
                  <span class="text-yellow-900">{{ point }}</span>
                </li>
              </ul>
            </div>
          </div>
        </div>

        <!-- Section de compatibilité - affichée uniquement si une offre est fournie -->
        <div v-if="analysisResults.jobMatch && jobOffer" class="mb-8">
          <h3 class="text-xl font-semibold text-gray-700 mb-4">Compatibilité avec l'offre</h3>
          
          <!-- Scores de compatibilité -->
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            <div class="bg-white p-4 rounded-lg shadow">
              <div class="text-2xl font-bold text-blue-600 mb-1">{{ analysisResults.jobMatch.score }}%</div>
              <div class="text-sm text-gray-600">Score global</div>
            </div>
            <div class="bg-white p-4 rounded-lg shadow">
              <div class="text-2xl font-bold text-green-600 mb-1">{{ analysisResults.jobMatch.technicalMatch }}%</div>
              <div class="text-sm text-gray-600">Technique</div>
            </div>
            <div class="bg-white p-4 rounded-lg shadow">
              <div class="text-2xl font-bold text-purple-600 mb-1">{{ analysisResults.jobMatch.experienceMatch }}%</div>
              <div class="text-sm text-gray-600">Expérience</div>
            </div>
            <div class="bg-white p-4 rounded-lg shadow">
              <div class="text-2xl font-bold text-indigo-600 mb-1">{{ analysisResults.jobMatch.softSkillsMatch }}%</div>
              <div class="text-sm text-gray-600">Soft Skills</div>
            </div>
          </div>

          <!-- Analyse détaillée -->
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Points forts -->
            <div class="bg-green-50 p-6 rounded-lg">
              <h4 class="font-medium text-green-800 mb-4 flex items-center">
                <span class="text-xl mr-2">💪</span>
                Points forts
              </h4>
              <ul class="space-y-2">
                <li 
                  v-for="(strength, index) in analysisResults.jobMatch.strengths" 
                  :key="index"
                  class="flex items-start"
                >
                  <span class="text-green-600 mr-2">✓</span>
                  <span class="text-green-900">{{ strength }}</span>
                </li>
              </ul>
            </div>

            <!-- Écarts -->
            <div class="bg-yellow-50 p-6 rounded-lg">
              <h4 class="font-medium text-yellow-800 mb-4 flex items-center">
                <span class="text-xl mr-2">⚠️</span>
                Points à améliorer
              </h4>
              <ul class="space-y-2">
                <li 
                  v-for="(gap, index) in analysisResults.jobMatch.gaps" 
                  :key="index"
                  class="flex items-start"
                >
                  <span class="text-yellow-600 mr-2">→</span>
                  <span class="text-yellow-900">{{ gap }}</span>
                </li>
              </ul>
            </div>
          </div>

          <!-- Recommandations -->
          <div class="mt-6 bg-blue-50 p-6 rounded-lg">
            <h4 class="font-medium text-blue-800 mb-4 flex items-center">
              <span class="text-xl mr-2">💡</span>
              Recommandations pour cette offre
            </h4>
            <ul class="space-y-2">
              <li 
                v-for="(rec, index) in analysisResults.jobMatch.recommendations" 
                :key="index"
                class="flex items-start"
              >
                <span class="text-blue-600 mr-2">•</span>
                <span class="text-blue-900">{{ rec }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Built with section -->
      <div class="py-16 border-t">
        <div class="max-w-6xl mx-auto">
          <div class="text-center">
            <p class="text-sm text-gray-500 mb-6">DÉVELOPPÉ AVEC CES OUTILS</p>
            <div class="flex justify-center items-center space-x-12">
              <a 
                href="https://groq.com" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="text-gray-400 hover:text-gray-600 transition-colors duration-200"
              >
                <img src="/groq-logo.svg" alt="Groq" class="h-8">
              </a>
              <a 
                href="https://ai.meta.com/llama/" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="text-gray-400 hover:text-gray-600 transition-colors duration-200"
              >
                <img src="/llama-logo.svg" alt="LLaMA" class="h-8">
              </a>
              <a 
                href="https://nuxt.com" 
                target="_blank" 
                rel="noopener noreferrer" 
                class="text-gray-400 hover:text-gray-600 transition-colors duration-200"
              >
                <img src="/nuxt-logo.svg" alt="Nuxt" class="h-8">
              </a>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <footer class="bg-white dark:bg-gray-950 border-t border-gray-100 dark:border-gray-800 mt-16">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
            <!-- À propos -->
            <div>
              <h3 class="text-gray-900 dark:text-white font-semibold mb-4">À propos</h3>
              <p class="text-gray-600 dark:text-gray-400 text-sm">
                Optimise-ton-CV vous aide à optimiser votre CV pour les systèmes de suivi des candidatures (ATS) grâce à l'intelligence artificielle.
              </p>
            </div>
            
            <!-- Créateur -->
            <div>
              <h3 class="text-gray-900 dark:text-white font-semibold mb-4">Créateur</h3>
              <div class="text-gray-600 space-y-2">
                <p>Développé par Massyl OUADDOUR</p>
                <div class="flex space-x-4">
                  <a 
                    href="https://www.linkedin.com/in/massylouaddour/" 
                    target="_blank"
                    rel="noopener noreferrer" 
                    class="text-gray-600 hover:text-blue-600 transition-colors duration-200 flex items-center"
                  >
                    <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/>
                    </svg>
                    LinkedIn
                  </a>
                  <a 
                    href="https://masoddr.github.io/portfolio_massyl/" 
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-gray-600 hover:text-blue-600 transition-colors duration-200 flex items-center"
                  >
                    <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/>
                    </svg>
                    Portfolio
                  </a>
                </div>
              </div>
            </div>
            
            <!-- Liens utiles -->
            <div>
              <h3 class="text-gray-900 dark:text-white font-semibold mb-4">Liens utiles</h3>
              <ul class="space-y-2">
                <li>
                  <NuxtLink to="/guide" class="text-gray-600 hover:text-blue-600 text-sm transition-colors duration-200">
                    Guide d'utilisation
                  </NuxtLink>
                </li>
                <li>
                  <NuxtLink to="/faq" class="text-gray-600 hover:text-blue-600 text-sm transition-colors duration-200">
                    FAQ
                  </NuxtLink>
                </li>
              </ul>
            </div>
            
            <!-- Légal -->
            <div>
              <h3 class="text-gray-900 dark:text-white font-semibold mb-4">Informations légales</h3>
              <ul class="space-y-2">
                <li>
                  <NuxtLink to="/cgu" class="text-gray-600 hover:text-blue-600 text-sm transition-colors duration-200">
                    Conditions générales d'utilisation
                  </NuxtLink>
                </li>
                <li>
                  <NuxtLink to="/privacy" class="text-gray-600 hover:text-blue-600 text-sm transition-colors duration-200">
                    Politique de confidentialité
                  </NuxtLink>
                </li>
                <li>
                  <NuxtLink to="/legal" class="text-gray-600 hover:text-blue-600 text-sm transition-colors duration-200">
                    Mentions légales
                  </NuxtLink>
                </li>
              </ul>
            </div>
            
            <!-- Contact -->
            <div>
              <h3 class="text-gray-900 dark:text-white font-semibold mb-4">Contact</h3>
              <div class="space-y-2">
                <NuxtLink 
                  to="/contact" 
                  class="text-gray-600 hover:text-blue-600 transition-colors duration-200 block"
                >
                  Formulaire de contact
                </NuxtLink>
                <a 
                  href="mailto:ouaddour.massyl@gmail.com"
                  class="text-gray-600 hover:text-blue-600 transition-colors duration-200 block"
                >
                  ouaddour.massyl@gmail.com
                </a>
              </div>
            </div>
          </div>
          
          <!-- Copyright -->
          <div class="border-t border-gray-200 mt-8 pt-8 text-center">
            <p class="text-gray-500 text-sm">
              © {{ new Date().getFullYear() }} Optimise-ton-CV. Tous droits réservés.
            </p>
          </div>
        </div>
      </footer>
    </div>
    <Toast v-bind="toast" />
    <ProgressSteps 
      :steps="steps"
      :currentStep="currentStep"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Toast from '~/components/Toast.vue'
import ProgressSteps from '~/components/ProgressSteps.vue'

definePageMeta({
  layout: 'default'
})

const importMode = ref('text')
const cvContent = ref('')
const jobOffer = ref('')
const selectedFile = ref(null)
const fileInput = ref(null)
const isAnalyzing = ref(false)
const analysisResults = ref(null)

const toast = ref({
  isVisible: false,
  type: 'info',
  message: ''
})

const steps = [
  'Import du CV',
  'Analyse ATS',
  'Résultats'
]

const currentStep = ref(0)

const resetForm = () => {
  // Réinitialisation des champs
  cvContent.value = ''
  jobOffer.value = ''
  selectedFile.value = null
  analysisResults.value = null
  currentStep.value = 0

  // Réinitialisation du mode d'import si nécessaire
  importMode.value = 'text'

  // Notification à l'utilisateur
  showToast('info', 'Formulaire réinitialisé')
}

const canAnalyze = computed(() => {
  return importMode.value === 'text' ? cvContent.value.trim() !== '' : selectedFile.value !== null
})

const handleFileSelect = (event) => {
  const file = event.target.files[0]
  if (file && file.type === 'application/pdf') {
    selectedFile.value = file
  }
}

const handleFileDrop = (event) => {
  const file = event.dataTransfer.files[0]
  if (file && file.type === 'application/pdf') {
    selectedFile.value = file
  }
}

const analyzeCV = async () => {
  if (!canAnalyze.value) return
  
  console.log('Début de l\'analyse...')
  isAnalyzing.value = true
  currentStep.value = 1
  
  try {
    const formData = new FormData()
    
    if (importMode.value === 'file') {
      formData.append('file', selectedFile.value)
      console.log('Fichier ajouté:', selectedFile.value.name)
    } else {
      formData.append('cv_content', cvContent.value)
      console.log('Contenu CV ajouté, longueur:', cvContent.value.length)
    }
    
    if (jobOffer.value.trim()) {
      formData.append('job_offer', jobOffer.value)
      console.log('Offre d\'emploi ajoutée')
    }

    const response = await fetch('http://localhost:8000/analyze-cv', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Origin': window.location.origin
      },
      body: formData,
      credentials: 'include'
    })

    if (!response.ok) {
      const error = await response.json()
      if (response.status === 429) {
        // Extraction du temps d'attente du message d'erreur
        const waitTimeMatch = error.detail.match(/try again in (\d+)m(\d+\.\d+)s/)
        if (waitTimeMatch) {
          const minutes = parseInt(waitTimeMatch[1])
          const seconds = Math.round(parseFloat(waitTimeMatch[2]))
          showToast(
            'error',
            `Service temporairement indisponible. Veuillez réessayer dans ${minutes} minutes et ${seconds} secondes.`
          )
        } else {
          showToast(
            'error',
            'Service temporairement indisponible. Veuillez réessayer dans quelques minutes.'
          )
        }
        return
      }
      throw new Error(error.detail || 'Erreur lors de l\'analyse')
    }

    const data = await response.json()
    console.log('Réponse du backend:', data)
    analysisResults.value = data
    currentStep.value = 2
    showToast('success', 'Analyse terminée avec succès !')

  } catch (error) {
    console.error('Erreur détaillée:', error)
    showToast('error', error.message || 'Une erreur est survenue lors de l\'analyse. Veuillez réessayer.')
  } finally {
    isAnalyzing.value = false
    currentStep.value = 0
    console.log('Fin de l\'analyse')
  }
}

const exportOptimizedVersion = () => {
  if (!analysisResults.value?.optimizedVersion) return

  // Création du blob avec le contenu
  const blob = new Blob([analysisResults.value.optimizedVersion], { type: 'text/plain' })
  
  // Création de l'URL du blob
  const url = window.URL.createObjectURL(blob)
  
  // Création d'un lien temporaire pour le téléchargement
  const link = document.createElement('a')
  link.href = url
  link.download = 'cv_optimise.txt'
  
  // Ajout du lien au document et simulation du clic
  document.body.appendChild(link)
  link.click()
  
  // Nettoyage
  document.body.removeChild(link)
  window.URL.revokeObjectURL(url)
}

const exportKeywords = () => {
  if (!analysisResults.value) return

  const content = `ANALYSE DÉTAILLÉE DES MOTS-CLÉS DE VOTRE CV

STATISTIQUES
-----------
Total mots-clés importants : ${analysisResults.value.topKeywords.length}
Mots-clés présents : ${analysisResults.value.presentKeywords.length}
Mots-clés manquants : ${analysisResults.value.missingKeywords.length}

MOTS-CLÉS PRÉSENTS
-----------------
${analysisResults.value.presentKeywords.join(', ')}

MOTS-CLÉS MANQUANTS
-----------------
${analysisResults.value.missingKeywords.join(', ')}

SUGGESTIONS DE FORMULATION
------------------------
${Object.entries(analysisResults.value.keywordSuggestions)
  .map(([keyword, alternatives]) => `${keyword}:\n  - ${alternatives.join('\n  - ')}`)
  .join('\n\n')}

POINTS FORTS
-----------
${analysisResults.value.contentFeedback.points_forts.map(point => `- ${point}`).join('\n')}

SUGGESTIONS D'AMÉLIORATION
------------------------
${analysisResults.value.contentFeedback.points_amelioration.map(point => `- ${point}`).join('\n')}

SCORE GLOBAL: ${analysisResults.value.totalScore.toFixed(1)}/20`

  const blob = new Blob([content], { type: 'text/plain' })
  const url = window.URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.href = url
  link.download = 'analyse_complete_cv.txt'
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
  window.URL.revokeObjectURL(url)
}

const copyKeyword = async (keyword) => {
  try {
    await navigator.clipboard.writeText(keyword)
    showToast('success', 'Mot-clé copié !')
  } catch (err) {
    showToast('error', 'Erreur lors de la copie')
  }
}

const copyMissingKeywords = async () => {
  if (!analysisResults.value?.missingKeywords) return
  
  try {
    const keywords = analysisResults.value.missingKeywords.join(', ')
    await navigator.clipboard.writeText(keywords)
    showToast('success', 'Mots-clés copiés !')
  } catch (err) {
    showToast('error', 'Erreur lors de la copie')
  }
}

const contactForm = ref({
  name: '',
  email: '',
  message: ''
})

const isSubmitting = ref(false)

const sendContactForm = async () => {
  isSubmitting.value = true
  try {
    // Création du contenu de l'email avec mailto
    const subject = `Contact Optimise-ton-CV- ${contactForm.value.name}`
    const body = `Message de : ${contactForm.value.name}\nEmail : ${contactForm.value.email}\n\n${contactForm.value.message}`
    const mailtoLink = `mailto:ouaddour.massyl@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`
    
    // Ouverture du client mail
    window.location.href = mailtoLink
    
    // Réinitialisation du formulaire
    contactForm.value = {
      name: '',
      email: '',
      message: ''
    }
    
    showToast('info', 'Votre client mail a été ouvert. N\'oubliez pas d\'envoyer le message !')
  } catch (error) {
    showToast('error', 'Erreur lors de l\'ouverture de votre client mail')
  } finally {
    isSubmitting.value = false
  }
}

const scrollToAnalysis = () => {
  const analysisSection = document.getElementById('analysis-section')
  if (analysisSection) {
    analysisSection.scrollIntoView({ 
      behavior: 'smooth',
      block: 'start'
    })
  }
}

// État pour le thème et la langue
const isDarkMode = ref(false)
const locale = ref('fr')

// Initialisation du thème au chargement
onMounted(() => {
  // Vérifier la préférence sauvegardée
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDarkMode.value = true
    document.documentElement.classList.add('dark')
  }
})

const toggleDarkMode = () => {
  isDarkMode.value = !isDarkMode.value
  // Appliquer la classe dark au document
  document.documentElement.classList.toggle('dark', isDarkMode.value)
  // Sauvegarder la préférence
  localStorage.setItem('theme', isDarkMode.value ? 'dark' : 'light')
}

// Méthode pour changer la langue
const switchLanguage = (lang) => {
  locale.value = lang
  // Ici, vous pouvez ajouter la logique pour changer la langue de l'application
}
</script>

<style>
.shadow-md {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.shadow-md:hover {
  transform: translateY(-2px);
}

/* Ajout d'animations subtiles */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fadeIn {
  animation: fadeIn 0.5s ease-out forwards;
}
</style> 