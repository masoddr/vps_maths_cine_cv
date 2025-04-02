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

    <h1 class="text-4xl font-bold mb-12 text-center text-gray-800">Guide d'utilisation</h1>
    
    <div class="prose prose-blue max-w-none">
      <h2 class="text-2xl text-blue-600 mb-8">Comment utiliser Optimise-ton-CV?</h2>
      
      <div class="mb-12">
        <h3 class="text-xl text-gray-800 mb-4">1. Importation de votre CV</h3>
        <p>Deux méthodes sont disponibles :</p>
        <ul class="mt-4 space-y-3">
          <li>
            <strong>Copier-coller</strong> : Copiez le contenu de votre CV et collez-le directement dans la zone de texte.
          </li>
          <li>
            <strong>Upload PDF</strong> : Téléchargez votre CV au format PDF en le glissant dans la zone prévue ou en cliquant pour sélectionner le fichier.
          </li>
        </ul>
      </div>

      <div class="mb-12">
        <h3 class="text-xl text-gray-800 mb-4">2. Ajout d'une offre d'emploi (optionnel)</h3>
        <p>
          Pour une analyse plus pertinente, vous pouvez ajouter le texte de l'offre d'emploi qui vous intéresse. 
          Cela permettra d'évaluer la compatibilité de votre CV avec les exigences du poste.
        </p>
      </div>

      <div class="mb-12">
        <h3 class="text-xl text-gray-800 mb-4">3. Analyse du CV</h3>
        <p>L'analyse comprend :</p>
        <ul class="mt-4 space-y-2">
          <li>Vérification de la structure et du format</li>
          <li>Identification des mots-clés importants</li>
          <li>Évaluation de la lisibilité ATS</li>
          <li>Analyse du contenu et de l'impact</li>
          <li>Score de compatibilité avec l'offre (si fournie)</li>
        </ul>
      </div>

      <div class="mb-12">
        <h3 class="text-xl text-gray-800 mb-4">4. Interprétation des résultats</h3>
        <p>Votre rapport d'analyse inclut :</p>
        <ul class="mt-4 space-y-2">
          <li>Un score global sur 20 points</li>
          <li>Des scores détaillés par catégorie (sur 5 points)</li>
          <li>Une liste des mots-clés présents et manquants</li>
          <li>Des suggestions d'amélioration concrètes</li>
          <li>Une version optimisée de votre CV</li>
        </ul>
      </div>

      <div class="mb-12">
        <h3 class="text-xl text-gray-800 mb-4">5. Optimisation</h3>
        <p>Pour améliorer votre CV :</p>
        <ul class="mt-4 space-y-2">
          <li>Intégrez les mots-clés manquants pertinents</li>
          <li>Suivez les recommandations de structure</li>
          <li>Utilisez les suggestions de formulation</li>
          <li>Téléchargez la version optimisée proposée</li>
        </ul>
      </div>

      <div class="bg-blue-50 p-6 rounded-lg">
        <h2 class="text-2xl text-blue-600 mb-4">Conseils pour de meilleurs résultats</h2>
        <ul class="space-y-3 text-gray-700">
          <li>Utilisez un format simple et clair</li>
          <li>Évitez les tableaux et les mises en page complexes</li>
          <li>Privilégiez le texte brut aux images</li>
          <li>Vérifiez que votre PDF est bien lisible et sélectionnable</li>
        </ul>
      </div>
    </div>
  </div>
</template> 