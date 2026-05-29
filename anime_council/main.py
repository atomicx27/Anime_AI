import sys
from parser import parse_readme_characters
from moderator import ModeratorAgent
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def main():
    welcome_text = Text("Welcome to Anime Council AI!", justify="center", style="bold cyan")
    console.print(Panel(welcome_text, border_style="cyan", padding=(1, 2), title="[bold blue]Grand Assembly[/bold blue]"))

    with console.status("[bold green]Loading characters from README.md to assemble the council...[/bold green]", spinner="arc"):
        characters = parse_readme_characters()

    if not characters:
        console.print(Panel("[bold red]No characters found. Make sure the README.md is formatted correctly.[/bold red]", border_style="red"))
        sys.exit(1)

    console.print(Panel(f"[bold green]Successfully assembled {len(characters)} characters for the council.[/bold green]", border_style="green", expand=False))

    moderator = ModeratorAgent(characters)

    while True:
        try:
            console.print("\n[bold magenta]Enter a topic or problem for the council to discuss (or type 'quit' to exit):[/bold magenta]", end=" ")
            topic = input()

            if not topic.strip():
                continue

            if topic.lower() == 'quit':
                console.print(Panel("[bold yellow]Council adjourned. Goodbye![/bold yellow]", border_style="yellow", expand=False))
                break

            moderator.discuss_topic(topic)

        except KeyboardInterrupt:
            console.print("\n" + "-"*40)
            console.print(Panel("[bold yellow]Council adjourned by user interrupt. Goodbye![/bold yellow]", border_style="yellow", expand=False))
            break

if __name__ == "__main__":
    main()
