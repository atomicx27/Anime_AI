import random

class SurvivalAgent:
    def __init__(self, characters):
        self.characters = characters

        self.survival_roles = [
            "Leader/Strategist",
            "Scavenger/Forager",
            "Defender/Vanguard",
            "Wildcard/Lone Wolf",
            "Medic/Support",
            "Scout/Recon",
            "Engineer/Builder"
        ]

    def _determine_role(self, char):
        core_emotion = char.get("core_emotion", "").lower()
        personality = char.get("personality_profile", "").lower()
        archetype = char.get("archetype", "").lower()

        if "control" in core_emotion or "ambition" in core_emotion or "strategist" in personality or "intj" in archetype or "entj" in archetype:
            return "Leader/Strategist"
        elif "protect" in core_emotion or "duty" in core_emotion or "vanguard" in personality:
            return "Defender/Vanguard"
        elif "empathy" in core_emotion or "comfort" in core_emotion or "hope" in core_emotion:
            return "Medic/Support"
        elif "excitement" in core_emotion or "combat" in core_emotion or "reckless" in personality:
            return "Wildcard/Lone Wolf"
        elif "logic" in core_emotion or "pragmatic" in personality:
            return "Engineer/Builder"
        elif "stealth" in personality or "scout" in personality:
            return "Scout/Recon"
        else:
            return random.choice(["Scavenger/Forager", "Scout/Recon", "Defender/Vanguard"])

    def _generate_strategy(self, char, role, scenario):
        name = char.get("name")
        unique_quality = char.get("unique_quality", "")

        # Determine survival status based on role and a bit of randomness
        survives = random.choice([True, True, True, False]) # High chance to survive
        status = "Survived" if survives else "Perished"

        if role == "Leader/Strategist":
            action = f"{name} immediately analyzed the situation. They formulated a plan taking advantage of their {unique_quality}. By assigning tasks efficiently, they managed to keep the group cohesive during the {scenario}."
        elif role == "Defender/Vanguard":
            action = f"When the {scenario} hit, {name} put themselves on the front lines. Utilizing their {unique_quality}, they protected the weaker members of the group, taking the brunt of the danger."
        elif role == "Medic/Support":
            action = f"{name} focused on keeping morale high and treating injuries. Their {unique_quality} proved invaluable for maintaining the group's physical and mental health through the hardships of the {scenario}."
        elif role == "Wildcard/Lone Wolf":
            action = f"{name} struck out on their own to face the {scenario} head-on. Relying on their {unique_quality}, their unpredictable actions ended up saving the group, albeit in a highly reckless manner."
        elif role == "Engineer/Builder":
            action = f"{name} gathered materials to build shelter and defenses. Their {unique_quality} allowed them to construct a safe haven against the elements of the {scenario}."
        elif role == "Scout/Recon":
            action = f"{name} ventured ahead to gather intelligence. Using their {unique_quality}, they navigated the {scenario} to find safe paths and essential supplies."
        else:
            action = f"{name} scavenged for resources to ensure the group's survival. Their {unique_quality} helped them uncover hidden caches of supplies needed during the {scenario}."

        if not survives:
            action += f" Ultimately, however, they sacrificed themselves to ensure the others could escape the {scenario}."

        return {
            "name": name,
            "role": role,
            "avatar": char.get("avatar"),
            "status": status,
            "strategy": action
        }

    def simulate_survival(self, scenario):
        results = []
        for char in self.characters:
            role = self._determine_role(char)
            result = self._generate_strategy(char, role, scenario)
            results.append(result)

        # Optional: Sort so leaders/defenders appear first, or keep it random/original order
        # We'll just return as generated
        return {
            "scenario": scenario,
            "survivors": [r for r in results if r['status'] == 'Survived'],
            "casualties": [r for r in results if r['status'] == 'Perished'],
            "all_results": results
        }
