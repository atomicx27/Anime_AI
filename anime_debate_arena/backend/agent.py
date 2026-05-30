import time
import random

class DebateAgent:
    def __init__(self, characters):
        self.characters = characters

    def _generate_argument(self, character, topic):
        """Generates an argument for a character based on a topic."""
        core_emotion = character["core_emotion"]
        philosophy = character["unique_quality"]
        personality = character["personality_profile"]
        name = character["name"]

        topic_lower = topic.lower()

        # Simple logic to determine their stance based on keywords
        stance = "Neutral"
        agreement_words = ["peace", "love", "friends", "teamwork", "protect", "understanding", "growth"]
        disagreement_words = ["war", "pain", "destruction", "control", "despair", "manipulate", "betrayal"]

        score = 0
        for word in agreement_words:
            if word in topic_lower or word in core_emotion.lower():
                score += 1
        for word in disagreement_words:
            if word in topic_lower or word in core_emotion.lower():
                score -= 1

        # Add personality bias
        if "optimistic" in personality.lower() or "cheerful" in personality.lower():
            score += 1
        if "cynical" in personality.lower() or "cold" in personality.lower():
            score -= 1

        if score > 0:
            stance = "In Favor"
            intro = f"I strongly agree with this."
        elif score < 0:
            stance = "Against"
            intro = f"I cannot accept this."
        else:
            stance = "Nuanced"
            intro = f"This is a complex issue."

        # Template for response
        argument = f"{intro} Driven by my {core_emotion}, I believe that {philosophy.split('.')[0].lower()}. Because I am {personality.split(',')[0].lower()}, my perspective is that we must focus on our core values rather than give in to base impulses."

        # Make it a bit more dynamic
        responses = [
            f"{intro} It all comes down to {core_emotion}. My philosophy is simple: {philosophy} This means in the context of '{topic}', we have to act according to our true nature. Being {personality.split(',')[0].lower()} shapes how I see this.",
            f"When I hear about '{topic}', my immediate reaction is {stance}. My life has been defined by {core_emotion}, and I've learned that {philosophy} I approach this by being {personality.split('and')[0].strip().lower()}.",
            f"I take a {stance} stance here. Why? Because my core drive is {core_emotion}. You see, {philosophy} That's the only way someone like me, who is {personality.split('.')[0].lower()}, can process this."
        ]

        argument = random.choice(responses)

        return {
            "name": name,
            "stance": stance,
            "argument": argument
        }

    def debate_topic(self, topic):
        """Simulates a debate by picking a few random characters to argue the topic."""
        logs = []
        logs.append(f"Debate initialized for topic: '{topic}'")

        # Select 4 random characters to debate
        selected_chars = random.sample(self.characters, min(4, len(self.characters)))

        logs.append(f"Selected debaters: {', '.join([c['name'] for c in selected_chars])}")

        arguments = []
        for char in selected_chars:
            logs.append(f"{char['name']} is preparing their argument based on '{char['core_emotion']}'...")
            time.sleep(0.1) # Simulate thought
            arg = self._generate_argument(char, topic)
            arguments.append(arg)
            logs.append(f"{char['name']} delivered their argument ({arg['stance']}).")

        return {
            "topic": topic,
            "arguments": arguments,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = DebateAgent(chars)
    res = agent.debate_topic("Should we use preemptive strikes against potential threats?")
    print(f"Debate Topic: {res['topic']}\n")
    for arg in res['arguments']:
        print(f"[{arg['stance']}] {arg['name']}: {arg['argument']}\n")