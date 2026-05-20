import re
from tools import TOOLS

class AnimeAgent:
    def __init__(self, character_data):
        self.name = character_data.get("name", "Unknown")
        self.archetype = character_data.get("archetype", "Unknown")
        self.core_emotion = character_data.get("core_emotion", "Unknown")
        self.personality_profile = character_data.get("personality_profile", "Unknown")
        self.unique_quality = character_data.get("unique_quality", "Unknown")

        self.system_prompt = self._construct_system_prompt()
        self.tools = TOOLS

    def _construct_system_prompt(self):
        return (
            f"You are {self.name}, an AI agent.\n"
            f"Archetype & MBTI: {self.archetype}\n"
            f"Core Emotion: {self.core_emotion}\n"
            f"Personality Profile: {self.personality_profile}\n"
            f"Unique Quality & Philosophy: {self.unique_quality}\n"
            f"Always stay in character based on the above profile. Do not break character.\n\n"
            f"You have access to the following tools:\n"
            f"1. calculator: Evaluates mathematical expressions. Input: string (e.g., '2 + 2')\n"
            f"2. write_file: Writes content to a file. Input: string (e.g., 'file.txt|content')\n\n"
            f"To use a tool, output exactly:\n"
            f"Thought: [your reasoning here]\n"
            f"Action: [tool_name]\n"
            f"Action Input: [input string for tool]\n\n"
            f"Wait for the Observation, then you can output your Final Answer in the format:\n"
            f"Thought: [your reasoning here]\n"
            f"Final Answer: [your response to the user]\n"
        )

    def _mock_llm_call(self, prompt, history=None):
        """A simple mock LLM for testing without API keys."""
        # Check if the prompt seems to be asking a math question
        if "math" in prompt.lower() or "calculate" in prompt.lower() or "+" in prompt or "*" in prompt:
            # Try to extract the math expression
            match = re.search(r'calculate\s*(.*)', prompt.lower())
            if match:
                expr = match.group(1).strip().replace("?", "")
            else:
                # Default mock expression if we can't parse one
                expr = "10 + 10"
            return f"Thought: I need to use the calculator to answer this.\nAction: calculator\nAction Input: {expr}"

        elif "Observation: " in prompt:
            # We got an observation back, provide a final answer
            obs = prompt.split("Observation: ")[-1]
            return f"Thought: I got the observation: {obs}. I can now give the final answer.\nFinal Answer: The result is {obs}. As {self.name}, I'm glad I could help with my {self.core_emotion}!"

        # Default non-tool response
        return f"Thought: I don't need a tool for this.\nFinal Answer: [{self.name}] I am responding to your message based on my {self.core_emotion} and unique philosophy: {self.unique_quality}!"

    def chat(self, user_message):
        """Implements the ReAct (Reason + Act) loop."""
        # Simple loop for the mock LLM
        max_iterations = 5
        history = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message}
        ]

        output_log = []
        current_prompt = user_message

        for i in range(max_iterations):
            # Call the LLM
            llm_response = self._mock_llm_call(current_prompt, history)

            # Record the raw response
            output_log.append({
                "type": "llm_response",
                "content": llm_response
            })

            # Parse the response for Final Answer
            if "Final Answer:" in llm_response:
                final_answer = llm_response.split("Final Answer:")[1].strip()
                thought = ""
                if "Thought:" in llm_response:
                    thought = llm_response.split("Thought:")[1].split("Final Answer:")[0].strip()

                return {
                    "agent": self.name,
                    "thought": thought,
                    "final_answer": final_answer,
                    "log": output_log
                }

            # Parse the response for Action and Action Input
            thought_match = re.search(r'Thought:(.*?)(?:Action:|Final Answer:|$)', llm_response, re.DOTALL)
            action_match = re.search(r'Action:\s*(.*?)\n', llm_response + "\n")
            action_input_match = re.search(r'Action Input:\s*(.*?)(?:\n|$)', llm_response + "\n")

            if action_match and action_input_match:
                thought = thought_match.group(1).strip() if thought_match else ""
                action_name = action_match.group(1).strip()
                action_input = action_input_match.group(1).strip()

                # Execute the tool
                if action_name in self.tools:
                    observation = self.tools[action_name](action_input)
                else:
                    observation = f"Error: Tool '{action_name}' not found."

                output_log.append({
                    "type": "tool_execution",
                    "tool": action_name,
                    "input": action_input,
                    "observation": observation,
                    "thought": thought
                })

                # Update prompt with the observation
                current_prompt = f"Observation: {observation}"
                history.append({"role": "assistant", "content": llm_response})
                history.append({"role": "user", "content": current_prompt})

            else:
                # Malformed output, break the loop and return what we have
                return {
                    "agent": self.name,
                    "error": "Malformed LLM output. Expected Action or Final Answer.",
                    "log": output_log
                }

        return {
            "agent": self.name,
            "error": "Max iterations reached without finding a Final Answer.",
            "log": output_log
        }

if __name__ == "__main__":
    # Test the chat function
    sample_data = {
        "name": "Naruto Uzumaki",
        "archetype": "Protagonist, ENFP",
        "core_emotion": "Desire for Acknowledgment & Empathy",
        "personality_profile": "Boisterous...",
        "unique_quality": "Talk no Jutsu..."
    }
    agent = AnimeAgent(sample_data)

    print("\n--- Test 1: Simple greeting ---")
    response1 = agent.chat("Hello there!")
    import json
    print(json.dumps(response1, indent=2))

    print("\n--- Test 2: Math query requiring tool ---")
    response2 = agent.chat("Can you calculate 15 * 4?")
    print(json.dumps(response2, indent=2))
