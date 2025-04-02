# Guide de la Base de Données - Révise Tes Maths

## 1. Architecture de la Base de Données

### 1.1 Modèles de Données

#### User (Utilisateur)
```sql
CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    password_hash VARCHAR(128) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);
```

#### ExamPaper (Annale)
```sql
CREATE TABLE exam_paper (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    year INTEGER NOT NULL,
    pdf_url VARCHAR(500) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

#### Exercise (Exercice)
```sql
CREATE TABLE exercise (
    id SERIAL PRIMARY KEY,
    number INTEGER NOT NULL,
    description TEXT,
    themes VARCHAR(100)[], -- Tableau de thèmes
    exam_paper_id INTEGER REFERENCES exam_paper(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

#### Progress (Progression)
```sql
CREATE TABLE progress (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES "user"(id) ON DELETE CASCADE,
    exercise_id INTEGER REFERENCES exercise(id) ON DELETE CASCADE,
    status VARCHAR(32) NOT NULL, -- 'not_started', 'in_progress', 'completed'
    time_spent INTEGER, -- temps en minutes
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### 1.2 Relations

- Un `User` peut avoir plusieurs `Progress`
- Un `ExamPaper` contient plusieurs `Exercise`
- Un `Exercise` peut avoir plusieurs `Progress`
- Chaque `Progress` est lié à un `User` et un `Exercise`

## 2. Administration de la Base de Données

### 2.1 Installation sur un VPS

```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y

# Installation de PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Vérification du statut
sudo systemctl status postgresql
```

### 2.2 Configuration Initiale

```bash
# Connexion en tant qu'utilisateur postgres
sudo -u postgres psql

# Création de la base de données
CREATE DATABASE revise_tes_maths;

# Création de l'utilisateur de l'application
CREATE USER app_user WITH PASSWORD 'votre_mot_de_passe_securise';

# Attribution des privilèges
GRANT ALL PRIVILEGES ON DATABASE revise_tes_maths TO app_user;
```

### 2.3 Configuration de PostgreSQL

Éditer le fichier `/etc/postgresql/[version]/main/postgresql.conf` :

```ini
# Ajustements de mémoire
shared_buffers = 256MB          # 25% de la RAM pour un petit VPS
work_mem = 16MB                 # Pour les opérations de tri
maintenance_work_mem = 128MB    # Pour les opérations de maintenance

# Paramètres de journalisation
log_min_duration_statement = 200  # Log des requêtes lentes (>200ms)
log_checkpoints = on
log_connections = on
log_disconnections = on

# Optimisations diverses
effective_cache_size = 768MB    # 75% de la RAM pour un petit VPS
random_page_cost = 1.1          # Pour SSD
```

### 2.4 Sécurisation

Éditer le fichier `/etc/postgresql/[version]/main/pg_hba.conf` :

```conf
# IPv4 local connections:
host    revise_tes_maths    app_user    127.0.0.1/32         scram-sha-256
host    revise_tes_maths    app_user    [votre_ip_vps]/32    scram-sha-256
```

## 3. Maintenance et Sauvegardes

### 3.1 Sauvegarde Automatique

Créer un script `/usr/local/bin/backup_db.sh` :

```bash
#!/bin/bash
BACKUP_DIR="/var/backups/postgresql"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
DB_NAME="revise_tes_maths"

# Création du répertoire de sauvegarde
mkdir -p $BACKUP_DIR

# Sauvegarde de la base
pg_dump -U postgres $DB_NAME | gzip > "$BACKUP_DIR/${DB_NAME}_${TIMESTAMP}.sql.gz"

# Conservation des 7 derniers jours uniquement
find $BACKUP_DIR -name "${DB_NAME}_*.sql.gz" -mtime +7 -delete
```

Configurer une tâche cron :

```bash
# Éditer avec : sudo crontab -e
0 3 * * * /usr/local/bin/backup_db.sh
```

### 3.2 Restauration

```bash
# Restauration complète
gunzip -c backup_file.sql.gz | psql -U postgres revise_tes_maths

# Restauration sélective (exemple pour la table progress)
pg_restore -U postgres -d revise_tes_maths --table=progress backup_file.sql
```

### 3.3 Maintenance Régulière

```sql
-- Analyse des tables pour le planificateur
ANALYZE VERBOSE;

-- Nettoyage (VACUUM) des tables
VACUUM ANALYZE;

-- Reconstruction des index
REINDEX DATABASE revise_tes_maths;
```

## 4. Comprendre les Migrations de Base de Données

### 4.1 Qu'est-ce qu'une Migration ?

Une migration est un système de contrôle de version pour votre base de données. Elle permet de :
- Faire évoluer le schéma de la base de données de manière contrôlée
- Garder un historique des modifications
- Collaborer en équipe sur la structure de la base
- Revenir en arrière en cas de problème

#### Exemple Concret
Imaginons que vous souhaitez ajouter une colonne `phone_number` à la table `user` :

1. **Sans migration** :
   - Modification directe de la base : `ALTER TABLE user ADD COLUMN phone_number VARCHAR(20);`
   - Problèmes : pas de traçabilité, risque d'erreurs, difficile à répliquer sur d'autres environnements

2. **Avec migration** :
   ```python
   # migrations/versions/abc123_add_phone_number.py
   def upgrade():
       op.add_column('user', sa.Column('phone_number', sa.String(20)))

   def downgrade():
       op.drop_column('user', 'phone_number')
   ```
   - Changements tracés et versionnés
   - Possibilité de revenir en arrière
   - Facilement applicable sur tous les environnements

### 4.2 Pourquoi Utiliser les Migrations ?

1. **Traçabilité**
   - Historique complet des modifications
   - Qui a fait quoi et quand
   - Documentation automatique de l'évolution du schéma

2. **Sécurité**
   - Tests possibles avant application en production
   - Rollback possible en cas de problème
   - Validation des modifications avant déploiement

3. **Collaboration**
   - Plusieurs développeurs peuvent modifier la structure
   - Résolution automatique des conflits
   - Synchronisation facilitée entre environnements

4. **Déploiement**
   - Automatisation des mises à jour
   - Cohérence entre développement et production
   - Réduction des erreurs humaines

### 4.3 Cycle de Vie d'une Migration

1. **Création**
   - Détection des changements dans les modèles
   - Génération automatique du script de migration
   - Vérification et ajustement manuel si nécessaire

2. **Test**
   - Application sur un environnement de développement
   - Vérification du upgrade() et downgrade()
   - Validation des données et des contraintes

3. **Déploiement**
   - Sauvegarde de la base de production
   - Application de la migration
   - Vérification post-déploiement

4. **Maintenance**
   - Conservation de l'historique
   - Nettoyage des anciennes migrations si nécessaire
   - Documentation des changements majeurs

## 5. Utilisation de Flask-Migrate

### 5.1 Commandes Principales

```bash
# Initialisation des migrations
flask db init

# Création d'une nouvelle migration
flask db migrate -m "description de la migration"

# Application des migrations
flask db upgrade

# Retour en arrière
flask db downgrade
```

### 5.2 Bonnes Pratiques pour les Migrations

1. **Toujours vérifier** les fichiers de migration générés
2. **Tester** les migrations sur un environnement de développement
3. **Sauvegarder** la base avant d'appliquer une migration
4. **Documenter** les changements importants

## 6. Surveillance et Optimisation

### 6.1 Requêtes Lentes

```sql
-- Identifier les requêtes lentes
SELECT 
    (total_exec_time / 1000 / 60) as total_minutes,
    calls,
    rows,
    query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;
```

### 6.2 Index Recommandés

```sql
-- Index essentiels
CREATE INDEX idx_progress_user ON progress(user_id);
CREATE INDEX idx_progress_exercise ON progress(exercise_id);
CREATE INDEX idx_exercise_exam_paper ON exercise(exam_paper_id);
CREATE INDEX idx_exam_paper_year ON exam_paper(year);
```

### 6.3 Monitoring

Installation de pgAdmin4 pour le monitoring visuel :

```bash
# Installation
sudo apt install pgadmin4

# Configuration de l'accès web
sudo /usr/pgadmin4/bin/setup-web.sh
```

## 7. Résolution des Problèmes Courants

### 7.1 Connexions

```sql
-- Voir les connexions actives
SELECT * FROM pg_stat_activity;

-- Terminer une connexion bloquée
SELECT pg_terminate_backend(pid);
```

### 7.2 Espace Disque

```sql
-- Taille des tables
SELECT
    relname as table_name,
    pg_size_pretty(pg_total_relation_size(relid)) as total_size
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

### 7.3 Performances

```sql
-- Réinitialiser les statistiques
SELECT pg_stat_reset();

-- Forcer une mise à jour des statistiques
ANALYZE VERBOSE;
```

## 8. Sécurité

### 8.1 Audit des Accès

```sql
-- Créer une table d'audit
CREATE TABLE user_audit_log (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    action VARCHAR(50),
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Exemple de trigger d'audit
CREATE OR REPLACE FUNCTION audit_user_changes()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO user_audit_log(user_id, action)
    VALUES (NEW.id, TG_OP);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### 8.2 Bonnes Pratiques de Sécurité

1. **Sauvegardes Chiffrées**
```bash
# Chiffrement des sauvegardes
gpg --encrypt --recipient your@email.com backup_file.sql
```

2. **Rotation des Mots de Passe**
```sql
-- Modification du mot de passe utilisateur
ALTER USER app_user WITH PASSWORD 'nouveau_mot_de_passe_securise';
```

3. **Limitation des Accès**
```sql
-- Restreindre les privilèges
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM public;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_user;
```

### 8.3 Sécurité des Mots de Passe Utilisateurs

#### Hashage des Mots de Passe
- Les mots de passe sont hashés avec bcrypt avant stockage
- Le processus est unidirectionnel et irréversible
- Même avec un accès complet à la base de données, il est impossible de retrouver les mots de passe originaux

#### Exemple de Fonctionnement
```python
# Dans le modèle User
from werkzeug.security import generate_password_hash, check_password_hash

def set_password(self, password):
    self.password_hash = generate_password_hash(password)

def check_password(self, password):
    return check_password_hash(self.password_hash, password)
```

#### Procédure de Réinitialisation
En cas d'oubli de mot de passe par un utilisateur :
1. L'utilisateur doit demander une réinitialisation
2. Un nouveau mot de passe temporaire est généré
3. Le nouveau hash remplace l'ancien
4. L'ancien mot de passe devient irrécupérable

#### Bonnes Pratiques
1. Ne jamais stocker les mots de passe en clair
2. Ne jamais transmettre les mots de passe par email
3. Forcer la complexité des mots de passe
4. Utiliser HTTPS pour toutes les transmissions
5. Logger les tentatives de connexion échouées

## 9. Variables d'Environnement

Exemple de fichier `.env` pour la configuration de la base de données :

```bash
# Configuration PostgreSQL
POSTGRES_USER=app_user
POSTGRES_PASSWORD=votre_mot_de_passe_securise
POSTGRES_DB=revise_tes_maths
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Configuration des sauvegardes
BACKUP_RETENTION_DAYS=7
BACKUP_DIR=/var/backups/postgresql
```

## 10. Recommandations pour la Production

1. **Monitoring**
   - Mettre en place une surveillance des métriques clés
   - Configurer des alertes pour l'espace disque et la charge CPU

2. **Sauvegardes**
   - Tester régulièrement les restaurations
   - Stocker les sauvegardes sur un système distant

3. **Maintenance**
   - Planifier des fenêtres de maintenance régulières
   - Documenter toutes les interventions

4. **Sécurité**
   - Mettre à jour régulièrement PostgreSQL
   - Auditer régulièrement les accès et permissions 