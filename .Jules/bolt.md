# Bolt's Journal

## 2026-04-03 - Optimizing test suite performance
**Learning:** Using `setUp` in Python's `unittest` causes file I/O to occur before every single test method. For read-only tests, `setUpClass` can be used to read files once per class, significantly reducing I/O overhead. Additionally, pre-compiling regular expressions at the module level avoids redundant compilation during test execution.
**Action:** Always prefer `setUpClass` for static file reading in test suites and pre-compile `re` patterns when they are used across multiple tests.
