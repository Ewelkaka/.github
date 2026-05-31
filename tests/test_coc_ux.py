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

    def test_coc_contact_email_present(self):
        """Verify the security email is present as a mailto link in CODE_OF_CONDUCT.md"""
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)

    def test_coc_alert_block_present(self):
        """Verify the Enforcement section in CODE_OF_CONDUCT.md uses an [!IMPORTANT] alert block"""
        self.assertIn("> [!IMPORTANT]", self.coc_content)

    def test_readme_local_coc_link(self):
        """Verify README.md links to the local CODE_OF_CONDUCT.md"""
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)

if __name__ == "__main__":
    unittest.main()
