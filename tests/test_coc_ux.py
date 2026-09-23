import os
import sys
import unittest
from test_pr_accessibility import _read_cached, TrackingTestCase

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

from test_pr_accessibility import _read_cached, TrackingTestCase

REPO_ROOT = os.path.dirname(TESTS_DIR)
README_PATH = os.path.join(REPO_ROOT, "README.md")
COC_PATH = os.path.join(REPO_ROOT, "CODE_OF_CONDUCT.md")
CONTRIBUTING_PATH = os.path.join(REPO_ROOT, "CONTRIBUTING.md")


# Inherit from TrackingTestCase so test IDs are recorded in _PASSED_TESTS,
# enabling meta-test runners (e.g. TestRefactoredSuitesStillPass) to bypass redundant re-executions.
# Optimization: Inherit from TrackingTestCase to record passed test IDs in _PASSED_TESTS,
# ensuring global test tracking and preventing redundant suite re-executions in meta-tests.
class TestCoCUX(TrackingTestCase):
    @classmethod
    def setUpClass(cls):
        cls.coc_content = _read_cached(COC_PATH)
        cls.readme_content = _read_cached(README_PATH)
        cls.contributing_content = _read_cached(CONTRIBUTING_PATH)
        cls.content = cls.coc_content

    def test_readme_local_coc_link(self):
        self.assertIn("[Code of Conduct](CODE_OF_CONDUCT.md)", self.readme_content)

    def test_coc_reporting_instructions(self):
        self.assertNotIn("[INSERT CONTACT METHOD]", self.coc_content)
        self.assertIn("> [!IMPORTANT]", self.coc_content)
        self.assertIn("opensource-security@github.com", self.coc_content)
        self.assertIn("mailto:opensource-security@github.com", self.coc_content)

    def test_no_duplicate_enforcement_blocks(self):
        self.assertEqual(
            self.coc_content.count("> [!IMPORTANT]"),
            1,
            "CODE_OF_CONDUCT.md should contain exactly one > [!IMPORTANT] alert block.",
        )

    def test_contributing_coc_link(self):
        self.assertIn("CODE_OF_CONDUCT.md", self.contributing_content)


if __name__ == "__main__":
    unittest.main()
