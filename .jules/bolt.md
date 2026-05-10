# Bolt Journal

## 2026-05-10 - Suite-wide impact: Optimized redundant file I/O in test suite
**Learning:** In a document-heavy repository where tests primarily verify static file content, using the `setUp` method in `unittest.TestCase` leads to redundant disk I/O as the file is re-read for every single test case.
**Action:** Use the `@classmethod setUpClass` decorator to read file contents once per class instead of using the instance-level `setUp` method. This reduces system calls and disk I/O, which was verified by reducing `openat` calls from 19 to 3 in this suite.
