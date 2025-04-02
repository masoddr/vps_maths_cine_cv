<template>
  <nav class="fixed top-0 left-0 right-0 bg-gray-800 shadow-md z-50">
    <div class="container mx-auto px-4">
      <div class="flex justify-between items-center h-16">
        <!-- Logo -->
        <div class="flex items-center">
          <NuxtLink to="/" class="flex items-center gap-2">
            <img 
              src="/images/logo.png" 
              alt="Logo Cinémas Toulouse" 
              class="h-8 w-8"
            />
            <span class="text-xl font-semibold text-white">
              Cinéphoria
            </span>
          </NuxtLink>
        </div>

        <!-- Menu desktop -->
        <div class="hidden md:flex space-x-8">
          <NuxtLink 
            to="/films" 
            class="text-gray-300 hover:text-white transition-colors"
            :class="{ 'text-white font-medium': route.path === '/films' }"
          >
            Séances
          </NuxtLink>
          <NuxtLink 
            to="/cinemas" 
            class="text-gray-300 hover:text-white transition-colors"
            :class="{ 'text-white font-medium': route.path === '/cinemas' }"
          >
            Cinémas
          </NuxtLink>
        </div>

        <!-- Bouton hamburger -->
        <button 
          @click="isMenuOpen = !isMenuOpen"
          class="md:hidden p-2"
          aria-label="Menu"
        >
          <div class="w-6 h-5 relative flex flex-col justify-between">
            <span 
              class="w-full h-0.5 bg-white transition-all duration-300"
              :class="{ 'rotate-45 translate-y-2': isMenuOpen }"
            ></span>
            <span 
              class="w-full h-0.5 bg-white transition-all duration-300"
              :class="{ 'opacity-0': isMenuOpen }"
            ></span>
            <span 
              class="w-full h-0.5 bg-white transition-all duration-300"
              :class="{ '-rotate-45 -translate-y-2': isMenuOpen }"
            ></span>
          </div>
        </button>
      </div>

      <!-- Menu mobile -->
      <div 
        v-show="isMenuOpen"
        class="md:hidden fixed left-0 right-0 bg-gray-700 border-t border-gray-600"
        :class="{ 'animate-slide-in': isMenuOpen }"
      >
        <div class="py-4 space-y-4">
          <NuxtLink 
            to="/films" 
            class="block px-4 py-2 text-gray-300 hover:bg-gray-600 hover:text-white"
            :class="{ 'text-white bg-gray-600': route.path === '/films' }"
            @click="isMenuOpen = false"
          >
            Séances
          </NuxtLink>
          <NuxtLink 
            to="/cinemas" 
            class="block px-4 py-2 text-gray-300 hover:bg-gray-600 hover:text-white"
            :class="{ 'text-white bg-gray-600': route.path === '/cinemas' }"
            @click="isMenuOpen = false"
          >
            Cinémas
          </NuxtLink>
        </div>
      </div>
    </div>
  </nav>

  <!-- Spacer pour compenser la navbar fixe -->
  <div class="h-16"></div>
</template>

<script setup lang="ts">
const route = useRoute()
const isMenuOpen = ref(false)

// Fermer le menu quand on change de route
watch(
  () => route.path,
  () => {
    isMenuOpen.value = false
  }
)
</script>

<style scoped>
.animate-slide-in {
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    transform: translateY(-100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
</style> 