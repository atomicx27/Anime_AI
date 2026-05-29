class PowerScalerAgent:
    def __init__(self, characters):
        self.characters = characters

    def scale_character(self, character, opponent):
        opponent_lower = opponent.lower()
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()

        # Simple keyword matching heuristic
        score = 0
        if any(w in opponent_lower for w in ["god", "universe", "alien", "demon", "king"]):
            if "combat" in core_emotion or "limitless" in quality or "overwhelming" in quality:
                score += 3
            if "defiance" in core_emotion or "grit" in quality:
                score += 2
        if any(w in opponent_lower for w in ["ninja", "magic", "sword", "army", "villain"]):
            if "protect" in core_emotion or "strategic" in personality or "genjutsu" in quality:
                score += 2
            if "passion" in core_emotion or "combat" in core_emotion:
                score += 1
        if any(w in opponent_lower for w in ["peace", "diplomat", "talk", "political"]):
            if "diplomatic" in personality or "empathy" in core_emotion:
                score += 3
            if "arrogance" in core_emotion or "despair" in core_emotion:
                score -= 1

        # Base power check
        if "protagonist" in character["archetype"].lower() or "antagonist" in character["archetype"].lower():
            score += 1

        if score >= 4:
            tier = "Overkill"
            strategy = f"Easily dominates using their {character['core_emotion']}. {character['unique_quality']}"
        elif score >= 2:
            tier = "Even Match"
            strategy = f"Fights on equal footing. Will need to rely on their {character['personality_profile'].split('.')[0].lower()} to find an edge."
        elif score >= 1:
            tier = "Underdog"
            strategy = f"Struggles significantly, but their {character['core_emotion']} gives them a slight chance of a miracle."
        else:
            tier = "Support / Outmatched"
            strategy = f"Cannot win directly. Should focus on supporting allies using their unique philosophy: {character['unique_quality'].split('.')[0]}."

        return {
            "name": character["name"],
            "tier": tier,
            "strategy": strategy,
            "core_emotion": character["core_emotion"]
        }

    def evaluate_opponent(self, opponent):
        results = []
        for char in self.characters:
            results.append(self.scale_character(char, opponent))

        # Sort by tier: Overkill > Even Match > Underdog > Support
        tier_order = {"Overkill": 0, "Even Match": 1, "Underdog": 2, "Support / Outmatched": 3}
        results.sort(key=lambda x: tier_order.get(x["tier"], 4))

        return results

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = PowerScalerAgent(chars)
    res = agent.evaluate_opponent("A Demon Lord with overwhelming magic")
    for r in res[:3]:
        print(f"[{r['tier']}] {r['name']}: {r['strategy']}")
