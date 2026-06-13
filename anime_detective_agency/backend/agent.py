import random

class DetectiveAgencyAgent:
    def __init__(self, characters):
        self.characters = characters

    def _select_investigators(self, mystery_description):
        # Determine roles based on character traits
        investigators = []

        # We need an analytical/logical person
        analysts = [c for c in self.characters if 'INTJ' in c['archetype'] or 'Logic' in c['unique_quality'] or 'Stoic' in c['personality_profile']]

        # We need an intuitive/instinctive person
        intuitives = [c for c in self.characters if 'Instinct' in c['personality_profile'] or 'ENFP' in c['archetype'] or 'Intuition' in c['unique_quality']]

        # We need an interrogator/forceful person
        interrogators = [c for c in self.characters if 'ENTJ' in c['archetype'] or 'Combat' in c['core_emotion'] or 'Antagonist' in c['archetype']]

        if analysts:
            investigators.append({"role": "Lead Analyst", "char": random.choice(analysts)})
        if intuitives:
            investigators.append({"role": "Field Investigator", "char": random.choice(intuitives)})
        if interrogators:
            investigators.append({"role": "Interrogator", "char": random.choice(interrogators)})

        # Fill with random if we don't have enough
        while len(investigators) < 3 and len(self.characters) >= 3:
            candidate = random.choice(self.characters)
            if not any(i['char']['name'] == candidate['name'] for i in investigators):
                roles = ["Forensic Expert", "Undercover Agent", "Profiler"]
                investigators.append({"role": random.choice(roles), "char": candidate})

        return investigators[:3]

    def _generate_clue_from_char(self, char, role, mystery):
        clue_type = ""
        clue_desc = ""

        # Simple rule-based clue generation based on character traits
        if "Logic" in char['unique_quality'] or "INTJ" in char['archetype']:
            clue_type = "Logical Deduction"
            clue_desc = f"Based on the facts, {char['name']} deduces that the timeline doesn't add up. They applied {char['unique_quality'].lower()} to find a hidden pattern in the mystery: '{mystery}'."
        elif "Instinct" in char['personality_profile'] or "ENFP" in char['archetype']:
            clue_type = "Intuitive Hunch"
            clue_desc = f"Driven by {char['core_emotion'].lower()}, {char['name']} followed a gut feeling about the scene, discovering something everyone else missed."
        elif "Combat" in char['core_emotion'] or "Antagonist" in char['archetype']:
            clue_type = "Physical Evidence"
            clue_desc = f"Using a forceful approach, {char['name']} found signs of struggle. Their {char['personality_profile'].lower()} nature led them to uncover key evidence."
        else:
            clue_type = "Puzzling Discovery"
            clue_desc = f"Applying their philosophy of {char['unique_quality']}, {char['name']} uncovered a strange anomaly related to the case."

        return {
            "character": char['name'],
            "role": role,
            "trait_used": char['core_emotion'],
            "clue_type": clue_type,
            "description": clue_desc
        }

    def solve_mystery(self, mystery_description):
        if not mystery_description or len(mystery_description.strip()) == 0:
            return {"error": "Please provide a mystery description."}

        investigators = self._select_investigators(mystery_description)

        clues = []
        for inv in investigators:
            clues.append(self._generate_clue_from_char(inv['char'], inv['role'], mystery_description))

        # Synthesize final conclusion
        lead = investigators[0]['char']['name'] if investigators else "The Agency"
        conclusion = f"By combining the analytical mind of the Lead Analyst, the intuition of the Field Investigator, and the pressure applied by the Interrogator, {lead} and the team were able to piece together the truth behind '{mystery_description}'. The case is closed."

        return {
            "mystery": mystery_description,
            "investigators": [
                {
                    "name": inv['char']['name'],
                    "role": inv['role'],
                    "avatar": f"https://api.dicebear.com/7.x/bottts/svg?seed={inv['char']['name'].replace(' ', '')}"
                } for inv in investigators
            ],
            "clues": clues,
            "conclusion": conclusion
        }
