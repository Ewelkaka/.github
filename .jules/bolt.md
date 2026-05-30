# Bolt Journal
## 2026-05-30 - Optimized test suite file I/O
**Learning:** The test suite was performing redundant file reads in every test method via `setUp`, leading to excessive system calls.
**Action:** Use `@classmethod setUpClass` to read static documentation files once per test class instead of once per test method, significantly reducing `openat` calls across the suite.
