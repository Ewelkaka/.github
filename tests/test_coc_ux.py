import os
import unittest
from test_pr_accessibility import _read_cached

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
README_PATH = os.path.join(REPO_ROOT, "README.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")


class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.coc_content = _read_cached(COC_PATH)
        cls.readme_content = _read_cached(README_PATH)
        cls.contributing_content = _read_cached(CONTRIBUTING_PATH)
        cls.content = cls.coc_content

    def test_reporting_contact_updated(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)

    def test_enforcement_alert_block(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)

    def test_readme_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)

    def test_contributing_coc_link(self):
        self.assertIn("[Contributor Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)


if __name__ == "__main__":
    unittest.main()
