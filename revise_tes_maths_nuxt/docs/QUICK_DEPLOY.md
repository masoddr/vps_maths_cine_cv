# Guide de Déploiement Rapide - Revise Tes Maths

## 0. Pré-requis et checklist

### Checklist avant déploiement
- [ ] Nom de domaine configuré et pointant vers votre serveur
- [ ] Accès SSH au serveur
- [ ] Au moins 2GB de RAM sur le serveur
- [ ] Au moins 20GB d'espace disque
- [ ] Ports 80 et 443 ouverts

### Variables à préparer
1. Générer une clé secrète pour Flask :
```bash
# Sur votre machine locale avec Python
python3 -c "import secrets; print(secrets.token_hex(32))"
```

2. Préparer les informations suivantes :
- Nom de domaine (ex: revise-tes-maths.fr)
- Mot de passe PostgreSQL sécurisé
- Email pour le certificat SSL

## 1. Préparation du serveur

```bash
# Installation des dépendances
sudo apt update
sudo apt install -y docker.io docker-compose nginx certbot python3-certbot-nginx

# Ajout de votre utilisateur au groupe docker
sudo usermod -aG docker massyl
# Déconnectez-vous et reconnectez-vous pour que les changements prennent effet
```

## 2. Configuration du projet

```bash
# Création du répertoire
mkdir -p ~/apps/revise-tes-maths
cd ~/apps/revise-tes-maths

# Clonage du projet
git clone https://github.com/masoddr/revise_tes_maths_nuxt.git .
git checkout docker

# Configuration des variables d'environnement
cp .env.example .env
```

Éditez le fichier `.env` avec vos valeurs :
```env
# PostgreSQL
POSTGRES_DB=rtm
POSTGRES_USER=rtm_user
POSTGRES_PASSWORD=votre_mot_de_passe_securise  # Changez ceci !

# Flask
FLASK_ENV=production
SECRET_KEY=votre_cle_secrete_aleatoire        # Collez ici la clé générée précédemment
SESSION_COOKIE_SECURE=true
PERMANENT_SESSION_LIFETIME=86400  # 24 heures en secondes

# Frontend
NODE_ENV=production
NUXT_PUBLIC_API_BASE=https://votre-domaine.com/api  # Changez ceci !
```

## 3. Configuration Nginx

```bash
# Création du fichier de configuration
sudo nano /etc/nginx/sites-available/revise-tes-maths
```

Contenu du fichier :
```nginx
server {
    listen 80;
    server_name votre-domaine.com;  # Changez ceci !
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name votre-domaine.com;  # Changez ceci !

    ssl_certificate /etc/letsencrypt/live/votre-domaine.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/votre-domaine.com/privkey.pem;

    # Configuration SSL renforcée
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers on;
    
    # Headers de sécurité
    add_header Strict-Transport-Security "max-age=31536000" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;

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
}
```

```bash
# Activation de la configuration
sudo ln -s /etc/nginx/sites-available/revise-tes-maths /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default  # Supprime la configuration par défaut
sudo nginx -t  # Vérifie la configuration
sudo systemctl restart nginx
```

## 4. Configuration SSL

```bash
# Obtention du certificat SSL
sudo certbot --nginx -d votre-domaine.com
```

## 5. Lancement de l'application

```bash
cd ~/apps/revise-tes-maths

# Arrêt des conteneurs existants (si nécessaire)
docker-compose down

# Construction et démarrage des conteneurs
docker-compose up -d --build

# Vérification des logs
docker-compose logs -f
```

## 6. Vérification du déploiement

### 6.1 Vérification des conteneurs
```bash
docker-compose ps
```

### 6.2 Vérification des services
1. Testez l'accès à l'application :
   - Frontend : https://votre-domaine.com
   - Backend : https://votre-domaine.com/api/health

2. Vérifiez les logs de chaque service :
```bash
# Logs du backend
docker-compose logs backend

# Logs du frontend
docker-compose logs frontend

# Logs de la base de données
docker-compose logs db
```

3. Vérifiez la sécurité :
```bash
# Tester les en-têtes de sécurité
curl -I https://votre-domaine.com

# Vérifier le certificat SSL
curl https://www.ssllabs.com/ssltest/analyze.html?d=votre-domaine.com
```

4. Connectez-vous avec le compte admin :
   - Email : admin@example.com
   - Mot de passe : admin123
   
   **IMPORTANT** : Changez immédiatement le mot de passe admin après la première connexion !

## 7. Configuration des sauvegardes

```bash
# Création du script de backup
mkdir -p ~/apps/revise-tes-maths/backups
nano ~/apps/revise-tes-maths/backup.sh
```

Contenu du script :
```bash
#!/bin/bash
BACKUP_DIR="/home/massyl/apps/revise-tes-maths/backups"
DATE=$(date +%Y%m%d_%H%M%S)

# Backup de la base de données
cd /home/massyl/apps/revise-tes-maths
docker-compose exec -T db pg_dump -U rtm_user rtm > $BACKUP_DIR/db_$DATE.sql
gzip $BACKUP_DIR/db_$DATE.sql

# Nettoyage des backups de plus de 7 jours
find $BACKUP_DIR -type f -mtime +7 -delete
```

```bash
# Rendre le script exécutable
chmod +x ~/apps/revise-tes-maths/backup.sh

# Configuration de la sauvegarde quotidienne
(crontab -l 2>/dev/null; echo "0 2 * * * /home/massyl/apps/revise-tes-maths/backup.sh") | crontab -
```

## 8. Commandes utiles

### Gestion des conteneurs
```bash
# Voir les logs en temps réel
docker-compose logs -f

# Redémarrer un service spécifique
docker-compose restart backend  # ou frontend ou db

# Voir l'utilisation des ressources
docker stats
```

### Maintenance
```bash
# Nettoyage des images non utilisées
docker system prune -a

# Sauvegarde manuelle
~/apps/revise-tes-maths/backup.sh
```

### Mise à jour de l'application
```bash
cd ~/apps/revise-tes-maths
git pull origin docker
docker-compose down
docker-compose up -d --build
```

## 9. Résolution des problèmes courants

1. **Les conteneurs ne démarrent pas** :
```bash
# Vérifier les logs détaillés
docker-compose logs --tail=100
```

2. **Problèmes de base de données** :
```bash
# Vérifier la connexion à la base de données
docker-compose exec backend python -c "from app import db; db.create_all()"
```

3. **Problèmes de permissions** :
```bash
# Vérifier les permissions des volumes
sudo ls -la /var/lib/docker/volumes/
```

4. **Erreurs Nginx** :
```bash
# Vérifier les logs Nginx
sudo tail -f /var/log/nginx/error.log
```

## 10. Maintenance de Production

### 10.1 Surveillance des ressources
```bash
# Espace disque
df -h

# Utilisation mémoire
free -m

# Charge CPU
top

# Logs système
sudo journalctl -f
```

### 10.2 Maintenance régulière
```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Nettoyage des logs
sudo journalctl --vacuum-time=7d

# Vérification des certificats SSL
sudo certbot certificates
```

### 10.3 Sécurité
```bash
# Vérification des tentatives de connexion échouées
sudo grep "Failed password" /var/log/auth.log

# Liste des connexions actives
netstat -tulpn

# Vérification des services en cours
systemctl status nginx docker
``` 