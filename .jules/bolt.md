## 2025-05-15 - Redundant File I/O in Python Tests
**Learning:** Python's `unittest.TestCase.setUp` runs before *every* test method, which can lead to excessive `openat` system calls if tests read static files. Using `@classmethod setUpClass` ensures the file is read only once per class.
**Action:** Use `setUpClass` for expensive or redundant I/O operations that provide read-only data to multiple tests within the same class.
