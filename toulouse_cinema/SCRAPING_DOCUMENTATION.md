# Documentation du Système de Scraping - Projet Cinéma Toulouse

Ce document décrit comment le projet récupère et met à jour les séances de cinéma dans le fichier JSON `frontend/public/seances.json`.

## 📋 Table des matières

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture du système](#architecture-du-système)
3. [Workflow complet](#workflow-complet)
4. [Script principal : `update_seances.py`](#script-principal-update_seancespy)
5. [Scraper Allociné](#scraper-allociné)
6. [Enrichissement TMDb](#enrichissement-tmdb)
7. [Structure des données](#structure-des-données)
8. [Configuration et dépendances](#configuration-et-dépendances)
9. [Automatisation avec Cron](#automatisation-avec-cron)
10. [Synchronisation vers Vercel](#synchronisation-vers-vercel)

---

## 🎯 Vue d'ensemble

Le système de scraping fonctionne en plusieurs étapes :

1. **Scraping Allociné** : Récupère les séances depuis l'API Allociné pour chaque cinéma
2. **Récupération des affiches et synopsis** : Scrape les pages Allociné pour obtenir les posters et synopsis
3. **Enrichissement TMDb** : Ajoute les données manquantes (durée, date de sortie, note, trailer) via l'API TMDb
4. **Sauvegarde** : Génère le fichier JSON dans `frontend/public/seances.json`
5. **Synchronisation** (optionnelle) : Push vers Git pour déclencher un rebuild Vercel

---

## 🏗️ Architecture du système

```
scripts/
├── update_seances.py          # Script principal d'orchestration
├── get_tmdb_data.py           # Enrichissement avec TMDb
├── sync_to_vercel.py          # Synchronisation vers Vercel
├── scrapers/
│   ├── base_scraper.py        # Classe abstraite de base
│   └── allocine.py            # Scraper Allociné
└── constants/
    ├── cinemas.py             # Configuration des cinémas
    └── tarifs.py              # Tarifs par cinéma

data/
├── seances_cache.json         # Cache backend (sans TMDb)
└── tmdb_cache.json            # Cache des données TMDb

frontend/public/
└── seances.json               # Fichier final pour le frontend
```

---

## 🔄 Workflow complet

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Scraping Allociné                                         │
│    - Pour chaque cinéma (6 cinémas)                          │
│    - Pour chaque jour (7 jours : aujourd'hui + 6 suivants)   │
│    - Récupération des séances via API Allociné                │
│    - Récupération des affiches et synopsis                   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. Sauvegarde initiale                                        │
│    - data/seances_cache.json (cache backend)                 │
│    - frontend/public/seances.json (copie)                    │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. Enrichissement TMDb                                       │
│    - Pour chaque film unique                                  │
│    - Recherche sur TMDb API                                   │
│    - Ajout : durée, date_sortie, note, tmdb_id, trailer_url  │
│    - Utilisation d'un cache pour éviter les appels répétés   │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. Sauvegarde finale                                          │
│    - data/seances_cache.json (mis à jour)                    │
│    - frontend/public/seances.json (mis à jour)               │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│ 5. Synchronisation Vercel (optionnelle)                       │
│    - Git commit + push                                        │
│    - Déclenchement du rebuild Vercel                         │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 Script principal : `update_seances.py`

### Description

Script d'orchestration qui coordonne toutes les étapes du scraping.

### Code

```python
#!/usr/bin/env python
"""
Script de production pour la mise à jour des séances de cinéma.

Ce script est destiné à être exécuté en production pour :
1. Scraper les nouvelles séances et les synopsis
2. Mettre à jour le cache backend (seances_cache.json)
3. Enrichir les données avec TMDb (durée, date de sortie, note)
4. Copier les données vers le frontend (public/seances.json)

Usage:
    ./update_seances.py
    # ou
    python update_seances.py

Output:
    - Met à jour backend/data/seances_cache.json
    - Met à jour backend/data/tmdb_cache.json
    - Met à jour frontend/public/seances.json avec les données enrichies
"""

import os
import sys
from pathlib import Path
import shutil
import logging
from datetime import datetime
import json

# Ajouter le répertoire parent au PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from scripts.scrapers.allocine import AllocineScraper
from scripts.get_tmdb_data import update_seances_with_tmdb_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def datetime_handler(obj):
    """Gestionnaire personnalisé pour la sérialisation JSON des objets datetime"""
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def main():
    logger.info("Démarrage du scraping des séances...")
    
    # Définir les chemins
    cache_path = Path(__file__).parent.parent / 'data' / 'seances_cache.json'
    frontend_path = Path(__file__).parent.parent.parent / 'frontend' / 'public' / 'seances.json'
    
    # Créer les répertoires de destination s'ils n'existent pas
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    os.makedirs(os.path.dirname(frontend_path), exist_ok=True)
    
    # 1. Scraping avec AllocineScraper
    scraper = AllocineScraper()
    
    # Récupérer les séances et les synopsis
    seances_data = scraper.get_seances_with_synopsis()
    
    # Sauvegarder dans le cache avec le gestionnaire personnalisé
    with open(cache_path, 'w', encoding='utf-8') as f:
        json.dump(seances_data, f, ensure_ascii=False, indent=2, default=datetime_handler)
    logger.info(f"Cache backend mis à jour avec les synopsis : {cache_path}")
    
    # 2. Copie vers le frontend
    shutil.copy2(cache_path, frontend_path)
    logger.info(f"Cache frontend mis à jour : {frontend_path}")
    
    # 3. Enrichissement avec TMDb
    logger.info("Enrichissement des données avec TMDb...")
    update_seances_with_tmdb_data()
    logger.info("Données TMDb ajoutées avec succès")
    
    # 4. Synchronisation optionnelle vers Vercel
    if os.getenv('SYNC_TO_VERCEL', 'false').lower() == 'true':
        logger.info("Synchronisation vers Vercel...")
        try:
            from scripts.sync_to_vercel import sync_via_git, load_seances_file
            seances_data = load_seances_file()
            sync_method = os.getenv('VERCEL_SYNC_METHOD', 'git')
            if sync_method == 'git':
                success = sync_via_git(seances_data)
            else:
                logger.warning(f"Sync method '{sync_method}' not implemented in update script. Use sync_to_vercel.py directly.")
                success = False
            
            if success:
                logger.info("Synchronisation Vercel réussie")
            else:
                logger.warning("Échec de la synchronisation Vercel (non bloquant)")
        except Exception as e:
            logger.warning(f"Erreur lors de la synchronisation Vercel (non bloquant): {e}")

if __name__ == "__main__":
    main()
```

### Étapes détaillées

1. **Initialisation** : Définit les chemins des fichiers de cache et frontend
2. **Scraping** : Appelle `AllocineScraper.get_seances_with_synopsis()`
3. **Sauvegarde initiale** : Sauvegarde dans `data/seances_cache.json` et copie vers `frontend/public/seances.json`
4. **Enrichissement** : Appelle `update_seances_with_tmdb_data()` pour ajouter les données TMDb
5. **Synchronisation** (optionnelle) : Push vers Git si `SYNC_TO_VERCEL=true`

---

## 🎬 Scraper Allociné

### Classe `AllocineScraper`

Hérite de `BaseScraper` et implémente le scraping depuis Allociné.

### Configuration des cinémas

Fichier : `scripts/constants/cinemas.py`

```python
CINEMAS = {
    'ABC': {
        'id': 'P0071',
        'name': 'ABC'
    },
    'AMERICAN_COSMOGRAPH': {
        'id': 'P0235',
        'name': 'American Cosmograph'
    },
    'UTOPIA_BORDEROUGE': {
        'id': 'W3120',
        'name': 'Utopia Borderouge'
    },
    'CRATERE': {
        'id': 'P0056',
        'name': 'Le cratère'
    },
    'PATHE_WILSON': {
        'id': 'P0057',
        'name': 'Pathé Wilson'
    },
    'UGC_MONTAUDRAN': {
        'id': 'W3140',
        'name': 'UGC Montaudran'
    }
}
```

### Méthodes principales

#### `get_seances()`

Récupère toutes les séances pour tous les cinémas :

1. Pour chaque cinéma dans `CINEMAS`
2. Appelle `get_seances_cinema(cinema_id, cinema_name)`
3. Nettoie les titres avec `clean_title()`
4. Retourne la liste complète des séances

#### `get_seances_cinema(cinema_id, cinema_name)`

Récupère les séances pour un cinéma spécifique :

1. **Boucle sur 7 jours** : Aujourd'hui + 6 jours suivants
2. **Appel API Allociné** : `AllocineAPI.get_showtime(cinema_id, date_str)`
3. **Pour chaque film** :
   - Récupère l'affiche via `get_movie_poster_from_cinema_page()` ou `get_movie_details()`
   - Récupère le synopsis via `get_movie_details()`
   - Évite les doublons (réutilise l'affiche déjà trouvée)
4. **Pour chaque séance** :
   - Extrait l'horaire (`startsAt`)
   - Détermine la version (VO/VF) depuis `diffusionVersion`
   - Crée l'objet séance

#### `get_seances_with_synopsis()`

Version améliorée qui récupère aussi les synopsis :

1. Appelle `get_seances()` pour obtenir les séances de base
2. Pour chaque film unique :
   - Vérifie le cache de synopsis
   - Essaie Allociné d'abord (si `allocine_id` disponible)
   - Sinon, essaie TMDb via `search_movie_tmdb()`
   - Ajoute un délai de 0.2s entre les appels

#### `AllocineAPI.get_showtime(id_cinema, date_str)`

Appelle l'API Allociné pour récupérer les séances :

- **URL** : `https://www.allocine.fr/_/showtimes/theater-{id_cinema}/d-{date_str}/p-1/`
- **Format** : JSON
- **Structure de réponse** :
  ```json
  {
    "results": [
      {
        "movie": {
          "title": "...",
          "originalTitle": "..."
        },
        "showtimes": {
          "dubbed": [...],
          "original": [...],
          "local": [...],
          "multiple": [...]
        }
      }
    ]
  }
  ```

### Récupération des affiches

Deux méthodes complémentaires :

1. **`get_movie_poster_from_cinema_page()`** : Scrape la page du cinéma sur Allociné
2. **`get_movie_details()`** : Scrape la page de recherche ou la fiche film

Les affiches sont converties en haute qualité (remplacement de `c_160_213` par `c_310_420`).

---

## 🎞️ Enrichissement TMDb

### Script : `scripts/get_tmdb_data.py`

### Fonction `update_seances_with_tmdb_data()`

Enrichit les séances avec les données TMDb :

1. **Charge les séances** depuis `data/seances_cache.json`
2. **Charge le cache TMDb** depuis `data/tmdb_cache.json`
3. **Pour chaque séance** :
   - Si le film n'est pas dans le cache TMDb :
     - Appelle `search_movie_tmdb(titre)`
     - Sauvegarde dans le cache
     - Délai de 0.25s entre les appels
   - Met à jour la séance avec :
     - `duree` : Durée en minutes
     - `tmdb_id` : ID TMDb du film
     - `date_sortie` : Date de sortie
     - `note` : Note moyenne
     - `trailer_url` : URL de la bande-annonce YouTube
4. **Sauvegarde** :
   - Cache TMDb mis à jour
   - `data/seances_cache.json` mis à jour
   - `frontend/public/seances.json` mis à jour

### Fonction `search_movie_tmdb(title)`

Recherche un film sur TMDb :

1. **Recherche** : `GET /search/movie` avec le titre
2. **Détails** : `GET /movie/{id}` pour les informations complètes
3. **Trailer** : `GET /movie/{id}/videos` pour la bande-annonce
4. **Retourne** :
   ```python
   {
       "tmdb_id": int,
       "runtime": int,  # minutes
       "release_date": str,  # "YYYY-MM-DD"
       "vote_average": float,
       "trailer_url": str | None,
       "synopsis": str
   }
   ```

### Clé API TMDb

La clé API est hardcodée dans le script :
```python
TMDB_API_KEY = "21698af2bd148f0cfedc858588259fa0"
```

⚠️ **Note** : Pour un nouveau projet, il faudra obtenir une clé API TMDb sur [themoviedb.org](https://www.themoviedb.org/settings/api).

---

## 📊 Structure des données

### Format final : `seances.json`

```json
{
  "last_update": "2025-01-XX",
  "seances": [
    {
      "titre": "Nom du film",
      "heure": "20h30",
      "jour": "2025-01-XX",
      "cinema": "ABC",
      "version": "VF",
      "duree": 120,
      "tags": [],
      "poster": "https://...",
      "tmdb_id": 123456,
      "date_sortie": "2025-01-XX",
      "note": 8.5,
      "trailer_url": "https://www.youtube.com/watch?v=...",
      "synopsis": "Synopsis du film..."
    }
  ]
}
```

### Champs par source

| Champ | Source | Description |
|-------|--------|-------------|
| `titre` | Allociné | Titre du film |
| `heure` | Allociné | Heure de la séance (format "HHhMM") |
| `jour` | Allociné | Date de la séance (ISO format) |
| `cinema` | Allociné | Nom du cinéma |
| `version` | Allociné | "VF" ou "VO" |
| `poster` | Allociné | URL de l'affiche |
| `synopsis` | Allociné / TMDb | Synopsis du film |
| `duree` | TMDb | Durée en minutes |
| `tmdb_id` | TMDb | ID TMDb du film |
| `date_sortie` | TMDb | Date de sortie |
| `note` | TMDb | Note moyenne (/10) |
| `trailer_url` | TMDb | URL YouTube de la bande-annonce |
| `tags` | - | Liste vide (non utilisée actuellement) |

---

## ⚙️ Configuration et dépendances

### Fichier : `scripts/requirements.txt`

```txt
# Scraping
beautifulsoup4==4.12.3
requests==2.31.0
scrapy==2.11.1

# Utilitaires
python-dotenv==1.0.1

# Api
allocine-seances==0.0.12
```

### Installation

```bash
cd scripts
pip install -r requirements.txt
```

### Variables d'environnement (optionnelles)

- `SYNC_TO_VERCEL` : `true` pour activer la synchronisation automatique
- `VERCEL_SYNC_METHOD` : `git` (par défaut), `blob`, ou `api`
- `GIT_REPO_PATH` : Chemin vers le dépôt Git (pour la sync)

---

## ⏰ Automatisation avec Cron

### Fichier : `crontab`

```bash
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
PYTHONPATH=/app

# Mise à jour des séances tous les jours à 1h du matin
0 1 * * * cd /app && python scripts/update_seances.py >> /var/log/cron.log 2>&1 && echo "Cron job executed at $(date)" >> /var/log/cron.log

# Redémarrage des conteneurs Docker 25 minutes après le scraping (1h25)
25 1 * * * cd /home/massyl/vps_maths_cine_cv/toulouse_cinema && docker-compose down && sleep 2 && docker-compose up --build -d >> /var/log/cron.log 2>&1 && echo "Docker containers restarted at $(date)" >> /var/log/cron.log
```

### Installation du crontab

```bash
crontab crontab
```

### Exécution manuelle

```bash
# Depuis la racine du projet
python scripts/update_seances.py
```

---

## 🚀 Synchronisation vers Vercel

### Script : `scripts/sync_to_vercel.py`

### Méthode recommandée : Git

La méthode Git est la plus simple et recommandée :

1. **Commit** : Ajoute et commit `frontend/public/seances.json`
2. **Push** : Push vers le dépôt distant
3. **Vercel** : Détecte automatiquement le changement et rebuild

### Utilisation

```bash
# Méthode Git (recommandée)
python scripts/sync_to_vercel.py --method git

# Ou depuis update_seances.py (si SYNC_TO_VERCEL=true)
```

### Prérequis

- Le dépôt doit être un dépôt Git initialisé
- Les credentials Git doivent être configurés
- Le fichier `seances.json` doit être tracké par Git

### Workflow recommandé

1. **VPS** : Exécute `update_seances.py` (génère `seances.json`)
2. **Git** : Le script commit et push automatiquement
3. **Vercel** : Détecte le push et rebuild automatiquement
4. **Frontend** : Le nouveau fichier est disponible

---

## 🔍 Détails techniques

### Gestion des erreurs

- **Logging** : Utilise le module `logging` pour tracer les opérations
- **Try/Except** : Gestion d'erreurs à chaque étape critique
- **Fallbacks** : Si une affiche n'est pas trouvée, utilise une image par défaut
- **Cache** : Évite les appels API répétés pour les mêmes films

### Optimisations

- **Cache de synopsis** : Évite de récupérer plusieurs fois le synopsis du même film
- **Cache TMDb** : Sauvegarde les données TMDb pour éviter les appels répétés
- **Délais** : Délais entre les appels API (0.2s pour Allociné, 0.25s pour TMDb)
- **Réutilisation des affiches** : Si un film apparaît plusieurs fois, réutilise l'affiche déjà trouvée

### Limitations

- **Allociné** : L'API peut changer de structure (nécessite des ajustements)
- **TMDb** : Limite de taux d'appels API (40 requêtes / 10 secondes)
- **Cinémas** : Les IDs Allociné doivent être maintenus à jour
- **Pathé Wilson** : Note dans le code indiquant un problème potentiel

---

## 📝 Notes pour la recréation du projet

### Étapes à suivre

1. **Créer la structure** :
   ```
   scripts/
   ├── scrapers/
   ├── constants/
   └── update_seances.py
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r scripts/requirements.txt
   ```

3. **Configurer les cinémas** :
   - Modifier `scripts/constants/cinemas.py` avec les IDs Allociné
   - Obtenir les IDs depuis les URLs Allociné des cinémas

4. **Configurer TMDb** :
   - Obtenir une clé API sur themoviedb.org
   - Modifier `scripts/get_tmdb_data.py` avec votre clé

5. **Tester le scraping** :
   ```bash
   python scripts/update_seances.py
   ```

6. **Configurer Cron** (optionnel) :
   ```bash
   crontab crontab
   ```

7. **Configurer la sync Vercel** (optionnel) :
   - Définir `SYNC_TO_VERCEL=true` dans l'environnement
   - S'assurer que Git est configuré

---

## 🐛 Dépannage

### Problèmes courants

1. **Aucune séance trouvée** :
   - Vérifier les IDs Allociné dans `cinemas.py`
   - Vérifier que l'API Allociné répond

2. **Erreur TMDb** :
   - Vérifier la clé API
   - Vérifier les limites de taux

3. **Fichier JSON invalide** :
   - Vérifier les logs pour les erreurs de sérialisation
   - Vérifier que les dates sont bien converties en ISO format

4. **Sync Git échoue** :
   - Vérifier que Git est initialisé
   - Vérifier les credentials Git
   - Vérifier que le fichier est tracké

---

## 📚 Ressources

- [API Allociné](https://www.allocine.fr) (non documentée officiellement)
- [API TMDb](https://developers.themoviedb.org/3)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/)

---

## ⚠️ Avertissements

1. **Respect des ToS** : S'assurer de respecter les conditions d'utilisation d'Allociné et TMDb
2. **Rate limiting** : Respecter les limites d'appels API
3. **Maintenance** : Les scrapers peuvent casser si les sites changent leur structure
4. **Clé API** : Ne pas commiter la clé API TMDb dans le dépôt public
