import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")
SECURITY_MD_PATH = os.path.join(REPO_ROOT, "SECURITY.md")
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_alert_block_present(self):
        """Verify that the security warning is formatted as a GitHub alert block."""
    def test_warning_alert_present(self):
        """Verify the semantic warning alert block is present."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

    def test_security_email_present(self):
        """Verify the security reporting email is present."""
        self.assertIn("opensource-security@github.com", self.content)
        with open(SECURITY_MD_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_security_warning_alert_block(self):
        """Verify that the security reporting warning uses a GitHub-native alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.", self.content)

    def test_no_bold_warning(self):
        """Ensure the old bolded warning is removed."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

        """Verify that the warning is no longer just bold text, ensuring the alert block is used instead."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

    def test_security_email_present(self):
        """Verify that the security email is still present in the document."""
        self.assertIn("opensource-security@github.com", self.content)
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_alert_block_present(self):
    def test_warning_alert_present(self):
        """Verify that the security reporting warning is in a [!WARNING] alert block."""
        with open(SECURITY_MD_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_warning_alert_present(self):
        """The security reporting section should use a [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues", self.content)

    def test_mailto_link_present(self):
        """The security email should be a mailto: link for better UX."""
        with open(SECURITY_MD, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_warning_alert_present(self):
        """Verify that the security warning is wrapped in a [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

    def test_mailto_link_present(self):
        """Verify that the security email is a clickable mailto: link."""
        """Verify that the security email is converted to a mailto: link."""
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

if __name__ == "__main__":
    unittest.main()
