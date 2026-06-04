import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")

class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.coc_content = f.read()
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.readme_content = f.read()

    def test_coc_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)

    def test_coc_contact_method_updated(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)

    def test_readme_coc_link_local(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", self.readme_content)

if __name__ == "__main__":
    unittest.main()
