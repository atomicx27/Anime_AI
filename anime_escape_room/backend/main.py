from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import re
import os
import random
from contextlib import asynccontextmanager

app_data = {}

def load_characters():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    readme_path = os.path.join(base_dir, 'README.md')

    characters = []
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()

        table_match = re.search(r'\| Character \| Archetype & MBTI \| Core Emotion \| Personality Profile \| Unique Quality & Philosophy \|\n\|---\|---\|---\|---\|---\|\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
        if table_match:
            table_content = table_match.group(1)
            for line in table_content.strip().split('\n'):
                cols = [col.strip() for col in line.split('|')[1:-1]]
                if len(cols) == 5:
                    characters.append({
                        'name': cols[0],
                        'archetype': cols[1],
                        'core_emotion': cols[2],
                        'personality': cols[3],
                        'unique_quality': cols[4]
                    })
    except Exception as e:
        print(f"Error loading characters: {e}")
    return characters

@asynccontextmanager
async def lifespan(app: FastAPI):
    app_data["characters"] = load_characters()
    yield
    app_data.clear()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScenarioRequest(BaseModel):
    scenario: str

class EscapeAction(BaseModel):
    role: str
    character_name: str
    action: str

class EscapeResponse(BaseModel):
    scenario: str
    actions: List[EscapeAction]

roles = ["The Leader", "The Puzzle Solver", "The Muscle", "The Wildcard"]

@app.post("/api/escape", response_model=EscapeResponse)
async def escape_room(request: ScenarioRequest):
    characters = app_data.get("characters", [])
    if not characters:
        raise HTTPException(status_code=500, detail="Characters not loaded")

    if len(characters) < 4:
        raise HTTPException(status_code=500, detail="Not enough characters in the database")

    selected_chars = random.sample(characters, 4)
    actions = []

    for i, role in enumerate(roles):
        char = selected_chars[i]

        if role == "The Leader":
            action_desc = f"Takes charge by leveraging '{char['core_emotion']}'. They motivate the team, observing the room based on '{char['unique_quality']}'."
        elif role == "The Puzzle Solver":
            action_desc = f"Approaches the puzzle with their {char['archetype']} mindset. Using their '{char['personality']}', they crack the code."
        elif role == "The Muscle":
            action_desc = f"Relies on '{char['unique_quality']}' to physically manipulate or break obstacles, reacting with '{char['core_emotion']}'."
        else: # The Wildcard
            action_desc = f"Does something unexpected driven by '{char['personality']}', which accidentally opens a secret passage aligned with '{char['unique_quality']}'."

        actions.append(EscapeAction(
            role=role,
            character_name=char['name'],
            action=action_desc
        ))

    return EscapeResponse(
        scenario=request.scenario,
        actions=actions
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8009)
