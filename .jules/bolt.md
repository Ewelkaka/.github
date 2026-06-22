## 2026-05-24 - Redundant File I/O in Test Suite
**Learning:** The Python test suite was performing redundant `openat()` calls by reading static documentation files in `setUp()` (per-test) instead of `@classmethod setUpClass()` (per-class).
**Action:** Use `@classmethod setUpClass()` to load immutable resources once per test class to improve execution efficiency and reduce system call overhead.
