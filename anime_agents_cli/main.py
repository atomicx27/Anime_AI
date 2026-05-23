import sys
from parser import parse_readme_characters
from agent import AnimeAgent
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import time
import sys

console = Console()

def type_text(text, style="magenta", delay=0.03):
    sys.stdout.write(f"\033[35m")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(f"\033[0m\n")


def main():
    console.print(Panel.fit("[bold cyan]Welcome to Anime Agents CLI![/bold cyan]"))
    with console.status("[bold green]Loading characters from README.md..."):
        characters = parse_readme_characters()

    if not characters:
        console.print("[bold red]No characters found. Make sure the README.md is formatted correctly.[/bold red]")
        sys.exit(1)

    while True:
        table = Table(title="Available Characters")
        table.add_column("No.", justify="right", style="cyan", no_wrap=True)
        table.add_column("Character", style="magenta")
        table.add_column("Core Emotion", style="green")

        for idx, char in enumerate(characters):
            table.add_row(str(idx + 1), char['name'], char['core_emotion'])

        console.print(table)
        console.print("[bold yellow]0.[/bold yellow] Exit")

        try:
            choice = input("\nSelect a character by number to chat with them: ")
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
                console.print(Panel(agent.get_system_prompt(), title="System Prompt Generated", expand=False))

                console.print(f"\nYou are now chatting with [bold cyan]{agent.name}[/bold cyan]. Type 'quit' to select someone else.")
                while True:
                    user_msg = input("\nYou: ")
                    if user_msg.lower() == 'quit':
                        break

                    with console.status(f"[bold cyan]{agent.name} is thinking...[/bold cyan]"):
                        response = agent.chat(user_msg)
                    print("\n")
                    type_text(response)
            else:
                console.print("[bold red]Invalid selection. Please try again.[/bold red]")
        except ValueError:
            console.print("[bold red]Please enter a valid number.[/bold red]")
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Goodbye![/bold yellow]")
            break

if __name__ == "__main__":
    main()
