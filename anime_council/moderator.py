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
        console.print(Panel(f"Council Meeting on: [bold yellow]'{topic}'[/bold yellow]", border_style="cyan", title="[bold blue]Topic[/bold blue]"))

        insights = []

        table = Table(title="[bold blue]Live Council Deliberation[/bold blue]", show_header=True, header_style="bold magenta", border_style="cyan", show_lines=True)
        table.add_column("Agent", style="bold cyan", width=20, justify="right")
        table.add_column("Status / Advice", style="green")

        with Live(table, console=console, refresh_per_second=10) as live:
            for agent in self.agents:
                # Show agent is thinking
                temp_table = Table(title="[bold blue]Live Council Deliberation[/bold blue]", show_header=True, header_style="bold magenta", border_style="cyan", show_lines=True)
                temp_table.add_column("Agent", style="bold cyan", width=20, justify="right")
                temp_table.add_column("Status / Advice", style="green")

                for i in range(len(insights)):
                    temp_table.add_row(self.agents[i].name, insights[i])

                temp_table.add_row(agent.name, "[italic yellow]Formulating perspective...[/italic yellow]")
                live.update(temp_table)

                # Simulate thinking time and get advice
                time.sleep(0.5)
                advice = agent.give_advice(topic)
                insights.append(advice)

                # Add current insight with a typing effect
                displayed_advice = ""
                for char in advice:
                    displayed_advice += char
                    type_table = Table(title="[bold blue]Live Council Deliberation[/bold blue]", show_header=True, header_style="bold magenta", border_style="cyan", show_lines=True)
                    type_table.add_column("Agent", style="bold cyan", width=20, justify="right")
                    type_table.add_column("Status / Advice", style="green")
                    for i in range(len(insights) - 1):
                        type_table.add_row(self.agents[i].name, insights[i])
                    type_table.add_row(agent.name, displayed_advice + "[bold yellow]█[/bold yellow]")
                    live.update(type_table)
                    time.sleep(0.005)

                # Add the final completed row without the cursor
                new_table = Table(title="[bold blue]Live Council Deliberation[/bold blue]", show_header=True, header_style="bold magenta", border_style="cyan", show_lines=True)
                new_table.add_column("Agent", style="bold cyan", width=20, justify="right")
                new_table.add_column("Status / Advice", style="green")
                for i in range(len(insights)):
                    new_table.add_row(self.agents[i].name, insights[i])

                table = new_table
                live.update(table)
                time.sleep(0.2)

        console.print()
        console.print(Panel(Text("Moderator Synthesis", justify="center", style="bold cyan"), border_style="cyan", expand=False))
        console.print("[italic]The council has deliberated. Here is the synthesized resolution:[/italic]")

        summary_table = Table(title="[bold blue]Council Perspectives[/bold blue]", show_header=True, header_style="bold magenta", border_style="cyan", show_lines=True)
        summary_table.add_column("Agent", style="bold cyan", justify="right")
        summary_table.add_column("Core Emotion", style="green")
        summary_table.add_column("Perspective Suggestion", style="magenta")

        for idx, advice in enumerate(insights):
            agent_name = self.agents[idx].name
            core_emotion = self.agents[idx].core_emotion
            summary_table.add_row(agent_name, core_emotion, "[italic]Approaching it with their core emotion[/italic]")

        console.print(summary_table)

        final_verdict = f"Final Verdict: By combining the insights of all these characters, we can address [bold yellow]'{topic}'[/bold yellow] from multiple philosophical angles."
        console.print(Panel(final_verdict, title="[bold green]Resolution[/bold green]", border_style="green", expand=False))

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
