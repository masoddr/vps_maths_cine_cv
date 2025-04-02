<template>
  <div>
    <div class="md:flex md:items-center md:justify-between">
      <div class="flex-1 min-w-0">
        <h2 class="text-2xl font-bold leading-7 text-gray-900 dark:text-gray-100 sm:text-3xl sm:truncate">
          Gestion des annales
        </h2>
      </div>
      <div class="mt-4 flex md:mt-0 md:ml-4">
        <button
          @click="showAddModal = true"
          class="ml-3 inline-flex items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Ajouter une annale
        </button>
      </div>
    </div>

    <!-- Liste des annales -->
    <div class="mt-8 flex flex-col">
      <div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8">
          <div class="shadow overflow-hidden border-b border-gray-200 dark:border-dark-700 sm:rounded-lg">
            <table class="min-w-full divide-y divide-gray-200 dark:divide-dark-700">
              <thead class="bg-gray-50 dark:bg-dark-800">
                <tr>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                    Titre
                  </th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                    Année
                  </th>
                  <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-400 uppercase tracking-wider">
                    Exercices
                  </th>
                  <th scope="col" class="relative px-6 py-3">
                    <span class="sr-only">Actions</span>
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white dark:bg-dark-800 divide-y divide-gray-200 dark:divide-dark-700">
                <tr v-for="annale in annales" :key="annale.id">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="text-sm font-medium text-gray-900 dark:text-gray-100">
                      {{ annale.title }}
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="text-sm text-gray-900 dark:text-gray-100">
                      {{ annale.year }}
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="text-sm text-gray-900 dark:text-gray-100">
                      {{ annale.exercises?.length || 0 }} exercices
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                    <button
                      @click="editAnnale(annale)"
                      class="text-indigo-600 dark:text-indigo-400 hover:text-indigo-900 dark:hover:text-indigo-300 mr-4"
                    >
                      Modifier
                    </button>
                    <button
                      @click="deleteAnnale(annale)"
                      class="text-red-600 dark:text-red-400 hover:text-red-900 dark:hover:text-red-300"
                    >
                      Supprimer
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal d'ajout/modification -->
    <div v-if="showAddModal || showEditModal" class="fixed z-10 inset-0 overflow-y-auto">
      <div class="flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <div class="fixed inset-0 bg-gray-500 dark:bg-dark-900 bg-opacity-75 transition-opacity"></div>

        <div class="inline-block align-bottom bg-white dark:bg-dark-800 rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <form @submit.prevent="saveAnnale">
            <div class="bg-white dark:bg-dark-800 px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
              <div class="sm:flex sm:items-start">
                <div class="mt-3 text-center sm:mt-0 sm:text-left w-full">
                  <h3 class="text-lg leading-6 font-medium text-gray-900 dark:text-gray-100">
                    {{ showEditModal ? 'Modifier l\'annale' : 'Ajouter une annale' }}
                  </h3>
                  <div class="mt-2 space-y-4">
                    <div>
                      <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                        Titre
                      </label>
                      <input
                        type="text"
                        v-model="editedAnnale.title"
                        required
                        class="mt-1 block w-full border-gray-300 dark:border-dark-600 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm dark:bg-dark-700 dark:text-gray-100"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                        Année
                      </label>
                      <input
                        type="number"
                        v-model="editedAnnale.year"
                        required
                        min="2000"
                        max="2100"
                        class="mt-1 block w-full border-gray-300 dark:border-dark-600 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm dark:bg-dark-700 dark:text-gray-100"
                      />
                    </div>
                    <div>
                      <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                        PDF
                      </label>
                      <input
                        type="file"
                        ref="fileInput"
                        accept=".pdf"
                        :required="!showEditModal"
                        @change="handleFileChange"
                        class="mt-1 block w-full text-sm text-gray-900 dark:text-gray-100"
                      />
                    </div>
                    <div>
                      <h4 class="text-lg font-medium text-gray-900 dark:text-gray-100 mb-4">Exercices</h4>
                      <div v-for="exercise in editedAnnale.exercises" :key="exercise.number" class="mb-6 p-4 border border-gray-200 dark:border-dark-600 rounded-lg">
                        <h5 class="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                          Exercice {{ exercise.number }}
                        </h5>
                        <div class="space-y-4">
                          <div>
                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                              Description
                            </label>
                            <input
                              type="text"
                              v-model="exercise.description"
                              class="mt-1 block w-full border-gray-300 dark:border-dark-600 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm dark:bg-dark-700 dark:text-gray-100"
                              :placeholder="'Description de l\'exercice ' + exercise.number"
                            />
                          </div>
                          <div>
                            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                              Thèmes
                            </label>
                            <select
                              v-model="exercise.themes"
                              multiple
                              required
                              class="mt-1 block w-full border-gray-300 dark:border-dark-600 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm dark:bg-dark-700 dark:text-gray-100"
                            >
                              <option v-for="theme in availableThemes" :key="theme" :value="theme">
                                {{ theme }}
                              </option>
                            </select>
                            <p class="mt-1 text-xs text-gray-500 dark:text-gray-400">
                              Maintenez Ctrl (ou Cmd sur Mac) pour sélectionner plusieurs thèmes
                            </p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="bg-gray-50 dark:bg-dark-700 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
              <button
                type="submit"
                class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-indigo-600 text-base font-medium text-white hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:ml-3 sm:w-auto sm:text-sm"
              >
                {{ showEditModal ? 'Enregistrer' : 'Ajouter' }}
              </button>
              <button
                type="button"
                @click="closeModal"
                class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 dark:border-dark-600 shadow-sm px-4 py-2 bg-white dark:bg-dark-800 text-base font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-dark-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
              >
                Annuler
              </button>
            </div>
          </form>
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
const annales = ref([])
const showAddModal = ref(false)
const showEditModal = ref(false)
const editedAnnale = ref({
  title: '',
  year: new Date().getFullYear(),
  pdf: null,
  exercises: [
    { number: 1, description: '', themes: [] },
    { number: 2, description: '', themes: [] },
    { number: 3, description: '', themes: [] },
    { number: 4, description: '', themes: [] }
  ]
})
const fileInput = ref(null)

const availableThemes = [
  'Probabilités',
  'Géométrie dans l\'espace',
  'Suites numériques',
  'Fonctions',
  'Primitives',
  'Équations différentielles',
  'Logarithmes',
  'Nombres complexes',
  'Python'
]

// Charger la liste des annales
async function loadAnnales() {
  try {
    const response = await useFetch('/api/exampapers', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (response.data.value) {
      annales.value = response.data.value
    }
  } catch (error) {
    console.error('Erreur lors du chargement des annales:', error)
  }
}

// Gérer le changement de fichier
function handleFileChange(event) {
  const file = event.target.files[0]
  if (file && file.type === 'application/pdf') {
    editedAnnale.value.pdf = file
  } else {
    alert('Veuillez sélectionner un fichier PDF valide')
    event.target.value = '' // Réinitialiser l'input
  }
}

// Modifier une annale
function editAnnale(annale) {
  editedAnnale.value = { ...annale }
  showEditModal.value = true
}

// Sauvegarder une annale
async function saveAnnale() {
  try {
    const formData = new FormData()
    formData.append('title', editedAnnale.value.title)
    formData.append('year', editedAnnale.value.year)
    if (editedAnnale.value.pdf) {
      formData.append('pdf', editedAnnale.value.pdf, editedAnnale.value.pdf.name)
    }
    
    // Ajouter les exercices
    formData.append('exercises', JSON.stringify(editedAnnale.value.exercises))

    const url = showEditModal.value
      ? `/api/exampapers/${editedAnnale.value.id}`
      : '/api/exampapers'

    const response = await fetch(`${config.public.apiBase}${url}`, {
      method: showEditModal.value ? 'PUT' : 'POST',
      body: formData,
      credentials: 'include'
    })

    if (!response.ok) {
      const error = await response.json()
      throw new Error(error.error || 'Erreur lors de la sauvegarde de l\'annale')
    }

    const result = await response.json()
    if (showEditModal.value) {
      const index = annales.value.findIndex(a => a.id === editedAnnale.value.id)
      if (index !== -1) {
        annales.value[index] = result
      }
    } else {
      annales.value.push(result)
    }
    closeModal()
  } catch (error) {
    console.error('Erreur lors de la sauvegarde de l\'annale:', error)
    alert(error.message)
  }
}

// Supprimer une annale
async function deleteAnnale(annale) {
  if (!confirm(`Êtes-vous sûr de vouloir supprimer l'annale "${annale.title}" ?`)) {
    return
  }

  try {
    const response = await useFetch(`/api/exampapers/${annale.id}`, {
      method: 'DELETE',
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    if (response.data.value) {
      annales.value = annales.value.filter(a => a.id !== annale.id)
    }
  } catch (error) {
    console.error('Erreur lors de la suppression de l\'annale:', error)
  }
}

// Fermer le modal
function closeModal() {
  showAddModal.value = false
  showEditModal.value = false
  editedAnnale.value = {
    title: '',
    year: new Date().getFullYear(),
    pdf: null,
    exercises: [
      { number: 1, description: '', themes: [] },
      { number: 2, description: '', themes: [] },
      { number: 3, description: '', themes: [] },
      { number: 4, description: '', themes: [] }
    ]
  }
  if (fileInput.value) {
    fileInput.value.value = ''
  }
}

// Charger les annales au montage
onMounted(() => {
  loadAnnales()
})
</script> 