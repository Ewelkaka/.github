## 2026-04-03 - Redundant I/O in Test Suites
**Learning:** In Python unittest, using `setUp()` to read static files results in redundant disk I/O for every test case. For a suite with 19 tests, this leads to 19 file opens.
**Action:** Use `@classmethod setUpClass` to read and cache static file content once per test class, significantly reducing I/O operations. Pre-compiling regular expressions at the module level also avoids redundant parsing during test execution.
