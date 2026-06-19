## 2026-06-19 - Reduced Redundant File I/O in Python Tests
**Learning:** Python's `unittest` framework runs `setUp` before *every* test method, which can lead to significant redundant file I/O if the test methods are only performing read-only assertions on static files. Moving file reading to `@classmethod setUpClass` ensures the file is read only once per test class.
**Action:** Always prefer `@classmethod setUpClass` for reading static test fixtures or repository files that do not change during the test run to minimize system calls.
