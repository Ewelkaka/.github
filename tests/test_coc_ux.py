import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.readme_content = f.read()
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.coc_content = f.read()

    def test_readme_links_locally_to_coc(self):
        """README.md should link to the local CODE_OF_CONDUCT.md file."""
        self.assertIn("[Code of Conduct](./CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", self.readme_content)

    def test_coc_has_important_alert(self):
        """CODE_OF_CONDUCT.md should have an [!IMPORTANT] alert block in Enforcement section."""
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("Instances of abusive, harassing, or otherwise unacceptable behavior", self.coc_content)

    def test_coc_has_correct_email_link(self):
        """CODE_OF_CONDUCT.md should have the correct mailto link for reporting."""
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)

if __name__ == "__main__":
    unittest.main()
