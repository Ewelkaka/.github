import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_alert_block_present(self):
        """Ensure the security warning is using the GitHub-native alert block syntax."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.", self.content)

    def test_no_bold_warning(self):
        """Ensure the old bold warning is removed."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

if __name__ == "__main__":
    unittest.main()
