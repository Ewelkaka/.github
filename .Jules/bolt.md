## 2024-03-27 - Test Suite I/O and Regex Optimization
**Learning:** Even in small test suites, repeated file I/O and regex compilation can add up. Using `setUpClass` and `re.compile` are simple ways to ensure efficiency as the suite grows. Pre-calculating results like list of tags in `setUpClass` further reduces redundant work.
**Action:** Always prefer `setUpClass` for immutable test data, pre-compile regexes, and pre-calculate search results used by multiple tests.
