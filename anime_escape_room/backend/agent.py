class EscapeRoomAgent:
    def __init__(self, characters):
        self.characters = characters

    def _assign_roles(self):
        roles = {
            "Leader": None,
            "Codebreaker": None,
            "Brawn": None,
            "Scout": None
        }

        # Simplified assignment logic for demo purposes based on character traits
        for char in self.characters:
            prof = char["personality_profile"].lower()
            arch = char["archetype"].lower()

            if not roles["Leader"] and ("protagonist" in arch or "mentor" in arch):
                roles["Leader"] = char
            elif not roles["Codebreaker"] and ("logic" in char["core_emotion"].lower() or "hyper-intelligent" in prof or "calculating" in prof or "composed" in prof):
                roles["Codebreaker"] = char
            elif not roles["Brawn"] and ("combat" in char["core_emotion"].lower() or "effort" in prof or "destructive" in prof):
                roles["Brawn"] = char
            elif not roles["Scout"] and ("optimistic" in prof or "cheerful" in prof or "reckless" in prof):
                roles["Scout"] = char

        # Fill any unassigned roles with remaining characters
        assigned_names = [char["name"] for char in roles.values() if char]
        unassigned_chars = [char for char in self.characters if char["name"] not in assigned_names]

        for role, char in roles.items():
            if not char and unassigned_chars:
                roles[role] = unassigned_chars.pop(0)

        return roles

    def simulate_escape(self, puzzle_theme):
        roles = self._assign_roles()

        log = [
            f"The team enters the '{puzzle_theme}' escape room.",
            "The door locks behind them. The timer starts ticking.",
            f"\n--- ROOM 1: THE DISCOVERY ---",
            f"{roles['Scout']['name']} dashes ahead, relying on their '{roles['Scout']['unique_quality']}'. They quickly locate a hidden mechanism under the floorboards.",
            f"{roles['Brawn']['name']} forces the mechanism open with raw strength, embodying their '{roles['Brawn']['core_emotion']}'.",
            f"\n--- ROOM 2: THE PUZZLE ---",
            f"A complex cipher blocks the next door. {roles['Codebreaker']['name']} steps up. Using their '{roles['Codebreaker']['unique_quality']}', they logically deduce the sequence in seconds.",
            f"The team is momentarily divided on the next path.",
            f"\n--- THE CLIMAX ---",
            f"{roles['Leader']['name']} rallies everyone, utilizing their '{roles['Leader']['core_emotion']}' to ensure group cohesion.",
            f"Working together, they solve the final riddle and burst through the exit door with seconds to spare!"
        ]

        return {
            "roles": roles,
            "log": log
        }
