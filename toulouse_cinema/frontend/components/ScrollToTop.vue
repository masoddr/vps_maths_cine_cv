<template>
  <button
    @click="scrollToTop"
    class="fixed bottom-8 right-8 bg-gray-800 text-white p-4 rounded-full shadow-lg hover:bg-gray-700 transition-all duration-300 z-50"
    :class="{ 'translate-y-20': !isVisible, 'translate-y-0': isVisible }"
    aria-label="Retour en haut"
  >
    <svg 
      xmlns="http://www.w3.org/2000/svg" 
      class="h-8 w-8" 
      fill="none" 
      viewBox="0 0 24 24" 
      stroke="currentColor"
    >
      <path 
        stroke-linecap="round" 
        stroke-linejoin="round" 
        stroke-width="2" 
        d="M5 10l7-7m0 0l7 7m-7-7v18"
      />
    </svg>
  </button>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const isVisible = ref(false)

const checkScroll = () => {
  isVisible.value = window.scrollY > 300
}

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  })
}

onMounted(() => {
  window.addEventListener('scroll', checkScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', checkScroll)
})
</script>

<style scoped>
button {
  opacity: 0.75;
  transition: all 0.3s ease;
}

button:hover {
  opacity: 1;
  transform: translateY(-4px);
}
</style> 