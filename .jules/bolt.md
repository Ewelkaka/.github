## 2024-06-06 - Optimized test suite I/O performance
**Learning:** In Python's `unittest` framework, reading static files in `setUp()` causes the file to be re-opened for every single test method in the class. Using `@classmethod setUpClass` instead ensures the file is read only once per test class.
**Action:** Always prefer `setUpClass` over `setUp` for static file I/O in test suites to reduce system call overhead and improve execution speed.
