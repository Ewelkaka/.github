## 2025-05-04 - Optimize Test Suite File I/O
**Learning:** Redundant file reading in test `setUp` methods can significantly increase system calls when the test suite grows. Using `@classmethod setUpClass` to cache static file content at the class level reduces I/O overhead.
**Action:** Always prefer `setUpClass` over `setUp` for reading static resource files in Python `unittest` suites to ensure the test suite remains fast and efficient. Suite-wide impact: 19 openat calls reduced to 3.
