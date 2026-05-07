import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    def setUp(self):
        with open(SECURITY_MD_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_alert_block_present(self):
        """The security warning should be in an [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.", self.content)

    def test_old_bold_text_absent(self):
        """The old bold version of the warning should no longer be present."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

if __name__ == "__main__":
    unittest.main()
