#!/bin/bash

# Définir le répertoire de backup
BACKUP_DIR="/home/massyl/backups/uploads"
mkdir -p $BACKUP_DIR

# Créer le nom du fichier avec la date
BACKUP_FILE="uploads_$(date +%Y%m%d_%H%M%S).tar.gz"

# Créer la sauvegarde
docker run --rm -v revise_tes_maths_nuxt_uploads:/source -v $BACKUP_DIR:/backup alpine tar czf /backup/$BACKUP_FILE -C /source .

# Garder seulement les 7 dernières sauvegardes
cd $BACKUP_DIR && ls -t | tail -n +8 | xargs -r rm --

# Afficher un message de confirmation
echo "Sauvegarde créée : $BACKUP_DIR/$BACKUP_FILE" 