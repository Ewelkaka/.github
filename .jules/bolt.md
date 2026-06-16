## 2026-04-10 - Optimizing Test Suite File I/O
**Learning:** Using `@classmethod setUpClass` in Python unittest significantly reduces redundant file I/O when multiple tests in a class require the same file content. `strace` is a powerful tool to verify these improvements at the system call level.
**Action:** Always prefer `setUpClass` for expensive or repeated read-only operations in test suites to minimize execution overhead.
