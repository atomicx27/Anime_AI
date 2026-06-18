from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os

# Add the current directory to sys.path so we can import modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser import parse_readme_characters
from agent import AnimeAgent



# Load characters once on startup
CHARACTERS = []
AGENTS = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global CHARACTERS, AGENTS
    # Look for README.md in the parent directory
    readme_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "README.md")
    CHARACTERS = parse_readme_characters(readme_path)
    print(f"Loaded {len(CHARACTERS)} characters.")

    # Initialize agents
    for char in CHARACTERS:
        name = char["name"]
        AGENTS[name] = AnimeAgent(char)

    yield

app = FastAPI(lifespan=lifespan, title="Anime Agents API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    agent_name: str
    message: str

@app.get("/api/agents")
def get_agents():
    return {"agents": CHARACTERS}

@app.post("/api/chat")
def chat(request: ChatRequest):
    if request.agent_name not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent = AGENTS[request.agent_name]
    response = agent.chat(request.message)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
