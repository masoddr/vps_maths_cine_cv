# Image de base
FROM python:3.11.8-slim

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=run.py

# Répertoire de travail
WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code
COPY . .

# Rendre le script d'entrée exécutable
RUN chmod +x docker-entrypoint.sh

# Exposition du port
EXPOSE 5000

# Utiliser le script comme point d'entrée
ENTRYPOINT ["./docker-entrypoint.sh"] 