from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path
from app.api.endpoints import router as api_router  # nouvelle route

# --- Initialisation de l'application ---

# BASE_DIR = dossier racine du projet (en remontant 2 fois depuis ce fichier main.py)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC_DIR = chemin complet vers le dossier "static" qui contient index.html, js, css, etc.
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Création de l'app FastAPI
app = FastAPI(title="Itinéraire Cyclable API", version="1.0")

# Montage des fichiers statiques sous la route "/static"
# Tous les fichiers statiques sont accessibles via http://localhost:8000/static/...
app.mount("/static", StaticFiles(directory=STATIC_DIR, html=True), name="static")

# Middleware CORS (autorise tout pour dev, à restreindre en production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En prod, mettre la liste de tes domaines front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route pour servir index.html à la racine "/"
@app.get("/")
async def serve_index():
    # renvoie le fichier index.html en réponse
    return FileResponse(Path(STATIC_DIR) / "index.html")

# Enregistrement des routes de l'API (ex : /route, /autres)
app.include_router(api_router)
