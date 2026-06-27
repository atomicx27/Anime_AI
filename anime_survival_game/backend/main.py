import re
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import uvicorn
import os
from contextlib import asynccontextmanager

class Character(BaseModel):
    name: str
    archetype_mbti: str
    core_emotion: str
    personality_profile: str
    unique_quality_philosophy: str

class SimulationRequest(BaseModel):
    scenario: str

class SimulationResponse(BaseModel):
    character: str
    survival_strategy: str
    survival_status: str
    tier: str

characters_db: List[Character] = []

def parse_readme() -> List[Character]:
    chars = []
    # Walk up to the root directory assuming backend is in root/anime_survival_game/backend
    readme_path = os.path.join(os.path.dirname(__file__), '..', '..', 'README.md')
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Extract the table
            table_match = re.search(r'\| Character .*?\|\n\|--.*?\|\n(.*?)\n\n', content, re.DOTALL)
            if table_match:
                rows = table_match.group(1).strip().split('\n')
                for row in rows:
                    cols = [c.strip() for c in row.split('|') if c.strip()]
                    if len(cols) == 5:
                        chars.append(Character(
                            name=cols[0],
                            archetype_mbti=cols[1],
                            core_emotion=cols[2],
                            personality_profile=cols[3],
                            unique_quality_philosophy=cols[4]
                        ))
    except Exception as e:
        print(f"Error parsing README.md: {e}")
    return chars

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load characters on startup
    global characters_db
    characters_db = parse_readme()
    yield

app = FastAPI(title="Anime Survival Game AI", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/characters", response_model=List[Character])
async def get_characters():
    return characters_db

@app.post("/api/simulate", response_model=List[SimulationResponse])
async def simulate_scenario(request: SimulationRequest):
    if not characters_db:
        raise HTTPException(status_code=500, detail="Character database is empty.")

    scenario = request.scenario.lower()
    responses = []

    for char in characters_db:
        char_lower = char.name.lower()
        core_emotion = char.core_emotion.lower()
        unique_quality = char.unique_quality_philosophy.lower()

        # Simple simulated logic based on traits and scenario
        strategy = f"Relies on {char.core_emotion} and {char.unique_quality_philosophy} to navigate the {request.scenario}."
        status = "Unknown"
        tier = "Unknown"

        if "zombie" in scenario or "combat" in scenario or "fight" in scenario or "monster" in scenario:
            if "combat" in core_emotion or "power" in unique_quality or "protect" in core_emotion or "limitless" in unique_quality or "martial" in unique_quality:
                status = "Survived easily"
                tier = "S-Tier Survivor"
                strategy = f"Uses their incredible combat prowess and {char.unique_quality_philosophy} to obliterate the threat."
            elif "diplomacy" in unique_quality or "talk" in unique_quality or "peace" in core_emotion:
                status = "Struggled but survived"
                tier = "B-Tier Survivor"
                strategy = f"Tried to negotiate, but when that failed, relied on their {char.core_emotion} to scrape by."
            else:
                status = "Perished"
                tier = "F-Tier Survivor"
                strategy = f"Their reliance on {char.unique_quality_philosophy} was ineffective against this physical threat."
        elif "apocalypse" in scenario or "starvation" in scenario or "resource" in scenario:
            if "comfort" in core_emotion or "economic" in unique_quality or "diplomacy" in unique_quality:
                status = "Thrived"
                tier = "S-Tier Survivor"
                strategy = f"Used their {char.unique_quality_philosophy} to establish a thriving settlement."
            elif "protect" in core_emotion or "family" in core_emotion:
                status = "Survived through sacrifice"
                tier = "A-Tier Survivor"
                strategy = f"Pushed themselves to the limit due to their {char.core_emotion} to keep others alive."
            else:
                status = "Survived barely"
                tier = "C-Tier Survivor"
                strategy = f"Struggled with the lack of resources, using sheer {char.core_emotion} to keep going."
        elif "betrayal" in scenario or "deception" in scenario or "game" in scenario:
             if "logic" in core_emotion or "strategic" in unique_quality or "genjutsu" in unique_quality or "manipulative" in unique_quality or "calculating" in unique_quality:
                status = "Masterminded the situation"
                tier = "S-Tier Survivor"
                strategy = f"Saw through the lies using their {char.unique_quality_philosophy} and turned the tables."
             elif "empathy" in core_emotion or "naive" in core_emotion or "innocent" in unique_quality or "trust" in core_emotion:
                status = "Betrayed and Perished"
                tier = "F-Tier Survivor"
                strategy = f"Their {char.core_emotion} made them too trusting, leading to their downfall."
             else:
                status = "Survived with trust issues"
                tier = "B-Tier Survivor"
                strategy = f"Relied on instinct and {char.unique_quality_philosophy} to suspect others and survive."
        else:
             # Default fallback
             if "determination" in core_emotion or "unyielding" in unique_quality or "will" in core_emotion:
                 status = "Survived through sheer grit"
                 tier = "A-Tier Survivor"
             elif "logic" in core_emotion or "strategic" in unique_quality:
                 status = "Survived through smarts"
                 tier = "A-Tier Survivor"
             else:
                 status = "Survived"
                 tier = "B-Tier Survivor"

        responses.append(SimulationResponse(
            character=char.name,
            survival_strategy=strategy,
            survival_status=status,
            tier=tier
        ))

    return responses

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8009, reload=True)
