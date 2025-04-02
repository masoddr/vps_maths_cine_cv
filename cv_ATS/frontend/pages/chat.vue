<template>
  <div class="max-w-4xl mx-auto">
    <div class="bg-white shadow rounded-lg p-6">
      <div class="space-y-4 mb-4 h-[500px] overflow-y-auto">
        <!-- Messages will go here -->
      </div>
      <div class="mt-4">
        <form @submit.prevent="sendMessage" class="flex gap-2">
          <input
            v-model="message"
            type="text"
            class="flex-1 rounded-lg border border-gray-300 px-4 py-2"
            placeholder="Tapez votre message..."
          />
          <button
            type="submit"
            class="bg-blue-500 text-white px-6 py-2 rounded-lg hover:bg-blue-600"
          >
            Envoyer
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
const message = ref('')

const sendMessage = () => {
  // TODO: Implémenter l'envoi du message
  console.log('Message à envoyer:', message.value)
  message.value = ''
}
</script> 