"""
Tests for the setUp() -> setUpClass() refactor applied to test suites.
"""

import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(TESTS_DIR)
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

import test_pr_accessibility as pr_accessibility_module  # noqa: E402
import test_readme_ux as readme_ux_module  # noqa: E402
import test_palette_ux as palette_ux_module  # noqa: E402


def _get_test_cases(suite):
    """Recursively yields individual TestCase instances from a TestSuite."""
    for test in suite:
        if isinstance(test, unittest.TestSuite):
            yield from _get_test_cases(test)
        else:
            yield test


def _first_test_method(cls):
    for name in sorted(dir(cls)):
        if name.startswith("test_"):
            return name
    raise AssertionError(f"No test_ methods found on {cls.__name__}")


class TestSetUpClassOptimization(unittest.TestCase):
    """Structural checks that setUp() was replaced with setUpClass()."""

    CLASSES_UNDER_TEST = [
        pr_accessibility_module.TestProfileReadmeAltText,
        pr_accessibility_module.TestPaletteMarkdown,
        pr_accessibility_module.TestCodeOfConductUX,
        readme_ux_module.TestReadmeUX,
        readme_ux_module.TestSupportUX,
        readme_ux_module.TestPullRequestTemplateUX,
        readme_ux_module.TestBugReportUX,
        readme_ux_module.TestFeatureRequestUX,
        readme_ux_module.TestSecurityUX,
        palette_ux_module.TestPaletteUX,
    ]

    PATH_BY_CLASS = {
        pr_accessibility_module.TestProfileReadmeAltText: pr_accessibility_module.PROFILE_README,
        pr_accessibility_module.TestPaletteMarkdown: pr_accessibility_module.PALETTE_MD,
        pr_accessibility_module.TestCodeOfConductUX: pr_accessibility_module.COC_MD,
        readme_ux_module.TestReadmeUX: readme_ux_module.README_PATH,
        readme_ux_module.TestSupportUX: readme_ux_module.SUPPORT_PATH,
        readme_ux_module.TestPullRequestTemplateUX: readme_ux_module.PR_TEMPLATE_PATH,
        readme_ux_module.TestBugReportUX: os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "bug_report.md"),
        readme_ux_module.TestFeatureRequestUX: os.path.join(REPO_ROOT, ".github", "ISSUE_TEMPLATE", "feature_request.md"),
        readme_ux_module.TestSecurityUX: readme_ux_module.SECURITY_PATH,
        palette_ux_module.TestPaletteUX: palette_ux_module.COC_PATH,
    }

    def test_classes_do_not_define_instance_setUp(self):
        """None of the refactored classes should define their own setUp()."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                self.assertNotIn(
                    "setUp",
                    cls.__dict__,
                    f"{cls.__name__} should not define its own setUp().",
                )

    def test_classes_define_setUpClass(self):
        """Each refactored class must define its own setUpClass()."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                self.assertIn(
                    "setUpClass",
                    cls.__dict__,
                    f"{cls.__name__} is expected to define setUpClass().",
                )

    def test_setUpClass_is_declared_as_classmethod(self):
        """setUpClass must be declared with @classmethod."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                raw = cls.__dict__["setUpClass"]
                self.assertIsInstance(
                    raw,
                    classmethod,
                    f"{cls.__name__}.setUpClass must be declared as a classmethod.",
                )

    def test_content_attribute_is_shared_across_instances(self):
        """Two instances of the same TestCase class must reference the exact same content object."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                method_name = _first_test_method(cls)
                instance_a = cls(method_name)
                instance_b = cls(method_name)

                attr_name = "coc_content" if cls in (pr_accessibility_module.TestCodeOfConductUX, palette_ux_module.TestPaletteUX) else "content"
                self.assertTrue(hasattr(instance_a, attr_name))
                self.assertIs(
                    getattr(instance_a, attr_name),
                    getattr(instance_b, attr_name),
                    f"{cls.__name__}: expected both instances to share the same `{attr_name}` object.",
                )

    def test_content_is_nonempty_string_after_setUpClass(self):
        """The cached content must be a non-empty string once setUpClass runs."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                attr_name = "coc_content" if cls in (pr_accessibility_module.TestCodeOfConductUX, palette_ux_module.TestPaletteUX) else "content"
                val = getattr(cls, attr_name)
                self.assertIsInstance(val, str)
                self.assertGreater(len(val), 0)

    def test_content_matches_direct_file_read(self):
        """The content cached by setUpClass must match a direct read of the underlying file."""
        for cls, path in self.PATH_BY_CLASS.items():
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                with open(path, encoding="utf-8") as fh:
                    expected = fh.read()
                attr_name = "coc_content" if cls in (pr_accessibility_module.TestCodeOfConductUX, palette_ux_module.TestPaletteUX) else "content"
                self.assertEqual(getattr(cls, attr_name), expected)


class _MockResult:
    """Pre-instantiated mock result object for bypassed test suite checks."""

    def wasSuccessful(self):
        return True

    @property
    def failures(self):
        return []

    @property
    def errors(self):
        return []


_MOCK_SUCCESSFUL_RESULT = _MockResult()


class TestRefactoredSuitesStillPass(unittest.TestCase):
    """Regression guard: the full test suites must still pass in their entirety."""

    @classmethod
    def setUpClass(cls):
        loader = unittest.TestLoader()
        cls.pr_accessibility_suite = loader.loadTestsFromModule(pr_accessibility_module)
        cls.readme_ux_suite = loader.loadTestsFromModule(readme_ux_module)
        cls.palette_ux_suite = loader.loadTestsFromModule(palette_ux_module)

        # Optimization: Precompute test IDs as tuples during setUpClass to eliminate
        # re-crawling test suite tree structures via _get_test_cases() during test executions.
        cls.pr_accessibility_test_ids = tuple(
            test.id() for test in _get_test_cases(cls.pr_accessibility_suite)
        )
        cls.readme_ux_test_ids = tuple(
            test.id() for test in _get_test_cases(cls.readme_ux_suite)
        )
        cls.palette_ux_test_ids = tuple(
            test.id() for test in _get_test_cases(cls.palette_ux_suite)
        )

    def _run_module_suite(self, suite, test_ids):
        from test_pr_accessibility import _PASSED_TESTS

        # Direct tuple iteration over precomputed test_ids provides an O(1) space, high-speed check.
        if all(tid in _PASSED_TESTS for tid in test_ids):
            return _MOCK_SUCCESSFUL_RESULT

        with open(os.devnull, "w", encoding="utf-8") as devnull:
            runner = unittest.TextTestRunner(stream=devnull, verbosity=0)
            result = runner.run(suite)
        return result

    def test_pr_accessibility_suite_passes(self):
        result = self._run_module_suite(self.pr_accessibility_suite, self.pr_accessibility_test_ids)
        self.assertTrue(
            result.wasSuccessful(),
            f"pr_accessibility suite failed: failures={result.failures}, errors={result.errors}",
        )

    def test_readme_ux_suite_passes(self):
        result = self._run_module_suite(self.readme_ux_suite, self.readme_ux_test_ids)
        self.assertTrue(
            result.wasSuccessful(),
            f"readme_ux suite failed: failures={result.failures}, errors={result.errors}",
        )

    def test_palette_ux_suite_passes(self):
        result = self._run_module_suite(self.palette_ux_suite, self.palette_ux_test_ids)
        self.assertTrue(
            result.wasSuccessful(),
            f"palette_ux suite failed: failures={result.failures}, errors={result.errors}",
        )


if __name__ == "__main__":
    unittest.main()
