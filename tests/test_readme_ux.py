import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
PULL_REQUEST_TEMPLATE_PATH = os.path.join(REPO_ROOT, "PULL_REQUEST_TEMPLATE.md")

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
        self.assertIn("[ask on our community forum](https://github.com/skills/.github/discussions)", self.content)

class TestPullRequestTemplateUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Use the centralized in-memory cache _read_cached
        # to ensure the file is read from disk exactly once across the whole suite.
        cls.content = _read_cached(PULL_REQUEST_TEMPLATE_PATH)

    def test_alert_block_present(self):
        self.assertIn("> [!NOTE]", self.content)

class TestBugReportUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "bug_report.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("Please search existing issues and discussions", self.content)

class TestFeatureRequestUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "feature_request.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("Please search existing feature requests and discussions", self.content)

if __name__ == "__main__":
    unittest.main()
