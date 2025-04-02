<template>
  <div class="flex justify-between mb-8">
    <div 
      v-for="(step, index) in steps" 
      :key="index"
      class="flex items-center"
    >
      <div 
        class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium"
        :class="[
          currentStep > index 
            ? 'bg-green-500 text-white' 
            : currentStep === index 
              ? 'bg-blue-500 text-white'
              : 'bg-gray-200 text-gray-500'
        ]"
      >
        {{ index + 1 }}
      </div>
      <div 
        v-if="index < steps.length - 1" 
        class="flex-1 h-1 mx-4"
        :class="[
          currentStep > index ? 'bg-green-500' : 'bg-gray-200'
        ]"
      ></div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  steps: {
    type: Array,
    required: true
  },
  currentStep: {
    type: Number,
    default: 0
  }
})
</script> 