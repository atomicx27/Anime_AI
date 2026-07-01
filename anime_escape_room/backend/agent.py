class EscapeRoomAgent:
    def __init__(self, characters):
        self.characters = characters

    def _assign_roles(self, scenario):
        assigned = []
        roles = ["Puzzle Solver", "Scout", "Leader", "Muscle"]

        # Simple heuristic to assign roles based on traits
        for char in self.characters:
            role = None
            if "INTJ" in char["archetype"] or "logic" in char["personality_profile"].lower():
                role = "Puzzle Solver"
            elif "hyperactive" in char["personality_profile"].lower() or "speed" in char["unique_quality"].lower():
                role = "Scout"
            elif "ENTJ" in char["archetype"] or "Diplomatic" in char["personality_profile"]:
                role = "Leader"
            elif "physical" in char["unique_quality"].lower() or "combat" in char["core_emotion"].lower():
                role = "Muscle"
            else:
                role = "Support"

            if role in roles or role == "Support":
                assigned.append({
                    "character": char,
                    "role": role
                })

        # Ensure we have a mix, if not just distribute randomly or return all as assigned
        return assigned

    def _generate_action(self, char_assignment, scenario):
        char = char_assignment["character"]
        role = char_assignment["role"]

        if role == "Puzzle Solver":
            action = f"Observes the room's mechanisms carefully, applying cold logic to decrypt the locks blocking their path, channeling their {char['core_emotion']}."
        elif role == "Scout":
            action = f"Quickly maneuvers through the traps, checking for hidden paths and pressure plates, utilizing their {char['unique_quality']}."
        elif role == "Leader":
            action = f"Directs the group to coordinate their efforts, ensuring panic doesn't set in while managing resources, showing their {char['core_emotion']}."
        elif role == "Muscle":
            action = f"Forces a jammed door open or holds up a collapsing ceiling to buy time for the others, relying on their {char['unique_quality']}."
        else:
            action = f"Provides encouragement and watches the team's back, relying on their {char['core_emotion']} to keep morale high."

        return action

    def escape(self, scenario):
        assignments = self._assign_roles(scenario)
        results = []

        for assignment in assignments:
            # We select top 4 characters based on the primary roles to form the core team
            if assignment["role"] != "Support" or len(results) < 4:
                action = self._generate_action(assignment, scenario)
                results.append({
                    "name": assignment["character"]["name"],
                    "avatar": assignment["character"]["avatar"],
                    "role": assignment["role"],
                    "action": action,
                    "philosophy": assignment["character"]["unique_quality"]
                })

        # Limit to 4 for a concise response
        return {"scenario": scenario, "team": results[:4]}
