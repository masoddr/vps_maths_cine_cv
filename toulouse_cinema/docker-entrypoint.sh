#!/bin/bash
set -e

echo "Starting entrypoint script..."

# Vérifier les permissions
ls -l /etc/cron.d/update-seances
cat /etc/cron.d/update-seances

# Installer le crontab
echo "Installing crontab..."
crontab /etc/cron.d/update-seances

echo "Crontab configuration:"
crontab -l

# Démarrer cron en premier plan
echo "Starting cron daemon..."
cron -f

# Exécuter le script une première fois au démarrage
echo "Running initial script execution..."
cd /app && python scripts/update_seances.py >> /var/log/cron.log 2>&1

# Garder le conteneur en vie et suivre les logs
echo "Tailing cron logs..."
tail -f /var/log/cron.log 