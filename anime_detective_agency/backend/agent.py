import random

class DetectiveAgent:
    def __init__(self, characters):
        self.characters = characters

        self.investigation_roles = [
            "Forensic Analyst",
            "Interrogator",
            "Undercover Operative",
            "Profiler",
            "Evidence Collector",
            "Tactical Support",
            "Lead Detective",
            "Surveillance Expert"
        ]

    def _determine_role(self, character):
        core = character['core_emotion'].lower()
        prof = character['personality_profile'].lower()

        if "empathy" in core or "pain" in core:
            return "Profiler"
        elif "combat" in core or "battle" in prof or "destructive" in prof:
            return "Tactical Support"
        elif "diplomacy" in prof or "diplomatic" in prof:
            return "Undercover Operative"
        elif "logic" in core or "intelligent" in prof or "calculating" in prof:
            return "Forensic Analyst"
        elif "control" in core or "arrogance" in core:
            return "Lead Detective"
        elif "determination" in core or "stubborn" in prof:
            return "Evidence Collector"
        else:
            return random.choice(self.investigation_roles)

    def _generate_action(self, character, case_description, role):
        core = character['core_emotion']
        unique = character['unique_quality']
        name = character['name']

        # We simulate the agent's LLM generation based on character traits
        # by building a templated response that utilizes their unique qualities.
        action = f"Utilizing my {unique}, I will approach this case by focusing on {core}."

        if role == "Profiler":
            action += f" I will analyze the psychological motives of the suspects."
        elif role == "Tactical Support":
            action += f" I will secure the perimeter and prepare for any hostile threats."
        elif role == "Undercover Operative":
            action += f" I will blend in with the local factions to gather intel."
        elif role == "Forensic Analyst":
            action += f" I will logically dissect the physical evidence left at the scene."
        elif role == "Lead Detective":
            action += f" I will orchestrate the team's movements to trap the culprit."
        elif role == "Evidence Collector":
            action += f" I will thoroughly search every inch of the scene without giving up."
        else:
            action += f" I will assist the investigation wherever my skills are needed."

        return action

    def solve_case(self, case_description):
        investigation_team = []

        for char in self.characters:
            role = self._determine_role(char)
            action = self._generate_action(char, case_description, role)

            investigation_team.append({
                "name": char["name"],
                "role": role,
                "action": action,
                "core_emotion": char["core_emotion"],
                "unique_quality": char["unique_quality"]
            })

        return {
            "case_description": case_description,
            "team_actions": investigation_team
        }
