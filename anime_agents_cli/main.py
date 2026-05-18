import sys
from parser import parse_readme_characters
from agent import AnimeAgent

def main():
    print("Welcome to Anime Agents CLI!")
    print("Loading characters from README.md...")

    characters = parse_readme_characters()

    if not characters:
        print("No characters found. Make sure the README.md is formatted correctly.")
        sys.exit(1)

    while True:
        print("\nAvailable Characters:")
        for idx, char in enumerate(characters):
            print(f"{idx + 1}. {char['name']} - {char['core_emotion']}")

        print("0. Exit")

        try:
            choice = input("\nSelect a character by number to chat with them: ")
            if not choice.strip():
                continue

            choice_idx = int(choice) - 1

            if choice_idx == -1:
                print("Goodbye!")
                break

            if 0 <= choice_idx < len(characters):
                selected_char = characters[choice_idx]
                agent = AnimeAgent(selected_char)

                print(f"\n--- Initializing Agent: {agent.name} ---")
                print("System Prompt Generated:")
                print("-" * 40)
                print(agent.get_system_prompt())
                print("-" * 40)

                print(f"\nYou are now chatting with {agent.name}. Type 'quit' to select someone else.")
                while True:
                    user_msg = input("\nYou: ")
                    if user_msg.lower() == 'quit':
                        break

                    response = agent.chat(user_msg)
                    print(f"\n{response}")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
