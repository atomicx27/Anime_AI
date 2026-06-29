import time

class SurvivalAgent:
    def __init__(self, characters):
        self.characters = characters

    def _assign_role(self, char):
        # Extremely simplified logic for assigning roles based on traits
        archetype = char['archetype'].lower()
        personality = char['personality'].lower()
        emotion = char['emotion'].lower()

        if "entj" in archetype or "intj" in archetype or "leader" in personality or "strategic" in personality or "arrogance" in emotion:
            return "Leader"
        elif "protect" in emotion or "protector" in personality or "combat" in emotion:
            return "Defender"
        elif "diplomatic" in personality or "comfort" in emotion or "medic" in personality:
            return "Medic"
        elif "scavenger" in personality or "effort" in emotion or "adaptability" in personality:
            return "Scavenger"
        else:
            return "Wildcard"

    def _generate_action(self, char, role, scenario):
        # Generate an in-character action
        if role == "Leader":
            return f"{char['name']} takes charge, using their '{char['emotion']}' to organize the group and devise a plan to survive the {scenario}."
        elif role == "Defender":
            return f"{char['name']} steps to the frontlines, determined to protect the group from the {scenario}, motivated by their {char['emotion']}."
        elif role == "Medic":
            return f"{char['name']} focuses on treating injuries and maintaining morale, relying on their {char['philosophy']}."
        elif role == "Scavenger":
            return f"{char['name']} heads out to find supplies, using their {char['unique_quality'] if 'unique_quality' in char else char['philosophy']} to navigate the dangers of the {scenario}."
        else:
            return f"{char['name']} acts unpredictably in the {scenario}, driven by their {char['personality']}."

    def simulate_survival(self, scenario):
        results = []
        logs = []

        logs.append(f"Initializing survival simulation for scenario: {scenario}...")

        for char in self.characters:
            logs.append(f"Analyzing {char['name']}'s traits...")
            role = self._assign_role(char)
            logs.append(f"Assigned role {role} to {char['name']}.")

            action = self._generate_action(char, role, scenario)

            results.append({
                "character": char['name'],
                "role": role,
                "action": action,
                "emotion": char['emotion']
            })

        logs.append("Survival simulation complete.")

        return {
            "scenario": scenario,
            "results": results,
            "logs": logs
        }
