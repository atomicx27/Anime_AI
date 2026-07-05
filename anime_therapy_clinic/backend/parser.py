import os
import re

def parse_readme_characters():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    readme_path = os.path.join(base_dir, "README.md")

    if not os.path.exists(readme_path):
        return []

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    table_match = re.search(r"\| Character \| Archetype & MBTI \| Core Emotion \| Personality Profile \| Unique Quality & Philosophy \|\n\|---\|---\|---\|---\|---\|\n(.*?)(?=\n\n|\n---|$)", content, re.DOTALL)

    characters = []
    if table_match:
        table_rows = table_match.group(1).strip().split('\n')
        for row in table_rows:
            cols = [col.strip() for col in row.split('|') if col.strip()]
            if len(cols) == 5:
                characters.append({
                    "name": cols[0],
                    "archetype": cols[1],
                    "core_emotion": cols[2],
                    "personality": cols[3],
                    "philosophy": cols[4]
                })

    return characters
