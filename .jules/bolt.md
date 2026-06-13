## 2025-05-14 - [Optimize Test Suite I/O]
**Learning:** Redundant file I/O in Python test suites (using 'setUp' to read static files for every test method) significantly increases system calls like 'openat', especially as the number of tests grows.
**Action:** Use '@classmethod setUpClass' to read static documentation files once per test class and store them as class attributes, drastically reducing redundant disk access.
