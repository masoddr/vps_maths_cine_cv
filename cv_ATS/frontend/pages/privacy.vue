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

    <h1 class="text-4xl font-bold mb-12 text-center text-gray-800">Politique de Confidentialité</h1>
    
    <div class="prose prose-blue max-w-none">
      <div class="mb-12">
        <h2 class="text-2xl text-blue-600 mb-6">1. Collecte des données</h2>
        <p>
          Nous collectons les informations suivantes :
        </p>
        <ul class="mt-4 space-y-2 bg-gray-50 p-4 rounded-lg text-gray-700">
          <li>Le contenu des CV soumis pour analyse</li>
          <li>Les offres d'emploi soumises pour comparaison</li>
          <li>Les informations de contact fournies volontairement</li>
        </ul>
      </div>

      <h2>2. Utilisation des données</h2>
      <p>
        Les données collectées sont utilisées pour :
      </p>
      <ul>
        <li>Fournir le service d'analyse de CV</li>
        <li>Traiter les analyses via les services Groq et le modèle LLaMA</li>
        <li>Répondre aux demandes de support</li>
      </ul>

      <h2>3. Traitement par l'Intelligence Artificielle</h2>
      <p>
        Votre CV est analysé par :
      </p>
      <ul>
        <li>Le service Groq, qui fournit l'infrastructure d'intelligence artificielle</li>
        <li>Le modèle LLaMA 3.3 70B Versatile, un modèle de langage développé par Meta AI</li>
      </ul>
      <p>
        Important : 
      </p>
      <ul>
        <li>Vos données sont traitées de manière confidentielle</li>
        <li>Les CV sont analysés en temps réel et ne sont pas stockés de manière permanente</li>
        <li>Aucune donnée personnelle n'est utilisée pour entraîner les modèles d'IA</li>
      </ul>

      <h2>4. Protection des données</h2>
      <p>
        Nous mettons en œuvre des mesures de sécurité pour protéger vos données :
      </p>
      <ul>
        <li>Chiffrement des données en transit</li>
        <li>Accès restreint aux données personnelles</li>
        <li>Suppression automatique des CV après analyse</li>
        <li>Transmission sécurisée vers les services d'IA</li>
      </ul>

      <h2>5. Vos droits</h2>
      <p>
        Conformément au RGPD, vous disposez des droits suivants :
      </p>
      <ul>
        <li>Droit d'accès à vos données</li>
        <li>Droit de rectification</li>
        <li>Droit à l'effacement</li>
        <li>Droit à la portabilité</li>
      </ul>

      <h2>6. Contact</h2>
      <p>
        Pour exercer vos droits ou pour toute question, contactez-nous à :
        <a href="mailto:ouaddour.massyl@gmail.com">ouaddour.massyl@gmail.com</a>
      </p>
    </div>
  </div>
</template> 