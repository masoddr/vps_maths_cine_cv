#!/bin/sh

# Attendre que PostgreSQL soit prêt
echo "Waiting for PostgreSQL..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done
echo "PostgreSQL started"

# Initialiser la base de données
echo "Running database migrations..."
flask db upgrade

# Créer l'utilisateur admin s'il n'existe pas déjà
echo "Creating admin user if not exists..."
python create_admin_user.py || echo "Admin user already exists"

# Démarrer Gunicorn
echo "Starting Gunicorn server..."
exec gunicorn --bind 0.0.0.0:5000 run:app 