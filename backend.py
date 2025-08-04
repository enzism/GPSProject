# main.py (back-end FastAPI)
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import osmnx as ox
import networkx as nx

app = FastAPI()

# Autoriser les requêtes du front (localhost)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Charger le graphe cyclable à l'avance (évite de le recharger à chaque requête)
print("Chargement du graphe OSM...")
G = ox.graph_from_place("Grenoble, France", network_type='bike')

class RouteRequest(BaseModel):
    origin: tuple  # (lat, lon)
    destination: tuple

@app.post("/route")
async def get_route(req: RouteRequest):
    orig_node = ox.distance.nearest_nodes(G, X=req.origin[1], Y=req.origin[0])
    dest_node = ox.distance.nearest_nodes(G, X=req.destination[1], Y=req.destination[0])
    route = nx.shortest_path(G, orig_node, dest_node, weight='length')
    coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]
    return {"route": coords}
