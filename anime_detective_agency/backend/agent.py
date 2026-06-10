import random

class DetectiveAgencyAgent:
    def __init__(self, characters):
        self.characters = characters

    def _evaluate_role(self, case_description: str, character: dict):
        """Evaluates a character for a role in the detective agency based on their traits."""
        case_lower = case_description.lower()
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()
        archetype = character["archetype"].lower()

        # Traits
        analytical_keywords = ["calm", "smart", "logic", "diplomatic", "calculating", "wisdom", "quiet", "intelligent"]
        action_keywords = ["combat", "fight", "power", "reckless", "destructive", "effort", "physical"]
        empathy_keywords = ["empathy", "love", "protect", "peace", "resonance", "hope"]
        dark_keywords = ["trauma", "pain", "despair", "nihilism", "manipulative", "arrogance", "control", "cynical"]

        def score_keywords(keywords, text):
            return sum(1 for kw in keywords if kw in text)

        char_text = f"{core_emotion} {personality} {quality} {archetype}"
        char_analytical = score_keywords(analytical_keywords, char_text)
        char_action = score_keywords(action_keywords, char_text)
        char_empathy = score_keywords(empathy_keywords, char_text)
        char_dark = score_keywords(dark_keywords, char_text)

        # Determine Role
        if char_analytical > char_action and char_analytical >= char_empathy and char_analytical > char_dark:
            role = "Lead Detective"
            insight = f"{character['name']} approaches the case with a focus on logic. Their unique quality '{character['unique_quality'].split('.')[0]}' allows them to see the hidden threads connecting the clues."
        elif char_action > char_analytical and char_action > char_empathy:
            role = "Enforcer / Field Agent"
            insight = f"{character['name']} takes the physical approach. Driven by '{character['core_emotion']}', they will break down doors and secure the perimeter rather than analyze fingerprints."
        elif char_empathy > char_analytical and char_empathy > char_dark:
            role = "Interrogator (Good Cop)"
            insight = f"Using their '{character['core_emotion']}', {character['name']} connects with witnesses. They can intuitively understand the motives behind the crime, as seen in their '{character['personality_profile'].split('.')[0]}'."
        elif char_dark > char_empathy and char_dark >= char_analytical:
            role = "Forensics / Profiler (Dark Ops)"
            insight = f"{character['name']} understands the criminal mind perfectly because they share its shadows. Their focus on '{character['core_emotion']}' helps them predict the suspect's next move."
        else:
             role = "Wildcard / Consultant"
             insight = f"{character['name']} offers an unconventional perspective. Their approach is unpredictable, heavily influenced by their '{character['core_emotion']}'."

        # Add a random factor to spice things up if it's a tie or to make it dynamic
        if "protagonist" in archetype and role == "Forensics / Profiler (Dark Ops)":
            role = "Lead Detective"

        return {
            "name": character["name"],
            "archetype": character["archetype"],
            "role": role,
            "insight": insight,
            "analytical_score": char_analytical,
            "action_score": char_action,
            "empathy_score": char_empathy,
            "dark_score": char_dark
        }

    def assign_roles(self, case_description: str):
        """Assigns roles to all characters based on the case."""
        assignments = []
        logs = []

        logs.append(f"Agency Director AI initialized for case: '{case_description[:50]}...'")
        logs.append(f"Analyzing {len(self.characters)} available operatives for deployment...")

        for char in self.characters:
            logs.append(f"Evaluating operative profile: {char['name']}...")
            eval_result = self._evaluate_role(case_description, char)
            assignments.append(eval_result)
            logs.append(f"Result: Assigned to division [{eval_result['role']}].")

        # Sort assignments by role to group them nicely
        roles_order = {
            "Lead Detective": 0,
            "Interrogator (Good Cop)": 1,
            "Forensics / Profiler (Dark Ops)": 2,
            "Enforcer / Field Agent": 3,
            "Wildcard / Consultant": 4
        }
        assignments.sort(key=lambda x: (roles_order.get(x["role"], 5), x["name"]))

        return {
            "assignments": assignments,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DetectiveAgencyAgent(chars)
    res = agent.assign_roles("A mysterious serial thief is stealing legendary weapons across the continent. There are no traces left behind, only a strange magical residue.")
    for a in res['assignments']:
        print(f"[{a['role']}] {a['name']}: {a['insight']}")
