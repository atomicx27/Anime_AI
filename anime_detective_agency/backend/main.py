from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from parser import parse_readme_characters
from agent import DetectiveAgencyAgent

app = FastAPI(title="Anime Detective Agency API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InvestigationRequest(BaseModel):
    mystery: str

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/investigate")
async def investigate_mystery(request: InvestigationRequest):
    try:
        characters = parse_readme_characters()
        if not characters:
            raise HTTPException(status_code=500, detail="Failed to load characters from README.md")

        agent = DetectiveAgencyAgent(characters)
        result = agent.investigate(request.mystery)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8007)
