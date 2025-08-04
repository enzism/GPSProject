# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import osmnx as ox
import networkx as nx
from typing import Tuple, List
import json

# --- Initialisation de l'application ---
app = FastAPI(title="Itinéraire Cyclable API", version="1.0")

# --- Middleware CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Chargement du graphe OSM ---
print("[INFO] Chargement du graphe OSM...")
# Filtres servant à choisir le type de route autorisées par l'itinéraire
custom_filter = (
    '["highway"]'
    '["area"!~"yes"]'
    '["highway"!~"motorway|motorway_link|trunk|trunk_link|raceway"]'
    '["access"!~"private"]'
)

GRAPH = ox.graph_from_place("Marseille, France")#, custom_filter=custom_filter)

# --- Modèle de requête ---
class RouteRequest(BaseModel):
    origin: Tuple[float, float]       # (latitude, longitude)
    destination: Tuple[float, float]

# Charger la zone de la ville (polygone)
print("[INFO] Chargement du polygone de la zone...")
gdf = ox.geocode_to_gdf("Marseille, France")
city_polygon_geojson = json.loads(gdf.to_json())

@app.get("/zone")
async def get_zone():
    """Retourne le polygone GeoJSON de la zone de la ville."""
    return JSONResponse(content=city_polygon_geojson)

# --- Endpoint principal ---
@app.post("/route")
async def get_route(req: RouteRequest) -> dict:
    """Retourne une liste de coordonnées (lat, lon) représentant l'itinéraire le plus court."""
    try:
        orig_node = ox.distance.nearest_nodes(GRAPH, X=req.origin[1], Y=req.origin[0])
        dest_node = ox.distance.nearest_nodes(GRAPH, X=req.destination[1], Y=req.destination[0])
        route_nodes = nx.shortest_path(GRAPH, orig_node, dest_node, weight='length')
        coordinates = [(GRAPH.nodes[n]['y'], GRAPH.nodes[n]['x']) for n in route_nodes]
        return {"route": coordinates}
    except Exception as e:
        return {"error": str(e)}