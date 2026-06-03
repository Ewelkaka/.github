# Bolt Journal

## 2024-06-03 - Redundant File I/O in Test Suite
**Learning:** Using `setUp` to read static test data from disk causes redundant `openat` calls for every test method, which scales poorly as the test suite grows.
**Action:** Use `@classmethod setUpClass` to read static fixtures once per test class.
