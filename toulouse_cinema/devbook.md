Je veux développer un site web pour aggréger les séances de cinéma de tous les cinémas
de Toulouse.

Spécifications :

- Le site doit permettre à un utilisateur de rechercher un film et de trouver les séances
de cinéma les plus proches.

- Le site doit être accessible sur tous les appareils mobiles et tablettes.

- Le site doit être optimisé pour les moteurs de recherche.

- Le site doit être sécurisé.

- Le site doit être optimisé pour les moteurs de recherche.

Fonctionnement : 

Un script de scraping 'update_seances.py' qui récupère les séances de cinéma de tous les cinémas de Toulouse sur le site d'allociné, qui met à jour chaque jour un fichier
seances.json dans scripts/data.

Un front-end Nuxt.js qui génère et sert des pages statiques.

Un mécanisme pour rebuid le front-end Nuxt.js en production automatiquement tous les jours.



# Projet CinéToulouse - Agrégateur de séances de cinéma

## Objectif
Développer une application web qui agrège les séances de cinéma de tous les cinémas de Toulouse, offrant une interface utilisateur intuitive et optimisée pour le référencement.

## Architecture technique

### Scraping
- **Script**: `update_seances.py`
  - Langage: Python 3.11+
  - Fréquence d'exécution: 1 fois par jour (00h01)
  - Source des données: Allociné
  - Output: `scripts/data/seances.json`
  - Structure du JSON:
    ```json
    {
  "last_update": "2025-03-19T19:45:07.126359",
  "seances": [
    {
      "titre": "La Cache",
      "heure": "19h10",
      "jour": "2025-03-19T00:00:00",
      "cinema": "ABC",
      "version": "VF",
      "duree": 90,
      "tags": [],
      "poster": "https://fr.web.img6.acsta.net/c_310_420/img/42/8f/428ff3673214bf3174e58d02016f89f1.jpg",
      "tmdb_id": 1266809,
      "date_sortie": "2025-03-19",
      "note": 4.0,
      "trailer_url": "https://www.youtube.com/watch?v=-NJM3MGF1dQ"
    },
    ]
    }
    ```

### Frontend (Nuxt.js)
- **Framework**: Nuxt.js 3
- **Mode**: Static Site Generation (SSG)
- **Hébergement**: Vercel/Netlify

#### Pages principales
1. **Page d'accueil** (`/`)
   - Liste des films à l'affiche
   - Recherche par titre/cinéma
   - Filtres (VF/VOST, 3D, etc.)

2. **Page film** (`/film/[titre]`)
   - Détails du film
   - Liste des séances par cinéma
   - Carte interactive des cinémas

3. **Page cinéma** (`/cinema/[cinema]`)
   - Informations du cinéma
   - Programme du jour/semaine

#### Optimisations SEO
- Meta tags dynamiques par page
- Sitemap.xml automatique
- Schema.org markup pour les films et séances
- URLs propres et significatives
- Pages statiques pré-rendues

#### Responsive Design
- Breakpoints:
  - Mobile: < 640px
  - Tablet: 641px - 1024px
  - Desktop: > 1024px

## Workflow de déploiement
1. Exécution du script de scraping (00h01)
2. Génération du nouveau JSON
3. Déclenchement automatique du rebuild Nuxt.js
4. Déploiement des nouvelles pages statiques

## Sécurité
- Rate limiting sur le script de scraping
- Headers de sécurité (HSTS, CSP, etc.)
- Validation des données JSON
- Protection contre les injections XSS

## Performance
- Images optimisées et lazy-loading
- Cache-Control headers appropriés
- Minification des assets
- Core Web Vitals optimisés

## Monitoring
- Logs du script de scraping
- Alertes en cas d'échec
- Métriques de performance
- Suivi du trafic

## Stack technique complète
- **Backend**:
  - Python 3.11+
  - Requests
  - BeautifulSoup4
  - Schedule (pour le cron)

- **Frontend**:
  - Nuxt.js 3
  - Vue.js 3
  - TailwindCSS
  - Leaflet (pour les cartes)

## Développement local
1. Créer un environnement virtuel Python
2. Installer les dépendances: `pip install -r requirements.txt`
3. Installer les dépendances Node: `npm install`
4. Lancer le script de scraping: `python scripts/update_seances.py`
5. Lancer le serveur de développement: `npm run dev`


