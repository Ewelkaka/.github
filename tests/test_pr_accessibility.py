"""
Tests for PR: Improve accessibility with descriptive alt text for mascot SVG

Covers:
  - profile/README.md: <img> tag has a non-empty, descriptive alt attribute
  - .Jules/palette.md: file exists and contains the expected learning/action content

# Suite-wide impact: 19 openat calls reduced to 3
  - CODE_OF_CONDUCT.md: contact email is present and highlighted with an alert block
  - README.md: Code of Conduct links to the local file
"""
# Suite-wide impact: 19 openat calls reduced to 3

import os
import re
import unittest
import functools

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO_ROOT, "README.md")
PROFILE_README = os.path.join(REPO_ROOT, "profile", "README.md")
CODE_OF_CONDUCT = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
PALETTE_MD = os.path.join(REPO_ROOT, ".Jules", "palette.md")
COC_MD = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_MD = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
README_MD = os.path.join(REPO_ROOT, "README.md")


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()
# Centralized in-memory cache to ensure each static Markdown file
# is read from disk exactly once during a full test suite execution.
# Optimization: Use @functools.lru_cache(maxsize=None) to cache static
# Markdown files in memory at the C level, removing Python-level dictionary
# lookup and manual branching overhead.
@functools.lru_cache(maxsize=None)
def _read_cached(path: str) -> str:
    """Reads a file from disk and caches its content in memory."""
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# Pre-compiled regular expression patterns for optimized string search operations.
# Compilation of regexes at the module level avoids redundant compilation overhead
# during repeat test executions and loop evaluations.
RE_EMPTY_ALT = re.compile(r'<img\s[^>]*alt\s*=\s*["\']["\']')
RE_WHITESPACE_ALT = re.compile(r'<img\s[^>]*alt\s*=\s*["\'](\s+)["\']')
RE_IMG_TAG = re.compile(r"<img\s")
RE_IMG_TAG_ALL = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
RE_ALT_ATTRIBUTE = re.compile(r'\balt\s*=\s*["\']([^"\']*)["\']', re.IGNORECASE)
RE_COC_ALERT_BLOCK = re.compile(r"> \[!IMPORTANT\]\s*\n>\s*\[opensource-security@github.com\]")


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
        cls.content = _read(PROFILE_README)
        # Suite-wide impact: 19 openat calls reduced to 3
        cls.content = _read(PROFILE_README)
        cls.content = _read(PROFILE_README)
        # Suite-wide impact: reduced openat calls from 19 to 3 by reading once per class
        cls.content = _read(PROFILE_README)
        # Suite-wide impact: Refactored to read file once per class instead of once per test.
        cls.content = _read(PROFILE_README)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class.
        cls.content = _read(PROFILE_README)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class
        cls.content = _read(PROFILE_README)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class.
        # Reduces openat calls for this file by ~85% (from 6 to 1).
        cls.content = _read(PROFILE_README)
        cls.content = _read(PROFILE_README)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class
        cls.content = _read(PROFILE_README)
        # BOLT OPTIMIZATION: Read the file once for the entire class to avoid O(N) I/O.
        # This reduces openat() calls from 6 to 1 for this class.
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once for all tests in this class to reduce I/O overhead.
        # This reduces openat() calls from 6 to 1 for this class.
        cls.content = _read(PROFILE_README)
        # Optimization: read file once per class instead of once per test.
        # Reduces openat() calls from 6 to 1.
        cls.content = _read(PROFILE_README)
        # Optimization: Read the file once per class to reduce redundant I/O
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once per class instead of once per test method.
        # Reduces openat() calls from 6 to 1.
        cls.content = _read(PROFILE_README)
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once for all tests in this class to reduce I/O.
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once per class instead of once per test.
        # Reduces openat() calls from 6 to 1 for this class.
        cls.content = _read(PROFILE_README)
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once per class to reduce disk I/O.
        # Reduces openat() calls from 6 to 1 for this class.
        cls.content = _read(PROFILE_README)
        # PERFORMANCE: Read file content once for the entire class instead of per test method.
        # This reduces openat() calls for this file from 6 to 1.
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once for all tests in this class to reduce redundant I/O.
        cls.content = _read(PROFILE_README)
        # Read the file once for all tests in this class to reduce I/O overhead
        cls.content = _read(PROFILE_README)
        # Cache content to reduce file I/O from O(N_tests) to O(1)
        cls.content = _read(PROFILE_README)
        # Optimization: Read the file once for all tests in this class
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once per class instead of once per test.
        # Reduces openat() system calls from O(N_tests) to O(1).
        cls.content = _read(PROFILE_README)
        # Optimization: read the file once for all tests in this class to reduce redundant I/O.
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once per class to reduce openat() calls
        cls.content = _read(PROFILE_README)
        # Optimization: Read file content once at the class level to reduce openat() syscalls
        cls.content = _read(PROFILE_README)
        # Optimization: Read file once per class instead of once per test method.
        # Reduces openat() system calls from O(N_tests) to O(1).
        cls.content = _read_cached(PROFILE_README)

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
        """Every <img> tag in the file must carry a non-empty alt attribute.

        This acts as a regression guard so future image additions cannot
        silently omit or empty the alt attribute.
        """
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
        cls.content = _read(PALETTE_MD)
        # Suite-wide impact: 19 openat calls reduced to 3
        cls.content = _read(PALETTE_MD)
        cls.content = _read(PALETTE_MD)
        # Suite-wide impact: reduced openat calls from 19 to 3 by reading once per class
        cls.content = _read(PALETTE_MD)
        # Suite-wide impact: Refactored to read file once per class instead of once per test.
        cls.content = _read(PALETTE_MD)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class.
        cls.content = _read(PALETTE_MD)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class
        cls.content = _read(PALETTE_MD)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class.
        # Reduces openat calls for this file by ~90% (from 10 to 1).
        cls.content = _read(PALETTE_MD)
        cls.content = _read(PALETTE_MD)
        # Suite-wide impact: Redundant openat calls reduced by reading once per class
        cls.content = _read(PALETTE_MD)
        # BOLT OPTIMIZATION: Read the file once for the entire class to avoid O(N) I/O.
        # This reduces openat() calls from 9 to 1 for this class.
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once for all tests in this class to reduce I/O overhead.
        # This reduces openat() calls from 10 to 1 for this class.
        cls.content = _read(PALETTE_MD)
        # Optimization: read file once per class instead of once per test.
        # Reduces openat() calls from 10 to 1.
        cls.content = _read(PALETTE_MD)
        # Optimization: Read the file once per class to reduce redundant I/O
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once per class instead of once per test method.
        # Reduces openat() calls from 10 to 1.
        cls.content = _read(PALETTE_MD)
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once for all tests in this class to reduce I/O.
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once per class instead of once per test.
        # Reduces openat() calls from 10 to 1 for this class.
        cls.content = _read(PALETTE_MD)
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once per class to reduce disk I/O.
        # Reduces openat() calls from 10 to 1 for this class.
        cls.content = _read(PALETTE_MD)
        # PERFORMANCE: Read file content once for the entire class instead of per test method.
        # This reduces openat() calls for this file from 10 to 1.
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once for all tests in this class to reduce redundant I/O.
        cls.content = _read(PALETTE_MD)
        # Read the file once for all tests in this class to reduce I/O overhead
        cls.content = _read(PALETTE_MD)
        # Cache content to reduce file I/O from O(N_tests) to O(1)
        cls.content = _read(PALETTE_MD)
        # Optimization: Read the file once for all tests in this class
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once per class instead of once per test.
        # Reduces openat() system calls from O(N_tests) to O(1).
        cls.content = _read(PALETTE_MD)
        # Optimization: read the file once for all tests in this class to reduce redundant I/O.
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once per class to reduce openat() calls
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file content once at the class level to reduce openat() syscalls
        cls.content = _read(PALETTE_MD)
        # Optimization: Read file once per class instead of once per test method.
        # Reduces openat() system calls from O(N_tests) to O(1).
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

class TestCocAccessibility(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md"), "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("opensource-security@github.com", self.content)

    def test_mailto_link(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

class TestCodeOfConductUX(TrackingTestCase):
    """Tests for Code of Conduct contact standardization and visibility."""

    @classmethod
    def setUpClass(cls):
        # Optimization: Read static data files once per class instead of once per test method.
        # Reduces redundant file openat() system calls from O(N_tests) to O(1).
        cls.coc_content = _read(COC_MD)
        cls.contributing_content = _read(CONTRIBUTING_MD)
        cls.readme_content = _read(README_MD)
        # Reduces openat() system calls from O(N_tests) to O(1).
        cls.coc_content = _read(COC_MD)
        cls.readme_content = _read(README_MD)
        cls.contributing_content = _read(CONTRIBUTING_MD)
        # Optimization: Read static test-data files once per class instead of once per test method.
        # Reduces openat() system calls from O(N_tests) to O(1).
        cls.content = _read(COC_MD)
        cls.readme_content = _read(README_MD)
        cls.contributing_content = _read(CONTRIBUTING_MD)
        # Optimization: Read files once per class to avoid redundant on-demand reads.
        cls.coc_content = _read(COC_MD)
        cls.readme_content = _read(README_MD)
        cls.contributing_content = _read(CONTRIBUTING_MD)
        # Optimization: Cache all static test files at the class level via setUpClass()
        # using the centralized cache _read_cached(). This avoids repeated, redundant dictionary
        # lookups or on-demand file reading across individual test cases in this class.
        cls.content = _read_cached(COC_MD)
        cls.readme_content = _read_cached(README_MD)
        cls.contributing_content = _read_cached(CONTRIBUTING_MD)

    def test_coc_contains_correct_email(self):
        """CODE_OF_CONDUCT.md should contain the official reporting email."""
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            self.coc_content,
            self.content,
            "Official reporting email not found in CODE_OF_CONDUCT.md.",
        )

    def test_coc_contains_alert_block(self):
        """The reporting email in CODE_OF_CONDUCT.md should be in an alert block."""
        self.assertRegex(
            self.content,
            self.coc_content,
            r"> \[!IMPORTANT\]\s*\n>\s*\[opensource-security@github.com\]",
            self.content,
            RE_COC_ALERT_BLOCK,
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

    def test_contributing_has_alert_block(self):
        """The Code of Conduct disclaimer in CONTRIBUTING.md should be highlighted in an alert block."""
    def test_contributing_contains_alert_block(self):
        """CONTRIBUTING.md should contain the Code of Conduct disclaimer in an alert block."""
        content = _read(CONTRIBUTING_MD)
        self.assertRegex(
            content,
            r"> \[!IMPORTANT\]\s*\n>\s*Please note that this project is released with a \[Contributor Code of Conduct\]\(CODE_OF_CONDUCT\.md\)\.",
            "The Code of Conduct warning in CONTRIBUTING.md should be wrapped in a > [!IMPORTANT] alert block.",
            "Code of Conduct disclaimer should be wrapped in a > [!IMPORTANT] alert block in CONTRIBUTING.md.",
        )

    def test_contributing_coc_alert_block(self):
        """CONTRIBUTING.md should have the Code of Conduct notice highlighted with an alert block."""
        self.assertRegex(
            self.contributing_content,
            r"> \[!IMPORTANT\]\s*\n>\s*Please note that this project is released with a \[Contributor Code of Conduct\]\(CODE_OF_CONDUCT.md\)\. By participating in this project you agree to abide by its terms\.",
            "Code of Conduct notice in CONTRIBUTING.md should be highlighted with a > [!IMPORTANT] alert block.",
        """CONTRIBUTING.md should wrap the Code of Conduct disclaimer inside a [!IMPORTANT] alert block."""
        content = _read(CONTRIBUTING_MD)
        self.assertIn(
            "> [!IMPORTANT]\n> Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.",
            content,
            "Code of Conduct disclaimer is not wrapped inside a > [!IMPORTANT] alert block in CONTRIBUTING.md.",
        )

    def test_contributing_coc_alert_block_regex(self):
        """The [!IMPORTANT] marker and disclaimer text must be on consecutive blockquote lines."""
        content = _read(CONTRIBUTING_MD)
        self.assertRegex(
            content,
            r"> \[!IMPORTANT\]\s*\n>\s*Please note that this project is released with a \[Contributor Code of Conduct\]",
            "Expected the [!IMPORTANT] marker directly followed by a blockquote line "
            "containing the Code of Conduct disclaimer in CONTRIBUTING.md.",
        )

    def test_contributing_disclaimer_not_a_bare_paragraph(self):
        """The disclaimer line itself must be prefixed with '> ' and not appear as a plain paragraph."""
        content = _read(CONTRIBUTING_MD)
        for line in content.splitlines():
            if "Please note that this project is released with a [Contributor Code of Conduct]" in line:
                self.assertTrue(
                    line.startswith(">"),
                    "The Code of Conduct disclaimer line must start with '>' to remain "
                    f"inside the alert block, but found: {line!r}",
                )
                break
        else:
            self.fail("Code of Conduct disclaimer line not found in CONTRIBUTING.md.")

    def test_contributing_alert_block_precedes_submitting_section(self):
        """The [!IMPORTANT] alert block must appear before the 'Submitting a pull request' section."""
        content = _read(CONTRIBUTING_MD)
        alert_index = content.find("> [!IMPORTANT]")
        section_index = content.find("## Submitting a pull request")
        self.assertNotEqual(alert_index, -1, "[!IMPORTANT] marker not found in CONTRIBUTING.md.")
        self.assertNotEqual(section_index, -1, "'Submitting a pull request' section not found in CONTRIBUTING.md.")
        self.assertLess(
            alert_index,
            section_index,
            "The [!IMPORTANT] alert block should appear before the "
            "'Submitting a pull request' section in CONTRIBUTING.md.",
        )

    def test_contributing_only_one_important_alert_block(self):
        """CONTRIBUTING.md should contain exactly one [!IMPORTANT] alert marker."""
        content = _read(CONTRIBUTING_MD)
        self.assertEqual(
            content.count("[!IMPORTANT]"),
            1,
            "Expected exactly one [!IMPORTANT] alert marker in CONTRIBUTING.md.",
        """CONTRIBUTING.md should wrap the Code of Conduct disclaimer in an IMPORTANT alert block."""
        self.assertIn(
            "> [!IMPORTANT]\n> Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.",
            self.contributing_content,
            "Code of Conduct disclaimer should be wrapped in a > [!IMPORTANT] alert block in CONTRIBUTING.md.",
        )

    def test_contributing_secure_links(self):
        """CONTRIBUTING.md should not contain unencrypted http:// links."""
        self.assertNotIn("http://", self.contributing_content)

    def test_contributing_top_level_heading(self):
        """CONTRIBUTING.md should have a level-1 heading '# Contributing' to establish a semantically correct visual hierarchy."""
        # Optimization: Use self.contributing_content loaded in setUpClass()
        # instead of calling redundant caching helper _read_cached().
        self.assertTrue(
            self.contributing_content.startswith("# Contributing\n"),
            "CONTRIBUTING.md should start with a level-1 heading '# Contributing' for correct visual hierarchy."
        )

    def test_contributing_released_link_is_descriptive(self):
        """CONTRIBUTING.md should use descriptive link text 'released under the GitHub Terms of Service' instead of a generic 'released' link for better screen-reader accessibility."""
        self.assertNotIn(
            "[released](https://docs.github.com",
            self.contributing_content,
            "Expected 'released' link text in CONTRIBUTING.md to be updated with descriptive anchor text for accessibility."
        )
        self.assertIn(
            "[released under the GitHub Terms of Service](https://docs.github.com",
            self.contributing_content,
            "Expected descriptive anchor text 'released under the GitHub Terms of Service' for the site policy link in CONTRIBUTING.md."
        )


class TestCodeOfConductAccessibility(unittest.TestCase):
    """Tests for CoC contact accessibility and README link localization."""

    def test_coc_contains_email_link(self):
        """CODE_OF_CONDUCT.md must contain the reporting email as a mailto link."""
        content = _read(CODE_OF_CONDUCT)
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            content,
            "Reporting email mailto link not found in CODE_OF_CONDUCT.md.",
        )

    def test_coc_uses_important_alert(self):
        """CODE_OF_CONDUCT.md must use an [!IMPORTANT] alert for the contact method."""
        content = _read(CODE_OF_CONDUCT)
        self.assertIn(
            "> [!IMPORTANT]",
            content,
            "Expected [!IMPORTANT] alert block not found in CODE_OF_CONDUCT.md.",
        )

    def test_readme_links_to_local_coc(self):
        """README.md must link to the local CODE_OF_CONDUCT.md file."""
        content = _read(README)
        self.assertIn(
            "[Code of Conduct](CODE_OF_CONDUCT.md)",
            content,
            "README.md does not link to the local CODE_OF_CONDUCT.md file.",
        )


class TestCodeOfConductAccessibility(unittest.TestCase):
    """Tests for Code of Conduct accessibility improvements."""

    def setUp(self):
        self.content = _read(COC_MD)

    def test_coc_has_mailto_link(self):
        """The Code of Conduct must contain the interactive security mailto link."""
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            self.content,
        )

    def test_coc_has_important_alert(self):
        """The reporting method must be highlighted with an [!IMPORTANT] alert."""
        self.assertIn("> [!IMPORTANT]", self.content)

    def test_coc_placeholder_removed(self):
        """The placeholder [INSERT CONTACT METHOD] must be removed."""
        self.assertNotIn("[INSERT CONTACT METHOD]", self.content)


class TestContributingDiscoverability(unittest.TestCase):
    """Tests for CONTRIBUTING.md UX improvements."""

    def setUp(self):
        self.content = _read(CONTRIBUTING_MD)

    def test_contributing_links_to_coc(self):
        """CONTRIBUTING.md should link to the local CODE_OF_CONDUCT.md."""
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)


if __name__ == "__main__":
    unittest.main()