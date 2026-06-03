import random

class CourtroomAgent:
    def __init__(self, characters):
        self.characters = characters

    def _assign_roles(self):
        """Assigns roles based on core emotions and personality."""
        roles = {"Judge": None, "Prosecutor": None, "Defense": None, "Jury": []}
        available_chars = list(self.characters)

        # Find a Judge (needs logic/calm)
        judge_candidates = [c for c in available_chars if any(word in c["core_emotion"].lower() or word in c["personality_profile"].lower() for word in ["logic", "calm", "wisdom", "diplomatic"])]
        if judge_candidates:
            roles["Judge"] = random.choice(judge_candidates)
        else:
            roles["Judge"] = random.choice(available_chars)
        available_chars.remove(roles["Judge"])

        # Find a Prosecutor (needs aggression/control/justice)
        prosecutor_candidates = [c for c in available_chars if any(word in c["core_emotion"].lower() or word in c["personality_profile"].lower() for word in ["control", "justice", "pride", "aggression"])]
        if prosecutor_candidates:
            roles["Prosecutor"] = random.choice(prosecutor_candidates)
        else:
            roles["Prosecutor"] = random.choice(available_chars)
        available_chars.remove(roles["Prosecutor"])

        # Find a Defense (needs empathy/protection)
        defense_candidates = [c for c in available_chars if any(word in c["core_emotion"].lower() or word in c["personality_profile"].lower() for word in ["empathy", "protect", "love", "hope"])]
        if defense_candidates:
            roles["Defense"] = random.choice(defense_candidates)
        else:
            roles["Defense"] = random.choice(available_chars)
        available_chars.remove(roles["Defense"])

        # Remaining 3 for jury
        roles["Jury"] = random.sample(available_chars, min(3, len(available_chars)))
        return roles

    def simulate_trial(self, case_description):
        """Simulates a courtroom trial based on the case description."""
        roles = self._assign_roles()
        logs = []
        logs.append(f"⚖️ Court is now in session. The Honorable {roles['Judge']['name']} presiding.")
        logs.append(f"Case: {case_description}")

        # Prosecutor Opening
        prosecutor = roles["Prosecutor"]
        prosecutor_arg = f"As Prosecutor, I, {prosecutor['name']}, will prove the defendant's guilt using my {prosecutor['core_emotion']}. My unique approach: {prosecutor['unique_quality'].split('.')[0]} leaves no room for doubt."

        # Defense Opening
        defense = roles["Defense"]
        defense_arg = f"As Defense Attorney, I, {defense['name']}, stand to protect the accused, driven by my {defense['core_emotion']}. I will leverage my {defense['unique_quality'].split('.')[0]} to reveal the truth."

        # Jury deliberation
        jury_thoughts = []
        guilty_votes = 0
        for juror in roles["Jury"]:
            # Simple heuristic for voting
            if any(word in juror["core_emotion"].lower() or word in juror["personality_profile"].lower() for word in ["logic", "control", "despair", "justice"]):
                vote = "Guilty"
                guilty_votes += 1
            else:
                vote = "Not Guilty"

            thought = f"Juror {juror['name']} ({juror['core_emotion']}): Votes {vote} based on their worldview."
            jury_thoughts.append(thought)

        # Verdict
        if guilty_votes > len(roles["Jury"]) / 2:
            verdict = "GUILTY"
            judge_statement = f"I agree with the jury. Utilizing my {roles['Judge']['core_emotion']}, I find the defendant {verdict}."
        else:
            verdict = "NOT GUILTY"
            judge_statement = f"The jury has spoken. Driven by my {roles['Judge']['core_emotion']}, I find the defendant {verdict}."

        result = {
            "case": case_description,
            "roles": {
                "Judge": roles["Judge"]["name"],
                "Prosecutor": roles["Prosecutor"]["name"],
                "Defense": roles["Defense"]["name"],
                "Jury": [j["name"] for j in roles["Jury"]]
            },
            "transcript": [
                {"speaker": "Judge " + roles["Judge"]["name"], "text": f"Court is in session. We are hearing the case: {case_description}"},
                {"speaker": "Prosecutor " + prosecutor["name"], "text": prosecutor_arg},
                {"speaker": "Defense " + defense["name"], "text": defense_arg},
                {"speaker": "Jury", "text": " | ".join(jury_thoughts)},
                {"speaker": "Judge " + roles["Judge"]["name"], "text": judge_statement}
            ],
            "verdict": verdict
        }
        return result

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = CourtroomAgent(chars)
    res = agent.simulate_trial("Did Naruto steal the forbidden ramen recipe?")
    import json
    print(json.dumps(res, indent=2))
