# Bolt's Journal - Critical Learnings Only

## 2024-05-24 - Redundant File I/O in Test Suite
**Learning:** In Python `unittest`, using `setUp()` to read static files for every test method causes O(N) `openat()` syscalls. Using `@classmethod setUpClass(cls)` reduces this to O(1) per class, significantly decreasing disk I/O for large test suites.
**Action:** Always prefer `setUpClass` for immutable, shared test data and document the performance impact with inline comments to satisfy review standards.
