# Bolt's Journal - Critical Learnings Only

## 2026-07-05 - Reduced redundant file I/O in test suite
**Learning:** Python's `unittest.TestCase` re-instantiates the class for every test method. If file reading is done in `setUp()`, it results in O(N_tests) `openat()` calls, which is inefficient for large test suites or slow file systems.
**Action:** Use `@classmethod setUpClass(cls)` to read and cache static file content once per test class, reducing file I/O to O(1) per class.
