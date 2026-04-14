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

class TestDocumentationUX(unittest.TestCase):
    def test_contributing_sequential_numbers(self):
        with open(os.path.join(REPO_ROOT, "CONTRIBUTING.md"), "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("1. Fork and clone the repository", content)
        self.assertIn("2. Create a new branch", content)
        self.assertIn("3. Make your change", content)
        self.assertIn("4. Push to your fork", content)
        self.assertIn("5. Wait for your pull request", content)
        self.assertNotIn("0. Fork and clone the repository", content)

    def test_contributing_alert_block(self):
        with open(os.path.join(REPO_ROOT, "CONTRIBUTING.md"), "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("> [!IMPORTANT]", content)
        self.assertIn("> Please note that this project is released with a Contributor Code of Conduct.", content)

    def test_profile_readme_quoted_attributes(self):
        with open(os.path.join(REPO_ROOT, "profile", "README.md"), "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn('src="https://user-images.githubusercontent.com/1221423/156894097-ff2d6566-7b6a-4488-950e-f4ebe990965a.svg"', content)
        self.assertIn('width="200"', content)
        self.assertIn('align="right"', content)

    def test_support_alert_block(self):
        with open(os.path.join(REPO_ROOT, "SUPPORT.md"), "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("> [!NOTE]", content)
        self.assertIn("> GitHub Skills is under active development", content)

if __name__ == "__main__":
    unittest.main()
