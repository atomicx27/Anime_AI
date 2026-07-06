import os
import re
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager

# Global store for characters
characters_db = []

def parse_readme():
    """Parses the root README.md to extract character data."""
    readme_path = os.path.join(os.path.dirname(__file__), '..', '..', 'README.md')
    if not os.path.exists(readme_path):
        print(f"Warning: README.md not found at {readme_path}")
        return []

    chars = []
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract table rows
    table_pattern = re.compile(r'\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|')
    matches = table_pattern.findall(content)

    for match in matches:
        # Skip header and separator rows
        col1 = match[0].strip()
        if col1 == 'Character' or col1.startswith('---') or not col1:
            continue

        char_data = {
            'name': col1,
            'archetype': match[1].strip(),
            'core_emotion': match[2].strip(),
            'personality': match[3].strip(),
            'philosophy': match[4].strip()
        }
        chars.append(char_data)

    return chars

@asynccontextmanager
async def lifespan(app: FastAPI):
    global characters_db
    characters_db = parse_readme()
    print(f"Loaded {len(characters_db)} characters from README.md")
    yield
    characters_db.clear()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TherapyRequest(BaseModel):
    problem: str

class TherapyResponse(BaseModel):
    role: str
    character: str
    advice: str
    avatar_url: str

def assign_roles(problem: str):
    """Dynamically assign characters to therapy roles."""
    roles = [
        "Lead Therapist",
        "Empathetic Support",
        "Harsh Truth Realist"
    ]

    assigned = []
    available_chars = list(characters_db)

    # Simplified assignment: pick characters that somewhat match the role archetypes
    # For a real implementation, this would use more complex LLM logic

    # Lead Therapist: look for Mentors or calm/diplomatic
    lead_candidates = [c for c in available_chars if "Mentor" in c['archetype'] or "diplomatic" in c['personality'].lower() or "wise" in c['personality'].lower()]
    lead = lead_candidates[0] if lead_candidates else (available_chars[0] if available_chars else None)
    if lead and lead in available_chars: available_chars.remove(lead)

    # Empathetic Support: look for empathy/protect/love
    empathy_candidates = [c for c in available_chars if "Empathy" in c['core_emotion'] or "Love" in c['core_emotion'] or "protect" in c['philosophy'].lower()]
    empathy = empathy_candidates[0] if empathy_candidates else (available_chars[0] if available_chars else None)
    if empathy and empathy in available_chars: available_chars.remove(empathy)

    # Harsh Truth: look for logic/cynical/abrasive
    harsh_candidates = [c for c in available_chars if "Logic" in c['core_emotion'] or "cynical" in c['personality'].lower() or "abrasive" in c['personality'].lower()]
    harsh = harsh_candidates[0] if harsh_candidates else (available_chars[0] if available_chars else None)
    if harsh and harsh in available_chars: available_chars.remove(harsh)

    if lead: assigned.append((roles[0], lead))
    if empathy: assigned.append((roles[1], empathy))
    if harsh: assigned.append((roles[2], harsh))

    return assigned

def generate_advice(role: str, character: dict, problem: str):
    """Generate simulated advice based on character traits."""
    name = character['name']
    philosophy = character['philosophy']
    emotion = character['core_emotion']

    if role == "Lead Therapist":
        return f"As your Lead Therapist, I've analyzed your situation: '{problem}'. Based on my philosophy ('{philosophy}'), we must approach this methodically. Let's focus on understanding the root cause."
    elif role == "Empathetic Support":
        return f"Oh no, I'm so sorry you're going through: '{problem}'. My core emotion is {emotion}, and I want you to know you're not alone. We will get through this together, drawing strength from our bonds."
    elif role == "Harsh Truth Realist":
        return f"Listen up. Your problem ('{problem}') is just an obstacle. Driven by {emotion}, I say you need to stop complaining and face reality. '{philosophy}' - apply that to your life and get stronger."

    return "I don't know what to say."

@app.post("/api/therapy_session", response_model=list[TherapyResponse])
async def get_therapy_session(request: TherapyRequest):
    if not characters_db:
        return []

    assigned_roles = assign_roles(request.problem)

    responses = []
    for role, char in assigned_roles:
        advice = generate_advice(role, char, request.problem)
        # Dummy avatar URL generation (e.g., UI avatars)
        avatar_name = char['name'].split()[0].lower()
        avatar_url = f"https://ui-avatars.com/api/?name={avatar_name}&background=random&color=fff"

        responses.append(TherapyResponse(
            role=role,
            character=char['name'],
            advice=advice,
            avatar_url=avatar_url
        ))

    return responses

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8011)
