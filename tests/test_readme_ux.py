import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

class TestReadmeUX(unittest.TestCase):
    def setUp(self):
        with open(README_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("> This repository is not a course.", self.content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.content)
        self.assertIn("[organization profile](profile/README.md)", self.content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.content)

    def test_copyright_year(self):
        self.assertIn("&copy; 2026 GitHub", self.content)

    def test_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

class TestOtherDocsUX(unittest.TestCase):
    def test_support_typo_fixed(self):
        with open(SUPPORT_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("feature request", content)
        self.assertNotIn("feaure request", content)

    def test_coc_alert_and_email(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("> [!IMPORTANT]", content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", content)
        self.assertNotIn("[INSERT CONTACT METHOD]", content)

    def test_contributing_coc_link(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)

if __name__ == "__main__":
    unittest.main()
