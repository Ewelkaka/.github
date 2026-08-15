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


class TestCoCUX(TrackingTestCase):
    """Tests for Code of Conduct UX and localized linking."""

    @classmethod
    def setUpClass(cls):
        # Optimization: Read and cache files at class level using centralized LRU cache.
        cls.coc_content = _read_cached(COC_PATH)
        cls.readme_content = _read_cached(README_PATH)
        cls.contributing_content = _read_cached(CONTRIBUTING_PATH)
        cls.support_content = _read_cached(SUPPORT_PATH)
        cls.content = cls.coc_content

    def test_readme_link_is_local(self):
        """The README footer should link to the local CODE_OF_CONDUCT.md."""
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)
        self.assertNotIn(
            "https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md",
            self.readme_content,
        )

    def test_coc_contact_info(self):
        """The Code of Conduct should have the correct security contact email."""
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            self.coc_content,
        )
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)

    def test_coc_alert_block(self):
        """The Enforcement section in CoC should be wrapped in an IMPORTANT alert block."""
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn(
            "Instances of abusive, harassing, or otherwise unacceptable behavior",
            self.coc_content,
        )

    def test_contributing_coc_link(self):
        """CONTRIBUTING.md should link to the local Code of Conduct."""
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.contributing_content)

    def test_support_typo_fix(self):
        """SUPPORT.md should have typo 'feaure' corrected to 'feature'."""
        self.assertIn("feature request", self.support_content)
        self.assertNotIn("feaure request", self.support_content)


if __name__ == "__main__":
    unittest.main()
