import time
import random

class ScenarioRankerAgent:
    def __init__(self, characters):
        self.characters = characters

    def _evaluate_character(self, character, scenario):
        """Mock evaluation of a character for a given scenario."""
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()
        scenario_lower = scenario.lower()

        # Simple keyword matching to influence rank
        score = 0
        keywords = {
            "fight": ["combat", "battle", "strength", "power", "protect", "will", "effort", "violence", "war", "martial"],
            "peace": ["peace", "diplomacy", "empathy", "talk", "calm", "understanding", "negotiation", "trade"],
            "smart": ["logic", "intelligent", "calculating", "acumen", "wisdom", "strategy", "politics", "political"],
            "evil": ["control", "despair", "nihilism", "pain", "trauma", "genocidal", "manipulate", "subjugation"],
            "magic": ["magic", "spiritual", "genjutsu", "spell", "illusion", "energy", "dimension"],
            "leadership": ["guild", "lead", "subordinates", "king", "protect", "village", "family"]
        }

        for category, words in keywords.items():
            matches_in_scenario = sum(1 for w in words if w in scenario_lower)
            if category in scenario_lower:
                 matches_in_scenario += 1

            if matches_in_scenario > 0:
                # Diminishing returns for multiple matches in the scenario
                scenario_multiplier = 1.0 + (matches_in_scenario * 0.2)

                for word in words:
                    if word in core_emotion:
                        score += 12 * scenario_multiplier
                    if word in personality:
                        score += 8 * scenario_multiplier
                    if word in quality:
                        score += 10
            # Synergistic scoring: deduct points if category is in scenario but character lacks it
            elif (category in scenario_lower) and not any(w in core_emotion or w in personality or w in quality for w in words):
                score -= 10

        # Add some randomness to make it interesting
        score += random.randint(-5, 15)

        if score > 20:
            rank = "S"
            reasoning = f"{character['name']}'s {character['core_emotion']} perfectly aligns with this scenario. Their {character['unique_quality'].split('.')[0]} gives them a massive advantage."
        elif score > 10:
            rank = "A"
            reasoning = f"{character['name']} would handle this well. Their {character['personality_profile'].split('.')[0]} is well-suited for the challenge."
        elif score > 0:
            rank = "B"
            reasoning = f"{character['name']} is decent here, relying on their {character['unique_quality'].split('.')[0]}, though it's not their ideal situation."
        elif score > -5:
            rank = "C"
            reasoning = f"{character['name']} might struggle slightly. Their focus on {character['core_emotion']} doesn't perfectly match the needs of the scenario."
        else:
            rank = "D"
            reasoning = f"This is a terrible situation for {character['name']}. Their {character['personality_profile'].split('.')[0]} would actively hinder them here."

        return {
            "name": character["name"],
            "rank": rank,
            "reasoning": reasoning
        }

    def rank_scenario(self, scenario):
        """Evaluates all characters and ranks them for the given scenario."""
        results = []
        logs = []

        logs.append(f"Agent initiated evaluation for scenario: '{scenario}'")
        logs.append(f"Loaded {len(self.characters)} characters for assessment.")

        for char in self.characters:
            logs.append(f"Evaluating {char['name']}...")
            logs.append(f"Analyzing traits: {char['archetype']} | Core: {char['core_emotion']}")

            evaluation = self._evaluate_character(char, scenario)
            results.append(evaluation)

            logs.append(f"Decision: Assigned Rank {evaluation['rank']}.")
            logs.append(f"Reasoning: {evaluation['reasoning']}")

        # Sort results S -> D
        rank_order = {"S": 0, "A": 1, "B": 2, "C": 3, "D": 4}
        results.sort(key=lambda x: rank_order[x["rank"]])

        return {
            "scenario": scenario,
            "rankings": results,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = ScenarioRankerAgent(chars)
    res = agent.rank_scenario("A high-stakes diplomatic negotiation to prevent a war")
    print(f"Results for: {res['scenario']}")
    for r in res['rankings']:
        print(f"[{r['rank']}] {r['name']}: {r['reasoning']}")
