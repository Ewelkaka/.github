import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCoCUX(unittest.TestCase):
    def test_readme_link_is_local(self):
        """The README footer should link to the local CODE_OF_CONDUCT.md."""
        with open(README_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](./CODE_OF_CONDUCT.md)", content)
        self.assertNotIn("https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md", content)

    def test_coc_contact_info(self):
        """The Code of Conduct should have the correct security contact email."""
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", content)
        self.assertNotIn("[INSERT CONTACT METHOD]", content)

    def test_coc_alert_block(self):
        """The Enforcement section in CoC should be wrapped in an IMPORTANT alert block."""
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        # Check for the alert block around the enforcement reporting instructions
        self.assertIn("> [!IMPORTANT]", content)
        self.assertRegex(content, r"> Instances of abusive, harassing, or otherwise unacceptable behavior")

if __name__ == "__main__":
    unittest.main()
