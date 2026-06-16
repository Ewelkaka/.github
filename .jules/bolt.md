## 2025-05-14 - Reducing redundant file I/O in Python test suites
**Learning:** In Python's `unittest` framework, using `setUp` to read static test files causes the file to be re-read for every single test method. For large test suites or slow file systems, this adds significant overhead.
**Action:** Use `@classmethod setUpClass` to read static files once per test class and store them as class attributes. This preserves the data for all tests while drastically reducing system calls (e.g., `openat()`).
