<template>
  <div class="py-6">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <h1 class="text-3xl font-bold text-gray-900 dark:text-gray-100">
        Messages de contact
      </h1>

      <!-- Message d'erreur -->
      <div v-if="error" class="mt-4 rounded-md bg-red-50 dark:bg-red-900 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-5 w-5 text-red-400 dark:text-red-300" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000-8zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="ml-3">
            <h3 class="text-sm font-medium text-red-800 dark:text-red-200">
              {{ error }}
            </h3>
          </div>
        </div>
      </div>

      <!-- Liste des messages -->
      <div class="mt-8 flex flex-col">
        <div class="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
            <div class="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
              <table class="min-w-full divide-y divide-gray-300 dark:divide-gray-700">
                <thead class="bg-gray-50 dark:bg-dark-800">
                  <tr>
                    <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 dark:text-gray-100 sm:pl-6">
                      Nom
                    </th>
                    <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-gray-100">
                      Email
                    </th>
                    <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-gray-100">
                      Date
                    </th>
                    <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-gray-100">
                      Statut
                    </th>
                    <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-6">
                      <span class="sr-only">Actions</span>
                    </th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-gray-200 dark:divide-gray-700 bg-white dark:bg-dark-900">
                  <tr v-for="message in messages" :key="message.id" :class="{ 'bg-indigo-50 dark:bg-indigo-900/30': !message.is_read }">
                    <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 dark:text-gray-100 sm:pl-6">
                      {{ message.name }}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 dark:text-gray-400">
                      {{ message.email }}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500 dark:text-gray-400">
                      {{ new Date(message.created_at).toLocaleString('fr-FR') }}
                    </td>
                    <td class="whitespace-nowrap px-3 py-4 text-sm">
                      <span :class="[
                        message.is_read 
                          ? 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200'
                          : 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200',
                        'inline-flex rounded-full px-2 text-xs font-semibold leading-5'
                      ]">
                        {{ message.is_read ? 'Lu' : 'Non lu' }}
                      </span>
                    </td>
                    <td class="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                      <button 
                        @click="openMessage(message)"
                        class="text-indigo-600 hover:text-indigo-900 dark:text-indigo-400 dark:hover:text-indigo-300 mr-4"
                      >
                        Voir le message
                      </button>
                      <button 
                        @click="deleteMessage(message.id)"
                        class="text-red-600 hover:text-red-900 dark:text-red-400 dark:hover:text-red-300"
                      >
                        Supprimer
                      </button>
                    </td>
                  </tr>
                  <tr v-if="messages.length === 0">
                    <td colspan="5" class="px-3 py-4 text-sm text-gray-500 dark:text-gray-400 text-center">
                      Aucun message
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de détail du message -->
    <div v-if="selectedMessage" class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity">
      <div class="fixed inset-0 z-10 overflow-y-auto">
        <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
          <div class="relative transform overflow-hidden rounded-lg bg-white dark:bg-dark-800 px-4 pt-5 pb-4 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
            <div>
              <div class="mt-3 text-center sm:mt-5">
                <h3 class="text-lg font-medium leading-6 text-gray-900 dark:text-gray-100">
                  Message de {{ selectedMessage.name }}
                </h3>
                <div class="mt-4">
                  <p class="text-sm text-gray-500 dark:text-gray-400">
                    Email: {{ selectedMessage.email }}
                  </p>
                  <p v-if="selectedMessage.phone" class="text-sm text-gray-500 dark:text-gray-400 mt-1">
                    Téléphone: {{ selectedMessage.phone }}
                  </p>
                  <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">
                    Date: {{ new Date(selectedMessage.created_at).toLocaleString('fr-FR') }}
                  </p>
                  <div class="mt-4 text-left">
                    <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                      Message:
                    </label>
                    <div class="mt-1 p-4 bg-gray-50 dark:bg-dark-700 rounded-md">
                      <p class="text-sm text-gray-900 dark:text-gray-100 whitespace-pre-wrap">
                        {{ selectedMessage.message }}
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="mt-5 sm:mt-6 sm:grid sm:grid-flow-row-dense sm:grid-cols-2 sm:gap-3">
              <button
                v-if="!selectedMessage.is_read"
                type="button"
                class="inline-flex w-full justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-base font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:col-start-2 sm:text-sm"
                @click="markAsRead(selectedMessage.id)"
              >
                Marquer comme lu
              </button>
              <button
                type="button"
                class="mt-3 inline-flex w-full justify-center rounded-md border border-gray-300 dark:border-gray-600 bg-white dark:bg-dark-700 px-4 py-2 text-base font-medium text-gray-700 dark:text-gray-300 shadow-sm hover:bg-gray-50 dark:hover:bg-dark-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:col-start-1 sm:mt-0 sm:text-sm"
                @click="closeMessage"
              >
                Fermer
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const config = useRuntimeConfig()
const messages = ref([])
const error = ref('')
const selectedMessage = ref(null)

// Charger les messages
async function loadMessages() {
  try {
    const response = await fetch('http://localhost:5000/api/admin/contact-messages', {
      credentials: 'include'
    })

    if (!response.ok) {
      throw new Error('Erreur lors du chargement des messages')
    }

    messages.value = await response.json()
  } catch (err) {
    error.value = err.message
  }
}

// Ouvrir le modal d'un message
function openMessage(message) {
  selectedMessage.value = message
}

// Fermer le modal
function closeMessage() {
  selectedMessage.value = null
}

// Marquer un message comme lu
async function markAsRead(id) {
  try {
    const response = await fetch(`http://localhost:5000/api/admin/contact-messages/${id}/mark-as-read`, {
      method: 'PUT',
      credentials: 'include'
    })

    if (!response.ok) {
      throw new Error('Erreur lors du marquage du message')
    }

    // Mettre à jour le message dans la liste
    const message = messages.value.find(m => m.id === id)
    if (message) {
      message.is_read = true
    }
    selectedMessage.value.is_read = true
  } catch (err) {
    error.value = err.message
  }
}

// Supprimer un message
async function deleteMessage(id) {
  if (!confirm('Êtes-vous sûr de vouloir supprimer ce message ?')) {
    return
  }

  try {
    const response = await fetch(`http://localhost:5000/api/admin/contact-messages/${id}`, {
      method: 'DELETE',
      credentials: 'include'
    })

    if (!response.ok) {
      throw new Error('Erreur lors de la suppression du message')
    }

    // Retirer le message de la liste
    messages.value = messages.value.filter(m => m.id !== id)
    if (selectedMessage.value?.id === id) {
      selectedMessage.value = null
    }
  } catch (err) {
    error.value = err.message
  }
}

// Charger les messages au montage du composant
onMounted(loadMessages)

definePageMeta({
  layout: 'admin',
  middleware: ['auth', 'admin']
})
</script> 