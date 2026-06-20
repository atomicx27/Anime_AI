from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
from parser import parse_readme_characters
from agent import StartupPitchAgent

characters_db = []

@asynccontextmanager
async def lifespan(app: FastAPI):
    global characters_db
    characters_db = parse_readme_characters()
    print(f"Loaded {len(characters_db)} characters on startup.")
    yield
    characters_db.clear()

app = FastAPI(title="Anime Startup Pitch API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PitchRequest(BaseModel):
    pitch: str

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "characters_loaded": len(characters_db)}

@app.post("/api/pitch")
async def evaluate_pitch(request: PitchRequest):
    try:
        if not characters_db:
            raise HTTPException(status_code=500, detail="Character database not loaded.")

        agent = StartupPitchAgent(characters_db)
        result = agent.evaluate_pitch(request.pitch)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8009, reload=True)
