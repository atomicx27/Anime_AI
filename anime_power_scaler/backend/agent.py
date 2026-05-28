class AnimePowerScalerAgent:
    def __init__(self, characters):
        self.characters = characters

    def evaluate_matchup(self, character, custom_ability):
        core_emotion = character.get("core_emotion", "").lower()
        unique_quality = character.get("unique_quality", "").lower()
        custom_ability_lower = custom_ability.lower()

        # Simple logic based on text match length/overlap or generic heuristics to assign Win/Loss/Draw
        words_in_ability = set(custom_ability_lower.split())
        words_in_char = set(core_emotion.split() + unique_quality.split())

        overlap = len(words_in_ability.intersection(words_in_char))

        if "laser" in custom_ability_lower or "destroy" in custom_ability_lower or "power" in custom_ability_lower:
             if "combat" in core_emotion or "adaptability" in unique_quality:
                 result = "Win"
                 explanation = f"{character['name']} uses their {character['core_emotion']} to counter the overwhelming force."
             else:
                 result = "Loss"
                 explanation = f"{character['name']}'s '{character['unique_quality'][:30]}...' is not enough to withstand the ability."
        elif "magic" in custom_ability_lower or "illusion" in custom_ability_lower:
             if "genjutsu" in unique_quality or "anti-magic" in unique_quality:
                 result = "Win"
                 explanation = f"{character['name']} easily negates the ability using their unique traits."
             else:
                 result = "Draw"
                 explanation = f"It's a stalemate. The custom ability creates confusion, but {character['name']} holds their ground."
        else:
             # Fallback based on overlap and generic character strength
             if overlap > 0 or len(custom_ability_lower) < 20:
                 result = "Win"
                 explanation = f"{character['name']} overpowers the straightforward ability with {character['core_emotion']}."
             elif len(custom_ability_lower) > 50:
                 result = "Loss"
                 explanation = f"The complex ability completely counters {character['name']}."
             else:
                 result = "Draw"
                 explanation = f"An even match against {character['name']}."

        return {
            "name": character["name"],
            "result": result,
            "explanation": explanation
        }

    def scale_ability(self, custom_ability):
        results = []
        for char in self.characters:
            results.append(self.evaluate_matchup(char, custom_ability))
        return results

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = AnimePowerScalerAgent(chars)
    res = agent.scale_ability("Laser vision that cuts through anything")
    for r in res:
        print(f"{r['name']}: {r['result']} - {r['explanation']}")
