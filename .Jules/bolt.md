# Bolt's Journal - Performance Critical Learnings

## 2026-05-24 - Optimization of Python Test Suites
**Learning:** Static file I/O in `setUp` methods and redundant regex compilation in test methods can be a performance bottleneck in Python test suites.
**Action:** Use `@classmethod setUpClass` to read static files once per test class and pre-compile regular expressions at the module level or in `setUpClass`.
