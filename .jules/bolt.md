# Bolt Journal

## 2024-05-24 - Efficient Test Resource Loading
**Learning:** In a document-heavy repository where tests primarily verify static file content, use the `@classmethod setUpClass` decorator in `unittest.TestCase` to read file contents once per class instead of using the instance-level `setUp` method. This significantly reduces redundant system calls and disk I/O, especially as the number of test methods in a class grows.
**Action:** Always check if test resources can be loaded once per class or suite rather than per test to minimize overhead.
