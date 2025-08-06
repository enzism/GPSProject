from fastapi import APIRouter, HTTPException
from app.models.models import RouteRequest  # tu l'avais ici
from app.services.routing import build_graph_around, compute_route
from app.exceptions import RoutingError
import traceback

router = APIRouter()

@router.post("/route")
async def get_route(req: RouteRequest) -> dict:
    """
    Calcule un itinéraire cyclable entre deux points géographiques.

    Args:
        req (RouteRequest): Coordonnées de départ et d’arrivée

    Returns:
        dict: Dictionnaire avec une clé 'route' contenant la liste des points
    """
    try:
        graph = build_graph_around(req.origin, req.destination)
        route_coords = compute_route(graph, req.origin, req.destination)
        return {"route": route_coords}
    
    except RoutingError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
    except Exception as e:
        # Imprime l’erreur dans le terminal
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
