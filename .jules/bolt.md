# Bolt Journal

## 2024-05-24 - Redundant file I/O in test suite
**Learning:** The test suite was reading markdown files from disk in the `setUp` method of every test class, leading to 19 `openat` calls (one per test case) for a small set of files. This is a common performance bottleneck in I/O-heavy test suites.
**Action:** Use `@classmethod setUpClass` to read the files only once per test class. This reduced the number of `openat` calls for target markdown files from 19 down to 3, achieving a significant reduction in redundant I/O operations while preserving test functionality.
