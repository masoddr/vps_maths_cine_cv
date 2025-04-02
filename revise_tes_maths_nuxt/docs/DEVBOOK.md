DEVBOOK - Dashboard Révisions Bac
0. Contexte

Le projet consiste à développer un Dashboard web (accessible via un navigateur) pour le suivi des révisions du bac. L'application permettra aux élèves de :

    Créer un compte (authentification, gestion du profil).
    Consulter des annales (sujets d'examens passés).
    Visualiser pour chaque exercice les thématiques abordées.
    Accéder aux PDF correspondants.
    Suivre l'avancement de leurs révisions (progression par exercice, par matière, etc.).

Technologies majeures

    Front : Nuxt.js (basé sur Vue.js)
    Back : Flask + SQLAlchemy
    Hébergement : VPS (Nginx/Traefik, Gunicorn, etc.)
    Base de données : PostgreSQL/MySQL

Cette application sera déployée en mode Front/Back séparés :

    Le Front (Nuxt) pourra être déployé sur Vercel/Netlify ou servi via Nginx sur le VPS.
    Le Back (Flask) sera géré par Gunicorn + Nginx (ou Traefik) sur le VPS.

1. Méthodologie TDD 🎯

Pour chaque fonctionnalité (front ou back) :

    - Écrire les tests d'abord (tests unitaires, d'intégration, e2e).
    - Implémenter la fonctionnalité pour répondre aux tests.
    - Lancer les tests et vérifier qu'ils passent.
    - Corriger si nécessaire (jusqu'à obtention du vert).
    - Refactoriser le code tout en gardant les tests au vert.
    - Mettre à jour ce DevBook, la documentation & les issues.
    - Demande une validation pour : Commit & push avec un message de commit parlant (cf. Conventions).
Quand il s'agit du frontend, prendre en compte le fichier DESIGN.md.

2. Étapes du Projet 📋
2.1. Configuration Initiale ⚙️ [✓]

[x] Backend : Créer un environnement virtuel Python, installer Flask, Pytest, SQLAlchemy, etc.
[x] Frontend : Initialiser un projet Nuxt (via npx nuxi init ou équivalent)
[x] Organisation du dépôt :
    [x] Structure backend/frontend établie
[x] Premier test :
    [x] Backend : "Hello World" route + test Pytest
    [x] Frontend : Page Nuxt "index.vue" créée

2.2. Base de Données (Backend) 🗄️ [✓]

[x] Configurer SQLAlchemy (connexion à PostgreSQL)
[x] Écrire les tests des modèles (Pytest)
[x] Implémenter les modèles :
    [x] User : Email, Password hash, Rôle (élève/admin), etc.
    [x] Subject : Matière Mathématiques, une seule pour l'instant
    [x] ExamPaper (annale) : Titre, Année, Lien PDF, Référence à Subject
    [x] Exercise : Lié à un ExamPaper, énoncé, thématique, etc.
    [x] Progress : Table de liaison (User <-> Exercise), statut (en cours/terminé), etc.
[x] Configurer Alembic ou Flask-Migrate pour les migrations
[x] Tests d'intégration DB (insertion, lecture, suppression)
[x] Mise à jour des champs datetime pour utiliser UTC
[x] Mise à jour de SQLAlchemy pour utiliser les nouvelles API (Session.get)

2.3. Authentification (Backend) 🔐 [✓]

[x] Tests des routes d'authentification (inscription, connexion, etc.)
[x] Implémenter Flask-Login
[x] Routes :
    [x] /api/register
    [x] /api/login
    [x] /api/logout
    [ ] /api/reset-password (optionnel)
[x] Gestion des sessions ou tokens pour sécuriser les échanges
[x] Tests d'intégration auth : création de compte, connexion, etc.
[x] Configuration de l'authentification API (401 au lieu de redirection)

2.4. Gestion de la Progression (Backend) 📊 [✓]

[x] Tests des routes de progression
[x] Routes :
    [x] /api/progress (GET : liste des progressions)
    [x] /api/progress/<exercise_id> (PUT : mettre à jour le statut)
    [x] /api/progress/<exercise_id>/notes (PUT : mettre à jour les notes)
    [x] /api/progress/stats (GET : statistiques)
[x] Tests d'intégration : manipuler le statut d'un exercice, vérifier la cohérence des données
[x] Validation des statuts de progression
[x] Calcul des statistiques de progression

2.5. Gestion des Annales (Backend) 📚 [✓]

[x] Tests upload/download PDF (API)
[x] Système de stockage :
    [x] Serveur local (chemin sécurisé)
    [ ] Service distant (S3) - Optionnel pour plus tard
[x] Routes :
    [x] /api/exampapers (GET : liste + filtres, POST : upload)
    [x] /api/exampapers/{id} (GET : détail, PUT : mise à jour, DELETE : suppression)
    [x] /api/exampapers/{id}/pdf (GET : téléchargement du PDF)
[x] Tests d'intégration : vérifier l'upload, la lecture et la suppression
[x] Enrichir les données de test :
    [x] Ajouter des exercices avec leurs thématiques (Probabilités, Géométrie, etc.)
    [x] Lier les exercices aux annales existantes
    [x] Ajouter des données de progression pour les tests

2.6. Interface Admin (Backend) 👑 [✓]

[x] Tests admin : vérification accès restreint, modification d'utilisateurs
[x] Middleware admin : décorateur ou contrôle d'accès sur les routes /admin
[x] Routes :
    [x] /api/admin/users (gestion utilisateurs)
    [x] /api/admin/exampapers (gestion annales)
[x] Tests d'intégration admin : test CRUD sur les utilisateurs, vérification des autorisations

2.7. Frontend Nuxt : Structure & Thèmes 🎨 [✓]

[x] Installer Nuxt et Tailwind dans Nuxt
[x] Configurer la structure : pages, layouts (header, footer), composants réutilisables
[x] Mise en place des routes Nuxt :
    [x] /login
    [x] /register
    [x] /dashboard (pour l'élève)
    [x] /annales
[x] Tests (Jest/Cypress) : vérifier l'affichage de la home, le routage, etc.

2.8. Frontend Nuxt : Authentification 🔑 [✓]

[x] Tests : scénarios d'inscription, connexion, déconnexion
[x] Intégration avec l'API Flask
[x] Pages / Composants :
    [x] pages/login.vue, pages/register.vue
    [x] Formulaires + validations
[x] Tests e2e : flux "Je m'inscris, je me connecte, je consulte mon compte"

2.9. Frontend Nuxt : Consultation des Annales 📚 [✓]

[x] Tests : chargement de la liste des annales, affichage des détails
[x] Intégration avec /api/exampapers (list, detail)
[x] Composant carte d'annale (titre, année, lien PDF)
[x] Affichage PDF : soit en iFrame, soit lien de téléchargement
[x] Tests d'intégration (Jest/Cypress)
[x] Ajout des fonctionnalités avancées :
    [x] Système de recherche par mot-clé
    [x] Filtrage par année et thème
    [x] Tri par date
    [x] Pagination
    [x] Vue détaillée des annales
    [x] Tags pour les concepts abordés

2.10. Frontend Nuxt : Suivi de Progression 📊 [✓]

[x] Tests : marquer un exercice comme terminé, calculer la progression
[x] Appels à l'API /api/progress et /api/progress/stats
[x] Tableau de bord : composant(s) pour afficher un résumé
    [x] Carte de progression globale
    [x] Carte de temps de révision
    [x] Carte des thèmes maîtrisés
    [x] Liste des derniers exercices avec statut
[x] Tests e2e : simuler un user cochant des exercices

2.11. UI/UX Avancé 🎨 [✓]

[x] Composants :
    [x] Barres de progression ou graphiques
    [x] Tableaux filtrables pour les annales/exercices
[x] Responsive design : tester sur mobile, tablette, desktop
[x] Transitions Nuxt : animations entre les pages
[x] Tests : cas d'affichage adaptif, zoom PDF, etc.
    [x] Tests responsive sur différents appareils
    [x] Tests du composant de visualisation PDF
    [x] Tests des contrôles de zoom et navigation
    [x] Tests d'accessibilité sur mobile
[x] Mode sombre :
    [x] Configuration Tailwind
    [x] Composant ThemeToggle
    [x] Adaptation des composants
    [x] Tests des transitions de thème

2.12. Sécurité & RGPD 🛡️ [En cours]

[x] Tests de sécurité : protection CSRF, XSS, injections
[x] Implémentation :
    [x] CSRF (sur Flask et/ou via tokens pour Nuxt)
    [x] Rate limiting (Flask-Limiter)
    [x] Validation stricte des données
[ ] Pages légales (front) :
    [ ] CGU
    [ ] Politique de confidentialité
[ ] Tests de pénétration basiques

2.13. Déploiement 🚀 [En cours]

[x] Backend (Flask) :
    [x] Configuration VPS (Ubuntu, firewall, users)
    [x] Installation : Gunicorn, Nginx (ou Traefik)
    [x] Mise en place SSL (Let's Encrypt)
    [ ] Scripts déploiement
[ ] Frontend (Nuxt) :
    [ ] Mode SSR ou SSG
    [ ] Hébergement : Netlify/Vercel ou VPS
[ ] Tests de production :
    [ ] Vérifier que l'API est fonctionnelle via HTTPS
    [ ] Vérifier que le front communique bien avec l'API
    [ ] Documentation : guides d'installation & de mise à jour


3. Conventions 📝
3.1. Format des Commits

    feat: … : nouvelle fonctionnalité
    fix: … : correction de bug
    test: … : ajout/modification de tests
    docs: … : documentation
    refactor: … : refactorisation de code
    style: … : formatage, indentation, style, pas de changement de code
    chore: … : tâches diverses (mise à jour dépendances, scripts)

3.2. Branches

    main : branche de production (stable)
    develop : branche de développement (intégration)
    feature/* : nouvelles fonctionnalités
    hotfix/* : corrections urgentes sur la production

4. Validation ✅

Pour valider chaque étape :

    Tous les tests passent (Pytest côté back, Jest/Cypress côté front)
    Documentation à jour (DevBook, README, swagger si besoin)
    Pas de régression sur les fonctionnalités déjà validées

    Tests de types et validations :
    Vérifier que toutes les données reçues de l'API sont du type attendu
    Ajouter des interfaces TypeScript pour tous les modèles de données
    Implémenter des validateurs de données côté frontend
    Documenter les structures de données attendues

    Documentation des endpoints API :
        Maintenir une liste à jour des endpoints avec leurs méthodes HTTP
        Documenter les payloads attendus et les réponses
        Vérifier la cohérence entre la documentation et l'implémentation
        Tester systématiquement les endpoints avec Postman ou similaire

    Gestion des erreurs :
        Vérifier tous les cas d'utilisation de .split(), .map(), etc.
        Ajouter des gardes de type (type guards) pour les données critiques
        Implémenter des fallbacks pour les données manquantes ou malformées
        Logger les erreurs de type et de données pour le debugging

    Conventions de validation :
        Toujours vérifier le type des données avant manipulation
        Documenter les formats attendus (dates, nombres, chaînes)
        Implémenter des fonctions de validation réutilisables
        Ajouter des tests unitaires pour les conversions de données

    Checklist avant modification :
        Vérifier les types de données dans les composants
        Tester les cas limites (undefined, null, formats invalides)
        Valider les manipulations de chaînes et dates
        S'assurer que les données correspondent aux interfaces TypeScript

4.1 Prévention des Bugs de Type et de Filtrage 🐛

    Validation des Types :
        Toujours utiliser parseInt/parseFloat pour les conversions de chaînes en nombres
        Définir des types TypeScript stricts pour les props et les données d'API
        Implémenter des fonctions de validation pour les données critiques
        Utiliser des types discriminants pour les unions de types

    Filtrage et Comparaison :
        Normaliser les types avant comparaison (ex: string vs number)
        Utiliser des comparaisons strictes (=== au lieu de ==)
        Documenter les formats attendus dans les filtres
        Tester les cas limites des filtres (valeurs vides, types mixtes)

    Tests Spécifiques :
        Ajouter des tests pour les conversions de types
        Tester les filtres avec différents formats de données
        Vérifier le comportement avec des données invalides
        Tester les cas de comparaison mixte (string vs number)
        Tests de filtrage des thèmes :
            - Vérifier la correspondance exacte des thèmes
            - Tester l'insensibilité à la casse
            - Valider le comportement avec des thèmes similaires
            - Vérifier le comportement avec des caractères spéciaux
            - Tester les thèmes composés (ex: "Géométrie dans l'espace")

    Bonnes Pratiques :
        Centraliser les fonctions de conversion et validation
        Documenter les hypothèses sur les types de données
        Logger les erreurs de conversion pour le debugging
        Implémenter des fallbacks pour les données invalides

    Revue de Code :
        Vérifier systématiquement les conversions de types
        Valider les comparaisons dans les filtres
        S'assurer que les tests couvrent les cas limites
        Documenter les choix de conception pour les types

5. Documentation API 📚

5.1. Endpoints de Progression
- GET /api/progress
  - Description : Récupère la liste des exercices avec leur progression
  - Authentification requise : Oui
  - Réponse : Liste des exercices avec leur statut

- PUT /api/progress/<exercise_id>
  - Description : Met à jour le statut d'un exercice
  - Authentification requise : Oui
  - Payload : { "status": "completed" | "in_progress" | "not_started" }

- PUT /api/progress/<exercise_id>/notes
  - Description : Met à jour les notes d'un exercice
  - Authentification requise : Oui
  - Payload : { "notes": "string" }

- GET /api/progress/stats
  - Description : Récupère les statistiques de progression
  - Authentification requise : Oui
  - Réponse : {
      "global": number,
      "completedExercises": number,
      "totalExercises": number,
      "totalHours": number,
      "masteredTopics": number,
      "totalTopics": number
    }

5.2. Endpoints d'Authentification
- POST /api/login
  - Description : Connexion utilisateur
  - Payload : { "email": "string", "password": "string" }

- POST /api/register
  - Description : Inscription utilisateur
  - Payload : { 
      "email": "string",
      "password": "string",
      "first_name": "string",
      "last_name": "string"
    }

- GET /api/auth/me
  - Description : Récupère les informations de l'utilisateur connecté
  - Authentification requise : Oui

5.3. Endpoints des Annales
- GET /api/exampapers
  - Description : Liste des annales
  - Filtres : year (optionnel)

- GET /api/exampapers/<id>
  - Description : Détails d'une annale
  - Réponse : Inclut les exercices associés

- GET /api/exampapers/<id>/pdf
  - Description : Téléchargement du PDF