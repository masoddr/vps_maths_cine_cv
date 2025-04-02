<template>
  <Transition name="fade">
    <div v-if="show" class="fixed inset-0 flex items-center justify-center z-50">
      <!-- Feux d'artifice -->
      <div class="fireworks">
        <div v-for="n in 5" :key="n" class="firework" :style="{ '--delay': `${n * 0.2}s` }"></div>
      </div>

      <div class="bg-white dark:bg-dark-800 rounded-lg shadow-xl p-6 max-w-sm mx-auto text-center transform transition-all duration-300 scale-100 animate-bounce-in relative">
        <div class="text-green-500 mb-4">
          <svg class="h-12 w-12 mx-auto animate-success" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <h3 class="text-lg font-medium text-gray-900 dark:text-gray-100">
          {{ message }}
        </h3>
        <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">
          {{ subMessage }}
        </p>
      </div>
    </div>
  </Transition>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  show: {
    type: Boolean,
    default: false
  }
})

const messages = [
  { main: '🌟 Bravo, c\'est excellent !', sub: 'Tu maîtrises de mieux en mieux' },
  { main: '🚀 Incroyable progression !', sub: 'Continue sur cette lancée' },
  { main: '💪 Tu es inarrêtable !', sub: 'Le succès se construit pas à pas' },
  { main: '🎯 Dans le mille !', sub: 'Ta persévérance paie' },
  { main: '🏆 Champion(ne) !', sub: 'Tu te rapproches du but' },
  { main: '⭐ Quelle performance !', sub: 'Le bac n\'a qu\'à bien se tenir' },
  { main: '🌈 Magnifique travail !', sub: 'Tu es sur la bonne voie' },
  { main: '✨ C\'est impressionnant !', sub: 'Garde ce rythme' },
  { main: '🎉 Félicitations !', sub: 'Un exercice de plus vers la réussite' },
  { main: '🌠 Tu brilles !', sub: 'Les maths n\'ont plus de secrets pour toi' }
]

const currentMessage = ref(messages[Math.floor(Math.random() * messages.length)])
const message = ref(currentMessage.value.main)
const subMessage = ref(currentMessage.value.sub)

watch(() => props.show, (newValue) => {
  if (newValue) {
    currentMessage.value = messages[Math.floor(Math.random() * messages.length)]
    message.value = currentMessage.value.main
    subMessage.value = currentMessage.value.sub
  }
})
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.animate-success {
  animation: success 0.5s ease-in-out;
}

@keyframes success {
  0% { transform: scale(0); }
  50% { transform: scale(1.2); }
  100% { transform: scale(1); }
}

.fireworks {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.firework {
  position: absolute;
  width: 10px;
  height: 10px;
  animation: firework 1s ease-out forwards;
  animation-delay: var(--delay);
}

.firework::before {
  content: '';
  position: absolute;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  background: radial-gradient(circle, 
    #ff0 0%, 
    #ff3 10%, 
    #f90 20%, 
    #f09 40%, 
    transparent 100%
  );
  animation: explosion 1s ease-out forwards;
  animation-delay: var(--delay);
}

@keyframes firework {
  0% {
    transform: translate(50vw, 100vh) scale(0);
  }
  50% {
    transform: translate(50vw, 50vh) scale(0);
  }
  100% {
    transform: translate(50vw, 50vh) scale(1);
  }
}

@keyframes explosion {
  0% {
    transform: scale(0);
    opacity: 1;
  }
  50% {
    transform: scale(1);
    opacity: 1;
  }
  100% {
    transform: scale(2);
    opacity: 0;
  }
}

/* Ajout de particules pour chaque feu d'artifice */
.firework::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 100%;
  height: 100%;
  transform: translate(-50%, -50%);
  background: radial-gradient(circle, 
    rgba(255, 255, 255, 0.8) 0%,
    rgba(255, 255, 255, 0) 100%
  );
  border-radius: 50%;
  animation: particles 1s ease-out forwards;
  animation-delay: calc(var(--delay) + 0.1s);
}

@keyframes particles {
  0% {
    transform: translate(-50%, -50%) scale(0);
    opacity: 1;
  }
  100% {
    transform: translate(-50%, -50%) scale(3);
    opacity: 0;
  }
}
</style> 