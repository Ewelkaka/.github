# Bolt's Journal - Critical Learnings Only

## 2026-04-10 - Redundant File I/O in Test Suite
**Learning:** Python's `unittest.TestCase.setUp` runs before every test method, leading to redundant file I/O when tests only perform read-only assertions on static fixtures. For a suite with 19 tests, this resulted in 19 `openat` calls for the same set of files.
**Action:** Use `@classmethod setUpClass` to read and cache file contents once per test class, significantly reducing system calls and improving test execution efficiency.
