import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestContributingUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_resource_tip_block_present(self):
        """The Resources section should use a [!TIP] alert block."""
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("**Check out these resources to help you get started:**", self.content)

    def test_resource_links_present(self):
        """The resource links should be present within the document."""
        self.assertIn("[How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)", self.content)
        self.assertIn("[Using Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)", self.content)
        self.assertIn("[GitHub Docs](https://docs.github.com/)", self.content)

if __name__ == "__main__":
    unittest.main()
