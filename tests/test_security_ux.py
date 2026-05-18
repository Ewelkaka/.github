import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_MD, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_warning_alert_block_present(self):
        """Verify that the critical security warning is in a GitHub-native alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.", self.content)

    def test_mailto_link_present(self):
        """Verify that the security email is a mailto: link for better UX."""
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

    def test_no_plain_bold_warning(self):
        """Verify that the warning is not just bold text anymore (improved visual hierarchy)."""
        # The original was **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

if __name__ == "__main__":
    unittest.main()
