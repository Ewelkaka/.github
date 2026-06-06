# Bolt Journal
## 2024-05-24 - Optimized Redundant File I/O in Tests
**Learning:** Using `setUp` in `unittest.TestCase` causes the setup logic (like reading a file) to run before EVERY test method. For tests that only read static documentation files, this creates significant redundant disk I/O.
**Action:** Use `@classmethod setUpClass` to perform expensive operations like file I/O once per class when the data is static and shared across tests.
