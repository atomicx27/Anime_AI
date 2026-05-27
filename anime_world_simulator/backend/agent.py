import random

class WorldSimulatorAgent:
    def __init__(self, characters):
        self.characters = characters

    def _simulate_character_reaction(self, character, scenario):
        """Simulates how a character would react to a given global event or scenario."""
        core_emotion = character["core_emotion"].lower()
        personality = character["personality_profile"].lower()
        quality = character["unique_quality"].lower()
        scenario_lower = scenario.lower()

        # Action states
        action_states = ["Aggressive", "Defensive", "Diplomatic", "Strategic", "Chaotic", "Neutral", "Protective"]

        # Simple heuristic to determine action state based on character traits and scenario
        chosen_state = "Neutral"

        if any(word in core_emotion or word in personality for word in ["combat", "defiance", "arrogance", "pride"]):
            chosen_state = "Aggressive"
        elif any(word in core_emotion or word in personality for word in ["protect", "love", "comfort"]):
            chosen_state = "Protective"
        elif any(word in core_emotion or word in personality for word in ["empathy", "peace", "diplomatic"]):
            chosen_state = "Diplomatic"
        elif any(word in core_emotion or word in personality for word in ["logic", "calm", "regret"]):
            chosen_state = "Strategic"
        elif any(word in core_emotion or word in personality for word in ["despair", "trauma"]):
            chosen_state = "Chaotic"

        # Refine based on scenario
        if "attack" in scenario_lower or "war" in scenario_lower or "fight" in scenario_lower:
            if chosen_state in ["Neutral", "Diplomatic"]:
                chosen_state = "Defensive"
            elif chosen_state == "Aggressive":
                chosen_state = "Aggressive"
        elif "peace" in scenario_lower or "negotiat" in scenario_lower:
            if chosen_state == "Aggressive":
                chosen_state = "Chaotic" # Might disrupt peace

        # Add a slight chance for unpredictability
        if random.random() < 0.15: # 15% chance to act out of character
             alternative_states = [s for s in action_states if s != chosen_state]
             chosen_state = random.choice(alternative_states)

        # Generate strategy/reaction text
        if chosen_state == "Aggressive":
            strategy = f"Charges headfirst into the situation, driven by {character['core_emotion']}. Relies on '{character['unique_quality'].split('.')[0]}' to overpower the challenge."
        elif chosen_state == "Protective":
            strategy = f"Prioritizes the safety of allies and bystanders. Uses '{character['unique_quality'].split('.')[0]}' as a shield against the scenario."
        elif chosen_state == "Diplomatic":
            strategy = f"Attempts to resolve the situation without unnecessary conflict, leveraging their {character['core_emotion']}. Seeks a path of understanding."
        elif chosen_state == "Strategic":
            strategy = f"Analyzes the scenario carefully. Will wait for an opening and apply their '{character['unique_quality'].split('.')[0]}' precisely when needed."
        elif chosen_state == "Chaotic":
            strategy = f"Reacts unpredictably, influenced by {character['core_emotion']}. Might escalate the scenario to achieve their own philosophical goals."
        elif chosen_state == "Defensive":
            strategy = f"Prepares for the worst-case scenario. Solidifies their position and readies their '{character['unique_quality'].split('.')[0]}' for retaliation."
        else:
            strategy = f"Observes the scenario unfolding, relying on their {character['core_emotion']} to guide their next move."

        return {
            "name": character["name"],
            "archetype": character["archetype"],
            "action_state": chosen_state,
            "reaction_strategy": strategy,
            "core_emotion": character["core_emotion"]
        }

    def simulate_world_event(self, scenario):
        """Processes an event and generates reactions for all characters."""
        logs = []
        logs.append(f"World Simulator initializing. Scenario: '{scenario}'")
        logs.append(f"Simulating reactions for {len(self.characters)} characters...")

        reactions = []
        for char in self.characters:
            reactions.append(self._simulate_character_reaction(char, scenario))

        # Group by action state for a summary
        state_counts = {}
        for r in reactions:
            state = r["action_state"]
            state_counts[state] = state_counts.get(state, 0) + 1

        summary = ", ".join([f"{count} {state}" for state, count in state_counts.items()])
        logs.append(f"Simulation complete. World state breakdown: {summary}")

        return {
            "scenario": scenario,
            "reactions": reactions,
            "logs": logs
        }

if __name__ == "__main__":
    from parser import parse_readme_characters
    chars = parse_readme_characters()
    agent = WorldSimulatorAgent(chars)
    res = agent.simulate_world_event("An alien invasion threatens the planet")
    print(f"Results for: {res['scenario']}")
    for r in res['reactions']:
        print(f"[{r['action_state']}] {r['name']} - {r['reaction_strategy']}")
