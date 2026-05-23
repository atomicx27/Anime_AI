from character_agent import CharacterAgent
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import time
import sys

console = Console()

def type_text(text, style="magenta", delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")


class ModeratorAgent:
    def __init__(self, character_data_list):
        self.agents = [CharacterAgent(data) for data in character_data_list]

    def discuss_topic(self, topic):
        console.print(f"\n[bold cyan]--- Council Meeting on: '{topic}' ---[/bold cyan]\n")

        insights = []
        for agent in self.agents:
            with console.status(f"[bold yellow]{agent.name} is speaking...[/bold yellow]"):
                advice = agent.give_advice(topic)
            insights.append(advice)
            console.print(f"[bold magenta]{agent.name}:[/bold magenta] ", end="")
            type_text(advice)
            console.print("-" * 40)

        console.print("\n[bold cyan]--- Moderator Synthesis ---[/bold cyan]")
        console.print("The council has deliberated. Here is the synthesized resolution:")

        table = Table(title="Council Perspectives")
        table.add_column("Agent", style="cyan")
        table.add_column("Core Emotion", style="green")
        table.add_column("Perspective Suggestion", style="magenta")

        for idx, advice in enumerate(insights):
            agent_name = self.agents[idx].name
            core_emotion = self.agents[idx].core_emotion
            table.add_row(agent_name, core_emotion, "Approaching it with their core emotion")

        console.print(table)

        final_verdict = f"\nFinal Verdict: By combining the insights of all these characters, we can address '{topic}' from multiple philosophical angles."
        console.print(Panel(final_verdict, title="Resolution"))

        return final_verdict

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
