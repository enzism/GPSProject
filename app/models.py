# app/models.py

from pydantic import BaseModel
from typing import Tuple

class RouteRequest(BaseModel):
    origin: Tuple[float, float]       # (lat, lon)
    destination: Tuple[float, float]
