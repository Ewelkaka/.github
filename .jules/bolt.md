## 2025-05-15 - Redundant I/O in Python Test Suites
**Learning:** Using `setUp()` in `unittest.TestCase` for static file reading causes the file to be re-opened for every single test method in the class, leading to O(N) file I/O where N is the number of tests.
**Action:** Use `@classmethod setUpClass` to read static files once per test class, reducing I/O to O(1) per class and significantly improving efficiency in documentation-heavy test suites.
