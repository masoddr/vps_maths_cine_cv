<template>
  <div class="min-h-[calc(100vh-4rem)] flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900 dark:text-gray-100">
          Crée ton compte
        </h2>
        <p class="mt-2 text-center text-sm text-gray-600 dark:text-gray-400">
          Ou
          <NuxtLink to="/login" class="font-medium text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300">
            connecte-toi à ton compte existant
          </NuxtLink>
        </p>
      </div>
      <div v-if="error" class="rounded-md bg-red-50 dark:bg-red-900 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-5 w-5 text-red-400 dark:text-red-300" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="ml-3">
            <h3 class="text-sm font-medium text-red-800 dark:text-red-200">
              {{ error }}
            </h3>
          </div>
        </div>
      </div>
      <!-- Message de succès -->
      <div v-if="successMessage" class="rounded-md bg-green-50 dark:bg-green-900 p-4">
        <div class="flex">
          <div class="flex-shrink-0">
            <svg class="h-5 w-5 text-green-400 dark:text-green-300" viewBox="0 0 20 20" fill="currentColor">
              <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
            </svg>
          </div>
          <div class="ml-3">
            <h3 class="text-sm font-medium text-green-800 dark:text-green-200">
              {{ successMessage }}
            </h3>
          </div>
        </div>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleRegister">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="name" class="sr-only">Nom complet</label>
            <input
              id="name"
              name="name"
              type="text"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 dark:border-dark-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-gray-100 dark:bg-dark-800 rounded-t-md focus:outline-none focus:ring-indigo-500 dark:focus:ring-indigo-400 focus:border-indigo-500 dark:focus:border-indigo-400 focus:z-10 sm:text-sm transition-colors duration-200"
              placeholder="Nom complet"
              v-model="name"
              @blur="validateName"
            />
            <p v-if="nameError" class="mt-1 text-sm text-red-600 dark:text-red-400">{{ nameError }}</p>
          </div>
          <div>
            <label for="email" class="sr-only">Adresse email</label>
            <input
              id="email"
              name="email"
              type="email"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 dark:border-dark-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-gray-100 dark:bg-dark-800 focus:outline-none focus:ring-indigo-500 dark:focus:ring-indigo-400 focus:border-indigo-500 dark:focus:border-indigo-400 focus:z-10 sm:text-sm transition-colors duration-200"
              placeholder="Adresse email"
              v-model="email"
              @blur="validateEmail"
            />
            <p v-if="emailError" class="mt-1 text-sm text-red-600 dark:text-red-400">{{ emailError }}</p>
          </div>
          <div>
            <label for="password" class="sr-only">Mot de passe</label>
            <input
              id="password"
              name="password"
              type="password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 dark:border-dark-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-gray-100 dark:bg-dark-800 focus:outline-none focus:ring-indigo-500 dark:focus:ring-indigo-400 focus:border-indigo-500 dark:focus:border-indigo-400 focus:z-10 sm:text-sm transition-colors duration-200"
              placeholder="Mot de passe"
              v-model="password"
              @blur="validatePassword"
            />
            <p v-if="passwordError" class="mt-1 text-sm text-red-600 dark:text-red-400">{{ passwordError }}</p>
          </div>
          <div>
            <label for="password_confirmation" class="sr-only">Confirmez le mot de passe</label>
            <input
              id="password_confirmation"
              name="password_confirmation"
              type="password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 dark:border-dark-600 placeholder-gray-500 dark:placeholder-gray-400 text-gray-900 dark:text-gray-100 dark:bg-dark-800 rounded-b-md focus:outline-none focus:ring-indigo-500 dark:focus:ring-indigo-400 focus:border-indigo-500 dark:focus:border-indigo-400 focus:z-10 sm:text-sm transition-colors duration-200"
              placeholder="Confirmez le mot de passe"
              v-model="passwordConfirmation"
              @blur="validatePasswordConfirmation"
            />
            <p v-if="passwordConfirmationError" class="mt-1 text-sm text-red-600 dark:text-red-400">{{ passwordConfirmationError }}</p>
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="accept-terms"
              name="accept-terms"
              type="checkbox"
              required
              class="h-4 w-4 text-indigo-600 dark:text-indigo-400 focus:ring-indigo-500 dark:focus:ring-indigo-400 border-gray-300 dark:border-dark-600 rounded dark:bg-dark-800 transition-colors duration-200"
              v-model="acceptTerms"
            />
            <label for="accept-terms" class="ml-2 block text-sm text-gray-900 dark:text-gray-100">
              J'accepte les
              <a href="#" class="font-medium text-indigo-600 dark:text-indigo-400 hover:text-indigo-500 dark:hover:text-indigo-300">
                conditions d'utilisation
              </a>
            </label>
          </div>
        </div>

        <div>
          <button
            type="submit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 dark:bg-indigo-500 hover:bg-indigo-700 dark:hover:bg-indigo-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 dark:focus:ring-indigo-400 transition-colors duration-200"
            :disabled="loading || !isFormValid"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <svg
                class="h-5 w-5 text-indigo-500 dark:text-indigo-400 group-hover:text-indigo-400 dark:group-hover:text-indigo-300"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z"
                  clip-rule="evenodd"
                />
              </svg>
            </span>
            {{ loading ? 'Inscription en cours...' : 'Créer mon compte' }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter, useRuntimeConfig } from '#app'

const router = useRouter()
const config = useRuntimeConfig()
const name = ref('')
const email = ref('')
const password = ref('')
const passwordConfirmation = ref('')
const acceptTerms = ref(false)
const loading = ref(false)
const error = ref('')
const successMessage = ref('')

// Messages d'erreur pour chaque champ
const nameError = ref('')
const emailError = ref('')
const passwordError = ref('')
const passwordConfirmationError = ref('')

// Fonctions de validation
function validateName() {
  nameError.value = name.value.length === 0 ? 'Le nom est requis' : ''
}

function validateEmail() {
  if (email.value.length === 0) {
    emailError.value = 'L\'email est requis'
  } else if (!email.value.includes('@')) {
    emailError.value = 'L\'email n\'est pas valide'
  } else {
    emailError.value = ''
  }
}

function validatePassword() {
  if (password.value.length === 0) {
    passwordError.value = 'Le mot de passe est requis'
  } else if (password.value.length < 8) {
    passwordError.value = 'Le mot de passe doit contenir au moins 8 caractères'
  } else {
    passwordError.value = ''
  }
}

function validatePasswordConfirmation() {
  if (passwordConfirmation.value !== password.value) {
    passwordConfirmationError.value = 'Les mots de passe ne correspondent pas'
  } else {
    passwordConfirmationError.value = ''
  }
}

const isFormValid = computed(() => {
  const valid = (
    name.value.length > 0 &&
    email.value.length > 0 &&
    email.value.includes('@') &&
    password.value.length >= 8 &&
    password.value === passwordConfirmation.value &&
    acceptTerms.value
  )
  return valid
})

async function handleRegister() {
  console.log('handleRegister appelé')
  if (!isFormValid.value) {
    console.log('Formulaire invalide:', {
      nameLength: name.value.length,
      emailLength: email.value.length,
      passwordLength: password.value.length,
      passwordsMatch: password.value === passwordConfirmation.value,
      termsAccepted: acceptTerms.value
    })
    return
  }
  error.value = ''
  successMessage.value = ''

  try {
    loading.value = true
    const apiUrl = 'https://revise-tes-maths.fr/api/register'
    console.log('URL de l\'API:', apiUrl)
    console.log('Données envoyées:', {
      email: email.value,
      first_name: name.value.split(' ')[0],
      last_name: name.value.split(' ').slice(1).join(' ')
    })
    
    const response = await $fetch(apiUrl, {
      method: 'POST',
      body: {
        email: email.value,
        password: password.value,
        first_name: name.value.split(' ')[0],
        last_name: name.value.split(' ').slice(1).join(' ')
      },
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Origin': 'https://revise-tes-maths.fr'
      }
    })

    console.log('Réponse de l\'API:', response)
    
    // Afficher le message de succès
    successMessage.value = 'Inscription réussie ! Vous allez être redirigé vers la page de connexion.'
    
    // Attendre 2 secondes avant la redirection pour que l'utilisateur puisse voir le message
    setTimeout(async () => {
      await navigateTo('/login')
    }, 2000)
    
  } catch (err) {
    console.error('Erreur d\'inscription détaillée:', err)
    error.value = err.message || 'Erreur lors de l\'inscription'
  } finally {
    loading.value = false
  }
}
</script> 