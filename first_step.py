import osmnx as ox
import networkx as nx
import folium

# 1. Définir la zone d'étude
place_name = "Grenoble, France"
print("Téléchargement de la carte...")
G = ox.graph_from_place(place_name, network_type='bike')

# 2. Convertir le graphe pour simplifier les calculs
G = ox.convert.to_undirected(G)

# 3. Trouver les noeuds les plus proches de deux points
origin_point = (45.1885, 5.7245)  # centre de Grenoble
destination_point = (45.1648, 5.7126)  # sud de Grenoble

orig_node = ox.distance.nearest_nodes(G, X=origin_point[1], Y=origin_point[0])
dest_node = ox.distance.nearest_nodes(G, X=destination_point[1], Y=destination_point[0])

# 4. Calculer l'itinéraire le plus court (en distance)
print("Calcul de l'itinéraire...")
route = nx.shortest_path(G, orig_node, dest_node, weight='length')

# 5. Visualiser sur une carte
# Obtenir les coordonnées (lat, lon) des noeuds de l'itinéraire
route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

# Centrer la carte sur le point de départ
route_map = folium.Map(location=origin_point, zoom_start=13)

# Ajouter le tracé
folium.PolyLine(route_coords, color='blue', weight=4).add_to(route_map)

# Ajouter les marqueurs de départ et d'arrivée
folium.Marker(location=origin_point, popup="Départ").add_to(route_map)
folium.Marker(location=destination_point, popup="Arrivée").add_to(route_map)

# Enregistrer
route_map.save("itineraire_grenoble.html")
print("Carte enregistrée sous 'itineraire_grenoble.html'")

# 6. Sauvegarder la carte
route_map.save("itineraire_grenoble.html")
print("Carte enregistrée sous 'itineraire_grenoble.html'")
