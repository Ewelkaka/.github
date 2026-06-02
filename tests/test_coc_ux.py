import os
import unittest
import re

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_reporting_contact_updated(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.content)

    def test_enforcement_alert_block(self):
        # Check for the alert block around the reporting section
        self.assertRegex(self.content, r"> \[!IMPORTANT\]\n> Instances of abusive")

    def test_mailto_link_accessibility(self):
        # Ensure mailto link is used for better UX
        self.assertIn("mailto:opensource-security@github.com", self.content)

if __name__ == "__main__":
    unittest.main()
