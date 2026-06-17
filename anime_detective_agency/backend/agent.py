import random

class DetectiveAgent:
    def __init__(self, characters):
        self.characters = characters

    def _select_lead_detective(self, mystery_description):
        # Simplistic mapping based on some keywords or random logic, to find best detective
        keywords_intellect = ["code", "puzzle", "logic", "murder", "locked room", "clue", "hidden", "intellect", "smart"]

        candidates = []
        for char in self.characters:
            score = 0
            text = (char['core_emotion'] + " " + char['personality_profile'] + " " + char['unique_quality']).lower()
            for kw in keywords_intellect:
                if kw in mystery_description.lower():
                    score += 1
            if "logic" in text or "intellectual" in text or "pragmatic" in text or "stoic" in text or "smart" in text or "calculate" in text or "calculating" in text or "wise" in text or "wisdom" in text:
                score += 2

            candidates.append((score, char))

        candidates.sort(key=lambda x: x[0], reverse=True)
        # Add some randomness among top 3
        top_candidates = [c[1] for c in candidates[:3]]
        return random.choice(top_candidates) if top_candidates else random.choice(self.characters)

    def _select_analyst(self, mystery_description, lead_detective):
        candidates = [c for c in self.characters if c['name'] != lead_detective['name']]
        # Analyst could be someone with contrasting traits or supportive
        return random.choice(candidates) if candidates else lead_detective

    def solve_case(self, mystery_description):
        lead = self._select_lead_detective(mystery_description)
        analyst = self._select_analyst(mystery_description, lead)

        # Generate a solution narrative based on traits
        lead_approach = f"Using their '{lead['unique_quality']}', {lead['name']} approached the mystery driven by {lead['core_emotion']}."
        analyst_support = f"Meanwhile, {analyst['name']} acted as the analyst, contrasting the approach with their '{analyst['personality_profile']}' and focusing on {analyst['core_emotion']}."

        # Simplified solution text
        resolution = f"By combining {lead['name']}'s deductive method and {analyst['name']}'s analytical support, the agency uncovered the truth behind the mystery: '{mystery_description[:30]}...'."

        return {
            "mystery": mystery_description,
            "lead_detective": lead,
            "analyst": analyst,
            "solution": f"{lead_approach}\n\n{analyst_support}\n\n{resolution}",
            "thought_process": [
                f"Analyzing mystery: {mystery_description}",
                f"Evaluating characters for Lead Detective role based on intellect, logic, and core emotions...",
                f"Selected {lead['name']} as Lead Detective (Core Emotion: {lead['core_emotion']}).",
                f"Selecting complementary Analyst...",
                f"Selected {analyst['name']} as Analyst.",
                "Synthesizing investigative approaches to generate solution..."
            ]
        }
