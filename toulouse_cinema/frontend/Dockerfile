# Image de base pour la construction
FROM node:20.11.1-slim as builder

# Définition des variables d'environnement pour npm
ENV NODE_ENV=production
ENV HUSKY=0
ENV PORT=3001

# Répertoire de travail
WORKDIR /app

# Copie uniquement des fichiers nécessaires pour l'installation des dépendances
COPY package*.json ./

# Installation des dépendances avec uniquement les dépendances de production
RUN npm install

# Copie des fichiers source nécessaires pour la construction
COPY . .

# Construction de l'application
RUN npm run build

# Image finale
FROM node:20.11.1-alpine

WORKDIR /app

# Copie uniquement les fichiers nécessaires depuis l'étape de build
COPY --from=builder /app/.output /app/.output

# Exposition du port (utilisation de la variable d'environnement)
EXPOSE ${PORT}

# Healthcheck pour vérifier que l'application fonctionne
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:${PORT}/ || exit 1

# Utilisateur non-root pour la sécurité
USER node

# Commande de démarrage
CMD ["node", ".output/server/index.mjs"] 