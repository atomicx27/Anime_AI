from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
from parser import parse_readme_characters
from agent import AnimePowerScalerAgent
import os

# Global agent instance
scaler_agent = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global scaler_agent
    characters = parse_readme_characters()
    if not characters:
        print("Warning: No characters loaded.")
    scaler_agent = AnimePowerScalerAgent(characters)
    yield
    # Clean up if needed

app = FastAPI(title="Anime Power Scaler API", lifespan=lifespan)

# Setup CORS to allow the frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScaleRequest(BaseModel):
    ability_description: str

@app.post("/scale")
async def scale_ability(request: ScaleRequest):
    if not scaler_agent:
        raise HTTPException(status_code=500, detail="Agent not initialized")

    results = scaler_agent.scale_ability(request.ability_description)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8006, reload=True)
