"""
Tests for PR: Enhance security warnings with native alert blocks

Covers:
  - SECURITY.md: critical warning uses a GitHub-native [!WARNING] alert block
  - SECURITY.md: old bold-text warning is removed
  - SECURITY.md: warning block is structurally correct and complete
  - .Jules/palette.md: new 2026-05-12 entry exists with expected content
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

    def test_warning_block_is_contiguous(self):
        """The [!WARNING] line and the warning message must be consecutive blockquote lines.

        A blank line between them would break the alert block rendering on GitHub.
        """
        # Match "> [!WARNING]" immediately followed (after optional \r) by a
        # blockquote continuation line ("> ...")
        self.assertRegex(
            self.content,
            r"> \[!WARNING\]\r?\n> ",
            "The [!WARNING] alert block must not have a blank line before the message.",
        )

    def test_warning_message_mentions_discussions(self):
        """The warning must explicitly call out 'discussions' as a forbidden channel."""
        self.assertIn(
            "discussions",
            self.content,
            "Expected 'discussions' to appear in the [!WARNING] message in SECURITY.md.",
        )

    def test_warning_message_mentions_pull_requests(self):
        """The warning must explicitly call out 'pull requests' as a forbidden channel."""
        self.assertIn(
            "pull requests",
            self.content,
            "Expected 'pull requests' to appear in the [!WARNING] message in SECURITY.md.",
        )

    def test_contact_email_present(self):
        """Regression: the contact email address must still be present after the change."""
        self.assertIn(
            "opensource-security@github.com",
            self.content,
            "Contact email 'opensource-security@github.com' was accidentally removed.",
        )

    def test_warning_appears_in_reporting_section(self):
        """The [!WARNING] block must appear inside the 'Reporting Security Issues' section."""
        reporting_start = self.content.find("## Reporting Security Issues")
        self.assertNotEqual(
            reporting_start,
            -1,
            "'## Reporting Security Issues' section not found in SECURITY.md.",
        )
        warning_pos = self.content.find("> [!WARNING]")
        self.assertNotEqual(warning_pos, -1, "> [!WARNING] not found in SECURITY.md.")
        self.assertGreater(
            warning_pos,
            reporting_start,
            "The [!WARNING] block must appear after the '## Reporting Security Issues' heading.",
        )

    def test_no_bold_wrapping_on_warning_text(self):
        """Regression: ensure no residual bold markdown wraps the warning text."""
        # Guard against partial reversion where ** markers remain anywhere on the line
        bold_warning = re.search(
            r"\*\*Please do not report security vulnerabilities",
            self.content,
        )
        self.assertIsNone(
            bold_warning,
            "Found bold-markdown (**) wrapping on the security warning text; "
            "this should now be a [!WARNING] alert block.",
        )

    def test_warning_block_full_message(self):
        """The blockquote warning line must contain the complete guidance message."""
        self.assertIn(
            "> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.",
            self.content,
            "The full warning message (including all forbidden channels) must appear "
            "as a blockquote line in SECURITY.md.",
        )

    def test_security_md_has_reporting_section(self):
        """SECURITY.md must retain the '## Reporting Security Issues' heading."""
        self.assertIn(
            "## Reporting Security Issues",
            self.content,
            "'## Reporting Security Issues' section is missing from SECURITY.md.",
        )

    def test_file_is_not_empty(self):
        """SECURITY.md must not be empty."""
        self.assertGreater(
            len(self.content.strip()),
            0,
            "SECURITY.md is empty.",
        )


class TestPaletteMarkdown(unittest.TestCase):
    """Tests for the new 2026-05-12 entry in .Jules/palette.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(PALETTE_MD)

    def test_file_exists(self):
        """.Jules/palette.md must exist in the repository."""
        self.assertTrue(
            os.path.isfile(PALETTE_MD),
            ".Jules/palette.md does not exist.",
        )

    def test_new_entry_date_heading(self):
        """The palette file must contain the 2026-05-12 entry heading."""
        self.assertIn(
            "2026-05-12",
            self.content,
            "Expected date '2026-05-12' not found in .Jules/palette.md.",
        )

    def test_new_entry_heading_text(self):
        """The 2026-05-12 heading must describe enhancing security warnings."""
        self.assertIn(
            "Enhance security warnings with native alert blocks",
            self.content,
            "Expected heading text 'Enhance security warnings with native alert blocks' "
            "not found in .Jules/palette.md.",
        )

    def test_new_entry_learning_mentions_bold_text(self):
        """The Learning section of the new entry must mention bold text as the prior approach."""
        self.assertIn(
            "bold text",
            self.content,
            "Expected 'bold text' in the new palette entry's Learning section.",
        )

    def test_new_entry_learning_mentions_scanning(self):
        """The Learning section must explain that bold text can be skipped while scanning."""
        self.assertIn(
            "scanning",
            self.content,
            "Expected 'scanning' in the new palette entry's Learning section.",
        )

    def test_new_entry_learning_mentions_assistive_technologies(self):
        """The Learning section must reference assistive technologies."""
        self.assertIn(
            "assistive technologies",
            self.content,
            "Expected 'assistive technologies' in the new palette entry's Learning section.",
        )

    def test_new_entry_learning_mentions_warning_alert(self):
        """The Learning section must reference the [!WARNING] alert block syntax."""
        self.assertIn(
            "> [!WARNING]",
            self.content,
            "Expected '> [!WARNING]' syntax reference in .Jules/palette.md.",
        )

    def test_new_entry_action_mentions_replace(self):
        """The Action section must instruct replacing bold-text warnings."""
        self.assertIn(
            "Replace",
            self.content,
            "Expected 'Replace' in the Action section of the new palette entry.",
        )

    def test_new_entry_action_mentions_warning_blocks(self):
        """The Action section must reference [!WARNING] blocks as the replacement format."""
        # The action should mention the [!WARNING] block type
        self.assertIn(
            "[!WARNING]",
            self.content,
            "Expected '[!WARNING]' block reference in the Action section of .Jules/palette.md.",
        )

    def test_new_entry_action_mentions_scannability(self):
        """The Action section must mention scannability as a benefit."""
        self.assertIn(
            "scannability",
            self.content,
            "Expected 'scannability' in the Action section of the new palette entry.",
        )

    def test_new_entry_action_mentions_accessibility(self):
        """The Action section must mention accessibility as a benefit."""
        self.assertIn(
            "accessibility",
            self.content,
            "Expected 'accessibility' in the Action section of the new palette entry.",
        )

    def test_learning_marker_present(self):
        """The palette entry must use the standard **Learning:** marker."""
        self.assertIn(
            "**Learning:**",
            self.content,
            "Expected '**Learning:**' marker not found in .Jules/palette.md.",
        )

    def test_action_marker_present(self):
        """The palette entry must use the standard **Action:** marker."""
        self.assertIn(
            "**Action:**",
            self.content,
            "Expected '**Action:**' marker not found in .Jules/palette.md.",
        )

    def test_new_entry_is_last(self):
        """The 2026-05-12 entry must appear after the previous 2026-04-02 entry."""
        pos_apr = self.content.find("2026-04-02")
        pos_may = self.content.find("2026-05-12")
        self.assertNotEqual(pos_apr, -1, "2026-04-02 entry not found in palette.md.")
        self.assertNotEqual(pos_may, -1, "2026-05-12 entry not found in palette.md.")
        self.assertGreater(
            pos_may,
            pos_apr,
            "The 2026-05-12 entry must appear after the 2026-04-02 entry.",
        )

    def test_file_is_not_empty(self):
        """.Jules/palette.md must not be empty."""
        self.assertGreater(
            len(self.content.strip()),
            0,
            ".Jules/palette.md is empty.",
        )


if __name__ == "__main__":
    unittest.main()
