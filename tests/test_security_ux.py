import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    def setUp(self):
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_warning_alert_block_present(self):
        """Verify that the security reporting instruction uses a [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues", self.content)
        self.assertIn("opensource-security@github.com", self.content)

    def test_no_bold_warning(self):
        """Verify that the old bold warning has been replaced."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

if __name__ == "__main__":
    unittest.main()
