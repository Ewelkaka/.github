## 2026-04-10 - Optimizing Python test suite I/O
**Learning:** In Python's `unittest`, using `setUp()` for static file reading causes redundant I/O operations for every test method. Moving this to `@classmethod setUpClass()` ensures the file is read only once per test class.
**Action:** Always check if file reading in `setUp()` can be moved to `setUpClass()` for static resources in Python test suites.
