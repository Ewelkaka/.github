# Bolt Journal

## 2024-05-24 - Optimize test suite file I/O
**Learning:** Using `setUp` in tests that read static files causes redundant disk I/O, which scales with the number of tests. For a test suite reading Markdown files, this resulted in 19 openat calls.
**Action:** Use `@classmethod setUpClass` to read static files once per test class to reduce I/O overhead. This reduced openat calls from 19 to 3.
