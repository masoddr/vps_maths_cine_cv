# Guide de Conteneurisation - Revise Tes Maths

## Table des matières
1. [Backend Flask](#1-backend-flask)
2. [Base de données](#2-base-de-données)
3. [Frontend Nuxt](#3-frontend-nuxt)
4. [Docker Compose](#4-docker-compose)
5. [Déploiement sur VPS](#5-déploiement-sur-vps)

## 1. Backend Flask

### Configuration requise
- Python 3.11.8
- Flask et dépendances (voir requirements.txt)
- PostgreSQL 15.6

### Fichiers importants
- `backend/Dockerfile`
- `backend/.env` (variables d'environnement)
- `backend/docker-entrypoint.sh` (script d'initialisation)

### Variables d'environnement backend
```env
FLASK_APP=run.py
FLASK_ENV=production
DATABASE_URL=postgresql://rtm_user:rtm_password@db:5432/rtm
SECRET_KEY=votre_clé_secrète
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

## 2. Base de données

### Configuration PostgreSQL
```yaml
services:
  db:
    image: postgres:15.6
    environment:
      POSTGRES_DB: rtm
      POSTGRES_USER: rtm_user
      POSTGRES_PASSWORD: rtm_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
```

### Initialisation automatique
L'initialisation de la base de données et la création de l'utilisateur admin sont automatisées via le script `docker-entrypoint.sh`. Au démarrage des conteneurs :
1. Le script attend que PostgreSQL soit prêt
2. Les migrations de la base de données sont appliquées
3. L'utilisateur admin est créé s'il n'existe pas déjà
4. Le serveur Gunicorn démarre

Identifiants admin par défaut :
- Email : admin@example.com
- Mot de passe : admin123

**Important** : Changez le mot de passe admin après la première connexion en production !

## 3. Frontend Nuxt

### Configuration requise
- Node.js 18.19.1
- Nuxt 3

### Variables d'environnement frontend
```env
NUXT_PUBLIC_API_BASE=http://localhost:5000
NODE_ENV=production
```

## 4. Docker Compose

### Développement local
```bash
# Premier démarrage ou après modifications
docker-compose up --build -d

# Démarrage normal
docker-compose up -d

# Logs en temps réel
docker-compose logs -f

# Arrêt des services
docker-compose down
```

## 5. Déploiement sur VPS

### 5.1 Prérequis sur le VPS
```bash
# Mise à jour du système
apt update && apt upgrade -y

# Installation de Docker et Docker Compose
apt install -y docker.io docker-compose

# Création de l'utilisateur de déploiement
adduser deployer
usermod -aG docker deployer
```

### 5.2 Structure des fichiers sur le VPS
```
/opt/revise-tes-maths/
├── docker-compose.yml
├── .env
├── backend/
│   ├── .env
│   └── ...
├── frontend/
│   └── ...
└── data/
    └── postgres/
```

### 5.3 Procédure de déploiement

1. **Préparation du VPS**
```bash
# Se connecter au VPS
ssh deployer@votre-vps

# Créer la structure
mkdir -p /opt/revise-tes-maths
cd /opt/revise-tes-maths

# Cloner le repository
git clone votre-repo .
```

2. **Configuration des variables d'environnement**
```bash
# Copier les exemples
cp backend/.env.example backend/.env
cp .env.example .env

# Éditer les fichiers avec les vraies valeurs
nano backend/.env
nano .env
```

3. **Premier déploiement**
```bash
# Construire et démarrer les conteneurs
docker-compose -f docker-compose.yml up -d --build
```

4. **Vérification**
```bash
# Vérifier les logs
docker-compose logs -f

# Tester les endpoints
curl http://localhost:5000/api/health
```

### 5.4 Mise à jour de l'application

```bash
# Arrêter les conteneurs
docker-compose down

# Puller les changements
git pull origin main

# Reconstruire et redémarrer
docker-compose up -d --build
```

### 5.5 Sauvegarde des données

```bash
# Backup de la base de données
docker-compose exec db pg_dump -U rtm_user rtm > backup_$(date +%Y%m%d).sql

# Backup des volumes
docker run --rm -v revise_tes_maths_nuxt_postgres_data:/data -v $(pwd):/backup ubuntu tar czf /backup/postgres_data_$(date +%Y%m%d).tar.gz /data
```

### 5.6 Restauration des données

```bash
# Restaurer la base de données
cat backup_YYYYMMDD.sql | docker-compose exec -T db psql -U rtm_user rtm

# Restaurer les volumes
docker run --rm -v revise_tes_maths_nuxt_postgres_data:/data -v $(pwd):/backup ubuntu bash -c "cd /data && tar xzf /backup/postgres_data_YYYYMMDD.tar.gz --strip 1"
```

### 5.7 Maintenance

```bash
# Nettoyage des images non utilisées
docker system prune -a

# Vérification de l'espace disque
docker system df

# Rotation des logs
docker-compose logs > logs_$(date +%Y%m%d).txt
```

### 5.8 Sécurité

1. **Pare-feu (UFW)**
```bash
ufw allow ssh
ufw allow http
ufw allow https
ufw enable
```

2. **Certificat SSL avec Let's Encrypt**
```bash
apt install certbot python3-certbot-nginx
certbot --nginx -d votre-domaine.com
```

3. **Configuration Nginx**
```nginx
server {
    listen 80;
    server_name votre-domaine.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name votre-domaine.com;

    ssl_certificate /etc/letsencrypt/live/votre-domaine.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/votre-domaine.com/privkey.pem;

    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 5.9 Monitoring

```bash
# Installation de Portainer (optionnel)
docker volume create portainer_data
docker run -d -p 9000:9000 --name=portainer --restart=always \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v portainer_data:/data \
    portainer/portainer-ce
```

### 5.10 Troubleshooting

1. **Problèmes de connexion à la base de données**
```bash
# Vérifier les logs de la base
docker-compose logs db

# Vérifier la connexion
docker-compose exec backend python -c "from app import db; db.create_all()"
```

2. **Problèmes de permissions**
```bash
# Vérifier les permissions des volumes
ls -la /var/lib/docker/volumes/

# Corriger les permissions
chown -R 1000:1000 /opt/revise-tes-maths/data
```

3. **Problèmes de mémoire**
```bash
# Vérifier l'utilisation des ressources
docker stats

# Nettoyer les conteneurs non utilisés
docker container prune
``` 