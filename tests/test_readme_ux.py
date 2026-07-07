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

    def test_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

class TestCodeOfConductUX(unittest.TestCase):
    def setUp(self):
        self.coc_path = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
        self.contributing_path = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

        with open(self.coc_path, "r", encoding="utf-8") as f:
            self.coc_content = f.read()
        with open(self.contributing_path, "r", encoding="utf-8") as f:
            self.contributing_content = f.read()

    def test_coc_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)

    def test_contributing_local_coc_link(self):
        self.assertIn("[Contributor Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

if __name__ == "__main__":
    unittest.main()
