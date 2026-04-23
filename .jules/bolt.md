## 2026-04-10 - Optimized test suite I/O by using setUpClass
**Learning:** Python's `unittest.TestCase.setUp()` runs before *every* test method, which can lead to redundant and expensive I/O operations if the tests only need to read static files. Using `@classmethod setUpClass(cls)` allows reading the file once per test class and sharing the content across all test methods.
**Action:** Always prefer `@classmethod setUpClass(cls)` for one-time setup of static resources (like reading README or configuration files) in test suites to minimize file system overhead.
