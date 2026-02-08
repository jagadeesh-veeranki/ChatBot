import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.prompt_loader import PromptLoader

class TestPromptBehavior(unittest.TestCase):
    def setUp(self):
        self.loader = PromptLoader()
        self.loader.load_prompt()

    def test_load_prompt(self):
        self.assertTrue(len(self.loader.content) > 0)

    def test_layer_integrity(self):
        valid, missing = self.loader.validate_integrity()
        self.assertTrue(valid, f"Missing layers: {missing}")

    def test_identity_layer(self):
        identity = self.loader.get_layer("IDENTITY")
        self.assertIsNotNone(identity)
        self.assertIn("AI agent", identity)
        self.assertIn("Senior AI Engineer", identity)

if __name__ == '__main__':
    unittest.main()
