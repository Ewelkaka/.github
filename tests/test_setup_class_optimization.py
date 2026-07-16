"""
Tests for the setUp() -> setUpClass() refactor applied to:
  - tests/test_pr_accessibility.py (TestProfileReadmeAltText, TestPaletteMarkdown)
  - tests/test_readme_ux.py (TestReadmeUX)

This refactor (see .jules/bolt.md) reads static test-data files once per
class via `setUpClass` instead of once per test method via `setUp`. These
tests verify:
  1. The classes no longer define an instance-level setUp().
  2. setUpClass is declared as a classmethod.
  3. The `content` attribute is class-level and shared identically across
     multiple instances (proving the file is read once, not once per test).
  4. The refactored suites still pass in full, as a regression guard.
"""

import os
import sys
import unittest

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
if TESTS_DIR not in sys.path:
    sys.path.insert(0, TESTS_DIR)

import test_pr_accessibility as pr_accessibility_module  # noqa: E402
import test_readme_ux as readme_ux_module  # noqa: E402


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
        readme_ux_module.TestReadmeUX,
    ]

    def test_classes_do_not_define_instance_setUp(self):
        """None of the refactored classes should define their own setUp();
        the one-time file read must happen in setUpClass() instead."""
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
        """setUpClass must be declared with @classmethod so `cls.content`
        is shared at the class level instead of per instance."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                raw = cls.__dict__["setUpClass"]
                self.assertIsInstance(
                    raw,
                    classmethod,
                    f"{cls.__name__}.setUpClass must be declared as a classmethod.",
                )

    def test_content_attribute_is_shared_across_instances(self):
        """Two instances of the same TestCase class must reference the exact
        same `content` object, proving the file is read once and cached on
        the class rather than re-read per instance/method."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                try:
                    method_name = _first_test_method(cls)
                    instance_a = cls(method_name)
                    instance_b = cls(method_name)
                    self.assertTrue(hasattr(instance_a, "content"))
                    self.assertIs(
                        instance_a.content,
                        instance_b.content,
                        f"{cls.__name__}: expected both instances to share the "
                        "identical `content` object set by setUpClass().",
                    )
                finally:
                    tear_down = getattr(cls, "tearDownClass", None)
                    if callable(tear_down):
                        tear_down()

    def test_content_is_nonempty_string_after_setUpClass(self):
        """The cached content must be a non-empty string once setUpClass runs."""
        for cls in self.CLASSES_UNDER_TEST:
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                self.assertIsInstance(cls.content, str)
                self.assertGreater(len(cls.content), 0)

    def test_content_matches_direct_file_read(self):
        """The content cached by setUpClass must match a fresh direct read
        of the underlying source file, proving no data was lost or altered
        by moving the read out of setUp()."""
        path_by_class = {
            pr_accessibility_module.TestProfileReadmeAltText: pr_accessibility_module.PROFILE_README,
            pr_accessibility_module.TestPaletteMarkdown: pr_accessibility_module.PALETTE_MD,
            readme_ux_module.TestReadmeUX: readme_ux_module.README_PATH,
        }
        for cls, path in path_by_class.items():
            with self.subTest(cls=cls.__name__):
                cls.setUpClass()
                with open(path, encoding="utf-8") as fh:
                    expected = fh.read()
                self.assertEqual(cls.content, expected)


class TestRefactoredSuitesStillPass(unittest.TestCase):
    """Regression guard: the full test suites for the refactored modules
    must still pass in their entirety after switching from setUp to
    setUpClass."""

    def _run_module_suite(self, module):
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(module)
        with open(os.devnull, "w", encoding="utf-8") as devnull:
            runner = unittest.TextTestRunner(stream=devnull, verbosity=0)
            result = runner.run(suite)
        return result

    def test_pr_accessibility_suite_passes(self):
        result = self._run_module_suite(pr_accessibility_module)
        self.assertTrue(
            result.wasSuccessful(),
            "tests/test_pr_accessibility.py failed after the setUp -> "
            f"setUpClass refactor: failures={result.failures}, errors={result.errors}",
        )

    def test_readme_ux_suite_passes(self):
        result = self._run_module_suite(readme_ux_module)
        self.assertTrue(
            result.wasSuccessful(),
            "tests/test_readme_ux.py failed after the setUp -> setUpClass "
            f"refactor: failures={result.failures}, errors={result.errors}",
        )


if __name__ == "__main__":
    unittest.main()