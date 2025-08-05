# 🧭 Moteurs de routage : compréhension & intégration
### Qu'est-ce qu'un moteur de routage ?
Un moteur de routage est un logiciel conçu pour calculer des itinéraires optimaux entre plusieurs points en s'appuyant sur un réseau de transport. Il est utilisé dans des applications comme Komoot, Google Maps, BRouter, etc.

## 🔧 Exemples de moteurs open source populaires :
1. **OSRM (Open Source Routing Machine)**
- Langage : C++
- Points forts :
    - Ultra rapide (grâce à la compilation en C++)
    - Prise en charge avancée de profils de routage (piéton, vélo, voiture)
- Fonctionnement :
    - Prétraitement du réseau avec osrm-extract et osrm-contract
    - Expose une API REST locale ou distante via osrm-routed
- Idéal si :
    - Tu veux héberger ton propre service de routage vélo (rapide)
    - Tu maîtrises Docker ou Linux en ligne de commande
2. **GraphHopper**
- Langage : Java
- Points forts :
    - Très flexible et modulaire
    - Supporte le multilingue, les itinéraires alternatifs
    - Très bon support vélo (VTT, route, etc.)
- Fonctionnement :
    - Télécharge les données OSM
    - Prépare le graphe à l’avance
    - Expose une API HTTP via un serveur Java
I- déal si :
    - Tu veux intégrer plus de logique métier et profils personnalisés
3. **Valhalla**
- Langage : C++
- Spécialités :
    - Routage multi-modal (vélo, marche, transports en commun)
    - Prend en compte les vitesses réelles ou horaires
    - Moins populaire que les deux précédents, mais très riche

## 🧩 Comparaison avec OSMnx
| Critère                       | OSRM / GraphHopper                         | OSMnx / NetworkX                     |
|------------------------------|--------------------------------------------|--------------------------------------|
| Type                         | Moteur de routage                          | Librairie Python de graphe OSM       |
| Langage                      | C++ / Java (très rapide)                   | Python (plus lent)                   |
| Usage                        | API HTTP, déployable en local ou serveur   | Script Python, usage en local        |
| Données                      | Préprocessées en `.osm.pbf` (rapide)       | Téléchargées via Overpass            |
| Performances                 | Très élevé (serveurs, mobile possible)     | Moyen (pas pour temps réel large)    |
| Fonctionnalités              | Itinéraire, profil vélo, stats, carrefours | Graphe OSM, analyse topologique      |
| Complexité d’installation    | Moyenne (Docker, setup initial)            | Faible (pip install)                 |
| Intégration API / UI         | Facile (API REST)                          | Doit être encapsulé manuellement     |


## 🔄 Intégration dans mon projet
- Utiliser OSRM ou GraphHopper me permettrait d’avoir un serveur de routage dédié, plus performant et scalable que OSMnx seul.
- OSMnx reste utile pour :
    - Visualisation du graphe
    - Analyse géospatiale (densité, accessibilité, etc.)

## 📚 Ressources à consulter
- [OSRM GitHub](https://github.com/Project-OSRM/osrm-backend)
- [GraphHopper GitHub](https://github.com/graphhopper/graphhopper)
- [Comparatif OSM Tools](https://wiki.openstreetmap.org/wiki/Routing)

### 🎯 Objectif :
> Valoriser mes compétences data science tout en explorant le géo-spatial et le web fullstack

| Domaine               | Stack ou outil à considérer                                   |
|-----------------------|---------------------------------------------------------------|
| **Backend API**       | FastAPI (tu le fais déjà 👌)                                  |
| **UI / Cartographie** | Leaflet.js, HTML/CSS/JS séparés                               |
| **Routage performant**| OSRM ou GraphHopper en Docker                                 |
| **Géo-analyse & données** | OSMnx + Pandas / GeoPandas                              |
| **Déploiement**       | Docker, Render, Railway, ou GitHub Pages + backend API       |
| **Industrialisation** | Séparation claire des modules + typage fort + doc générée    |
| **Scénario data science** | Recommandation d’itinéraires, Prédiction du temps ou de la fatigue selon le profil utilisateur    |

### Bonus portfolio :
- Documenter bien chaque étape (README, captures, GIFs, schémas).
- Intègrer un notebook explicatif sur la partie data.
- Faire une démonstration vidéo (Loom, OBS...).
- Créer un dépôt GitHub propre : readme, issues, projects, wiki.