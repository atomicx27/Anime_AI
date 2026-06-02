import random

class CourtroomAgent:
    def __init__(self, characters):
        self.characters = characters

    def _assign_roles(self, case_description):
        # Sort characters based on some logic or just assign randomly for the simulation
        shuffled_chars = random.sample(self.characters, len(self.characters))

        roles = {
            "Judge": None,
            "Prosecutor": None,
            "Defense": None,
            "Defendant": None, # The user is usually the defendant or plaintiff, but let's assign an anime char or leave it to user
            "Jury": []
        }

        for char in shuffled_chars:
            profile = (char['core_emotion'] + " " + char['personality_profile']).lower()
            if not roles["Judge"] and ("logic" in profile or "wisdom" in profile or "control" in profile or "stoic" in profile):
                roles["Judge"] = char
            elif not roles["Prosecutor"] and ("justice" in profile or "vengeance" in profile or "duty" in profile or "pride" in profile):
                roles["Prosecutor"] = char
            elif not roles["Defense"] and ("protect" in profile or "empathy" in profile or "hope" in profile):
                roles["Defense"] = char
            else:
                roles["Jury"].append(char)

        # Fallback if roles not filled
        if not roles["Judge"]:
            roles["Judge"] = shuffled_chars[0]
            shuffled_chars.remove(shuffled_chars[0])
        if not roles["Prosecutor"]:
            roles["Prosecutor"] = shuffled_chars[1]
            shuffled_chars.remove(shuffled_chars[1])
        if not roles["Defense"]:
            roles["Defense"] = shuffled_chars[2]
            shuffled_chars.remove(shuffled_chars[2])

        # Limit jury size
        roles["Jury"] = roles["Jury"][:5]

        return roles

    def _generate_statement(self, character, role, case_description, phase):
        name = character['name']
        emotion = character['core_emotion']
        quality = character['unique_quality']

        if role == "Judge":
            if phase == "opening":
                return f"Order in the court! I, {name}, preside over this case regarding '{case_description}'. I will judge based on my {emotion}. Let the trial begin!"
            elif phase == "verdict":
                return f"Having heard both sides, my {quality} guides my decision. The court finds the defendant... guilty/not guilty (left up to interpretation)."

        elif role == "Prosecutor":
            if phase == "opening":
                return f"Your Honor, the prosecution will prove beyond a doubt that the defendant is guilty of '{case_description}'. My {emotion} demands justice!"
            elif phase == "rebuttal":
                return f"Objection! The defense's arguments are as weak as their resolve. I will crush them with my {quality}!"

        elif role == "Defense":
            if phase == "opening":
                return f"Your Honor, my client is innocent of '{case_description}'! I will protect them with my {emotion}!"
            elif phase == "rebuttal":
                return f"Take that! The prosecution's evidence is circumstantial. I'll turn this case around using my {quality}!"

        elif role == "Jury":
            return f"As a jury member, my {emotion} makes me feel conflicted about this case. I must consider {quality}."

        return "No comment."

    def simulate_trial(self, case_description):
        roles = self._assign_roles(case_description)

        trial_log = []

        trial_log.append({
            "character": roles["Judge"],
            "role": "Judge",
            "phase": "Opening",
            "statement": self._generate_statement(roles["Judge"], "Judge", case_description, "opening")
        })

        trial_log.append({
            "character": roles["Prosecutor"],
            "role": "Prosecutor",
            "phase": "Opening",
            "statement": self._generate_statement(roles["Prosecutor"], "Prosecutor", case_description, "opening")
        })

        trial_log.append({
            "character": roles["Defense"],
            "role": "Defense",
            "phase": "Opening",
            "statement": self._generate_statement(roles["Defense"], "Defense", case_description, "opening")
        })

        trial_log.append({
            "character": roles["Prosecutor"],
            "role": "Prosecutor",
            "phase": "Rebuttal",
            "statement": self._generate_statement(roles["Prosecutor"], "Prosecutor", case_description, "rebuttal")
        })

        trial_log.append({
            "character": roles["Defense"],
            "role": "Defense",
            "phase": "Rebuttal",
            "statement": self._generate_statement(roles["Defense"], "Defense", case_description, "rebuttal")
        })

        # Add a couple jury thoughts
        for juror in roles["Jury"][:2]:
            trial_log.append({
                "character": juror,
                "role": "Jury",
                "phase": "Deliberation",
                "statement": self._generate_statement(juror, "Jury", case_description, "deliberation")
            })

        trial_log.append({
            "character": roles["Judge"],
            "role": "Judge",
            "phase": "Verdict",
            "statement": self._generate_statement(roles["Judge"], "Judge", case_description, "verdict")
        })

        return {
            "case": case_description,
            "roles": roles,
            "trial_log": trial_log
        }
