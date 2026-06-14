## 2024-06-14 - Reducing redundant file I/O in Python test suite
**Learning:** Refactoring static file reading from `setUp` (runs before every test method) to `@classmethod setUpClass` (runs once per test class) significantly reduces redundant `openat` system calls. In this codebase, it reduced file I/O from 19 to 3 `openat` calls for shared documentation files.
**Action:** Always check if files read in `setUp` are modified by tests. If they are read-only for the duration of the test class, use `setUpClass` to cache the content and improve test execution efficiency.
