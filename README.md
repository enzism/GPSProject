#  Planificateur d’Itinéraire Cyclable (Prototype)

Ce projet est un prototype d'API web pour le calcul d'itinéraires cyclables, basé sur OpenStreetMap et OSMnx.

###  Objectif final
Créer une application web de planification d’itinéraire de bikepacking :
- Multijour, avec suggestion automatique d’étapes.
- Destinée à plusieurs profils (cyclotouristes, sportifs, ultra).
- Intégrant les hébergements (camping, hôtel, bivouac, etc.).
- Personnalisable (distance, effort, équipement).
- Scalable (Europe entière, sans limite de zone).
- Industrialisable (architecture claire, API propre, interface user-friendly).

##  Fonctionnement global
L'application repose sur trois briques principales :
- FastAPI : framework web rapide et moderne pour construire des APIs REST.
- OSMnx : librairie Python qui facilite le téléchargement et la manipulation de réseaux routiers à partir d'OpenStreetMap.
- NetworkX : librairie Python pour la manipulation de graphes, utilisée ici pour calculer le plus court chemin entre deux noeuds du réseau.
L'utilisateur envoie une requête POST à l'API avec deux points (origine et destination), et reçoit en retour une liste de coordonnées représentant l'itinéraire.

##  Structure du projet
```bash
GPSProject/
├── app/                  # Backend FastAPI
├── static/               # Frontend (HTML/JS/CSS séparés)
├── routing/              # Logique de calcul d’itinéraire
├── notebooks/            # Explorations, démos, machine learning
├── tests/                # Tests unitaires
├── README.md             # Présentation claire du projet
└── Dockerfile            # Environnement reproductible

```

##  Prérequis
- Python 3.8+
- pip

##  Installation
```bash
git clone https://github.com/enzism/GPSProject.git
cd GPSProject
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##  Lancement du serveur
```bash
uvicorn app.main:app --reload
```
L’API est accessible sur : http://localhost:8000/docs

###  Exemple de requête
```python
POST /route
{
  "origin": [45.1885, 5.7245],
  "destination": [45.1648, 5.7126]
}
```

### Réponse attendue
```python
{
  "route": [
    [45.188511, 5.724543],
    [45.187900, 5.723700],
    ...
  ]
}
```

## Explication du code (fichier main.py)
1. Initialisation de l'application
```python
app - FastAPI(...)
```
Crée le serveur web (objet FastAPI)
2. Middleware CORS
```python
app.add_middleware(CORSMiddleware, ...)
```
Autorise un front-end (comme une page web avec Leaflet.js) à communiquer avec le back-end (app.py)
3. Cahrgement du graphe de routes
```python
GRAPH = ox.graph_from_place("Grenoble, France", network_type="bike")
```
Télécharge depuis OpenStreetMap un graphe de voirie cyclable pour la ville de Grenoble
4. Modèle de requête
```python
class RouteRequest(BaseModel):
    origin: Tuple[float, float]
    destination: Tuple[float, float]
```
Définit le format attendu de la requête API.
5. Calcul d’itinéraire
```python 
nx.shortest_path(GRAPH, orig_node, dest_node, weight='length')
```
Utilise NetworkX pour calculer le plus court chemin entre les deux points (pondéré par la distance réelle).

## TODO
- Modifier le planificateur pour lui permettre de traverser les zone protégées comme les calanques
- Intégrer le dénivelé dans le calcul (pondérer par l’effort)
- Afficher les hébergements à proximité d’un itinéraire
- Stocker les itinéraires et stats dans une base de données (ex: PostgreSQL/PostGIS)

## Technologies
- [FastAPI](https://fastapi.tiangolo.com)
- [OSMnx](https://osmnx.readthedocs.io/en/stable/)
- [NetworkX](https://networkx.org)
- [Leaflet.js](https://leafletjs.com/examples/quick-start/) (contient des explications sur la création du index.html)
