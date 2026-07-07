# Bolt's Journal - Critical Learnings Only

## 2024-05-24 - Test Suite File I/O Optimization
**Learning:** In Python `unittest`, using `setUpClass` instead of `setUp` for reading static test data (like Markdown files) significantly reduces redundant syscalls.
**Action:** Always prefer `setUpClass` for shared, immutable test fixtures to keep the test suite lightning fast as it scales.
