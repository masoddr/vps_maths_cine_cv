<template>
  <button
    @click="toggleTheme"
    class="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-dark-700 transition-colors duration-200"
    :title="isDark ? 'Passer en mode clair' : 'Passer en mode sombre'"
  >
    <!-- Icône soleil pour le mode clair -->
    <svg
      v-if="isDark"
      class="w-5 h-5 text-yellow-500"
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
    <!-- Icône lune pour le mode sombre -->
    <svg
      v-else
      class="w-5 h-5 text-gray-500"
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
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'

const isDark = ref(false)

function toggleTheme() {
  isDark.value = !isDark.value
}

function updateTheme(dark) {
  // Mettre à jour la classe sur l'élément HTML
  if (dark) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
  
  // Sauvegarder la préférence
  localStorage.setItem('theme', dark ? 'dark' : 'light')
}

// Observer les changements de isDark
watch(isDark, (newValue) => {
  updateTheme(newValue)
})

// Initialiser le thème au chargement
onMounted(() => {
  // Récupérer la préférence sauvegardée
  const savedTheme = localStorage.getItem('theme')
  
  if (savedTheme) {
    // Utiliser la préférence sauvegardée
    isDark.value = savedTheme === 'dark'
  } else {
    // Utiliser la préférence système
    isDark.value = window.matchMedia('(prefers-color-scheme: dark)').matches
  }
  
  // Appliquer le thème initial
  updateTheme(isDark.value)
  
  // Observer les changements de préférence système
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem('theme')) {
      isDark.value = e.matches
    }
  })
})
</script> 