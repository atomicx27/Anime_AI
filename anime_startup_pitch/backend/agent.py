import random

class StartupPitchAgent:
    def __init__(self, characters):
        self.characters = characters

    def _select_investors(self, count=4):
        return random.sample(self.characters, min(count, len(self.characters)))

    def _evaluate_pitch(self, pitch: str, character: dict):
        core_emotion = character['core_emotion'].lower()
        personality = character['personality_profile'].lower()
        philosophy = character['unique_quality'].lower()
        pitch_lower = pitch.lower()

        # Simple heuristic to determine "Invest" or "Pass"
        invest_score = 0
        if "ai" in pitch_lower or "tech" in pitch_lower or "magic" in pitch_lower:
            invest_score += 1

        if "power" in pitch_lower and "power" in philosophy:
            invest_score += 2

        if "peace" in pitch_lower and "peace" in philosophy:
            invest_score += 2

        if "combat" in pitch_lower and "combat" in core_emotion:
            invest_score += 2

        if "protect" in pitch_lower and "protect" in personality:
            invest_score += 2

        # Add some randomness to make it fun
        invest_score += random.randint(-1, 2)

        decision = "Invest" if invest_score >= 1 else "Pass"

        # Generate feedback based on character traits
        feedback = f"Based on my core of {character['core_emotion']}, "
        if decision == "Invest":
            feedback += f"I see potential here. {character['unique_quality']} tells me this aligns with my goals. Let's make it happen."
        else:
            feedback += f"I don't see the value. {character['unique_quality']} is what matters, and this doesn't have it."

        return {
            "name": character["name"],
            "archetype": character["archetype"],
            "decision": decision,
            "feedback": feedback
        }

    def pitch(self, pitch_text: str):
        investors = self._select_investors()
        results = []
        for inv in investors:
            results.append(self._evaluate_pitch(pitch_text, inv))

        total_invests = sum(1 for r in results if r["decision"] == "Invest")
        overall = "Funded!" if total_invests >= len(results) / 2 else "Rejected"

        return {
            "pitch": pitch_text,
            "overall_decision": overall,
            "investor_feedback": results
        }
