import os
import unittest
import re
from test_pr_accessibility import _read_cached, TrackingTestCase

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")

# Pre-compiled module-level regex objects for fast matching across tests
RE_TIP_ALERT = re.compile(r"> \[!TIP\]", re.IGNORECASE)


class TestContributingUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        # Optimization: Read file once per class using _read_cached to optimize I/O
        cls.content = _read_cached(CONTRIBUTING_PATH)

    def test_resource_tip_block_present(self):
        """The Resources section should use a [!TIP] alert block."""
        self.assertIsNotNone(RE_TIP_ALERT.search(self.content))
        self.assertIn("**Check out these resources to help you get started:**", self.content)

    def test_resource_links_present(self):
        """The resource links should be present within the document."""
        self.assertIn("[How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)", self.content)
        self.assertIn("[Using Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)", self.content)
        self.assertIn("[GitHub Docs](https://docs.github.com/)", self.content)


if __name__ == "__main__":
    unittest.main()
