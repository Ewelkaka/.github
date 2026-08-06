import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestContributingUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_tip_alert_block_present(self):
        """CONTRIBUTING.md should contain a [!TIP] alert block for Resources."""
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("> - [How to Contribute to Open Source]", self.content)

    def test_canonical_style_guide_link(self):
        """CONTRIBUTING.md should use the canonical Style Guide link."""
        canonical_url = "https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide"
        self.assertIn(canonical_url, self.content)
        # Ensure the old link is gone
        old_url = "https://github.com/github/docs/blob/main/contributing/content-style-guide.md"
        self.assertNotIn(old_url, self.content)

if __name__ == "__main__":
    unittest.main()
