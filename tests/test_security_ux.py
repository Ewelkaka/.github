import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_warning_alert_present(self):
        """Verify the semantic warning alert block is present."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

    def test_security_email_present(self):
        """Verify the security reporting email is present."""
        self.assertIn("opensource-security@github.com", self.content)

if __name__ == "__main__":
    unittest.main()
