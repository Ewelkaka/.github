## 2026-06-27 - Reducing redundant file I/O in test suite
**Learning:** The Python `unittest` suite was reading the same static documentation files (README.md, palette.md) in the `setUp` method of multiple test classes, leading to 19 `openat()` calls for just 3 files.
**Action:** Use `@classmethod setUpClass(cls)` to read static test data once per class instead of once per test method, significantly reducing system calls during test execution.
