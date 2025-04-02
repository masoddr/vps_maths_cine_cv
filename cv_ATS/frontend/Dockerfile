FROM node:20-alpine

WORKDIR /app

# Copie des fichiers de dépendances
COPY package*.json ./

# Installation des dépendances
RUN npm install

# Copie du reste des fichiers
COPY . .

# Copie de la favicon
COPY public ./public

# Build de l'application
RUN npm run build

# Exposition du port
EXPOSE 3002

# Vérification que le fichier existe
RUN ls -la .output/server/index.mjs

# Commande de démarrage en production
CMD ["node", ".output/server/index.mjs"] 