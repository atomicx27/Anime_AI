import random

class TherapyAgent:
    def __init__(self, characters):
        self.characters = characters

    def host_session(self):
        if len(self.characters) < 3:
            return {"error": "Not enough characters"}

        selected = random.sample(self.characters, 3)
        therapist = selected[0]
        patient = selected[1]
        observer = selected[2]

        roles = [
            {"role": "Therapist", "character": therapist},
            {"role": "Patient", "character": patient},
            {"role": "Observer", "character": observer}
        ]

        log = []
        log.append({
            "speaker": therapist["name"],
            "role": "Therapist",
            "message": f"Welcome to the clinic. I understand you're dealing with issues related to {patient['core_emotion']}. Let's discuss this.",
            "thought": f"I will guide them using my {therapist['philosophy']} to help them."
        })
        log.append({
            "speaker": patient["name"],
            "role": "Patient",
            "message": f"Yes, my {patient['core_emotion']} and {patient['personality']} make things difficult...",
            "thought": "I hope they understand."
        })
        log.append({
            "speaker": observer["name"],
            "role": "Observer",
            "message": f"Interesting dynamic... Their approaches clash, much like my {observer['core_emotion']}.",
            "thought": f"Observing this through my {observer['philosophy']} perspective."
        })
        log.append({
            "speaker": therapist["name"],
            "role": "Therapist",
            "message": f"I see. Let me help you find a way forward.",
            "thought": "Session proceeding well."
        })

        return {
            "roles": roles,
            "log": log,
            "conclusion": f"The session concludes with {therapist['name']} trying to apply their {therapist['philosophy']} to {patient['name']}'s {patient['core_emotion']}, while {observer['name']} watches closely."
        }
