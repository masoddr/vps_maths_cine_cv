<template>
  <footer class="bg-gray-100 mt-auto">
    <div class="max-w-7xl mx-auto py-8 px-4">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <!-- Informations légales -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Informations légales</h3>
          <ul class="space-y-2">
            <li><NuxtLink to="/mentions-legales" class="hover:text-primary">Mentions légales</NuxtLink></li>
            <li><NuxtLink to="/cgu" class="hover:text-primary">Conditions générales d'utilisation</NuxtLink></li>
            <li><NuxtLink to="/confidentialite" class="hover:text-primary">Politique de confidentialité</NuxtLink></li>
          </ul>
        </div>

        <!-- Contact -->
        <div>
          <h3 class="text-lg font-semibold mb-4">Contact</h3>
          <ul class="space-y-2">
            <li><NuxtLink to="/contact" class="hover:text-primary">Me contacter</NuxtLink></li>
            <li><a href="mailto:ouaddour.massyl@gmail.com" class="hover:text-primary">ouaddour.massyl@gmail.com</a></li>
          </ul>
        </div>

        <!-- À propos -->
        <div>
          <h3 class="text-lg font-semibold mb-4">À propos</h3>
          <ul class="space-y-2">
            <li><NuxtLink to="/a-propos" class="hover:text-primary">À propos de nous</NuxtLink></li>
            <li><NuxtLink to="/faq" class="hover:text-primary">FAQ</NuxtLink></li>
          </ul>
        </div>
      </div>
      
      <div class="text-center mt-8 pt-8 border-t border-gray-200">
        <p class="text-sm text-gray-600 mb-2">
          © {{ new Date().getFullYear() }} cinemas-toulouse. Tous droits réservés.
        </p>
        <p class="text-sm text-gray-600">
          Site créé par 
          <a 
            href="https://masoddr.github.io/portfolio_massyl/" 
            target="_blank" 
            rel="noopener noreferrer" 
            class="text-primary hover:underline"
          >
            Massyl OUADDOUR
          </a>
        </p>
      </div>
    </div>
  </footer>
</template> 