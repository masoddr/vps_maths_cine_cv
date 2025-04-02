import type { AuthResponse } from '~/types/auth'

export default defineNuxtRouteMiddleware(async (to) => {
  const config = useRuntimeConfig()
  
  try {
    // Vérifier si l'utilisateur est connecté et est admin
    const { data } = await useFetch<AuthResponse>('/api/auth/me', {
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    if (!data.value?.user?.is_admin) {
      // Rediriger vers la page d'accueil si l'utilisateur n'est pas admin
      return navigateTo('/')
    }
  } catch (error) {
    // En cas d'erreur (non connecté ou autre), rediriger vers la page de connexion
    return navigateTo('/login')
  }
}) 