"""
Tests for PR: Improve accessibility with descriptive alt text for mascot SVG

Covers:
  - profile/README.md: <img> tag has a non-empty, descriptive alt attribute
  - .Jules/palette.md: file exists and contains the expected learning/action content
  - CODE_OF_CONDUCT.md: contact email is present and highlighted with an alert block
  - README.md: Code of Conduct links to the local file
"""

import os
import re
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(REPO_ROOT, "README.md")
PROFILE_README = os.path.join(REPO_ROOT, "profile", "README.md")
CODE_OF_CONDUCT = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
PALETTE_MD = os.path.join(REPO_ROOT, ".Jules", "palette.md")


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class TestProfileReadmeAltText(unittest.TestCase):
    """Tests for the <img> alt attribute change in profile/README.md."""

    def setUp(self):
        self.content = _read(PROFILE_README)

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

    def setUp(self):
        self.content = _read(PALETTE_MD)

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


class TestCodeOfConductEnforcementSection(unittest.TestCase):
    """Deeper structural/regression tests for the Enforcement section rewrite."""

    def setUp(self):
        self.content = _read(CODE_OF_CONDUCT)

    def test_placeholder_contact_removed(self):
        """The old '[INSERT CONTACT METHOD]' placeholder must be gone."""
        self.assertNotIn(
            "[INSERT CONTACT METHOD]",
            self.content,
            "Placeholder '[INSERT CONTACT METHOD]' should have been replaced "
            "with a real contact method.",
        )

    def test_mailto_href_matches_display_text(self):
        """The mailto: target must match the displayed email text exactly."""
        match = re.search(r"\[([^\]]+)\]\(mailto:([^)]+)\)", self.content)
        self.assertIsNotNone(
            match, "No mailto-style Markdown link found in CODE_OF_CONDUCT.md."
        )
        self.assertEqual(
            match.group(1),
            match.group(2),
            "Displayed email text and mailto: href must match exactly.",
        )

    def test_email_format_is_valid(self):
        """The reporting email must look like opensource-security@github.com."""
        self.assertRegex(
            self.content,
            r"[\w.+-]+@[\w-]+\.[\w.-]+",
            "No valid-looking email address found in CODE_OF_CONDUCT.md.",
        )
        self.assertIn("opensource-security@github.com", self.content)

    def test_important_alert_appears_after_enforcement_heading(self):
        """The [!IMPORTANT] block must live inside the '## Enforcement' section."""
        enforcement_idx = self.content.find("## Enforcement\n")
        self.assertNotEqual(
            enforcement_idx, -1, "Could not locate the '## Enforcement' heading."
        )
        alert_idx = self.content.find("> [!IMPORTANT]")
        guidelines_idx = self.content.find("## Enforcement Guidelines")
        self.assertGreater(
            alert_idx,
            enforcement_idx,
            "[!IMPORTANT] alert block must appear after the Enforcement heading.",
        )
        self.assertLess(
            alert_idx,
            guidelines_idx,
            "[!IMPORTANT] alert block must appear before Enforcement Guidelines.",
        )

    def test_blockquote_lines_well_formed(self):
        """Every line of the alert block must be a valid Markdown blockquote line."""
        block_match = re.search(
            r"(> \[!IMPORTANT\]\n(?:>.*\n?)*)", self.content
        )
        self.assertIsNotNone(block_match, "Could not isolate the alert block body.")
        for line in block_match.group(1).splitlines():
            self.assertTrue(
                line.startswith(">"),
                f"Alert block line does not start with '>': {line!r}",
            )

    def test_surrounding_enforcement_text_preserved(self):
        """Existing enforcement copy must survive the rewrite untouched."""
        self.assertIn(
            "All complaints will be reviewed and investigated promptly and fairly.",
            self.content,
        )
        self.assertIn(
            "reported to the community leaders responsible for enforcement.",
            self.content,
        )


class TestReadmeFooterLinks(unittest.TestCase):
    """Tests for README.md footer link localization and regressions."""

    def setUp(self):
        self.content = _read(README)

    def test_external_contributor_covenant_link_removed(self):
        """The old external Contributor Covenant CoC URL must no longer appear."""
        self.assertNotIn(
            "https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md",
            self.content,
            "README.md still links to the external Contributor Covenant CoC URL.",
        )

    def test_mit_license_link_preserved(self):
        """The MIT License footer link must remain unchanged."""
        self.assertIn(
            "[MIT License](https://gh.io/mit)",
            self.content,
            "MIT License link is missing or was altered in README.md.",
        )

    def test_copyright_notice_preserved(self):
        """The copyright notice in the footer must remain unchanged."""
        self.assertIn("&copy; 2026 GitHub", self.content)

    def test_footer_line_structure(self):
        """The full footer line must match copyright, CoC, and license bullets in order."""
        self.assertRegex(
            self.content,
            r"&copy; 2026 GitHub\s*&bull;\s*\[Code of Conduct\]\(CODE_OF_CONDUCT\.md\)"
            r"\s*&bull;\s*\[MIT License\]\(https://gh\.io/mit\)",
            "Footer line does not match the expected copyright/CoC/license structure.",
        )

    def test_coc_link_target_is_relative(self):
        """The Code of Conduct link target must be a relative path, not a URL."""
        match = re.search(r"\[Code of Conduct\]\(([^)]+)\)", self.content)
        self.assertIsNotNone(match, "Code of Conduct link not found in README.md.")
        target = match.group(1)
        self.assertFalse(
            target.startswith("http://") or target.startswith("https://"),
            f"Code of Conduct link should be a local relative path, got: {target!r}",
        )

    def test_coc_link_target_file_exists(self):
        """The file referenced by the README's Code of Conduct link must exist."""
        self.assertTrue(
            os.path.isfile(CODE_OF_CONDUCT),
            "README.md links to CODE_OF_CONDUCT.md, but the file does not exist.",
        )


class TestPaletteNewLocalizationEntry(unittest.TestCase):
    """Tests for the new 2026-06-15 palette entry documenting this PR's changes."""

    def setUp(self):
        self.content = _read(PALETTE_MD)

    def test_contains_new_date_heading(self):
        """The new entry must include the expected date in its heading."""
        self.assertIn(
            "2026-06-15",
            self.content,
            "Expected date '2026-06-15' not found in .Jules/palette.md.",
        )

    def test_new_heading_text_present(self):
        """The new heading must describe localizing policy links and contact methods."""
        self.assertIn(
            "Localize policy links and use accessible contact methods",
            self.content,
        )

    def test_new_learning_mentions_localizing(self):
        """The new learning note must mention localizing links to retain context."""
        self.assertIn("Localizing", self.content)
        self.assertIn("lose context", self.content)

    def test_new_action_mentions_readme_and_coc_files(self):
        """The new action note must reference both README.md and CODE_OF_CONDUCT.md."""
        self.assertIn("README.md", self.content)
        self.assertIn("CODE_OF_CONDUCT.md", self.content)

    def test_new_action_mentions_important_alert_and_mailto(self):
        """The new action note must call out the [!IMPORTANT] block and mailto link."""
        self.assertIn("[!IMPORTANT]", self.content)
        self.assertIn("mailto:", self.content)

    def test_new_entry_appears_after_earlier_entries(self):
        """Palette entries must be appended in chronological order."""
        idx_2024 = self.content.find("2024-05-24")
        idx_2026_05 = self.content.find("2026-05-27")
        idx_2026_06 = self.content.find("2026-06-15")
        self.assertNotEqual(idx_2024, -1)
        self.assertNotEqual(idx_2026_05, -1)
        self.assertNotEqual(idx_2026_06, -1)
        self.assertLess(
            idx_2024,
            idx_2026_05,
            "2024-05-24 entry should appear before the 2026-05-27 entry.",
        )
        self.assertLess(
            idx_2026_05,
            idx_2026_06,
            "2026-05-27 entry should appear before the new 2026-06-15 entry.",
        )


if __name__ == "__main__":
    unittest.main()