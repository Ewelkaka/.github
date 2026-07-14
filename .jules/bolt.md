# Bolt's Journal - Critical Learnings Only

## 2025-01-24 - Test Suite File I/O Anti-pattern
**Learning:** The test suite was re-reading static Markdown files for every test method in `setUp()`, causing O(N) `openat()` calls. Since these files don't change during test execution, this was unnecessary overhead.
**Action:** Use `@classmethod setUpClass(cls)` to cache static file content at the class level in Python `unittest` to reduce I/O to O(1) per class.
