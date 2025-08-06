// Initialise la carte avec un centre par défaut (Marseille par exemple)
const map = L.map('map').setView([43.2965, 5.3698], 13);

// Ajoute les tuiles de fond OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(map);

// --- Barre de recherche (géocodeur) ---
L.Control.geocoder({
  defaultMarkGeocode: false
})
  .on('markgeocode', function (e) {
    const bbox = e.geocode.bbox;
    const bounds = L.latLngBounds(bbox);
    map.fitBounds(bounds); // Centre la carte sur le résultat
  })
  .addTo(map);

// --- Interaction avec la carte ---
let markers = [];
let routeLine = null;

// Clic sur la carte → ajout d’un point
map.on('click', async (e) => {
  // Limite à 2 points max pour l'instant
  if (markers.length >= 2) {
    markers.forEach(m => map.removeLayer(m));
    if (routeLine) map.removeLayer(routeLine);
    markers = [];
  }

  const marker = L.marker(e.latlng).addTo(map);
  markers.push(marker);

  if (markers.length === 2) {
    const origin = [markers[0].getLatLng().lat, markers[0].getLatLng().lng];
    const destination = [markers[1].getLatLng().lat, markers[1].getLatLng().lng];

    try {
      const response = await fetch('http://localhost:8000/route', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ origin, destination }),
      });

      const data = await response.json();

      if (data.route) {
        routeLine = L.polyline(data.route, { color: 'blue', weight: 4 }).addTo(map);
        map.fitBounds(routeLine.getBounds());
      } else {
        alert("Erreur : " + data.error);
      }

    } catch (err) {
      alert("Échec de la requête : " + err);
    }
  }
});
