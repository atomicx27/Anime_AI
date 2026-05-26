import random

class DebateArenaAgent:
    def __init__(self, characters):
        self.characters = characters

    def _evaluate_character(self, character, topic):
        """Evaluates a character's stance on a given debate topic."""
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()
        topic_lower = topic.lower()

        stance = "Neutral"

        # Determine stance based on topic keywords and character traits
        pro_keywords = ["peace", "love", "protect", "empathy", "freedom", "understanding", "growth", "life", "save", "justice"]
        con_keywords = ["control", "power", "war", "destruction", "subjugation", "pain", "trauma", "despair", "nihilism", "death", "force"]

        pro_score = 0
        con_score = 0

        # Check character traits against pro keywords
        for word in pro_keywords:
            if word in core_emotion or word in personality or word in quality:
                pro_score += 1

        # Check character traits against con keywords
        for word in con_keywords:
            if word in core_emotion or word in personality or word in quality:
                con_score += 1

        # Check topic alignment
        is_pro_topic = any(word in topic_lower for word in pro_keywords)
        is_con_topic = any(word in topic_lower for word in con_keywords)

        if is_pro_topic and not is_con_topic:
            if pro_score > con_score:
                stance = "Pro"
            elif con_score > pro_score:
                stance = "Con"
        elif is_con_topic and not is_pro_topic:
            if con_score > pro_score:
                stance = "Pro"
            elif pro_score > con_score:
                stance = "Con"
        else:
            # Topic is ambiguous or contains both, default based on character nature
            if pro_score > con_score + 1:
                stance = "Pro"
            elif con_score > pro_score + 1:
                stance = "Con"
            else:
                stance = random.choice(["Pro", "Con", "Neutral"])

        # Generate argument
        if stance == "Pro":
            argument = f"I strongly support this. Driven by my {character['core_emotion']}, I believe we must rely on '{character['unique_quality'].split('.')[0]}' to see this through for the greater good."
        elif stance == "Con":
            argument = f"I oppose this foolish idea. My philosophy centers on '{character['unique_quality'].split('.')[0]}', and this path only leads to failure or goes against my core beliefs."
        else:
            argument = f"I remain neutral. As long as it doesn't interfere with my {character['core_emotion']} or my goals involving '{character['unique_quality'].split('.')[0]}', I have no strong opinion."

        return {
            "name": character["name"],
            "archetype": character["archetype"],
            "stance": stance,
            "argument": argument,
            "core_emotion": character["core_emotion"]
        }

    def simulate_debate(self, topic):
        """Simulates a debate on the given topic for all characters."""
        logs = []
        logs.append(f"Debate Arena initialized. Topic: '{topic}'")
        logs.append(f"Analyzing stances for {len(self.characters)} participants...")

        evaluations = []
        for char in self.characters:
            evaluations.append(self._evaluate_character(char, topic))

        # Group by stance
        stance_counts = {"Pro": 0, "Con": 0, "Neutral": 0}
        for e in evaluations:
            stance_counts[e["stance"]] += 1

        logs.append(f"Debate concluded. Stances: Pro({stance_counts['Pro']}), Con({stance_counts['Con']}), Neutral({stance_counts['Neutral']})")

        return {
            "topic": topic,
            "evaluations": evaluations,
            "logs": logs,
            "stance_counts": stance_counts
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DebateArenaAgent(chars)
    res = agent.simulate_debate("Should true peace be achieved through absolute control?")
    print(f"Topic: {res['topic']}")
    for e in res['evaluations']:
        print(f"[{e['stance']}] {e['name']}: {e['argument']}")
