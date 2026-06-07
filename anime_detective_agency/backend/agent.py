import random
from typing import List, Dict

class DetectiveAgent:
    def __init__(self, characters: List[Dict]):
        self.characters = characters
        self.roles = ["Forensics Expert", "Lead Investigator", "Profiler", "Interrogator", "Undercover Specialist", "Tactical Support"]

    def analyze_case(self, case_description: str) -> Dict:
        # Select 3-4 random characters for the agency task force
        team_size = random.randint(3, 4)
        selected_chars = random.sample(self.characters, team_size)

        team_roles = random.sample(self.roles, team_size)

        task_force = []
        for i, char in enumerate(selected_chars):
            role = team_roles[i]
            deduction = self._generate_deduction(char, role, case_description)
            task_force.append({
                "name": char["name"],
                "role": role,
                "core_emotion": char["core_emotion"],
                "archetype": char["archetype"],
                "deduction": deduction
            })

        # Synthesize final conclusion
        synthesis = self._generate_synthesis(task_force, case_description)

        return {
            "case": case_description,
            "task_force": task_force,
            "conclusion": synthesis
        }

    def _generate_deduction(self, char: Dict, role: str, case: str) -> str:
        # A simple template-based mock logic, can be replaced by LLM call
        name = char["name"]
        emotion = char["core_emotion"]
        quality = char["unique_quality"]

        lower_case = case.lower()
        if "murder" in lower_case or "kill" in lower_case:
            theme = "motive for violence"
        elif "stolen" in lower_case or "theft" in lower_case or "robbery" in lower_case:
            theme = "desire for possession"
        elif "missing" in lower_case or "kidnap" in lower_case:
            theme = "reason for disappearance"
        else:
            theme = "underlying truth"

        templates = [
            f"As the {role}, my analysis is driven by {emotion}. Given their {quality}, I deduce that the {theme} is directly tied to a hidden emotional scar.",
            f"Focusing on the evidence, my {emotion} tells me we are missing something. Using my {quality}, I believe the culprit left a trace of their true intentions behind.",
            f"I approach this case through the lens of {emotion}. The {theme} reveals a pattern that only someone with my {quality} could see clearly.",
            f"This is a classic misdirection. As the {role}, I use my {quality} to bypass the noise and see that {emotion} is at the heart of this mystery."
        ]

        return random.choice(templates)

    def _generate_synthesis(self, task_force: List[Dict], case: str) -> str:
        names = [member["name"] for member in task_force]
        lead = names[0]
        others = ", ".join(names[1:])

        return f"By combining the unique perspectives of our task force, {lead} realized the key to the case. Supported by the insights from {others}, the agency concludes that the culprit's actions were a desperate cry for help, masked as a complex crime. The case is closed."

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DetectiveAgent(chars)
    result = agent.analyze_case("The mysterious theft of the Crimson Diamond from the heavily guarded museum.")
    print(result)
