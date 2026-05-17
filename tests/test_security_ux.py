import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_MD_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_security_warning_alert_block(self):
        """Verify that the security reporting warning uses a GitHub-native alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.", self.content)

    def test_no_bold_warning(self):
        """Verify that the warning is no longer just bold text, ensuring the alert block is used instead."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

    def test_security_email_present(self):
        """Verify that the security email is still present in the document."""
        self.assertIn("opensource-security@github.com", self.content)

if __name__ == "__main__":
    unittest.main()
