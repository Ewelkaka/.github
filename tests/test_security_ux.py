import os
import unittest
import re
from test_pr_accessibility import _read_cached, TrackingTestCase

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECURITY_PATH = os.path.join(REPO_ROOT, "SECURITY.md")

# Module-level pre-compiled regex objects for efficient search operations.
RE_WARNING_ALERT = re.compile(r"> \[!WARNING\]", re.IGNORECASE)
RE_MAILTO_LINK = re.compile(r"\[opensource-security@github\.com\]\(mailto:opensource-security@github\.com\)")


class TestSecurityUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Read file once per class via centralized _read_cached helper
        cls.content = _read_cached(SECURITY_PATH)

    def test_warning_alert_block_present(self):
        """Verify that the warning alert block is present in SECURITY.md."""
        self.assertIsNotNone(RE_WARNING_ALERT.search(self.content))
        self.assertIn("Please do not report security vulnerabilities through public GitHub issues", self.content)

    def test_mailto_link_present(self):
        """Verify that the security email is a mailto: link."""
        self.assertIsNotNone(RE_MAILTO_LINK.search(self.content))

    def test_no_bold_warning(self):
        """Verify that the old bold warning is removed."""
        self.assertNotIn("**Please do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**", self.content)


if __name__ == "__main__":
    unittest.main()
