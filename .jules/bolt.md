# Bolt Journal

## 2026-05-29 - Reduce redundant file I/O in test suite
**Learning:** In documentation-heavy repositories where tests primarily verify static file content, reading the same file for every test method significantly increases redundant system calls (openat) and disk I/O.
**Action:** Use the `@classmethod setUpClass` decorator in `unittest.TestCase` to read file contents once per class instead of using the instance-level `setUp` method.
