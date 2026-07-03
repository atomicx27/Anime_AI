import re

def parse_readme_characters(file_path="README.md"):
    characters = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find the markdown table
        table_match = re.search(r"\| Character \|.*?\n\|---\|.*?\n(.*?)(?=\n\n|\Z)", content, re.DOTALL)
        if not table_match:
            return characters

        table_rows = table_match.group(1).strip().split("\n")

        for row in table_rows:
            cols = [col.strip() for col in row.split("|")[1:-1]]
            if len(cols) == 5:
                name = cols[0]
                archetype = cols[1]
                core_emotion = cols[2]
                personality = cols[3]
                unique_quality = cols[4]

                characters.append({
                    "name": name,
                    "archetype": archetype,
                    "core_emotion": core_emotion,
                    "personality": personality,
                    "unique_quality": unique_quality
                })
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")

    return characters
