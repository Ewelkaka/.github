import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestContributingUX(unittest.TestCase):
    def setUp(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_resources_tip_block(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("> - [How to Contribute to Open Source]", self.content)

if __name__ == "__main__":
    unittest.main()
