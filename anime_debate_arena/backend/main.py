from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser import parse_readme_characters
from agent import DebateArenaAgent

# Global state
app_state = {
    "characters": [],
    "agent": None
}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app_state["characters"] = parse_readme_characters()
    if app_state["characters"]:
        print(f"Loaded {len(app_state['characters'])} characters.")
        app_state["agent"] = DebateArenaAgent(app_state["characters"])
    else:
        print("Warning: Could not load characters from README.md")

    yield
    # Shutdown (nothing specific to do)
    print("Shutting down Debate Arena API")


app = FastAPI(title="Anime Debate Arena API", lifespan=lifespan)
from agent import DebateAgent

@asynccontextmanager
async def lifespan(app: FastAPI):

    global CHARACTERS, AGENT
    CHARACTERS = parse_readme_characters()
    if CHARACTERS:
        print(f"Loaded {len(CHARACTERS)} characters.")
        AGENT = DebateAgent(CHARACTERS)
    else:
        print("Warning: Could not load characters from README.md")
    yield

app = FastAPI(title="Anime Debate Arena API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

@app.get("/api/characters")
def get_characters():
    return {"characters": app_state["characters"]}

@app.post("/api/debate")
def simulate_debate(request: TopicRequest):
    if not app_state["agent"]:
        raise HTTPException(status_code=500, detail="Agent not initialized")

    result = app_state["agent"].simulate_debate(request.topic)
    return result

# Serve frontend
CHARACTERS = []
AGENT = None

class DebateRequest(BaseModel):
    topic: str

@app.post("/api/debate")
def host_debate(request: DebateRequest):
    if not AGENT:
        raise HTTPException(status_code=500, detail="Agent not initialized")

    result = AGENT.host_debate(request.topic)
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
    uvicorn.run(app, host="0.0.0.0", port=8006)
    uvicorn.run(app, host="0.0.0.0", port=8005)
