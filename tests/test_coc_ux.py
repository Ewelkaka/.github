import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestCoCUX(unittest.TestCase):
    def test_readme_local_coc_link(self):
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", content)

    def test_coc_reporting_instructions(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("[INSERT CONTACT METHOD]", content)
        self.assertIn("> [!IMPORTANT]", content)
        self.assertIn("opensource-security@github.com", content)
        self.assertIn("mailto:opensource-security@github.com", content)

    def test_contributing_coc_link(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)

if __name__ == "__main__":
    unittest.main()
