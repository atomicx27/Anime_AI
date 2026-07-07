from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from parser import parse_readme_characters
from agent import TherapyAgent

CHARACTERS = []
AGENT = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global CHARACTERS, AGENT

    # Try different paths to README.md
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
                print(f"Loaded {len(CHARACTERS)} characters from {path}.")
                AGENT = TherapyAgent(CHARACTERS)
                loaded = True
                break

    if not loaded:
        print("Warning: Could not load characters from README.md")

    yield

app = FastAPI(title="Anime Therapy Clinic AI API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TherapyRequest(BaseModel):
    problem: str

@app.post("/api/therapy")
def start_therapy_session(request: TherapyRequest):
    if not AGENT:
        raise HTTPException(status_code=500, detail="Agent not initialized")

    result = AGENT.conduct_session(request.problem)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8011, reload=True)
