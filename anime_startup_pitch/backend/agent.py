import random

class StartupPitchAgent:
    def __init__(self, characters):
        self.characters = characters

    def evaluate_pitch(self, pitch_description):
        # We need to assign 4 VC roles
        roles = [
            {"title": "The Visionary Investor", "trait": "Enthusiastic and forward-thinking, focuses on potential and disruption.", "decision_bias": 0.7},
            {"title": "The Pragmatic Critic", "trait": "Focuses on execution, business model, and realistic hurdles.", "decision_bias": 0.4},
            {"title": "The Skeptical Analyst", "trait": "Hyper-analytical, looks for flaws, market size issues, and unit economics.", "decision_bias": 0.2},
            {"title": "The Wildcard", "trait": "Unpredictable, focuses on intuition, emotional resonance, or sheer chaos.", "decision_bias": 0.5}
        ]

        # Select 4 unique characters
        selected_chars = random.sample(self.characters, 4)

        vc_panel = []
        for i, char in enumerate(selected_chars):
            role = roles[i]

            # Simple simulation for decision
            score = random.random()
            decision = "Fund" if score < role["decision_bias"] else "Pass"

            # Generate in-character feedback based on traits
            feedback = self._generate_feedback(char, role, decision, pitch_description)

            vc_panel.append({
                "character_name": char["name"],
                "role": role["title"],
                "core_emotion": char["core_emotion"],
                "decision": decision,
                "feedback": feedback
            })

        return {
            "pitch": pitch_description,
            "panel": vc_panel
        }

    def _generate_feedback(self, char, role, decision, pitch):
        name = char["name"]
        emotion = char["core_emotion"].lower()
        quality = char["unique_quality"]

        if decision == "Fund":
            if "Visionary" in role["title"]:
                return f"As {name}, driven by {emotion}, I see the immense potential here! Your idea resonates with my {quality}. I'm all in, let's change the world!"
            elif "Pragmatic" in role["title"]:
                return f"I'm {name}. It's a solid plan. Your execution strategy aligns with my approach of {quality}. It's risky, but the foundation is there. I'll fund it."
            elif "Skeptical" in role["title"]:
                return f"This is {name}. The numbers barely make sense, but... the underlying mechanics are sound. It reminds me of {quality}. Against my better judgment, I'm in."
            else:
                return f"Hahaha! I am {name}! This is absolute madness, fueled by {emotion}! It's exactly the kind of chaos that fits my {quality}! Take my money!"
        else:
            if "Visionary" in role["title"]:
                return f"I am {name}. While I appreciate the energy, it lacks the true spark of {emotion}. My {quality} tells me this isn't the right path. I have to pass."
            elif "Pragmatic" in role["title"]:
                return f"I'm {name}. The unit economics don't work. It's too idealistic and ignores the reality of {quality}. Come back when you have a real business model. Pass."
            elif "Skeptical" in role["title"]:
                return f"{name} here. Driven by {emotion}? Perhaps. But logically flawed. My {quality} exposes too many vulnerabilities in your pitch. It's a hard pass."
            else:
                return f"I am {name}. Boring. It lacks {emotion}. Where is the thrill? My {quality} rejects this mundane concept. Pass!"
