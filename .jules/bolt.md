## 2026-04-10 - Optimizing test performance by reducing redundant file I/O
**Learning:** Python's `unittest` framework runs `setUp` before every test case, leading to redundant file system calls if tests read the same static files. Using `@classmethod setUpClass` ensures the file is read only once per test class.
**Action:** Always prefer `setUpClass` over `setUp` for reading static test data that remains unchanged throughout the test suite.
