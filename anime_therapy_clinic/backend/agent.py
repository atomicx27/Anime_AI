import random

class TherapyAgent:
    def __init__(self, characters):
        self.characters = characters

    def _score_for_role(self, character, role):
        score = 0
        desc = (character["archetype"] + " " + character["core_emotion"] + " " +
                character["personality_profile"] + " " + character["unique_quality"]).lower()

        if role == "Empathetic Listener":
            keywords = ["empathy", "love", "comfort", "peaceful", "compassion", "understanding", "support"]
        elif role == "Tough Love Coach":
            keywords = ["defiance", "ambition", "pride", "effort", "rival", "determination", "gritty"]
        elif role == "Philosophical Guide":
            keywords = ["wisdom", "mentor", "logic", "philosophy", "truth", "justice", "calm"]
        else:
            keywords = []

        for kw in keywords:
            if kw in desc:
                score += 1

        # Add a bit of randomness to avoid always picking the exact same characters
        score += random.random()
        return score

    def conduct_session(self, problem_description):
        roles = ["Empathetic Listener", "Tough Love Coach", "Philosophical Guide"]
        team = []
        available_chars = self.characters.copy()

        for role in roles:
            # Sort available characters based on score for this role
            available_chars.sort(key=lambda c: self._score_for_role(c, role), reverse=True)
            selected = available_chars.pop(0)
            team.append({"role": role, "character": selected})

        # Generate simulation log
        logs = []

        # Empathetic Listener
        listener = team[0]["character"]
        logs.append({
            "character": listener,
            "role": "Empathetic Listener",
            "message": f"I hear you. My {listener['core_emotion']} tells me you're carrying a heavy burden. It's okay to feel this way. With my {listener['unique_quality']}, I want to help you find comfort and a path forward."
        })

        # Tough Love Coach
        coach = team[1]["character"]
        logs.append({
            "character": coach,
            "role": "Tough Love Coach",
            "message": f"Listen up! You can't let this hold you back. Given my {coach['personality_profile']}, I know what it means to struggle. Use this as fuel! Rely on your own strength, just like I use my {coach['unique_quality']} to break limits!"
        })

        # Philosophical Guide
        guide = team[2]["character"]
        logs.append({
            "character": guide,
            "role": "Philosophical Guide",
            "message": f"Consider the bigger picture. Your situation reflects a deeper struggle. My perspective, rooted in {guide['unique_quality']}, suggests that this pain is merely a lesson. Acceptance and wisdom will guide you."
        })

        return {
            "team": team,
            "advice": logs
        }
