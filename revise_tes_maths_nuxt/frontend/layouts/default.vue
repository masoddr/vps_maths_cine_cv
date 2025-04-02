<template>
  <div>
    <slot />
  </div>
</template>

<script setup>
async function handleLogout() {
  try {
    const response = await useFetch('/api/logout', {
      method: 'POST',
      baseURL: config.public.apiBase,
      credentials: 'include'
    })

    if (response.error.value) {
      throw new Error(response.error.value?.data?.error || 'Erreur lors de la déconnexion')
    }

    // Rediriger vers la page d'accueil et forcer le rechargement
    window.location.href = '/'
  } catch (error) {
    console.error('Erreur lors de la déconnexion:', error)
  }
}
</script> 