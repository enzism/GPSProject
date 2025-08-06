# app/routing.py

import osmnx as ox
import networkx as nx
from typing import Tuple, List

def build_graph_around(point: Tuple[float, float], dist: float = 7000):
    """
    Construit un graphe OSMnx centré autour d'un point GPS.

    Args:
        point: Tuple (lat, lon)
        dist: Rayon en mètres

    Returns:
        networkx.MultiDiGraph
    """
    custom_filter = (
        '["highway"]'
        '["area"!~"yes"]'
        '["highway"!~"motorway|motorway_link|trunk|trunk_link|raceway"]'
        '["access"!~"private"]'
    )
    return ox.graph_from_point(point, dist=dist, custom_filter=custom_filter, network_type="bike")


def compute_route(
    G: nx.MultiDiGraph,
    origin: Tuple[float, float],
    destination: Tuple[float, float]
) -> List[Tuple[float, float]]:
    """
    Calcule le plus court chemin entre deux points.

    Args:
        G: Graphe OSMnx
        origin: Coordonnées GPS (lat, lon)
        destination: Coordonnées GPS (lat, lon)

    Returns:
        Liste de points GPS du chemin [(lat1, lon1), (lat2, lon2), ...]
    """
    orig_node = ox.distance.nearest_nodes(G, X=origin[1], Y=origin[0])
    dest_node = ox.distance.nearest_nodes(G, X=destination[1], Y=destination[0])
    route_nodes = nx.shortest_path(G, orig_node, dest_node, weight="length")
    return [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route_nodes]
