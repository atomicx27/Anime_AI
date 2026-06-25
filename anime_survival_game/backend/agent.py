import random

class SurvivalAgent:
    def __init__(self, characters):
        self.characters = characters

    def evaluate_scenario(self, scenario: str):
        if not self.characters:
            return {"error": "No characters available."}

        # Shuffle for randomness in selection, but keep a copy
        chars = list(self.characters)
        random.shuffle(chars)

        # Select 5 characters for the survival simulation
        participants = chars[:5]

        # Assign roles based on traits
        roles = {
            "Leader": None,
            "Medic/Support": None,
            "Scout": None,
            "Wildcard": None,
            "First Casualty": None
        }

        assigned_chars = set()

        # 1. Leader (Look for ENTJ, INTJ, Protagonist, or high logic/strategy)
        for c in participants:
            if "ENTJ" in c['archetype'] or "INTJ" in c['archetype'] or "Protagonist" in c['archetype'] or "Control" in c['emotion']:
                roles["Leader"] = c
                assigned_chars.add(c['name'])
                break

        # 2. Medic/Support (Look for Empathy, Protection, Love)
        for c in participants:
            if c['name'] not in assigned_chars and ("Empathy" in c['emotion'] or "Protect" in c['emotion'] or "Love" in c['emotion'] or "Peace" in c['emotion']):
                roles["Medic/Support"] = c
                assigned_chars.add(c['name'])
                break

        # 3. Scout (Look for Combat, Speed, Excitement)
        for c in participants:
            if c['name'] not in assigned_chars and ("Combat" in c['emotion'] or "Excitement" in c['emotion'] or "ESFP" in c['archetype']):
                roles["Scout"] = c
                assigned_chars.add(c['name'])
                break

        # 4. Wildcard (Look for Chaos, Despair, Nihilism, Reckless)
        for c in participants:
            if c['name'] not in assigned_chars and ("Despair" in c['emotion'] or "Nihilism" in c['emotion'] or "Reckless" in c['profile'] or "Antagonist" in c['archetype']):
                roles["Wildcard"] = c
                assigned_chars.add(c['name'])
                break

        # Fill remaining roles with remaining characters
        for role in roles:
            if roles[role] is None:
                for c in participants:
                    if c['name'] not in assigned_chars:
                        roles[role] = c
                        assigned_chars.add(c['name'])
                        break

        # Ensure First Casualty is filled if needed, by swapping if it's somehow empty (shouldn't be)
        if roles["First Casualty"] is None:
             for c in participants:
                    if c['name'] not in assigned_chars:
                        roles["First Casualty"] = c
                        assigned_chars.add(c['name'])
                        break

        # Generate Survival Log
        log = []

        leader = roles["Leader"]
        medic = roles["Medic/Support"]
        scout = roles["Scout"]
        wildcard = roles["Wildcard"]
        casualty = roles["First Casualty"]

        log.append(f"Scenario: {scenario}")
        log.append("--- Day 1: The Incident ---")
        log.append(f"{leader['name']} takes charge, driven by their {leader['emotion']}. They organize the group based on their philosophy: '{leader['philosophy'][:50]}...'")
        log.append(f"{scout['name']} immediately goes ahead to scout, motivated by {scout['emotion']}. Their {scout['profile'].split(',')[0].lower()} nature helps them navigate.")

        log.append("--- Day 2: The First Crisis ---")
        log.append(f"A major threat emerges. {casualty['name']}, despite being {casualty['profile'].split(',')[0].lower()}, takes the brunt of the attack. Their philosophy of '{casualty['philosophy'][:50]}...' isn't enough to save them. They are the first casualty.")
        log.append(f"{medic['name']} tries to save them, driven by {medic['emotion']}, but it's too late.")

        log.append("--- Day 3: The Breaking Point ---")
        log.append(f"{wildcard['name']} snaps. Their core emotion of {wildcard['emotion']} takes over. They cause chaos, putting the remaining survivors in danger.")
        log.append(f"{leader['name']} and {wildcard['name']} clash. {leader['name']} relies on their {leader['unique_quality'] if 'unique_quality' in leader else 'skills'} to regain control.")

        log.append("--- Day 4: Resolution ---")
        survivors = [leader['name'], medic['name'], scout['name'], wildcard['name']]
        random.shuffle(survivors)
        final_survivor = survivors[0]

        if final_survivor == wildcard['name']:
            log.append(f"In a shocking twist, {wildcard['name']} is the sole survivor, their {wildcard['profile'].split(',')[0].lower()} nature prevailing against all odds.")
        elif final_survivor == leader['name']:
            log.append(f"{leader['name']} successfully leads themselves to safety, their {leader['emotion']} pushing them through.")
        else:
             log.append(f"{final_survivor} surprisingly makes it out alive, relying on their unique quality: {roles[[k for k, v in roles.items() if v['name'] == final_survivor][0]]['philosophy'][:50]}...")


        return {
            "scenario": scenario,
            "roles": {k: v['name'] for k, v in roles.items() if v},
            "role_details": roles,
            "log": log
        }
