import os
import sys
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser import parse_readme_characters
from agent import DetectiveAgent

CHARACTERS = []
AGENT = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global CHARACTERS, AGENT
    CHARACTERS = parse_readme_characters()
    if CHARACTERS:
        print(f"Loaded {len(CHARACTERS)} characters.")
        AGENT = DetectiveAgent(CHARACTERS)
    else:
        print("Warning: Could not load characters from README.md")
    yield

app = FastAPI(title="Anime Detective Agency API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MysteryRequest(BaseModel):
    mystery: str

@app.get("/api/characters")
def get_characters():
    return {"characters": CHARACTERS}

@app.post("/api/investigate")
def investigate(request: MysteryRequest):
    if not AGENT:
        raise HTTPException(status_code=500, detail="Agent not initialized")
    if not request.mystery.strip():
        raise HTTPException(status_code=400, detail="Mystery cannot be empty")

    result = AGENT.investigate(request.mystery)
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
    uvicorn.run(app, host="0.0.0.0", port=8007)
