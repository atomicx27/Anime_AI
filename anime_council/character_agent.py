class CharacterAgent:
    def __init__(self, character_data):
        self.name = character_data.get("name", "Unknown")
        self.archetype = character_data.get("archetype", "Unknown")
        self.core_emotion = character_data.get("core_emotion", "Unknown")
        self.personality_profile = character_data.get("personality_profile", "Unknown")
        self.unique_quality = character_data.get("unique_quality", "Unknown")

    def give_advice(self, topic):
        # Generate a templated advice based on the character's traits
        advice = f"[{self.name}] speaking with {self.core_emotion}.\n"
        advice += f"My approach is shaped by my personality: {self.personality_profile}\n"
        advice += f"My philosophy: {self.unique_quality}\n"
        advice += f"Regarding '{topic}': I believe we should face this using my unique perspective and abilities.\n"
        return advice

if __name__ == "__main__":
    sample_data = {
        "name": "Naruto Uzumaki",
        "archetype": "Protagonist, ENFP",
        "core_emotion": "Desire for Acknowledgment & Empathy",
        "personality_profile": "Boisterous...",
        "unique_quality": "Talk no Jutsu..."
    }
    agent = CharacterAgent(sample_data)
    print(agent.give_advice("how to overcome failure"))
