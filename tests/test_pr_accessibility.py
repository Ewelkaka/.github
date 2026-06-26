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

# Pre-compile regex patterns for performance
RE_EMPTY_ALT = re.compile(r'<img\s[^>]*alt\s*=\s*["\']["\']')
RE_WHITESPACE_ALT = re.compile(r'<img\s[^>]*alt\s*=\s*["\'](\s+)["\']')
RE_IMG_TAG_START = re.compile(r"<img\s")
RE_ALL_IMG_TAGS = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
RE_ALT_ATTR = re.compile(r'\balt\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class TestProfileReadmeAltText(unittest.TestCase):
    """Tests for the <img> alt attribute change in profile/README.md."""

    @classmethod
    def setUpClass(cls):
        # Optimization: Read file content once for all tests in this class
        cls.content = _read(PROFILE_README)

    def test_img_alt_is_not_empty(self):
        """The mascot <img> must not carry an empty alt attribute (alt="")."""
        # Match alt="" or alt='' (empty)
        empty_alt = RE_EMPTY_ALT.search(self.content)
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
        whitespace_alt = RE_WHITESPACE_ALT.search(self.content)
        self.assertIsNone(
            whitespace_alt,
            "Found an <img> tag whose alt attribute contains only whitespace.",
        )

    def test_img_tag_present(self):
        """The profile README must still contain the mascot <img> tag."""
        self.assertRegex(
            self.content,
            RE_IMG_TAG_START,
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
        img_tags = RE_ALL_IMG_TAGS.findall(self.content)
        for tag in img_tags:
            alt_match = RE_ALT_ATTR.search(tag)
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
        # Optimization: Read file content once for all tests in this class
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


if __name__ == "__main__":
    unittest.main()
