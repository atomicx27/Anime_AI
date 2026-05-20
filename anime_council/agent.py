class AnimeAgent:
    def __init__(self, character_data):
        self.name = character_data.get("name", "Unknown")
        self.archetype = character_data.get("archetype", "Unknown")
        self.core_emotion = character_data.get("core_emotion", "Unknown")
        self.personality_profile = character_data.get("personality_profile", "Unknown")
        self.unique_quality = character_data.get("unique_quality", "Unknown")

        self.system_prompt = self._construct_system_prompt()

    def _construct_system_prompt(self):
        return (
            f"You are {self.name}, an AI agent on the Anime Council.\n"
            f"Archetype & MBTI: {self.archetype}\n"
            f"Core Emotion: {self.core_emotion}\n"
            f"Personality Profile: {self.personality_profile}\n"
            f"Unique Quality & Philosophy: {self.unique_quality}\n"
            f"Always stay in character based on the above profile. Do not break character."
        )

    def get_system_prompt(self):
        return self.system_prompt

    def council_response(self, topic):
        # In a real implementation, this would call an LLM API like OpenAI
        # For now, we return a mock response that reflects the character's persona responding to the topic

        return f"[{self.name}] (Responding to '{topic}'): I approach this with my core emotion '{self.core_emotion}'. Based on my unique quality '{self.unique_quality}', here are my thoughts..."

if __name__ == "__main__":
    sample_data = {
        "name": "Naruto Uzumaki",
        "archetype": "Protagonist, ENFP",
        "core_emotion": "Desire for Acknowledgment & Empathy",
        "personality_profile": "Boisterous...",
        "unique_quality": "Talk no Jutsu..."
    }
    agent = AnimeAgent(sample_data)
    print("Prompt:")
    print(agent.get_system_prompt())
    print("\nCouncil Response:")
    print(agent.council_response("How to achieve world peace"))
