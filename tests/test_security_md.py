"""
Tests for PR changes to SECURITY.md, .jules/bolt.md, and .gitignore.
"""

import os
import re
import unittest
from test_pr_accessibility import _read_cached

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")
BOLT_MD = os.path.join(REPO_ROOT, ".jules", "bolt.md")
GITIGNORE = os.path.join(REPO_ROOT, ".gitignore")


class TestSecurityMdChanges(unittest.TestCase):
    """Tests for SECURITY.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SECURITY_MD)

    def test_file_exists(self):
        """SECURITY.md must exist."""
        self.assertTrue(os.path.isfile(SECURITY_MD), "SECURITY.md does not exist.")

    def test_warning_alert_block_present(self):
        """[!WARNING] alert block must be present in SECURITY.md."""
        self.assertIn("[!WARNING]", self.content)

    def test_mailto_hyperlink_present(self):
        """The mailto: hyperlink for the security email must be present."""
        self.assertIn("mailto:", self.content)

    def test_plain_email_address_present(self):
        """The plain security email address must appear in SECURITY.md."""
        self.assertIn("opensource-security@github.com", self.content)

    def test_reporting_section_heading_present(self):
        """The '## Reporting Security Issues' heading must be present."""
        self.assertIn("## Reporting Security Issues", self.content)


class TestBoltJournalFile(unittest.TestCase):
    """Tests for the .jules/bolt.md file."""

    @classmethod
    def setUpClass(cls):
        cls.path = BOLT_MD
        cls.content = _read_cached(BOLT_MD)

    def test_file_exists(self):
        """.jules/bolt.md must exist in the repository."""
        self.assertTrue(os.path.isfile(self.path), ".jules/bolt.md does not exist.")

    def test_has_bolt_journal_heading(self):
        """The file must contain the title heading."""
        self.assertIn("# Bolt's Journal - Critical Learnings Only", self.content)


class TestGitignorePythonEntries(unittest.TestCase):
    """Tests for Python-related patterns added to .gitignore."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(GITIGNORE)
        cls.lines = cls.content.splitlines()

    def test_pycache_entry_present(self):
        """__pycache__/ must be listed in .gitignore."""
        self.assertIn("__pycache__/", self.lines)

    def test_pyc_glob_pattern_present(self):
        """*.py[cod] must be listed in .gitignore."""
        self.assertIn("*.py[cod]", self.lines)


if __name__ == "__main__":
    unittest.main()
