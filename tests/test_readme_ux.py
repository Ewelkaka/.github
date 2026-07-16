import os
import unittest
from test_pr_accessibility import _read

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")

class TestReadmeUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Read file once per class instead of once per test method.
        # Reduces openat() system calls from O(N_tests) to O(1).
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("> This repository is not a course.", self.content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.content)
        self.assertIn("[organization profile](profile/README.md)", self.content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.content)

    def test_copyright_year(self):
        self.assertIn("&copy; 2026 GitHub", self.content)

    def test_localized_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

class TestSupportUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Use the cached _read helper to prevent duplicate file I/O
        cls.content = _read(SUPPORT_PATH)

    def test_alert_blocks_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("> [!NOTE]", self.content)

    def test_clean_title(self):
        # Ensure no trailing space in title
        self.assertTrue(self.content.startswith("# Support\n"))

    def test_community_forum_link(self):
        self.assertIn("[ask on our community forum](https://github.com/skills/.github/discussions)", self.content)

if __name__ == "__main__":
    unittest.main()
