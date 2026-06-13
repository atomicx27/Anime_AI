import os
import re

def parse_readme_characters():
    """
    Parses the root README.md to extract character data.
    Looks for the Markdown table and parses each row into a dictionary.
    """
    root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    readme_path = os.path.join(root_dir, "README.md")

    characters = []

    if not os.path.exists(readme_path):
        print(f"Warning: README.md not found at {readme_path}")
        return characters

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract the table portion
        # Table starts with | Character | Archetype & MBTI | ...
        table_match = re.search(r"\| Character \|.*?\n\|---\|.*?\n(.*?)(?:\n\n|\n---|$)", content, re.DOTALL)

        if table_match:
            table_body = table_match.group(1).strip()
            rows = table_body.split('\n')

            for row in rows:
                if not row.strip() or not row.startswith('|'):
                    continue

                cols = [col.strip() for col in row.split('|')[1:-1]]
                if len(cols) >= 5:
                    characters.append({
                        "name": cols[0],
                        "archetype": cols[1],
                        "core_emotion": cols[2],
                        "personality_profile": cols[3],
                        "unique_quality": cols[4]
                    })
    except Exception as e:
        print(f"Error parsing README.md: {e}")

    return characters

if __name__ == "__main__":
    chars = parse_readme_characters()
    print(f"Found {len(chars)} characters.")
    for c in chars[:2]:
        print(f"- {c['name']}: {c['core_emotion']}")
