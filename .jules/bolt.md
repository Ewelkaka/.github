# Bolt's Journal - Critical Learnings Only

## 2026-07-03 - Optimize test suite I/O with setUpClass
**Learning:** In Python `unittest`, using `setUp` to read static data files for every test method causes redundant disk I/O proportional to the number of tests. Refactoring to `@classmethod setUpClass` reduces I/O to a constant O(1) per test class, which is a significant efficiency gain as the test suite grows.
**Action:** Use `setUpClass` for expensive, read-only setup operations that can be shared across all tests in a class. Always ensure `__pycache__` and `*.pyc` are in `.gitignore` to maintain repository hygiene.
