import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")

class TestReadmeUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Suite-wide impact: Redundant openat calls reduced by reading once per class.
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

    # --- Tests for the PR change: setUp -> setUpClass refactor ---

    def test_content_is_class_level_attribute(self):
        """After the setUpClass refactor, content must be stored on the class dict."""
        self.assertIn(
            "content",
            TestReadmeUX.__dict__,
            "'content' should be a class-level attribute set by setUpClass, not just an instance attribute.",
        )

    def test_content_accessible_via_instance(self):
        """Class-level content must be accessible via self in test methods."""
        self.assertIs(
            self.content,
            TestReadmeUX.__dict__["content"],
            "self.content must resolve to the class attribute set by setUpClass.",
        )

    def test_content_is_string(self):
        """The content attribute must be a non-empty string (regression for setUpClass refactor)."""
        self.assertIsInstance(self.content, str)
        self.assertGreater(
            len(self.content),
            0,
            "cls.content must not be empty after setUpClass reads README.md.",
        )

if __name__ == "__main__":
    unittest.main()
