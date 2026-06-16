class DetectiveAgencyAgent:
    def __init__(self, characters):
        self.characters = characters

    def investigate_mystery(self, mystery_description: str):
        logs = []
        logs.append("The Chief Inspector calls the Anime Detective Agency to order...")
        logs.append(f"Case File: '{mystery_description}'")
        logs.append("Assigning deductive roles based on character traits...")

        results = []

        for char in self.characters:
            role = self._assign_role(char)
            deduction = self._generate_deduction(char, role, mystery_description)

            results.append({
                "name": char["name"],
                "role": role,
                "archetype": char["archetype"],
                "deduction": deduction
            })

            logs.append(f"[{role}] {char['name']} is investigating...")

        return {
            "mystery": mystery_description,
            "investigations": results,
            "logs": logs
        }

    def _assign_role(self, character: dict):
        emotion = character["core_emotion"].lower()
        quality = character["unique_quality"].lower()
        profile = character["personality_profile"].lower()

        if "logic" in emotion or "logic" in profile or "intelligent" in profile or "calculating" in profile:
            return "Forensic Analyst"
        elif "empathy" in emotion or "love" in emotion or "trauma" in emotion:
            return "Psychological Profiler"
        elif "combat" in emotion or "fight" in emotion or "power" in quality:
            return "Enforcer / Scene Security"
        elif "diplomatic" in quality or "peace" in emotion:
            return "Interrogator / Negotiator"
        elif "grief" in emotion or "despair" in emotion or "nihilism" in emotion:
            return "Cold Case Specialist"
        elif "mentor" in character["archetype"].lower() or "wisdom" in profile:
            return "Senior Consultant"
        else:
            return "Field Investigator"

    def _generate_deduction(self, character: dict, role: str, mystery: str):
        # A simple simulated deduction based on their unique traits
        base_insight = f"Approaching the mystery through my focus on {character['core_emotion']}."
        action = f"Using my {character['unique_quality'].split('.')[0].lower()}, I deduce the following:"

        if role == "Forensic Analyst":
            finding = "The evidence points to a highly calculated act. No wasted movements."
        elif role == "Psychological Profiler":
            finding = "I sense deep emotional turmoil in the perpetrator. They acted out of pain."
        elif role == "Enforcer / Scene Security":
            finding = "Whoever did this had significant physical power. The scene is completely wrecked."
        elif role == "Interrogator / Negotiator":
            finding = "If we can just talk to the witnesses, I can uncover the hidden motives."
        elif role == "Cold Case Specialist":
            finding = "This reminds me of a darker time. There are hidden layers of tragedy here."
        elif role == "Senior Consultant":
            finding = "Look past the obvious. The true answer lies in the history of the location."
        else:
            finding = "I'll track down any leads out on the streets with sheer determination!"

        return f"{base_insight} {action} {finding}"
