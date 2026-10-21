import random

class LifeCoachAgent:
    def __init__(self, characters):
        self.characters = characters
        self.roles = ["Motivational", "Strategic", "Empathetic", "Tough Love"]

    def assign_coaches(self, problem_description):
        assigned_coaches = []
        available_chars = list(self.characters)

        # Logic for assigning Motivational
        motivational_candidates = [c for c in available_chars if any(word in c['core_emotion'].lower() or word in c['personality_profile'].lower() for word in ['optimistic', 'passion', 'determination', 'hope'])]
        if not motivational_candidates:
            motivational_candidates = available_chars
        motivational_coach = random.choice(motivational_candidates)
        available_chars.remove(motivational_coach)

        # Logic for assigning Strategic
        strategic_candidates = [c for c in available_chars if any(word in c['archetype'].lower() or word in c['personality_profile'].lower() for word in ['intj', 'entj', 'logic', 'calculating', 'pragmatic'])]
        if not strategic_candidates:
            strategic_candidates = available_chars
        strategic_coach = random.choice(strategic_candidates)
        available_chars.remove(strategic_coach)

        # Logic for assigning Empathetic
        empathetic_candidates = [c for c in available_chars if any(word in c['core_emotion'].lower() or word in c['personality_profile'].lower() for word in ['empathy', 'love', 'comfort', 'diplomatic', 'infj', 'infp'])]
        if not empathetic_candidates:
            empathetic_candidates = available_chars
        empathetic_coach = random.choice(empathetic_candidates)
        available_chars.remove(empathetic_coach)

        # Logic for assigning Tough Love
        tough_love_candidates = [c for c in available_chars if any(word in c['core_emotion'].lower() or word in c['personality_profile'].lower() for word in ['pride', 'stubborn', 'defiance', 'arrogance'])]
        if not tough_love_candidates:
            tough_love_candidates = available_chars
        tough_love_coach = random.choice(tough_love_candidates)
        available_chars.remove(tough_love_coach)

        def generate_advice(coach, role, problem):
            name = coach['name']
            quality = coach['unique_quality']
            emotion = coach['core_emotion']

            if role == "Motivational":
                return f"Listen up! I know things seem tough with '{problem[:20]}...', but you can't give up! My core drive is {emotion}, and I believe you have the strength to push through. {quality.split('.')[0]}. Let's go!"
            elif role == "Strategic":
                return f"Let's analyze your situation regarding '{problem[:20]}...'. Acting on impulse will only lead to failure. My approach relies on {emotion}. You need to step back, assess your resources, and form a concrete plan. Remember: {quality.split('.')[0]}."
            elif role == "Empathetic":
                return f"I hear your struggles with '{problem[:20]}...'. It's okay to feel overwhelmed. I understand the weight of {emotion}. Take a deep breath. {quality.split('.')[0]}. I'm here to support you."
            elif role == "Tough Love":
                return f"Stop making excuses about '{problem[:20]}...'! You're only holding yourself back. I had to fight for my {emotion}. If you want to change, you need to put in the work, period. {quality.split('.')[0]}!"

        assigned_coaches.append({
            "role": "Motivational",
            "character": motivational_coach,
            "advice": generate_advice(motivational_coach, "Motivational", problem_description)
        })

        assigned_coaches.append({
            "role": "Strategic",
            "character": strategic_coach,
            "advice": generate_advice(strategic_coach, "Strategic", problem_description)
        })

        assigned_coaches.append({
            "role": "Empathetic",
            "character": empathetic_coach,
            "advice": generate_advice(empathetic_coach, "Empathetic", problem_description)
        })

        assigned_coaches.append({
            "role": "Tough Love",
            "character": tough_love_coach,
            "advice": generate_advice(tough_love_coach, "Tough Love", problem_description)
        })

        logs = []
        logs.append(f"Analyzing user problem: '{problem_description}'...")
        logs.append(f"Assigning Motivational role to {motivational_coach['name']} based on traits...")
        logs.append(f"Assigning Strategic role to {strategic_coach['name']} based on logical profile...")
        logs.append(f"Assigning Empathetic role to {empathetic_coach['name']} for emotional support...")
        logs.append(f"Assigning Tough Love role to {tough_love_coach['name']} for reality check...")
        logs.append(f"All coaches assigned successfully.")

        return {
            "coaches": assigned_coaches,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = LifeCoachAgent(chars)
    res = agent.assign_coaches("I feel stuck in my career and I don't know what to do next.")
    import json
    print(json.dumps(res, indent=2))
