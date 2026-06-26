# Bolt Journal
## 2025-05-15 - Optimizing File I/O in Test Suites
**Learning:** In document-heavy repositories where tests primarily verify static file content, reading the same file in every test method's `setUp` creates unnecessary system call overhead.
**Action:** Use `@classmethod setUpClass` to read file contents once per test class instead of once per test instance.
