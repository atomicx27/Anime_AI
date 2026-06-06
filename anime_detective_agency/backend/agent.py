class DetectiveAgencyAgent:
    def __init__(self, characters):
        self.characters = characters

    def investigate_mystery(self, mystery_description: str):
        roles = [
            "Lead Detective",
            "Profiler",
            "Forensics Specialist",
            "Interrogator",
            "Field Investigator",
            "Undercover Operative",
            "Consulting Detective",
            "Tactical Analyst",
            "Medical Examiner",
            "Crime Scene Photographer",
            "Legal Advisor",
            "Evidence Custodian",
            "Surveillance Expert",
            "Crisis Negotiator"
        ]

        assigned_roles = []
        terminal_log = [
            f"[SYSTEM] Initializing Anime Detective Agency for case: '{mystery_description}'...",
            "[SYSTEM] Evaluating operative profiles...",
        ]

        # In a real scenario, an LLM would make these choices based on the mystery.
        # Here we simulate the assignment using the character traits and the predefined roles.

        # Sort characters to have a deterministic (or pseudo-intelligent) assignment
        # We'll just do a simple assignment based on the character's archetype/emotion for this simulation.

        sorted_chars = sorted(self.characters, key=lambda x: x['name'])

        for i, char in enumerate(sorted_chars):
            role = roles[i % len(roles)]

            terminal_log.append(f"[ANALYSIS] Evaluating {char['name']}...")
            terminal_log.append(f"  - Core Emotion: {char['core_emotion']}")
            terminal_log.append(f"  - Unique Quality: {char['unique_quality']}")

            insight = self._generate_insight(char, role, mystery_description)
            terminal_log.append(f"[ASSIGNMENT] -> Role: {role}")

            assigned_roles.append({
                "character": char,
                "role": role,
                "insight": insight
            })

        terminal_log.append("[SYSTEM] Investigation team assembled.")

        return {
            "terminal_log": terminal_log,
            "team": assigned_roles
        }

    def _generate_insight(self, character, role, mystery_description):
        # Generate a simulated insight based on the character's unique philosophy and the role
        name = character['name']
        quality = character['unique_quality']

        if "Naruto" in name:
            return f"As {role}, I'll use my empathy to understand the culprit's pain. My 'Talk no Jutsu' might just get a confession!"
        elif "Goku" in name:
            return f"This case sounds tough! If the culprit is strong, I can't wait to fight them as the {role}!"
        elif "Ichigo" in name:
            return f"As {role}, my main priority is protecting the innocent victims involved in this case."
        elif "Rimuru" in name:
            return f"I'll handle the {role} duties pragmatically. Let's solve this through diplomacy and avoid unnecessary conflict."
        elif "Asta" in name:
            return f"I won't give up! My grit as the {role} will break through any magic involved in this mystery!"
        elif "Yuno" in name:
            return f"I will calmly deduce the facts as {role}. My ambition won't let me fail."
        elif "Natsu" in name:
            return f"I'm fired up! If anyone hurt my friends, I'll burn the evidence to find the truth as the {role}!"
        elif "Itachi" in name:
            return f"As {role}, I will look past the illusions of this case. The truth often hides behind a complex genjutsu."
        elif "Obito" in name:
            return f"The reality of this case is despair. As {role}, I will slip through the lies."
        elif "Madara" in name:
            return f"I will enforce order on this chaotic case. As {role}, my strategic dominance will find the culprit."
        elif "Vegeta" in name:
            return f"Hmph. As {role}, my pride won't allow this mystery to remain unsolved. I'll crush the culprit."
        elif "Jiraiya" in name:
            return f"A true {role} endures the pain of the investigation. Let's uncover the truth, for the future."
        elif "Pain" in name:
            return f"This case is born of shared trauma. As {role}, I will bring divine justice to the perpetrators."
        elif "Kakashi" in name:
            return f"As {role}, I'll read underneath the underneath. We must work as a team to solve this."
        else:
            return f"Applying my unique quality ({quality}) to my role as {role}."
