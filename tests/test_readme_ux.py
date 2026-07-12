import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestReadmeUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.readme_content = f.read()
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            cls.contributing_content = f.read()
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.coc_content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.readme_content)
        self.assertIn("> This repository is not a course.", self.readme_content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.readme_content)
        self.assertIn("[organization profile](profile/README.md)", self.readme_content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.readme_content)

    def test_localized_coc_links(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

    def test_coc_contact_info(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)

    def test_copyright_year(self):
        self.assertIn("&copy; 2026 GitHub", self.readme_content)

if __name__ == "__main__":
    unittest.main()
