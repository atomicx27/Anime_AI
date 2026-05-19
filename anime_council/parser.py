import os

def parse_readme_characters(file_path="README.md"):
    # If run from inside anime_council, look in parent directory
    if not os.path.exists(file_path):
        file_path = "../README.md"

    if not os.path.exists(file_path):
        print(f"Could not find {file_path}")
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split('\n')

    characters = []
    in_table = False

    for line in lines:
        line = line.strip()
        if line.startswith("| Character | Archetype & MBTI |"):
            in_table = True
            continue

        if in_table and line.startswith("|---"):
            continue

        if in_table and not line.startswith("|"):
            in_table = False
            continue

        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 7:
                character = {
                    "name": parts[1],
                    "archetype": parts[2],
                    "core_emotion": parts[3],
                    "personality_profile": parts[4],
                    "unique_quality": parts[5]
                }
                characters.append(character)

    return characters

if __name__ == "__main__":
    chars = parse_readme_characters()
    for c in chars:
        print(f"Parsed: {c['name']}")
