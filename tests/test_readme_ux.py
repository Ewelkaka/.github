import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
PULL_REQUEST_TEMPLATE_PATH = os.path.join(REPO_ROOT, "PULL_REQUEST_TEMPLATE.md")
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

from test_pr_accessibility import _read_cached, TrackingTestCase

class TestReadmeUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Use the centralized in-memory cache _read_cached
        # to ensure the file is read from disk exactly once across the whole suite.
        cls.content = _read_cached(README_PATH)

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("> This repository is not a course.", self.content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.content)
        self.assertIn("[organization profile](profile/README.md)", self.content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.content)
        self.assertNotIn(
            "[discussion](https://github.com",
            self.content,
            "Expected 'discussion' link text in README.md to be updated with descriptive anchor text for accessibility."
        )
        self.assertIn(
            "[discussion in our community forum](https://github.com/orgs/skills/discussions)",
            self.content,
            "Expected descriptive anchor text 'discussion in our community forum' for the feedback link in README.md."
        )

    def test_copyright_year(self):
        self.assertIn("&copy; 2026 GitHub", self.content)

    def test_localized_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

    def test_localized_license_link(self):
        self.assertIn("[MIT License](LICENSE)", self.content)

class TestSupportUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Use the centralized in-memory cache _read_cached
        # to ensure the file is read from disk exactly once across the whole suite.
        cls.content = _read_cached(SUPPORT_PATH)

    def test_alert_blocks_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("> [!NOTE]", self.content)

    def test_clean_title(self):
        # Ensure no trailing space in title
        self.assertTrue(self.content.startswith("# Support\n"))

    def test_community_forum_link(self):
        self.assertIn("[ask on our community forum](https://github.com/orgs/skills/discussions)", self.content)

    def test_interactive_issue_links(self):
        self.assertIn("[GitHub issues](https://github.com/skills/.github/issues)", self.content)
        self.assertIn("[search the existing issues](https://github.com/skills/.github/issues)", self.content)
    def test_direct_active_links(self):
        self.assertIn("[GitHub issues](https://github.com/skills/.github/issues)", self.content)
        self.assertIn("[existing issues](https://github.com/skills/.github/issues)", self.content)
        self.assertIn("[new issue](https://github.com/skills/.github/issues/new/choose)", self.content)

class TestPullRequestTemplateUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Use the centralized in-memory cache _read_cached
        # to ensure the file is read from disk exactly once across the whole suite.
        cls.content = _read_cached(PULL_REQUEST_TEMPLATE_PATH)

    def test_alert_block_present(self):
        self.assertIn("> [!NOTE]", self.content)

    def test_interactive_issue_link(self):
        self.assertIn("[open a new issue](https://github.com/skills/.github/issues/new/choose)", self.content)
    def test_direct_active_links(self):
        self.assertIn("[open one first](https://github.com/skills/.github/issues/new/choose)", self.content)

class TestBugReportUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "bug_report.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("[search existing issues](https://github.com/skills/.github/issues)", self.content)
        self.assertIn("[discussions](https://github.com/skills/.github/discussions)", self.content)
        self.assertIn("Please search [existing issues](https://github.com/skills/.github/issues) and [discussions](https://github.com/skills/.github/discussions)", self.content)

class TestFeatureRequestUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "feature_request.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("[search existing feature requests](https://github.com/skills/.github/issues?q=is%3Aissue+label%3Afeature)", self.content)
        self.assertIn("[discussions](https://github.com/skills/.github/discussions)", self.content)
        self.assertIn("Please search [existing feature requests](https://github.com/skills/.github/issues?q=is%3Aissue+label%3Afeature) and [discussions](https://github.com/skills/.github/discussions)", self.content)

class TestSecurityUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Use the centralized in-memory cache _read_cached
        # to ensure the file is read from disk exactly once across the whole suite.
        cls.content = _read_cached(SECURITY_PATH)

    def test_security_starts_with_h1_heading(self):
        """SECURITY.md must start with a level-1 heading '# Security Policy'."""
        self.assertTrue(
            self.content.startswith("# Security Policy\n"),
            "SECURITY.md must start with a level-1 heading '# Security Policy' for screen reader accessibility."
        )

if __name__ == "__main__":
    unittest.main()
