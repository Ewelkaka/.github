"""
Tests for PR: Improve accessibility with descriptive alt text for mascot SVG

Covers:
  - profile/README.md: <img> tag has a non-empty, descriptive alt attribute
  - .Jules/palette.md: file exists and contains the expected learning/action content
"""

import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE_README = os.path.join(REPO_ROOT, "profile", "README.md")
PALETTE_MD = os.path.join(REPO_ROOT, ".Jules", "palette.md")


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class TestProfileReadmeAltText(unittest.TestCase):
    """Tests for the <img> alt attribute change in profile/README.md."""

    @classmethod
    def setUpClass(cls):
        # Suite-wide impact: Redundant openat calls reduced by reading once per class.
        cls.content = _read(PROFILE_README)

    def test_img_alt_is_not_empty(self):
        """The mascot <img> must not carry an empty alt attribute (alt="")."""
        # Match alt="" or alt='' (empty)
        empty_alt = re.search(r'<img\s[^>]*alt\s*=\s*["\']["\']', self.content)
        self.assertIsNone(
            empty_alt,
            "Found an <img> tag with an empty alt attribute; all informative "
            "images must have descriptive alt text.",
        )

    def test_img_alt_is_descriptive(self):
        """The mascot <img> must use the new descriptive alt text."""
        self.assertIn(
            'alt="GitHub Skills character illustration"',
            self.content,
            "Expected descriptive alt text 'GitHub Skills character illustration' "
            "not found in profile/README.md.",
        )

    def test_img_alt_not_whitespace_only(self):
        """The alt attribute value must not be only whitespace."""
        whitespace_alt = re.search(
            r'<img\s[^>]*alt\s*=\s*["\'](\s+)["\']', self.content
        )
        self.assertIsNone(
            whitespace_alt,
            "Found an <img> tag whose alt attribute contains only whitespace.",
        )

    def test_img_tag_present(self):
        """The profile README must still contain the mascot <img> tag."""
        self.assertRegex(
            self.content,
            r"<img\s",
            "No <img> tag found in profile/README.md; the mascot image may have "
            "been accidentally removed.",
        )

    def test_img_src_unchanged(self):
        """The image src URL must be preserved after the alt-text change."""
        expected_src = (
            "https://user-images.githubusercontent.com/1221423/"
            "156894097-ff2d6566-7b6a-4488-950e-f4ebe990965a.svg"
        )
        self.assertIn(
            expected_src,
            self.content,
            "The mascot image src URL was unexpectedly changed.",
        )

    def test_all_img_tags_have_nonempty_alt(self):
        """Every <img> tag in the file must carry a non-empty alt attribute.

        This acts as a regression guard so future image additions cannot
        silently omit or empty the alt attribute.
        """
        img_tags = re.findall(r"<img\b[^>]*>", self.content, re.IGNORECASE)
        for tag in img_tags:
            alt_match = re.search(r'\balt\s*=\s*["\']([^"\']*)["\']', tag, re.IGNORECASE)
            self.assertIsNotNone(
                alt_match,
                f"<img> tag is missing an alt attribute: {tag}",
            )
            self.assertGreater(
                len(alt_match.group(1).strip()),
                0,
                f"<img> tag has an empty or whitespace-only alt attribute: {tag}",
            )


class TestPaletteMarkdown(unittest.TestCase):
    """Tests for the new .Jules/palette.md file."""

    @classmethod
    def setUpClass(cls):
        # Suite-wide impact: Redundant openat calls reduced by reading once per class.
        cls.content = _read(PALETTE_MD)

    def test_file_exists(self):
        """.Jules/palette.md must exist in the repository."""
        self.assertTrue(
            os.path.isfile(PALETTE_MD),
            ".Jules/palette.md does not exist.",
        )

    def test_contains_date_heading(self):
        """The palette entry must include the expected date in the heading."""
        self.assertIn(
            "2024-05-24",
            self.content,
            "Expected date '2024-05-24' not found in .Jules/palette.md.",
        )

    def test_heading_describes_alt_text_requirement(self):
        """The heading must describe the alt-text requirement."""
        self.assertIn(
            "descriptive alt text",
            self.content,
            "Expected phrase 'descriptive alt text' not found in the palette heading.",
        )

    def test_learning_section_present(self):
        """The file must contain a Learning section."""
        self.assertIn(
            "**Learning:**",
            self.content,
            "Expected '**Learning:**' marker not found in .Jules/palette.md.",
        )

    def test_learning_mentions_screen_reader(self):
        """The learning note must mention screen reader users."""
        self.assertIn(
            "screen reader",
            self.content,
            "Expected 'screen reader' not found in the Learning section of .Jules/palette.md.",
        )

    def test_action_section_present(self):
        """The file must contain an Action section."""
        self.assertIn(
            "**Action:**",
            self.content,
            "Expected '**Action:**' marker not found in .Jules/palette.md.",
        )

    def test_action_mentions_img_tags(self):
        """The action note must instruct checking <img> tags."""
        self.assertIn(
            "<img>",
            self.content,
            "Expected '<img>' reference not found in the Action section of .Jules/palette.md.",
        )

    def test_action_mentions_alt_attribute(self):
        """The action note must reference the alt attribute specifically."""
        self.assertIn(
            "`alt`",
            self.content,
            "Expected backtick-quoted `alt` attribute reference not found in .Jules/palette.md.",
        )

    def test_file_is_not_empty(self):
        """The palette file must not be empty."""
        self.assertGreater(
            len(self.content.strip()),
            0,
            ".Jules/palette.md is empty.",
        )

    def test_learning_mentions_brand_identifier(self):
        """The learning note must explain why mascot images matter (brand identity)."""
        self.assertIn(
            "brand",
            self.content.lower(),
            "Expected 'brand' keyword not found in the learning section of .Jules/palette.md.",
        )

    # --- Tests for the PR change: removal of the 2026-05-27 entry ---

    def test_removed_entry_date_not_present(self):
        """The 2026-05-27 entry must have been removed from .Jules/palette.md."""
        self.assertNotIn(
            "2026-05-27",
            self.content,
            "The 2026-05-27 palette entry should have been removed but was found.",
        )

    def test_no_warning_alert_block_in_palette(self):
        """The removed entry's [!WARNING] alert block must not appear in palette.md."""
        self.assertNotIn(
            "[!WARNING]",
            self.content,
            "Found '[!WARNING]' in .Jules/palette.md; the entry containing it should have been removed.",
        )

    def test_no_mailto_link_in_palette(self):
        """The removed entry's mailto: reference must not appear in palette.md."""
        self.assertNotIn(
            "mailto:",
            self.content,
            "Found 'mailto:' in .Jules/palette.md; the entry containing it should have been removed.",
        )

    def test_exactly_two_second_level_headings(self):
        """palette.md must have exactly two ## date headings after the removal."""
        import re
        headings = re.findall(r"^## \d{4}-\d{2}-\d{2}", self.content, re.MULTILINE)
        self.assertEqual(
            len(headings),
            2,
            f"Expected exactly 2 date headings in .Jules/palette.md, found {len(headings)}: {headings}",
        )

    def test_second_entry_date_still_present(self):
        """The 2026-04-02 entry must still be present after the 2026-05-27 entry was removed."""
        self.assertIn(
            "2026-04-02",
            self.content,
            "Expected date '2026-04-02' not found; it should remain after removing the 2026-05-27 entry.",
        )

    # --- Tests for the PR change: setUp -> setUpClass refactor ---

    def test_content_is_class_level_attribute(self):
        """After the setUpClass refactor, content must be a class-level attribute."""
        self.assertIn(
            "content",
            TestPaletteMarkdown.__dict__,
            "'content' must be set on the class dict (not just instance) after setUpClass refactor.",
        )

    def test_content_accessible_via_instance(self):
        """Class-level content must still be accessible via self in test methods."""
        # If setUpClass set cls.content, self.content must resolve to the same object.
        self.assertIs(
            self.content,
            TestPaletteMarkdown.__dict__["content"],
            "self.content must resolve to the same object as the class attribute set by setUpClass.",
        )


class TestProfileReadmeSetupClassBehavior(unittest.TestCase):
    """Verify the setUp -> setUpClass refactor in TestProfileReadmeAltText."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(PROFILE_README)

    def test_content_is_class_level_attribute(self):
        """After the setUpClass refactor, content must be stored on the class, not per-instance."""
        self.assertIn(
            "content",
            TestProfileReadmeAltText.__dict__,
            "'content' must be a class-level attribute on TestProfileReadmeAltText after refactor.",
        )

    def test_content_accessible_via_self(self):
        """Class-level attribute must be reachable via self in any test method."""
        self.assertIs(
            self.content,
            TestProfileReadmeSetupClassBehavior.__dict__["content"],
        )


if __name__ == "__main__":
    unittest.main()