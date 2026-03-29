"""
Tests for Palette PR: Use alert block for README disclaimer
"""

import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO_ROOT, "README.md")

def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()

class TestReadmeUX(unittest.TestCase):
    def setUp(self):
        self.content = _read(README)

    def test_alert_block_present(self):
        """README.md should contain a [!NOTE] alert block."""
        self.assertIn("> [!NOTE]", self.content)

    def test_descriptive_link_present(self):
        """README.md should use descriptive links instead of raw URLs."""
        self.assertIn("[skills.github.com](https://skills.github.com)", self.content)
        self.assertNotIn("See https://skills.github.com for", self.content)

if __name__ == "__main__":
    unittest.main()
