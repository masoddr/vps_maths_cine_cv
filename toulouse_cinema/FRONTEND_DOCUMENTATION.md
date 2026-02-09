# Documentation Frontend - Projet Cinéma Toulouse

Ce document décrit la structure complète du frontend Nuxt.js pour permettre la recréation du projet.

## 📋 Table des matières

1. [Structure du projet](#structure-du-projet)
2. [Configuration](#configuration)
3. [Dépendances](#dépendances)
4. [Composants](#composants)
5. [Pages](#pages)
6. [Stores Pinia](#stores-pinia)
7. [Plugins](#plugins)
8. [Utils et Constants](#utils-et-constants)
9. [Assets publics](#assets-publics)
10. [Docker](#docker)
11. [Vercel](#vercel)

---

## 📁 Structure du projet

```
frontend/
├── components/          # Composants Vue réutilisables
├── pages/              # Pages de l'application (routing automatique)
├── layouts/            # Layouts de pages
├── stores/             # Stores Pinia pour la gestion d'état
├── composables/        # Composables Vue (vide actuellement)
├── plugins/            # Plugins Nuxt
├── utils/              # Utilitaires
├── constants/          # Constantes
├── server/             # API routes (optionnel)
├── public/             # Fichiers statiques
├── app.vue             # Composant racine
├── nuxt.config.ts      # Configuration Nuxt
├── tailwind.config.js  # Configuration Tailwind CSS
├── tsconfig.json       # Configuration TypeScript
├── package.json        # Dépendances npm
├── vercel.json         # Configuration Vercel
├── Dockerfile          # Image Docker production
├── Dockerfile.dev      # Image Docker développement
└── .gitignore          # Fichiers ignorés par Git
```

---

## ⚙️ Configuration

### `package.json`

```json
{
  "name": "nuxt-app",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "nuxt build",
    "dev": "nuxt dev",
    "generate": "nuxt generate",
    "preview": "nuxt preview",
    "postinstall": "nuxt prepare"
  },
  "dependencies": {
    "@nuxtjs/tailwindcss": "^6.13.2",
    "@pinia/nuxt": "^0.10.1",
    "@types/leaflet": "^1.9.16",
    "@vue-leaflet/vue-leaflet": "^0.10.1",
    "leaflet": "^1.9.4",
    "nuxt": "^3.16.1",
    "pinia": "^3.0.1",
    "vue": "^3.5.13",
    "vue-router": "^4.5.0",
    "vue3-leaflet": "^1.0.50"
  },
  "devDependencies": {
    "@fawmi/vue-google-maps": "^0.9.79"
  }
}
```

### `nuxt.config.ts`

```typescript
// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  // Mode statique
  ssr: true,

  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/']
    },
    server: {
      port: process.env.PORT,
      host: process.env.HOST || '0.0.0.0'
    },
    routeRules: {
      '/': { prerender: process.env.NODE_ENV === 'production' },
      '/films': { prerender: process.env.NODE_ENV === 'production' },
      '/cinemas': { prerender: process.env.NODE_ENV === 'production' }
    }
  },

  // Modules utiles
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt',
  ],

  // Configuration des répertoires publics
  dir: {
    public: 'public'
  },

  // Configuration de Leaflet
  plugins: [
    '~/plugins/leaflet.client.ts'
  ],

  build: {
    transpile: ['@vue-leaflet/vue-leaflet']
  },

  compatibilityDate: '2025-03-20',

  app: {
    head: {
      htmlAttrs: {
        lang: 'fr'
      },
      title: 'Cinéma Toulouse - Guide des séances et films | Cinéphoria',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'format-detection', content: 'telephone=no' },
        { name: 'robots', content: 'index, follow' },
        { name: 'theme-color', content: '#6B46C1' },
        { name: 'geo.region', content: 'FR-31' },
        { name: 'geo.placename', content: 'Toulouse' },
        { name: 'geo.position', content: '43.604652;1.444209' },
        { name: 'ICBM', content: '43.604652, 1.444209' }
      ],
      link: [
        { 
          rel: 'icon', 
          type: 'image/png', 
          href: '/favicon-16x16.png',
          sizes: '16x16'
        },
        { 
          rel: 'icon', 
          type: 'image/png', 
          href: '/favicon-32x32.png',
          sizes: '32x32'
        },
        { 
          rel: 'apple-touch-icon', 
          href: '/apple-touch-icon.png',
          sizes: '180x180'
        },
        { rel: 'canonical', href: 'https://cinephoria.fr' }
      ]
    }
  }
})
```

### `tailwind.config.js`

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './components/**/*.{vue,js,ts}',
    './layouts/**/*.vue',
    './pages/**/*.vue',
    './plugins/**/*.{js,ts}',
    './app.vue',
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#f5f3ff',
          100: '#ede9fe',
          200: '#ddd6fe',
          300: '#c4b5fd',
          400: '#a78bfa',
          500: '#8b5cf6',
          600: '#7c3aed',
          700: '#6d28d9',
          800: '#5b21b6',
          900: '#4c1d95',
        },
        accent: {
          50: '#fef3c7',
          100: '#fde68a',
          200: '#fcd34d',
          300: '#fbbf24',
          400: '#f59e0b',
          500: '#d97706',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Playfair Display', 'serif'],
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'slide-down': 'slideDown 0.3s ease-out',
        'scale-in': 'scaleIn 0.3s ease-out',
        'shimmer': 'shimmer 2s infinite',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-100%)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        scaleIn: {
          '0%': { transform: 'scale(0.95)', opacity: '0' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
        shimmer: {
          '0%': { backgroundPosition: '-1000px 0' },
          '100%': { backgroundPosition: '1000px 0' },
        },
      },
      boxShadow: {
        'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
        'glow': '0 0 20px rgba(139, 92, 246, 0.3)',
      },
    },
  },
  plugins: [],
}
```

### `tsconfig.json`

```json
{
  // https://nuxt.com/docs/guide/concepts/typescript
  "extends": "./.nuxt/tsconfig.json"
}
```

### `vercel.json`

```json
{
  "framework": "nuxtjs"
}
```

### `.gitignore`

```
# Nuxt dev/build outputs
.output
.data
.nuxt
.nitro
.cache
dist

# Node dependencies
node_modules

# Logs
logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# Misc
.DS_Store
.fleet
.idea
.vscode
*.suo
*.ntvs*
*.njsproj
*.sln
*.sw?

# Local env files
.env
.env.*
!.env.example

# TypeScript
*.tsbuildinfo

# Coverage directory used by tools like istanbul
coverage

# Temporary files
*.tmp
*.bak
.temp
```

---

## 🧩 Composants

### `app.vue`

Composant racine de l'application :

```vue
<template>
  <div class="min-h-screen flex flex-col">
    <TheNavbar />
    <main class="flex-grow">
      <NuxtPage />
    </main>
    <TheFooter />
  </div>
</template>
```

### `components/TheNavbar.vue`

Barre de navigation fixe avec menu mobile responsive. Inclut :
- Logo et nom du site
- Liens vers Films et Cinémas
- Menu hamburger pour mobile
- Animation de transition

### `components/TheFooter.vue`

Pied de page avec :
- Liens vers mentions légales, CGU, confidentialité
- Section contact
- Section à propos
- Copyright et lien vers portfolio

### `components/DaySelector.vue`

Sélecteur de jour pour filtrer les séances :
- Boutons horizontaux scrollables
- Format de date en français
- Émission d'événement `update:day`

### `components/ScrollToTop.vue`

Bouton flottant pour remonter en haut de page :
- Apparaît après 300px de scroll
- Animation smooth
- Position fixe en bas à droite

---

## 📄 Pages

### `pages/index.vue`

Page d'accueil avec :
- Hero section avec image de fond et effet parallaxe
- Liste des films à l'affiche (grille responsive)
- SEO optimisé avec structured data
- Animations fade-in

### `pages/films/index.vue`

Page de liste des films avec :
- Sélecteur de jour (`DaySelector`)
- Barre de recherche par titre
- Filtres par cinéma (badges colorés)
- Tri par note ou durée
- Grille de cartes de films avec :
  - Poster
  - Titre
  - Durée et note
  - Séances groupées par cinéma
  - Badges horaires colorés par cinéma

### `pages/films/[id].vue`

Page de détail d'un film avec :
- Poster et informations (durée, date de sortie, synopsis, note)
- Trailer YouTube intégré (si disponible)
- Séances groupées par jour et cinéma
- Design responsive (poster caché sur mobile)

### `pages/cinemas/index.vue`

Page de liste des cinémas avec :
- Grille de cartes pour chaque cinéma
- Image, adresse, horaires
- Liens vers itinéraire et site web

### Pages statiques

- `pages/a-propos.vue`
- `pages/cgu.vue`
- `pages/confidentialite.vue`
- `pages/contact.vue`
- `pages/faq.vue`
- `pages/mentions-legales.vue`

---

## 🗄️ Stores Pinia

### `stores/seances.ts`

Store pour la gestion des séances :

**Interface `Seance`** :
```typescript
interface Seance {
  titre: string
  heure: string
  jour: string
  cinema: string
  version: string
  duree: number
  tags: string[]
  poster: string
  tmdb_id: number
  date_sortie: string
  note: number
  trailer_url: string | null
  synopsis: string
}
```

**State** :
- `seances`: Liste des séances
- `lastUpdate`: Date de dernière mise à jour
- `loading`: État de chargement
- `error`: Message d'erreur

**Getters** :
- `seancesByDay`: Séances groupées par jour
- `cinemas`: Liste des cinémas uniques
- `films`: Liste des films uniques

**Actions** :
- `fetchSeances()`: Charge les séances depuis `/seances.json`

### `stores/cinemas.ts`

Store pour la gestion des cinémas :

**Interface `Cinema`** :
```typescript
interface Cinema {
  id: string
  nom: string
  adresse: string
  ville: string
  nombreSalles: number
  telephone: string
  siteWeb: string
  latitude: number
  longitude: number
}
```

**Cinémas définis** :
- ABC
- American Cosmograph
- Utopia Borderouge
- Le cratère
- Pathé Wilson
- UGC Montaudran

**Getters** :
- `getColor(cinema)`: Retourne la couleur du cinéma
- `getLightColor(cinema)`: Retourne la couleur claire du cinéma

---

## 🔌 Plugins

### `plugins/leaflet.client.ts`

Plugin pour charger Leaflet uniquement côté client :

- Import dynamique de Leaflet et @vue-leaflet/vue-leaflet
- Configuration des icônes de marqueurs personnalisées
- Enregistrement des composants Leaflet globalement :
  - `LMap`
  - `LTileLayer`
  - `LMarker`
  - `LPopup`

---

## 🛠️ Utils et Constants

### `utils/seo.ts`

Utilitaires pour le SEO :

```typescript
export const defaultMeta = {
  title: 'Cinéphoria - Les séances de cinéma à Toulouse',
  description: 'Trouvez facilement toutes les séances de cinéma à Toulouse...',
  image: '/images/social-share.jpg',
  url: 'https://cinephoria.fr'
}

export const generateMeta(options: Partial<typeof defaultMeta> = {}) => {
  // Génère les meta tags Open Graph et Twitter Card
}
```

### `constants/tarifs.ts`

Constantes des tarifs par cinéma :

```typescript
export const TARIFS_CINEMA = {
  "AMERICAN_COSMOGRAPH": {
    "normal": 8.00,
    "carnet": { ... },
    "reduit": { ... }
  },
  // ... autres cinémas
}
```

---

## 📦 Assets publics

### Structure `public/`

```
public/
├── favicon-16x16.png
├── favicon-32x32.png
├── apple-touch-icon.png
├── images/
│   ├── cinema-hero.jpg
│   ├── logo.png
│   └── massyl.jpg
├── marker-icon.png
├── marker-icon-2x.png
├── marker-shadow.png
├── robots.txt
├── seances.json        # Fichier généré par le script de scraping
└── sitemap.xml
```

### `public/robots.txt`

```
User-agent: *
Allow: /

Sitemap: https://cinephoria.fr/sitemap.xml
```

### `public/seances.json`

Fichier JSON généré par le script de scraping avec la structure :

```json
{
  "last_update": "2025-01-XX",
  "seances": [
    {
      "titre": "...",
      "heure": "...",
      "jour": "...",
      "cinema": "...",
      "version": "...",
      "duree": 120,
      "tags": [...],
      "poster": "...",
      "tmdb_id": 123,
      "date_sortie": "...",
      "note": 8.5,
      "trailer_url": "...",
      "synopsis": "..."
    }
  ]
}
```

---

## 🐳 Docker

### `Dockerfile` (Production)

Image multi-stage pour la production :
- Stage 1 : Build avec Node 20.18.0-slim
- Stage 2 : Runtime avec Node 20.18.0-alpine
- Port : 3001 (configurable via env)
- Healthcheck inclus
- Utilisateur non-root

### `Dockerfile.dev` (Développement)

Image pour le développement avec hot-reload :
- Node 20.18.0-slim
- Port : 3000
- Toutes les dépendances (dev incluses)

---

## 🚀 Vercel

### Configuration

Le fichier `vercel.json` indique à Vercel d'utiliser le framework Nuxt.js.

### Déploiement

1. Connecter le dépôt Git à Vercel
2. Vercel détecte automatiquement Nuxt.js
3. Le build se fait automatiquement à chaque push
4. Le fichier `public/seances.json` doit être présent dans le repo ou généré lors du build

### Workflow recommandé

1. **VPS** : Exécuter le script de scraping qui génère `seances.json`
2. **Git** : Pousser le fichier `seances.json` dans le dépôt
3. **Vercel** : Déploiement automatique avec le nouveau fichier

---

## 📝 Layouts

### `layouts/default.vue`

Layout par défaut :

```vue
<template>
  <div class="min-h-screen bg-gray-50">
    <slot />
  </div>
</template>
```

---

## 🎨 Styles et Design

### Couleurs principales

- **Primary** : Violet (50-900)
- **Accent** : Jaune/Orange (50-500)
- **Cinémas** :
  - ABC : Bleu (`rgb(59, 130, 246)`)
  - Autres : Rouge (`rgb(220, 38, 38)`)

### Typographie

- **Sans-serif** : Inter (Google Fonts)
- **Display** : Playfair Display (Google Fonts)

### Animations

- `fade-in` : Apparition en fondu
- `slide-up` : Glissement vers le haut
- `slide-down` : Glissement vers le bas
- `scale-in` : Zoom d'entrée
- `shimmer` : Effet de brillance

---

## 🔄 Workflow de développement

### Installation

```bash
cd frontend
npm install
```

### Développement

```bash
npm run dev
```

### Build production

```bash
npm run build
npm run preview  # Pour tester le build localement
```

### Génération statique

```bash
npm run generate
```

---

## 📌 Points importants

1. **Fichier `seances.json`** : Doit être généré par le script de scraping et placé dans `public/`
2. **Leaflet** : Chargé uniquement côté client via le plugin
3. **SEO** : Meta tags configurés dans `nuxt.config.ts` et via `utils/seo.ts`
4. **Responsive** : Design mobile-first avec Tailwind CSS
5. **TypeScript** : Configuration minimale, étend `.nuxt/tsconfig.json`
6. **SSR** : Activé pour le SEO, avec prerendering pour certaines routes

---

## 🚨 Notes de migration

Lors de la recréation du projet :

1. Créer un nouveau projet Nuxt 3 : `npx nuxi@latest init`
2. Installer les dépendances listées dans `package.json`
3. Copier tous les fichiers de configuration
4. Créer la structure de dossiers
5. Copier tous les composants, pages, stores, etc.
6. Ajouter les assets publics (images, favicons, etc.)
7. Configurer Vercel avec `vercel.json`
8. S'assurer que le script de scraping génère `public/seances.json`

---

## 📚 Ressources

- [Documentation Nuxt 3](https://nuxt.com/docs)
- [Tailwind CSS](https://tailwindcss.com/docs)
- [Pinia](https://pinia.vuejs.org/)
- [Vue Leaflet](https://vue-leaflet.js.org/)
- [Vercel Documentation](https://vercel.com/docs)
