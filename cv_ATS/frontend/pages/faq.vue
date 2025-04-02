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

    <h1 class="text-4xl font-bold mb-12 text-center text-gray-800">Questions Fréquentes (FAQ)</h1>
    
    <div class="prose prose-blue max-w-none">
      <div class="space-y-12">
        <div>
          <h3 class="text-xl text-blue-600 mb-3">Qu'est-ce qu'un ATS ?</h3>
          <p class="bg-gray-50 p-4 rounded-lg text-gray-700">
            Un ATS (Applicant Tracking System) est un logiciel utilisé par les recruteurs pour gérer les candidatures. 
            Il analyse et filtre automatiquement les CV avant qu'ils ne soient lus par un humain.
          </p>
        </div>

        <div>
          <h3 class="text-xl text-blue-600 mb-3">Comment fonctionne l'analyse de CV ?</h3>
          <p class="bg-gray-50 p-4 rounded-lg text-gray-700">
            Notre système utilise l'intelligence artificielle (LLaMA via Groq) pour analyser votre CV selon plusieurs critères :
            structure, mots-clés, lisibilité, et compatibilité avec l'offre d'emploi si fournie.
          </p>
        </div>

        <div>
          <h3 class="text-xl text-blue-600 mb-3">Mes données sont-elles sécurisées ?</h3>
          <p class="bg-gray-50 p-4 rounded-lg text-gray-700">
            Oui. Vos données sont traitées de manière confidentielle, ne sont pas stockées de façon permanente, 
            et sont supprimées automatiquement après l'analyse.
          </p>
        </div>

        <div>
          <h3>Quels formats de CV sont acceptés ?</h3>
          <p>
            Vous pouvez soit copier-coller le texte de votre CV directement, soit télécharger un fichier PDF.
          </p>
        </div>

        <div>
          <h3>Le service est-il gratuit ?</h3>
          <p>
            Oui, le service est entièrement gratuit.
          </p>
        </div>

        <div>
          <h3 class="text-xl text-blue-600 mb-3">Comment améliorer mon score ?</h3>
          <p>
            Suivez les recommandations fournies dans l'analyse :
          </p>
          <ul class="mt-4 space-y-2 bg-gray-50 p-4 rounded-lg text-gray-700">
            <li>Intégrez les mots-clés manquants pertinents</li>
            <li>Améliorez la structure selon les suggestions</li>
            <li>Utilisez des formulations claires et directes</li>
            <li>Adaptez votre CV à l'offre d'emploi</li>
          </ul>
        </div>

        <div>
          <h3>Puis-je utiliser la version optimisée telle quelle ?</h3>
          <p>
            La version optimisée est une suggestion. Nous vous recommandons de l'utiliser comme base 
            tout en personnalisant le contenu pour refléter fidèlement votre profil.
          </p>
        </div>
      </div>
    </div>
  </div>
</template> 