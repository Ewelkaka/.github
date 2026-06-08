## 2026-06-08 - Optimized test suite file I/O
**Learning:** In Python's 'unittest' framework, reading static assets in 'setUp' causes redundant file I/O operations equal to the number of test methods. Refactoring to '@classmethod setUpClass' reduces this to once per class.
**Action:** Always prefer '@classmethod setUpClass' for reading static files or performing expensive, shared setup in test suites to improve execution efficiency.
