## 2025-01-24 - Reducing redundant file I/O in test suite
**Learning:** Python's `unittest.TestCase.setUp` runs before every single test method. When tests read static files (like READMEs or metadata) for assertion, this leads to O(n) file I/O operations where n is the number of test methods. Using `@classmethod setUpClass` reduces this to O(1) per test class.
**Action:** Always prefer `setUpClass` for expensive or static resource initialization in test suites to minimize system calls and improve execution speed.
