import random

class VentureCapitalAgent:
    def __init__(self, characters):
        self.characters = characters

    def assign_roles(self):
        pragmatist_pool = []
        visionary_pool = []
        skeptic_pool = []
        wildcard_pool = []

        for char in self.characters:
            core = char["core_emotion"].lower()
            mbti = char["archetype"].lower()
            prof = char["personality_profile"].lower()

            # Pragmatist: logical, calculating, strategic
            if "logic" in core or "pragmatic" in prof or "calculating" in prof or "intj" in mbti or "entj" in mbti:
                pragmatist_pool.append(char)

            # Visionary: hope, ambition, future, potential
            if "hope" in core or "ambition" in core or "potential" in char["unique_quality"].lower() or "enfp" in mbti:
                visionary_pool.append(char)

            # Skeptic: cynical, rules, protection, doubt
            if "cynical" in prof or "protect" in core or "pain" in core or "infj" in mbti:
                skeptic_pool.append(char)

            # Wildcard: reckless, destructive, chaotic, emotional
            if "reckless" in prof or "destructive" in prof or "instinct" in prof or "esfp" in mbti or "7w6" in mbti:
                wildcard_pool.append(char)

        if not pragmatist_pool: pragmatist_pool = self.characters
        if not visionary_pool: visionary_pool = self.characters
        if not skeptic_pool: skeptic_pool = self.characters
        if not wildcard_pool: wildcard_pool = self.characters

        pragmatist = random.choice(pragmatist_pool)
        visionary = random.choice([c for c in visionary_pool if c["name"] != pragmatist["name"]] or visionary_pool)
        skeptic = random.choice([c for c in skeptic_pool if c["name"] not in (pragmatist["name"], visionary["name"])] or skeptic_pool)
        wildcard = random.choice([c for c in wildcard_pool if c["name"] not in (pragmatist["name"], visionary["name"], skeptic["name"])] or wildcard_pool)

        return pragmatist, visionary, skeptic, wildcard

    def generate_feedback(self, character, role, pitch):
        core = character["core_emotion"]
        phil = character["unique_quality"].split(".")[0]
        decision = random.choice(["Invest", "Pass", "Wait & See"])

        if role == "Pragmatist":
            # Pragmatist tends to be Pass or Wait & See, sometimes Invest if good
            decision = random.choice(["Pass", "Pass", "Wait & See", "Invest"])
            templates = [
                f"Analyzing your pitch... my {core} dictates that numbers matter more than dreams. Because of my {phil}, I see too many risks here. Decision: {decision}.",
                f"Your proposal lacks structural integrity. I operate on {phil}, and this doesn't align with my logical {core}. Decision: {decision}."
            ]
        elif role == "Visionary":
            # Visionary tends to Invest
            decision = random.choice(["Invest", "Invest", "Wait & See", "Pass"])
            templates = [
                f"I love the passion! My {core} resonates with what you're trying to build. Through {phil}, I see limitless potential. Decision: {decision}.",
                f"This pitch has spirit! It aligns perfectly with my {core}. Using {phil}, I can see this changing everything. Decision: {decision}."
            ]
        elif role == "Skeptic":
            # Skeptic tends to Pass
            decision = random.choice(["Pass", "Pass", "Wait & See"])
            templates = [
                f"I have seen too many ventures fail. My {core} makes me question your underlying motives. Relying on {phil}, I must decline. Decision: {decision}.",
                f"You paint a pretty picture, but the reality is harsh. My {core} warns me this will end in pain. Based on {phil}. Decision: {decision}."
            ]
        elif role == "Wildcard":
            # Wildcard is completely random
            templates = [
                f"Who cares about the business plan?! This sounds fun! My {core} is fired up! With {phil}, I say let's blow this up! Decision: {decision}.",
                f"I'm bored by the details, but my {core} says go for it! Let's just use {phil} and see what happens! Decision: {decision}."
            ]

        feedback = random.choice(templates)
        return feedback, decision

    def evaluate_pitch(self, pitch):
        logs = []
        logs.append(f"Analyzing pitch: '{pitch}'")

        pragmatist, visionary, skeptic, wildcard = self.assign_roles()

        roles = [
            ("Pragmatist", pragmatist),
            ("Visionary", visionary),
            ("Skeptic", skeptic),
            ("Wildcard", wildcard)
        ]

        evaluations = []
        investments = 0
        passes = 0

        for role_name, char in roles:
            logs.append(f"Assigning {role_name}: {char['name']} ({char['core_emotion']})")
            feedback, decision = self.generate_feedback(char, role_name, pitch)
            evaluations.append({
                "role": role_name,
                "character": char["name"],
                "feedback": feedback,
                "decision": decision
            })
            if decision == "Invest": investments += 1
            elif decision == "Pass": passes += 1

        if investments >= 3:
            final_verdict = "Funded! The council sees great potential."
        elif passes >= 3:
            final_verdict = "Rejected. Try again when you have a real plan."
        else:
            final_verdict = "Mixed feelings. Come back with more data."

        logs.append(f"Final Verdict: {final_verdict}")

        return {
            "pitch": pitch,
            "evaluations": evaluations,
            "final_verdict": final_verdict,
            "logs": logs
        }
