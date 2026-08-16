import os
import unittest
from test_pr_accessibility import _read_cached

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")


class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coc_content = _read_cached(COC_PATH)
        cls.readme_content = _read_cached(README_PATH)
        cls.contributing_content = _read_cached(CONTRIBUTING_PATH)
        cls.content = cls.coc_content

    def test_readme_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)

    def test_coc_reporting_instructions(self):
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("opensource-security@github.com", self.coc_content)
        self.assertIn("mailto:opensource-security@github.com", self.coc_content)

    def test_contributing_coc_link(self):
        self.assertIn("CODE_OF_CONDUCT.md", self.contributing_content)


if __name__ == "__main__":
    unittest.main()
