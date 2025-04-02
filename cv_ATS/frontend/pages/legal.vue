<template>
  <div class="max-w-4xl mx-auto px-4 py-12">
    <NuxtLink 
      to="/" 
      class="inline-flex items-center mb-8 text-gray-600 hover:text-blue-600 transition-colors duration-200"
    >
      <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
      </svg>
      Retour à l'accueil
    </NuxtLink>

    <h1 class="text-4xl font-bold mb-12 text-center text-gray-800">Mentions Légales</h1>
    
    <div class="prose prose-blue max-w-none">
      <div class="mb-12">
        <h2 class="text-2xl text-blue-600 mb-6">1. Éditeur du site</h2>
        <p class="bg-gray-50 p-4 rounded-lg text-gray-700">
          Optimise-ton-CV<br>
          Développé par : Massyl OUADDOUR<br>
          Email : ouaddour.massyl@gmail.com<br>
          Adresse : Paris, France
        </p>
      </div>

      <div class="mb-12">
        <h2 class="text-2xl text-blue-600 mb-6">2. Hébergement</h2>
        <p class="bg-gray-50 p-4 rounded-lg text-gray-700">
          Le site est hébergé par :<br>
          [Nom de l'hébergeur]<br>
          [Adresse de l'hébergeur]
        </p>
      </div>

      <h2>3. Propriété intellectuelle</h2>
      <p>
        L'ensemble des éléments constituant ce site (textes, images, code source, etc.) 
        est protégé par les lois relatives à la propriété intellectuelle.
      </p>

      <h2>4. Technologies utilisées</h2>
      <p>
        Ce site utilise les technologies suivantes :
      </p>
      <ul>
        <li>
          <strong>Groq</strong> : Service d'API pour l'intelligence artificielle.<br>
          Plus d'informations sur : <a href="https://groq.com" class="text-blue-600 hover:underline">https://groq.com</a>
        </li>
        <li>
          <strong>LLaMA</strong> : Modèle de langage développé par Meta AI.<br>
          Version utilisée : LLaMA 3.3 70B Versatile
        </li>
      </ul>

      <h2>5. Cookies</h2>
      <p>
        Ce site utilise des cookies techniques nécessaires à son fonctionnement. 
        Aucun cookie publicitaire n'est utilisé.
      </p>

      <h2>6. Responsabilité</h2>
      <p>
        Malgré les soins apportés, nous ne pouvons garantir l'exactitude, la précision 
        ou l'exhaustivité des informations mises à disposition sur ce site.
      </p>

      <h2>7. Droit applicable</h2>
      <p>
        Les présentes mentions légales sont soumises au droit français. En cas de litige, 
        les tribunaux français seront seuls compétents.
      </p>
    </div>
  </div>
</template> 