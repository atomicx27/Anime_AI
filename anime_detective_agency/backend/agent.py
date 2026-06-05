import random

class DetectiveAgencyAgent:
    def __init__(self, characters):
        self.characters = characters

    def _assign_role(self, character, mystery):
        """Assigns an investigation role based on character traits and the mystery."""
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()

        roles = ["Lead Investigator", "Forensics Analyst", "Interrogator", "Undercover Operative", "Profiler", "Wildcard"]

        # Simple heuristic to determine role
        chosen_role = "Wildcard"
        score = {role: 0 for role in roles}

        if any(word in core_emotion or word in personality or word in quality for word in ["logic", "calm", "analyze", "strategy", "smart"]):
            score["Lead Investigator"] += 3
            score["Forensics Analyst"] += 2

        if any(word in core_emotion or word in personality or word in quality for word in ["science", "detail", "observe", "meticulous"]):
            score["Forensics Analyst"] += 3
            score["Lead Investigator"] += 1

        if any(word in core_emotion or word in personality or word in quality for word in ["intimidation", "combat", "force", "aggressive", "pride"]):
            score["Interrogator"] += 3

        if any(word in core_emotion or word in personality or word in quality for word in ["deception", "stealth", "shadow", "actor", "manipulate"]):
            score["Undercover Operative"] += 3

        if any(word in core_emotion or word in personality or word in quality for word in ["empathy", "psychology", "understanding", "read"]):
            score["Profiler"] += 3

        if any(word in core_emotion or word in personality or word in quality for word in ["chaos", "unpredictable", "crazy", "mad"]):
            score["Wildcard"] += 3

        # Add a little randomness
        for role in roles:
            score[role] += random.random()

        # Find the role with the highest score
        chosen_role = max(score, key=score.get)

        # Generate investigation finding/strategy
        if chosen_role == "Lead Investigator":
            finding = f"Analyzes the clues left at the scene using their '{character['unique_quality'].split('.')[0]}', deducing the culprit's motive with sharp logic."
        elif chosen_role == "Forensics Analyst":
            finding = f"Meticulously examines the physical evidence, leveraging their {character['core_emotion']} to uncover hidden details others missed."
        elif chosen_role == "Interrogator":
            finding = f"Corners the prime suspect and uses their intimidating {character['personality_profile'].split('.')[0]} to extract a confession."
        elif chosen_role == "Undercover Operative":
            finding = f"Infiltrates the criminal underworld, using their {character['core_emotion']} to blend in and gather crucial intel."
        elif chosen_role == "Profiler":
            finding = f"Gets into the mind of the criminal, using their deep understanding of {character['core_emotion']} to predict the suspect's next move."
        else: # Wildcard
            finding = f"Takes an entirely unorthodox approach to the mystery, driven by '{character['unique_quality'].split('.')[0]}', surprisingly finding a breakthrough."

        return {
            "name": character["name"],
            "archetype": character["archetype"],
            "role": chosen_role,
            "finding": finding,
            "core_emotion": character["core_emotion"],
            "unique_quality": character["unique_quality"]
        }

    def investigate_mystery(self, mystery):
        """Processes a mystery and assigns investigation roles and findings to characters."""
        logs = []
        logs.append(f"Anime Detective Agency opening case file: '{mystery}'")
        logs.append(f"Assembling the task force from {len(self.characters)} available agents...")

        # Select a smaller task force to avoid clutter (e.g., 4-6 characters)
        num_agents = min(len(self.characters), random.randint(4, 6))

        # Pick characters pseudo-randomly but try to get diverse roles
        task_force = random.sample(self.characters, num_agents)

        investigators = []
        for char in task_force:
            investigators.append(self._assign_role(char, mystery))

        # Summarize roles
        role_counts = {}
        for inv in investigators:
            role = inv["role"]
            role_counts[role] = role_counts.get(role, 0) + 1

        summary = ", ".join([f"{count} {role}" for role, count in role_counts.items()])
        logs.append(f"Task force assembled: {summary}")

        # Check for case resolution status based on roles
        if "Lead Investigator" in role_counts and ("Forensics Analyst" in role_counts or "Interrogator" in role_counts):
             logs.append("CASE STATUS: The team is well-balanced. High probability of solving the mystery.")
             conclusion = "The case was successfully closed thanks to the team's combined efforts."
        elif role_counts.get("Wildcard", 0) >= 2:
             logs.append("CASE STATUS: Too many wildcards! The investigation is pure chaos.")
             conclusion = "The truth remains elusive as the agency caused more problems than they solved."
        else:
             logs.append("CASE STATUS: The investigation is proceeding, but lacks a clear direction.")
             conclusion = "The mystery is partially solved, but some secrets remain hidden."

        return {
            "mystery": mystery,
            "investigators": investigators,
            "logs": logs,
            "conclusion": conclusion
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DetectiveAgencyAgent(chars)
    res = agent.investigate_mystery("The Phantom Thief has stolen the Crown Jewels.")
    print(f"Results for: {res['mystery']}")
    for r in res['investigators']:
        print(f"[{r['role']}] {r['name']} - {r['finding']}")
    print(f"Conclusion: {res['conclusion']}")