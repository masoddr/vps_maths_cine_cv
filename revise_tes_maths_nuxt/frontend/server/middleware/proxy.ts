import { defineEventHandler, proxyRequest } from 'h3'

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig()
  
  // Gérer uniquement les requêtes vers /api
  if (!event.path.startsWith('/api')) {
    return
  }

  // Rediriger les requêtes vers le backend
  return proxyRequest(event, `${config.public.apiBase}${event.path}`, {
    headers: {
      ...event.headers,
      host: new URL(config.public.apiBase).host
    }
  })
}) 