## 2026-04-30 - Optimization of Test Suite File I/O
**Learning:** Redundant file I/O in test `setUp` methods can significantly increase the number of system calls. Using `@classmethod setUpClass` allows for reading static resources once per test class.
**Action:** Always check for repeated file reads in test suites and use `@classmethod setUpClass` to cache static content for all tests in a class.
