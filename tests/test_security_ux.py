import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")
PALETTE_PATH = os.path.join(REPO_ROOT, ".Jules", "palette.md")


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

    def test_warning_block_exact_syntax(self):
        """Verify the alert block uses exact uppercase [!WARNING] syntax, not a lowercase variant."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertNotIn("> [!warning]", self.content)
        self.assertNotIn("> [!Warning]", self.content)

    def test_warning_message_uses_blockquote_prefix(self):
        """Verify the warning message line itself starts with the blockquote prefix '> '."""
        self.assertIn(
            "> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.",
            self.content,
        )

    def test_warning_block_and_message_are_adjacent(self):
        """Verify the [!WARNING] line is immediately followed by the warning message line."""
        lines = self.content.splitlines()
        for i, line in enumerate(lines):
            if line.strip() == "> [!WARNING]":
                self.assertLess(
                    i + 1,
                    len(lines),
                    "The [!WARNING] line is the last line; expected a following message line.",
                )
                next_line = lines[i + 1]
                self.assertIn(
                    "Please do not report security vulnerabilities",
                    next_line,
                    "Line immediately after '> [!WARNING]' does not contain the expected warning text.",
                )
                return
        self.fail("'> [!WARNING]' line not found in SECURITY.md.")

    def test_warning_block_appears_exactly_once(self):
        """Verify [!WARNING] appears exactly once to prevent accidental duplication."""
        count = self.content.count("> [!WARNING]")
        self.assertEqual(count, 1, f"Expected exactly one '> [!WARNING]' block, found {count}.")

    def test_warning_full_phrase_preserved(self):
        """Verify the complete warning phrase including 'pull requests' is present."""
        self.assertIn(
            "do not report security vulnerabilities through public GitHub issues, discussions, or pull requests",
            self.content,
        )

    def test_no_bare_bold_vulnerability_warning(self):
        """Verify no bold-text wrapping of the vulnerability warning exists anywhere in the file."""
        self.assertNotIn(
            "**Please do not report security vulnerabilities",
            self.content,
        )
        # Also guard against trailing-bold variant: text followed by **
        self.assertNotIn(
            "pull requests.**",
            self.content,
        )

    def test_email_address_still_present(self):
        """Verify the contact email address was not accidentally removed during the change."""
        self.assertIn("opensource-security@github.com", self.content)

    def test_reporting_section_heading_present(self):
        """Verify the 'Reporting Security Issues' heading still exists."""
        self.assertIn("## Reporting Security Issues", self.content)

    def test_file_is_not_empty(self):
        """Verify SECURITY.md was not accidentally emptied."""
        self.assertGreater(len(self.content.strip()), 0, "SECURITY.md appears to be empty.")


class TestPaletteSecurityEntry(unittest.TestCase):
    """Tests for the new 2026-05-12 entry added to .Jules/palette.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(PALETTE_PATH)

    def test_new_entry_date_heading_present(self):
        """Verify the 2026-05-12 dated heading was added to palette.md."""
        self.assertIn("2026-05-12", self.content)

    def test_new_entry_heading_describes_security_warnings(self):
        """Verify the heading text describes enhancing security warnings."""
        self.assertIn(
            "Enhance security warnings with native alert blocks",
            self.content,
        )

    def test_new_entry_learning_section_present(self):
        """Verify the new entry contains a Learning section marker."""
        # Check that at least one **Learning:** marker is present (may have multiple entries)
        self.assertIn("**Learning:**", self.content)

    def test_new_entry_learning_mentions_warning_block_syntax(self):
        """Verify the learning note references the [!WARNING] GitHub alert syntax."""
        self.assertIn("> [!WARNING]", self.content)

    def test_new_entry_learning_mentions_bold_text_problem(self):
        """Verify the learning note identifies bold text as the problem being solved."""
        self.assertIn("bold text", self.content)

    def test_new_entry_learning_mentions_assistive_technologies(self):
        """Verify the learning note mentions accessibility / assistive technologies."""
        self.assertIn("assistive technologies", self.content)

    def test_new_entry_action_section_present(self):
        """Verify the new entry contains an Action section marker."""
        self.assertIn("**Action:**", self.content)

    def test_new_entry_action_mentions_replacing_bold_warnings(self):
        """Verify the action instructs replacing bold-text warnings."""
        # The action should reference replacing bold-text with WARNING blocks
        self.assertIn("Replace", self.content)
        self.assertIn("> [!WARNING]", self.content)

    def test_new_entry_is_a_level_two_heading(self):
        """Verify the new palette entry uses a level-2 Markdown heading (##)."""
        self.assertRegex(
            self.content,
            r"## 2026-05-12",
            "Expected a level-2 heading '## 2026-05-12' in .Jules/palette.md.",
        )

    def test_new_entry_action_mentions_scannability(self):
        """Verify the action note explains the scannability benefit."""
        self.assertIn("scannability", self.content)

    def test_palette_file_contains_multiple_entries(self):
        """Verify palette.md still retains prior entries alongside the new one."""
        # Count level-2 headings as a proxy for number of entries
        headings = re.findall(r"^## ", self.content, re.MULTILINE)
        self.assertGreaterEqual(
            len(headings),
            2,
            "Expected at least 2 entries in .Jules/palette.md (prior entries plus the new one).",
        )

    def test_new_entry_learning_mentions_github_native(self):
        """Verify the learning note references GitHub-native alert blocks."""
        self.assertIn("GitHub-native", self.content)


if __name__ == "__main__":
    unittest.main()
