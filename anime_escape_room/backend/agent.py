import random

class EscapeRoomAgent:
    def __init__(self, characters):
        self.characters = characters
        self.roles = ["Leader / Strategist", "Puzzle Solver / Decoder", "Physical Breaker / Enforcer", "Support / Scout"]

    def _assign_roles(self):
        # Randomly pick 4 distinct characters for the team
        if len(self.characters) < 4:
            team = self.characters
        else:
            team = random.sample(self.characters, 4)

        assignments = []
        available_roles = list(self.roles)

        # Sort characters to try and assign roles based on traits somewhat (simplified here)
        for char in team:
            role = ""
            if "INTJ" in char["archetype"] or "Strategist" in char.get("personality", ""):
                if "Leader / Strategist" in available_roles:
                    role = "Leader / Strategist"
            if not role and ("Logic" in char["core_emotion"] or "Intelligence" in char.get("unique_quality", "")):
                if "Puzzle Solver / Decoder" in available_roles:
                    role = "Puzzle Solver / Decoder"
            if not role and ("Combat" in char["core_emotion"] or "Physical" in char.get("unique_quality", "")):
                if "Physical Breaker / Enforcer" in available_roles:
                    role = "Physical Breaker / Enforcer"

            if not role:
                role = available_roles[0] # Pick the first available

            if role in available_roles:
                available_roles.remove(role)

            assignments.append({
                "character": char,
                "role": role,
                "action": f"Using '{char['unique_quality']}' to fulfill their role as {role}."
            })

        return assignments

    def simulate_escape(self, scenario: str):
        team_assignments = self._assign_roles()

        narrative = [
            f"The team finds themselves trapped in: {scenario}",
            "--- Escape Attempt Begins ---"
        ]

        success_score = 0

        for member in team_assignments:
            char = member["character"]
            role = member["role"]

            # Simple heuristic for success based on traits matching role (for flavor)
            action_success = random.choice([True, True, False]) # 66% chance of success per action

            if action_success:
                success_score += 1
                narrative.append(f"[{role}] {char['name']} successfully utilized their '{char['core_emotion']}'. {member['action']}")
            else:
                narrative.append(f"[{role}] {char['name']} struggled, their '{char['personality']}' clashing with the puzzle.")

        narrative.append("--- Final Outcome ---")
        if success_score >= 3:
            outcome = "SUCCESS - The team managed to escape!"
        elif success_score == 2:
            outcome = "NARROW ESCAPE - The team barely made it out in time!"
        else:
            outcome = "FAILURE - The team remains trapped..."

        narrative.append(outcome)

        return {
            "scenario": scenario,
            "team": team_assignments,
            "narrative": narrative,
            "outcome": outcome
        }
