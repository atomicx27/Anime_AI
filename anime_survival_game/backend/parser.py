import os

def parse_readme_characters():
    readme_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "README.md")
    characters = []

    if not os.path.exists(readme_path):
        print(f"Error: Could not find README.md at {readme_path}")
        return characters

    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        in_table = False
        for line in lines:
            line = line.strip()
            if line.startswith("| Character |"):
                in_table = True
                continue
            if in_table and line.startswith("|---"):
                continue
            if in_table and line.startswith("|"):
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 6:
                    name = parts[1]
                    archetype = parts[2]
                    emotion = parts[3]
                    profile = parts[4]
                    philosophy = parts[5]
                    characters.append({
                        "name": name,
                        "archetype": archetype,
                        "emotion": emotion,
                        "profile": profile,
                        "philosophy": philosophy
                    })
            if in_table and not line:
                break

        return characters
    except Exception as e:
        print(f"Error parsing README.md: {e}")
        return []
