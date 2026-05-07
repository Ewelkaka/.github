## 2026-05-07 - Optimize test suite file I/O
**Learning:** In a document-heavy repository where tests primarily verify file content, using `setUp` to read files causes redundant disk access. Moving file reading to `@classmethod setUpClass` ensures files are read once per test class.
**Action:** Use `setUpClass` for static test resources to minimize system calls and improve test execution efficiency.
