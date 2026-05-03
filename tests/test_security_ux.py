import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    def setUp(self):
        with open(SECURITY_MD, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_security_warning_alert_present(self):
        """Verify that the security reporting warning uses a GitHub-native alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues", self.content)

if __name__ == "__main__":
    unittest.main()
