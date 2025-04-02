# Révise Tes Maths - Application de Révision du Bac

Une application web moderne pour aider les lycéens à réviser leurs mathématiques pour le bac.

## Structure du Projet

Le projet est divisé en deux parties principales :
- `frontend/` : Application Nuxt.js
- `backend/` : API Flask

## Prérequis

- Python 3.12+
- Node.js 18+
- PostgreSQL 16+

## Installation

### Backend (Flask)

1. Créer un environnement virtuel et l'activer :
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Sur Linux/Mac
# ou
venv\Scripts\activate  # Sur Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer la base de données :
```bash
# Créer la base de données PostgreSQL
sudo -u postgres psql -c "CREATE DATABASE revise_tes_maths;"
sudo -u postgres psql -c "CREATE USER revise_tes_maths WITH PASSWORD 'revise_tes_maths';"
sudo -u postgres psql -c "ALTER USER revise_tes_maths WITH SUPERUSER;"
```

4. Configurer les variables d'environnement :
```bash
# Copier le fichier .env.example
cp .env.example .env
# Modifier les variables selon votre configuration
```

5. Initialiser la base de données :
```bash
flask db upgrade
```

6. Lancer le serveur de développement :
```bash
flask run
```

### Frontend (Nuxt.js)

1. Installer les dépendances :
```bash
cd frontend
npm install
```

2. Lancer le serveur de développement :
```bash
npm run dev
```

## Utilisation

- Backend : http://localhost:5000
- Frontend : http://localhost:3000

## Tests

### Backend
```bash
cd backend
pytest
```

### Frontend
```bash
cd frontend
npm run test
```

## Déploiement

Instructions de déploiement à venir...

## Gestion des fichiers statiques

### Configuration des volumes Docker

Les fichiers statiques (PDFs, images, etc.) sont stockés dans un volume Docker persistant. Voici les modifications nécessaires dans le `docker-compose.yml` :

```yaml
services:
  backend:
    # ... configuration existante ...
    volumes:
      - uploads:/app/static/uploads  # Volume pour les fichiers uploadés

  traefik:
    # ... configuration existante ...
    labels:
      - "traefik.http.routers.backend-static.rule=Host(`revise-tes-maths.fr`, `www.revise-tes-maths.fr`) && PathPrefix(`/static`)"
      - "traefik.http.routers.backend-static.entrypoints=websecure"
      - "traefik.http.routers.backend-static.tls=true"
      - "traefik.http.routers.backend-static.service=backend"

volumes:
  uploads:    # Volume persistant pour les fichiers uploadés
```

### Structure des dossiers

```
backend/
└── static/
    └── uploads/
        ├── pdfs/        # Pour les annales en PDF
        └── images/      # Pour les images du site
```

### Accès aux fichiers

Les fichiers sont accessibles via les URLs suivantes :
- PDFs : `https://revise-tes-maths.fr/static/uploads/pdfs/{filename}`
- Images : `https://revise-tes-maths.fr/static/uploads/images/{filename}`

### Sauvegarde des fichiers

#### Sauvegarde manuelle

Pour sauvegarder les fichiers du volume :

```bash
# Créer une sauvegarde
docker run --rm -v revise_tes_maths_uploads:/source -v $(pwd):/backup alpine tar czf /backup/uploads.tar.gz -C /source .

# Restaurer une sauvegarde
docker run --rm -v revise_tes_maths_uploads:/target -v $(pwd):/backup alpine sh -c "cd /target && tar xzf /backup/uploads.tar.gz"
```

#### Sauvegarde automatique

Un script de backup automatique (`backup_uploads.sh`) est configuré pour sauvegarder quotidiennement les fichiers :

1. **Fonctionnement** :
   - Exécution automatique tous les jours à 2h du matin
   - Création d'une archive datée dans `/home/massyl/backups/uploads`
   - Conservation des 7 dernières sauvegardes uniquement
   - Format du nom de fichier : `uploads_YYYYMMDD_HHMMSS.tar.gz`

2. **Vérification des sauvegardes** :
```bash
# Lister les sauvegardes existantes
ls -l /home/massyl/backups/uploads

# Vérifier le contenu d'une sauvegarde spécifique
tar -tvf /home/massyl/backups/uploads/uploads_20240321_020000.tar.gz
```

3. **Restauration d'une sauvegarde** :
```bash
# Restaurer une sauvegarde spécifique
docker run --rm -v revise_tes_maths_nuxt_uploads:/target -v /home/massyl/backups/uploads:/backup alpine sh -c "cd /target && tar xzf /backup/uploads_20240321_020000.tar.gz"
```

4. **Localisation des fichiers** :
   - Volume Docker : `/var/lib/docker/volumes/revise_tes_maths_nuxt_uploads/_data/`
   - Sauvegardes : `/home/massyl/backups/uploads/`

## Contribution

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 