from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser import parse_readme_characters
from agent import ScenarioRankerAgent

@asynccontextmanager
async def lifespan(app: FastAPI):
    global CHARACTERS, AGENT
    CHARACTERS = parse_readme_characters()
    if CHARACTERS:
        print(f"Loaded {len(CHARACTERS)} characters.")
        AGENT = ScenarioRankerAgent(CHARACTERS)
    else:
        print("Warning: Could not load characters from README.md")

    yield

app = FastAPI(lifespan=lifespan, title="Anime Scenario Ranker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CHARACTERS = []
AGENT = None


class RankRequest(BaseModel):
    scenario: str

@app.get("/api/characters")
def get_characters():
    return {"characters": CHARACTERS}

@app.post("/api/rank")
def rank_scenario(request: RankRequest):
    if not AGENT:
        raise HTTPException(status_code=500, detail="Agent not initialized")

    result = AGENT.rank_scenario(request.scenario)
    return result

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
    uvicorn.run(app, host="0.0.0.0", port=8002)
