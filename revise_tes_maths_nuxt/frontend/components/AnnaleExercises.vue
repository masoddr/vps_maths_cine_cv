<template>
  <div class="mt-4">
    <div v-for="exercise in exercises" :key="exercise.id" class="mb-2 flex items-center justify-between">
      <div>
        <span class="text-sm font-medium text-gray-700 dark:text-gray-300">Exercice {{ exercise.number }}:</span>
        <span v-for="theme in exercise.themes" :key="theme" class="ml-2 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 dark:bg-indigo-900 text-indigo-800 dark:text-indigo-200 mr-1">
          {{ theme }}
        </span>
      </div>
      <button
        @click="updateStatus(exercise)"
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

    <!-- Message d'encouragement -->
    <SuccessMessage :show="showSuccessMessage" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRuntimeConfig } from '#app'
import SuccessMessage from './SuccessMessage.vue'

const config = useRuntimeConfig()
const showSuccessMessage = ref(false)

const props = defineProps({
  exercises: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['update'])

async function updateStatus(exercise) {
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
    
    // Émettre l'événement de mise à jour
    emit('update', exercise)

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
</script> 