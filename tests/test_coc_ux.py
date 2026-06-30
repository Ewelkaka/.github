import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCocUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.readme_content = f.read()
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            cls.contributing_content = f.read()
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.coc_content = f.read()

    def test_readme_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)

    def test_contributing_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

    def test_coc_alert_block(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)

    def test_coc_contact_email(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)

if __name__ == "__main__":
    unittest.main()
