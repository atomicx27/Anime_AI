from character_agent import CharacterAgent

class ModeratorAgent:
    def __init__(self, character_data_list):
        self.agents = [CharacterAgent(data) for data in character_data_list]

    def discuss_topic(self, topic):
        print(f"\n--- Council Meeting on: '{topic}' ---\n")

        insights = []
        for agent in self.agents:
            print(f"{agent.name} is speaking...")
            advice = agent.give_advice(topic)
            insights.append(advice)
            print("-" * 40)

        print("\n--- Moderator Synthesis ---")
        print("The council has deliberated. Here is the synthesized resolution:")

        resolution = "Synthesis of perspectives:\n"
        for idx, advice in enumerate(insights):
            agent_name = self.agents[idx].name
            resolution += f"- {agent_name} suggests approaching it with their core emotion: {self.agents[idx].core_emotion}\n"

        resolution += f"\nFinal Verdict: By combining the insights of all these characters, we can address '{topic}' from multiple philosophical angles."
        print(resolution)

        return resolution

if __name__ == "__main__":
    sample_data_list = [
        {
            "name": "Naruto Uzumaki",
            "archetype": "Protagonist, ENFP",
            "core_emotion": "Desire for Acknowledgment & Empathy",
            "personality_profile": "Boisterous...",
            "unique_quality": "Talk no Jutsu..."
        },
        {
            "name": "Itachi Uchiha",
            "archetype": "Antagonist, INFJ",
            "core_emotion": "Deep Love Masked by Cold Logic",
            "personality_profile": "Stoic, hyper-intelligent...",
            "unique_quality": "Mastery of genjutsu..."
        }
    ]
    moderator = ModeratorAgent(sample_data_list)
    moderator.discuss_topic("how to achieve true peace")
