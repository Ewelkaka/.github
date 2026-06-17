# Bolt Journal

## 2026-05-21 - Optimized test suite file I/O using setUpClass
**Learning:** In a document-heavy repository where tests primarily verify static file content, using the instance-level `setUp` method causes redundant disk I/O as the same file is read for every single test case.
**Action:** Use `@classmethod setUpClass` to read static file contents once per test class. This significantly reduces `openat` calls and improves test suite efficiency, especially as the number of tests grows.
