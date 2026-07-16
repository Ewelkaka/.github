"""
Tests for the new .jules/bolt.md journal entry.

Covers:
  - .jules/bolt.md: file exists and documents the setUp -> setUpClass
    test-optimization learning/action, following the same conventions used
    for .Jules/palette.md in tests/test_pr_accessibility.py.
"""

import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOLT_MD = os.path.join(REPO_ROOT, ".jules", "bolt.md")


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class TestBoltJournal(unittest.TestCase):
    """Tests for the .jules/bolt.md journal file."""

    @classmethod
    def setUpClass(cls):
        # Read once per class, mirroring the exact optimization this file
        # documents (see .jules/bolt.md itself).
        cls.content = _read(BOLT_MD)

    def test_file_exists(self):
        """.jules/bolt.md must exist in the repository."""
        self.assertTrue(
            os.path.isfile(BOLT_MD),
            ".jules/bolt.md does not exist.",
        )

    def test_file_is_not_empty(self):
        """The journal file must not be empty."""
        self.assertGreater(
            len(self.content.strip()),
            0,
            ".jules/bolt.md is empty.",
        )

    def test_title_heading_present(self):
        """The journal must have the expected top-level title."""
        self.assertIn(
            "# Bolt's Journal - Critical Learnings Only",
            self.content,
            "Expected title heading not found in .jules/bolt.md.",
        )

    def test_contains_dated_entry_heading(self):
        """The entry must include the expected date in its heading."""
        self.assertIn(
            "2026-07-15",
            self.content,
            "Expected date '2026-07-15' not found in .jules/bolt.md.",
        )

    def test_entry_heading_describes_topic(self):
        """The heading must describe the file-I/O reduction topic."""
        self.assertIn(
            "Reduce redundant file I/O in test suites",
            self.content,
            "Expected heading text about reducing redundant file I/O not found.",
        )

    def test_learning_section_present(self):
        """The file must contain a Learning section."""
        self.assertIn(
            "**Learning:**",
            self.content,
            "Expected '**Learning:**' marker not found in .jules/bolt.md.",
        )

    def test_action_section_present(self):
        """The file must contain an Action section."""
        self.assertIn(
            "**Action:**",
            self.content,
            "Expected '**Action:**' marker not found in .jules/bolt.md.",
        )

    def test_learning_mentions_setUp(self):
        """The learning note must reference the setUp() method being replaced."""
        self.assertIn(
            "setUp()",
            self.content,
            "Expected reference to 'setUp()' not found in the Learning section.",
        )

    def test_learning_mentions_setUpClass(self):
        """The learning note must reference the setUpClass optimization."""
        self.assertIn(
            "setUpClass",
            self.content,
            "Expected reference to 'setUpClass' not found in .jules/bolt.md.",
        )

    def test_learning_mentions_unittest(self):
        """The learning note must call out the Python unittest framework."""
        self.assertIn(
            "unittest",
            self.content,
            "Expected reference to 'unittest' not found in the Learning section.",
        )

    def test_action_recommends_setUpClass_for_static_data(self):
        """The action note must instruct preferring setUpClass for static,
        read-only test data."""
        self.assertIn(
            "Always prefer `setUpClass`",
            self.content,
            "Expected explicit recommendation to prefer setUpClass not found "
            "in the Action section of .jules/bolt.md.",
        )
        self.assertIn(
            "read-only test data",
            self.content,
            "Expected reference to 'read-only test data' not found in the "
            "Action section of .jules/bolt.md.",
        )

    def test_directory_is_lowercase_jules(self):
        """The journal must live under the lowercase '.jules' directory,
        distinct from the existing '.Jules' directory used for palette.md."""
        self.assertTrue(
            os.path.isdir(os.path.join(REPO_ROOT, ".jules")),
            "Expected a lowercase '.jules' directory containing bolt.md.",
        )
        self.assertEqual(
            os.path.basename(os.path.dirname(BOLT_MD)),
            ".jules",
        )


if __name__ == "__main__":
    unittest.main()