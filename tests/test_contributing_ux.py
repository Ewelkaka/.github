import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestContributingUX(unittest.TestCase):
    def setUp(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_alert_block_present(self):
        """Verify that the Resources section uses a TIP alert block."""
        self.assertIn("> [!TIP]", self.content)

    def test_resource_links_in_alert_block(self):
        """Verify that resource links are preserved within the alert block."""
        self.assertIn("> - [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)", self.content)
        self.assertIn("> - [Using Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)", self.content)
        self.assertIn("> - [GitHub Docs](https://docs.github.com/)", self.content)

if __name__ == "__main__":
    unittest.main()
