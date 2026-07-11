# Bolt's Journal - Critical Learnings Only

## 2024-05-24 - Optimizing Test Suite I/O with setUpClass
**Learning:** In Python `unittest`, using `setUp()` for file I/O causes the file to be re-opened and read for every single test method in a class. For documentation-heavy test suites, this leads to O(N_tests) system calls.
**Action:** Use `@classmethod setUpClass(cls)` to read static data once per test class, reducing system calls to O(1) per class and significantly improving efficiency for large test suites.
