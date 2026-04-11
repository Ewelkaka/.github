## 2026-04-10 - Optimizing Test Suite File I/O
**Learning:** Python's `unittest` calls `setUp` before every single test case. When tests involve reading static files (like READMEs or profile documentation), this leads to redundant I/O operations proportional to the number of test cases. Using `setUpClass` and pre-compiling regular expressions significantly reduces system calls and execution time for content-heavy test suites.
**Action:** Always prefer `setUpClass` over `setUp` for static file I/O and pre-compile `re` patterns at the module level when they are reused across multiple tests.
