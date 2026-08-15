"""
Tests for UX & accessibility across repository documentation files (README.md, SUPPORT.md,
PULL_REQUEST_TEMPLATE.md, issue templates, SECURITY.md).
"""

import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

from test_pr_accessibility import _read_cached, TrackingTestCase  # noqa: E402

REPO_ROOT = os.path.dirname(TESTS_DIR)
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
PR_TEMPLATE_PATH = os.path.join(REPO_ROOT, "PULL_REQUEST_TEMPLATE.md")
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")


class TestReadmeUX(TrackingTestCase):
    """Tests for README.md accessibility, links, and footer compliance."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(README_PATH)
        cls.readme_content = cls.content
        cls.contributing_content = _read_cached(CONTRIBUTING_PATH)
        cls.coc_content = _read_cached(COC_PATH)

    def test_alert_block_present(self):
        """README.md should contain an important alert block."""
        self.assertIn("> [!IMPORTANT]", self.readme_content)

    def test_descriptive_links(self):
        """Links in README.md should have descriptive anchor text."""
        self.assertIn("[skills.github.com](https://skills.github.com)", self.readme_content)
        self.assertIn("[organization profile](profile/README.md)", self.readme_content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.readme_content)
        self.assertIn(
            "[discussion in our community forum](https://github.com/orgs/skills/discussions)",
            self.readme_content,
        )

    def test_localized_coc_links(self):
        """README.md and CONTRIBUTING.md should link to local Code of Conduct."""
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

    def test_localized_links(self):
        """README.md should contain localized links for security, support, and license."""
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)
        self.assertIn("[Security Policy](SECURITY.md)", self.content)
        self.assertIn("[Support](SUPPORT.md)", self.content)
        self.assertIn("[MIT License](LICENSE)", self.content)

    def test_content_is_class_level_attribute(self):
        """After setUpClass refactor, content must be stored on class dict."""
        self.assertIn("content", TestReadmeUX.__dict__)

    def test_content_accessible_via_instance(self):
        """Class-level content must be accessible via self in test methods."""
        self.assertIs(self.content, TestReadmeUX.__dict__["content"])


class TestSupportUX(TrackingTestCase):
    """Tests for SUPPORT.md UX improvements."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SUPPORT_PATH)

    def test_typo_fix(self):
        """SUPPORT.md typo 'feaure' should be fixed to 'feature'."""
        self.assertIn("feature request", self.content)
        self.assertNotIn("feaure request", self.content)

    def test_alert_blocks_present(self):
        """SUPPORT.md should contain > [!TIP] and > [!NOTE] alert blocks."""
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("> [!NOTE]", self.content)

    def test_clean_title(self):
        """Title should be level-1 heading without trailing spaces."""
        self.assertTrue(self.content.startswith("# Support\n"))

    def test_community_forum_link(self):
        """Community forum link should point to discussions."""
        self.assertIn("[ask on our community forum](https://github.com/orgs/skills/discussions)", self.content)


class TestPullRequestTemplateUX(TrackingTestCase):
    """Tests for PULL_REQUEST_TEMPLATE.md UX improvements."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(PR_TEMPLATE_PATH)

    def test_alert_block_present(self):
        """PR template should contain a > [!NOTE] alert block."""
        self.assertIn("> [!NOTE]", self.content)

    def test_summary_section_present(self):
        """PR template should contain summary and task sections."""
        self.assertIn("### Summary", self.content)


class TestBugReportUX(TrackingTestCase):
    """Tests for bug_report.md issue template."""

    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "bug_report.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        """Bug report template should contain a tip alert block encouraging search."""
        self.assertIn("> [!TIP]", self.content)


class TestFeatureRequestUX(TrackingTestCase):
    """Tests for feature_request.md issue template."""

    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "feature_request.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        """Feature request template should contain a tip alert block encouraging search."""
        self.assertIn("> [!TIP]", self.content)


class TestSecurityUX(TrackingTestCase):
    """Tests for SECURITY.md UX improvements."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SECURITY_PATH)

    def test_security_starts_with_h1_heading(self):
        """SECURITY.md must start with '# Security Policy'."""
        self.assertTrue(self.content.startswith("# Security Policy\n"))


if __name__ == "__main__":
    unittest.main()
