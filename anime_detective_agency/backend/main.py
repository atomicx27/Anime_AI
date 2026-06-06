from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
from parser import parse_readme_characters
from agent import DetectiveAgencyAgent

# Global state for characters
app_state = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Load characters
    characters = parse_readme_characters()
    if not characters:
        print("Warning: Failed to load characters from README.md")
    app_state["characters"] = characters
    app_state["agent"] = DetectiveAgencyAgent(characters)
    yield
    # Shutdown: Clean up if necessary
    app_state.clear()

app = FastAPI(title="Anime Detective Agency API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MysteryRequest(BaseModel):
    description: str

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "characters_loaded": len(app_state.get("characters", []))}

@app.post("/api/investigate")
async def investigate(request: MysteryRequest):
    try:
        agent = app_state.get("agent")
        if not agent:
            raise HTTPException(status_code=500, detail="Agent not initialized")

        result = agent.investigate_mystery(request.description)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)
