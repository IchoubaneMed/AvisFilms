# Projet de Gestion d'Avis sur les Films

Ce projet est un site de gestion d'avis sur des films. La page d'accueil affiche une liste de 5 films à la fois.

## Installation

Pour démarrer le projet, assurez-vous que vous êtes dans le répertoire contenant les dossiers frontend et backend, puis exécutez la commande suivante :

``bash
docker-compose up -d --build

Cette commande construira et démarrera les conteneurs Docker pour le backend et le frontend du projet.

## Accès au Site

Après avoir démarré les conteneurs Docker, vous pouvez accéder au site en naviguant vers le lien suivant dans votre navigateur web :

http://localhost:5173/

## Structure du Projet

Backend : Le dossier backend contient le code source du serveur backend de l'application. Il est écrit en Django et fournit une API pour gérer les films et les avis

Frontend : Le dossier frontend contient le code source de l'interface utilisateur de l'application. Il est écrit en Vue.js et communique avec le backend via l'API fournie.