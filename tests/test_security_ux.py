import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")

class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_MD, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_warning_alert_present(self):
        """Verify that the security warning is wrapped in a [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> **Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)

    def test_mailto_link_present(self):
        """Verify that the security email is converted to a mailto: link."""
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

if __name__ == "__main__":
    unittest.main()
