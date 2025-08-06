# app/models.py


from typing import List
from pydantic import BaseModel
from typing import Tuple

class RouteRequest(BaseModel):
    origin: Tuple[float, float]       # (lat, lon)
    destination: Tuple[float, float]

class RouteResponse(BaseModel):
    """
    Réponse renvoyée par l'API : une liste de points (lat, lon).
    """
    route: List[List[float]]