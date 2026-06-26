## 2026-03-29 - Optimize Python test suite I/O and regex compilation
**Learning:** Python's `unittest.TestCase.setUp` runs before every single test method, which can lead to redundant I/O operations if the same file is read multiple times. Additionally, compiling regular expressions inside test methods adds overhead.
**Action:** Use `@classmethod setUpClass` to perform expensive setup (like file I/O) once per test class and pre-compile regular expressions at the module level using `re.compile()` to improve test suite performance.
