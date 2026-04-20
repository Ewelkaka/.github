## 2026-04-10 - Optimizing Test Suite File I/O
**Learning:** In the Python unittest framework, using `setUp` for static file reading causes the file to be opened once for every test method in the class. For suites with many tests, this significantly increases the number of `openat` system calls.
**Action:** Use `@classmethod setUpClass` to perform static file reading once per test class, sharing the content across all test methods.
