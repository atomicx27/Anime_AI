import random

class CourtroomAgent:
    def __init__(self, characters):
        self.characters = characters

    def assign_roles(self):
        judge_pool = []
        prosecutor_pool = []
        defense_pool = []

        for char in self.characters:
            core = char["core_emotion"].lower()
            mbti = char["archetype"].lower()
            prof = char["personality_profile"].lower()

            # Judge traits: logic, peace, wisdom, rules, control
            if "logic" in core or "peace" in core or "wisdom" in prof or "control" in core or "intj" in mbti or "infj" in mbti:
                judge_pool.append(char)

            # Prosecutor traits: ambition, justice, duty, conflict, cynical
            if "ambition" in core or "justice" in core or "duty" in core or "cynical" in prof or "entj" in mbti or "antagonist" in mbti:
                prosecutor_pool.append(char)

            # Defense traits: empathy, protection, hope, love
            if "empathy" in core or "protect" in core or "hope" in core or "love" in core or "enfp" in mbti or "infp" in mbti:
                defense_pool.append(char)

        # Fallback to random if empty
        if not judge_pool: judge_pool = self.characters
        if not prosecutor_pool: prosecutor_pool = self.characters
        if not defense_pool: defense_pool = self.characters

        judge = random.choice(judge_pool)

        prosecutor = random.choice([c for c in prosecutor_pool if c["name"] != judge["name"]]) if len(prosecutor_pool) > 1 else random.choice([c for c in self.characters if c["name"] != judge["name"]])

        defense = random.choice([c for c in defense_pool if c["name"] not in (judge["name"], prosecutor["name"])]) if len(defense_pool) > 2 else random.choice([c for c in self.characters if c["name"] not in (judge["name"], prosecutor["name"])])

        return judge, prosecutor, defense

    def generate_statement(self, character, role, crime, phase):
        core = character["core_emotion"]
        phil = character["unique_quality"].split(".")[0]

        if phase == "opening_prosecutor":
            templates = [
                f"The defendant is accused of {crime}. Driven by {core}, I see this as an absolute violation of order. My approach of {phil} demands strict punishment.",
                f"As Prosecutor, I must address this offense: {crime}. Because my philosophy involves {phil}, I cannot let this slide. {core} compells me to seek justice."
            ]
        elif phase == "opening_defense":
            templates = [
                f"My client is accused of {crime}, but let us look deeper. Influenced by {core}, I urge the court to consider the circumstances. Using {phil}, I see hope for redemption.",
                f"The charge of {crime} is severe, yes. However, guided by {core}, we must understand the pain behind the action. {phil} is the key here."
            ]
        elif phase == "rebuttal_prosecutor":
            templates = [
                f"The defense speaks of redemption, but what of the victims of {crime}? My {core} will not be swayed by such naive ideals.",
                f"Objection! The defense's reliance on empathy ignores the harsh reality. {phil} proves that consequences are necessary."
            ]
        elif phase == "rebuttal_defense":
            templates = [
                f"The prosecution is too rigid! If we only punish for {crime} without understanding, the cycle of hatred continues. My {core} refuses that outcome.",
                f"Objection! You're focusing only on the act, not the person. My {phil} allows me to see the potential for change."
            ]
        elif phase == "verdict":
            # Judge's verdict
            templates = [
                f"I have heard both sides regarding the charge of {crime}. Balancing the arguments with my {core}, and applying my wisdom of {phil}, I find the defendant... Guilty, but with room for atonement.",
                f"Order in the court! The charge of {crime} has been debated. Guided by {core}, and my principle of {phil}, I decree the defendant... Not Guilty due to extenuating circumstances."
            ]

        return random.choice(templates)

    def host_trial(self, crime):
        logs = []
        logs.append(f"Agent initiated. Analyzing trial for crime: '{crime}'")

        judge, prosecutor, defense = self.assign_roles()
        logs.append(f"Selected Judge: {judge['name']} ({judge['core_emotion']})")
        logs.append(f"Selected Prosecutor: {prosecutor['name']} ({prosecutor['core_emotion']})")
        logs.append(f"Selected Defense Attorney: {defense['name']} ({defense['core_emotion']})")

        transcript = []

        # Prosecutor Opening
        logs.append("Generating Prosecutor Opening Statement...")
        msg1 = self.generate_statement(prosecutor, "Prosecutor", crime, "opening_prosecutor")
        transcript.append({"speaker": prosecutor["name"], "role": "Prosecutor", "message": msg1})

        # Defense Opening
        logs.append("Generating Defense Opening Statement...")
        msg2 = self.generate_statement(defense, "Defense Attorney", crime, "opening_defense")
        transcript.append({"speaker": defense["name"], "role": "Defense Attorney", "message": msg2})

        # Prosecutor Rebuttal
        logs.append("Generating Prosecutor Rebuttal...")
        msg3 = self.generate_statement(prosecutor, "Prosecutor", crime, "rebuttal_prosecutor")
        transcript.append({"speaker": prosecutor["name"], "role": "Prosecutor", "message": msg3})

        # Defense Rebuttal
        logs.append("Generating Defense Rebuttal...")
        msg4 = self.generate_statement(defense, "Defense Attorney", crime, "rebuttal_defense")
        transcript.append({"speaker": defense["name"], "role": "Defense Attorney", "message": msg4})

        # Verdict
        logs.append("Generating Judge Verdict...")
        msg5 = self.generate_statement(judge, "Judge", crime, "verdict")
        transcript.append({"speaker": judge["name"], "role": "Judge", "message": msg5})

        logs.append("Trial concluded.")

        return {
            "crime": crime,
            "judge": judge,
            "prosecutor": prosecutor,
            "defense": defense,
            "transcript": transcript,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = CourtroomAgent(chars)
    res = agent.host_trial("Stealing a sweetroll")
    print("LOGS:")
    for log in res["logs"]:
        print(log)
    print("\nTRANSCRIPT:")
    for t in res["transcript"]:
        print(f"[{t['role']}] {t['speaker']}: {t['message']}")
