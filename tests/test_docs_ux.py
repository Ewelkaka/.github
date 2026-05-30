import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestDocsUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SUPPORT_PATH, "r", encoding="utf-8") as f:
            cls.support_content = f.read()
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            cls.contributing_content = f.read()

    def test_support_note_block_present(self):
        self.assertIn("> [!NOTE]", self.support_content)
        self.assertIn("For help or questions about using this project, please [ask on our community forum]", self.support_content)

    def test_contributing_tip_block_present(self):
        self.assertIn("> [!TIP]", self.contributing_content)
        self.assertIn("- [How to Contribute to Open Source]", self.contributing_content)
        self.assertIn("- [Using Pull Requests]", self.contributing_content)
        self.assertIn("- [GitHub Docs]", self.contributing_content)

if __name__ == "__main__":
    unittest.main()
