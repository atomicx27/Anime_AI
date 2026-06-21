import random

class TherapyAgent:
    def __init__(self, characters):
        self.characters = characters

    def assign_roles(self):
        empathetic_pool = []
        tough_love_pool = []
        pragmatic_pool = []

        for char in self.characters:
            core = char["core_emotion"].lower()
            prof = char["personality_profile"].lower()
            mbti = char["archetype"].lower()

            # Empathetic Listener: empathy, hope, love, protect
            if "empathy" in core or "love" in core or "protect" in core or "hope" in core or "enfp" in mbti or "infp" in mbti:
                empathetic_pool.append(char)

            # Tough Love Challenger: combat, defiance, pride, ambition, arrogant, rival
            if "combat" in core or "defiance" in core or "pride" in core or "ambition" in core or "rival" in mbti or "arrogant" in prof:
                tough_love_pool.append(char)

            # Pragmatic Analyst: logic, wisdom, control, calm, intj, entj, mentor
            if "logic" in core or "wisdom" in prof or "control" in core or "calm" in core or "intj" in mbti or "entj" in mbti or "mentor" in mbti:
                pragmatic_pool.append(char)

        if not empathetic_pool: empathetic_pool = self.characters
        if not tough_love_pool: tough_love_pool = self.characters
        if not pragmatic_pool: pragmatic_pool = self.characters

        listener = random.choice(empathetic_pool)

        challenger_candidates = [c for c in tough_love_pool if c["name"] != listener["name"]]
        challenger = random.choice(challenger_candidates) if challenger_candidates else random.choice([c for c in self.characters if c["name"] != listener["name"]])

        analyst_candidates = [c for c in pragmatic_pool if c["name"] not in (listener["name"], challenger["name"])]
        analyst = random.choice(analyst_candidates) if analyst_candidates else random.choice([c for c in self.characters if c["name"] not in (listener["name"], challenger["name"])])

        return {
            "listener": listener,
            "challenger": challenger,
            "analyst": analyst
        }

    def generate_advice(self, role_name, character, struggle):
        core = character["core_emotion"]
        phil = character["unique_quality"].split(".")[0]
        name = character["name"]

        if role_name == "Empathetic Listener":
            templates = [
                f"I hear you. This struggle with {struggle}... it's painful. Driven by {core}, I want you to know you aren't alone. {phil}. We can get through this.",
                f"Your feelings about {struggle} are completely valid. My {core} resonates with what you're going through. Let's use {phil} to heal."
            ]
        elif role_name == "Tough Love Challenger":
            templates = [
                f"Enough making excuses about {struggle}! My {core} demands that you stand up and face it! Channel your frustration into action, just like {phil}!",
                f"You think {struggle} is the end of the world? It's just a hurdle! Fuel yourself with {core} and crush it. Remember: {phil}."
            ]
        elif role_name == "Pragmatic Analyst":
            templates = [
                f"Let's break down {struggle} logically. Emotion aside, driven by {core}, we need a step-by-step plan. Applying {phil}, here is your path forward.",
                f"The issue of {struggle} requires a calculated approach. Guided by {core}, observe the variables. {phil} is the key to resolving this efficiently."
            ]

        return random.choice(templates)

    def provide_therapy(self, struggle):
        logs = []
        logs.append(f"Analyzing patient struggle: '{struggle}'")

        roles = self.assign_roles()

        logs.append(f"Assigned Empathetic Listener: {roles['listener']['name']} ({roles['listener']['core_emotion']})")
        logs.append(f"Assigned Tough Love Challenger: {roles['challenger']['name']} ({roles['challenger']['core_emotion']})")
        logs.append(f"Assigned Pragmatic Analyst: {roles['analyst']['name']} ({roles['analyst']['core_emotion']})")

        advice_list = []

        # Generate Listener Advice
        logs.append(f"Generating Empathetic response from {roles['listener']['name']}...")
        msg1 = self.generate_advice("Empathetic Listener", roles['listener'], struggle)
        advice_list.append({"role": "Empathetic Listener", "character": roles['listener'], "message": msg1})

        # Generate Challenger Advice
        logs.append(f"Generating Tough Love response from {roles['challenger']['name']}...")
        msg2 = self.generate_advice("Tough Love Challenger", roles['challenger'], struggle)
        advice_list.append({"role": "Tough Love Challenger", "character": roles['challenger'], "message": msg2})

        # Generate Analyst Advice
        logs.append(f"Generating Pragmatic response from {roles['analyst']['name']}...")
        msg3 = self.generate_advice("Pragmatic Analyst", roles['analyst'], struggle)
        advice_list.append({"role": "Pragmatic Analyst", "character": roles['analyst'], "message": msg3})

        logs.append("Therapy session synthesis complete.")

        return {
            "struggle": struggle,
            "advice": advice_list,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = TherapyAgent(chars)
    res = agent.provide_therapy("feeling unmotivated to study")
    for log in res["logs"]:
        print(log)
    for adv in res["advice"]:
        print(f"\n[{adv['role']}] {adv['character']['name']}: {adv['message']}")
