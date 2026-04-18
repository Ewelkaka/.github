## 2026-04-10 - Optimizing Test Suite File I/O
**Learning:** Python's `unittest` framework runs `setUp` before every test method, which can lead to redundant I/O if the test data is static. Using `@classmethod setUpClass` allows for one-time setup and caching of data at the class level.
**Action:** Always check if `setUp` can be replaced with `setUpClass` for static resources in Python tests to reduce system calls.
