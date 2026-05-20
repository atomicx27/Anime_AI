import unittest
from parser import parse_readme_characters

class TestParser(unittest.TestCase):
    def test_parse_readme_characters(self):
        chars = parse_readme_characters("../../README.md")
        self.assertTrue(len(chars) > 0)
        self.assertIn("name", chars[0])
        self.assertIn("archetype", chars[0])

if __name__ == '__main__':
    unittest.main()
