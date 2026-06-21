## 2025-01-24 - Reducing redundant I/O in Python test suites
**Learning:** Using `setUp()` in `unittest.TestCase` causes the setup logic (like reading a file) to run before *every* test method. For static files that don't change during tests, this leads to redundant system calls (like `openat()`).
**Action:** Use `@classmethod setUpClass(cls)` to perform one-time setup for the entire test class. This significantly reduces file I/O when a class has multiple test methods that consume the same static data.
