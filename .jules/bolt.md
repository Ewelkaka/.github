# Bolt Journal

## 2026-05-27 - Redundant File I/O in Test Suite
**Learning:** Using `setUp` to read static documentation files for testing leads to redundant disk I/O (one `openat` call per test method). In this repo, it resulted in 19 calls for just a few files.
**Action:** Use `@classmethod setUpClass` to read static files once per test class. This significantly reduces system calls in document-heavy test suites.
