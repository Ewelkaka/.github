## 2026-04-10 - Reduced Redundant File I/O in Test Suite
**Learning:** Python's `unittest.TestCase.setUp()` runs before every test method, which can lead to significant redundant file I/O if the test methods only perform read-only assertions on static files. Moving file reading to `@classmethod setUpClass()` ensures the file is read only once per test class.
**Action:** Always check if file I/O in `setUp()` can be moved to `setUpClass()` for read-only test suites to minimize system calls and improve performance.
