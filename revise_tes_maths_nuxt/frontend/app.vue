<template>
  <div class="min-h-screen bg-gray-50 dark:bg-dark-900 transition-colors duration-200">
    <!-- En-tête -->
    <nav class="fixed top-0 left-0 right-0 z-50 bg-white/80 dark:bg-dark-800/80 backdrop-blur-lg shadow-sm transition-all duration-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex">
            <!-- Logo -->
            <div class="flex-shrink-0 flex items-center">
              <NuxtLink :to="isLoggedIn ? '/dashboard' : '/'" class="flex items-center space-x-2 text-xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent hover:from-purple-600 hover:to-indigo-600 transform hover:scale-105 transition-all duration-300">
                <img src="/images/mascotte.png" alt="Logo Révise Tes Maths" class="h-8 w-8 object-contain animate-bounce-soft" />
                <span>Révise Tes Maths</span>
              </NuxtLink>
            </div>
            <!-- Navigation principale -->
            <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
              <template v-if="!isLoggedIn">
                <button
                  v-for="section in presentationSections" 
                  :key="section.id"
                  @click="navigateToSection(section.id)"
                  class="nav-link inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-all duration-200 relative"
                  :class="{ 'text-indigo-600 dark:text-indigo-400': $route.path === '/presentation' && activeSection === section.id }"
                >
                  {{ section.name }}
                  <span class="nav-link-underline"></span>
                </button>
              </template>
              <NuxtLink 
                v-if="isLoggedIn"
                to="/dashboard" 
                class="nav-link inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-all duration-200 relative"
                :class="{ 'text-indigo-600 dark:text-indigo-400': $route.path === '/dashboard' }"
              >
                Tableau de bord
                <span class="nav-link-underline"></span>
              </NuxtLink>
              <NuxtLink 
                v-if="isLoggedIn"
                to="/annales" 
                class="nav-link inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-all duration-200 relative"
                :class="{ 'text-indigo-600 dark:text-indigo-400': $route.path === '/annales' }"
              >
                Annales
                <span class="nav-link-underline"></span>
              </NuxtLink>
              <NuxtLink 
                v-if="isAdmin"
                to="/admin" 
                class="nav-link inline-flex items-center px-1 pt-1 text-sm font-medium text-indigo-600 dark:text-indigo-400 hover:text-indigo-700 dark:hover:text-indigo-300 transition-all duration-200 relative"
              >
                Administration
                <span class="nav-link-underline"></span>
              </NuxtLink>
            </div>
          </div>
          <!-- Boutons de connexion/inscription et thème -->
          <div class="hidden sm:ml-6 sm:flex sm:items-center sm:space-x-4">
            <ThemeToggle />
            <template v-if="!isLoggedIn">
              <NuxtLink 
                to="/login" 
                class="nav-link text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100 transition-all duration-200 relative"
              >
                Me connecter
                <span class="nav-link-underline"></span>
              </NuxtLink>
              <NuxtLink 
                to="/register" 
                class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-purple-600 hover:to-indigo-600 transform hover:scale-105 transition-all duration-300 shadow-md hover:shadow-lg"
              >
                M'inscrire
              </NuxtLink>
            </template>
            <template v-else>
              <span class="text-sm font-medium text-gray-500 dark:text-gray-400">
                {{ userEmail }}
              </span>
              <button 
                @click="handleLogout"
                class="nav-link text-sm font-medium text-red-600 dark:text-red-400 hover:text-red-800 dark:hover:text-red-300 transition-all duration-200 relative"
              >
                Déconnexion
                <span class="nav-link-underline"></span>
              </button>
            </template>
          </div>
          <!-- Menu mobile -->
          <div class="sm:hidden flex items-center">
            <button 
              @click="mobileMenuOpen = !mobileMenuOpen"
              class="inline-flex items-center justify-center p-3 rounded-md text-indigo-600 dark:text-indigo-400 hover:text-indigo-800 dark:hover:text-indigo-300 hover:bg-indigo-50 dark:hover:bg-dark-700 transition-all duration-200"
              aria-label="Menu principal"
            >
              <span class="sr-only">Ouvrir le menu</span>
              <div class="hamburger-menu" :class="{ 'is-active': mobileMenuOpen }">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </button>
          </div>
        </div>
      </div>

      <!-- Menu mobile déroulant -->
      <Transition
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="transform -translate-y-2 opacity-0"
        enter-to-class="transform translate-y-0 opacity-100"
        leave-active-class="transition duration-150 ease-in"
        leave-from-class="transform translate-y-0 opacity-100"
        leave-to-class="transform -translate-y-2 opacity-0"
      >
        <div 
          v-show="mobileMenuOpen" 
          class="sm:hidden fixed top-16 left-0 right-0 bg-white dark:bg-dark-800 shadow-lg max-h-[calc(100vh-4rem)] overflow-y-auto"
        >
          <div class="pt-2 pb-3 space-y-1">
            <template v-if="!isLoggedIn">
              <button
                v-for="section in presentationSections" 
                :key="section.id"
                @click="navigateToSection(section.id)"
                class="block w-full text-left pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium text-gray-600 dark:text-gray-400 hover:border-indigo-500 hover:bg-indigo-50 dark:hover:bg-dark-700 hover:text-indigo-700 dark:hover:text-indigo-300 transition-all duration-200"
                :class="{ 'border-indigo-500 text-indigo-600 dark:text-indigo-400': $route.path === '/presentation' && activeSection === section.id }"
              >
                {{ section.name }}
              </button>
            </template>
            <NuxtLink 
              v-if="isLoggedIn"
              to="/dashboard" 
              class="block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium text-gray-600 dark:text-gray-400 hover:border-indigo-500 hover:bg-indigo-50 dark:hover:bg-dark-700 hover:text-indigo-700 dark:hover:text-indigo-300 transition-all duration-200"
              @click="mobileMenuOpen = false"
            >
              Tableau de bord
            </NuxtLink>
            <NuxtLink 
              v-if="isLoggedIn"
              to="/annales" 
              class="block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium text-gray-600 dark:text-gray-400 hover:border-indigo-500 hover:bg-indigo-50 dark:hover:bg-dark-700 hover:text-indigo-700 dark:hover:text-indigo-300 transition-all duration-200"
              @click="mobileMenuOpen = false"
            >
              Annales
            </NuxtLink>
            <NuxtLink 
              v-if="isAdmin"
              to="/admin" 
              class="block pl-3 pr-4 py-2 border-l-4 border-transparent text-base font-medium text-gray-600 dark:text-gray-400 hover:border-indigo-500 hover:bg-indigo-50 dark:hover:bg-dark-700 hover:text-indigo-700 dark:hover:text-indigo-300 transition-all duration-200"
              @click="mobileMenuOpen = false"
            >
              Administration
            </NuxtLink>
          </div>
          <div class="pt-4 pb-3 border-t border-gray-200 dark:border-dark-700">
            <div v-if="isLoggedIn" class="flex items-center px-4">
              <div class="ml-3">
                <div class="text-base font-medium text-gray-800 dark:text-gray-200">{{ userEmail }}</div>
              </div>
            </div>
            <div class="mt-3 space-y-1">
              <template v-if="!isLoggedIn">
                <NuxtLink 
                  to="/login"
                  class="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-dark-700 transition-all duration-200"
                  @click="mobileMenuOpen = false"
                >
                  Connexion
                </NuxtLink>
                <NuxtLink 
                  to="/register"
                  class="block px-4 py-2 text-base font-medium text-gray-500 dark:text-gray-400 hover:text-indigo-600 dark:hover:text-indigo-400 hover:bg-indigo-50 dark:hover:bg-dark-700 transition-all duration-200"
                  @click="mobileMenuOpen = false"
                >
                  Inscription
                </NuxtLink>
              </template>
              <button 
                v-else
                @click="handleLogout(); mobileMenuOpen = false"
                class="block w-full text-left px-4 py-2 text-base font-medium text-red-600 dark:text-red-400 hover:text-red-800 dark:hover:text-red-300 hover:bg-red-50 dark:hover:bg-dark-700 transition-all duration-200"
              >
                Déconnexion
              </button>
            </div>
          </div>
        </div>
      </Transition>
    </nav>

    <!-- Contenu principal -->
    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8 mt-16">
      <NuxtPage />
    </main>

    <!-- Pied de page -->
    <footer class="bg-white dark:bg-dark-800 mt-auto transition-colors duration-200">
      <div class="max-w-7xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
        <div class="mt-8 border-t border-gray-200 dark:border-dark-700 pt-8 md:flex md:items-center md:justify-between">
          <div class="text-base text-gray-400 dark:text-gray-500">
            &copy; 2024 Révise Tes Maths. Tous droits réservés.
          </div>
          <div class="mt-4 md:mt-0">
            <div class="flex space-x-6">
              <NuxtLink 
                to="/legal/cgu" 
                class="text-gray-400 dark:text-gray-500 hover:text-gray-500 dark:hover:text-gray-400 transition-colors duration-200"
              >
                CGU
              </NuxtLink>
              <NuxtLink 
                to="/legal/privacy" 
                class="text-gray-400 dark:text-gray-500 hover:text-gray-500 dark:hover:text-gray-400 transition-colors duration-200"
              >
                Politique de confidentialité
              </NuxtLink>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import ThemeToggle from '~/components/ThemeToggle.vue'
import { ref, onMounted, watch, nextTick } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const config = useRuntimeConfig()
const isAdmin = ref(false)
const isLoggedIn = ref(false)
const userEmail = ref('')
const mobileMenuOpen = ref(false)

// Sections de la page présentation
const presentationSections = [
  { id: 'hero', name: 'Cours particuliers' },
  { id: 'services', name: 'Services' },
  { id: 'pricing', name: 'Tarifs' },
  { id: 'testimonials', name: 'Témoignages' },
  { id: 'contact', name: 'Contact' },
  { id: 'faq', name: 'FAQ' }
]

// Section active de la page présentation
const activeSection = ref('')

// Observer les sections visibles
function setupSectionObserver() {
  if (process.client && router.currentRoute.value.path === '/presentation') {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          activeSection.value = entry.target.id
        }
      })
    }, {
      rootMargin: '-50% 0px -50% 0px'
    })

    // Observer chaque section
    presentationSections.forEach(section => {
      const element = document.getElementById(section.id)
      if (element) {
        observer.observe(element)
      }
    })
  }
}

// Fonction pour gérer la navigation vers les sections
async function navigateToSection(sectionId) {
  // Si on n'est pas déjà sur la page de présentation, naviguer d'abord vers celle-ci
  if (router.currentRoute.value.path !== '/presentation') {
    await router.push({
      path: '/presentation',
      hash: `#${sectionId}`
    })
  } else {
    // Si on est déjà sur la page de présentation, faire défiler jusqu'à la section
    const element = document.getElementById(sectionId)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' })
    }
  }
  
  // Fermer le menu mobile si ouvert
  mobileMenuOpen.value = false
}

// Vérifier l'état de connexion
async function checkAuthState() {
  try {
    const { data } = await useFetch('/api/auth/me', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })
    
    if (data.value?.user) {
      isLoggedIn.value = true
      isAdmin.value = data.value.user.is_admin
      userEmail.value = data.value.user.email
      
      // Rediriger vers le tableau de bord uniquement si on est sur la page d'accueil
      // et qu'on n'est pas déjà sur une page protégée
      const protectedRoutes = ['/dashboard', '/annales', '/admin']
      const currentPath = window.location.pathname
      if (currentPath === '/' && !protectedRoutes.some(route => currentPath.startsWith(route))) {
        await router.push('/dashboard')
      }
    } else {
      isLoggedIn.value = false
      isAdmin.value = false
      userEmail.value = ''
      
      // Rediriger vers la page d'accueil uniquement si on est sur une page protégée
      const protectedRoutes = ['/dashboard', '/annales', '/admin']
      if (protectedRoutes.some(route => window.location.pathname.startsWith(route))) {
        await router.push('/')
      }
    }
  } catch (error) {
    console.error('Erreur lors de la vérification de l\'authentification:', error)
    isLoggedIn.value = false
    isAdmin.value = false
    userEmail.value = ''
  }
}

// Gérer la déconnexion
async function handleLogout() {
  // Demander confirmation
  if (!confirm('Êtes-vous sûr de vouloir vous déconnecter ?')) {
    return
  }

  try {
    const response = await fetch(`${config.public.apiBase}/api/logout`, {
      method: 'GET',
      credentials: 'include'
    })

    if (response.ok) {
      isLoggedIn.value = false
      isAdmin.value = false
      userEmail.value = ''
      await router.push('/')
    } else {
      console.error('Erreur lors de la déconnexion')
    }
  } catch (error) {
    console.error('Erreur lors de la déconnexion:', error)
  }
}

// Initialisation au chargement
onMounted(async () => {
  const savedTheme = localStorage.getItem('theme')
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches
  
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.documentElement.classList.add('dark')
  }

  await checkAuthState()
  setupSectionObserver()
})

// Vérifier l'état de connexion à chaque changement de route
watch(() => router.currentRoute.value.path, (newPath) => {
  if (newPath === '/presentation') {
    // Attendre que le DOM soit mis à jour
    nextTick(() => {
      setupSectionObserver()
      // Si un hash est présent dans l'URL, faire défiler jusqu'à la section
      if (window.location.hash) {
        const sectionId = window.location.hash.slice(1)
        const element = document.getElementById(sectionId)
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' })
        }
      }
    })
  } else {
    activeSection.value = ''
  }
  checkAuthState()
})
</script>

<style>
/* Styles de transition globaux */
.page-enter-active,
.page-leave-active {
  transition: all 0.3s ease-in-out;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* Styles pour le mode sombre */
html.dark {
  color-scheme: dark;
}

/* Styles pour la barre de défilement personnalisée */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  @apply bg-gray-100 dark:bg-dark-800;
}

::-webkit-scrollbar-thumb {
  @apply bg-gray-400 dark:bg-dark-600 rounded-full;
}

::-webkit-scrollbar-thumb:hover {
  @apply bg-gray-500 dark:bg-dark-500;
}

/* Styles pour la barre de navigation */
.nav-link {
  position: relative;
  overflow: hidden;
}

.nav-link-underline {
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: linear-gradient(to right, #4f46e5, #9333ea);
  transform: scaleX(0);
  transition: transform 0.3s ease;
  transform-origin: right;
}

.nav-link:hover .nav-link-underline {
  transform: scaleX(1);
  transform-origin: left;
}

/* Animation pour le menu burger */
.hamburger-menu {
  width: 28px;
  height: 24px;
  position: relative;
  cursor: pointer;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.hamburger-menu span {
  display: block;
  height: 2px;
  width: 100%;
  background: currentColor;
  transition: all 0.3s ease;
  transform-origin: center;
}

.hamburger-menu.is-active span:first-child {
  transform: translateY(11px) rotate(45deg);
}

.hamburger-menu.is-active span:nth-child(2) {
  opacity: 0;
}

.hamburger-menu.is-active span:last-child {
  transform: translateY(-11px) rotate(-45deg);
}

/* Effet de glassmorphisme pour la barre de navigation */
@supports (backdrop-filter: blur(12px)) {
  nav {
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
  }
}
</style>
