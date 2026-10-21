import random

class AnimeMatchmakerAgent:
    def __init__(self, characters):
        self.characters = characters

    def _evaluate_match(self, character, user_profile, relationship_type):
        """Mock evaluation of a character for a given user profile and relationship type."""
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()
        user_lower = user_profile.lower()

        # Simple keyword matching to influence match score
        score = 0

        # Compatibility logic
        if "introvert" in user_lower and ("quiet" in personality or "stoic" in personality):
            score += 15
        if "extrovert" in user_lower and ("loud" in personality or "boisterous" in personality):
            score += 15

        if "smart" in user_lower or "logic" in user_lower:
            if "logic" in core_emotion or "intelligent" in personality or "calculating" in personality:
                score += 12

        if "adventure" in user_lower or "fun" in user_lower:
            if "excitement" in core_emotion or "hyperactive" in personality:
                score += 12

        if "peace" in user_lower or "chill" in user_lower:
            if "peace" in core_emotion or "easygoing" in personality or "lazy" in personality:
                score += 12

        if "ambition" in user_lower or "driven" in user_lower:
            if "ambition" in core_emotion or "determination" in core_emotion or "competitive" in personality:
                score += 12

        # Relationship type specific scoring
        if relationship_type == "romantic":
            if "love" in core_emotion or "protect" in core_emotion:
                score += 10
            if "arrogance" in core_emotion or "despair" in core_emotion:
                score -= 10 # Usually bad for romance
        elif relationship_type == "rival":
            if "combat" in core_emotion or "ambition" in core_emotion:
                score += 15
            if "pride" in core_emotion or "competitive" in personality:
                score += 10

        # Add some randomness
        score += random.randint(-5, 15)

        if score > 25:
            match_level = "Soulmate / Best Friend"
            reasoning = f"{character['name']} perfectly complements your personality. Your desire for {user_profile} deeply resonates with their {character['core_emotion']}."
        elif score > 15:
            match_level = "Great Match"
            reasoning = f"You and {character['name']} would get along very well. Their {character['personality_profile'].split('.')[0]} aligns with what you're looking for."
        elif score > 5:
            match_level = "Good Friend"
            reasoning = f"{character['name']} is a decent match. You might have some differences given their {character['unique_quality'].split('.')[0]}, but it could work."
        elif score > -5:
            match_level = "Acquaintance"
            reasoning = f"You might struggle to connect with {character['name']}. Their focus on {character['core_emotion']} doesn't perfectly match your vibe."
        else:
            match_level = "Incompatible"
            reasoning = f"This is a terrible match. {character['name']}'s {character['personality_profile'].split('.')[0]} would likely clash heavily with your personality."

        return {
            "name": character["name"],
            "match_level": match_level,
            "score": score,
            "reasoning": reasoning,
            "archetype": character["archetype"]
        }

    def find_matches(self, user_profile, relationship_type="friendship", top_n=5):
        """Evaluates all characters and ranks them as matches for the user."""
        results = []
        logs = []

        logs.append(f"Matchmaker Agent initiated.")
        logs.append(f"Analyzing User Profile: '{user_profile}'")
        logs.append(f"Desired Relationship Type: {relationship_type}")
        logs.append(f"Loaded {len(self.characters)} candidates for assessment.")

        for char in self.characters:
            logs.append(f"Evaluating compatibility with {char['name']}...")

            evaluation = self._evaluate_match(char, user_profile, relationship_type)
            results.append(evaluation)

            logs.append(f"Assessment: {evaluation['match_level']} (Score: {evaluation['score']})")

        # Sort results by score descending
        results.sort(key=lambda x: x["score"], reverse=True)

        # Take top N
        top_results = results[:top_n]

        logs.append(f"Evaluation complete. Found top {top_n} matches.")

        return {
            "user_profile": user_profile,
            "relationship_type": relationship_type,
            "matches": top_results,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = AnimeMatchmakerAgent(chars)
    res = agent.find_matches("I am a chill introvert who likes peace and quiet, but I admire people with strong ambition.", "friendship")
    print(f"Top matches for: {res['user_profile']}")
    for r in res['matches']:
        print(f"[{r['match_level']}] {r['name']}: {r['reasoning']}")
