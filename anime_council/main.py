import sys
from parser import parse_readme_characters
from moderator import ModeratorAgent

def main():
    print("Welcome to Anime Council AI!")
    print("Loading characters from README.md to assemble the council...")

    characters = parse_readme_characters()

    if not characters:
        print("No characters found. Make sure the README.md is formatted correctly.")
        sys.exit(1)

    print(f"Successfully assembled {len(characters)} characters for the council.")

    moderator = ModeratorAgent(characters)

    while True:
        try:
            topic = input("\nEnter a topic or problem for the council to discuss (or type 'quit' to exit): ")
            if not topic.strip():
                continue

            if topic.lower() == 'quit':
                print("Goodbye!")
                break

            moderator.discuss_topic(topic)

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
