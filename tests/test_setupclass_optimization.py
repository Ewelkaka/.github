"""
Tests for the setUp -> setUpClass fixture refactor.

This PR changed `tests/test_pr_accessibility.py` (TestProfileReadmeAltText,
TestPaletteMarkdown) and `tests/test_readme_ux.py` (TestReadmeUX) so that the
static markdown fixtures they read are loaded once per class in
`setUpClass` instead of once per test method in `setUp`.

These tests verify that the refactor:
  * Declares `setUpClass` as an actual `@classmethod` (and that the old
    `setUp` method is gone).
  * Reads each source file exactly once per class run, regardless of how
    many test methods exist on that class (the whole point of the change).
  * Still produces the correct file content, shared identically as a class
    attribute across every test instance/method.
  * Surfaces a missing source file as a single class-level setup error
    instead of duplicating the failure once per test method.
"""

import io
import os
import sys
import unittest
from unittest import mock

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

import test_pr_accessibility as pr_accessibility  # noqa: E402
import test_readme_ux as readme_ux  # noqa: E402


def _run_suite(test_case_cls):
    """Run every test on a TestCase class and return the TestResult."""
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case_cls)
    runner = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0)
    return runner.run(suite)


class TestSetUpClassIsProperlyDeclared(unittest.TestCase):
    """The refactored classes must use @classmethod setUpClass, not setUp."""

    REFACTORED_CLASSES = (
        pr_accessibility.TestProfileReadmeAltText,
        pr_accessibility.TestPaletteMarkdown,
        readme_ux.TestReadmeUX,
    )

    def test_setupclass_is_a_classmethod_on_each_refactored_class(self):
        for cls in self.REFACTORED_CLASSES:
            raw = cls.__dict__.get("setUpClass")
            self.assertIsNotNone(
                raw, f"{cls.__name__} does not define setUpClass directly"
            )
            self.assertIsInstance(
                raw,
                classmethod,
                f"{cls.__name__}.setUpClass must be declared with @classmethod",
            )

    def test_setup_instance_method_no_longer_defined(self):
        for cls in self.REFACTORED_CLASSES:
            self.assertNotIn(
                "setUp",
                cls.__dict__,
                f"{cls.__name__} should no longer define an instance-level "
                "setUp() now that setUpClass() replaces it",
            )


class TestFileReadHappensExactlyOncePerClass(unittest.TestCase):
    """The optimization's entire purpose: O(1) reads instead of O(N_tests)."""

    def test_profile_readme_is_read_exactly_once(self):
        real_read = pr_accessibility._read
        with mock.patch.object(
            pr_accessibility, "_read", wraps=real_read
        ) as spy:
            result = _run_suite(pr_accessibility.TestProfileReadmeAltText)

        self.assertTrue(result.wasSuccessful(), result.errors + result.failures)
        self.assertGreater(
            result.testsRun,
            1,
            "expected multiple test methods to actually exercise the class",
        )
        self.assertEqual(
            spy.call_count,
            1,
            "expected exactly one _read() call for the whole class, "
            f"regardless of the {result.testsRun} test methods that ran",
        )

    def test_palette_markdown_is_read_exactly_once(self):
        real_read = pr_accessibility._read
        with mock.patch.object(
            pr_accessibility, "_read", wraps=real_read
        ) as spy:
            result = _run_suite(pr_accessibility.TestPaletteMarkdown)

        self.assertTrue(result.wasSuccessful(), result.errors + result.failures)
        self.assertGreater(result.testsRun, 1)
        self.assertEqual(spy.call_count, 1)

    def test_readme_ux_is_read_exactly_once(self):
        real_open = open
        with mock.patch("builtins.open", wraps=real_open) as spy:
            result = _run_suite(readme_ux.TestReadmeUX)

        self.assertTrue(result.wasSuccessful(), result.errors + result.failures)
        self.assertGreater(result.testsRun, 1)
        self.assertEqual(
            spy.call_count,
            1,
            "expected exactly one open() call for the whole class, "
            f"regardless of the {result.testsRun} test methods that ran",
        )


class TestClassContentIsCorrectAndShared(unittest.TestCase):
    """cls.content must hold the right data and be shared, not per-instance."""

    def test_profile_readme_content_matches_file_on_disk(self):
        pr_accessibility.TestProfileReadmeAltText.setUpClass()
        with open(pr_accessibility.PROFILE_README, encoding="utf-8") as fh:
            expected = fh.read()
        self.assertEqual(
            pr_accessibility.TestProfileReadmeAltText.content, expected
        )

    def test_palette_markdown_content_matches_file_on_disk(self):
        pr_accessibility.TestPaletteMarkdown.setUpClass()
        with open(pr_accessibility.PALETTE_MD, encoding="utf-8") as fh:
            expected = fh.read()
        self.assertEqual(pr_accessibility.TestPaletteMarkdown.content, expected)

    def test_readme_ux_content_matches_file_on_disk(self):
        readme_ux.TestReadmeUX.setUpClass()
        with open(readme_ux.README_PATH, encoding="utf-8") as fh:
            expected = fh.read()
        self.assertEqual(readme_ux.TestReadmeUX.content, expected)

    def test_content_attribute_is_identical_object_across_instances(self):
        cls = pr_accessibility.TestProfileReadmeAltText
        cls.setUpClass()

        instance_a = cls("test_img_tag_present")
        instance_b = cls("test_img_src_unchanged")

        self.assertIs(
            instance_a.content,
            instance_b.content,
            "content should be the same shared object across test "
            "instances, confirming it was read once at the class level "
            "rather than re-read per instance",
        )
        self.assertIs(instance_a.content, cls.content)


class TestMissingSourceFileFailsOnceAtClassLevel(unittest.TestCase):
    """Negative path: a missing file must fail setup once, not per-test.

    This is a direct behavioral consequence of moving the read from
    setUp() (which used to fail independently for every test method) to
    setUpClass() (which now fails a single time for the whole class).
    """

    def test_missing_profile_readme_produces_a_single_class_level_error(self):
        missing_path = os.path.join(
            os.path.dirname(pr_accessibility.PROFILE_README),
            "does-not-exist.md",
        )
        with mock.patch.object(
            pr_accessibility, "PROFILE_README", missing_path
        ):
            result = _run_suite(pr_accessibility.TestProfileReadmeAltText)

        self.assertEqual(
            result.testsRun,
            0,
            "no individual test method should run once setUpClass fails",
        )
        self.assertEqual(len(result.errors), 1)
        self.assertIn("setUpClass", result.errors[0][0].id())

    def test_missing_palette_markdown_produces_a_single_class_level_error(self):
        missing_path = os.path.join(
            os.path.dirname(pr_accessibility.PALETTE_MD), "does-not-exist.md"
        )
        with mock.patch.object(pr_accessibility, "PALETTE_MD", missing_path):
            result = _run_suite(pr_accessibility.TestPaletteMarkdown)

        self.assertEqual(result.testsRun, 0)
        self.assertEqual(len(result.errors), 1)
        self.assertIn("setUpClass", result.errors[0][0].id())

    def test_missing_readme_produces_a_single_class_level_error(self):
        missing_path = os.path.join(
            os.path.dirname(readme_ux.README_PATH), "does-not-exist.md"
        )
        with mock.patch.object(readme_ux, "README_PATH", missing_path):
            result = _run_suite(readme_ux.TestReadmeUX)

        self.assertEqual(result.testsRun, 0)
        self.assertEqual(len(result.errors), 1)
        self.assertIn("setUpClass", result.errors[0][0].id())


if __name__ == "__main__":
    unittest.main()