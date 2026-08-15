"""
Tests for README, Support, PR template, Bug report, Feature request, and Security UX.
"""

import os
import unittest
from test_pr_accessibility import TrackingTestCase, _read_cached

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
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("This repository is not a course.", self.content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.content)
        self.assertIn("[organization profile](profile/README.md)", self.content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.content)
        self.assertIn("[discussion in our community forum](https://github.com/orgs/skills/discussions)", self.content)

    def test_localized_links(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)
        self.assertIn("[Security Policy](SECURITY.md)", self.content)
        self.assertIn("[Support](SUPPORT.md)", self.content)
        self.assertIn("[MIT License](LICENSE)", self.content)

    def test_content_is_class_level_attribute(self):
        self.assertIn("content", TestReadmeUX.__dict__)

    def test_content_accessible_via_instance(self):
        self.assertIs(self.content, TestReadmeUX.__dict__["content"])


class TestSupportUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SUPPORT_PATH)

    def test_alert_blocks_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("> [!NOTE]", self.content)

    def test_clean_title(self):
        self.assertTrue(self.content.startswith("# Support\n"))

    def test_community_forum_link(self):
        self.assertIn("[ask on our community forum](https://github.com/orgs/skills/discussions)", self.content)

    def test_direct_active_links(self):
        self.assertIn("[GitHub issues](https://github.com/skills/.github/issues)", self.content)
        self.assertIn("[existing issues](https://github.com/skills/.github/issues)", self.content)
        self.assertIn("[new issue](https://github.com/skills/.github/issues/new/choose)", self.content)

    def test_security_policy_link(self):
        self.assertIn("[Security Policy](SECURITY.md)", self.content)


class TestPullRequestTemplateUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(PR_TEMPLATE_PATH)

    def test_alert_block_present(self):
        self.assertIn("> [!NOTE]", self.content)
        self.assertIn("If there's an existing issue for your change", self.content)

    def test_task_list_present(self):
        self.assertIn("- [ ] For workflow changes", self.content)
        self.assertIn("- [ ] For content changes", self.content)


class TestBugReportUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "bug_report.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("Please search [existing issues](https://github.com/skills/.github/issues) and [discussions](https://github.com/skills/.github/discussions)", self.content)


class TestFeatureRequestUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.path = os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "feature_request.md")
        cls.content = _read_cached(cls.path)

    def test_alert_block_present(self):
        self.assertIn("> [!TIP]", self.content)
        self.assertIn("Please search [existing feature requests](https://github.com/skills/.github/issues?q=is%3Aissue+label%3Afeature) and [discussions](https://github.com/skills/.github/discussions)", self.content)


class TestSecurityUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = _read_cached(SECURITY_PATH)

    def test_security_starts_with_h1_heading(self):
        self.assertTrue(self.content.startswith("# Security Policy\n"))


if __name__ == "__main__":
    unittest.main()
