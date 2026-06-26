## 2026-04-10 - Reduce redundant file I/O in test suite
**Learning:** Python's `unittest.TestCase.setUp()` runs before every test method, which can lead to significant redundant file I/O when testing static content. Using `@classmethod setUpClass()` allows reading the file once per class.
**Action:** Always check if file loading in tests can be moved to `setUpClass()` if the content is read-only and shared across multiple tests.
