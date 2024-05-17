# Utiliser une image de Node.js comme base
FROM node:20.13.1

# Répertoire de travail dans le conteneur
WORKDIR /app
# Copier les fichiers package.json du projet dans le conteneur
COPY package.json ./
RUN npm install

# Copier les fichiers du projet dans le conteneur
COPY . .

# Construire l'application Vue.js
RUN npm run build
# Exposer le port 5173 pour que l'application soit accessible depuis l'extérieur
EXPOSE 5173
CMD ["npm","run","dev"]