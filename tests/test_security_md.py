"""
Tests for SECURITY.md, .jules/bolt.md, and .gitignore consistency.
"""

import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

from test_pr_accessibility import _read_cached, TrackingTestCase  # noqa: E402

REPO_ROOT = os.path.dirname(TESTS_DIR)
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")
BOLT_MD = os.path.join(REPO_ROOT, ".jules", "bolt.md")
GITIGNORE = os.path.join(REPO_ROOT, ".gitignore")


class TestSecurityMdChanges(TrackingTestCase):
    """Tests for SECURITY.md formatting and reporting email."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SECURITY_MD)

    def test_file_exists(self):
        """SECURITY.md must exist."""
        self.assertTrue(os.path.isfile(SECURITY_MD), "SECURITY.md does not exist.")

    def test_warning_alert_block_present(self):
        """[!WARNING] alert block must be present in SECURITY.md."""
        self.assertIn(
            "[!WARNING]",
            self.content,
            "Expected '[!WARNING]' alert block in SECURITY.md.",
        )

    def test_mailto_hyperlink_present(self):
        """The mailto: hyperlink for the security email must be present."""
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            self.content,
            "Expected mailto link in SECURITY.md.",
        )

    def test_plain_email_address_present(self):
        """The plain security email address must still appear in SECURITY.md."""
        self.assertIn(
            "opensource-security@github.com",
            self.content,
            "Expected plain email 'opensource-security@github.com' in SECURITY.md.",
        )

    def test_reporting_section_heading_present(self):
        """The '## Reporting Security Issues' heading must still be present."""
        self.assertIn(
            "## Reporting Security Issues",
            self.content,
            "Expected '## Reporting Security Issues' heading in SECURITY.md.",
        )

    def test_coordinated_disclosure_text_present(self):
        """The coordinated disclosure instruction must still be present."""
        self.assertIn(
            "coordinated disclosure",
            self.content,
            "Expected 'coordinated disclosure' text in SECURITY.md.",
        )


class TestBoltJournalFile(TrackingTestCase):
    """Tests for the .jules/bolt.md file."""

    @classmethod
    def setUpClass(cls):
        cls.path = BOLT_MD
        cls.content = _read_cached(BOLT_MD)

    def test_file_exists(self):
        """.jules/bolt.md must exist in the repository."""
        self.assertTrue(
            os.path.isfile(self.path),
            ".jules/bolt.md does not exist.",
        )

    def test_has_bolt_journal_heading(self):
        """The file must contain the journal heading."""
        self.assertIn(
            "# Bolt's Journal - Critical Learnings Only",
            self.content,
            "Expected title heading not found in .jules/bolt.md.",
        )

    def test_file_is_not_empty(self):
        """.jules/bolt.md must not be empty."""
        self.assertGreater(
            len(self.content.strip()),
            0,
            ".jules/bolt.md is empty.",
        )


class TestGitignorePythonEntries(TrackingTestCase):
    """Tests for Python-related patterns added to .gitignore."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(GITIGNORE)
        cls.lines = cls.content.splitlines()

    def test_pycache_entry_present(self):
        """__pycache__/ must be listed in .gitignore."""
        self.assertIn(
            "__pycache__/",
            self.lines,
            "'__pycache__/' entry not found in .gitignore.",
        )

    def test_pyc_glob_pattern_present(self):
        """*.py[cod] must be listed in .gitignore."""
        self.assertIn(
            "*.py[cod]",
            self.lines,
            "'*.py[cod]' entry not found in .gitignore.",
        )


if __name__ == "__main__":
    unittest.main()
