import random
import time

class DetectiveAgencyAgent:
    def __init__(self, characters):
        self.characters = characters

    def investigate(self, mystery_description: str):
        # We need to pick a Lead Detective, a Forensic Expert, and a Suspect/Wildcard

        # Categorize characters based on their traits
        detectives = []
        forensics = []
        wildcards = []

        for char in self.characters:
            archetype = char['archetype'].lower()
            emotion = char['core_emotion'].lower()

            if 'intj' in archetype or 'infj' in archetype or 'logic' in emotion or 'strategic' in emotion:
                detectives.append(char)
                forensics.append(char)
            elif 'protagonist' in archetype or 'mentor' in archetype:
                detectives.append(char)
            else:
                wildcards.append(char)

        # Ensure we have at least some characters in each pool
        if not detectives:
            detectives = self.characters.copy()
        if not forensics:
            forensics = self.characters.copy()
        if not wildcards:
            wildcards = self.characters.copy()

        lead = random.choice(detectives)
        # remove lead from other pools to avoid duplicates
        forensics = [c for c in forensics if c['name'] != lead['name']]
        if not forensics: forensics = [c for c in self.characters if c['name'] != lead['name']]
        expert = random.choice(forensics)

        wildcards = [c for c in wildcards if c['name'] not in [lead['name'], expert['name']]]
        if not wildcards: wildcards = [c for c in self.characters if c['name'] not in [lead['name'], expert['name']]]
        wildcard = random.choice(wildcards)

        # Generate a solution and roles
        response = {
            "mystery": mystery_description,
            "team": [
                {
                    "role": "Lead Detective",
                    "character": lead['name'],
                    "approach": f"Uses their {lead['core_emotion']} to understand the motive. Their {lead['unique_quality']} helps them piece together the psychological aspects of the crime.",
                    "quote": self._generate_quote(lead, "Lead Detective")
                },
                {
                    "role": "Forensic Expert",
                    "character": expert['name'],
                    "approach": f"Relies on their {expert['personality_profile']} to analyze the evidence. They use their {expert['unique_quality']} to uncover hidden physical clues.",
                    "quote": self._generate_quote(expert, "Forensic Expert")
                },
                {
                    "role": "The Wildcard / Prime Suspect",
                    "character": wildcard['name'],
                    "approach": f"Complicates the investigation with their {wildcard['core_emotion']}. Their {wildcard['personality_profile']} makes them unpredictable in the interrogation room.",
                    "quote": self._generate_quote(wildcard, "Wildcard")
                }
            ],
            "conclusion": f"After a thorough investigation, {lead['name']} and {expert['name']} deduce that the culprit used a method reflecting {wildcard['unique_quality']}. The case is solved through a combination of deduction and {lead['unique_quality']}."
        }

        return response

    def _generate_quote(self, character, role):
        if role == "Lead Detective":
            return f"The truth is hidden in their hearts. With my {character['core_emotion']}, I'll uncover it!"
        elif role == "Forensic Expert":
            return f"The evidence never lies. Let me use my {character['unique_quality']} to analyze this."
        else:
            return f"You think I did it? My {character['core_emotion']} says otherwise! Prove it!"

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DetectiveAgencyAgent(chars)
    print(agent.investigate("The missing ramen bowl of the Hidden Leaf Village."))
