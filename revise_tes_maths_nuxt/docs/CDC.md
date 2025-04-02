## 1. Contexte
Le projet consiste à développer un Dashboard web (accessible via un navigateur) pour le suivi des révisions du bac. L’application permettra aux élèves de créer un compte, de consulter des annales (sujets d’examens passés), de voir pour chaque exercice les thématiques abordées (Probabilités
Loi Binomiale
Géométrie dans l'espace
Suites
Etudes de fonctions
Exponentielle
Logarithme Népérien
Intégrale
Convexité
Equations différentielles
Python), d’accéder aux PDF correspondants, et de suivre l’avancement de leurs révisions.
Cette application web sera hébergée sur un VPS.

## 2. Objectifs généraux
1. **Simplifier l’accès aux annales du bac** : les élèves doivent pouvoir rechercher et consulter rapidement des sujets.  
2. **Suivre la progression** : l’application doit proposer une vue détaillée de l’avancement de chaque élève (exercices terminés, en cours, nombre d'exercices effectués par thème, etc.).
3. **Assurer une authentification sécurisée** : chaque élève doit avoir un compte protégé par mot de passe.
   Une fois connecté à son compte, l'élève doit pouvoir accéder à ses annales, à ses exercices, et à ses statistiques.
4. **Permettre l’hébergement sur un VPS** : l’application doit être déployée sur un serveur dédié, avec certificat SSL, et offrir une performance suffisante pour un nombre d’élèves déterminé.

## 3. Fonctionnalités attendues
1. **Authentification (Login / Logout / Register)**
   - Création de compte (nom, email, mot de passe sécurisé).  
   - Système de sessions (via cookies sécurisés).  
   - Rôles possibles (admin / élève).

2. **Gestion des annales**
   - Liste paginée des sujets (par année, par matière).  
   - Visualisation des exercices d’un sujet, avec thématiques.  
   - Téléchargement ou visualisation PDF (intégré ou lien protégé).

3. **Progression**
   - Possibilité pour l’élève de marquer un exercice comme “terminé” ou “en cours”.  
   - Tableau de bord global (statistiques, pourcentages d’avancement).

4. **Interface utilisateur**
   - Tableaux de bord ergonomiques (possibilité de graphiques ou indicateurs).  
   - Système de filtres (ex. filtrer par matière, type d’exercices).

5. **Administration**
   - Gestion des utilisateurs (activation / suppression).  
   - Ajout / modification / suppression de nouvelles annales.

## 4. Contraintes techniques
6. **Framework** : Flask (Python 3.x).  
7. **Base de données** : PostgreSQL ou MySQL.  
8. **Hébergement** : VPS (Ubuntu), serveur d’application WSGI (Gunicorn) et reverse-proxy (Nginx ou Traefik).  
9. **Sécurité** :  
   - Gestion des mots de passe avec hashage (bcrypt).  
   - Utilisation d’un certificat SSL (Let’s Encrypt).  
   - Protection CSRF (Flask-WTF).
10. **Tests** : Approche TDD (Pytest).

## 5. Architecture logicielle (vue d’ensemble)
- **Front** : HTML/CSS/JS (framework type Bootstrap ou Tailwind), templates Jinja2.  
- **Back** : Flask + Blueprints (`auth`, `dashboard`, `admin`), Flask-Login, SQLAlchemy.  
- **Stockage** : Base de données relationnelle (PostgreSQL/MySQL), et stockage sécurisé pour les PDF.  
- **Déploiement** : VPS, Gunicorn, Nginx/Traefik avec SSL.

## 6. Sécurité & RGPD
- **SSL/TLS** obligatoire pour les échanges.  
- Données personnelles stockées de manière sécurisée (email, progression).  
- Fournis des CGU / mentions légales pour expliquer ce qui est collecté et pourquoi
- Politique de confidentialité (notamment pour le RGPD) : préciser la durée de conservation,  possibilité de permettre à un élève de supprimer son compte ou ses données s’il le souhaite.

## 7. Livrables
1. **Code source** (GitHub) avec README clair.  
2. **Documentation technique** (config, installation, déploiement).  
3. **Jeu de tests unitaires et d’intégration** (Pytest).  
4. **Scripts de création / migrations** (Alembic si besoin).


## 8. Planification (exemple)
5. Initialisation du projet, configuration Flask, première route, mise en place TDD.  
6. Authentification (inscription, login, logout).  
7. Implémentation du modèle (annales, exercices, progression) + tests.  
8. Interface utilisateur (templates), mise en forme du dashboard.  
9. Déploiement sur VPS, configuration SSL, tests d’intégration.  
10. Corrections, finalisation et livraison.