"""
Tests for PR: Improve accessibility with descriptive alt text for mascot SVG

Covers:
  - profile/README.md: <img> tag has a non-empty, descriptive alt attribute and quoted HTML attributes
  - .Jules/palette.md: file exists and contains the expected learning/action content
  - CODE_OF_CONDUCT.md: contact email is present and highlighted with an alert block
  - README.md: Code of Conduct links to the local file
"""

import functools
import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_MD = os.path.join(REPO_ROOT, "README.md")
PROFILE_README = os.path.join(REPO_ROOT, "profile", "README.md")
COC_MD = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
PALETTE_MD = os.path.join(REPO_ROOT, ".Jules", "palette.md")
CONTRIBUTING_MD = os.path.join(REPO_ROOT, "CONTRIBUTING.md")


@functools.lru_cache(maxsize=None)
def _read_cached(path: str) -> str:
    """Reads a file from disk and caches its content in memory."""
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _read(path: str) -> str:
    return _read_cached(path)


# Pre-compiled regular expression patterns for optimized string search operations.
RE_EMPTY_ALT = re.compile(r'<img\s[^>]*alt\s*=\s*["\']["\']')
RE_WHITESPACE_ALT = re.compile(r'<img\s[^>]*alt\s*=\s*["\'](\s+)["\']')
RE_IMG_TAG = re.compile(r"<img\s")
RE_IMG_TAG_ALL = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
RE_ALT_ATTRIBUTE = re.compile(r'\balt\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)


# Global tracker of passed test IDs to prevent redundant re-execution in meta-test suites.
_PASSED_TESTS = set()


class TrackingTestCase(unittest.TestCase):
    """Base test case that records completed tests to avoid redundant runs."""
    def tearDown(self):
        super().tearDown()
        _PASSED_TESTS.add(self.id())


class TestProfileReadmeAltText(TrackingTestCase):
    """Tests for the <img> alt attribute change in profile/README.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(PROFILE_README)

    def test_img_alt_is_not_empty(self):
        """The mascot <img> must not carry an empty alt attribute (alt="")."""
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

    def test_img_attributes_quoted(self):
        """All HTML attributes on the mascot <img> tag must be quoted for compliance and robust parsing."""
        self.assertIn('width="200"', self.content)
        self.assertIn('align="right"', self.content)
        self.assertIn('src="https://user-images.githubusercontent.com', self.content)

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
            RE_IMG_TAG,
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
        """Every <img> tag in the file must carry a non-empty alt attribute."""
        img_tags = RE_IMG_TAG_ALL.findall(self.content)
        for tag in img_tags:
            alt_match = RE_ALT_ATTRIBUTE.search(tag)
            self.assertIsNotNone(
                alt_match,
                f"<img> tag is missing an alt attribute: {tag}",
            )
            self.assertGreater(
                len(alt_match.group(1).strip()),
                0,
                f"<img> tag has an empty or whitespace-only alt attribute: {tag}",
            )


class TestPaletteMarkdown(TrackingTestCase):
    """Tests for the new .Jules/palette.md file."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(PALETTE_MD)

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

    def test_content_is_class_level_attribute(self):
        """After the setUpClass refactor, content must be a class-level attribute."""
        self.assertIn(
            "content",
            TestPaletteMarkdown.__dict__,
            "'content' must be set on the class dict after setUpClass refactor.",
        )

    def test_content_accessible_via_instance(self):
        """Class-level content must still be accessible via self in test methods."""
        self.assertIs(
            self.content,
            TestPaletteMarkdown.__dict__["content"],
            "self.content must resolve to the same object as the class attribute set by setUpClass.",
        )


class TestProfileReadmeSetupClassBehavior(unittest.TestCase):
    """Verify the setUp -> setUpClass refactor in TestProfileReadmeAltText."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(PROFILE_README)

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


class TestCodeOfConductUX(TrackingTestCase):
    """Tests for Code of Conduct contact standardization and visibility."""

    @classmethod
    def setUpClass(cls):
        cls.coc_content = _read_cached(COC_MD)
        cls.readme_content = _read_cached(README_MD)
        cls.contributing_content = _read_cached(CONTRIBUTING_MD)
        cls.content = cls.coc_content

    def test_coc_contains_correct_email(self):
        """CODE_OF_CONDUCT.md should contain the official reporting email."""
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            self.coc_content,
            "Official reporting email not found in CODE_OF_CONDUCT.md.",
        )

    def test_coc_contains_alert_block(self):
        """The reporting email in CODE_OF_CONDUCT.md should be in an alert block."""
        self.assertIn(
            "> [!IMPORTANT]",
            self.coc_content,
            "Reporting email should be wrapped in a > [!IMPORTANT] alert block in CODE_OF_CONDUCT.md.",
        )

    def test_readme_localized_coc_link(self):
        """README.md should have a localized link to CODE_OF_CONDUCT.md."""
        self.assertIn(
            "[Code of Conduct](CODE_OF_CONDUCT.md)",
            self.readme_content,
            "Localized Code of Conduct link not found in README.md footer.",
        )

    def test_contributing_localized_coc_link(self):
        """CONTRIBUTING.md should have a localized link to CODE_OF_CONDUCT.md."""
        self.assertIn(
            "[Contributor Code of Conduct](CODE_OF_CONDUCT.md)",
            self.contributing_content,
            "Localized Code of Conduct link not found in CONTRIBUTING.md.",
        )

    def test_contributing_coc_alert_block(self):
        """CONTRIBUTING.md should wrap the Code of Conduct disclaimer in an IMPORTANT alert block."""
        self.assertIn(
            "> [!IMPORTANT]",
            self.contributing_content,
            "Code of Conduct notice should be wrapped in a > [!IMPORTANT] alert block in CONTRIBUTING.md.",
        )

    def test_contributing_secure_links(self):
        """CONTRIBUTING.md should not contain unencrypted http:// links."""
        self.assertNotIn("http://", self.contributing_content)

    def test_contributing_top_level_heading(self):
        """CONTRIBUTING.md should have a level-1 heading '# Contributing'."""
        self.assertTrue(
            self.contributing_content.startswith("# Contributing\n"),
            "CONTRIBUTING.md should start with a level-1 heading '# Contributing'."
        )

    def test_contributing_released_link_is_descriptive(self):
        """CONTRIBUTING.md should use descriptive link text."""
        self.assertIn(
            "[released under the GitHub Terms of Service](https://docs.github.com",
            self.contributing_content,
            "Expected descriptive anchor text in CONTRIBUTING.md."
        )


if __name__ == "__main__":
    unittest.main()
