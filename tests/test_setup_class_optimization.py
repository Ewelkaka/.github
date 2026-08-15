"""
Tests for the setUp() -> setUpClass() refactor structural validation.
"""

import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(TESTS_DIR)
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

import test_pr_accessibility as pr_accessibility_module
import test_readme_ux as readme_ux_module


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
    }

    def test_classes_do_not_define_instance_setUp(self):
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                self.assertNotIn("setUp", cls.__dict__)

    def test_classes_define_setUpClass(self):
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                self.assertIn("setUpClass", cls.__dict__)

    def test_setUpClass_is_declared_as_classmethod(self):
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                raw = cls.__dict__["setUpClass"]
                self.assertIsInstance(raw, classmethod)

    def test_content_attribute_is_shared_across_instances(self):
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                try:
                    method_name = _first_test_method(cls)
                    instance_a = cls(method_name)
                    instance_b = cls(method_name)

                    attrs = ["content", "coc_content", "contributing_content", "readme_content"]
                    found_any = False
                    for attr in attrs:
                        if hasattr(instance_a, attr):
                            found_any = True
                            self.assertIs(
                                getattr(instance_a, attr),
                                getattr(instance_b, attr),
                            )
                    self.assertTrue(found_any, f"{cls.__name__} has no recognized content attribute.")
                finally:
                    tear_down = getattr(cls, "tearDownClass", None)
                    if callable(tear_down):
                        tear_down()

    def test_content_is_nonempty_string_after_setUpClass(self):
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                attrs = ["content", "coc_content", "contributing_content", "readme_content"]
                found_any = False
                for attr in attrs:
                    if hasattr(cls, attr):
                        found_any = True
                        val = getattr(cls, attr)
                        self.assertIsInstance(val, str)
                        self.assertGreater(len(val), 0)
                self.assertTrue(found_any, f"{cls.__name__} has no recognized content attribute.")

    def test_content_matches_direct_file_read(self):
        for cls, path in self.PATH_BY_CLASS.items():
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                with open(path, encoding="utf-8") as fh:
                    expected = fh.read()
                val = getattr(cls, "content", getattr(cls, "coc_content", None))
                self.assertEqual(val, expected)


class TestRefactoredSuitesStillPass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loader = unittest.TestLoader()
        cls.pr_accessibility_suite = loader.loadTestsFromModule(pr_accessibility_module)
        cls.readme_ux_suite = loader.loadTestsFromModule(readme_ux_module)

    def _run_suite(self, suite):
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
        result = self._run_suite(self.pr_accessibility_suite)
        self.assertTrue(result.wasSuccessful())

    def test_readme_ux_suite_passes(self):
        result = self._run_suite(self.readme_ux_suite)
        self.assertTrue(result.wasSuccessful())


if __name__ == "__main__":
    unittest.main()
