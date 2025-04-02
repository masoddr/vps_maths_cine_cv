# Toulouse Cinéma - Système de mise à jour automatique

Ce document explique comment le système de mise à jour automatique des séances de cinéma est configuré dans le projet Toulouse Cinéma.

## Architecture

Le projet utilise deux conteneurs Docker :
- **Backend** : Exécute le script de mise à jour des séances via cron
- **Frontend** : Sert l'application web aux utilisateurs

Les données sont partagées entre les conteneurs via un volume Docker.

## Fichiers de configuration

### 1. Crontab (`toulouse_cinema/crontab`)
Le fichier crontab configure l'exécution automatique du script de mise à jour toutes les heures :