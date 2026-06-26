## 2026-06-26 - Excessive file I/O in Python test suite
**Learning:** Using `setUp` to read static test data (like Markdown files) causes a redundant `openat()` syscall for every single test method. For large test suites, this significantly increases overhead.
**Action:** Refactor static file reading into `@classmethod setUpClass` to load data once per test class, ensuring it's inherited by all test instances and reducing total file I/O operations.
