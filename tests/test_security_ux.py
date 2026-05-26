import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_MD, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_warning_alert_block_present(self):
        """Check if the security reporting warning is now an alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.", self.content)

    def test_mailto_link_present(self):
        """Check if the security email is a mailto link."""
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

    def test_old_bold_warning_removed(self):
        """Ensure the old bold-only warning is replaced."""
        self.assertNotIn("**Please do not report security vulnerabilities", self.content)

if __name__ == "__main__":
    unittest.main()
