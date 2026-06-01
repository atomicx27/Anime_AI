import random

class TeamBuilderAgent:
    def __init__(self, characters):
        self.characters = characters

    def _evaluate_character(self, character, mission):
        """Mock evaluation of a character for a given mission."""
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()
        mission_lower = mission.lower()

        score = 0
        assigned_role = "Support"

        # Define keyword mappings to roles and scores
        role_keywords = {
            "Combat Specialist": ["fight", "combat", "battle", "strength", "power", "protect", "defeat", "enemy", "war"],
            "Diplomat / Negotiator": ["peace", "diplomacy", "empathy", "talk", "calm", "understanding", "negotiate", "persuade"],
            "Strategist / Tactician": ["logic", "intelligent", "calculating", "acumen", "wisdom", "strategy", "plan", "infiltrate", "stealth"],
            "Wildcard": ["chaos", "despair", "nihilism", "pain", "trauma", "unpredictable", "magic", "limitless"]
        }

        role_scores = {}

        for role, words in role_keywords.items():
            role_score = 0
            if any(w in mission_lower for w in words):
                # If mission needs this role, check if character has traits for it
                for word in words:
                    if word in core_emotion or word in personality or word in quality:
                        role_score += 15
                        score += 15
            role_scores[role] = role_score

        best_role = "Support"
        best_role_score = 0

        # Determine the primary role definitively
        for role, r_score in role_scores.items():
            if r_score > best_role_score:
                best_role_score = r_score
                best_role = role

        if best_role_score > 0:
            assigned_role = best_role

        # Add some randomness
        score += random.randint(-5, 15)

        reasoning = f"{character['name']} was selected as the {assigned_role}. Their unique trait ('{character['unique_quality'].split('.')[0]}') aligns well with the mission requirements."

        return {
            "name": character["name"],
            "archetype": character["archetype"],
            "role": assigned_role,
            "score": score,
            "reasoning": reasoning
        }

    def build_team(self, mission, team_size=3):
        """Evaluates characters and selects the best team for the mission."""
        logs = []
        logs.append(f"Agent Commander initializing team selection for mission: '{mission}'")
        logs.append(f"Analyzing {len(self.characters)} available operatives...")

        evaluations = []
        for char in self.characters:
            evaluations.append(self._evaluate_character(char, mission))

        # Sort by score descending
        evaluations.sort(key=lambda x: x["score"], reverse=True)

        selected_team = evaluations[:team_size]

        roles_filled = [member["role"] for member in selected_team]
        logs.append(f"Team selected. Roles filled: {', '.join(roles_filled)}")

        # Calculate Synergy
        wildcard_count = roles_filled.count("Wildcard")
        if wildcard_count >= 2:
            logs.append("Synergy Warning: Too many Wildcards. Deducting 15 points from team cohesion.")
            for member in selected_team:
                member["score"] -= 15

        if "Combat Specialist" in roles_filled and "Diplomat / Negotiator" in roles_filled and "Strategist / Tactician" in roles_filled:
            logs.append("Synergy Bonus: Perfect role balance achieved. Adding 15 points to team aptitude.")
            for member in selected_team:
                member["score"] += 15

        return {
            "mission": mission,
            "team": selected_team,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = TeamBuilderAgent(chars)
    res = agent.build_team("Infiltrate the enemy base and negotiate a peace treaty without starting a fight")
    print(f"Results for: {res['mission']}")
    for member in res['team']:
        print(f"[{member['role']}] {member['name']} (Score: {member['score']}) - {member['reasoning']}")
