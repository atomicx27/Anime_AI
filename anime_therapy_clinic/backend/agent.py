import random

class TherapyAgent:
    def __init__(self, characters):
        self.characters = characters

    def _assign_roles(self):
        """Assign therapy roles based on core emotions and personality traits."""
        roles = {
            "Empathic Listener": None,
            "Tough Love Coach": None,
            "Philosophical Guide": None,
            "Practical Problem Solver": None
        }

        # Shuffle to introduce variety
        shuffled = list(self.characters)
        random.shuffle(shuffled)

        for char in shuffled:
            emotion = char.get("core_emotion", "").lower()
            personality = char.get("personality_profile", "").lower()

            if roles["Empathic Listener"] is None and ("empathy" in emotion or "love" in emotion or "protective" in personality or "comfort" in emotion or "empathic" in personality):
                roles["Empathic Listener"] = char
            elif roles["Tough Love Coach"] is None and ("pride" in emotion or "defiance" in emotion or "stubborn" in personality or "tough" in personality or "arrogant" in personality):
                roles["Tough Love Coach"] = char
            elif roles["Philosophical Guide"] is None and ("logic" in emotion or "regret" in emotion or "wisdom" in personality or "wise" in personality or "philosophy" in char.get("unique_quality", "").lower() or "stoic" in personality):
                roles["Philosophical Guide"] = char
            elif roles["Practical Problem Solver"] is None and ("pragmatic" in personality or "ambition" in emotion or "control" in emotion or "practical" in personality or "calculating" in personality):
                roles["Practical Problem Solver"] = char

            if all(v is not None for v in roles.values()):
                break

        # Fallbacks
        available = [c for c in self.characters if c not in roles.values()]
        for role, char in roles.items():
            if char is None and available:
                roles[role] = available.pop(0)

        return roles

    def _generate_advice(self, role, char, problem):
        """Generate simulated advice based on character traits and assigned role."""
        if not char:
            return "No counselor available for this role."

        emotion = char.get("core_emotion", "")
        quality = char.get("unique_quality", "")

        advice_templates = {
            "Empathic Listener": [
                f"I hear your pain. With my {emotion}, I understand how difficult this is. My approach involves {quality}. I suggest we start by validating your feelings.",
                f"It's okay to feel this way. Guided by my {emotion}, I want you to know you're not alone. We can use {quality} to find a comforting path forward."
            ],
            "Tough Love Coach": [
                f"Stop making excuses! My {emotion} demands action. You need to use {quality} to push through this. No more self-pity!",
                f"Listen closely. Let my {emotion} fuel your resolve. Rely on {quality} to break this cycle. Get up and fight!"
            ],
            "Philosophical Guide": [
                f"Reflect on this deeply. Given my {emotion}, we must consider the broader implications. Applying {quality}, I advise seeking inner balance before acting.",
                f"Every challenge is a lesson. Through the lens of {emotion}, examine your attachments. Use {quality} to attain clarity and peace."
            ],
            "Practical Problem Solver": [
                f"Let's break this down logically. Influenced by my {emotion}, we need a step-by-step plan. Utilizing {quality}, here is your actionable strategy.",
                f"We must be pragmatic. Focus your {emotion} efficiently. By applying {quality}, we can optimize the outcome and resolve this issue."
            ]
        }

        templates = advice_templates.get(role, ["I advise you to stay strong."])
        return random.choice(templates)

    def _generate_resolution(self, problem):
        resolutions = [
            "We recommend a balanced approach: validate your feelings first, then take decisive action.",
            "Take time for introspection, but do not ignore the practical steps needed to move forward.",
            "Combine resilience with empathy. Acknowledge the hardship, but use it as fuel to grow stronger.",
            "Seek out trusted allies while simultaneously working on your own inner peace and adaptability."
        ]
        return random.choice(resolutions)

    def conduct_session(self, problem: str):
        roles = self._assign_roles()

        session_transcript = []
        for role, char in roles.items():
            if char:
                advice = self._generate_advice(role, char, problem)
                session_transcript.append({
                    "role": role,
                    "character_name": char["name"],
                    "character_archetype": char["archetype"],
                    "advice": advice
                })

        resolution = self._generate_resolution(problem)

        return {
            "problem": problem,
            "session_transcript": session_transcript,
            "final_resolution": resolution
        }
