import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    def setUp(self):
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues", self.content)
        self.assertIn("opensource-security@github.com", self.content)

if __name__ == "__main__":
    unittest.main()
