import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.readme_content = f.read()
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            cls.contributing_content = f.read()
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.coc_content = f.read()

    def test_readme_links_to_local_coc(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)

    def test_contributing_links_to_local_coc(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

    def test_coc_has_correct_contact_and_alert(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)

if __name__ == "__main__":
    unittest.main()
