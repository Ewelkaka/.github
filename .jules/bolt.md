## 2026-04-10 - Optimized File I/O in Python Tests
**Learning:** In Python's `unittest`, using `setUp` for static file reading causes redundant I/O operations for every test method. Refactoring to `@classmethod setUpClass` ensures the file is read once per test case class, significantly reducing file system calls.
**Action:** Always prefer `setUpClass` for reading immutable test data or configuration files in Python test suites.
