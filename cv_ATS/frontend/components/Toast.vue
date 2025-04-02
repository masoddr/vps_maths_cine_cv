<template>
  <div 
    v-if="isVisible"
    class="fixed bottom-4 right-4 z-50 animate-slideIn"
    :class="typeClasses"
  >
    <div class="flex items-center p-4 rounded-lg shadow-lg">
      <span class="mr-2" v-html="icon"></span>
      <p class="font-medium">{{ message }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  type: {
    type: String,
    default: 'info'
  },
  message: {
    type: String,
    required: true
  },
  isVisible: {
    type: Boolean,
    default: false
  }
})

const typeClasses = computed(() => ({
  'bg-green-100 text-green-800': props.type === 'success',
  'bg-red-100 text-red-800': props.type === 'error',
  'bg-blue-100 text-blue-800': props.type === 'info'
}))

const icon = computed(() => ({
  success: '✅',
  error: '❌',
  info: 'ℹ️'
}[props.type]))
</script>

<style scoped>
.animate-slideIn {
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}
</style> 