import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCoCUX(unittest.TestCase):
    def setUp(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_enforcement_alert_block(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("Instances of abusive, harassing, or otherwise unacceptable behavior", self.content)

    def test_reporting_email_link(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

if __name__ == "__main__":
    unittest.main()
