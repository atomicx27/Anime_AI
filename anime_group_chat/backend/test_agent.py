import unittest
from agent import OrchestratorAgent

class TestAgent(unittest.TestCase):
    def test_orchestrator(self):
        chars = [
            {"name": "Naruto", "core_emotion": "Desire for Acknowledgment", "unique_quality": "Talk no Jutsu", "archetype": "Protagonist"},
            {"name": "Sasuke", "core_emotion": "Desire for Power", "unique_quality": "Sharingan", "archetype": "Rival"},
            {"name": "Sakura", "core_emotion": "Desire for Strength", "unique_quality": "Healing", "archetype": "Heroine"}
        ]
        agent = OrchestratorAgent(chars)
        responses = agent.process_group_chat("Hello")

        self.assertTrue(2 <= len(responses) <= 3)
        self.assertIn("sender", responses[0])
        self.assertIn("content", responses[0])

if __name__ == '__main__':
    unittest.main()
