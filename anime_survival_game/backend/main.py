import os
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Add the current directory to sys.path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser import parse_readme_characters
from agent import SurvivalAgent

# Global state
CHARACTERS = []
AGENT = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global CHARACTERS, AGENT

    # Load characters from README.md
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    parent_dir = os.path.dirname(base_dir)

    readme_paths = [
        os.path.join(base_dir, "README.md"),
        os.path.join(parent_dir, "README.md"),
        "README.md"
    ]

    loaded = False
    for path in readme_paths:
        if os.path.exists(path):
            CHARACTERS = parse_readme_characters(path)
            if CHARACTERS:
                print(f"Loaded {len(CHARACTERS)} characters from {path}")
                loaded = True
                break

    if not loaded:
        print("Warning: Could not load characters from README.md")

    AGENT = SurvivalAgent(CHARACTERS)
    yield
    # Cleanup code here if needed

app = FastAPI(title="Anime Survival Game API", lifespan=lifespan)

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SurvivalScenario(BaseModel):
    scenario: str

@app.get("/api/characters")
def get_characters():
    return {"characters": CHARACTERS}

@app.post("/api/survive")
def simulate_survival(request: SurvivalScenario):
    if not AGENT:
        raise HTTPException(status_code=500, detail="SurvivalAgent not initialized")

    result = AGENT.simulate_survival(request.scenario)
    return result

# Serve static frontend files
frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "frontend")

if os.path.exists(frontend_dir):
    app.mount("/static", StaticFiles(directory=frontend_dir), name="static")

    @app.get("/")
    def read_index():
        index_path = os.path.join(frontend_dir, "index.html")
        if os.path.exists(index_path):
            return FileResponse(index_path)
        return {"message": "Frontend index.html not found"}

if __name__ == "__main__":
    import uvicorn
    # Use port 8008 to avoid conflicts
    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True)
