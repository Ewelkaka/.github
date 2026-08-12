"""
Tests for PR changes to SECURITY.md, .jules/bolt.md, and .gitignore.

Covers:
  - SECURITY.md: removal of [!WARNING] alert block and mailto: hyperlink;
    preservation of plain-text disclaimer and plain email address.
  - .jules/bolt.md: new file with correct heading.
  - .gitignore: addition of Python cache/bytecode patterns.
"""

import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_MD = os.path.join(REPO_ROOT, "SECURITY.md")
BOLT_MD = os.path.join(REPO_ROOT, ".jules", "bolt.md")
GITIGNORE = os.path.join(REPO_ROOT, ".gitignore")


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class TestSecurityMdChanges(unittest.TestCase):
    """Tests for SECURITY.md: [!WARNING] alert block and mailto link removed."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(SECURITY_MD)

    def test_file_exists(self):
        """SECURITY.md must exist."""
        self.assertTrue(os.path.isfile(SECURITY_MD), "SECURITY.md does not exist.")

    def test_no_warning_alert_block(self):
        """[!WARNING] alert block must have been removed from SECURITY.md."""
        self.assertNotIn(
            "[!WARNING]",
            self.content,
            "Found '[!WARNING]' in SECURITY.md; the alert block should have been removed.",
        )

    def test_no_mailto_hyperlink(self):
        """The mailto: hyperlink for the security email must have been removed."""
        self.assertNotIn(
            "mailto:",
            self.content,
            "Found 'mailto:' in SECURITY.md; the hyperlinked email should have been converted to plain text.",
        )

    def test_email_not_as_markdown_link(self):
        """The security email must not appear inside a Markdown link construct."""
        # Match pattern like [text](mailto:...) or [email@domain](mailto:...)
        mailto_link = re.search(
            r"\[.*?\]\(mailto:[^\)]+\)", self.content
        )
        self.assertIsNone(
            mailto_link,
            "Found a Markdown mailto: link in SECURITY.md; the email should be plain text.",
        )

    def test_plain_email_address_present(self):
        """The plain security email address must still appear in SECURITY.md."""
        self.assertIn(
            "opensource-security@github.com",
            self.content,
            "Expected plain email 'opensource-security@github.com' not found in SECURITY.md.",
        )

    def test_plain_bold_disclaimer_present(self):
        """The plain bold disclaimer text must be present."""
        self.assertIn(
            "**Please do not report security vulnerabilities through public GitHub issues",
            self.content,
            "Expected bold disclaimer text not found in SECURITY.md.",
        )

    def test_reporting_section_heading_present(self):
        """The '## Reporting Security Issues' heading must still be present."""
        self.assertIn(
            "## Reporting Security Issues",
            self.content,
            "Expected '## Reporting Security Issues' heading not found in SECURITY.md.",
        )

    def test_coordinated_disclosure_text_present(self):
        """The coordinated disclosure instruction must still be present."""
        self.assertIn(
            "coordinated disclosure",
            self.content,
            "Expected 'coordinated disclosure' text not found in SECURITY.md.",
        )

    def test_alert_block_syntax_absent(self):
        """No blockquote-style GitHub alert block (> [!) must remain."""
        alert_block = re.search(r"^>\s*\[!", self.content, re.MULTILINE)
        self.assertIsNone(
            alert_block,
            "Found a GitHub-style alert block (> [!) in SECURITY.md; all alert blocks should have been removed.",
        )

    def test_email_appears_as_plain_text_not_linked(self):
        """The email must appear as bare text, not as part of a Markdown hyperlink."""
        # Confirm the email is present as plain text (not inside [text](url) syntax)
        plain_pattern = re.search(
            r"(?<!\])\(mailto:\)|(?<!\[)opensource-security@github\.com(?!\))",
            self.content,
        )
        # A simpler check: the email exists AND is not immediately preceded by '](' and 'mailto:'
        self.assertIn("opensource-security@github.com", self.content)
        # The email should not be the URL part of a link: [anything](mailto:opensource-security...)
        linked_email = re.search(
            r"\[[^\]]*\]\(mailto:opensource-security@github\.com\)", self.content
        )
        self.assertIsNone(
            linked_email,
            "Security email must not be a linked mailto: address in SECURITY.md.",
        )


class TestBoltJournalFile(unittest.TestCase):
    """Tests for the newly added .jules/bolt.md file."""

    @classmethod
    def setUpClass(cls):
        cls.path = BOLT_MD
        cls.content = _read(BOLT_MD)

    def test_file_exists(self):
        """.jules/bolt.md must exist in the repository."""
        self.assertTrue(
            os.path.isfile(self.path),
            ".jules/bolt.md does not exist.",
        )

    def test_has_bolt_journal_heading(self):
        """The file must contain the '# Bolt Journal' heading."""
        self.assertIn(
            "# Bolt Journal",
            self.content,
            "Expected '# Bolt Journal' heading not found in .jules/bolt.md.",
        )

    def test_heading_is_h1(self):
        """The heading must be a Markdown H1 (single # prefix)."""
        h1 = re.search(r"^# Bolt Journal", self.content, re.MULTILINE)
        self.assertIsNotNone(
            h1,
            "Expected an H1 heading '# Bolt Journal' in .jules/bolt.md.",
        )

    def test_heading_is_not_h2_or_deeper(self):
        """The heading must not be H2 or deeper (## or more)."""
        wrong_level = re.search(r"^#{2,}\s+Bolt Journal", self.content, re.MULTILINE)
        self.assertIsNone(
            wrong_level,
            "Found 'Bolt Journal' as an H2+ heading; it should be H1.",
        )

    def test_file_is_not_empty(self):
        """.jules/bolt.md must not be empty."""
        self.assertGreater(
            len(self.content.strip()),
            0,
            ".jules/bolt.md is empty.",
        )

    def test_no_unexpected_content_outside_heading(self):
        """The new file should consist of the heading (and optional whitespace only)."""
        # Strip the heading and any surrounding whitespace; remainder should be empty.
        stripped = re.sub(r"^# Bolt Journal\s*", "", self.content.strip())
        self.assertEqual(
            stripped,
            "",
            f".jules/bolt.md contains unexpected content beyond the heading: {stripped!r}",
        )


class TestGitignorePythonEntries(unittest.TestCase):
    """Tests for Python-related patterns added to .gitignore."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(GITIGNORE)
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

    def test_pycache_pattern_exact_format(self):
        """__pycache__/ must include the trailing slash (directory marker)."""
        self.assertTrue(
            any(line == "__pycache__/" for line in self.lines),
            "Expected '__pycache__/' (with trailing slash) in .gitignore.",
        )

    def test_pyc_pattern_uses_character_class(self):
        """*.py[cod] must use a bracket character class, not separate glob lines."""
        # The exact pattern must be *.py[cod], not *.pyc / *.pyo / *.pyd individually
        self.assertIn(
            "*.py[cod]",
            self.lines,
            "Expected character-class glob '*.py[cod]' in .gitignore.",
        )
        # Ensure it is NOT split into three separate lines as a regression check
        self.assertNotIn("*.pyc", self.lines, "Found bare '*.pyc' line; should use *.py[cod] instead.")

    def test_python_entries_in_compiled_source_section(self):
        """The new Python patterns must appear in the 'Compiled source' section."""
        compiled_section_start = next(
            (i for i, line in enumerate(self.lines) if "Compiled source" in line), None
        )
        self.assertIsNotNone(
            compiled_section_start,
            "Could not find 'Compiled source' section header in .gitignore.",
        )
        # Both patterns must appear after the section header
        pycache_idx = next(
            (i for i, line in enumerate(self.lines) if line == "__pycache__/"), None
        )
        pyc_idx = next(
            (i for i, line in enumerate(self.lines) if line == "*.py[cod]"), None
        )
        self.assertIsNotNone(pycache_idx)
        self.assertIsNotNone(pyc_idx)
        self.assertGreater(
            pycache_idx,
            compiled_section_start,
            "'__pycache__/' must appear after the 'Compiled source' section header.",
        )
        self.assertGreater(
            pyc_idx,
            compiled_section_start,
            "'*.py[cod]' must appear after the 'Compiled source' section header.",
        )

    def test_existing_entries_not_removed(self):
        """Adding Python patterns must not have removed any pre-existing .gitignore entries."""
        for entry in ("*.com", "*.class", "*.dll", "*.exe", ".DS_Store"):
            self.assertIn(
                entry,
                self.lines,
                f"Pre-existing .gitignore entry '{entry}' appears to have been removed.",
            )


if __name__ == "__main__":
    unittest.main()
