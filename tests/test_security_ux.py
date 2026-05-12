"""
Tests for PR: Enhance security warnings with native alert blocks

Covers:
  - SECURITY.md: bold warning replaced with > [!WARNING] alert block
  - .Jules/palette.md: new 2026-05-12 entry documenting the warning-block pattern
"""

import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")
PALETTE_MD = os.path.join(REPO_ROOT, ".Jules", "palette.md")


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class TestSecurityUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(SECURITY_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_security_warning_alert_block(self):
        """Verify that the security report warning is in a [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn("> Please do not report security vulnerabilities through public GitHub issues", self.content)

    def test_no_bold_warning(self):
        """Verify that the old bold warning is removed."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues", self.content)


class TestSecurityMdStructure(unittest.TestCase):
    """Structural tests for the [!WARNING] alert block change in SECURITY.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(SECURITY_PATH)
        cls.lines = cls.content.splitlines()

    def test_warning_block_uses_warning_type(self):
        """The alert block must use the [!WARNING] type, not [!CAUTION] or [!IMPORTANT]."""
        self.assertIn(
            "> [!WARNING]",
            self.content,
            "Expected '> [!WARNING]' not found; the warning must use the WARNING alert type.",
        )
        # Guard against accidentally using a different alert type
        self.assertNotIn(
            "> [!CAUTION]",
            self.content,
            "Found '> [!CAUTION]' in SECURITY.md; the warning should use [!WARNING].",
        )
        self.assertNotIn(
            "> [!IMPORTANT]",
            self.content,
            "Found '> [!IMPORTANT]' in SECURITY.md; the warning should use [!WARNING].",
        )

    def test_warning_block_content_line_prefixed(self):
        """The warning text must be a blockquote line (prefixed with '> ')."""
        self.assertIn(
            "> Please do not report security vulnerabilities",
            self.content,
            "Warning text is not prefixed with '> '; it must be part of the blockquote.",
        )

    def test_warning_block_consecutive_lines(self):
        """The [!WARNING] marker and the warning text must appear on consecutive lines."""
        warning_marker_idx = None
        for i, line in enumerate(self.lines):
            if line.strip() == "> [!WARNING]":
                warning_marker_idx = i
                break
        self.assertIsNotNone(
            warning_marker_idx,
            "Could not find '> [!WARNING]' line in SECURITY.md.",
        )
        next_line = self.lines[warning_marker_idx + 1] if warning_marker_idx + 1 < len(self.lines) else ""
        self.assertTrue(
            next_line.startswith("> "),
            f"Line after '> [!WARNING]' must be a blockquote continuation; got: {next_line!r}",
        )

    def test_warning_covers_full_message(self):
        """The warning text must mention issues, discussions, and pull requests."""
        self.assertIn(
            "discussions, or pull requests",
            self.content,
            "Warning text is missing 'discussions, or pull requests'.",
        )

    def test_warning_block_appears_exactly_once(self):
        """The [!WARNING] block should appear exactly once to avoid duplication."""
        count = self.content.count("> [!WARNING]")
        self.assertEqual(
            count,
            1,
            f"Expected exactly one '> [!WARNING]' block, found {count}.",
        )

    def test_email_address_preserved(self):
        """The contact email address must still be present after the warning block."""
        self.assertIn(
            "opensource-security@github.com",
            self.content,
            "Contact email 'opensource-security@github.com' is missing from SECURITY.md.",
        )

    def test_reporting_section_heading_present(self):
        """The 'Reporting Security Issues' section heading must be preserved."""
        self.assertIn(
            "## Reporting Security Issues",
            self.content,
            "'## Reporting Security Issues' heading missing from SECURITY.md.",
        )

    def test_no_bare_bold_security_warnings(self):
        """No security-critical instructions must remain as bare bold text (regression guard)."""
        # Bold text matching the old pattern should not exist anywhere in the file
        bold_warning = re.search(
            r"\*\*Please do not report security vulnerabilities",
            self.content,
        )
        self.assertIsNone(
            bold_warning,
            "Found a bold-text security warning that should have been converted to an alert block.",
        )


class TestPaletteSecurityEntry(unittest.TestCase):
    """Tests for the new 2026-05-12 entry added to .Jules/palette.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(PALETTE_MD)

    def test_new_entry_date_heading_present(self):
        """The 2026-05-12 palette entry must be present as a heading."""
        self.assertIn(
            "## 2026-05-12",
            self.content,
            "Expected '## 2026-05-12' heading not found in .Jules/palette.md.",
        )

    def test_new_entry_heading_describes_security_warnings(self):
        """The 2026-05-12 heading must describe the security warning pattern."""
        self.assertIn(
            "security",
            self.content.lower(),
            "Expected 'security' keyword not found in .Jules/palette.md.",
        )

    def test_new_entry_references_warning_alert_type(self):
        """The new entry must document the [!WARNING] alert block pattern."""
        self.assertIn(
            "> [!WARNING]",
            self.content,
            "New palette entry must reference the '> [!WARNING]' pattern.",
        )

    def test_new_entry_learning_section_present(self):
        """The 2026-05-12 entry must contain a Learning section."""
        self.assertIn(
            "**Learning:**",
            self.content,
            "Expected '**Learning:**' marker not found in .Jules/palette.md.",
        )

    def test_new_entry_action_section_present(self):
        """The 2026-05-12 entry must contain an Action section."""
        self.assertIn(
            "**Action:**",
            self.content,
            "Expected '**Action:**' marker not found in .Jules/palette.md.",
        )

    def test_new_entry_mentions_bold_replacement(self):
        """The new entry learning note must explain that bold text is being replaced."""
        self.assertIn(
            "bold",
            self.content.lower(),
            "Expected 'bold' keyword not found in 2026-05-12 palette entry.",
        )

    def test_new_entry_mentions_assistive_technologies(self):
        """The new entry must mention assistive technologies for accessibility context."""
        self.assertIn(
            "assistive technolog",
            self.content.lower(),
            "Expected 'assistive technolog' not found in 2026-05-12 palette entry.",
        )

    def test_new_entry_action_instructs_replacing_bold_warnings(self):
        """The action section must instruct replacing bold-text warnings."""
        self.assertIn(
            "Replace",
            self.content,
            "Expected 'Replace' action instruction in 2026-05-12 palette entry.",
        )

    def test_new_entry_is_chronologically_last(self):
        """The 2026-05-12 entry must be the most recent (last heading) in the file."""
        date_headings = re.findall(r"^## (\d{4}-\d{2}-\d{2})", self.content, re.MULTILINE)
        self.assertTrue(
            len(date_headings) > 0,
            "No date headings found in .Jules/palette.md.",
        )
        self.assertEqual(
            date_headings[-1],
            "2026-05-12",
            f"Expected '2026-05-12' to be the last date heading; got '{date_headings[-1]}'.",
        )

    def test_file_not_empty(self):
        """.Jules/palette.md must not be empty."""
        self.assertGreater(
            len(self.content.strip()),
            0,
            ".Jules/palette.md is empty.",
        )


if __name__ == "__main__":
    unittest.main()
