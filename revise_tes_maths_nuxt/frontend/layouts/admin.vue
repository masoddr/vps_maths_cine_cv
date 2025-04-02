<template>
  <div class="min-h-screen bg-gray-100 dark:bg-dark-900">
    <!-- En-tête -->
    <nav class="bg-white dark:bg-dark-800 shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex">
            <!-- Logo -->
            <div class="flex-shrink-0 flex items-center">
              <NuxtLink to="/admin" class="text-xl font-bold text-indigo-600 dark:text-indigo-400">
                Administration
              </NuxtLink>
            </div>
            <!-- Navigation principale -->
            <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
              <NuxtLink 
                to="/admin/users" 
                class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100"
              >
                Utilisateurs
              </NuxtLink>
              <NuxtLink 
                to="/admin/annales" 
                class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100"
              >
                Annales
              </NuxtLink>
              <NuxtLink 
                to="/admin/messages" 
                class="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100"
              >
                Messages
              </NuxtLink>
            </div>
          </div>
          <!-- Boutons -->
          <div class="hidden sm:ml-6 sm:flex sm:items-center sm:space-x-4">
            <ThemeToggle />
            <NuxtLink 
              to="/" 
              class="text-sm font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-100"
            >
              Retour au site
            </NuxtLink>
          </div>
        </div>
      </div>
    </nav>

    <!-- Contenu principal -->
    <main class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
      <slot />
    </main>
  </div>
</template>

<script setup>
import ThemeToggle from '~/components/ThemeToggle.vue'
</script> 