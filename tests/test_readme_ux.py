import os
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
SUPPORT_PATH = os.path.join(REPO_ROOT, "SUPPORT.md")
PULL_REQUEST_TEMPLATE_PATH = os.path.join(REPO_ROOT, "PULL_REQUEST_TEMPLATE.md")
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

class TestReadmeUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Read file once for all tests in this class to reduce I/O.
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Optimization: Read file once per class instead of once per test.
        # Reduces openat() calls from 3 to 1 for this class.
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Optimization: Read file once per class to reduce disk I/O.
        # Reduces openat() calls from 3 to 1 for this class.
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # PERFORMANCE: Read README.md once for the entire class instead of per test method.
        # This reduces openat() calls for README.md from 3 to 1.
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Optimization: Read file once for all tests in this class to reduce redundant I/O.
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Read the file once for all tests in this class to reduce I/O overhead
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Cache content to reduce file I/O from O(N_tests) to O(1)
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Optimization: Read the file once for all tests in this class
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Optimization: Read file once per class instead of once per test.
        # Reduces openat() system calls from O(N_tests) to O(1).
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Optimization: read the file once for all tests in this class to reduce redundant I/O.
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        # Optimization: Read file once per class to reduce openat() calls
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.readme_content = f.read()
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            cls.contributing_content = f.read()
        with open(COC_PATH, "r", encoding="utf-8") as f:
            cls.coc_content = f.read()
        # Optimization: Read file content once at the class level to reduce openat() syscalls
        with open(README_PATH, "r", encoding="utf-8") as f:
            cls.content = f.read()
from test_pr_accessibility import _read_cached, TrackingTestCase

class TestReadmeUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Use the centralized in-memory cache _read_cached
        # to ensure the file is read from disk exactly once across the whole suite.
        cls.content = _read_cached(README_PATH)

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.readme_content)
        self.assertIn("> This repository is not a course.", self.readme_content)

    def test_descriptive_links(self):
        self.assertIn("[skills.github.com](https://skills.github.com)", self.readme_content)
        self.assertIn("[organization profile](profile/README.md)", self.readme_content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.readme_content)

    def test_localized_coc_links(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

    def test_coc_contact_info(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)
        self.assertIn("[skills.github.com](https://skills.github.com)", self.content)
        self.assertIn("[organization profile](profile/README.md)", self.content)
        self.assertIn("[GitHub Skills content model](https://skills.github.com/content-model)", self.content)
        self.assertIn("[Code of Conduct](./CODE_OF_CONDUCT.md)", self.content)
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)
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

    def test_localized_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

    def test_copyright_year(self):
        self.assertIn("&copy; 2026 GitHub", self.readme_content)

    def test_localized_links(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)
        self.assertIn("[MIT License](LICENSE)", self.content)

class TestSupportUX(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(REPO_ROOT, "SUPPORT.md"), "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_typo_fix(self):
        self.assertIn("feature request", self.content)
        self.assertNotIn("feaure request", self.content)
    def test_localized_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

    def test_localized_security_link(self):
        self.assertIn("[Security Policy](SECURITY.md)", self.content)

    def test_localized_support_link(self):
        self.assertIn("[Support](SUPPORT.md)", self.content)

    def test_localized_license_link(self):
        self.assertIn("[MIT License](LICENSE)", self.content)

    def test_localized_security_link(self):
        self.assertIn("[Security Policy](SECURITY.md)", self.content)

    def test_localized_support_link(self):
        self.assertIn("[Support](SUPPORT.md)", self.content)

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

    def test_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

class TestOtherDocsUX(unittest.TestCase):
    def test_support_typo_fixed(self):
        with open(SUPPORT_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("feature request", content)
        self.assertNotIn("feaure request", content)

    def test_coc_alert_and_email(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("> [!IMPORTANT]", content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", content)
        self.assertNotIn("[INSERT CONTACT METHOD]", content)

    def test_contributing_coc_link(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", content)


class TestCodeOfConductUX(unittest.TestCase):
    def setUp(self):
        coc_path = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
        with open(coc_path, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.content)

    def test_contact_email_present(self):
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

    def test_no_placeholder(self):
        self.assertNotIn("[INSERT CONTACT METHOD]", self.content)


class TestCodeOfConductUX(unittest.TestCase):
    def setUp(self):
        coc_path = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
        with open(coc_path, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_contact_method_alert(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)

    def test_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.content)

class TestCodeOfConductUX(unittest.TestCase):
    def setUp(self):
        self.coc_path = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
        self.contributing_path = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

        with open(self.coc_path, "r", encoding="utf-8") as f:
            self.coc_content = f.read()
        with open(self.contributing_path, "r", encoding="utf-8") as f:
            self.contributing_content = f.read()

    def test_coc_alert_block_present(self):
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.coc_content)

    def test_contributing_local_coc_link(self):
        self.assertIn("[Contributor Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

class TestCodeOfConductUX(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        coc_path = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
        with open(coc_path, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_coc_reporting_instructions(self):
        self.assertIn("> [!IMPORTANT]", self.content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", self.content)
        self.assertNotIn("[INSERT CONTACT METHOD]", self.content)

class TestCoCUX(unittest.TestCase):
    def test_coc_alert_and_mailto(self):
        with open(COC_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("> [!IMPORTANT]", content)
        self.assertIn("[opensource-security@github.com](mailto:opensource-security@github.com)", content)

    def test_contributing_coc_link(self):
        with open(CONTRIBUTING_PATH, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("[Contributor Code of Conduct](CODE_OF_CONDUCT.md)", content)

if __name__ == "__main__":
    unittest.main()
