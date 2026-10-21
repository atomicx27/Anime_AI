import re

def parse_readme_characters(file_path):
    characters = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Find the Character Data Table
        table_start = content.find("| Character | Archetype")
        if table_start == -1:
            return characters

        table_end = content.find("## Projects", table_start)
        if table_end == -1:
            table_end = len(content)

        table_content = content[table_start:table_end]

        # Parse rows
        lines = table_content.strip().split("\n")
        # Skip header and separator
        for line in lines[2:]:
            if not line.strip():
                continue

            # Remove leading/trailing pipes and split
            cols = [col.strip() for col in line.strip().strip("|").split("|")]

            if len(cols) == 5:
                characters.append({
                    "name": cols[0],
                    "archetype": cols[1],
                    "emotion": cols[2],
                    "personality": cols[3],
                    "philosophy": cols[4]
                })

    except Exception as e:
        print(f"Error parsing README.md: {e}")

    return characters

if __name__ == "__main__":
    # Test parser
    import os
    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    readme_path = os.path.join(parent_dir, "README.md")
    chars = parse_readme_characters(readme_path)
    print(f"Found {len(chars)} characters.")
