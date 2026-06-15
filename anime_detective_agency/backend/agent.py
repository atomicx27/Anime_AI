import json
from typing import List, Dict

class DetectiveAgent:
    def __init__(self, characters: List[Dict]):
        self.characters = characters

    def investigate(self, mystery: str) -> Dict:
        """
        Takes a mystery scenario and generates an investigation profile for all characters.
        """
        results = []

        # We simulate the AI by generating specific responses based on character traits
        for char in self.characters:
            # Determine role based on traits
            role = self._determine_role(char)
            theory = self._generate_theory(char, mystery)
            action = self._determine_action(char)

            results.append({
                "name": char["name"],
                "role": role,
                "theory": theory,
                "action": action,
                "core_emotion": char["core_emotion"]
            })

        return {
            "mystery": mystery,
            "investigation": results
        }

    def _determine_role(self, char: Dict) -> str:
        emotion = char["core_emotion"].lower()
        archetype = char["archetype"].lower()

        if "intj" in archetype or "infj" in archetype or "logic" in emotion or "regret" in emotion:
            return "Lead Investigator"
        elif "enfp" in archetype or "esfp" in archetype or "passion" in emotion or "determination" in emotion:
            return "Field Operative"
        elif "protect" in emotion or "peace" in emotion:
            return "Witness/Victim Liaison"
        elif "antagonist" in archetype or "control" in emotion or "justice" in emotion:
            return "Rogue Profiler"
        else:
            return "Consultant"

    def _generate_theory(self, char: Dict, mystery: str) -> str:
        quality = char["unique_quality"].lower()
        emotion = char["core_emotion"].lower()
        name = char["name"]

        if "talk no jutsu" in quality or "empathy" in emotion:
            return f"Believes the perpetrator is acting out of unacknowledged pain. Suggests the mystery ({mystery}) is a cry for help."
        elif "combat" in emotion or "anti-magic" in quality:
            return f"Focuses on the physical evidence. Suspects a strong opponent caused the mystery ({mystery}) to test their limits."
        elif "logic" in emotion or "genjutsu" in quality:
            return f"Thinks the obvious clues in the mystery ({mystery}) are an illusion meant to distract from the real mastermind."
        elif "trauma" in emotion or "justice" in quality:
            return f"Theorizes that the mystery ({mystery}) is an attempt to enforce a twisted sense of divine justice on the world."
        elif "diplomacy" in quality or "comfort" in emotion:
            return f"Suspects economic or political motives behind the mystery ({mystery}). Suggests looking at who profits from the chaos."
        elif "pride" in emotion or "control" in emotion:
            return f"Concludes the mystery ({mystery}) is a direct challenge to their authority. Suspects someone trying to usurp control."
        else:
            return f"Relies on their unique instincts to deduce that the mystery ({mystery}) is tied to hidden emotional motives."

    def _determine_action(self, char: Dict) -> str:
        profile = char["personality_profile"].lower()

        if "boisterous" in profile or "loud" in profile or "reckless" in profile:
            return "Charges directly into the suspected location, kicking down doors."
        elif "pragmatic" in profile or "diplomatic" in profile:
            return "Gathers information through trade networks and safe dialogue."
        elif "stoic" in profile or "hyper-intelligent" in profile or "composed" in profile:
            return "Patiently observes from the shadows, waiting for the culprit to slip up."
        elif "arrogant" in profile or "prideful" in profile:
            return "Issues a public challenge to draw the perpetrator out."
        elif "trauma" in profile or "cynical" in profile:
            return "Manipulates minor variables to force the culprit into a trap."
        else:
            return "Follows their gut feeling to track the suspect."

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DetectiveAgent(chars)
    res = agent.investigate("Someone stole the secret recipe!")
    print(json.dumps(res, indent=2))
