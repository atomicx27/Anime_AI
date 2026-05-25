from character_agent import CharacterAgent
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
import time

console = Console()

class ModeratorAgent:
    def __init__(self, character_data_list):
        self.agents = [CharacterAgent(data) for data in character_data_list]

    def discuss_topic(self, topic):
        console.print(f"\n[bold cyan]--- Council Meeting on: '{topic}' ---[/bold cyan]\n")

        insights = []

        table = Table(title="Live Council Deliberation", show_header=True, header_style="bold magenta")
        table.add_column("Agent", style="cyan", width=20)
        table.add_column("Status / Advice", style="green")

        with Live(table, console=console, refresh_per_second=10) as live:
            for agent in self.agents:
                # Show agent is thinking
                table.add_row(agent.name, "[italic yellow]Thinking...[/italic yellow]")
                live.update(table)

                # Simulate thinking time and get advice
                time.sleep(0.5)
                advice = agent.give_advice(topic)
                insights.append(advice)

                # Update row with actual advice
                # We need to recreate the table or modify the rows (rich Tables aren't easily mutable like this, so we rebuild it)
                new_table = Table(title="Live Council Deliberation", show_header=True, header_style="bold magenta")
                new_table.add_column("Agent", style="cyan", width=20)
                new_table.add_column("Status / Advice", style="green")

                # Add all past insights
                for i in range(len(insights) - 1):
                    new_table.add_row(self.agents[i].name, insights[i])

                # Add current insight with a typing effect
                displayed_advice = ""
                for char in advice:
                    displayed_advice += char
                    temp_table = Table(title="Live Council Deliberation", show_header=True, header_style="bold magenta")
                    temp_table.add_column("Agent", style="cyan", width=20)
                    temp_table.add_column("Status / Advice", style="green")
                    for i in range(len(insights) - 1):
                        temp_table.add_row(self.agents[i].name, insights[i])
                    temp_table.add_row(agent.name, displayed_advice + "█")
                    live.update(temp_table)
                    time.sleep(0.005)

                # Add the final completed row without the cursor
                new_table.add_row(agent.name, advice)
                table = new_table
                live.update(table)
                time.sleep(0.2)

        console.print("\n[bold cyan]--- Moderator Synthesis ---[/bold cyan]")
        console.print("The council has deliberated. Here is the synthesized resolution:")

        summary_table = Table(title="Council Perspectives")
        summary_table.add_column("Agent", style="cyan")
        summary_table.add_column("Core Emotion", style="green")
        summary_table.add_column("Perspective Suggestion", style="magenta")

        for idx, advice in enumerate(insights):
            agent_name = self.agents[idx].name
            core_emotion = self.agents[idx].core_emotion
            summary_table.add_row(agent_name, core_emotion, "Approaching it with their core emotion")

        console.print(summary_table)

        final_verdict = f"\nFinal Verdict: By combining the insights of all these characters, we can address '{topic}' from multiple philosophical angles."
        console.print(Panel(final_verdict, title="Resolution", expand=False))

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
