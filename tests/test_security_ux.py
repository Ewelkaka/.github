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

    def test_warning_block_uses_uppercase(self):
        """Verify that the alert type is uppercase WARNING, not a variant."""
        # Confirm uppercase form exists
        self.assertIn("> [!WARNING]", self.content)
        # Confirm no lowercase/mixed-case variant slipped in
        self.assertNotIn("> [!warning]", self.content)
        self.assertNotIn("> [!Warning]", self.content)

    def test_warning_text_includes_full_sentence(self):
        """Verify the full warning sentence is present, including all channel types."""
        self.assertIn(
            "> Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.",
            self.content,
        )

    def test_warning_block_structure_is_adjacent(self):
        """Verify the [!WARNING] marker and warning text appear as consecutive blockquote lines."""
        # The two lines must be adjacent with only a newline between them
        self.assertIn(
            "> [!WARNING]\n> Please do not report security vulnerabilities",
            self.content,
        )

    def test_contact_email_present_after_warning(self):
        """Verify that the contact email instruction still follows the warning block."""
        self.assertIn("opensource-security@github.com", self.content)
        # Email line must come after the WARNING block in the document
        warning_pos = self.content.find("> [!WARNING]")
        email_pos = self.content.find("opensource-security@github.com")
        self.assertGreater(
            email_pos,
            warning_pos,
            "Contact email should appear after the [!WARNING] block.",
        )

    def test_security_file_is_not_empty(self):
        """Verify SECURITY.md is not empty and has substantive content."""
        self.assertGreater(len(self.content.strip()), 0)

    def test_no_bare_warning_outside_blockquote(self):
        """Verify the warning text is only inside a blockquote (prefixed with >)."""
        # Any line with the core warning text must start with '>'
        for line in self.content.splitlines():
            if "do not report security vulnerabilities" in line:
                self.assertTrue(
                    line.lstrip().startswith(">"),
                    f"Warning text found outside a blockquote: {line!r}",
                )


class TestPaletteSecurityEntry(unittest.TestCase):
    """Tests for the new 2026-05-12 entry added to .Jules/palette.md in this PR."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(PALETTE_PATH)

    def test_new_entry_date_heading_present(self):
        """The new palette entry must include the 2026-05-12 date."""
        self.assertIn(
            "2026-05-12",
            self.content,
            "Expected date '2026-05-12' not found in .Jules/palette.md.",
        )

    def test_new_entry_heading_describes_security_warnings(self):
        """The new entry heading must describe the security warning enhancement."""
        self.assertIn(
            "Enhance security warnings with native alert blocks",
            self.content,
            "Expected heading text not found in .Jules/palette.md.",
        )

    def test_new_entry_learning_mentions_warning_alert_syntax(self):
        """The Learning section of the new entry must reference the [!WARNING] syntax."""
        self.assertIn(
            "[!WARNING]",
            self.content,
            "Expected '[!WARNING]' syntax reference not found in .Jules/palette.md.",
        )

    def test_new_entry_learning_mentions_bold_text_problem(self):
        """The Learning section must describe the problem with bold-text warnings."""
        self.assertIn(
            "bold text",
            self.content,
            "Expected 'bold text' description not found in .Jules/palette.md.",
        )

    def test_new_entry_action_mentions_replacement(self):
        """The Action section must instruct replacing bold warnings."""
        self.assertIn(
            "Replace critical bold-text warnings",
            self.content,
            "Expected replacement instruction not found in the Action section of .Jules/palette.md.",
        )

    def test_new_entry_action_mentions_accessibility(self):
        """The Action section must reference accessibility as a goal."""
        self.assertIn(
            "accessibility",
            self.content,
            "Expected 'accessibility' not found in the Action section of .Jules/palette.md.",
        )

    def test_new_entry_learning_mentions_assistive_technologies(self):
        """The Learning section must mention assistive technologies."""
        self.assertIn(
            "assistive technologies",
            self.content,
            "Expected 'assistive technologies' not found in the Learning section.",
        )

    def test_new_entry_follows_existing_structure(self):
        """The new entry must use the standard Learning/Action structure."""
        # Locate the new entry block starting from the 2026-05-12 heading
        entry_start = self.content.find("## 2026-05-12")
        self.assertNotEqual(entry_start, -1, "New entry heading not found.")
        entry_text = self.content[entry_start:]
        self.assertIn("**Learning:**", entry_text, "New entry is missing '**Learning:**' marker.")
        self.assertIn("**Action:**", entry_text, "New entry is missing '**Action:**' marker.")

    def test_new_entry_is_last_entry(self):
        """The 2026-05-12 entry should be the most recent (last) entry in the file."""
        pos_new = self.content.find("## 2026-05-12")
        pos_older = self.content.find("## 2026-04-02")
        self.assertGreater(
            pos_new,
            pos_older,
            "The 2026-05-12 entry should appear after the 2026-04-02 entry.",
        )


if __name__ == "__main__":
    unittest.main()
