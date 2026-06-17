import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")

class TestReadmeUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Read the file once per class to reduce I/O (Baseline: 19 openat calls)
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

if __name__ == "__main__":
    unittest.main()
