import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")

class TestCoCUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.content)

    def test_reporting_email_present(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

if __name__ == "__main__":
    unittest.main()
