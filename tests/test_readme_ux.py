import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")

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

class TestCodeOfConductUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        coc_path = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
        with open(coc_path, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_coc_reporting_instructions(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.content)

if __name__ == "__main__":
    unittest.main()
