"""
Tests for PR: Reduce redundant file I/O in test suite

Covers:
  - .jules/bolt.md: new journal entry documenting the setUp -> setUpClass
    optimization.
  - tests/test_pr_accessibility.py: TestProfileReadmeAltText and
    TestPaletteMarkdown now load their fixture content once per class via
    setUpClass instead of once per test via setUp.
  - tests/test_readme_ux.py: TestReadmeUX now loads README.md once per class
    via setUpClass instead of once per test via setUp.
"""

import os
import sys
import unittest
from unittest import mock

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOLT_MD = os.path.join(REPO_ROOT, ".jules", "bolt.md")

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

import test_pr_accessibility  # noqa: E402
import test_readme_ux  # noqa: E402


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


class TestBoltJournalMarkdown(unittest.TestCase):
    """Tests for the new .jules/bolt.md file."""

    @classmethod
    def setUpClass(cls):
        cls.content = _read(BOLT_MD)

    def test_file_exists(self):
        """.jules/bolt.md must exist in the repository."""
        self.assertTrue(os.path.isfile(BOLT_MD), ".jules/bolt.md does not exist.")

    def test_title_present(self):
        """The journal must start with its title heading."""
        self.assertIn("# Bolt's Journal", self.content)

    def test_contains_date_heading(self):
        """The journal entry must include the expected date."""
        self.assertIn("2026-07-15", self.content)

    def test_heading_describes_topic(self):
        """The heading must describe the file I/O reduction topic."""
        self.assertIn("Reduce redundant file I/O in test suites", self.content)

    def test_learning_section_present(self):
        """The file must contain a Learning section."""
        self.assertIn("**Learning:**", self.content)

    def test_learning_mentions_setup_methods(self):
        """The learning note must reference both setUp() and setUpClass."""
        self.assertIn("setUp()", self.content)
        self.assertIn("setUpClass", self.content)

    def test_learning_mentions_unittest(self):
        """The learning note must reference the unittest module."""
        self.assertIn("unittest", self.content)

    def test_action_section_present(self):
        """The file must contain an Action section."""
        self.assertIn("**Action:**", self.content)

    def test_action_recommends_setupclass(self):
        """The action note must recommend setUpClass for static test data."""
        self.assertIn("setUpClass", self.content)

    def test_file_is_not_empty(self):
        """The journal entry must not be empty."""
        self.assertGreater(len(self.content.strip()), 0, ".jules/bolt.md is empty.")

    def test_file_starts_with_markdown_heading(self):
        """The file must start with a level-1 markdown heading."""
        self.assertTrue(
            self.content.startswith("# "),
            "File should start with a level-1 markdown heading.",
        )


def _run_suite_quietly(test_case_class):
    """Run every test method of test_case_class and return the TestResult."""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    with open(os.devnull, "w") as devnull:
        runner = unittest.TextTestRunner(stream=devnull, verbosity=0)
        return runner.run(suite)


class TestAccessibilitySetUpClassRefactor(unittest.TestCase):
    """Verify the setUp -> setUpClass optimization applied to
    TestProfileReadmeAltText and TestPaletteMarkdown in
    tests/test_pr_accessibility.py.
    """

    def _assert_uses_setupclass_not_setup(self, cls):
        self.assertIn(
            "setUpClass", vars(cls), f"{cls.__name__} should define setUpClass."
        )
        self.assertNotIn(
            "setUp", vars(cls), f"{cls.__name__} should no longer define setUp."
        )

    def test_profile_readme_uses_setupclass_not_setup(self):
        self._assert_uses_setupclass_not_setup(
            test_pr_accessibility.TestProfileReadmeAltText
        )

    def test_palette_markdown_uses_setupclass_not_setup(self):
        self._assert_uses_setupclass_not_setup(
            test_pr_accessibility.TestPaletteMarkdown
        )

    def test_profile_readme_content_is_shared_across_test_instances(self):
        """cls.content set by setUpClass must be a single shared object,
        not re-created per instance the way setUp would."""
        cls = test_pr_accessibility.TestProfileReadmeAltText
        self.addCleanup(delattr, cls, "content")
        cls.setUpClass()

        first = cls("test_img_tag_present")
        second = cls("test_img_src_unchanged")

        self.assertIs(first.content, second.content)
        self.assertEqual(
            first.content,
            test_pr_accessibility._read(test_pr_accessibility.PROFILE_README),
        )

    def test_palette_markdown_content_is_shared_across_test_instances(self):
        cls = test_pr_accessibility.TestPaletteMarkdown
        self.addCleanup(delattr, cls, "content")
        cls.setUpClass()

        first = cls("test_file_exists")
        second = cls("test_learning_section_present")

        self.assertIs(first.content, second.content)

    def test_profile_readme_file_is_read_only_once_for_full_class_run(self):
        """The whole point of the refactor: one file read for the entire
        class run, regardless of the number of test methods."""
        cls = test_pr_accessibility.TestProfileReadmeAltText
        self.addCleanup(delattr, cls, "content")
        real_read = test_pr_accessibility._read

        with mock.patch.object(
            test_pr_accessibility, "_read", wraps=real_read
        ) as mocked_read:
            result = _run_suite_quietly(cls)

        self.assertTrue(result.wasSuccessful())
        self.assertGreater(result.testsRun, 1)
        self.assertEqual(mocked_read.call_count, 1)

    def test_palette_markdown_file_is_read_only_once_for_full_class_run(self):
        cls = test_pr_accessibility.TestPaletteMarkdown
        self.addCleanup(delattr, cls, "content")
        real_read = test_pr_accessibility._read

        with mock.patch.object(
            test_pr_accessibility, "_read", wraps=real_read
        ) as mocked_read:
            result = _run_suite_quietly(cls)

        self.assertTrue(result.wasSuccessful())
        self.assertGreater(result.testsRun, 1)
        self.assertEqual(mocked_read.call_count, 1)


class TestReadmeUxSetUpClassRefactor(unittest.TestCase):
    """Verify the setUp -> setUpClass optimization applied to TestReadmeUX
    in tests/test_readme_ux.py.
    """

    def test_readme_ux_uses_setupclass_not_setup(self):
        cls = test_readme_ux.TestReadmeUX
        self.assertIn("setUpClass", vars(cls))
        self.assertNotIn("setUp", vars(cls))

    def test_readme_ux_content_is_shared_across_test_instances(self):
        cls = test_readme_ux.TestReadmeUX
        self.addCleanup(delattr, cls, "content")
        cls.setUpClass()

        first = cls("test_alert_block_present")
        second = cls("test_copyright_year")

        self.assertIs(first.content, second.content)
        with open(test_readme_ux.README_PATH, "r", encoding="utf-8") as f:
            expected = f.read()
        self.assertEqual(first.content, expected)

    def test_readme_ux_file_is_opened_only_once_for_full_class_run(self):
        cls = test_readme_ux.TestReadmeUX
        self.addCleanup(delattr, cls, "content")
        real_open = open
        open_calls = []

        def counting_open(*args, **kwargs):
            if args and args[0] == test_readme_ux.README_PATH:
                open_calls.append(args)
            return real_open(*args, **kwargs)

        with open(os.devnull, "w") as devnull:
            with mock.patch("builtins.open", side_effect=counting_open):
                suite = unittest.TestLoader().loadTestsFromTestCase(cls)
                runner = unittest.TextTestRunner(stream=devnull, verbosity=0)
                result = runner.run(suite)

        self.assertTrue(result.wasSuccessful())
        self.assertGreater(result.testsRun, 1)
        self.assertEqual(len(open_calls), 1)


class TestSetUpClassFailureSemantics(unittest.TestCase):
    """Regression guard documenting a trade-off of the setUp -> setUpClass
    refactor: a failure in class-level setup is reported once for the whole
    class rather than once per test method, unlike a failure in setUp().
    """

    def test_setupclass_error_is_reported_once_for_whole_class(self):
        class Dummy(unittest.TestCase):
            @classmethod
            def setUpClass(cls):
                raise IOError("simulated missing fixture file")

            def test_one(self):
                pass

            def test_two(self):
                pass

            def test_three(self):
                pass

        suite = unittest.TestLoader().loadTestsFromTestCase(Dummy)
        result = unittest.TestResult()
        suite.run(result)

        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(result.testsRun, 0)


if __name__ == "__main__":
    unittest.main()