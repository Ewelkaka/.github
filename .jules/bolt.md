## 2025-05-15 - Optimizing Test Suite I/O with setUpClass
**Learning:** In Python's `unittest` framework, using `setUp()` triggers for every single test method, leading to redundant I/O (e.g., re-reading the same Markdown files). Switching to `@classmethod setUpClass()` allows expensive setup like file reading to happen once per test class, significantly reducing system calls.
**Action:** Always prefer `setUpClass()` for reading static test data or performing expensive initialization that is shared across all tests in a class.
