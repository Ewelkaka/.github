## 2026-04-10 - Optimizing Test Suite I/O with setUpClass
**Learning:** Redundant file I/O in test suites can significantly increase the number of system calls, especially when using `setUp()` for multiple tests within a class. Switching to `@classmethod setUpClass()` allows for reading static test data once per class, reducing the I/O overhead.
**Action:** Use `setUpClass` for expensive or redundant setup operations in Python tests, such as reading files that are shared across all test methods in a class.
