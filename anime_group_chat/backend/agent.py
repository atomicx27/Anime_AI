import random
import time

class OrchestratorAgent:
    def __init__(self, characters):
        self.recent_responders = []
        self.characters = characters
        self.char_map = {c["name"]: c for c in characters}

    def _generate_mock_response(self, character, prompt, previous_messages=None):
        """Mock LLM response for a specific character based on their traits."""
        core_emotion = character["core_emotion"].split("&")[0].strip()
        quality = character["unique_quality"].split(".")[0]

        # Determine sentiment based on character traits
        if "Desire for Comfort" in character["core_emotion"] or "Calm" in character["core_emotion"]:
            tone = "calmly"
            action = "adjusts glasses"
        elif "Excitement" in character["core_emotion"] or "Fiery" in character["core_emotion"]:
            tone = "excitedly"
            action = "clenches fist"
        elif "Pride" in character["core_emotion"] or "Arrogance" in character["core_emotion"]:
            tone = "proudly"
            action = "crosses arms"
        elif "Grief" in character["core_emotion"] or "Regret" in character["core_emotion"]:
            tone = "solemnly"
            action = "looks away"
        else:
            tone = "thoughtfully"
            action = "nods slowly"

        # Build context from previous messages if any
        context_reaction = ""
        if previous_messages:
            last_msg = previous_messages[-1]
            if last_msg["sender"] != "User":
                context_reaction = f" Addressing {last_msg['sender']}'s point: "

        # Dynamic injection
        dynamic_responses = [
            f"I hear what you're saying about '{prompt[:20]}...'. As someone who believes in {quality}, my perspective is that we must stay true to our path!",
            f"Interesting take on '{prompt[:20]}...'. However, driven by {core_emotion}, I firmly hold that {quality} is the answer.",
            f"When looking at '{prompt[:20]}...', one must consider {quality}. That is the reality of {core_emotion}."
        ]
        chosen_response = random.choice(dynamic_responses)

        return f"*Replies {tone} and {action}* {context_reaction}{chosen_response}"

    def process_group_chat(self, user_message, selected_characters=None):
        """
        Orchestrates a group chat response.
        If selected_characters is None, picks 2-4 random characters to respond.
        """
        if not selected_characters:
            num_responders = random.randint(2, 4)
            available = [c for c in self.characters if c["name"] not in self.recent_responders]
            if len(available) < num_responders:
                available = self.characters # Reset if not enough available
            responders = random.sample(available, min(num_responders, len(available)))
        else:
            # Use specific characters if provided (useful if user tags someone)
            responders = [self.char_map[name] for name in selected_characters if name in self.char_map]
            if not responders:
                available = [c for c in self.characters if c["name"] not in self.recent_responders]
                if len(available) < 2:
                     available = self.characters
                responders = random.sample(available, min(2, len(available)))

        self.recent_responders.extend([r["name"] for r in responders])
        # keep only last 4
        if len(self.recent_responders) > 4:
            self.recent_responders = self.recent_responders[-4:]

        responses = []

        # Add user message to sequence for context
        sequence = [{"sender": "User", "content": user_message}]

        for char in responders:
            # Simulate thinking time
            time.sleep(0.5)

            # Generate character's response
            reply_text = self._generate_mock_response(char, user_message, sequence)

            msg = {
                "id": str(time.time()),
                "sender": char["name"],
                "avatar": char.get("avatar", ""),
                "content": reply_text,
                "timestamp": time.time(),
                "archetype": char["archetype"]
            }

            responses.append(msg)
            sequence.append(msg)

        return responses

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    orchestrator = OrchestratorAgent(chars)

    print("Testing group chat orchestration:")
    responses = orchestrator.process_group_chat("What is the meaning of true strength?")
    for r in responses:
        print(f"\n[{r['sender']}]: {r['content']}")
