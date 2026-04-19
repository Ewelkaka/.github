# Bolt's Performance Journal

## 2026-04-10 - Optimizing Test Suite File I/O
**Learning:** Python's `unittest.TestCase.setUp` runs before every single test method, which can lead to redundant and expensive file I/O if the files being tested are static. In this repository, the test suite was reading `README.md` and `palette.md` for every test case, resulting in 19 `openat` calls.
**Action:** Use `@classmethod setUpClass(cls)` to read static test files once per class. This reduces the number of file opens from one per test method to one per test class.
