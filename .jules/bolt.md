## 2025-05-15 - Redundant openat() calls in test suite
**Learning:** The Python test suite was performing redundant file I/O by reading the same documentation files in the `setUp` method of multiple test classes, leading to 19 `openat` calls for just 3 files.
**Action:** Refactor test classes to use `@classmethod setUpClass` to read static documentation files once per class, significantly reducing system calls and improving test execution efficiency.
