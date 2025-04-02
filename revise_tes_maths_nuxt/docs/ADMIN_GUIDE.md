# Guide Administrateur - Dashboard Révisions Bac

## 1. Comptes Utilisateurs

### 1.1 Compte Administrateur par défaut
```
Email: admin@example.com
Mot de passe: admin123
```

### 1.2 Compte Test (utilisateur normal)
```
Email: test@example.com
Mot de passe: password123
```

## 2. Fonctionnalités Administrateur

### 2.1 Gestion des Utilisateurs
- Accès via `/api/admin/users`
- Liste de tous les utilisateurs
- Modification des informations utilisateur
- Activation/désactivation des comptes
- Suppression des comptes

### 2.2 Gestion des Annales
- Accès via `/api/admin/exampapers`
- Ajout de nouvelles annales
- Modification des annales existantes
- Suppression d'annales
- Gestion des fichiers PDF associés

### 2.3 Gestion des Exercices
- Ajout/modification des exercices dans les annales
- Attribution des thèmes aux exercices
- Organisation des exercices par difficulté

## 3. Sécurité

### 3.1 Bonnes Pratiques
- Changer le mot de passe administrateur par défaut
- Utiliser des mots de passe forts
- Ne pas partager les identifiants administrateur
- Se déconnecter après chaque session

### 3.2 Gestion des Accès
- Seuls les utilisateurs avec `is_admin=True` peuvent accéder aux fonctionnalités d'administration
- Les routes administratives sont protégées par authentification
- Les tentatives d'accès non autorisées sont journalisées

## 4. Maintenance

### 4.1 Base de Données
- Les migrations sont gérées avec Flask-Migrate
- Pour créer une nouvelle migration : `flask db migrate -m "description"`
- Pour appliquer les migrations : `flask db upgrade`

### 4.2 Fichiers
- Les PDF des annales sont stockés dans `backend/static/uploads/pdfs/`
- Sauvegarder régulièrement ce dossier

## 5. Scripts Utiles

### 5.1 Création d'Utilisateurs
- `create_admin_user.py` : Crée un compte administrateur
- `create_test_user.py` : Crée un compte utilisateur de test

### 5.2 Commandes de Base
```bash
# Créer un nouvel administrateur
python create_admin_user.py

# Créer un utilisateur test
python create_test_user.py

# Mettre à jour la base de données
flask db upgrade
```

## 6. Résolution des Problèmes Courants

### 6.1 Problèmes d'Authentification
- Vérifier que la base de données est à jour
- Vérifier que les tables existent avec `flask db current`
- Réinitialiser le mot de passe si nécessaire

### 6.2 Problèmes de Fichiers
- Vérifier les permissions du dossier `uploads`
- S'assurer que le dossier existe
- Vérifier l'espace disque disponible 

## 7. Gestion des Thèmes

### 7.1 Thèmes Disponibles
- Probabilités
- Loi Binomiale
- Géométrie dans l'espace
- Suites
- Études de fonctions
- Exponentielle
- Logarithme Népérien
- Intégrale
- Convexité
- Equations différentielles
- Python

### 7.2 Attribution des Thèmes
- Chaque exercice peut avoir plusieurs thèmes
- Veiller à la cohérence des thèmes entre les exercices similaires
- Utiliser exactement les mêmes noms de thèmes pour garantir un bon fonctionnement des filtres

## 8. Surveillance et Statistiques

### 8.1 Statistiques Globales
- Nombre total d'utilisateurs actifs
- Nombre d'annales disponibles
- Taux de complétion moyen des exercices
- Thèmes les plus/moins travaillés

### 8.2 Surveillance des Performances
- Vérifier régulièrement l'espace disque (notamment pour les PDFs)
- Surveiller les temps de réponse de l'API
- Monitorer les erreurs dans les logs

## 9. Gestion du Contenu

### 9.1 Format des Annales
- Format attendu des PDFs
- Nommage recommandé : `bac_[ANNÉE]_[SESSION].pdf`
- Taille maximale acceptée : 10 MB par fichier

### 9.2 Organisation des Exercices
- Numérotation cohérente des exercices
- Description claire et concise
- Vérification des liens PDF
- Validation des thèmes attribués

## 10. Procédures de Sauvegarde

### 10.1 Base de Données
```bash
# Sauvegarde de la base de données
pg_dump nom_base > backup_[DATE].sql

# Restauration
psql nom_base < backup_[DATE].sql
```

### 10.2 Fichiers PDF
```bash
# Sauvegarde des PDFs
tar -czf pdfs_backup_[DATE].tar.gz backend/static/uploads/pdfs/
```

## 11. Déploiement et Maintenance en Production

### 11.1 Prérequis Serveur
- Ubuntu 22.04 LTS ou plus récent
- Au moins 2GB de RAM
- 20GB d'espace disque
- Un nom de domaine configuré

### 11.2 Installation Initiale
```bash
# Connexion au serveur
ssh root@votre-serveur

# Mise à jour du système
apt update && apt upgrade -y

# Installation des dépendances
apt install -y docker.io docker-compose nginx certbot python3-certbot-nginx

# Création de l'utilisateur de déploiement
adduser deployer
usermod -aG docker deployer
```

### 11.3 Configuration du Déploiement
1. **Structure des répertoires**
```bash
mkdir -p /opt/revise-tes-maths
chown -R deployer:deployer /opt/revise-tes-maths
```

2. **Variables d'environnement**
Créer `/opt/revise-tes-maths/.env` :
```env
# PostgreSQL
POSTGRES_DB=rtm
POSTGRES_USER=rtm_user
POSTGRES_PASSWORD=votre_mot_de_passe_securise

# Backend
FLASK_ENV=production
SECRET_KEY=votre_cle_secrete_tres_longue
DATABASE_URL=postgresql://rtm_user:votre_mot_de_passe_securise@db:5432/rtm

# Frontend
NODE_ENV=production
```

3. **Configuration Nginx**
Créer `/etc/nginx/sites-available/revise-tes-maths` :
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

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Limites et sécurité
    client_max_body_size 10M;
    add_header X-Frame-Options "SAMEORIGIN";
    add_header X-XSS-Protection "1; mode=block";
    add_header X-Content-Type-Options "nosniff";
}
```

### 11.4 Procédures de Déploiement

1. **Premier déploiement**
```bash
# En tant que deployer
cd /opt/revise-tes-maths

# Cloner le repository
git clone votre-repo .

# Copier et configurer les variables d'environnement
cp .env.example .env
nano .env

# Démarrer les services
docker-compose up -d

# Initialiser la base de données
docker-compose exec backend python init_db.py
```

2. **Mise à jour de l'application**
```bash
# Arrêter les services
docker-compose down

# Mettre à jour le code
git pull

# Reconstruire et redémarrer
docker-compose up -d --build
```

### 11.5 Sauvegardes

1. **Sauvegarde automatique**
Créer `/opt/revise-tes-maths/backup.sh` :
```bash
#!/bin/bash
BACKUP_DIR="/opt/revise-tes-maths/backups"
DATE=$(date +%Y%m%d_%H%M%S)

# Créer le répertoire de backup
mkdir -p $BACKUP_DIR

# Backup de la base de données
docker-compose exec -T db pg_dump -U rtm_user rtm > $BACKUP_DIR/db_$DATE.sql

# Backup des uploads
tar -czf $BACKUP_DIR/uploads_$DATE.tar.gz backend/static/uploads/

# Nettoyer les vieux backups (garder 7 jours)
find $BACKUP_DIR -type f -mtime +7 -delete
```

2. **Configuration de cron**
```bash
# Ajouter au crontab
0 2 * * * /opt/revise-tes-maths/backup.sh
```

### 11.6 Monitoring

1. **Logs Docker**
```bash
# Voir les logs en temps réel
docker-compose logs -f

# Sauvegarder les logs
docker-compose logs > logs_$(date +%Y%m%d).txt
```

2. **Surveillance des ressources**
```bash
# Utilisation des ressources
docker stats

# Espace disque
df -h
```

### 11.7 Résolution des Problèmes

1. **L'application ne répond pas**
```bash
# Vérifier l'état des conteneurs
docker-compose ps

# Redémarrer les services
docker-compose restart

# Vérifier les logs
docker-compose logs --tail=100
```

2. **Problèmes de base de données**
```bash
# Vérifier la connexion
docker-compose exec backend python -c "from app import db; db.create_all()"

# Vérifier les migrations
docker-compose exec backend flask db current
```

3. **Problèmes de certificat SSL**
```bash
# Renouveler le certificat
certbot renew

# Vérifier la configuration Nginx
nginx -t
```

### 11.8 Sécurité

1. **Pare-feu (UFW)**
```bash
ufw default deny incoming
ufw default allow outgoing
ufw allow ssh
ufw allow http
ufw allow https
ufw enable
```

2. **Fail2ban**
```bash
apt install fail2ban
cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
systemctl enable fail2ban
systemctl start fail2ban
```

3. **Mises à jour de sécurité**
```bash
# Activer les mises à jour automatiques
apt install unattended-upgrades
dpkg-reconfigure -plow unattended-upgrades
```

### 11.9 Performance

1. **Optimisation Nginx**
```nginx
# Ajouter dans nginx.conf
worker_processes auto;
worker_connections 1024;
keepalive_timeout 65;
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;
```

2. **Cache**
```nginx
# Ajouter dans la configuration du site
location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
    expires 7d;
    add_header Cache-Control "public, no-transform";
}
```

### 11.10 Maintenance Quotidienne

1. **Vérifications quotidiennes**
- [ ] Vérifier les logs pour des erreurs
- [ ] Vérifier l'espace disque disponible
- [ ] Vérifier que les backups sont à jour
- [ ] Vérifier l'état des conteneurs

2. **Vérifications hebdomadaires**
- [ ] Vérifier les mises à jour disponibles
- [ ] Nettoyer les vieux logs
- [ ] Vérifier les performances
- [ ] Tester la restauration des backups

3. **Vérifications mensuelles**
- [ ] Renouvellement du certificat SSL
- [ ] Audit de sécurité
- [ ] Nettoyage des données temporaires
- [ ] Test de restauration complète

## 12. RGPD et Conformité

### 12.1 Données Personnelles
- Types de données collectées
- Durée de conservation
- Procédure de suppression des comptes
- Export des données personnelles

### 12.2 Mentions Légales
- CGU à maintenir à jour
- Politique de confidentialité
- Procédure de contact
- Droits des utilisateurs

## 13. Support Utilisateur

### 13.1 Problèmes Fréquents
- Réinitialisation de mot de passe
- Problèmes d'accès aux PDFs
- Questions sur les statistiques
- Erreurs de synchronisation

### 13.2 Procédures de Support
- Canal de contact privilégié
- Temps de réponse attendu
- Escalade des problèmes
- Documentation des solutions 