## 2026-04-09 - Optimize test suite I/O and regex compilation
**Learning:** The test suite was reading static files (README.md, .Jules/palette.md) in the 'setUp' method of multiple test classes, leading to redundant file I/O (19 'openat' calls for 19 tests). Additionally, regular expressions were being re-compiled in every test method.
**Action:** Use '@classmethod setUpClass' to perform file I/O once per class and pre-compile regular expressions at the module level to improve test execution efficiency.
