# Bolt's Journal - Critical Learnings Only

## 2026-02-21 - Test Suite I/O Optimization
**Learning:** Redundant file I/O in test suites can be easily avoided by using `setUpClass` instead of `setUp` when test data is static and used in a read-only manner.
**Action:** Always prefer `@classmethod setUpClass(cls)` for loading static resources or reading files that are shared across all test methods in a class to minimize system calls.
