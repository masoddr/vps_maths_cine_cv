<template>
  <div class="bg-white shadow">
    <div class="container mx-auto px-4">
      <div class="flex space-x-2 py-4 overflow-x-auto">
        <button
          v-for="day in availableDays"
          :key="day"
          @click="selectDay(day)"
          class="px-4 py-2 rounded-full whitespace-nowrap"
          :class="selectedDay === day ? 'bg-blue-500 text-white' : 'bg-gray-100 hover:bg-gray-200'"
        >
          {{ formatDate(day) }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useSeancesStore } from '~/stores/seances'
import { storeToRefs } from 'pinia'

const store = useSeancesStore()
const { seancesByDay } = storeToRefs(store)

const availableDays = computed(() => Object.keys(seancesByDay.value).sort())
const selectedDay = ref(availableDays.value[0] || '')

const emit = defineEmits(['update:day'])

function selectDay(day: string) {
  selectedDay.value = day
  emit('update:day', day)
}

const formatDate = (dateStr: string) => {
  return new Date(dateStr).toLocaleDateString('fr-FR', {
    weekday: 'long',
    day: 'numeric',
    month: 'long'
  })
}
</script> 