import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestPaletteUX(unittest.TestCase):
    def test_code_of_conduct_improvements(self):
        path = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Verify alert block
        self.assertIn("> [!IMPORTANT]", content)

        # Verify mailto link
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", content)

        # Verify placeholder is gone
        self.assertNotIn("[INSERT CONTACT METHOD]", content)

    def test_readme_localized_coc_link(self):
        path = os.path.join(REPO_ROOT, "README.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", content)

    def test_contributing_localized_coc_link(self):
        path = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("[Contributor Code of Conduct](CODE_OF_CONDUCT.md)", content)

    def test_support_typo_fix(self):
        path = os.path.join(REPO_ROOT, "SUPPORT.md")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        self.assertIn("feature request", content)
        self.assertNotIn("feaure request", content)

if __name__ == "__main__":
    unittest.main()
