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

    def setUp(self):
        self.coc_content = _read(CODE_OF_CONDUCT)
        self.readme_content = _read(README)

    def test_coc_contains_email_link(self):
        """CODE_OF_CONDUCT.md must contain the reporting email as a mailto link."""
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            self.coc_content,
            "Reporting email mailto link not found in CODE_OF_CONDUCT.md.",
        )

    def test_coc_uses_important_alert(self):
        """CODE_OF_CONDUCT.md must use an [!IMPORTANT] alert for the contact method."""
        self.assertIn(
            "> [!IMPORTANT]",
            self.coc_content,
            "Expected [!IMPORTANT] alert block not found in CODE_OF_CONDUCT.md.",
        )

    def test_readme_links_to_local_coc(self):
        """README.md must link to the local CODE_OF_CONDUCT.md file."""
        self.assertIn(
            "[Code of Conduct](CODE_OF_CONDUCT.md)",
            self.readme_content,
            "README.md does not link to the local CODE_OF_CONDUCT.md file.",
        )

    def test_coc_placeholder_contact_method_removed(self):
        """The old '[INSERT CONTACT METHOD]' placeholder must no longer exist."""
        self.assertNotIn(
            "[INSERT CONTACT METHOD]",
            self.coc_content,
            "Placeholder '[INSERT CONTACT METHOD]' should have been replaced "
            "with a real contact method in CODE_OF_CONDUCT.md.",
        )

    def test_coc_mailto_href_matches_display_text(self):
        """The mailto link target must match its displayed link text exactly."""
        match = re.search(
            r"\[([^\]]+)\]\(mailto:([^)]+)\)", self.coc_content
        )
        self.assertIsNotNone(
            match,
            "No mailto link found in CODE_OF_CONDUCT.md.",
        )
        display_text, href = match.group(1), match.group(2)
        self.assertEqual(
            display_text,
            href,
            f"Mailto link display text '{display_text}' does not match "
            f"href target '{href}'.",
        )

    def test_coc_alert_appears_under_enforcement_section(self):
        """The [!IMPORTANT] alert must appear within the Enforcement section,
        before the complaints-review sentence."""
        enforcement_idx = self.coc_content.index("## Enforcement\n")
        alert_idx = self.coc_content.index("> [!IMPORTANT]")
        complaints_idx = self.coc_content.index(
            "All complaints will be reviewed"
        )
        self.assertTrue(
            enforcement_idx < alert_idx < complaints_idx,
            "Expected the [!IMPORTANT] alert to be located between the "
            "'## Enforcement' heading and the complaints-review sentence.",
        )

    def test_coc_alert_includes_reporting_instruction_text(self):
        """The alert block must explain how to report an incident, not just
        contain a bare email address."""
        self.assertIn(
            "To report an incident, please email community leaders at",
            self.coc_content,
            "Expected reporting instruction sentence not found alongside "
            "the mailto link in CODE_OF_CONDUCT.md.",
        )

    def test_coc_enforcement_section_still_present(self):
        """Surrounding Enforcement content must be preserved (regression guard)."""
        self.assertIn(
            "All complaints will be reviewed and investigated promptly and fairly.",
            self.coc_content,
        )
        self.assertIn(
            "All community leaders are obligated to respect the privacy and "
            "security of the",
            self.coc_content,
        )

    def test_readme_no_longer_links_external_coc(self):
        """README.md must not link to the external Contributor Covenant URL anymore."""
        self.assertNotIn(
            "https://www.contributor-covenant.org/version/2/1/code_of_conduct/"
            "code_of_conduct.md",
            self.readme_content,
            "README.md still links to the external Contributor Covenant URL; "
            "it should link to the local CODE_OF_CONDUCT.md instead.",
        )

    def test_readme_footer_line_structure(self):
        """The README footer must retain copyright, CoC, and license links
        separated by the bullet HTML entity, in that order."""
        footer_pattern = (
            r"&copy;\s*2026\s*GitHub\s*&bull;\s*"
            r"\[Code of Conduct\]\(CODE_OF_CONDUCT\.md\)\s*&bull;\s*"
            r"\[MIT License\]\(https://gh\.io/mit\)"
        )
        self.assertRegex(
            self.readme_content,
            footer_pattern,
            "README.md footer line no longer matches the expected "
            "copyright / Code of Conduct / MIT License structure.",
        )

    def test_coc_file_not_empty_after_edit(self):
        """CODE_OF_CONDUCT.md must still contain substantial content."""
        self.assertGreater(
            len(self.coc_content.strip()),
            0,
            "CODE_OF_CONDUCT.md is unexpectedly empty.",
        )


class TestPaletteLocalizationEntry(unittest.TestCase):
    """Tests for the new palette.md entry documenting the CoC/README change."""

    def setUp(self):
        self.content = _read(PALETTE_MD)

    def test_contains_new_entry_date(self):
        """The new palette entry must include its date heading."""
        self.assertIn(
            "2026-06-15",
            self.content,
            "Expected date '2026-06-15' not found in .Jules/palette.md.",
        )

    def test_new_entry_heading_text(self):
        """The new entry heading must describe localizing policy links."""
        self.assertIn(
            "## 2026-06-15 - Localize policy links and use accessible contact methods",
            self.content,
            "Expected heading for the new palette entry not found.",
        )

    def test_new_entry_learning_mentions_context_loss(self):
        """The Learning note must explain the localization rationale."""
        idx = self.content.index("## 2026-06-15")
        entry = self.content[idx:]
        self.assertIn(
            "lose context",
            entry,
            "Expected explanation about losing context not found in the "
            "2026-06-15 palette entry.",
        )

    def test_new_entry_action_references_both_files(self):
        """The Action note must reference both README.md and CODE_OF_CONDUCT.md."""
        idx = self.content.index("## 2026-06-15")
        entry = self.content[idx:]
        self.assertIn("`README.md`", entry)
        self.assertIn("`CODE_OF_CONDUCT.md`", entry)

    def test_new_entry_action_mentions_important_alert(self):
        """The Action note must mention the [!IMPORTANT] alert convention."""
        idx = self.content.index("## 2026-06-15")
        entry = self.content[idx:]
        self.assertIn(
            "[!IMPORTANT]",
            entry,
            "Expected reference to the [!IMPORTANT] alert block not found "
            "in the 2026-06-15 palette entry.",
        )

    def test_previous_entries_still_present(self):
        """Earlier palette entries must not be removed by the new addition."""
        self.assertIn("## 2024-05-24", self.content)
        self.assertIn("## 2026-04-02", self.content)
        self.assertIn("## 2026-05-27", self.content)

    def test_entries_appear_in_chronological_order(self):
        """Palette entries must be appended in order, with the newest last."""
        dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})", self.content, re.MULTILINE)
        self.assertEqual(
            dates,
            sorted(dates),
            "Palette entries are not in chronological order.",
        )


if __name__ == "__main__":
    unittest.main()