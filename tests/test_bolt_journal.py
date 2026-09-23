"""
Tests for the new .jules/bolt.md journal entry.

Covers:
  - .jules/bolt.md: file exists and documents performance learnings
"""

import os
import unittest
from test_pr_accessibility import _read_cached, TrackingTestCase

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOLT_MD = os.path.join(REPO_ROOT, ".jules", "bolt.md")


class TestBoltJournal(TrackingTestCase):
    """Tests for the .jules/bolt.md journal file."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(BOLT_MD)

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


if __name__ == "__main__":
    unittest.main()
