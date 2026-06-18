## 2026-06-18 - [Reduce Redundant File I/O in Python Tests]
**Learning:** Re-reading static files in the `setUp` method of a `unittest.TestCase` causes redundant `openat` system calls proportional to the number of test methods. Moving file I/O to `@classmethod setUpClass` ensures the file is read only once per test class.
**Action:** Always prefer `@classmethod setUpClass` for reading static test data or configuration files that do not change between test runs to improve I/O efficiency.
