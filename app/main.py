# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.models import RouteRequest
from app.routing import build_graph_around, compute_route

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
    
# --- Endpoint de calcul d'itinéraire ---
@app.post("/route")
async def get_route(req: RouteRequest) -> dict:
    """Retourne une liste de coordonnées (lat, lon) représentant l'itinéraire."""
    try:
        graph = build_graph_around(req.origin)
        route_coords = compute_route(graph, req.origin, req.destination)
        return {"route": route_coords}
    except Exception as e:
        return {"error": str(e)}