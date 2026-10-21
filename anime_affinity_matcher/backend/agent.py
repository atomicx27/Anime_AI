import random

class AffinityMatcherAgent:
    def __init__(self, characters):
        self.characters = characters

    def _calculate_affinity(self, user_description: str, character: dict):
        """Calculates an affinity score and category between a user and a character."""
        desc_lower = user_description.lower()
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()

        # Simple keyword matching for affinity scoring
        affinity_score = 0

        # Positive traits that might match
        positive_keywords = ["empathy", "love", "protect", "peace", "cheerful", "effort", "optimistic", "friendly"]
        # Aggressive/ambitious traits
        aggressive_keywords = ["combat", "fight", "power", "ambition", "control", "battle", "pride", "competitive"]
        # Strategic/calm traits
        strategic_keywords = ["calm", "smart", "logic", "diplomatic", "calculating", "wisdom", "quiet"]
        # Tragic/dark traits
        dark_keywords = ["trauma", "pain", "despair", "lonely", "grief", "nihilism", "regret"]

        def score_keywords(keywords, text):
            return sum(1 for kw in keywords if kw in text)

        user_pos = score_keywords(positive_keywords, desc_lower)
        user_agg = score_keywords(aggressive_keywords, desc_lower)
        user_strat = score_keywords(strategic_keywords, desc_lower)
        user_dark = score_keywords(dark_keywords, desc_lower)

        char_text = f"{core_emotion} {personality} {quality}"
        char_pos = score_keywords(positive_keywords, char_text)
        char_agg = score_keywords(aggressive_keywords, char_text)
        char_strat = score_keywords(strategic_keywords, char_text)
        char_dark = score_keywords(dark_keywords, char_text)

        # Calculate a similarity score (higher means more similar)
        similarity = (
            min(user_pos, char_pos) * 2 +
            min(user_agg, char_agg) * 2 +
            min(user_strat, char_strat) * 2 +
            min(user_dark, char_dark) * 2
        )

        # Calculate a difference score (higher means more opposite)
        difference = (
            abs(user_pos - char_pos) +
            abs(user_agg - char_agg) +
            abs(user_strat - char_strat) +
            abs(user_dark - char_dark)
        )

        # Determine category based on similarity and difference
        # Introduce a little randomness to make it fun, but keep it mostly deterministic based on keywords
        random_factor = random.randint(-1, 2)
        similarity += random_factor

        if similarity >= 3 and difference <= 2:
            category = "Soulmate/Best Friend"
            reasoning = f"{character['name']}'s core emotion ({character['core_emotion']}) resonates deeply with your description. You both share similar values and outlooks on life."
        elif similarity >= 2 and difference > 2:
            category = "Rival"
            reasoning = f"You and {character['name']} have some common ground, but your differing approaches (like their {character['personality_profile'].split('.')[0].lower()}) would create a fierce but respectful rivalry."
        elif "mentor" in character["archetype"].lower() or (user_pos == 0 and user_agg == 0 and user_strat == 0 and user_dark == 0):
            # If no clear keywords or they are a mentor archetype
            category = "Mentor"
            reasoning = f"{character['name']} could teach you a lot. Their unique quality ({character['unique_quality'].split('.')[0]}) would provide valuable guidance for your path."
        elif difference > 4 and similarity <= 1:
            category = "Opposite/Enemy"
            reasoning = f"Your worldview clashes completely with {character['name']}. Their focus on {character['core_emotion']} is directly opposed to your stated traits."
        else:
            category = "Acquaintance"
            reasoning = f"You might get along with {character['name']} occasionally, but their {character['personality_profile'].split('.')[0].lower()} means you wouldn't be particularly close."

        return {
            "name": character["name"],
            "archetype": character["archetype"],
            "category": category,
            "reasoning": reasoning,
            "similarity_score": similarity
        }

    def match_user(self, user_description: str):
        """Matches a user description against all characters."""
        matches = []
        logs = []

        logs.append(f"Agent initiated affinity matching for description: '{user_description}'")
        logs.append(f"Analyzing {len(self.characters)} characters for compatibility...")

        for char in self.characters:
            logs.append(f"Evaluating affinity with {char['name']}...")
            match_result = self._calculate_affinity(user_description, char)
            matches.append(match_result)
            logs.append(f"Result: Categorized as {match_result['category']}.")

        # Sort matches by category to group them nicely, or by similarity
        categories_order = {"Soulmate/Best Friend": 0, "Rival": 1, "Mentor": 2, "Acquaintance": 3, "Opposite/Enemy": 4}
        matches.sort(key=lambda x: (categories_order.get(x["category"], 5), -x["similarity_score"]))

        return {
            "matches": matches,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = AffinityMatcherAgent(chars)
    res = agent.match_user("I am very calm, calculating, and prefer diplomacy over fighting. I like peace.")
    for m in res['matches']:
        print(f"[{m['category']}] {m['name']}: {m['reasoning']}")
