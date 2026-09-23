import os
import unittest
from test_pr_accessibility import _read_cached

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")


class TestPaletteUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Read static Markdown files once per class using _read_cached
        cls.coc_content = _read_cached(COC_PATH)
        cls.readme_content = _read_cached(README_PATH)
        cls.contributing_content = _read_cached(CONTRIBUTING_PATH)
        cls.support_content = _read_cached(SUPPORT_PATH)
        cls.content = cls.coc_content

    def test_code_of_conduct_improvements(self):
        # Verify alert block
        self.assertIn("> [!IMPORTANT]", self.coc_content)

        # Verify mailto link
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)

        # Verify placeholder is gone
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)

    def test_readme_localized_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", self.readme_content)

    def test_contributing_localized_coc_link(self):
        self.assertIn("[Contributor Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

    def test_support_typo_fix(self):
        self.assertIn("feature request", self.support_content)
        self.assertNotIn("feaure request", self.support_content)


if __name__ == "__main__":
    unittest.main()
