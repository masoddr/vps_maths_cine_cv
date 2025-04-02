<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold mb-6">Ajouter une annale</h1>

    <form @submit.prevent="handleSubmit" class="max-w-2xl space-y-6">
      <!-- Titre -->
      <div>
        <label for="title" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
          Titre
        </label>
        <input
          type="text"
          id="title"
          v-model="formData.title"
          required
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 dark:bg-gray-800 dark:border-gray-700"
        />
      </div>

      <!-- Année -->
      <div>
        <label for="year" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
          Année
        </label>
        <input
          type="number"
          id="year"
          v-model="formData.year"
          required
          min="2000"
          max="2100"
          class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 dark:bg-gray-800 dark:border-gray-700"
        />
      </div>

      <!-- PDF -->
      <div>
        <label for="pdf" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
          PDF du sujet
        </label>
        <input
          type="file"
          id="pdf"
          ref="pdfInput"
          accept=".pdf"
          required
          @change="handleFileChange"
          class="mt-1 block w-full text-sm text-gray-900 dark:text-gray-100 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100"
        />
      </div>

      <!-- Exercices -->
      <div>
        <h3 class="text-lg font-medium mb-4">Exercices</h3>
        <div v-for="(exercise, index) in exercises" :key="index" class="border p-4 rounded-md mb-4">
          <h4 class="font-medium mb-4">Exercice {{ index + 1 }}</h4>

          <!-- Thèmes -->
          <div>
            <label class="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              Thèmes
            </label>
            <div class="space-y-2">
              <div v-for="theme in availableThemes" :key="theme" class="flex items-center">
                <input
                  type="checkbox"
                  :id="'theme-' + index + '-' + theme"
                  :value="theme"
                  v-model="exercise.themes"
                  class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                />
                <label :for="'theme-' + index + '-' + theme" class="ml-2 block text-sm text-gray-900 dark:text-gray-300">
                  {{ theme }}
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Message d'erreur -->
      <div v-if="error" class="text-red-600 dark:text-red-400">
        {{ error }}
      </div>

      <!-- Boutons -->
      <div class="flex justify-end space-x-4">
        <NuxtLink
          to="/admin/exam-papers"
          class="inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Annuler
        </NuxtLink>
        <button
          type="submit"
          :disabled="loading"
          class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          {{ loading ? 'Enregistrement...' : 'Enregistrer' }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()
const router = useRouter()

const formData = ref({
  title: '',
  year: new Date().getFullYear(),
  pdf: null
})

const pdfInput = ref(null)

const loading = ref(false)
const error = ref('')

const exercises = ref([
  { themes: [] },
  { themes: [] },
  { themes: [] },
  { themes: [] }
])

const availableThemes = [
  'Probabilités',
  'Loi Binomiale',
  'Géométrie dans l\'espace',
  'Suites',
  'Etudes de fonctions',
  'Exponentielle',
  'Logarithme Népérien',
  'Intégrale',
  'Convexité',
  'Equations différentielles',
  'Python'
]

function handleFileChange(event) {
  const file = event.target.files[0]
  if (file && file.type === 'application/pdf') {
    formData.value.pdf = file
  } else {
    alert('Veuillez sélectionner un fichier PDF valide')
    event.target.value = '' // Réinitialiser l'input
  }
}

async function handleSubmit() {
  try {
    loading.value = true
    error.value = ''

    if (!formData.value.pdf) {
      throw new Error('Veuillez sélectionner un fichier PDF')
    }

    const form = new FormData()
    form.append('title', formData.value.title)
    form.append('year', formData.value.year)
    form.append('pdf', formData.value.pdf)
    
    // Préparer les exercices avec leurs thèmes
    const exercisesData = exercises.value.map((exercise, index) => ({
      number: index + 1,
      themes: exercise.themes
    }))
    form.append('exercises', JSON.stringify(exercisesData))

    const response = await fetch(`${config.public.apiBase}/api/exampapers`, {
      method: 'POST',
      body: form,
      credentials: 'include'
    })

    if (!response.ok) {
      const data = await response.json()
      throw new Error(data.error || 'Erreur lors de la création de l\'annale')
    }

    await router.push('/admin/exam-papers')
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script> 