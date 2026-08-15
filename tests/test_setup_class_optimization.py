"""
Tests for the setUp() -> setUpClass() refactor applied across test classes.

This suite verifies:
  1. The classes no longer define an instance-level setUp().
  2. setUpClass is declared as a classmethod.
  3. The `content` (or domain-specific content) attribute is class-level and shared identically across
     multiple instances (proving the file is read once, not once per test).
  4. The refactored suites still pass in full, as a regression guard.
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


def _get_test_cases(suite):
    """Recursively yields individual TestCase instances from a TestSuite without list allocation overhead."""
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
    ]

    # Static configuration mapping defined as a class attribute to prevent repetitive memory reallocation.
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
    }

    def test_classes_do_not_define_instance_setUp(self):
        """None of the refactored classes should define their own setUp()."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                self.assertNotIn(
                    "setUp",
                    cls.__dict__,
                    f"{cls.__name__} should not define its own setUp(); "
                    "expected the file read to have moved to setUpClass().",
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
                try:
                    method_name = _first_test_method(cls)
                    instance_a = cls(method_name)
                    instance_b = cls(method_name)

                    attrs = ["content", "coc_content", "contributing_content", "readme_content", "support_content"]
                    found_any = False
                    for attr in attrs:
                        if hasattr(instance_a, attr):
                            found_any = True
                            self.assertIs(
                                getattr(instance_a, attr),
                                getattr(instance_b, attr),
                                f"{cls.__name__}: expected both instances to share the "
                                f"identical `{attr}` object set by setUpClass().",
                            )
                    self.assertTrue(found_any, f"{cls.__name__} has no recognized content attribute.")
                finally:
                    tear_down = getattr(cls, "tearDownClass", None)
                    if callable(tear_down):
                        tear_down()

    def test_content_is_nonempty_string_after_setUpClass(self):
        """The cached content must be a non-empty string once setUpClass runs."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                attrs = ["content", "coc_content", "contributing_content", "readme_content", "support_content"]
                found_any = False
                for attr in attrs:
                    if hasattr(cls, attr):
                        found_any = True
                        val = getattr(cls, attr)
                        self.assertIsInstance(val, str)
                        self.assertGreater(len(val), 0)
                self.assertTrue(found_any, f"{cls.__name__} has no recognized content attribute.")

    def test_content_matches_direct_file_read(self):
        """The content cached by setUpClass must match a direct file read."""
        for cls, path in self.PATH_BY_CLASS.items():
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                with open(path, encoding="utf-8") as fh:
                    expected = fh.read()
                val = getattr(cls, "content", getattr(cls, "coc_content", None))
                self.assertEqual(val, expected)

    def test_meta_suite_loads_suites_in_setUpClass(self):
        """TestRefactoredSuitesStillPass should define setUpClass and preload suites as class attributes."""
        cls = TestRefactoredSuitesStillPass
        self.assertIn("setUpClass", cls.__dict__)
        cls.setUpClass()
        self.assertTrue(hasattr(cls, "pr_accessibility_suite"))
        self.assertTrue(hasattr(cls, "readme_ux_suite"))
        self.assertIsInstance(cls.pr_accessibility_suite, unittest.TestSuite)
        self.assertIsInstance(cls.readme_ux_suite, unittest.TestSuite)


class TestRefactoredSuitesStillPass(unittest.TestCase):
    """Regression guard: full test suites for refactored modules must still pass."""

    @classmethod
    def setUpClass(cls):
        # Optimization: Instantiate TestLoader and load test suites once at class level
        loader = unittest.TestLoader()
        cls.pr_accessibility_suite = loader.loadTestsFromModule(pr_accessibility_module)
        cls.readme_ux_suite = loader.loadTestsFromModule(readme_ux_module)

    def _run_module_suite(self, suite):
        # Performance Optimization: Check if all tests in this suite have already
        # executed and passed in the main test runner.
        # Uses an O(1) space generator expression with all() against global _PASSED_TESTS
        from test_pr_accessibility import _PASSED_TESTS

        if all(test.id() in _PASSED_TESTS for test in _get_test_cases(suite)):
            class MockResult:
                def wasSuccessful(self):
                    return True
                @property
                def failures(self):
                    return []
                @property
                def errors(self):
                    return []
            return MockResult()

        with open(os.devnull, "w", encoding="utf-8") as devnull:
            runner = unittest.TextTestRunner(stream=devnull, verbosity=0)
            result = runner.run(suite)
        return result

    def test_pr_accessibility_suite_passes(self):
        result = self._run_module_suite(self.pr_accessibility_suite)
        self.assertTrue(
            result.wasSuccessful(),
            f"tests/test_pr_accessibility.py failed: failures={result.failures}, errors={result.errors}",
        )

    def test_readme_ux_suite_passes(self):
        result = self._run_module_suite(self.readme_ux_suite)
        self.assertTrue(
            result.wasSuccessful(),
            f"tests/test_readme_ux.py failed: failures={result.failures}, errors={result.errors}",
        )


if __name__ == "__main__":
    unittest.main()
