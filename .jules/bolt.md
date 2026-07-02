# Bolt's Journal - Critical Learnings Only

## 2024-05-24 - Test Suite I/O Optimization
**Learning:** In Python `unittest`, using `setUp()` for file operations causes the file to be re-opened for every single test method in the class. For a documentation-heavy test suite, this results in significant redundant system calls.
**Action:** Use `@classmethod setUpClass(cls)` to read static test data once per test class. This reduced `openat()` calls from 19 to 3 in the current suite.
