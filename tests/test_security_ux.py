import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

from test_pr_accessibility import _read_cached, TrackingTestCase  # noqa: E402

REPO_ROOT = os.path.dirname(TESTS_DIR)
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")


class TestSecurityUX(TrackingTestCase):
    """Tests for Security Policy UX improvements."""

    @classmethod
    def setUpClass(cls):
        # Optimization: Use the centralized in-memory cache _read_cached
        # to ensure the file is read from disk exactly once across the whole suite.
        cls.content = _read_cached(SECURITY_PATH)

    def test_security_starts_with_h1_heading(self):
        """SECURITY.md must start with a level-1 heading '# Security Policy'."""
        self.assertTrue(
            self.content.startswith("# Security Policy\n"),
            "SECURITY.md must start with '# Security Policy'.",
        )

    def test_warning_alert_block_present(self):
        """Verify that the critical security warning is in a GitHub-native alert block."""
        self.assertIn("> [!WARNING]", self.content)
        self.assertIn(
            "Please do not report security vulnerabilities through public GitHub issues",
            self.content,
        )

    def test_mailto_link_present(self):
        """Verify that the security email is formatted as a mailto: link."""
        self.assertIn(
            "[opensource-security@github.com](mailto:opensource-security@github.com)",
            self.content,
        )

    def test_old_bold_warning_removed(self):
        """Verify that the old plain bold warning line is removed in favor of the alert block."""
        self.assertNotIn(
            "**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**",
            self.content,
        )


if __name__ == "__main__":
    unittest.main()
