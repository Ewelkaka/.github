import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    def setUp(self):
        with open(SECURITY_MD_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_warning_alert_block_present(self):
        """Verify that the security reporting warning is in a GitHub-native [!WARNING] block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.", self.content)

    def test_alert_block_formatting(self):
        """Verify the alert block follows the expected multi-line blockquote format."""
        # Simple check for the block structure
        expected_block = "> [!WARNING]\n> **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**"
        self.assertIn(expected_block, self.content)

if __name__ == "__main__":
    unittest.main()
