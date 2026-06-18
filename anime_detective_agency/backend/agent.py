import random
import time

class DetectiveAgent:
    def __init__(self, characters):
        self.characters = characters

    def _score_for_role(self, character, role):
        # A simple keyword-based heuristic to assign roles
        score = 0
        desc = (character["archetype"] + " " + character["core_emotion"] + " " +
                character["personality_profile"] + " " + character["unique_quality"]).lower()

        if role == "Lead Detective":
            keywords = ["intelligent", "calm", "wisdom", "leader", "strategic", "pragmatic", "mentor"]
        elif role == "Forensics/Analyst":
            keywords = ["logic", "calculating", "smart", "analytical", "adaptability", "observation", "knowledge"]
        elif role == "Interrogator/Enforcer":
            keywords = ["combat", "intense", "intimidating", "power", "loud", "gritty", "aggressive"]
        else:
            keywords = []

        for kw in keywords:
            if kw in desc:
                score += 1

        # Add some randomness
        score += random.random()
        return score

    def assemble_team(self, mystery_description):
        roles = ["Lead Detective", "Forensics/Analyst", "Interrogator/Enforcer"]
        team = []
        available_chars = self.characters.copy()

        for role in roles:
            # Sort available characters based on score for this role
            available_chars.sort(key=lambda c: self._score_for_role(c, role), reverse=True)
            selected = available_chars.pop(0)
            team.append({"role": role, "character": selected})

        return team

    def investigate(self, mystery_description):
        team = self.assemble_team(mystery_description)

        # Generate simulation log
        logs = []

        # Initial Assessment
        lead = team[0]["character"]
        logs.append({
            "character": lead,
            "action": "Briefing",
            "message": f"Alright team, we have a new case: '{mystery_description}'. My {lead['unique_quality']} will guide us. Let's get to work."
        })

        # Forensics
        forensics = team[1]["character"]
        logs.append({
            "character": forensics,
            "action": "Analyzing Evidence",
            "message": f"Looking at the clues... Given my {forensics['personality_profile']}, I can deduce some hidden patterns here."
        })

        # Interrogation
        enforcer = team[2]["character"]
        logs.append({
            "character": enforcer,
            "action": "Questioning Suspects",
            "message": f"I'll handle the suspects! My {enforcer['core_emotion']} will make sure they spill everything they know!"
        })

        # Conclusion
        logs.append({
            "character": lead,
            "action": "Case Closed",
            "message": f"Based on the evidence and confessions, we've solved it. Another mystery unraveled by the Anime Detective Agency."
        })

        return {
            "team": team,
            "logs": logs
        }
