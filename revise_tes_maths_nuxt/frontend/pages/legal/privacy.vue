<template>
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <h1 class="text-3xl font-bold text-gray-900 dark:text-gray-100 mb-8">
      Politique de Confidentialité
    </h1>

    <div class="prose dark:prose-invert max-w-none">
      <h2>1. Collecte des données personnelles</h2>
      <p>
        Dans le cadre de votre utilisation du site "Révise Tes Maths", nous collectons les données personnelles suivantes :
      </p>
      <ul>
        <li>Nom et prénom</li>
        <li>Adresse email</li>
        <li>Données de progression dans les exercices</li>
        <li>Historique de connexion</li>
      </ul>

      <h2>2. Utilisation des données</h2>
      <p>
        Vos données personnelles sont utilisées pour :
      </p>
      <ul>
        <li>Gérer votre compte et vous permettre d'accéder aux services</li>
        <li>Suivre votre progression dans les exercices</li>
        <li>Vous envoyer des notifications importantes concernant le service</li>
        <li>Améliorer nos services et votre expérience utilisateur</li>
      </ul>

      <h2>3. Conservation des données</h2>
      <p>
        Vos données personnelles sont conservées pendant la durée de votre inscription sur le site. 
        Vous pouvez demander la suppression de votre compte à tout moment, ce qui entraînera la 
        suppression de toutes vos données personnelles sous 30 jours.
      </p>

      <h2>4. Sécurité des données</h2>
      <p>
        Nous mettons en œuvre des mesures de sécurité appropriées pour protéger vos données personnelles :
      </p>
      <ul>
        <li>Chiffrement des mots de passe</li>
        <li>Connexions sécurisées (HTTPS)</li>
        <li>Accès restreint aux données personnelles</li>
        <li>Sauvegardes régulières</li>
      </ul>

      <h2>5. Cookies</h2>
      <p>
        Nous utilisons des cookies essentiels pour :
      </p>
      <ul>
        <li>Maintenir votre session de connexion</li>
        <li>Mémoriser vos préférences (thème sombre/clair)</li>
        <li>Assurer le bon fonctionnement du site</li>
      </ul>

      <h2>6. Vos droits</h2>
      <p>
        Conformément au RGPD, vous disposez des droits suivants :
      </p>
      <ul>
        <li>Droit d'accès à vos données</li>
        <li>Droit de rectification</li>
        <li>Droit à l'effacement</li>
        <li>Droit à la portabilité des données</li>
        <li>Droit d'opposition au traitement</li>
      </ul>

      <h2>7. Contact</h2>
      <p>
        Pour exercer vos droits ou pour toute question concernant la protection de vos données, 
        vous pouvez nous contacter à l'adresse : [EMAIL_DE_CONTACT]
      </p>

      <h2>8. Modifications</h2>
      <p>
        Nous nous réservons le droit de modifier cette politique de confidentialité. Les modifications 
        importantes vous seront notifiées par email ou via le site.
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