<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-blue-50 py-16">
    <div class="max-w-4xl mx-auto px-4">
      <!-- Bouton retour -->
      <NuxtLink 
        to="/" 
        class="inline-flex items-center mb-8 text-gray-600 hover:text-blue-600 transition-colors duration-200"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Retour à l'accueil
      </NuxtLink>

      <div class="bg-white rounded-2xl shadow-xl p-8 mb-8">
        <h1 class="text-3xl font-bold text-center mb-8">Contactez-moi</h1>

        <div class="grid md:grid-cols-2 gap-8">
          <!-- Informations de contact -->
          <div class="space-y-6">
            <h2 class="text-xl font-semibold text-gray-800 mb-4">Informations</h2>
            <div class="flex items-center space-x-3 text-gray-600">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
              <a href="mailto:ouaddour.massyl@gmail.com" class="hover:text-blue-600 transition-colors">
                ouaddour.massyl@gmail.com
              </a>
            </div>
            <div class="flex items-center space-x-3 text-gray-600">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <a href="https://www.linkedin.com/in/massylouaddour/" target="_blank" rel="noopener noreferrer" class="hover:text-blue-600 transition-colors">
                LinkedIn
              </a>
            </div>
          </div>

          <!-- Formulaire de contact -->
          <form @submit.prevent="sendContactForm" class="space-y-6">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Nom</label>
              <input
                id="name"
                v-model="contactForm.name"
                type="text"
                required
                class="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
            </div>

            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <input
                id="email"
                v-model="contactForm.email"
                type="email"
                required
                class="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              >
            </div>

            <div>
              <label for="message" class="block text-sm font-medium text-gray-700 mb-1">Message</label>
              <textarea
                id="message"
                v-model="contactForm.message"
                rows="4"
                required
                class="w-full px-4 py-2 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none"
              ></textarea>
            </div>

            <button
              type="submit"
              :disabled="isSubmitting"
              class="w-full px-6 py-3 bg-blue-600 text-white rounded-lg font-medium hover:bg-blue-700 transition-colors duration-200 disabled:opacity-50"
            >
              {{ isSubmitting ? 'Envoi en cours...' : 'Envoyer' }}
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const contactForm = ref({
  name: '',
  email: '',
  message: ''
})

const isSubmitting = ref(false)

const sendContactForm = async () => {
  isSubmitting.value = true
  try {
    const subject = `Contact Optimise-ton-CV- ${contactForm.value.name}`
    const body = `Message de : ${contactForm.value.name}\nEmail : ${contactForm.value.email}\n\n${contactForm.value.message}`
    const mailtoLink = `mailto:ouaddour.massyl@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`
    
    window.location.href = mailtoLink
    
    contactForm.value = {
      name: '',
      email: '',
      message: ''
    }
  } catch (error) {
    console.error('Erreur:', error)
  } finally {
    isSubmitting.value = false
  }
}
</script> 