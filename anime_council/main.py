import sys
from parser import parse_readme_characters
from agent import AnimeAgent

def main():
    print("========================================")
    print("Welcome to the Anime Council!")
    print("Gathering the council members from README.md...")
    print("========================================")

    characters = parse_readme_characters()

    if not characters:
        print("No characters found. Make sure the README.md is formatted correctly.")
        sys.exit(1)

    council = [AnimeAgent(char) for char in characters]
    print(f"\nThe council of {len(council)} members is now assembled.\n")

    while True:
        try:
            topic = input("\nEnter a topic or problem for the council to discuss (or type 'quit' to exit): ")
            if not topic.strip():
                continue

            if topic.lower() == 'quit':
                print("The council is adjourned. Goodbye!")
                break

            print(f"\n--- Council Discussion on: '{topic}' ---\n")

            for member in council:
                response = member.council_response(topic)
                print(response)
                print("-" * 60)

        except KeyboardInterrupt:
            print("\nThe council is adjourned. Goodbye!")
            break

if __name__ == "__main__":
    main()
