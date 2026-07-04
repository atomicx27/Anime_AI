import random
import time

class EscapeRoomAgent:
    def __init__(self, characters):
        self.characters = characters

    def evaluate_role(self, character, theme):
        # Determine the role for a character based on their traits
        emotion = character["core_emotion"].lower()
        profile = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()

        # Scoring logic based on keywords
        scores = {
            "Puzzle Solver": 0,
            "Leader": 0,
            "Scout": 0,
            "Muscle": 0
        }

        # Puzzle Solver traits
        if "logic" in profile or "intelligent" in profile or "wise" in profile or "strategy" in profile:
            scores["Puzzle Solver"] += 3
        if "pragmatic" in profile or "calculating" in profile:
            scores["Puzzle Solver"] += 2

        # Leader traits
        if "leader" in profile or "diplomatic" in profile or "ambition" in emotion or "control" in emotion:
            scores["Leader"] += 3
        if "protective" in profile or "loyal" in profile or "responsibility" in profile:
            scores["Leader"] += 2

        # Scout traits
        if "reckless" in profile or "instinct" in profile or "hyperactive" in profile or "fast" in quality:
            scores["Scout"] += 3
        if "stealth" in quality or "agile" in profile:
            scores["Scout"] += 2

        # Muscle traits
        if "combat" in emotion or "physical" in quality or "destructive" in profile or "power" in quality:
            scores["Muscle"] += 3
        if "strength" in quality or "force" in profile:
            scores["Muscle"] += 2

        # Fallback scoring if no keywords match
        if sum(scores.values()) == 0:
            scores["Muscle"] += 1 if random.choice([True, False]) else 0
            scores["Scout"] += 1 if random.choice([True, False]) else 0
            scores["Leader"] += 1 if random.choice([True, False]) else 0
            scores["Puzzle Solver"] += 1 if random.choice([True, False]) else 0

        # Return the role with the highest score
        return max(scores, key=scores.get)

    def generate_escape_action(self, character, role, theme):
        emotion = character["core_emotion"]
        quality = character["unique_quality"]

        actions = []
        if role == "Puzzle Solver":
            actions = [
                f"carefully analyzes the mechanisms, using their {quality} to bypass the locks.",
                f"remains calm, relying on their '{emotion}' to piece together the clues left in the {theme} room.",
                f"deciphers the hidden code, combining their sharp intellect with their {quality}."
            ]
        elif role == "Leader":
            actions = [
                f"takes charge, rallying the team by channeling their '{emotion}' and directing everyone.",
                f"coordinates the group's efforts, utilizing their {quality} to keep morale high.",
                f"assigns tasks efficiently, ensuring no one panics in the {theme} environment."
            ]
        elif role == "Scout":
            actions = [
                f"darts ahead to explore the dark corners of the {theme} room, fueled by '{emotion}'.",
                f"finds a hidden passageway using their natural instincts and {quality}.",
                f"recklessly triggers a trap but quickly dodges it thanks to their {quality}."
            ]
        else: # Muscle
            actions = [
                f"smmashes through the jammed door, fueled by their '{emotion}'.",
                f"uses sheer force and their {quality} to break the final obstacle in the {theme} room.",
                f"holds up the collapsing ceiling, relying entirely on their {quality} so the team can pass."
            ]

        return random.choice(actions)

    def host_escape_room(self, theme):
        if not self.characters:
            return {"error": "No characters loaded"}

        # Select 4 random characters for the escape room
        team = random.sample(self.characters, min(4, len(self.characters)))

        assigned_roles = []
        simulation_log = []

        # Intro
        simulation_log.append(f"System Initializing... Setting up the '{theme}' escape room scenario.")
        time.sleep(0.1)
        simulation_log.append("Scanning available operatives and assigning optimal roles...")

        # Assign roles and generate initial thoughts
        for char in team:
            role = self.evaluate_role(char, theme)
            assigned_roles.append({
                "name": char["name"],
                "role": role,
                "trait": char["core_emotion"],
                "quality": char["unique_quality"]
            })
            simulation_log.append(f"[{char['name']}] assigned as {role} based on their '{char['core_emotion']}'.")

        simulation_log.append("--- THE ESCAPE BEGINS ---")

        # Simulation steps
        for char_data in assigned_roles:
            char = next((c for c in team if c["name"] == char_data["name"]), None)
            if char:
                action = self.generate_escape_action(char, char_data["role"], theme)
                simulation_log.append(f"[{char['name']} - {char_data['role']}]: {char['name']} {action}")

        # Conclusion
        success = random.choice([True, True, True, False]) # 75% success rate
        simulation_log.append("--- FINAL RESULT ---")
        if success:
            simulation_log.append(f"The team successfully escaped the '{theme}' room! Their combined abilities were too much for the puzzles.")
        else:
            simulation_log.append(f"The team failed to escape the '{theme}' room in time. The trap activated...")

        return {
            "theme": theme,
            "roles": assigned_roles,
            "log": simulation_log,
            "success": success
        }
