import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_security_warning_alert_block(self):
        """Verify that the security report warning is in a [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> Please do not report security vulnerabilities through public GitHub issues", self.content)

    def test_no_bold_warning(self):
        """Verify that the old bold warning is removed."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues", self.content)

if __name__ == "__main__":
    unittest.main()
