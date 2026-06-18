from character_agent import CharacterAgent
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich import box
import time

console = Console()

class ModeratorAgent:
    def __init__(self, character_data_list):
        self.agents = [CharacterAgent(data) for data in character_data_list]

    def discuss_topic(self, topic):
        console.print(f"\n⚡ [bold cyan]--- Council Meeting on: '{topic}' ---[/bold cyan] ⚡\n")

        insights = []

        table = Table(title="🔥 [bold red]Live Council Deliberation[/bold red] 🔥", show_header=True, header_style="bold magenta", box=box.HEAVY_EDGE)
        table.add_column("Agent", style="cyan", width=20, justify="right")
        table.add_column("Status / Advice", style="green")

        from rich.progress import Progress, SpinnerColumn, TextColumn

        with Live(table, console=console, refresh_per_second=15) as live:
            for agent in self.agents:
                # Show agent is thinking with a more dynamic indicator
                temp_table = Table(title="Live Council Deliberation", show_header=True, header_style="bold magenta")
                temp_table.add_column("Agent", style="cyan", width=20)
                temp_table.add_column("Status / Advice", style="green")
                for i in range(len(insights)):
                    temp_table.add_row(self.agents[i].name, insights[i])
                temp_table.add_row(agent.name, "[italic yellow]... Processing Council Directive ...[/italic yellow]")
                live.update(temp_table)

                # Simulate thinking time and get advice
                time.sleep(0.6)
                advice = agent.give_advice(topic)
                insights.append(advice)

                # Add current insight with a typing effect
                displayed_advice = ""
                # Chunking the advice slightly for smoother typing rather than character by character
                chunk_size = 3
                for i in range(0, len(advice), chunk_size):
                    displayed_advice += advice[i:i+chunk_size]
                    temp_table = Table(title="Live Council Deliberation", show_header=True, header_style="bold magenta")
                    temp_table.add_column("Agent", style="cyan", width=20)
                    temp_table.add_column("Status / Advice", style="green")
                    for j in range(len(insights) - 1):
                        temp_table.add_row(self.agents[j].name, insights[j])
                    temp_table.add_row(agent.name, displayed_advice + "█")
                    live.update(temp_table)
                    time.sleep(0.01)

                # Add the final completed row without the cursor
                final_table = Table(title="Live Council Deliberation", show_header=True, header_style="bold magenta")
                final_table.add_column("Agent", style="cyan", width=20)
                final_table.add_column("Status / Advice", style="green")
                for j in range(len(insights)):
                    final_table.add_row(self.agents[j].name, insights[j])

                table = final_table
                live.update(table)
                time.sleep(0.3)

        console.print("\n⚖️  [bold cyan]--- Moderator Synthesis ---[/bold cyan] ⚖️")
        console.print("The council has deliberated. Here is the synthesized resolution:\n")

        summary_table = Table(title="💡 [bold yellow]Council Perspectives[/bold yellow] 💡", box=box.SIMPLE_HEAVY, show_lines=True)
        summary_table.add_column("Agent", style="cyan")
        summary_table.add_column("Core Emotion", style="green")
        summary_table.add_column("Perspective Suggestion", style="magenta")

        for idx, advice in enumerate(insights):
            agent_name = self.agents[idx].name
            core_emotion = self.agents[idx].core_emotion
            summary_table.add_row(agent_name, core_emotion, f"[italic]Approaching it with their core emotion[/italic]")

        console.print(summary_table)

        final_verdict = f"\nFinal Verdict: By combining the insights of all these characters, we can address '{topic}' from multiple philosophical angles."
        console.print(Panel(final_verdict, title="📜 [bold green]Resolution[/bold green] 📜", expand=False, border_style="green", box=box.DOUBLE_EDGE))

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
