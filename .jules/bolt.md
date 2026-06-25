## 2025-05-15 - Reducing redundant file I/O in Python test suites
**Learning:** Using `setUp` in `unittest.TestCase` causes the setup logic to run before every single test method. For tests that read static files, this results in redundant disk I/O. Switching to `@classmethod setUpClass` ensures the file is read only once per test class. In this suite, it reduced `openat()` calls from 19 to 3.
**Action:** Always use `@classmethod setUpClass` when loading static resources or performing expensive setup that can be shared across all tests in a class.
