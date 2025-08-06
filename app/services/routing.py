# app/routing.py

import osmnx as ox
import networkx as nx
from typing import Tuple, List
from app.exceptions import RoutingError
import numpy as np

def build_graph_around(origin: tuple[float, float], destination: tuple[float, float], padding_km: float = 1.0) -> nx.MultiDiGraph:
    """
    Construit un graphe couvrant l’origine et la destination, avec un léger padding.

    Args:
        origin (tuple): Coordonnées (lat, lon) de départ.
        destination (tuple): Coordonnées (lat, lon) d’arrivée.
        padding_km (float): Marge ajoutée en km autour de la zone couverte.

    Returns:
        MultiDiGraph: Graphe routier orienté.
    """
    latitudes = [origin[0], destination[0]]
    longitudes = [origin[1], destination[1]]

    # Calcul de la bounding box avec padding
    north = max(latitudes) + padding_km / 111
    south = min(latitudes) - padding_km / 111
    mean_lat = np.mean(latitudes)
    km_per_deg_lon = 111 * np.cos(np.radians(mean_lat))
    east = max(longitudes) + padding_km / km_per_deg_lon
    west = min(longitudes) - padding_km / km_per_deg_lon

    return ox.graph_from_bbox((north, south, east, west), network_type="bike")


def compute_route(
    G: nx.MultiDiGraph,
    origin: Tuple[float, float],
    destination: Tuple[float, float]
) -> List[Tuple[float, float]]:
    """
    Calcule un itinéraire entre deux points à partir d'un graphe.

    Args:
        G: Le graphe OSM centré autour du point de départ.
        origin (tuple): Coordonnées (lat, lon) du point de départ.
        destination (tuple): Coordonnées (lat, lon) du point d’arrivée.

    Returns:
        List[List[float]]: Liste de coordonnées de l’itinéraire.

    Raises:
        RoutingError: Si aucun itinéraire n'a pu être trouvé.
    """
    try:
        orig_node = ox.distance.nearest_nodes(G, X=origin[1], Y=origin[0])
        dest_node = ox.distance.nearest_nodes(G, X=destination[1], Y=destination[0])
        route_nodes = nx.shortest_path(G, orig_node, dest_node, weight="length")
        route = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route_nodes]
        return route
        if not route:
            raise RoutingError("Itinéraire introuvable entre ces deux points.")
        return route
    except Exception as e:
        raise RoutingError(str(e))

# Note: The RoutingError is raised if the route cannot be computed, ensuring that the API can handle errors gracefully.
# This allows the API to return a meaningful error message to the client.