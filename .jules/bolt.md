# Bolt's Journal - Critical Learnings Only

## 2026-07-06 - Optimized test suite file I/O
**Learning:** The test suite was redundant, reading Markdown files for every test method. Using `@classmethod setUpClass(cls)` allows caching file contents at the class level, reducing redundant `openat()` calls.
**Action:** When working with Python `unittest` for static file assertions, always use `setUpClass` to read static data once per class.
