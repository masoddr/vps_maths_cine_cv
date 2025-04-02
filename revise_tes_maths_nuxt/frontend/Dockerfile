# Image de base
FROM node:20.11.1-slim as builder

# Répertoire de travail
WORKDIR /app

# Copie des fichiers de dépendances
COPY package*.json ./

# Installation de toutes les dépendances (y compris dev)
RUN npm install

# Copie du reste du code
COPY . .

# Construction de l'application
RUN npm run build

# Image finale plus légère
FROM node:20.11.1-slim

# Installation de curl pour le healthcheck
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copie des fichiers nécessaires depuis l'étape de build
COPY --from=builder /app/.output /app/.output

# Exposition du port
EXPOSE 3000

# Commande par défaut
CMD ["node", ".output/server/index.mjs"] 