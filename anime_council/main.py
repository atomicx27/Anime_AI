import sys
from parser import parse_readme_characters
from moderator import ModeratorAgent
from rich.console import Console
from rich.panel import Panel
from rich import box

console = Console()

def main():
    console.print(Panel.fit("🏛️ [bold cyan]Welcome to Anime Council AI![/bold cyan] 🏛️", border_style="cyan", box=box.ROUNDED))
    with console.status("[bold green]Loading characters from README.md to assemble the council...[/bold green]", spinner="bouncingBar"):
        characters = parse_readme_characters()

    if not characters:
        console.print("❌ [bold red]No characters found. Make sure the README.md is formatted correctly.[/bold red]")
        sys.exit(1)

    console.print(f"✅ [bold green]Successfully assembled {len(characters)} characters for the council.[/bold green]")

    moderator = ModeratorAgent(characters)

    while True:
        try:
            console.print("\n")
            topic = console.input("🗣️  [bold yellow]Enter a topic or problem for the council to discuss (or type 'quit' to exit):[/bold yellow] ")
            if not topic.strip():
                continue

            if topic.lower() == 'quit':
                console.print("\n👋 [bold yellow]Meeting adjourned! Goodbye![/bold yellow] 👋\n")
                break

            moderator.discuss_topic(topic)

        except KeyboardInterrupt:
            console.print("\n\n👋 [bold yellow]Meeting adjourned! Goodbye![/bold yellow] 👋\n")
            break

if __name__ == "__main__":
    main()
