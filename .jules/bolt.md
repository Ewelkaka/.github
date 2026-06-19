# Bolt Journal

## 2024-05-24 - Redundant File I/O in Test Suite
**Learning:** Python's `unittest.TestCase.setUp()` runs before *every* test method, leading to redundant system calls (e.g., `openat`) when testing static content. Using `@classmethod setUpClass` allows reading the file once per class, which is significantly more efficient for documentation-heavy test suites.
**Action:** Always prefer `setUpClass` over `setUp` when the data being loaded is immutable across tests within the same class.
