import sys
import time
from parser import parse_readme_characters
from agent import AnimeAgent
from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.table import Table
from rich.live import Live
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def main():
    console.print(Panel.fit("[bold cyan]Welcome to Anime Agents CLI![/bold cyan]"))

    with Progress(
        SpinnerColumn("dots", style="cyan"),
        TextColumn("[bold green]Loading characters from README.md...[/bold green]"),
        transient=True,
    ) as progress:
        progress.add_task("loading", start=False)
        characters = parse_readme_characters()

    if not characters:
        console.print("[bold red]❌ No characters found. Make sure the README.md is formatted correctly.[/bold red]")
        sys.exit(1)

    while True:
        table = Table(title="🔥 [bold yellow]Available Characters[/bold yellow] 🔥", box=box.HEAVY_EDGE, title_style="bold magenta")
        table.add_column("No.", justify="right", style="cyan", no_wrap=True)
        table.add_column("Character", style="magenta", justify="center")
        table.add_column("Core Emotion", style="green", justify="left")

        for idx, char in enumerate(characters):
            table.add_row(str(idx + 1), char['name'], char['core_emotion'], char.get('archetype', 'N/A'))

        console.print(table)
        console.print(Panel("[bold yellow]0.[/bold yellow] Exit", expand=False, border_style="yellow"))

        try:
            console.print("\n")
            choice = console.input("🎯 [bold green]Select a character by number to chat with them (or 0 to exit): [/bold green]")
            if not choice.strip():
                continue

            choice_idx = int(choice) - 1

            if choice_idx == -1:
                console.print("\n👋 [bold yellow]Goodbye![/bold yellow] 👋\n")
                break

            if 0 <= choice_idx < len(characters):
                selected_char = characters[choice_idx]
                agent = AnimeAgent(selected_char)

                console.print(f"\n🚀 [bold green]--- Initializing Agent: {agent.name} ---[/bold green] 🚀")
                console.print(Panel(agent.get_system_prompt(), title=f"🤖 [bold yellow]{agent.name}'s System Prompt Generated[/bold yellow] 🤖", expand=False, border_style="yellow", box=box.DOUBLE_EDGE))

                console.print(f"\n💬 You are now chatting with [bold cyan]{agent.name}[/bold cyan]. Type 'quit' to select someone else.\n")
                while True:
                    user_msg = console.input("👤 [bold blue]You:[/bold blue] ")
                    if user_msg.lower() == 'quit':
                        break

                    with Progress(
                        SpinnerColumn(spinner_name="bouncingBar", style="cyan"),
                        TextColumn("[progress.description]{task.description}"),
                        transient=True,
                    ) as progress:
                        progress.add_task(description=f"[bold cyan]{agent.name} is thinking...", total=None)
                        response = agent.chat(user_msg)

                    console.print()
                    with Live(console=console, refresh_per_second=60) as live:
                        displayed_response = ""
                        for char in response:
                            displayed_response += char
                            # Using rich text to make the agent name bold and colored, but allow markdown for the rest
                            live.update(Panel(Markdown(displayed_response), title=f"🎌 [bold cyan]{agent.name}[/bold cyan]", border_style="cyan", box=box.ROUNDED, expand=False))
                            time.sleep(0.01)
                    console.print("\n")
            else:
                console.print("❌ [bold red]Invalid selection. Please try again.[/bold red] ❌")
        except ValueError:
            console.print("❌ [bold red]Please enter a valid number.[/bold red] ❌")
        except KeyboardInterrupt:
            console.print("\n\n👋 [bold yellow]Goodbye![/bold yellow] 👋\n")
            break

if __name__ == "__main__":
    main()
