# Bolt Journal

## 2024-05-24 - Optimization of Redundant File I/O in Tests
**Learning:** In test suites that verify static documentation, reading the same files in `setUp()` for every test case introduces significant, unnecessary disk I/O and system call overhead. Using `@classmethod setUpClass` to read the file once per class reduces `openat` calls by an order of magnitude (from 19 to 3 in this suite).
**Action:** Always prefer `@classmethod setUpClass` for reading immutable test data or files that are shared across all test methods in a class to minimize I/O overhead.
