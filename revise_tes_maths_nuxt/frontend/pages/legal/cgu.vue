<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <h1 class="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">
      Conditions Générales d'Utilisation
    </h1>

    <div class="prose dark:prose-invert max-w-none">
      <h2>1. Objet</h2>
      <p>
        Les présentes Conditions Générales d'Utilisation (CGU) régissent l'utilisation du site "Révise Tes Maths" 
        accessible à l'adresse [URL_DU_SITE]. Ce site est une plateforme éducative permettant aux élèves de réviser 
        les mathématiques pour le baccalauréat.
      </p>

      <h2>2. Accès au service</h2>
      <p>
        L'accès au service nécessite une inscription préalable. L'utilisateur s'engage à fournir des informations 
        exactes et à maintenir ces informations à jour. Le service est réservé aux élèves préparant le baccalauréat.
      </p>

      <h2>3. Compte utilisateur</h2>
      <p>
        L'utilisateur est responsable de la confidentialité de ses identifiants de connexion. Toute utilisation du 
        service avec ses identifiants est réputée avoir été effectuée par l'utilisateur.
      </p>

      <h2>4. Contenu</h2>
      <p>
        Les annales et exercices proposés sont la propriété de leurs auteurs respectifs. Leur utilisation est 
        strictement réservée à un usage personnel dans le cadre de la préparation au baccalauréat.
      </p>

      <h2>5. Responsabilités</h2>
      <p>
        Le site s'efforce d'assurer la disponibilité du service et l'exactitude des informations fournies. 
        Cependant, il ne peut être tenu responsable des erreurs ou omissions dans le contenu.
      </p>

      <h2>6. Propriété intellectuelle</h2>
      <p>
        L'ensemble du contenu du site (textes, images, logos, etc.) est protégé par le droit d'auteur. Toute 
        reproduction non autorisée est interdite.
      </p>

      <h2>7. Protection des données</h2>
      <p>
        Les données personnelles sont traitées conformément à notre politique de confidentialité, accessible 
        <NuxtLink to="/legal/privacy" class="text-indigo-600 dark:text-indigo-400 hover:underline">ici</NuxtLink>.
      </p>

      <h2>8. Modification des CGU</h2>
      <p>
        Les présentes CGU peuvent être modifiées à tout moment. Les utilisateurs seront informés des modifications 
        importantes par email ou notification sur le site.
      </p>

      <h2>9. Contact</h2>
      <p>
        Pour toute question concernant ces CGU, vous pouvez nous contacter à l'adresse : [EMAIL_DE_CONTACT]
      </p>

      <p class="text-sm text-gray-500 dark:text-gray-400 mt-8">
        Dernière mise à jour : {{ new Date().toLocaleDateString('fr-FR') }}
      </p>
    </div>
  </div>
</template>

<script setup>
definePageMeta({
  layout: 'default'
})
</script> 