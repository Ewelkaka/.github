"""
Tests for PR: Enhance security warnings with native alert blocks

Covers:
  - SECURITY.md: bold warning replaced with > [!WARNING] alert block
  - .Jules/palette.md: new entry (2026-05-12) documents the security-warning improvement
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
    """Tests for the [!WARNING] alert-block change in SECURITY.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(SECURITY_PATH)

    def test_security_warning_alert_block(self):
        """Verify that the security report warning is in a [!WARNING] alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn(
            "> Please do not report security vulnerabilities through public GitHub issues",
            self.content,
        )

    def test_no_bold_warning(self):
        """Verify that the old bold warning is removed."""
        self.assertNotIn(
            "**Please do not report security vulnerabilities through public GitHub issues",
            self.content,
        )

    def test_warning_body_is_full_sentence(self):
        """The warning block body must contain the complete warning sentence."""
        self.assertIn(
            "> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.",
            self.content,
        )

    def test_warning_block_marker_and_body_are_adjacent(self):
        """The > [!WARNING] marker must be immediately followed by the body line."""
        self.assertIn(
            "> [!WARNING]\n> Please do not report security vulnerabilities",
            self.content,
        )

    def test_warning_appears_before_email_instruction(self):
        """The [!WARNING] block must appear before the 'send an email' instruction."""
        warning_pos = self.content.find("> [!WARNING]")
        email_pos = self.content.find("opensource-security@github.com")
        self.assertGreater(
            warning_pos,
            -1,
            "> [!WARNING] block not found in SECURITY.md.",
        )
        self.assertGreater(
            email_pos,
            -1,
            "Email address not found in SECURITY.md.",
        )
        self.assertLess(
            warning_pos,
            email_pos,
            "Expected [!WARNING] block to appear before the contact email line.",
        )

    def test_contact_email_preserved(self):
        """The contact email address must still be present in the file."""
        self.assertIn("opensource-security@github.com", self.content)

    def test_reporting_section_heading_present(self):
        """The '## Reporting Security Issues' heading must still be present."""
        self.assertIn("## Reporting Security Issues", self.content)

    def test_no_bold_syntax_wrapping_warning(self):
        """Confirm no Markdown bold markers wrap the 'do not report' warning text."""
        match = re.search(
            r"\*{1,2}Please do not report security vulnerabilities",
            self.content,
        )
        self.assertIsNone(
            match,
            "Bold Markdown syntax still wraps the security warning; it should use a [!WARNING] block instead.",
        )

    def test_file_not_empty(self):
        """SECURITY.md must not be empty."""
        self.assertGreater(len(self.content.strip()), 0, "SECURITY.md appears to be empty.")

    def test_warning_block_uses_github_native_syntax(self):
        """The alert block must use the exact GitHub-native > [!WARNING] syntax."""
        # Must start at the beginning of a line (no leading spaces before >)
        self.assertRegex(
            self.content,
            r"(?m)^> \[!WARNING\]",
            "Expected '> [!WARNING]' at the start of a line.",
        )

    def test_warning_mentions_discussions_and_pull_requests(self):
        """The warning must mention all three forbidden channels: issues, discussions, pull requests."""
        warning_section = self.content[self.content.find("> [!WARNING]"):]
        first_blank = warning_section.find("\n\n")
        block = warning_section if first_blank == -1 else warning_section[:first_blank]
        self.assertIn("discussions", block)
        self.assertIn("pull requests", block)
        self.assertIn("issues", block)


class TestPaletteMarkdownSecurityEntry(unittest.TestCase):
    """Tests for the 2026-05-12 entry added to .Jules/palette.md in this PR."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(PALETTE_MD)

    def test_new_entry_date_present(self):
        """The new palette entry must carry the 2026-05-12 date."""
        self.assertIn(
            "2026-05-12",
            self.content,
            "Expected date '2026-05-12' not found in .Jules/palette.md.",
        )

    def test_new_entry_heading_mentions_security_warnings(self):
        """The new entry heading must mention security warnings."""
        self.assertIn(
            "security warning",
            self.content.lower(),
            "Expected phrase 'security warning' not found in the 2026-05-12 palette entry.",
        )

    def test_new_entry_heading_mentions_alert_blocks(self):
        """The new entry heading must mention alert blocks."""
        self.assertIn(
            "alert block",
            self.content.lower(),
            "Expected 'alert block' not found in the 2026-05-12 palette entry.",
        )

    def test_new_entry_learning_mentions_warning_syntax(self):
        """The Learning section must reference the [!WARNING] alert syntax."""
        self.assertIn(
            "[!WARNING]",
            self.content,
            "Expected '[!WARNING]' syntax reference not found in .Jules/palette.md.",
        )

    def test_new_entry_learning_mentions_assistive_technologies(self):
        """The Learning section must mention assistive technologies."""
        self.assertIn(
            "assistive technolog",
            self.content,
            "Expected 'assistive technolog' not found in the learning section of .Jules/palette.md.",
        )

    def test_new_entry_learning_mentions_scannability(self):
        """The Learning section must mention scannability."""
        self.assertIn(
            "scannability",
            self.content,
            "Expected 'scannability' not found in the learning section of .Jules/palette.md.",
        )

    def test_new_entry_action_instructs_bold_replacement(self):
        """The Action section must instruct replacing bold-text warnings."""
        self.assertIn(
            "bold",
            self.content.lower(),
            "Expected reference to 'bold' (replacement of bold warnings) in .Jules/palette.md.",
        )

    def test_new_entry_action_mentions_warning_block(self):
        """The Action section must reference [!WARNING] blocks as the replacement."""
        # The action line should specifically reference [!WARNING]
        action_idx = self.content.rfind("**Action:**")
        self.assertGreater(action_idx, -1, "No **Action:** marker found.")
        action_text = self.content[action_idx:]
        self.assertIn(
            "[!WARNING]",
            action_text,
            "Expected '[!WARNING]' in the Action section of the 2026-05-12 palette entry.",
        )

    def test_palette_has_three_dated_entries(self):
        """The palette file must contain exactly three dated ## entries after this PR."""
        dated_headings = re.findall(r"^## \d{4}-\d{2}-\d{2}", self.content, re.MULTILINE)
        self.assertEqual(
            len(dated_headings),
            3,
            f"Expected 3 dated entries in .Jules/palette.md, found {len(dated_headings)}: {dated_headings}",
        )

    def test_new_entry_is_last_entry(self):
        """The 2026-05-12 entry must be the last dated entry in the file."""
        dated_headings = re.findall(r"^## (\d{4}-\d{2}-\d{2})", self.content, re.MULTILINE)
        self.assertTrue(
            len(dated_headings) > 0,
            "No dated entries found in .Jules/palette.md.",
        )
        self.assertEqual(
            dated_headings[-1],
            "2026-05-12",
            f"Expected '2026-05-12' to be the last dated entry; got '{dated_headings[-1]}'.",
        )

    def test_new_entry_has_learning_marker(self):
        """The new entry must include a **Learning:** marker."""
        # Find the 2026-05-12 section and check it has a Learning marker
        idx = self.content.find("2026-05-12")
        self.assertGreater(idx, -1)
        section = self.content[idx:]
        # Cut to just this section (before the next ## heading, if any)
        next_heading = section.find("\n## ", 1)
        section = section if next_heading == -1 else section[:next_heading]
        self.assertIn(
            "**Learning:**",
            section,
            "Expected '**Learning:**' in the 2026-05-12 entry of .Jules/palette.md.",
        )

    def test_new_entry_has_action_marker(self):
        """The new entry must include an **Action:** marker."""
        idx = self.content.find("2026-05-12")
        self.assertGreater(idx, -1)
        section = self.content[idx:]
        next_heading = section.find("\n## ", 1)
        section = section if next_heading == -1 else section[:next_heading]
        self.assertIn(
            "**Action:**",
            section,
            "Expected '**Action:**' in the 2026-05-12 entry of .Jules/palette.md.",
        )


if __name__ == "__main__":
    unittest.main()
