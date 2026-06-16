## 2025-01-24 - Efficient static file reading in tests
**Learning:** Using `setUp` to read static files in unit tests leads to redundant I/O operations proportional to the number of test methods. For immutable files, `@classmethod setUpClass` can reduce file system calls significantly (e.g., from 19 to 3 in this suite).
**Action:** Always prefer `@classmethod setUpClass` for loading static resources or initializing expensive, immutable state in test suites to minimize I/O overhead.
