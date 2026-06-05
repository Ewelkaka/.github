## 2024-06-05 - Reducing redundant file I/O in Python test suite
**Learning:** Python's `unittest` framework calls `setUp` before every individual test method. For tests that only read static files, this leads to redundant `openat` calls (O(n) where n is the number of tests). Using `@classmethod setUpClass` allows reading the file once per class (O(m) where m is the number of test classes), significantly reducing file system overhead.
**Action:** Always prefer `@classmethod setUpClass` over `setUp` for initializing static test data that doesn't change between test runs.
