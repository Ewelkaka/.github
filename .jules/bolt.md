## 2026-04-10 - Optimized test suite file I/O
**Learning:** Python's `unittest.TestCase.setUp` runs before every single test method, which can lead to redundant file I/O if multiple tests read the same static assets. In this repository, 19 tests were performing 19 `openat` calls for the same three Markdown files.
**Action:** Use `@classmethod setUpClass(cls)` to perform one-time expensive setup (like reading static files) for all tests in a class. This reduced file I/O operations by ~84% (from 19 to 3 `openat` calls) without sacrificing readability.
