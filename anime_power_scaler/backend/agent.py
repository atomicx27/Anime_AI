import random

class PowerScalerAgent:
    def __init__(self, characters):
        self.characters = {c['name']: c for c in characters}

    def simulate_battle(self, char1_name, char2_name, context="Neutral Arena"):
        if char1_name not in self.characters or char2_name not in self.characters:
            return {"error": "One or both characters not found."}

        char1 = self.characters[char1_name]
        char2 = self.characters[char2_name]

        # Analyze traits to determine scores
        def analyze_combat_potential(char):
            score = 50
            emotion = char['core_emotion'].lower()
            personality = char['personality_profile'].lower()
            quality = char['unique_quality'].lower()
            archetype = char['archetype'].lower()

            if any(word in emotion or word in personality for word in ["combat", "battle", "power", "arrogance", "pride", "domination"]):
                score += 20
            if "protagonist" in archetype:
                score += 10
            if "antagonist" in archetype:
                score += 15
            if any(word in quality for word in ["limitless", "overwhelming", "mastery", "adaptability"]):
                score += 25
            if any(word in emotion or word in personality for word in ["empathy", "peace", "comfort"]):
                score -= 10

            return score

        score1 = analyze_combat_potential(char1)
        score2 = analyze_combat_potential(char2)

        # Introduce some randomness for dynamic battles
        score1 += random.randint(-10, 15)
        score2 += random.randint(-10, 15)

        winner = char1 if score1 >= score2 else char2
        loser = char2 if score1 >= score2 else char1

        logs = []
        logs.append(f"Power Scaler AI initialized.")
        logs.append(f"Matchup: {char1['name']} vs {char2['name']} in {context}.")
        logs.append(f"Analyzing {char1['name']}: Core Emotion - {char1['core_emotion']}.")
        logs.append(f"Analyzing {char2['name']}: Core Emotion - {char2['core_emotion']}.")

        # Determine battle narrative based on traits
        logs.append(f"The battle begins! {char1['name']} approaches with their {char1['personality_profile'].split('.')[0].lower()}.")
        logs.append(f"In response, {char2['name']} leverages their {char2['personality_profile'].split('.')[0].lower()}.")

        # Mid battle clash
        logs.append(f"A massive clash of ideals! {char1['name']} uses '{char1['unique_quality'].split('.')[0]}' against {char2['name']}'s '{char2['unique_quality'].split('.')[0]}'.")

        if score1 == score2:
            winner = None
            logs.append(f"The battle ends in a draw! Both characters counter each other perfectly.")
            summary = f"An absolute stalemate between {char1['name']} and {char2['name']}. Neither could overcome the other's unique qualities."
        else:
            logs.append(f"{winner['name']}'s '{winner['unique_quality'].split('.')[0]}' proves too effective.")
            logs.append(f"{loser['name']} is overwhelmed by {winner['name']}'s {winner['core_emotion']}.")
            summary = f"{winner['name']} wins! Their {winner['core_emotion']} and unique approach '{winner['unique_quality'].split('.')[0]}' outmatched {loser['name']}'s capabilities in this scenario."

        return {
            "char1": char1,
            "char2": char2,
            "winner": winner['name'] if winner else "Draw",
            "logs": logs,
            "summary": summary
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = PowerScalerAgent(chars)
    res = agent.simulate_battle("Naruto Uzumaki", "Son Goku")
    print(res)
