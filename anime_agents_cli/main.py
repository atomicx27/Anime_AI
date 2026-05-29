import sys
import time
from parser import parse_readme_characters
from agent import AnimeAgent
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.markdown import Markdown

console = Console()

def main():
    console.print(Panel.fit("[bold cyan]Welcome to Anime Agents CLI![/bold cyan]"))
    with console.status("[bold green]Loading characters from README.md..."):
        characters = parse_readme_characters()

    if not characters:
        console.print("[bold red]No characters found. Make sure the README.md is formatted correctly.[/bold red]")
        sys.exit(1)

    while True:
        table = Table(title="Available Characters", show_header=True, header_style="bold magenta", border_style="cyan")
        table.add_column("No.", justify="right", style="cyan", no_wrap=True)
        table.add_column("Character", style="bold white")
        table.add_column("Core Emotion", style="green")
        table.add_column("Archetype", style="yellow")

        for idx, char in enumerate(characters):
            table.add_row(str(idx + 1), char['name'], char['core_emotion'], char.get('archetype', 'N/A'))

        console.print(table)
        console.print(Panel("[bold yellow]0.[/bold yellow] Exit", expand=False, border_style="yellow"))

        try:
            console.print("\n[bold cyan]Select a character by number to chat with them:[/bold cyan]", end=" ")
            choice = input()
            if not choice.strip():
                continue

            choice_idx = int(choice) - 1

            if choice_idx == -1:
                console.print("[bold yellow]Goodbye![/bold yellow]")
                break

            if 0 <= choice_idx < len(characters):
                selected_char = characters[choice_idx]
                agent = AnimeAgent(selected_char)

                console.print(f"\n[bold green]--- Initializing Agent: {agent.name} ---[/bold green]")
                console.print(Panel(agent.get_system_prompt(), title="[bold blue]System Prompt Generated[/bold blue]", border_style="blue", expand=False))

                console.print(Panel(f"You are now chatting with [bold cyan]{agent.name}[/bold cyan]. Type 'quit' to select someone else.", style="bold green", expand=False))
                while True:
                    console.print("\n[bold magenta]You:[/bold magenta]", end=" ")
                    user_msg = input()
                    if user_msg.lower() == 'quit':
                        break

                    with console.status(f"[bold cyan]{agent.name} is thinking...[/bold cyan]", spinner="dots"):
                        response = agent.chat(user_msg)

                    console.print()
                    with Live(console=console, refresh_per_second=30) as live:
                        displayed_response = ""
                        for char in response:
                            displayed_response += char
                            live.update(Panel(Markdown(f"**{agent.name}:** {displayed_response}"), border_style="cyan"))
                            time.sleep(0.01)
            else:
                console.print("[bold red]Invalid selection. Please try again.[/bold red]")
        except ValueError:
            console.print("[bold red]Please enter a valid number.[/bold red]")
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Goodbye![/bold yellow]")
            break

if __name__ == "__main__":
    main()
