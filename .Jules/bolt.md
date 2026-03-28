# Bolt's Journal - Critical Performance Learnings

## 2024-05-24 - Optimize Python test suites with setUpClass and pre-compiled regex
**Learning:** In Python `unittest`, using `setUp` for file I/O and compiling regex within test methods causes redundant operations across multiple tests. Using `@classmethod setUpClass` ensures expensive I/O happens once per class, and module-level `re.compile` avoids repeated compilation.
**Action:** Always prefer `@classmethod setUpClass` for static file reading and pre-compile regex patterns at the module level in test suites to reduce overhead.
