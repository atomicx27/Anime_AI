from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from parser import parse_readme_characters
from agent import AffinityMatcherAgent




from contextlib import asynccontextmanager

CHARACTERS = []
AGENT = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global CHARACTERS, AGENT
    CHARACTERS = parse_readme_characters()
    if CHARACTERS:
        print(f"Loaded {len(CHARACTERS)} characters.")
        AGENT = AffinityMatcherAgent(CHARACTERS)
    else:
        print("Warning: Could not load characters from README.md")

    yield

app = FastAPI(title="Anime Affinity Matcher API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MatchRequest(BaseModel):
    description: str

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/match")
async def get_matches(request: MatchRequest):
    try:
        characters = parse_readme_characters()
        if not characters:
            raise HTTPException(status_code=500, detail="Failed to load characters from README.md")

        agent = AffinityMatcherAgent(characters)
        result = agent.match_user(request.description)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8006)
