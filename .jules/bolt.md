## 2026-04-10 - Reduce redundant file I/O in test suite
**Learning:** Python's `unittest.TestCase.setUp` runs before every test method, leading to redundant file I/O when multiple tests check the same file. In this codebase, it resulted in 19 `openat` calls for just 3 Markdown files.
**Action:** Use `@classmethod setUpClass(cls)` to read static files once per test class, significantly reducing system calls and improving test execution speed.
