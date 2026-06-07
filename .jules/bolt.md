## 2026-06-07 - Reduction of redundant file I/O in test suite
**Learning:** Python's `unittest` framework executes `setUp` before every single test method. In documentation-heavy test suites that perform regex checks on file content, this leads to $N$ `openat` calls for $N$ test cases. Using `@classmethod setUpClass` to read static documentation once per class drastically reduces system calls.
**Action:** Always prefer `@classmethod setUpClass` for reading static files or performing expensive setup that remains constant across all tests in a class.
