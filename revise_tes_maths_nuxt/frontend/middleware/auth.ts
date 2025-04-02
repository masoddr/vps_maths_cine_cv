import type { AuthResponse } from '~/types/auth'

export default defineNuxtRouteMiddleware(async (to) => {
  const config = useRuntimeConfig()
  
  // Ne pas vérifier l'authentification pour les pages publiques
  if (['/login', '/register', '/'].includes(to.path)) {
    return
  }

  try {
    const { data } = await useFetch<AuthResponse>('/api/auth/me', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    // Si l'utilisateur n'est pas connecté, rediriger vers la page de connexion
    if (!data.value?.user) {
      return navigateTo('/login')
    }

    // Pour les routes admin, vérifier les droits d'administration
    if (to.path.startsWith('/admin') && !data.value.user.is_admin) {
      return navigateTo('/')
    }
  } catch (error) {
    console.error('Erreur d\'authentification:', error)
    return navigateTo('/login')
  }
}) 