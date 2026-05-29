import os
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from rich.console import Console
from rich.table import Table

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser import parse_readme_characters
from agent import PowerScalerAgent

CHARACTERS = []
AGENT = None
console = Console()

@asynccontextmanager
async def lifespan(app: FastAPI):
    global CHARACTERS, AGENT
    CHARACTERS = parse_readme_characters()
    if CHARACTERS:
        table = Table(title="Loaded Anime Characters for Power Scaling")
        table.add_column("Name", style="cyan")
        table.add_column("Archetype", style="magenta")
        table.add_column("Core Emotion", style="green")
        for char in CHARACTERS:
            table.add_row(char["name"], char["archetype"], char["core_emotion"])
        console.print(table)
        AGENT = PowerScalerAgent(CHARACTERS)
    else:
        console.print("[red]Warning: Could not load characters from README.md[/red]")
    yield
    # Cleanup if needed

app = FastAPI(title="Anime Power Scaler API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScaleRequest(BaseModel):
    opponent: str

@app.post("/api/scale")
def scale(request: ScaleRequest):
    if not AGENT:
        raise HTTPException(status_code=500, detail="Agent not initialized")

    results = AGENT.evaluate_opponent(request.opponent)
    return {"opponent": request.opponent, "results": results}

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
    uvicorn.run(app, host="0.0.0.0", port=8006)
