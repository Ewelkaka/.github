## 2026-04-10 - Optimizing Test Suite File I/O
**Learning:** In Python's `unittest`, using `setUp` to read static files for every test method creates unnecessary file I/O overhead. For a suite with many tests, this significantly increases the number of `openat` system calls.
**Action:** Use `@classmethod setUpClass(cls)` to read static resources once per class. Store the data in `cls.attr` which is accessible via `self.attr` in test methods, preserving compatibility without increasing I/O.
