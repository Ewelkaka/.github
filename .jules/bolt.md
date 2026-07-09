# Bolt's Journal - Critical Learnings Only

## 2025-05-24 - Test suite I/O bottleneck
**Learning:** In documentation-heavy repositories where tests primarily validate Markdown content, redundant file I/O in `unittest.TestCase.setUp` can scale linearly with the number of tests. Using `@classmethod setUpClass` to read static files once per class significantly reduces system call overhead.
**Action:** Always check for repeated static file reads in test suites and consolidate them using `setUpClass` to minimize `openat()` calls.
