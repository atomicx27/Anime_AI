import random

class SurvivalAgent:
    def __init__(self, characters):
        self.characters = characters

    def _score_for_role(self, character, role):
        score = 0
        desc = (character["archetype"] + " " + character["core_emotion"] + " " +
                character["personality_profile"] + " " + character["unique_quality"]).lower()

        if role == "Leader":
            keywords = ["leader", "pragmatic", "strategy", "diplomatic", "protagonist", "mentor"]
        elif role == "Scavenger":
            keywords = ["adaptable", "quick", "instinct", "wild", "curious", "energy"]
        elif role == "Defender":
            keywords = ["protect", "combat", "power", "shield", "strong", "loyal", "fierce"]
        elif role == "Medic":
            keywords = ["heal", "empathy", "care", "support", "wisdom", "calm", "peace"]
        else:
            keywords = []

        for kw in keywords:
            if kw in desc:
                score += 1

        # Add a bit of randomness to allow for varied outcomes
        score += random.random()
        return score

    def assemble_squad(self):
        roles = ["Leader", "Scavenger", "Defender", "Medic"]
        team = []
        available_chars = self.characters.copy()

        for role in roles:
            if not available_chars:
                break
            # Sort available characters based on score for this role
            available_chars.sort(key=lambda c: self._score_for_role(c, role), reverse=True)
            selected = available_chars.pop(0)
            team.append({"role": role, "character": selected})

        return team

    def simulate_survival(self, scenario_description):
        team = self.assemble_squad()

        # Helper to easily find a character by role
        def get_char_by_role(role_name):
            for member in team:
                if member["role"] == role_name:
                    return member["character"]
            return None

        leader = get_char_by_role("Leader")
        scavenger = get_char_by_role("Scavenger")
        defender = get_char_by_role("Defender")
        medic = get_char_by_role("Medic")

        logs = []

        # Morning
        if leader:
            logs.append({
                "time": "08:00 AM",
                "character": leader,
                "event": "Morning Briefing",
                "message": f"Listen up! We are facing '{scenario_description}'. My {leader['unique_quality']} will help us coordinate. We need to survive the day."
            })

        # Midday
        if scavenger:
            logs.append({
                "time": "12:00 PM",
                "character": scavenger,
                "event": "Resource Run",
                "message": f"I found some supplies! Given my {scavenger['personality_profile']}, I managed to outrun the dangers out there."
            })

        # Afternoon
        if defender:
            logs.append({
                "time": "16:00 PM",
                "character": defender,
                "event": "Camp Defense",
                "message": f"They tried to ambush us, but my {defender['core_emotion']} gave me the strength to push them back. The perimeter is secure."
            })

        # Evening
        if medic:
            logs.append({
                "time": "20:00 PM",
                "character": medic,
                "event": "Tending Wounds",
                "message": f"Everyone, rest now. Let my {medic['unique_quality']} soothe your injuries and calm our spirits before nightfall."
            })

        # Night
        if leader:
            logs.append({
                "time": "23:59 PM",
                "character": leader,
                "event": "End of Day",
                "message": "We made it through day one. Rest up, tomorrow will be just as hard. Stay strong."
            })

        return {
            "team": team,
            "logs": logs
        }
