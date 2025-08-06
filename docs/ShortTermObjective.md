#  Objectif à court terme : fonctionnalité de base fonctionnelle
(last update: 06/08/2025)
## 🟩 1. Finaliser le routage de base
- ✅ Chargement dynamique du graphe autour du point de départ

- ✅ Calcul du chemin entre deux points

- ⬜️ Gestion propre des erreurs : renvoyer un message lisible en cas de routage impossible

**🔹 Priorité : Haute**\
🎯 Raison : cœur du fonctionnement. Il faut que l’utilisateur puisse obtenir une réponse fiable avant d’ajouter quoi que ce soit d’autre.

## 🟩 2. Interface utilisateur minimale mais fonctionnelle
- ✅ Carte Leaflet.js qui s'affiche

- ✅ Ajout de deux points

- ✅ Affichage de la route tracée

- ⬜️ Bouton "reset" pour effacer les points / itinéraire

**🔹 Priorité : Haute**\
🎯 Raison : avoir une démo utilisable rapidement même sans tout le reste.

## 🟧 3. Refactorisation / nettoyage du JS
- ⬜️ Séparer les fonctions (ajout de points, envoi de la requête, affichage itinéraire)

- ⬜️ Ajouter des logs dans la console pour debug plus facilement

- ⬜️ Ajouter des commentaires (comme tu le souhaitais pour Python)

**🔹 Priorité : Moyenne**\
🎯 Raison : utile pour la maintenabilité à moyen terme, surtout si tu ajoutes plusieurs fonctionnalités ensuite.

📦 Objectif à moyen terme : vers un produit exploitable
## 🟦 4. Ajout de fonctionnalités interactives
- ⬜️ Liste éditable de points (plus que 2)

- ⬜️ Géocodeur de villes (déjà partiellement présent)

- ⬜️ Suggestions automatiques d’étapes (plus tard)

- ⬜️ Prise en compte de profils cyclistes

**🔹 Priorité : Moyenne / Basse (par ordre d’ajout progressif)**\
🎯 Raison : à intégrer une fois le moteur de routage et la carte sont solides.

## 🟨 5. Logs, tests, monitoring
- ⬜️ Ajouter un logger Python au lieu d’un simple print

- ⬜️ Ajouter des tests unitaires dans /tests

- ⬜️ Gérer les erreurs 404 / 500 dans l’API

- ⬜️ Mesurer les temps de réponse des endpoints (si besoin)

**🔹 Priorité : Moyenne**\
🎯 Raison : nécessaire pour fiabiliser le backend, surtout avant de scaler.

## 🟪 6. Déploiement et conteneurisation
- ⬜️ Dockeriser proprement l’app

- ⬜️ Lancer en local avec docker-compose

- ⬜️ Préparer un déploiement sur Railway / Fly.io / Render

**🔹 Priorité : Moyenne → Haute une fois les fonctionnalités de base terminées**