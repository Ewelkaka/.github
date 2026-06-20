## 2025-05-14 - Redundant File I/O in Test Suite
**Learning:** Refactoring static file reading from `setUp` to `@classmethod setUpClass` significantly reduces the number of `openat` system calls during test execution.
**Action:** Always check if files being read in `setUp` are modified by tests; if not, move them to `setUpClass`.
