# Bolt's Journal - Critical Learnings Only

## 2025-05-24 - Efficient Test Data Loading with setUpClass
**Learning:** In Python's `unittest`, using `setUp()` to read static files for every test method creates O(N) I/O overhead. In this repository, 19 tests were performing 19 separate `openat` calls for just 3 Markdown files.
**Action:** Use `@classmethod setUpClass(cls)` to load read-only test data once per class, reducing I/O from O(N_tests) to O(1) per file. Measured a reduction from 19 to 3 `openat` calls across the suite.
