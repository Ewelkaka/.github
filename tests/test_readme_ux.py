"""
Tests for README and documentation UX improvements.
"""

import os
import unittest
from test_pr_accessibility import _read_cached, TrackingTestCase

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
PR_TEMPLATE_PATH = os.path.join(REPO_ROOT, "PULL_REQUEST_TEMPLATE.md")
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")


class TestReadmeUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(README_PATH)
        cls.readme_content = cls.content
        cls.coc_content = _read_cached(COC_PATH)
        cls.contributing_content = _read_cached(CONTRIBUTING_PATH)

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.readme_content)
        self.assertIn("> This repository is not a course.", self.readme_content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.readme_content)
        self.assertIn("[organization profile](profile/README.md)", self.readme_content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.readme_content)
        self.assertIn(
            "[discussion in our community forum](https://github.com/orgs/skills/discussions)",
            self.readme_content,
        )

    def test_localized_coc_links(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertIn("CODE_OF_CONDUCT.md", self.contributing_content)

    def test_copyright_year(self):
        self.assertIn("&copy; 2026 GitHub", self.readme_content)

    def test_localized_links(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertIn("[MIT License](LICENSE)", self.readme_content)
        self.assertIn("[Security Policy](SECURITY.md)", self.readme_content)
        self.assertIn("[Support](SUPPORT.md)", self.readme_content)


class TestSupportUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SUPPORT_PATH)

    def test_typo_fix(self):
        self.assertIn("feature request", self.content)
        self.assertNotIn("feaure request", self.content)

    def test_alert_blocks_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("> [!NOTE]", self.content)

    def test_clean_title(self):
        self.assertTrue(self.content.startswith("# Support\n"))

    def test_community_forum_link(self):
        self.assertIn("[ask on our community forum](https://github.com/orgs/skills/discussions)", self.content)

    def test_interactive_issue_links(self):
        self.assertIn("[GitHub issues](https://github.com/skills/.github/issues)", self.content)


class TestPullRequestTemplateUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(PR_TEMPLATE_PATH)

    def test_alert_block_present(self):
        self.assertIn("> [!NOTE]", self.content)

    def test_interactive_issue_link(self):
        self.assertIn("[open a new issue](https://github.com/skills/.github/issues/new/choose)", self.content)


class TestBugReportUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "bug_report.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("[search existing issues](https://github.com/skills/.github/issues)", self.content)


class TestFeatureRequestUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "feature_request.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)


class TestSecurityUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SECURITY_PATH)

    def test_security_starts_with_h1_heading(self):
        self.assertTrue(
            self.content.startswith("# Security Policy\n"),
            "SECURITY.md must start with '# Security Policy'."
        )


if __name__ == "__main__":
    unittest.main()
