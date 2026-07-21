# Bolt's Journal - Critical Learnings Only

## 2026-07-15 - Reduce redundant file I/O in test suites
**Learning:** In Python `unittest`, using `setUp()` to read static data files causes a read operation before every single test method. For large test suites or slow filesystems, this adds significant overhead. Refactoring to `@classmethod setUpClass(cls)` allows reading the file once per class and sharing the content across all test methods.
**Action:** Always prefer `setUpClass` for reading static, read-only test data to minimize system calls and improve test execution speed.

## 2026-07-16 - Expand setUpClass I/O caching to multi-file assertions
**Learning:** When a single test class asserts against multiple distinct static files (such as CODE_OF_CONDUCT.md, README.md, and CONTRIBUTING.md in TestCodeOfConductUX), performing `_read()` calls on-demand inside each test method leads to multiple redundant `openat()` calls. Caching all required static files at class creation time via `@classmethod setUpClass(cls)` completely eliminates redundant system-level disk reads.
**Action:** Identify all test methods performing raw direct file reads within a single class, and hoist all of them into a unified `@classmethod setUpClass(cls)` block.
