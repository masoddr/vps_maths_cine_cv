FROM node:20-alpine

WORKDIR /app

# Copie des fichiers de dépendances
COPY package*.json ./

# Installation des dépendances
RUN npm install

# Copie du reste des fichiers
COPY . .

# Build de l'application
RUN npm run build

# Exposition du port
EXPOSE 3002

# Commande de démarrage en production
CMD ["node", ".output/server/index.mjs"] 