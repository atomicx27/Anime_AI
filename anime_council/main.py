import sys
from parser import parse_readme_characters
from moderator import ModeratorAgent
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def main():
    console.print(Panel.fit("[bold cyan]Welcome to Anime Council AI![/bold cyan]"))

    with Progress(
        SpinnerColumn("dots", style="cyan"),
        TextColumn("[bold green]Loading characters from README.md to assemble the council...[/bold green]"),
        transient=True,
    ) as progress:
        progress.add_task("loading", start=False)
        characters = parse_readme_characters()

    if not characters:
        console.print("[bold red]No characters found. Make sure the README.md is formatted correctly.[/bold red]")
        sys.exit(1)

    console.print(f"[bold green]Successfully assembled {len(characters)} characters for the council.[/bold green]")

    moderator = ModeratorAgent(characters)

    while True:
        try:
            topic = input("\nEnter a topic or problem for the council to discuss (or type 'quit' to exit): ")
            if not topic.strip():
                continue

            if topic.lower() == 'quit':
                console.print("[bold yellow]Goodbye![/bold yellow]")
                break

            moderator.discuss_topic(topic)

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Goodbye![/bold yellow]")
            break

if __name__ == "__main__":
    main()
