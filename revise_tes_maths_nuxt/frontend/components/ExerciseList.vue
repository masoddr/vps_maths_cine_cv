<template>
  <div class="space-y-4">
    <div 
      v-for="exercise in exercises" 
      :key="exercise.id" 
      class="bg-white dark:bg-dark-800 shadow rounded-lg p-4 animate-slide-in transition-colors duration-200"
    >
      <div class="flex items-start justify-between">
        <div>
          <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">
            Exercice {{ exercise.number }}
          </h3>
          <div class="mt-1">
            <span 
              v-for="theme in exercise.themes" 
              :key="theme" 
              class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-200 mr-1 animate-fade-in"
            >
              {{ theme }}
            </span>
          </div>
          <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">{{ exercise.description }}</p>
        </div>
        <div class="flex-shrink-0">
          <button
            @click="updateStatus(exercise)"
            :class="[
              'px-3 py-1 rounded-md text-sm font-medium transition-all duration-300 transform hover:scale-105',
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
      
      <div class="mt-4">
        <label :for="'notes-' + exercise.id" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
          Notes personnelles
        </label>
        <div class="mt-1">
          <textarea
            :id="'notes-' + exercise.id"
            v-model="exercise.notes"
            rows="3"
            class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md dark:bg-dark-700 dark:border-dark-600 dark:text-gray-100 transition-colors duration-200"
            placeholder="Ajoutez vos notes ici..."
            @change="saveNotes(exercise)"
          ></textarea>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRuntimeConfig } from '#app'

const config = useRuntimeConfig()

const props = defineProps({
  exercises: {
    type: Array,
    required: true
  },
  annaleId: {
    type: Number,
    required: true
  }
})

const emit = defineEmits(['update'])

const statusText = {
  not_started: 'À faire',
  in_progress: 'En cours',
  completed: 'Terminé'
}

const statusClasses = {
  not_started: 'bg-gray-100 text-gray-800 dark:bg-dark-600 dark:text-gray-200 hover:bg-gray-200 dark:hover:bg-dark-500',
  in_progress: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200 hover:bg-yellow-200 dark:hover:bg-yellow-800',
  completed: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200 hover:bg-green-200 dark:hover:bg-green-800'
}

const nextStatus = {
  not_started: 'in_progress',
  in_progress: 'completed',
  completed: 'not_started'
}

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
    exercise.status = exercise.status === 'completed' ? 'in_progress' : 'completed'
    
    // Émettre l'événement de mise à jour
    emit('update', exercise)
  } catch (error) {
    console.error('Erreur lors de la mise à jour du statut:', error)
  }
}

async function saveNotes(exercise) {
  try {
    const response = await fetch(`${config.public.apiBase}/api/progress/${exercise.id}/notes`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify({
        notes: exercise.notes
      })
    })

    if (!response.ok) {
      throw new Error('Erreur lors de la sauvegarde des notes')
    }

    emit('update', exercise)
  } catch (error) {
    console.error('Erreur lors de la sauvegarde des notes:', error)
    // TODO: Afficher un message d'erreur à l'utilisateur
  }
}
</script> 