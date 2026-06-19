import os
import re

def parse_readme_characters(filepath=None):
    if filepath is None:
        filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "README.md")

    characters = []

    if not os.path.exists(filepath):
        print(f"Error: Could not find {filepath}")
        return characters

    with open(filepath, "r") as f:
        content = f.read()

    table_pattern = re.compile(r'\| Character \| Archetype & MBTI \| Core Emotion \| Personality Profile \| Unique Quality & Philosophy \|\n\|---\|---\|---\|---\|---\|\n(.*?)(?=\n\n|\n---|$)', re.DOTALL)
    match = table_pattern.search(content)

    if match:
        table_content = match.group(1)
        for line in table_content.strip().split('\n'):
            if line.startswith('|') and line.endswith('|'):
                parts = [p.strip() for p in line.strip('|').split('|')]
                if len(parts) >= 5:
                    characters.append({
                        "name": parts[0],
                        "archetype": parts[1],
                        "core_emotion": parts[2],
                        "personality_profile": parts[3],
                        "unique_quality": parts[4]
                    })

    return characters

if __name__ == "__main__":
    chars = parse_readme_characters()
    print(f"Loaded {len(chars)} characters")
    for char in chars[:2]:
        print(char)
