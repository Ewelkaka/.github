## 2026-03-27 - Redundant file I/O and regex compilation in Python test suites
**Learning:** Python's `unittest` calls `setUp` before every individual test method, which can lead to redundant and expensive file I/O if the content being tested is static across the entire class. Additionally, compiling the same regular expressions repeatedly within test methods adds unnecessary CPU overhead.
**Action:** Use `@classmethod setUpClass` to perform one-time file I/O for static test data and pre-compile regular expressions at the module level to improve test suite execution efficiency.
