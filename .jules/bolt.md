# Bolt Journal

## 2024-05-25 - Redundant file I/O in test suite
**Learning:** Using `setUp` in Python `unittest.TestCase` causes the setup logic to run for every single test method. In document-heavy repositories where tests verify static file content, this leads to significant redundant disk I/O.
**Action:** Use `@classmethod setUpClass` to perform one-time expensive setup (like reading files) and store results as class attributes (e.g., `cls.content`). This drastically reduces the number of `openat` system calls.
