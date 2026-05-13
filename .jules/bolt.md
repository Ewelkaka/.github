# Bolt Journal

## 2025-01-24 - Reducing test suite file I/O with setUpClass
**Learning:** In document-heavy test suites where multiple tests assert against the same file content, using `setUp` causes redundant file I/O. Refactoring to `@classmethod setUpClass` allows reading the file once per test class, significantly reducing system calls (e.g., from 19 to 3 in this case).
**Action:** Prefer `@classmethod setUpClass` over `setUp` when test methods within a class share the same static data (like file contents) to minimize disk I/O and improve suite performance.
