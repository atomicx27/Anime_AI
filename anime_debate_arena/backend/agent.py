import random

class DebateArenaAgent:
    def __init__(self, characters):
        self.characters = characters

    def _select_debaters(self, topic):
        # We'll randomly select two characters with different core emotions to debate, and one to judge.
        shuffled = list(self.characters)
        random.shuffle(shuffled)

        char1 = shuffled[0]
        char2 = shuffled[1]
        judge = shuffled[2]

        return char1, char2, judge

    def _generate_argument(self, character, topic, opponent=None, is_rebuttal=False):
        """Generates a character's argument based on their traits."""
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"]

        style = "passionately"
        if any(word in core_emotion or word in personality for word in ["logic", "calm", "regret", "cold"]):
            style = "logically and coldly"
        elif any(word in core_emotion or word in personality for word in ["arrogance", "pride"]):
            style = "arrogantly"
        elif any(word in core_emotion or word in personality for word in ["empathy", "peace", "diplomatic"]):
            style = "diplomatically and empathetically"

        arg_type = "Rebuttal" if is_rebuttal else "Opening Statement"

        text = f"Speaking {style}, {character['name']} argues based on their core emotion of '{character['core_emotion']}'. "

        if is_rebuttal and opponent:
            text += f"They dismiss {opponent['name']}'s point, "

        text += f"applying their philosophy: '{quality}' to the topic of '{topic}'."

        return {
            "speaker": character["name"],
            "archetype": character["archetype"],
            "type": arg_type,
            "text": text
        }

    def _generate_judgment(self, judge, char1, char2, topic):
        """Generates the judge's final verdict."""
        core_emotion = judge["core_emotion"].lower()
        personality = judge["personality_profile"].lower()
        quality = judge["unique_quality"]

        winner = random.choice([char1, char2])

        text = f"{judge['name']} steps in to judge the debate. Filtering the arguments through their core emotion of '{judge['core_emotion']}' and their unique quality: '{quality}', "
        text += f"they conclude that {winner['name']}'s perspective is more compelling regarding '{topic}'."

        return {
            "speaker": judge["name"],
            "archetype": judge["archetype"],
            "type": "Verdict",
            "text": text,
            "winner": winner["name"]
        }

    def simulate_debate(self, topic):
        """Simulates a full debate on a given topic."""
        logs = []
        logs.append(f"Debate Arena initializing. Topic: '{topic}'")

        char1, char2, judge = self._select_debaters(topic)

        logs.append(f"Debaters selected: {char1['name']} vs {char2['name']}. Judge: {judge['name']}")

        script = []

        # Opening Statements
        script.append(self._generate_argument(char1, topic))
        script.append(self._generate_argument(char2, topic))

        # Rebuttals
        script.append(self._generate_argument(char1, topic, opponent=char2, is_rebuttal=True))
        script.append(self._generate_argument(char2, topic, opponent=char1, is_rebuttal=True))

        # Verdict
        verdict = self._generate_judgment(judge, char1, char2, topic)
        script.append(verdict)

        logs.append(f"Debate concluded. Winner: {verdict['winner']}")

        return {
            "topic": topic,
            "char1": char1,
            "char2": char2,
            "judge": judge,
            "script": script,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DebateArenaAgent(chars)
    res = agent.simulate_debate("Should humanity embrace AI?")
    print(f"Topic: {res['topic']}")
    for line in res['script']:
        print(f"\n[{line['type']}] {line['speaker']}: {line['text']}")
