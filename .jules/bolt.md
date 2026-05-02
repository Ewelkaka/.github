## 2024-05-24 - Optimized test suite file I/O
**Learning:** In Python's `unittest.TestCase`, using `setUp()` for expensive operations like file I/O causes the operation to repeat for every test method. Transitioning to `@classmethod setUpClass(cls)` allows the resource to be loaded once per class, significantly reducing system calls.
**Action:** Always prefer `setUpClass` for loading static test resources (like Markdown files or configuration) that do not change between individual test cases.
