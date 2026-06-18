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
class DebateAgent:
    def __init__(self, characters):
        self.characters = characters

    def select_debaters(self, topic):
        topic_lower = topic.lower()

        # Categorize characters roughly into two opposing views based on their traits
        peace_oriented = []
        conflict_oriented = []

        for char in self.characters:
            core = char["core_emotion"].lower()
            if "peace" in core or "empathy" in core or "love" in core or "diplomacy" in core:
                peace_oriented.append(char)
            else:
                conflict_oriented.append(char)

        # If we couldn't split them well, just pick randomly
        if len(peace_oriented) == 0 or len(conflict_oriented) == 0:
            char1, char2 = random.sample(self.characters, 2)
        else:
            char1 = random.choice(peace_oriented)
            char2 = random.choice(conflict_oriented)

        return char1, char2

    def generate_response(self, character, topic, opponent=None, previous_statement=None):
        """Mock AI response generation based on character traits"""
        core = character["core_emotion"]
        phil = character["unique_quality"]
        name = character["name"]

        if not previous_statement:
            # Opening statement
            templates = [
                f"As someone driven by {core}, my stance on '{topic}' is clear. We must consider that {phil.split('.')[0]}.",
                f"When I look at '{topic}', I filter it through my own experience. {phil.split('.')[0]} is what matters most here.",
                f"Listen to me! If we're talking about '{topic}', you can't ignore the importance of {core}."
            ]
        else:
            # Rebuttal
            templates = [
                f"I hear what {opponent['name']} is saying, but their view ignores {core}. My philosophy of {phil.split('.')[0]} tells a different story.",
                f"That's completely wrong, {opponent['name']}! True understanding of '{topic}' comes from {core}, not whatever you just said.",
                f"Interesting point, but my reliance on {phil.split('.')[0]} proves that we must approach this differently."
            ]

        return random.choice(templates)

    def host_debate(self, topic):
        logs = []
        logs.append(f"Agent initiated. Analyzing debate topic: '{topic}'")

        char1, char2 = self.select_debaters(topic)
        logs.append(f"Selected Debater 1: {char1['name']} ({char1['core_emotion']})")
        logs.append(f"Selected Debater 2: {char2['name']} ({char2['core_emotion']})")

        transcript = []

        # Round 1
        logs.append("Generating Opening Statements...")
        msg1 = self.generate_response(char1, topic)
        transcript.append({"speaker": char1["name"], "message": msg1})

        msg2 = self.generate_response(char2, topic)
        transcript.append({"speaker": char2["name"], "message": msg2})

        # Round 2
        logs.append("Generating Rebuttals...")
        msg3 = self.generate_response(char1, topic, opponent=char2, previous_statement=msg2)
        transcript.append({"speaker": char1["name"], "message": msg3})

        msg4 = self.generate_response(char2, topic, opponent=char1, previous_statement=msg3)
        transcript.append({"speaker": char2["name"], "message": msg4})

        # Conclusion
        logs.append("Debate concluded.")

        return {
            "topic": topic,
            "debater1": char1,
            "debater2": char2,
            "transcript": transcript,
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
    agent = DebateAgent(chars)
    res = agent.host_debate("Is power more important than friendship?")
    print("LOGS:")
    for log in res["logs"]:
        print(log)
    print("\nTRANSCRIPT:")
    for t in res["transcript"]:
        print(f"{t['speaker']}: {t['message']}")
