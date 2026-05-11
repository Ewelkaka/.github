# Bolt Journal

## 2024-05-24 - Optimization of Redundant File I/O in Test Suite
**Learning:** In document-heavy repositories, tests often verify static file content. Using the `@classmethod setUpClass` decorator in `unittest.TestCase` allows reading file contents once per class instead of once per test method.
**Action:** Always prefer `setUpClass` for immutable setup data (like static files) to reduce redundant system calls and disk I/O, especially in larger test suites.
